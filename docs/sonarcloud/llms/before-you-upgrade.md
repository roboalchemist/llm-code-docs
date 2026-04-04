# Source: https://docs.sonarsource.com/sonarqube-server/9.8/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/before-you-upgrade.md

# Before you upgrade

This page contains some concepts and recommendations that you should familiarize yourself with before upgrading. See the [upgrade-guide](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/upgrade-the-server/upgrade-guide "mention") for information on the actual upgrade process.

### SonarQube version number format <a href="#sonarqube-version-number-format" id="sonarqube-version-number-format"></a>

Version numbers have up to three digits with each digit representing part of the release cycle:

![Picture explaining how to read the SonarQube version number format](https://353248219-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fl622HnhaCz6xSuy6XTfl%2Fuploads%2Fgit-blob-ac551b020ae3c344c36c234e5e76be3c89991ac1%2F01b6635d5a4fb4b0c86b6c6c3839bf1840a64b36.png?alt=media)

Picture explaining how to read the SonarQube version number format

**Major version number**

The major version number represents a series of releases with high-level objectives for the release cycle. It’s incremented with the release following an LTS version (for example, the release following 7.9 LTS was 8.0).

**Minor version number**

The minor version number corresponds to incremental functional changes within a major release cycle. At the time of an LTS release, the release cycle is closed and the minor version number is frozen.

**Patch release number**

The patch release number represents patches that fix blockers and critical problems.

### Migration path <a href="#migration-path" id="migration-path"></a>

Upgrading across multiple non-LTS versions is handled automatically. However, if there are one or multiple LTS versions in your migration path, you must first migrate to each intermediate LTS and then to your target version, as shown in the example below.

When upgrading to an LTS version, you should directly upgrade to its latest patch. This allows you to make sure everything runs well (see Practice your upgrade section below) with that patch.

You can upgrade from the latest LTS version to the latest non-LTS version directly. See the example below.

{% hint style="info" %}
If you’re migrating from an earlier patch version of an LTS, you can upgrade directly to the next LTS. You don’t need to install any intermediate patch versions.
{% endhint %}

**Migration path examples**:

**LTS > LTS (1)** – From 8.9 LTS > 9.9 LTS, the migration path is 8.9 LTS > 9.9 LTS\
**LTS > LTS** **(2)** – From 7.9 LTS > 9.9 LTS, the migration path is 7.9 LTS > 8.9 LTS > 9.9 LTS\
**LTS > non-LTS** – From 9.9 LTS > 10.1, the migration path is 9.9 LTS > 10.1\
**Non-LTS > LTS** – From 9.6 > 9.9 LTS, the migration path is 9.6 > 9.9 LTS\*\*\
Non-LTS > LTS > non-LTS\*\* – From 9.6 > 10.1, the migration path is 9.6 > 9.9 LTS > 10.1

### Release upgrade notes <a href="#release-upgrade-notes" id="release-upgrade-notes"></a>

SonarQube releases come with some specific recommendations for upgrading from the previous version. You should read the [release-upgrade-notes](https://docs.sonarsource.com/sonarqube-server/10.3/setup-and-upgrade/release-upgrade-notes "mention") for each version between your current version and the target version.

### Practice your upgrade <a href="#practice-your-upgrade" id="practice-your-upgrade"></a>

We recommend practicing your upgrade to:

* make sure your infrastructure can run the upgrade.
* get an idea of how long the upgrade will take.
* gain a better understanding of the upgrade process and anticipate what you’ll need to do when performing the actual upgrade.
* address any issues you encounter during the practice upgrade on the [Sonar community](https://community.sonarsource.com/).

To practice your upgrade, create a staging environment using a recent backup of your production database. You want your staging environment to be as similar to your production instance as possible because the resources and time needed to upgrade depends on what’s stored in your database. Use this staging environment to test the upgrade, observing how long it takes to back up and restore systems and complete the process.

You can use our calculator to help determine your update path.

{% @sonar-embeds/upgrade-calculator fullWidth="true" %}
