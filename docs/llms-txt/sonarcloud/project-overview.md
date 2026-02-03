# Source: https://docs.sonarsource.com/sonarqube-community-build/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/viewing-projects/project-overview.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/project-overview.md

# Viewing analysis summary

The project overview page allows you to view:

* The releasability status of the project.
* The current state of its quality.
* The quality of what has been produced since the start of your new code.

and answers two questions:

* Can I release my project today?
* If I cannot release it today, what should I improve to make the project pass its quality gate?

To open the project overview page:

* Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/retrieving-projects "mention") for more information. The **Overview** page opens. This page contains the following sections:

<details>

<summary>Quality gate status</summary>

The quality gate is your most powerful tool to enforce your quality policy. If the project passes, the **Quality Gate Status** will show a simple, green all-clear banner. See [introduction-to-quality-gates](https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates "mention") for more information.

If not, details and drill-downs are immediately available to quickly identify what went wrong. A section for each error condition shows the current project value and what it should be. As usual, you’ll be able to click through on current values to get more details about each issue.

</details>

<details>

<summary>Measures</summary>

In this section, you see all project measures. Select a measure for more details. Both list and tree views are available for each measure, and tree maps are available for percentages and ratings.

</details>

<details>

<summary>Activity</summary>

This section contains the full list of code scans performed on your project since it was created in SonarQube Server. By going there, you can follow the evolution of the quality gate, see the changes in quality profiles, discover when a given version of your code has been scanned, and more.

See also [activity-and-history](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/activity-and-history "mention").

</details>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-project-structure](https://docs.sonarsource.com/sonarqube-server/user-guide/viewing-projects/viewing-project-structure "mention")
* [managing-tokens](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-tokens "mention")
* [project-badge](https://docs.sonarsource.com/sonarqube-server/user-guide/project-badge "mention")
* [subscribing-to-notifications](https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/subscribing-to-notifications "mention")
* [introduction](https://docs.sonarsource.com/sonarqube-server/user-guide/issues/introduction "mention")
* [security-hotspots](https://docs.sonarsource.com/sonarqube-server/user-guide/security-hotspots "mention")
