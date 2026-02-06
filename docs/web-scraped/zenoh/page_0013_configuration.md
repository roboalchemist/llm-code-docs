# Configuration · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/configuration

# Source: https://zenoh.io/docs/manual/configuration

# Configuration
From version 0.6 of Zenoh, configuration has changed in major ways. This page will take you through the new behaviour of configuration, whether you’re using Zenoh as a library, or as an executable throughzenohd.

# Configuringzenohd
There are 3 ways to configurezenohd, which may be used in any combination:
- using aconfiguration file,
- through thecommand line arguments,
- and by putting values on the configuration through theadminspace.

## Configuration files
zenohdhas supported configuration files for a long time now, but with version 0.6, we hope to make this the primary interface for configuring your Zenoh infrastructure.
As was the case before, you can specify which configuration file to load with the--config=/path/to/config/fileCLI argument.
If no path is specified,zenohdwill use a default configuration instead.
Currently,JSON5and YAML are the primary configuration format (as opposed to v0.5’s flat key-value files), but we may add support for other serialization formats in the future.
An example configuration can be readhere, apart from thepluginssection, we make an effort to keep the values aligned with the defaults.
The exact schema for the configuration is theConfigstructure, which can be found inthis file.
Don’t be alarmed, all of these fields are optional. Only configure the parts that are of interest to you.
We’d like to bring your attention to thepluginspart of the configuration, as plugin management has also changed a lot with version 0.6.
More on this in the page onplugins.

## Command line arguments
If you want to runzenohdwith small changes in its configuration, without going through the hassle of writing a new configuration file for it, you may use the--cfgCLI argument to edit the configuration.
Specifically, you may use any amount of--cfg='PATH:VALUE'arguments to specify the VALUEs you’d like to insert at specific PATHs in the configuration.
PATHs are/-separated paths to the part of the configuration you wish to change.
Note for plugins that setting a value in a plugin-less configuration forplugins/example-plugin/example/pathwill result in the recursive creation of the intermediate objects if necessary.
VALUEs must be JSON5-deserializable values: don’t forget to surround strings with quotes. Due to this, surrounding the wholePATH:VALUEpair with single-quotes is a good practice to avoid parsing errors.
If a value was already present for the specified PATH, it will be replaced with VALUE.
For convenience, some arguments ofzenohdare provided as shorthands for particularly useful--cfgpatterns, such as-P <plugin_name>which desugars to--cfg='plugins/<plugin_name>/__required__:true'.
In case of conflicts,--cfgoptions will override any other sources of configuration for their PATH.
You can use--rest-http-port=8000to enable the REST plugin inzenohd.

## Reactive configuration
It is possible to register callbacks that will be called when the configuration structure is modified. This letszenohd(or your own application) react to changes in the configuration during runtime.
In the case ofzenohd, the only user-accessible way of editing the configuration during runtime is through the admin space, as explained a bitfurtherin this page. Whether and how to react to modifications to the configuration file when it exists is still under debate by the core team.

## Adminspace configuration
The configuration of a Zenoh router can be changed at runtime via its admin space, if it’s configured to be writeable:
- either via the configuration file in theadminspace.permissionssection
```
{
  adminspace: {
    permissions: {
      read: true,
      write: true
    }
  }
}
```

- either via thezenohdcommand line option:--adminspace-permissions <[r|w|rw|none]>
Then you can change elements of it’s configuration once it’s started, by sending PUT messages to itsadmin space.
If one of thezenohdinstances uses the REST plugin to expose Zenoh to HTTP requests, this can be done simply by sending such requests with tools such ascurl.
Remember to enable the REST plugin inzenohdwith the command line option--rest-http-port=8000.
To do this, use commands such as
```
curl -X PUT http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/my-storage -d '{key_expr:"demo/mystore/**", volume:{id:"memory"}}'
#           ^- REST plugin addr ^ ^--- config space --^ ^---- the path to the configured value ---^    ^-------------- the value to insert ----------------^
```

Path-value pairs work much like they do when usingCLI arguments.
Note that while you may attempt to change any part of the configuration through this mean, not all of its properties are actually watched.For example, while the storage plugin watches for any change in its configuration and will attempt to act on it, the REST plugin will only log a warning that it observed a change, but won’t apply it.Changes to non-plugin parts of the configuration may be registered by the configuration, but not acted upon, such as themodefield of the configuration which is only ever read at startup.