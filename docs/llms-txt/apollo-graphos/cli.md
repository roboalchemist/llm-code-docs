# Source: https://www.apollographql.com/docs/graphos/routing/configuration/cli.md

# Router CLI Configuration Reference

This reference covers the command-line options for configuring an Apollo Router.

## Command-line options

This reference lists and describes the options supported by the `router` binary via command-line options. Where indicated, some of these options can also be provided via an environment variable.

For options available as both a command-line option and an environment variable, the command-line value takes precedence.

Option / Environment Variable
Description

##### `-s` / `--supergraph`

`APOLLO_ROUTER_SUPERGRAPH_PATH`, `APOLLO_ROUTER_SUPERGRAPH_URLS`

The [supergraph schema](https://www.apollographql.com/docs/federation/federated-types/overview#supergraph-schema) of a router. Specified by absolute or relative path (`-s` / `--supergraph <supergraph_path>`, or `APOLLO_ROUTER_SUPERGRAPH_PATH`), or a comma-separated list of URLs (`--supergraph-urls <urls>`, or `APOLLO_ROUTER_SUPERGRAPH_URLS`).

> 💡 Avoid embedding tokens in `APOLLO_ROUTER_SUPERGRAPH_URLS` because the URLs may appear in log messages.

Setting this option disables polling from Apollo Uplink to fetch the latest supergraph schema.

To learn how to compose your supergraph schema with the Rover CLI, see the [Federation quickstart](https://www.apollographql.com/docs/federation/quickstart).

**Required** if you are *not* using managed federation. If you *are* using managed federation, you may need to set this option when following [advanced deployment workflows](https://www.apollographql.com/docs/federation/managed-federation/deployment/#advanced-deployment-workflows).

##### `-c` / `--config`

`APOLLO_ROUTER_CONFIG_PATH`

The absolute or relative path to the router's optional [YAML configuration file](https://www.apollographql.com/docs/graphos/routing/configuration/yaml).

##### `--apollo-key-path`

`APOLLO_KEY_PATH`

The absolute or relative path to a file containing the Apollo graph API key for use with managed federation.

⚠️ **This is not available on Windows.**

##### `--dev`

⚠️ **Do not set this option in production!**

If set, a router runs in dev mode to help with local development.

[Learn more about dev mode](https://www.apollographql.com/docs/graphos/routing/configuration/cli.md#development-mode).

##### `--hr` / `--hot-reload`

`APOLLO_ROUTER_HOT_RELOAD`

When you set this option, the router watches for changes to its configuration file and any supergraph file passed with `--supergraph`. It reloads them automatically without downtime. This setting only affects local files provided to the router. The router automatically reloads supergraphs and configurations from GraphOS (provided via Launches and delivered via Uplink), regardless of this setting.

For details on hot reload support for different schema sources and performance considerations, see [Hot Reload](https://www.apollographql.com/docs/graphos/routing/configuration/hot-reload-schema).

##### `--log`

`APOLLO_ROUTER_LOG`

The log level, indicating the *most* severe log message type to include. In ascending order of verbosity, can be one of: `off`, `error`, `warn`, `info`, `debug`, or `trace`.

The default value is `info`.

##### `--license`

`APOLLO_ROUTER_LICENSE_PATH`, `APOLLO_ROUTER_LICENSE`

An offline GraphOS Enterprise license. Enables Enterprise router features when disconnected from GraphOS.

An offline license is specified either as an absolute or relative path to a license file (`--license <license_path>` or `APOLLO_ROUTER_LICENSE_PATH`), or as the stringified contents of a license (`APOLLO_ROUTER_LICENSE`).

When not set, the router retrieves an Enterprise license [from GraphOS via Apollo Uplink](https://www.apollographql.com/docs/router/enterprise-features/#the-enterprise-license).

For information about fetching an offline license and configuring the router, see [Offline Enterprise license](https://www.apollographql.com/docs/graphos/routing/license/#offline-license).

##### `--apollo-uplink-endpoints`

`APOLLO_UPLINK_ENDPOINTS`

If using [managed federation](https://www.apollographql.com/docs/federation/managed-federation/overview/), the Apollo Uplink URL(s) that the router should poll to fetch its latest configuration. Almost all managed router instances should *omit* this option to use the default set of Uplink URLs.

If you specify multiple URLs, separate them with commas (no whitespace).

For default behavior and possible values, see [Apollo Uplink](https://www.apollographql.com/docs/federation/managed-federation/uplink/).

##### `--graph-artifact-reference`

`APOLLO_GRAPH_ARTIFACT_REFERENCE`

An OCI reference to a graph artifact that contains the supergraph schema for the router to run.

When you set this option, the router uses the schema from the specified graph artifact instead of Apollo Uplink.
The router still fetches entitlements and persisted queries from Uplink.

##### `--apollo-uplink-timeout`

`APOLLO_UPLINK_TIMEOUT`

The request timeout for each poll sent to Apollo Uplink.

The default value is `30s` (thirty seconds).

##### `--anonymous-telemetry-disabled`

`APOLLO_TELEMETRY_DISABLED`

If set, disables sending anonymous usage information to Apollo.

##### `--listen`

`APOLLO_ROUTER_LISTEN_ADDRESS`

If set, the listen address of the router.

##### `-V` / `--version`

If set, the router prints its version number, then exits.

### Development mode

The router can be run in development mode by using the `--dev` command-line option.

The `--dev` option is equivalent to running the router with the `--hot-reload` option the following configuration options:

```yaml
sandbox:
  enabled: true
homepage:
  enabled: false
supergraph:
  introspection: true
include_subgraph_errors:
  all: true
plugins:
  # Enable with the header, Apollo-Expose-Query-Plan: true
  experimental.expose_query_plan: true
```

**Don't set the `--dev` option in production.** If you want to replicate any specific dev mode functionality in production, set the corresponding option in your [YAML config file](https://www.apollographql.com/docs/graphos/routing/configuration/yaml).

## Configuration schema for IDE validation

The router can generate a JSON schema for config validation in your text editor. This schema helps you format the YAML file correctly and also provides content assistance.

Generate the schema with the following command:

```bash
./router config schema > configuration_schema.json
```

After you generate the schema, configure your text editor. Here are the instructions for some commonly used editors:

* [Visual Studio Code](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings)
* [Emacs](https://emacs-lsp.github.io/lsp-mode/page/lsp-yaml)
* [IntelliJ](https://www.jetbrains.com/help/idea/json.html#ws_json_using_schemas)
* [Sublime](https://github.com/sublimelsp/LSP-yaml)
* [Vim](https://github.com/Quramy/vison)

## Upgrading your router configuration

New releases of the router might introduce breaking changes to the [YAML config file's](https://www.apollographql.com/docs/graphos/routing/configuration/yaml) expected format, usually to extend existing functionality or improve usability.

**If you run a new version of your router with a configuration file that it no longer supports, it emits a warning on startup and terminates.**

If you encounter this warning, you can use the `router config upgrade` command to see the new expected format for your existing configuration file:

```bash
./router config upgrade <path_to_config.yaml>
```

You can also view a diff of exactly which changes are necessary to upgrade your existing configuration file:

```bash
./router config upgrade --diff <path_to_config.yaml>
```

## Validating your router configuration

The router can be used to validate an existing configuration file. This can be useful if you want to have a validate step as part of your CI pipeline.

```text
./router config validate <path-to-config-file.yaml>
```

This command takes a config file and validates it against the router's full supported configuration format.

This is a static validation that checks if it is syntactically correct using the JSON schema. The router does additional logical checks on startup against the config that this command does not capture.
