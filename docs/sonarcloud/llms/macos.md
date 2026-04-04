# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/pre-installation/macos.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/pre-installation/macos.md

# On macOS systems

Because SonarQube Server uses an embedded Elasticsearch, make sure that your host configuration complies with the [Elasticsearch production mode requirements](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html#docker-cli-run-prod-mode) and [File Descriptors configuration](https://www.elastic.co/guide/en/elasticsearch/reference/current/file-descriptors.html).

## Configuring the maximum number of open files <a href="#configuring-the-maximum-number-of-open-files" id="configuring-the-maximum-number-of-open-files"></a>

Set the file limit values by running the following commands.

```sh
sudo sysctl kern.maxfiles=131072
sudo sysctl kern.maxfilesperproc=131072
ulimit -n 131072
```
