# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association.md

# Quality profile

If you do not explicitly associate a language with a specific quality profile in your project, the default quality profile will be used for the analysis of this language’s code. To change a quality profile association in your project, you need the Administer permission on the project.

{% hint style="info" %}
With the Administer Quality Profiles permission, you can change the associations of a profile for any project. This is done from the respective quality profile. In addition, you can delegate this permission to any user for a given custom quality profile. See [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention") for more information.
{% endhint %}

To associate another quality profile to a language in your project:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more details.
2. In the left-side panel, select **Administration** > **Quality Profiles**.
3. Select another profile for the language.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-26f487377f287b512e256ddfcab08c22655578fb%2F19220466033d08e65e4869e11264d0403350dace.png?alt=media" alt="Navigate to Your Project > Administration > Quality profiles to see a list of langages and their assigned Quality Profiles."><figcaption></figcaption></figure></div>
