# Zenoh plugins · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/plugins

# Source: https://zenoh.io/docs/manual/plugins

# Zenoh plugins
The Zenoh router (zenohdexecutable) supports the loading of plugins at start-up, or at runtime if write permission is configured on its admin space.
A Zenoh plugin is a library that can be loaded by the Zenoh router at start-up. It shares a runtime with it, allowing the plugin to use the regular Zenoh rust APIs with the same peer ID.
Zenoh already provides the following plugins in its default repository:
- theREST plugin: providing the Zenoh REST API
- theStorage Manager plugin: providing management ofstorages
Zenoh relies on the configuration files provided to decide the plugins to be loaded at startup.
If a plugin is added to the configuration during runtime (for example through theadmin space), it will be loaded then.
The configuration has 2 fields that is related to plugins:
- plugins, where you may specify which plugins you require, as well as provide configuration for them.
- plugins_search_dirs, where you may specify a list of directories wherezenohdshould look for the specified plugins.

### Thepluginsconfiguration field
This field may contain a dictionary, where each key is the configured plugin’s name, and the associated value is a dictionary holding its configuration.
In this dictionary, 2 properties are reserved byzenohd:
- __path__may hold a string or list of strings, which are the paths where the plugin is expected to be located. If this option is defined, lookup-by-name is disabled for the requested plugin, and the first path to resolve in a successful load will be used as the plugin’s path.
- __required__may hold a boolean value. If set totrue,zenohdwill panic if unable to load the requested plugin. Otherwise, it will simply log an error. Plugins are encouraged to look to this field to ascertain whether they should be allowed to panic or not.
The rest of the dictionary may be used by each plugin as they see fit. If elements of their configuration are modified at runtime, plugins will be given a chance to observe the modification and interfere with it.