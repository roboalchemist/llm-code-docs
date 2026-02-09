# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/from-docker-image/set-up-and-start-container.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/from-docker-image/set-up-and-start-container.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/from-docker-image/set-up-and-start-container.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/from-docker-image/set-up-and-start-container.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container.md

# Set up and start your container

You can set up and start the SonarQube container either from the command line (docker run) or from a configuration file (docker compose). Installation setup relies on system properties, which are preferably configured via environment variables in a Docker environment.

### Using docker run

Run the image as illustrated in the docker run command below. You can define your system properties by using the `-e` environment variable flag in the command. See [#mandatory-and-relevant-settings](#mandatory-and-relevant-settings "mention") below for information about the properties to be set.

```sh
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

Note that:

* By default, the server running within the container will listen on port 9000. The `-p 9000:9000` argument is used to expose the container port 9000 to the host port 9000: `-p port1:port2` maps container’s port `port1` as `port2` on the host.
* For `<image_name>`, check the tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube).

### Using Docker compose <a href="#using-docker-run" id="using-docker-run"></a>

If you’re using [Docker Compose](https://docs.docker.com/compose/), use this [yml file example](https://github.com/SonarSource/docker-sonarqube/tree/master/example-compose-files/sq-with-postgres) as a reference when configuring your `.yml` file. You can define the system properties by setting the corresponding environment variables in the `environment` section of the .`yml` file. See [#mandatory-and-relevant-settings](#mandatory-and-relevant-settings "mention") below for information about the properties to be set.

Note that:

* By default, the server running within the container will listen on port 9000. The following code is used to expose the container port 9000 to the host port 9000 (`"port1:port2"` maps container’s port `port1` as `port2` on the host):

```yaml
ports:
      - "9000:9000"
```

* In the `image` tag, use the tag value corresponding to the SonarQube Server version you want to use. Check the SonarQube Server image tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube). For example, to use the LTA version of the Developer Edition:

  ```yaml
  image:  sonarqube:2025-lta-developer
  ```

{% hint style="info" %}
Unless you intend to delete the database and start new when running your image, be careful not to use `-v` to `docker-compose down` and, be careful when running commands like `docker system prune` or `docker volume prune`; regardless if you use an `external: true` parameter, your database volumes will not persist beyond the initial startup and shutdown of SonarQube.
{% endhint %}

### Mandatory and relevant settings

You must set the access to your database and you should check the web server connection parameters. This section explains also other settings that are optional.

#### Set access to the database <a href="#using-docker-run" id="using-docker-run"></a>

You must configure the access to your database (except if you want to use SonarQube for test purposes and want to use the embedded database H2). To do so, set the system properties (environment variables) related to database access:

* SONAR\_JDBC\_USERNAME
* SONAR\_JDBC\_PASSWORD
* SONAR\_JDBC\_URL

For more information, see [#general](https://docs.sonarsource.com/sonarqube-server/system-properties/common-properties#general "mention").

#### Check the web server connection parameters <a href="#check-web-server-connection-parameters" id="check-web-server-connection-parameters"></a>

Check the default values of the following system properties and change their values if necessary:

* SONAR\_WEB\_HOST
* SONAR\_WEB\_PORT
* SONAR\_WEB\_CONTEXT

To do so, see [#web-server-connection](https://docs.sonarsource.com/sonarqube-server/system-properties/common-properties#web-server-connection "mention").

#### Enabling IPv6 <a href="#enabling-ipv6" id="enabling-ipv6"></a>

When you run your Docker container:

* Enable IPv6 in the JVM by setting the `JAVA_TOOL_OPTIONS` environment variable to `-Djava.net.preferIPv6Addresses=true`.
* Enable IPv6 in SonarQube by setting the `SONAR_WEB_JAVAADDITIONALOPTS` environment variable (system property) to `-Djava.net.preferIPv6Addresses=true`.

See below for instructions depending on the Docker tool used.

<details>

<summary>With docker-run</summary>

Set the environment variables in the docker run command as illustrated below.

```sh
docker run -d --name sonarqube \
    -p 9000:9000 \
    -e JAVA_TOOL_OPTIONS="-Djava.net.preferIPv6Addresses=true" \
    -e SONAR_WEB_JAVAADDITIONALOPTS="-Djava.net.preferIPv6Addresses=true" \
    ...  \
    <image_name>
```

</details>

<details>

<summary>With docker-compose</summary>

Set the environment variables in the `environment` section of the .`yml` file as illustrated below.

```yaml
...
environment:
      SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonar
      SONAR_JDBC_USERNAME: sonar
      SONAR_JDBC_PASSWORD: sonar
      JAVA_TOOL_OPTIONS: ‘-Djava.net.preferIPv6Addresses=true’
      SONAR_WEB_JAVAADDITIONALOPTS: ‘-Djava.net.preferIPv6Addresses=true’

...
```

</details>

{% hint style="warning" %}
IPv6 is not officially supported for the Docker images of the Data Center Edition.
{% endhint %}

#### Keeping user sessions alive on server restart <a href="#keeping-user-sessions" id="keeping-user-sessions"></a>

To maintain your user sessions accross server restarts:

* Store the JWT token you generated during pre-installation in the `SONAR_AUTH_JWTBASE64HS256SECRET` system property.

See also [jwt-token](https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/jwt-token "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/installation-overview "mention")
* [prepare-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/prepare-installation "mention")
* [advanced-setup](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/advanced-setup "mention")
* [system-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules "mention")
