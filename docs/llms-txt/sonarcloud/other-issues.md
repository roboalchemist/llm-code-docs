# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/troubleshooting/other-issues.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/other-issues.md

# Other issues

### Issues with IIS and SAML integration <a href="#iis-through-saml" id="iis-through-saml"></a>

If you are using an IIS reverse proxy with SAML authentication, you may encounter one of the following issues:

* The URL redirection to the SAML Identity Provider (sonar.auth.saml.loginUrl) is not managed correctly.
* "You are not authorized to access this page" error is raised when logging in.

In that case, make sure that, at the IIS server level, you have performed all the configuration steps described in the [#using-iis-on-windows](https://docs.sonarsource.com/sonarqube-server/server-installation/network-security/securing-behind-proxy#using-iis-on-windows "mention") section.

### Issue with downloading regulatory reports <a href="#regulatory-reports" id="regulatory-reports"></a>

If nothing happens when you try to download a regulatory report (in the SonarQube Server UI at **Project Information > Regulatory Report**) and your SonarQube Server is deployed on Kubernetes, the issue could be your download speed or the report size. To fix this, increase your body size and connection timeout Ingress settings as follows:

```css-79elbk
annotations:
    cert-manager.io/cluster-issuer: sectigo
    nginx.ingress.kubernetes.io/proxy-body-size: "64m"
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "300"
```

### Invalid destination error <a href="#invalid-destination-error" id="invalid-destination-error"></a>

To help you find out what the issue is, check the valid destination in the log file as follows:

1. Set the log level to **`DEBUG`**. See [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention") for more information.
2. Check the `web.log` file for the `valid recipient` as illustrated below.

```css-79elbk
Failed to match SubjectConfirmationData@Recipient to any supplied valid recipients: [http://localhost:9000/oauth2/callback/saml]
```

### IIS 10 on Windows: running SonarQube as a service raises an error <a href="#iis-on-windows-sonarqube-as-a-service" id="iis-on-windows-sonarqube-as-a-service"></a>

If you’ve secured your SonarQube Server instance behind a proxy by using IIS 10 on Windows and the error `WinSW.CommandException: Failed to open the service control manager database. Access is denied —> System.ComponentModel.Win32Exception: Access is denied` is raised when you try to run SonarQube as a service, try the following:

* In IIS, disable **Dynamic Restriction Settings** which come enabled by default under the **IP Address and Domain Restrictions** feature.

### SonarQube on AWS ECS: startup fails with unknownhostexception <a href="#aws-ecs-startup-fails" id="aws-ecs-startup-fails"></a>

If your SonarQube, installed on AWS ECS, fails to start up with `unknownhostexception`, try the following:

* Check if the ECS container is running in network bridge mode and change it to host mode.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [server-logs](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/server-logs "mention")
* [performance-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/performance-issues "mention")
* [database-related-issues](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/database-related-issues "mention")
* [elasticsearch](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/troubleshooting/elasticsearch "mention")
