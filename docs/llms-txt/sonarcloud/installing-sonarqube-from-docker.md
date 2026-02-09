# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/install-the-server/installing-sonarqube-from-docker.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/install-the-server/installing-sonarqube-from-docker.md

# Installing from the Docker image

SonarQube Server docker images support running both on the `amd64` architecture and on `arm64`-based Apple Silicon.

We recommend using [Docker Engine](https://docs.docker.com/engine/) version 20.10 and above.

First, check the requirements (see [server-host](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/installation-requirements/server-host "mention")) and perform the pre-installation steps (see [pre-installation](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation "mention")). Then follow these steps for your first installation:

### Create volumes to persist data <a href="#create-volumes" id="create-volumes"></a>

Creating the following volumes helps prevent the loss of information when updating to a new version or upgrading to a higher edition:

* `sonarqube_data`: contains data files, such as Elasticsearch indexes.
* `sonarqube_logs`: contains SonarQube Server logs about access, web process, CE process, and Elasticsearch.
* `sonarqube_extensions`: will contain any plugins you install and the Oracle JDBC driver if necessary.

Create the volumes with the following commands:

```css-79elbk
$> docker volume create --name sonarqube_data
$> docker volume create --name sonarqube_logs
$> docker volume create --name sonarqube_extensions
```

{% hint style="warning" %}
Make sure you’re using [**volumes**](https://docs.docker.com/storage/volumes/) as shown with the above commands, and not [**bind mounts**](https://docs.docker.com/storage/bind-mounts/). Using bind mounts prevents plugins from populating correctly.
{% endhint %}

### Add the JDBC driver (if using an Oracle database) <a href="#add-jdbc-driver" id="add-jdbc-driver"></a>

Drivers for supported databases (except Oracle) are already provided. If you’re using an Oracle database, you need to add the JDBC driver to the `sonar_extensions` volume. To do this:

a. Start the SonarQube Server container with the embedded H2 database:

```css-79elbk
$ docker run --rm \
    -p 9000:9000 \
    -v sonarqube_extensions:/opt/sonarqube/extensions \
    <image_name>
```

For `<image_name>`, check the tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube).

b. Exit once SonarQube Server has started properly.

c. Copy the Oracle JDBC driver into `sonarqube_extensions/jdbc-driver/oracle`.

### Start the SonarQube Server container <a href="#start-container" id="start-container"></a>

Start the SonarQube Server container:

* either from the command line (docker run) or
* from a configuration file (docker compose).

For docker-based setups, environment variables supersede all parameters that were provided with properties. See [environment-variables](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/environment-variables "mention") for more details.

There is more information about installing and updating SonarQube Server plugins inside your Docker volume found on the [install-a-plugin](https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/plugins/install-a-plugin "mention") page.

#### Port binding <a href="#port-binding" id="port-binding"></a>

By default, the server running within the container will listen on port 9000. You can expose the container port 9000 to the host port 9000 with the `-p 9000:9000` argument to `docker run`, like the command below:

```css-79elbk
docker run --name sonarqube-custom -p 9000:9000 sonarqube:10.6-community
```

You can then browse to `http://localhost:9000` or `http://host-ip:9000` in your web browser to access the SonarQube Server web interface.

#### Starting the container by using docker run <a href="#starting-the-container-by-using-docker-run" id="starting-the-container-by-using-docker-run"></a>

Run the image with your database properties defined using the `-e` environment variable flag:

```css-79elbk
$> docker run -d --name sonarqube \
    -p 9000:9000 \
    -e SONAR_JDBC_URL=... \
    -e SONAR_JDBC_USERNAME=... \
    -e SONAR_JDBC_PASSWORD=... \
    -v sonarqube_data:/opt/sonarqube/data \
    -v sonarqube_extensions:/opt/sonarqube/extensions \
    -v sonarqube_logs:/opt/sonarqube/logs \
    <image_name>
```

For `<image_name>`, check the tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube).

#### Starting the container by using Docker compose <a href="#starting-the-container-by-using-docker-compose" id="starting-the-container-by-using-docker-compose"></a>

{% hint style="info" %}
Unless you intend to delete the database and start new when running your image ,be careful not to use `-v` to `docker-compose down` and, be careful when running commands like `docker system prune` or `docker volume prune`; regardless if you use an `external: true` parameter, your database volumes will not persist beyond the initial startup and shutdown of SonarQube Server.
{% endhint %}

If you’re using [Docker Compose](https://docs.docker.com/compose/), use this [yml file example](https://github.com/SonarSource/docker-sonarqube/tree/master/example-compose-files/sq-with-postgres) as a reference when configuring your `.yml` file. In the `image` tag, use the tag value corresponding to the SonarQube Server version you want to use, e.g, to use the LTA version of the Developer Edition:

```css-79elbk
image:  sonarqube:2025-lta-developer
```

Check the SonarQube Server image tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube).

#### Next steps <a href="#next-steps" id="next-steps"></a>

Once your server is installed and running, you can access SonarQube Server UI in your web browser (the default system administrator credentials are **admin**/**admin**) and you’re ready to begin [overview](https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/overview "mention").
