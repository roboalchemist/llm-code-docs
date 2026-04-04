# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/starting-sonarqube-container.md

# Starting SonarQube container

### Starting the container by using docker run <a href="#using-docker-run" id="using-docker-run"></a>

Run the image with your database properties defined using the `-e` environment variable flag:

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

### Starting the container by using Docker compose <a href="#by-using-docker-compose" id="by-using-docker-compose"></a>

If you’re using [Docker Compose](https://docs.docker.com/compose/), use this [yml file example](https://github.com/SonarSource/docker-sonarqube/tree/master/example-compose-files/sq-with-postgres) as a reference when configuring your `.yml` file.

Note that:

* By default, the server running within the container will listen on port 9000. The following code is used to expose the container port 9000 to the host port 9000 (`"port1:port2"` maps container’s port `port1` as `port2` on the host):

```css-79elbk
ports:

      - "9000:9000"
```

* In the `image` tag, use the tag value corresponding to the SonarQube Server version you want to use. Check the SonarQube Server image tags currently available on the [DockerHub page](https://hub.docker.com/_/sonarqube). For example, to use the LTA version of the Developer Edition:

```css-79elbk
image:  sonarqube:2025-lta-developer
```

{% hint style="info" %}
Unless you intend to delete the database and start new when running your image, be careful not to use `-v` to `docker-compose down` and, be careful when running commands like `docker system prune` or `docker volume prune`; regardless if you use an `external: true` parameter, your database volumes will not persist beyond the initial startup and shutdown of SonarQube.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [installation-overview](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/installation-overview "mention")
* [basic-installation](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/basic-installation "mention")
* [advanced-setup](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/advanced-setup "mention")
* **Configuring network security features:**
  * [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/network-security/securing-behind-proxy "mention")
  * [network-rules](https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/network-security/network-rules "mention")
