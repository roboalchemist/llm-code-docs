# Source: https://docs.sonarsource.com/sonarqube-community-build/server-update-and-maintenance/update/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/server-update-and-maintenance/upgrade/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-update-and-maintenance/upgrade/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-update-and-maintenance/update/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/server-update-and-maintenance/update/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-update-and-maintenance/update/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-update-and-maintenance/update/release-cycle-model.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/release-cycle-model.md

# Release cycle model

A new version of SonarQube Server is released every two months, with a new Long-Term Active (LTA) version (previously known as LTS) released every year. LTA is a functionally complete version of the product that will receive longer-term support.

This means that there are six releases of SonarQube Server per year, including the LTA version at the beginning of each year.

### Version scheme <a href="#version-scheme" id="version-scheme"></a>

SonarQube Server releases follow the following version scheme:

`YYYY.ReleaseNumber.PatchReleaseNumber`

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/hlESxkBpv2QARlu6hLEA/release-cycle-model-version-scheme.png" alt="Version scheme" width="563"><figcaption></figcaption></figure></div>

{% hint style="info" %}
Up to version 10.8, SonarQube Server followed the `MAJOR.MINOR.PATCH` version scheme.
{% endhint %}

### Support policy <a href="#support-policy" id="support-policy"></a>

The support policy is as follows:

* The latest version receives new features, enhancements, patches, and technical support.
* The latest-1 version receives technical support.
* The latest LTA receives:
  * Patches to fix vulnerabilities or blocker bugs until the next LTA is released.
  * Technical support up to 6 months after the next LTA is released.

The figure below shows the provided support when the latest version is 2025.6.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/zsAfCmWBjU7PMpf8BYRQ/release-cycle-model.png" alt="Active versions when the latest version is 2025.6"><figcaption></figcaption></figure>

### Active versions <a href="#active-versions" id="active-versions"></a>

In order to ensure that you continue to have the best user experience, you need to make sure that you are on an *active version*. An active version of SonarQube Server is a version that is deemed suitable for use and support.

<details>

<summary>How do I know if my SonarQube version is active?</summary>

There are two main ways to check if you are using an active version of SonarQube Server:

1. In SonarQube Server, in the footer next to the version number, you can immediately see if your version is *active* or *no longer active.*

<figure><img src="broken-reference" alt="Version status in the footer of the page on SonarQube Server"><figcaption></figcaption></figure>

2\. Administrators can go to the **Administration** > **System.** As per above, you can see in the footer if you are on an active version.

<figure><img src="broken-reference" alt="Version status on the system page"><figcaption></figcaption></figure>

If there is a new version available, administrators will see a message at the top of the screen prompting you to update to the latest version:

<figure><img src="broken-reference" alt=""><figcaption></figcaption></figure>

</details>

<details>

<summary>Active version definition</summary>

The following count as active versions:

* The latest version of SonarQube Server
* Latest -1
* LTA
* LTA -1, up to 6 months after the new LTA is released and as long as a maximum of 3 versions are active.

</details>

### Related pages

* [SonarQube Server Long Term Active (LTA) and FAQ](https://www.sonarsource.com/products/sonarqube/downloads/lts/)
* [determine-path](https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/update/determine-path "mention")
