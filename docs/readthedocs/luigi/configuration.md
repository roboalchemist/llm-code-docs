# Configuration

All configuration can be done by adding configuration files.

Supported config parsers:

- 

`cfg` (default), based on Python’s standard ConfigParser [https://docs.python.org/3/library/configparser.html]. Values may refer to environment variables using `${ENVVAR}` syntax.

- 

`toml`

You can choose right parser via `LUIGI_CONFIG_PARSER` environment variable. For example, `LUIGI_CONFIG_PARSER=toml`.

Default (cfg) parser are looked for in:

- 

`/etc/luigi/client.cfg` (deprecated)

- 

`/etc/luigi/luigi.cfg`

- 

`client.cfg` (deprecated)

- 

`luigi.cfg`

- 

`LUIGI_CONFIG_PATH` environment variable

TOML [https://github.com/toml-lang/toml] parser are looked for in:

- 

`/etc/luigi/luigi.toml`

- 

`luigi.toml`

- 

`LUIGI_CONFIG_PATH` environment variable

Both config lists increase in priority (from low to high). The order only
matters in case of key conflicts (see docs for ConfigParser.read [https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read]).
These files are meant for both the client and `luigid`.
If you decide to specify your own configuration you should make sure
that both the client and `luigid` load it properly.

The config file is broken into sections, each controlling a different part of the config.

Example cfg config:

```
[hadoop]
version=cdh4
streaming_jar=/usr/lib/hadoop-xyz/hadoop-streaming-xyz-123.jar

[core]
scheduler_host=luigi-host.mycompany.foo

```