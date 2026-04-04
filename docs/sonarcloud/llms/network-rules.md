# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/data-center-edition/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/data-center-edition/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/data-center-edition/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/data-center-edition/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/data-center-edition/network-security/network-rules.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/network-rules.md

# Network rules

To lock down the communication in between the reverse proxy and SonarQube, you can define the following network rules:

| Protocol | Source        | Destination | Port                | Default |
| -------- | ------------- | ----------- | ------------------- | ------- |
| TCP      | Reverse Proxy | SonarQube   | `sonar.web.port`    | 9000    |
| TCP      | SonarQube     | SonarQube   | `sonar.search.port` | 9001    |
| TCP      | SonarQube     | SonarQube   | `sonar.es.port`     | random  |

You can further segment your network configuration if you specify a frontend network and keep Elasticsearch restricted to the loopback NiC.

| Network       | Parameter           | Description           | Default   |
| ------------- | ------------------- | --------------------- | --------- |
| Frontend      | `sonar.web.host`    | Frontend HTTP Network | 0.0.0.0   |
| Elasticsearch | `sonar.search.host` | Elasticsearch Network | 127.0.0.1 |

For information about the parameters, see [common-properties](https://docs.sonarsource.com/sonarqube-server/server-installation/system-properties/common-properties "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [securing-behind-proxy](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy "mention")
