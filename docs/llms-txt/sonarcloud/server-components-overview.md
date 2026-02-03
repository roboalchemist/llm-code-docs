# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/server-components-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/server-components-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/server-components-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/server-components-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/server-components-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/server-components-overview.md

# Server components

SonarQube Server runs the following Java processes:

* **Web**: serves the SonarQube Server user interface.
* **Elasticsearch (ES)**: manages an indexed copy of the database.
* **Compute Engine (CE)**: is in charge of processing code analysis reports and saving them in the SonarQube Server database.

In addition, the Java process **Sonar** is used to manage the availability of these processes.

The SonarQube database is used to store the following:

* Metrics and issues for code quality and security generated during code scans.
* The SonarQube Server instance configuration.
* The report job queue that is populated by the Sonarscanner and processed by the Compute Engine.

Both the Web and the CE process ensure data consistency when writing to the ES and SonarQube databases. In case of a disaster recovery of the ES database, it’s the Web process’s responsibility to rebuild the ES indexes.

<figure><img src="broken-reference" alt="SonarQube Java processes consist of Web, Elasticsearch, and Compute Engine"><figcaption></figcaption></figure>
