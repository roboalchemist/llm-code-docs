# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-settings.md

# Changing organization settings

You must be an organization admin to perform the procedures described below.

### Changing organization details <a href="#change-details" id="change-details"></a>

You can:

* Change the organization name displayed on SonarQube Cloud UI.
* Add or change the avatar. The avatar is a small image representing the organization and displayed on the UI near the organization’s name.
* Add or change the organization description.
* Add or change the URL of the homepage of the organization displayed on the UI.

Proceed as follows:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
2. Go to **Administration** > **Organization settings** > **General** > **Organization details**.
3. Edit the field value(s).
4. Select **Save**.

### Changing the organization key <a href="#change-key" id="change-key"></a>

The organization key is set when you import the organization into SonarQube Cloud. At that point, you can choose your own key or accept the suggested key. In some cases, you may later wish to change this key (for example, if a new naming convention is adopted at your company, or if you initially chose a bad key by accident).

{% hint style="info" %}
The organization key is used in CI-based analysis setups to link the analysis produced by the scanner in your local or cloud-based build environment with the correct organization in SonarQube Cloud. It appears as the value of the `sonar.organization` parameter in your analysis configuration.
{% endhint %}

To change the key of your organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
2. Go to **Administration** > **Organization settings** > **General** > **Edit organization key**.
3. In **Key**, enter your new key, and select **Save**.
4. Make the same change to the `sonar.organization` setting of every project in the organization that is configured for CI-based analysis, or inform the respective project administrators.

### Allowing only private projects in an organization <a href="#allow-only-private-projects" id="allow-only-private-projects"></a>

By default, the visibility of newly created projects is set to private on Free, Team and Enterprise plans. However, In a Team or Enterprise plan organization, you can restrict project creation to private projects only. If public projects belong to the organization, you must make them private first, see [setting-permissions](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/administering-your-projects/setting-permissions "mention").

To allow only private projects in your organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
2. Go to **Administration** > **Organization settings** > **General** > **Only allow private projects**.
3. Select the **Only allow private projects** checkbox.
4. Select **Save**.

### Changing the token used to connect to GitLab or Azure DevOps organization <a href="#change-pat" id="change-pat"></a>

To change the personal access token used to connect to your GitLab or Azure DevOps organization:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more information.
2. Go to **Administration** > **Organization settings** > **Organization binding**.
3. In **Current binding**, select the **Edit token** button.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [binding-unbound-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/binding-unbound-organization "mention")
* [importing-github-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-github-organization "mention")
* [importing-bitbucket-workspace](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-bitbucket-workspace "mention")
* [importing-gitlab-group](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-gitlab-group "mention")
* [importing-azure-devops-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-azure-devops-organization "mention")
* [creating-organization-manually](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/creating-organization-manually "mention")
* [changing-organization-binding](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/changing-organization-binding "mention")
* [deleting-organization](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/deleting-organization "mention")
* [importing-from-multiple-platforms](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-organization/creating-organization/importing-from-multiple-platforms "mention")
