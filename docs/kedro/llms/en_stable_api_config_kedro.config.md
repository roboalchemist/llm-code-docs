# Source: https://docs.kedro.org/en/stable/api/config/kedro.config/index.md

# kedro.config

## kedro.config

`kedro.config` provides functionality for loading Kedro configuration from different file formats.

| Name                                                                                                                              | Type      | Description                               |
| --------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------------------------------------- |
| [`kedro.config.AbstractConfigLoader`](https://docs.kedro.org/en/stable/api/config/kedro.config.AbstractConfigLoader/index.md)     | Class     | Abstract base class for config loaders.   |
| [`kedro.config.OmegaConfigLoader`](https://docs.kedro.org/en/stable/api/config/kedro.config.OmegaConfigLoader/index.md)           | Class     | Config loader that uses OmegaConf.        |
| [`kedro.config.MissingConfigException`](https://docs.kedro.org/en/stable/api/config/kedro.config.MissingConfigException/index.md) | Exception | Raised when a required config is missing. |
