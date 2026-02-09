# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/inactive-projects.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/inactive-projects.md

# Inactive projects

Projects that are not analyzed for seven consecutive days are considered inactive, and SonarQube Server automatically deletes their cached data to free space in the database. See [maintaining-the-branches-of-your-project](https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/maintaining-the-branches-of-your-project "mention") for more information on inactive branches and cached data.

The **Projects Management** search interface includes a date picker to help you find all projects last analyzed before your specified date. From there you can deal with them on this page as a set, or click through to the individual project homepages for individual attention and administration.

In **Administration** > **Projects** > **Management** search for **Last analysis before** to filter projects not analyzed since a specific date. Then use bulk **Delete** to remove the projects that match your filter.

This can be automated by using the corresponding Web API: `api/projects/bulk_delete?analyzedBefore=YYYY-MM-DD`.
