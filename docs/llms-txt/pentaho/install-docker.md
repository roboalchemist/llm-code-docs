# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-docker.md

# Install Docker

Docker is essential for creating and managing containers required to run Pentaho Data Catalog and its dependencies, including Pentaho Server, MongoDB, and the Metadata Repository. Before installing Data Catalog using Docker, ensure that both Docker and Docker Compose are installed and configured on your system.

Perform the following steps to install Docker:

**Prerequisites**

Ensure you have referred to [Components Reference](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/components-reference) to ensure that your server meets Data Catalog's requirements for this version of the software.

**Procedure**

1. Refer to the [Install Docker Engine](https://docs.docker.com/engine/install/) instructions for your operating system and install the Docker Engine.

   **Note:** The code snippets in the following steps are provided as examples for the Ubuntu operating system.
2. If you are not logged in as root, run the following command to elevate privileges for the duration of installation as opposed to using `sudo` for most commands.

   ```
   sudo su
   ```
3. Update the required libraries and packages.

   ```
   apt-get update
   ```
4. Install the Docker packages.

   ```
   apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```
5. Verify Docker version is installed.

   ```
   docker --version
   ```

   It returns a valid version number.
6. Verify the installation is successful by running the `hello-world` image.

   ```
   docker run hello-world
   ```

   You see a message indicating that Docker is working.
7. Verify the Docker Compose is installed.

   ```
   docker-compose --version
   ```

   It returns a valid version number.

**Result**

You have successfully installed Docker and Docker Compose on the system.

**Nest steps**

You can [install Data Catalog](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog) on the server computer.
