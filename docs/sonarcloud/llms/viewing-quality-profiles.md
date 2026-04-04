# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/viewing-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles.md

# Viewing quality profiles

For information about the how a quality profile works, see the [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") page.

### Retrieving quality profiles <a href="#retrieving-quality-profiles" id="retrieving-quality-profiles"></a>

See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization and navigate to **Quality Profiles**. The **Quality Profiles** page opens with:

1. On the left-hand side, you will see a list of profile sets by language. Quality profiles inherited from a parent profile are displayed under their parent and with a left indent.\
   This list includes the following columns:
   * The **Projects** column shows the count of projects associated with a quality profile. Alternatively, it displays **`DEFAULT`** when the profile is the language’s default (any profile not explicitly associated with a quality profile is associated with the organization’s default profile).
   * The **Rules** column shows the total count of active rules within the profile. Additionally, if any of these active rules are deprecated, their number will also be indicated with a pink background.
   * The **Updated** column shows when the quality profile was last updated.
   * The **Used** column shows when the quality profile was last used during a project analysis.
2. On the right-hand side, you will see different sections with information relating to details associated with existing quality profiles:
   * The **Deprecated Rules** section lists the quality profiles that contain deprecated rules.
   * The **Recently Added Rules** section lists newly added rules and shows whether they are currently active in each profile.
   * The **Stagnant Profiles** section lists the custom profiles that have not been updated for more than one year.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-0fbd005ed43c8956bf27a7af48dd8ecf7b174e82%2F09ffcee7abca388e8d81ac6b6fce9c786c156e8e.png?alt=media" alt="The SonarQube Cloud UI displays information relating to your organization&#x27;s quality profiles."><figcaption></figcaption></figure></div>

### Viewing a quality profile <a href="#viewing-a-quality-profile" id="viewing-a-quality-profile"></a>

On the **Quality Profiles** page:

1. To view a specific language, select a language in **Filter by** at the top of the left-hand side list of quality profiles.
2. Select the quality profile you want to view. The quality profile is displayed as illustrated below.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e778cf93b229ee53ff602b7cc353f9c82faaf9f5%2F15b27c8d43c5ce51f4cd1c9fadce603cd90aec64.png?alt=media" alt="Once a quality profile is selected for viewing, SonarQube Cloud presents the profile&#x27;s inheritance status along with a Rule breakdown and list of Projects that use this profile."><figcaption></figcaption></figure></div>

The quality profile page includes the following sections:

1. **Inheritance**: shows the quality profile with its possible parent(s) and / or children. For each profile, the number of active, inactive, and overridden rules in the profile is shown. Select a number to view the corresponding list of rules.
2. **Projects**: shows the projects explicitly associated with the quality profile.
3. **Rule breakdown**: shows statistics about active and inactive rules contained in the quality profile. Select a statistic to view the corresponding rules.

If you have the Administer Quality Profiles permission, you will also see a **Permissions** section under the **Projects** section. The **Permissions** section shows the users and groups authorized to manage this quality profile.

### Comparing quality profiles <a href="#comparing-quality-profiles" id="comparing-quality-profiles"></a>

You can compare quality profiles of the same language.

To compare one profile with another:

1. In the SonarQube UI, retrieve one of the quality profiles you want to compare (quality-profile-1).
2. In the top right corner of the quality profile page, select the three-dot button, and select **Compare** in the menu. The comparison page opens.
3. In **Compare with**, select the profile to be compared to (quality-profile-2). The comparison results are displayed on the page as illustrated below. The left column corresponds to quality-profile-1 and the right column to quality-profile-2. In the comparison results, you can select a rule to inspect it.

In the example shown below, the comparison reveals the following differences between the two example profiles: **My ABAP profile** and **Sonar way**.

1. In part 1, the first column shows that **My ABAP profile** includes one rule that **Sonar way** excludes. In the second column shows that **My ABAP profile** excludes two rules that **Sonar way** includes.
2. In part 2, one rule has a different configuration in **My ABAP profile** that it does in the **Sonar way**.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-99171780fd7cfb0676905067d5f1993ed7aa0de3%2F931a0e5e3072188c6e8d0e6ec24b984dfe5dfe87.png?alt=media" alt="SonarQube Cloud presents an organized list of differences to help you comparing two quality profiles."><figcaption></figcaption></figure>

### Viewing the overridden rules of a quality profile <a href="#viewing-overrridden-rules" id="viewing-overrridden-rules"></a>

A rule is considered overridden in a custom quality profile if this profile defines, for this rule, different configurable parameters than its parent quality profile.

To view the overridden rules of a quality profile:

1\. Retrieve the quality profile as described above. The number of overridden rules in the profile (if any) is shown in the **Inheritance** section.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-6afa2aeda11011ca9896855e9d35c776608c49c4%2F63db79088f433eb134bec661f51be9a3dc083216.png?alt=media" alt="The number of overridden rules existing in your quality profile are displayed in the right-most column."><figcaption></figcaption></figure>

2\. Select the **<*****X*****> overridden rules** hyperlink. The list of overridden rules is displayed.

3\. In the list, select a rule on the **Rules** page and navigate to the **Quality Profiles** section to **Change**, **Revert**, or **Deactivate** the rule completely.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-ea86634bf29f9201031ced5eb0ad26fb373fb9e5%2F4daf1802b93a2814c67e477941325d6089eaa7fb.png?alt=media" alt="SonarQube Cloud will provide actions to Change, Revert, or Deactivate overridden rules when you select it from the Quality Profiles section of the Rules page."><figcaption></figcaption></figure>

### Viewing the change history of a quality profile <a href="#viewing-change-history-of-quality-profile" id="viewing-change-history-of-quality-profile"></a>

1. Retrieve the quality profile as described above.
2. In the top right corner of the profile page, select **See Changelog**. The profile change history opens and lists the different actions performed on rules in the quality profile:
   * **Date**: action date.
   * **User**: user who performed the action.
   * **Action**: action type (the user activated, deactivated, or updated the rule).
   * **Rule**: rule on which the action was performed.
   * **Updates**:
     * For an Updated action: describes the update.
     * For an Activated action: shows the rule’s severity level.

### Viewing the projects associated with a quality profile <a href="#viewing-projects-associated-with-a-quality-profile" id="viewing-projects-associated-with-a-quality-profile"></a>

The **Projects** section of a quality profile shows the projects associated with the profile. See **Retrieving a quality profile** above.

### Viewing the quality profiles where a rule is active <a href="#viewing-quality-profiles-where-a-rule-is-active" id="viewing-quality-profiles-where-a-rule-is-active"></a>

To view the quality profiles where a given rule is active:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization.
2. Go to the **Rules** page and retrieve the rule.
3. In the rule page, navigate to the bottom to the **Quality Profiles** section. The section lists all quality profiles where the rule is active.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [creating-a-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile "mention")
* [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention")
* [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention")
* [changing-default-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/changing-default-quality-profile "mention")
* [maintaining-your-custom-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/maintaining-your-custom-quality-profiles "mention")
* [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention")
* [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention")
