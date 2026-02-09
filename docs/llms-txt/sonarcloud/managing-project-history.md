# Source: https://docs.sonarsource.com/sonarqube-community-build/project-administration/maintaining-project/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/project-administration/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/project-administration/maintaining-project/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-server/project-administration/maintaining-project/managing-project-history.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/managing-project-history.md

# Managing project history

One of the most powerful features of SonarQube Cloud is that it shows you not just your project health today, but how it has changed over time. It does that by selectively keeping data from previous analyses (see the [housekeeping](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/housekeeping "mention") page). It doesn’t keep all previous analyses - that would bloat the database. Similarly, for the analyses it does keep, SonarQube Cloud doesn’t keep all the data. Once a project snapshot moves from the "last analysis", that is, the most recent, to being part of the project’s history, data below the project level is purged - again to keep from bloating the database.

Typically, these aren’t things you need to even think about; SonarQube Cloud just handles them for you, but occasionally, you may need to remove a bad snapshot from a project’s history or change the housekeeping algorithms.

### Managing history <a href="#managing-history" id="managing-history"></a>

Occasionally, you may need to manually delete a project snapshot, whether because the wrong quality profile was used, or because there was a problem with analysis, and so on. Note that the most recent snapshot (labeled "last snapshot") can never be deleted.

**Deleting snapshots**

{% hint style="info" %}
Deleting a snapshot is a 2-step process:

1. The snapshot must first be removed from the project history by selecting **Delete snapshot.** It won’t be displayed anymore on this **History** page but will still be present in the database.
2. The snapshot is actually deleted during the next project analysis.
   {% endhint %}

At the project level, from the front page **Activity** list, choose **Show More** to see the full activity list.

For every snapshot, it is possible to manually:

* Add, rename or remove a version
* Add, rename or remove an event
* Delete the snapshot
