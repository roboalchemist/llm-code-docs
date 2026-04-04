# Source: https://docs.sonarsource.com/sonarqube-server/9.9/setup-and-upgrade/upgrade-the-server/active-versions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/upgrade-the-server/active-versions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/upgrade-the-server/active-versions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/server-upgrade-and-maintenance/upgrade/upgrade-the-server/active-versions.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/active-versions.md

# Active versions

In order to ensure that you continue to avail of the best user experience, you need to make sure that you are on an *active version*. An active version of SonarQube Server is a version that is deemed suitable for use and support and will provide you with the best user experience, given how often you upgrade. Ensuring you are on an active version allows you to benefit from different levels of support from Sonar:

* New features - your organizations gain immediate access to all new capabilities released, as well as to continuous product improvements. This leads to a better user experience and improved developer productivity (LTA and latest versions only).
* Patch releases - users on the LTA and latest versions have immediate access to bug fixes and security patches from Sonar. Users on non-active versions don’t receive these patches so are at increased risk of operational issues.
* Technical support - all organizations receive [troubleshooting](https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/troubleshooting "mention") support and technical assistance from Sonar, addressing problems quickly and minimizing downtime.

### Examples of active versions <a href="#examples-of-active-versions" id="examples-of-active-versions"></a>

LTA (Long-Term Active) refers to the version of SonarQube Server that is released approximately every 18 to 24 months (previously known as LTS). It is a version of the product that is functionally complete and will stay active for a longer period of time.

The following count as active versions:

* Latest version of SonarQube Server, for example, 10.4
* Latest -1, for example, 10.3
* LTA, for example, 9.9
* LTA -1, for example, 8.9. This is only supported for a period of six months after the LTA is launched to allow you sufficient time to transition and upgrade.

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-4da1962984a9123283577a875d0693bf0dad6fab%2F4fa9163f24280edc1721804c0fd3872eda48e80d.png?alt=media)

### Checking if your version is active <a href="#checking-if-your-version-is-active" id="checking-if-your-version-is-active"></a>

There are two main ways to check if you are using an active version of SonarQube Server:

1. In SonarQube Server, in the footer next to the version number, you can immediately see if your version is *active* or *no longer active.*

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-8bc7433789dc03c71de054e4fb4d173aa583825e%2Fcbda1a4df7138887e4e0548a0d2377898f233684.png?alt=media)

2\. Administrators can go to the **Administration** > **System.** As per above, you can see in the footer if you are on an active version.

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-1618b050676431ef42157f60d01018aa72561872%2F95f18460116c475ed90fcb8e4c435e8e14069c44.png?alt=media)

If there is a new version available, administrators will see a message at the top of the screen prompting you to upgrade to the latest version:

![](https://312504542-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiJj3TXBdWssTGGg8qK5I%2Fuploads%2Fgit-blob-4b2bd648cb11bcabbc09e72b83a10356d2e78ac5%2F44de237e30e0f589b78e342b531a26a0f21f814d.png?alt=media)

### Reasons to upgrade immediately <a href="#reasons-to-upgrade-immediately" id="reasons-to-upgrade-immediately"></a>

In SonarQube Server, you need to perform an upgrade in the following situations:

1. If you are on a version of SonarQube Server that is no longer active.
2. If you are on the latest version of SonarQube Server and there is a new upgrade available.
3. If you are on the latest version or LTA for which there is a new patch version available (security and bug fixes).

### Learn more <a href="#learn-more" id="learn-more"></a>

For information on how to upgrade to and from an LTA, see [determine-path](https://docs.sonarsource.com/sonarqube-server/10.8/server-upgrade-and-maintenance/upgrade/upgrade-the-server/determine-path "mention").
