# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/from-docker-image/prepare-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/from-docker-image/prepare-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/from-docker-image/prepare-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/from-docker-image/prepare-installation.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/prepare-installation.md

# Prepare the Docker installation

### Perform the pre-installation steps

See:

* [linux](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/linux "mention")
* [unix](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/unix "mention")
* [macos](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/macos "mention")
* [jwt-token](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/jwt-token "mention") (to keep user sessions alive during startup)

### Create volumes to persist data <a href="#create-volumes" id="create-volumes"></a>

Creating the following volumes helps prevent the loss of information when updating to a new version or upgrading to a higher edition:

* `sonarqube_data`: contains data files, such as Elasticsearch indexes
* `sonarqube_logs`: contains SonarQube Server logs about access, web process, CE process, and Elasticsearch
* `sonarqube_extensions`: will contain any plugins you install and the Oracle JDBC driver if necessary.

Create the volumes with the following commands:

```bash
docker volume create --name sonarqube_data
docker volume create --name sonarqube_logs
docker volume create --name sonarqube_extensions
```

{% hint style="warning" %}
Make sure you’re using [**volumes**](https://docs.docker.com/storage/volumes/) as shown with the above commands, and not [**bind mounts**](https://docs.docker.com/storage/bind-mounts/). Using bind mounts prevents plugins from populating correctly.
{% endhint %}

### Oracle database: add the JDBC driver <a href="#add-jdbc-driver" id="add-jdbc-driver"></a>

Drivers for supported databases (except Oracle) are already provided. If you’re using an Oracle database, you need to add the JDBC driver to the `sonar_extensions` volume. To do this:

1. Start the SonarQube container with the embedded H2 database:

```bash
docker run --rm \
    -p 9000:9000 \
    -v sonarqube_extensions:/opt/sonarqube/extensions \
    <image_name>
```

For `<image_name>`, check the tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube).

2. Exit once SonarQube Server has started properly.
3. Copy the Oracle JDBC driver into `sonarqube_extensions/jdbc-driver/oracle`.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/installation-overview "mention")
* [set-up-and-start-container](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container "mention")
* [advanced-setup](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/advanced-setup "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules "mention")
