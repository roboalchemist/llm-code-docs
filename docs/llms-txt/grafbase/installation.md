# Source: https://grafbase.com/docs/cli/installation.md

# Source: https://grafbase.com/docs/platform/self-hosting/installation.md

# Source: https://grafbase.com/docs/gateway/installation.md

# Source: https://grafbase.com/docs/cli/installation.md

# Source: https://grafbase.com/docs/platform/self-hosting/installation.md

# Source: https://grafbase.com/docs/gateway/installation.md

# Source: https://grafbase.com/docs/cli/installation.md

# Source: https://grafbase.com/docs/platform/self-hosting/installation.md

# Source: https://grafbase.com/docs/gateway/installation.md

# Installation

To install the Grafbase Gateway, run the following command:

```bash
curl -fsSL https://grafbase.com/downloads/gateway | bash
```

## Hybrid operation

In hybrid mode, the gateway fetches the current federated graph from the Grafbase platform. Create a federated graph in the Grafbase API, publish the subgraphs, and the gateway will always have the current graph running.

Start the gateway in hybrid mode with the graph reference and an organization access token:

```bash
GRAFBASE_ACCESS_TOKEN=token ./grafbase-gateway \
  --config grafbase.toml \
  --graph-ref graph@branch
```

`graph-ref` points to a graph created in the Grafbase API and its branch. If the branch is empty, the gateway uses the production branch by default.

Create the organization access token in the account settings under "Access Tokens" and ensure it has permission to read the graph.

The gateway polls for graph changes every ten seconds.

## Air-gapped operation

In air-gapped mode, the gateway never calls the Grafbase API. You must provide the federated graph SDL as a file.

Start the gateway in self-hosted mode:

```bash
./grafbase-gateway \
  --config /path/to/grafbase.toml \
  --schema /path/to/federated-schema.graphql \
  --listen-address 127.0.0.1:4000
```

Every five seconds, the gateway checks for changes in the schema file and initializes itself with the modified contents if it detects any changes.

## Configuration

The Grafbase Gateway reads its configuration from a TOML file. Read the configuration reference for more information.