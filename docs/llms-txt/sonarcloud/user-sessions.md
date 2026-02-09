# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/security/user-sessions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/security/user-sessions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/security/user-sessions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/security/user-sessions.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/security/user-sessions.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/security/user-sessions.md

# User sessions

A user’s session will automatically end after a period of inactivity. This feature is called inactive session timeout. This is a security measure to prevent unauthorized access to sensitive data if a user leaves their computer unattended. SonarQube will log the user out after the timeout period. By default, the inactive session timeout is 3 days. You can change it.

The active session timeout is supported starting in [Enterprise edition](https://www.sonarsource.com/plans-and-pricing/enterprise/). An active session timeout means a user’s session will automatically end after a period of time, regardless of activity. SonarQube will log the user out after the timeout period even if the user is actively using the system. By default, the active session timeout is 90 days. You can change it.

To configure the user session timeouts, set the following sonar properties in `<sonarqubeHome>/conf/sonar.properties`. If applicable, you can use the environment variable instead.

<table><thead><tr><th width="337">System property (sonar property and ENVIRONMENT_VARIABLE)</th><th>Description</th></tr></thead><tbody><tr><td><p>sonar.web.sessionTimeoutInMinutes</p><p>SONAR_WEB_SESSIONTIMEOUTINMINUTES</p></td><td><p>Inactive session timeout (in minutes). The maximum time a user can remain idle (no activity) before the session ends. If the user does not interact with the system within this time, they are logged out.</p><p><strong>Default value</strong>: <code>4320</code> (3 days)</p><p><strong>Minimum value</strong>: <code>6</code></p><p><strong>Maximum value</strong>: <code>129 600</code> (90 days)</p></td></tr><tr><td>sonar.web.activeSessionTimeoutInMinutes</td><td><p>This property is supported starting in <a href="https://www.sonarsource.com/plans-and-pricing/enterprise/">Enterprise edition</a>.</p><p>Active session timeout (in minutes). The maximum time a user can remain logged in, regardless of activity. After this time, the session ends automatically even if the user is actively using the system.</p><p><strong>Default value</strong>: <code>129 600</code> (90 days)</p><p><strong>Minimum value:</strong><code>15</code></p><p><strong>Maximum value</strong>: <code>129 600</code> (90 days)</p></td></tr></tbody></table>
