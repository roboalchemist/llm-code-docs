# Source: https://docs.sonarsource.com/sonarqube-community-build/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/try-out-sonarqube.md

# Source: https://docs.sonarsource.com/sonarqube-server/try-out-sonarqube.md

# Try out SonarQube Server

You’ve heard about how [SonarQube Server](https://www.sonarsource.com/products/sonarqube/) can help you write high quality, safer code, and now you’re ready to try it out for yourself. This guide shows you how to install a local instance of SonarQube Server and analyze a project. Installing a local instance gets you up and running quickly, so you can experience SonarQube Server firsthand.

You can try [Developer edition](https://www.sonarsource.com/plans-and-pricing/developer/) or [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/) for free for 14 days.

Once you’re ready to set up a production instance, take a look at the [introduction](https://docs.sonarsource.com/sonarqube-server/server-installation/introduction "mention") documentation on installing the Developer or Enterprise Editions.

### Installing a local instance of SonarQube Server <a href="#installing-a-local-instance-of-sonarqube" id="installing-a-local-instance-of-sonarqube"></a>

You can evaluate SonarQube Server using a traditional installation with the [zip file](https://www.sonarsource.com/products/sonarqube/downloads/) or you can spin up a Docker container using one of our [Docker images](https://hub.docker.com/_/sonarqube/). Select the method you prefer below to expand the installation instructions:

<details>

<summary>From the zip file</summary>

1. Download and install [Java 21](https://adoptium.net/en-GB/temurin/releases/?version=21) on your system.
2. [Download](https://www.sonarsource.com/products/sonarqube/downloads/) the SonarQube Developer Edition zip file.
3. As a **non-`root`** **user**, unzip it in, for example, `C:\sonarqube` or `/opt/sonarqube`.
4. As a **non-`root`** **user**, start the SonarQube server:

```bash
# On Windows, execute:
C:\sonarqube\bin\windows-x86-64\StartSonar.bat
 
# On other operating systems, as a non-root user execute:
/opt/sonarqube/bin/<OS>/sonar.sh console
```

If your instance fails to start, check your [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention") to find the cause.

</details>

<details>

<summary>From the Docker image</summary>

Find the Developer Edition Docker image on [Docker hub](https://hub.docker.com/_/sonarqube/).

1. Start the server by running:

```bash
$ docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:latest
```

</details>

Once your instance is up and running, Log in to <http://localhost:9000> using System Administrator credentials:

* login: admin
* password: admin

### Analyzing a project <a href="#analyzing-a-project" id="analyzing-a-project"></a>

Now that you’re logged in to your local SonarQube Server instance, let’s analyze a project:

1. Select **Create new project**.
2. Give your project a **Project key** and a **Display name** and select **Set up**.
3. Under **Provide a token**, select **Generate a token**. Give your token a name, select **Generate**, and click **Continue**.
4. Select your project’s main language under **Run analysis on your project**, and follow the instructions to analyze your project. Here you’ll download and execute a scanner on your code (if you’re using Maven or Gradle, the scanner is automatically downloaded).

After successfully analyzing your code, you’ll see your first analysis on SonarQube Server:

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/Ql5VKaURlQx5AvFFM9ma/analyse-projects-mqr-mode.png.png" alt="Analysis of a project in Multi-Quality rule mode on SonarQube Server." width="563"><figcaption></figcaption></figure></div>

Your first analysis is a measure of your current code. As a developer, you focus on maintaining high standards and taking responsibility specifically for the new code you’re working on. Code that has been added or changed from this point should be your focus moving forward. See [about-new-code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code "mention") for more information.
