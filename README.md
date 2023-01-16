# indico-plugin-themes-awesome

A [Indico Software](https://getindico.io/) Plugin for Demonstration how to create a Theme Plugin.


## Screenshots

Following are some screenshots about Awesome Theme:


### Timetable view for Events

![Timetable View for Events](https://raw.githubusercontent.com/macagua/indico-plugin-themes-awesome/main/docs/screenshot_timetable_view_events.png)

**Timetable View for Events**


## What Indico version is supported?

 * [v3.2.2](https://pypi.org/project/indico/3.2.2/).


## What does it do this plugin?

This repository holds the Indico Plugin Themes used for the Indico deployment

- Awesome Theme for Indico Events, inspired by the [ThiefMaster's Github Gist](https://gist.github.com/ThiefMaster/8d5bc6791d8654b31f0ec3a5960693ad) post.


## Installing Indico software

Following the Installation guides for [Production](https://docs.getindico.io/en/stable/installation/production/) environment.


## Installing the Awesome theme plugin

Navigate to your Indico project and clone the theme repository:
```
mkdir ~/src/ ; cd $_
git clone https://github.com/macagua/indico-plugin-themes-awesome.git
```

Open ``indico.conf`` and add the following key-value pair to 'General settings' `PLUGINS = {'themes_awesome'}`:
```
nano ~/etc/indico.conf
```

Enter the virtualenv and pip install the plugin:
```
pip install -e ~/src/indico-plugin-themes-awesome/
```

Test the plugin installation with the following command:

```
indico setup list-plugins
```

The previous command generate a list the available plugins to use into Indico:

```
+Available Plugins--+------------------------------------+
| Name              | Title                              |
+-------------------+------------------------------------+
| themes_awesome    | Awesome Themes                     |
| vc_zoom           | Zoom                               |
+-------------------+------------------------------------+
```

For execute the migrations command for the installed plugin with the following command:

```
indico db --plugin themes_awesome upgrade
```

You can check the Awesome Themes Plugin installation go to ``Administration`` > ``Plugins`` > ``Other``,
then if exists an ``Awesome Themes`` reference, is ok installed it.

![Plugins Administration View](https://raw.githubusercontent.com/macagua/indico-plugin-themes-awesome/main/docs/screenshot_plugins_admin.png)

**Plugins Administration View**


## Build Wheel Package

This Theme Plugin use SASS Styles then you need build the CSS/JS assets compiled and minified.
You need to use a local [development](https://docs.getindico.io/en/stable/installation/development/)
environment to build wheel package and then copy just the wheel package generated to production
in order to install it there.

Create directory and download source codes, executing the following command:

```
mkdir -p ~/dev/indico/plugins
cd ~/dev/indico/
git clone https://github.com/indico/indico.git -b master src
git clone https://github.com/indico/indico-plugins.git -b master plugins/base
git clone https://github.com/macagua/indico-plugin-themes-awesome.git -b main plugins/indico-plugin-themes-awesome
```

Create virtual environment and install Python packages, executing the following command:

```
pyenv install 3.9.16
pyenv local 3.9.16
python -m venv --upgrade-deps venv
source ./venv/bin/activate
(venv) $ pip install -U pip setuptools wheel
(venv) $ cd ./src && pip install -e '.[dev]' && npm ci
```

Add Plugins configurations into ``indico.conf`` file, executing the following command:

```
(venv) echo -e "\n# List of plugins to be loaded on server start.\n#" >> ./src/indico/indico.conf
(venv) echo -e "PLUGINS = {'themes_awesome'}" >> ./src/indico/indico.conf
```

Build the Wheel Package for this theme, executing the following command:

```
(venv) ./src/bin/maintenance/build-wheel.py plugin $PWD/plugins/indico-plugin-themes-awesome/
```

Copying the Wheel Package generated to the Indico Production environment, executing the following command:

```
cp ../dist/indico_plugin_themes_awesome-0.0.1-py3-none-any.whl /path/to/production/env/indico_plugin_themes_awesome-0.0.1-py3-none-any.whl
$ sudo chown indico:www-data /path/to/production/env/indico_plugin_themes_awesome-0.0.1-py3-none-any.whl
$ sudo chmod 750 /path/to/production/env/indico_plugin_themes_awesome-0.0.1-py3-none-any.whl
```

Inside the Indico Production environment, install the Wheel Package, executing the following command:

```
(indico) $ pip install /path/to/production/env/indico_plugin_themes_awesome-0.0.1-py3-none-any.whl
```

## Use it

To use the Awesome Theme for an Event, create an Event and save it, then go to the *management area of this event* >
``Customization`` > ``Layout`` > ``Timetable`` > ``Theme`` here you can select the ``Foo Theme`` option, and got to
click on Save button at the **Theme** section botton.

![Layout Manage for Events View](https://raw.githubusercontent.com/macagua/indico-plugin-themes-awesome/main/docs/screenshot_events_manage_layout.png)

**Layout Manage for Events View**


## About Indico Software

<img src="https://github.com/indico/indico/raw/master/indico/web/static/images/logo_indico.png"
     align="right"
     width="300"
     style="width: 300px; float: right; margin-right: 50px;">

**Indico** is:
 * 🗓 a general-purpose **event management** tool;
 * 🌍 fully **web-based**;
 * 🧩 **feature-rich** but also **extensible** through the use of [plugins](https://docs.getindico.io/en/stable/plugins/);
 * ⚖️ **Open-Source** Software under the MIT License;
 * <img src="https://raw.githubusercontent.com/indico/assets/master/cern_badge.png" width="20"> **made at CERN**, [the place where the web was born](https://home.cern/science/computing/birth-web)!

![A sneak peek of Indico](https://raw.githubusercontent.com/indico/indico/master/sneakpeek.gif)

