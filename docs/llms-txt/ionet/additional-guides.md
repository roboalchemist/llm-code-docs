# Source: https://io.net/docs/guides/workers/additional-guides.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Additional Guides

### Ports

Expose the ports below to ensure platform stability for Linux:

* TCP: 443, 25061, 5432, 80
* UDP: 80, 443, 41641, 3478

Ensure that these ports are open and accessible to enable smooth operation of the platform.

### How can I verify that program has started successfully?

* When running the following command on Terminal, **you should always have 2 Docker containers running**:
  <CodeGroup>
    ```Text Terminal Command theme={null}
     docker ps
    ```
  </CodeGroup>

* If there are no containers or only one container running after running the docker run **-d ... command** from the website:

  * Stop the platform using the command provided in the guide above.
  * Restart the platform using the command from the website again.

### reset\_drivers\_and\_docker.sh :

Create a new file called `reset_drivers_and_docker.sh`, and copy paste the code snippet below:
