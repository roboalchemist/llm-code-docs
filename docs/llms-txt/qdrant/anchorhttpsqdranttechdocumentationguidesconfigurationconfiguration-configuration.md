# [Anchor](https://qdrant.tech/documentation/guides/configuration/\#configuration) Configuration

Qdrant ships with sensible defaults for collection and network settings that are suitable for most use cases. You can view these defaults in the [Qdrant source](https://github.com/qdrant/qdrant/blob/master/config/config.yaml). If you need to customize the settings, you can do so using configuration files and environment variables.

## [Anchor](https://qdrant.tech/documentation/guides/configuration/\#configuration-files) Configuration Files

To customize Qdrant, you can mount your configuration file in any of the following locations. This guide uses `.yaml` files, but Qdrant also supports other formats such as `.toml`, `.json`, and `.ini`.

1. **Main Configuration: `qdrant/config/config.yaml`**

Mount your custom `config.yaml` file to override default settings:



```bash
docker run -p 6333:6333 \
       -v $(pwd)/config.yaml:/qdrant/config/config.yaml \
       qdrant/qdrant

```

2. **Environment-Specific Configuration: `config/{RUN_MODE}.yaml`**

Qdrant looks for an environment-specific configuration file based on the `RUN_MODE` variable. By default, the [official Docker image](https://hub.docker.com/r/qdrant/qdrant) uses `RUN_MODE=production`, meaning it will look for `config/production.yaml`.

You can override this by setting `RUN_MODE` to another value (e.g., `dev`), and providing the corresponding file:



```bash
docker run -p 6333:6333 \
       -v $(pwd)/dev.yaml:/qdrant/config/dev.yaml \
       -e RUN_MODE=dev \
       qdrant/qdrant

```

3. **Local Configuration: `config/local.yaml`**

The `local.yaml` file is typically used for machine-specific settings that are not tracked in version control:



```bash
docker run -p 6333:6333 \
       -v $(pwd)/local.yaml:/qdrant/config/local.yaml \
       qdrant/qdrant

```

4. **Custom Configuration via `--config-path`**

You can specify a custom configuration file path using the `--config-path` argument. This will override other configuration files:



```bash
docker run -p 6333:6333 \
       -v $(pwd)/config.yaml:/path/to/config.yaml \
       qdrant/qdrant \
       ./qdrant --config-path /path/to/config.yaml

```


For details on how these configurations are loaded and merged, see the [loading order and priority](https://qdrant.tech/documentation/guides/configuration/#loading-order-and-priority). The full list of available configuration options can be found [below](https://qdrant.tech/documentation/guides/configuration/#configuration-options).

## [Anchor](https://qdrant.tech/documentation/guides/configuration/\#environment-variables) Environment Variables

You can also configure Qdrant using environment variables, which always take the highest priority and override any file-based settings.

Environment variables follow this format: they should be prefixed with `QDRANT__`, and nested properties should be separated by double underscores ( `__`). For example:

```bash
docker run -p 6333:6333 \
    -e QDRANT__LOG_LEVEL=INFO \
    -e QDRANT__SERVICE__API_KEY=<MY_SECRET_KEY> \
    -e QDRANT__SERVICE__ENABLE_TLS=1 \
    -e QDRANT__TLS__CERT=./tls/cert.pem \
    qdrant/qdrant

```

This results in the following configuration:

```yaml
log_level: INFO
service:
  enable_tls: true
  api_key: <MY_SECRET_KEY>
tls:
  cert: ./tls/cert.pem

```

## [Anchor](https://qdrant.tech/documentation/guides/configuration/\#loading-order-and-priority) Loading Order and Priority

During startup, Qdrant merges multiple configuration sources into a single effective configuration. The loading order is as follows (from least to most significant):

1. Embedded default configuration
2. `config/config.yaml`
3. `config/{RUN_MODE}.yaml`
4. `config/local.yaml`
5. Custom configuration file
6. Environment variables

### [Anchor](https://qdrant.tech/documentation/guides/configuration/\#overriding-behavior) Overriding Behavior

Settings from later sources in the list override those from earlier sources:

- Settings in `config/{RUN_MODE}.yaml` (3) will override those in `config/config.yaml` (2).
- A custom configuration file provided via `--config-path` (5) will override all other file-based settings.
- Environment variables (6) have the highest priority and will override any settings from files.

## [Anchor](https://qdrant.tech/documentation/guides/configuration/\#configuration-validation) Configuration Validation

Qdrant validates the configuration during startup. If any issues are found, the server will terminate immediately, providing information about the error. For example:

```console
Error: invalid type: 64-bit integer `-1`, expected an unsigned 64-bit or smaller integer for key `storage.hnsw_index.max_indexing_threads` in config/production.yaml

```

This ensures that misconfigurations are caught early, preventing Qdrant from running with invalid settings.

## [Anchor](https://qdrant.tech/documentation/guides/configuration/\#configuration-options) Configuration Options

The following YAML example describes the available configuration options.

```yaml
log_level: INFO