# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/update/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/upgrade-the-server/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/upgrade-the-server/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/determine-path.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/determine-path.md

# Determining the update path

This section explains the principles to follow to determine whether you can perform the update directly or must update first to an intermediate version(s). To understand the principles, you must first understand the [release-cycle-model](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model "mention").

To determine your update path, consider the following principles:

* You can update directly from a non-LTA version to another if there is no LTA version in your update path.
* If there is at least one LTA version in your update path, you must first update to each intermediate LTA and then to your target version.
* When upgrading to an LTA version, you should directly update to its latest patch.
* You can update from the latest LTA version to the latest non-LTA version directly.
* If you’re migrating from an earlier patch version of an LTA, you can update directly to the next LTA. You don’t need to install any intermediate patch versions.
* There is no LTA concept for SonarQube Community Build.

### Update path examples <a href="#path-examples" id="path-examples"></a>

| From version | To version | Update path                                               |
| ------------ | ---------- | --------------------------------------------------------- |
| 2025.1 LTA   | 2026.1 LTA | 2025.1 LTA > 2026.1 LTA (direct)                          |
| 9.9 LTA      | 2026.1 LTA | 9.9 LTA > 2025.1 LTA > 2026.1 LTA (one intermediate step) |
| 9.9 LTA      | 2025.4 LTA | 9.9 LTA > 2025.1 LTA > 2025.4 LTA (one intermediate step) |
| 9.9 LTA      | 2025.1 LTA | 9.9 LTA > 2025.1 LTA (direct)                             |
| 8.9          | 2025.1 LTA | 8.9 LTA > 9.9 LTA > 2025.1 LTA (one intermediate step)    |
| 2025.1 LTA   | 2025.3     | 2025.1 LTA > 2025.3 (direct)                              |
| 10.6         | 2025.1 LTA | 10.6 > 2025.1 LTA (direct)                                |
| 10.6         | 2025.3     | 10.6 > 2025.1 LTA > 2025.3 (one intermediate step)        |

### Update path calculator

You can use our calculator to help determine your update path.

{% @sonar-embeds/upgrade-calculator %}
