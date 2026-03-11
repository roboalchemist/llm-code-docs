# Source: https://docs.axonius.com/docs/sonar-qube-server.md

# SonarQube Server

SonarQube Server is a tool that provides automated code review and static analysis to detect coding issues and enforce quality rules.

### Asset Types Fetched

* Vulnerabilities, Users, SaaS Applications, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Token

### APIs

Axonius uses the [SonarQube Server Web API](https://docs.sonarsource.com/sonarqube-server/latest/extension-guide/web-api/).

### Permissions

**Authentication**:

* All three endpoints require authentication (via Bearer Token).

**Role Requirements**:

* `hotspots/search` and `issues/search` require:
  * The user to have Browse permission on the component/project.
* `rules/show`:
  * Generally accessible to authenticated users, as rules are global and not tied to a specific project.

**Token Scope**:

* A standard user token generated in the SonarQube UI is sufficient.

* For automation, use a token with appropriate project-level access.

#### Supported From Version

Supported from Axonius version 7.0.6

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the SonarQube server.
2. **Token**  - An API Token associated with a user account that has the  Required Permissions to fetch assets.

![SonarQube Server.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SonarQube%20Server.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).