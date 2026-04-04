# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/housekeeping.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/housekeeping.md

# Housekeeping

SonarQube Cloud retains project analysis data to allow tracking of the evolution of a project, but progressively deletes older information, including source code, measures, and most snapshots over time. Specific retention policies apply to PR data, background tasks, and issues, with projects on a free plan being deleted after one year of inactivity. SonarQube Cloud’s data retention policy is outlined below.

### Data retention policy <a href="#data-retention-policy" id="data-retention-policy"></a>

After each analysis the following is removed:

* The source code of the previous analysis.
* Measures at the directory and file levels.
* History at the package/directory level.

**PR data** is retained for four weeks after analysis. **Background tasks** are retained for 6 months. Additionally, for each project, **snapshots** of analyses (main branch, non-main branch, and pull request) are retained or removed according to the following rules:

* All snapshots are retained for one day.
* After one day, only one snapshot per day is retained.
* After one week, only one snapshot per week is retained.
* After 4 weeks, only one snapshot for every 4 weeks is retained.

In all the above cases, in addition to the single snapshot retained at each step, any snapshots marked by an event are also retained. See the [managing-project-history](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/managing-project-history "mention") page for information on events.

Continuing on:

* After 2 years, only snapshots with version events are retained. Snapshots without events or with only non-version events are deleted.
* After 5 years all snapshots are deleted, including snapshots marked by version events.

Separately:

* All closed issues more than 30 days old are deleted.
* Projects in organizations on a **Free plan** that have not been analyzed for one year are automatically deleted. This also applies to projects that were created one year previously but were never analyzed. Users receive notifications of this event on the SonarQube Cloud project interface four weeks before the deletion will take place.
* Scoped Organization Tokens without an expiration date that have been inactive for 60 days are deleted.
* Personal Access Tokens that have been inactive for 60 days are deleted.

These settings cannot be customized.
