# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/upgrade-the-server/testing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/upgrade-the-server/testing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/testing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/testing.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/testing.md

# Testing the upgrade

We recommend testing your upgrade to:

* Make sure your infrastructure can run the upgrade.
* Get an idea of how long the upgrade will take.
* Gain a better understanding of the upgrade process and anticipate what you’ll need to do when performing the actual upgrade.
* Address any issues you encounter during the practice upgrade on the Sonar community.

To test your upgrade:

1. Create a staging environment using a recent backup of your production database. You want your staging environment to be as similar to your production instance as possible because the resources and time needed to upgrade depends on what’s stored in your database.
2. Use this staging environment to test the upgrade.
3. Observe how long it takes to back up and restore systems and complete the process.
