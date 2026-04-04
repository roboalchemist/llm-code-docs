# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/from-docker-image/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/from-docker-image/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/from-docker-image/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/from-docker-image/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/from-docker-image/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/installation-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/installation-overview.md

# Installation overview

SonarQube Server docker images support running both on the `amd64` architecture and on `arm64`-based Apple Silicon.

We recommend using [Docker Engine](https://docs.docker.com/engine/) version 20.10 and above.

To install your SonarQube Server (Developer or Enterprise edition) from the Docker image:

1. Check the [server-host-requirements](https://docs.sonarsource.com/sonarqube-server/server-installation/server-host-requirements "mention").
2. Install the database. See [installing-the-database](https://docs.sonarsource.com/sonarqube-server/server-installation/installing-the-database "mention").
3. Prepare the Docker installation. See [prepare-installation](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/prepare-installation "mention")
4. Set up and start your Docker container. See [set-up-and-start-container](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/set-up-and-start-container "mention").
5. You can now open SonarQube Server in your web browser at the configured address (by default `http://localhost:9000`). The default system administrator credentials are **admin**/**admin**.
6. Depending on your environment, you may have to perform advanced setup. See [advanced-setup](https://docs.sonarsource.com/sonarqube-server/server-installation/from-docker-image/advanced-setup "mention").
7. You can secure SonarQube Server behind a proxy (see [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")) and configure network rules (see [network-rules](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules "mention")).
