# Source: https://docs.prefect.io/v3/how-to-guides/self-hosted/server-docker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# How to run the Prefect server in Docker

> Run a containerized Prefect server instance with Docker.

You can use the official Prefect Docker image to run a server in a container.

If you're running a server in a Docker container, you need to:

* Port forward the server to your local machine (e.g. `-p 4200:4200`)
* Set the `--host` flag on the `prefect server start` command to `0.0.0.0`
* Set the API server address, `PREFECT_API_URL`, to use Prefect within a container.

For example:

```bash  theme={null}
docker run -p 4200:4200 -d --rm prefecthq/prefect:3-latest -- prefect server start --host 0.0.0.0
```

<Tip>
  The `-d` flag runs the container in detached mode (i.e. in the background) and the `--rm` flag removes the container once it is stopped.
</Tip>

After running this command, verify that your local `prefect` profile is configured to point at your containerized server.

```bash  theme={null}
prefect config view --show-secrets
```

Open the dashboard in your browser:

```bash  theme={null}
prefect dashboard open
```

For more information, see the Docker topic about [Networking using the host network](https://docs.docker.com/network/network-tutorial-host/).

## Further reading

* [How to scale self-hosted Prefect](/v3/advanced/self-hosted)
* [Server concepts](/v3/concepts/server)
* [How to manage settings](/v3/how-to-guides/configuration/manage-settings)


Built with [Mintlify](https://mintlify.com).