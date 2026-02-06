# REST plugin · Zenoh - pub/sub, geo distributed storage, query

Source: https://zenoh.io/docs/manual/plugin-http

# Source: https://zenoh.io/docs/manual/plugin-http

# REST plugin
The REST plugin provides access to the ZenohREST APIby enabling an HTTP server on the Zenoh node where it is running.
Library name:zplugin_rest
There are two main ways to start this plugin:
- Through startup arguments:zenohd’s--rest-http-port=[PORT | IP:PORT | none]argument allows you to choose which port will be listened to by the HTTP server. Note that the default value for this argument is8000, meaning that unless you specifynoneexplicitly,zenohdwill use this plugin by default.
- Through configuration: you may also configure the rest plugin in azenohdconfig file, as illustrated in the Zenoh repo’sDEFAULT_CONFIG.json5 file