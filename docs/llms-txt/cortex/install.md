# Source: https://docs.cortexlabs.com/clients/install.md

# Source: https://docs.cortexlabs.com/0.41/clients/install.md

# Source: https://docs.cortexlabs.com/0.40/clients/install.md

# Source: https://docs.cortexlabs.com/0.39/clients/install.md

# Source: https://docs.cortexlabs.com/0.38/clients/install.md

# Source: https://docs.cortexlabs.com/0.37/clients/install.md

# Source: https://docs.cortexlabs.com/0.36/clients/install.md

# Source: https://docs.cortexlabs.com/0.35/clients/install.md

# Source: https://docs.cortexlabs.com/0.34/clients/install.md

# Source: https://docs.cortexlabs.com/0.33/clients/install.md

# Source: https://docs.cortexlabs.com/0.32/clients/install.md

# Source: https://docs.cortexlabs.com/0.31/clusters/gcp/install.md

# Source: https://docs.cortexlabs.com/0.31/clusters/aws/install.md

# Source: https://docs.cortexlabs.com/0.31/clients/install.md

# Source: https://docs.cortexlabs.com/0.30/clusters/gcp/install.md

# Source: https://docs.cortexlabs.com/0.30/clusters/aws/install.md

# Source: https://docs.cortexlabs.com/0.30/clients/install.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-core-on-kubernetes/install.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-gcp/install.md

# Source: https://docs.cortexlabs.com/0.29/clusters/cortex-cloud-on-aws/install.md

# Source: https://docs.cortexlabs.com/0.29/clients/install.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-core-on-kubernetes/install.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-gcp/install.md

# Source: https://docs.cortexlabs.com/0.28/clusters/cortex-cloud-on-aws/install.md

# Source: https://docs.cortexlabs.com/0.28/clients/install.md

# Install

## Install with pip

To install the latest version:

```bash
pip install cortex
```

To install or upgrade to a specific version (e.g. v0.28.0):

```bash
pip install cortex==0.28.0
```

To upgrade to the latest version:

```bash
pip install --upgrade cortex
```

## Install without the Python client

```bash
# For example to download CLI version 0.28.0 (Note the "v"):
$ bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/v0.28.0/get-cli.sh)"
```

By default, the Cortex CLI is installed at `/usr/local/bin/cortex`. To install the executable elsewhere, export the `CORTEX_INSTALL_PATH` environment variable to your desired location before running the command above.

## Changing the CLI/client configuration directory

By default, the Cortex CLI/client creates a directory at `~/.cortex/` and uses it to store environment configuration. To use a different directory, export the `CORTEX_CLI_CONFIG_DIR` environment variable before running any `cortex` commands.
