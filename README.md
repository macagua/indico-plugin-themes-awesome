# indico-plugin-themes-awesome

This repository holds the Indico Plugin Themes used for the Indico deployment

- Awesome Themes, inspired by him [ThiefMaster's Github Gist](https://gist.github.com/ThiefMaster/8d5bc6791d8654b31f0ec3a5960693ad) post.

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

