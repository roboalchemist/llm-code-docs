# Source: https://grafbase.com/docs/gateway/deployment/docker.md

# Deploy to Docker

The Grafbase Gateway is published as a Docker image to GitHub Container Registry.

Example `compose.yaml`:

```yaml
services:
  grafbase:
    image: ghcr.io/grafbase/gateway:latest
    restart: always
    volumes:
      - ./grafbase.toml:/etc/grafbase.toml
    environment:
      GRAFBASE_GRAPH_REF: 'graph-ref@branch'
      GRAFBASE_ACCESS_TOKEN: 'ACCESS_TOKEN_HERE'
    ports:
      - '5000:5000'
```

The above `compose.yaml` file will start the Grafbase Gateway with the latest version of the image, bind the configuration file `grafbase.toml` to the container, and set the environment variables `GRAFBASE_GRAPH_REF` and `GRAFBASE_ACCESS_TOKEN` to the desired graph reference and access token, respectively. The configuration file `grafbase.toml` should be present in the same directory as the `compose.yaml` file.