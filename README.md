# indico-plugin-themes-awesome

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

## Use it

To use the Awesome Theme for an Event, create an Event and save it, then go to the *management area of this event* >
``Customization`` > ``Layout`` > ``Timetable`` > ``Theme`` here you can select the ``Foo Theme`` option, and got to
click on Save button at the **Theme** section botton.

