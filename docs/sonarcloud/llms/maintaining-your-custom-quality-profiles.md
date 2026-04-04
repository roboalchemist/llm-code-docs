# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/maintaining-your-custom-quality-profiles.md

# Maintaining quality profiles

You should regularly maintain your organization’s custom quality profiles *that do not inherit from a built-in profile*. The built-in quality profiles are regularly updated to reflect the addition of new rules and the deprecation of existing ones. As a user with Administer Quality Profile permission, you will be notified by email each time a built-in profile is updated. Updates can be introduced through a SonarQube or third-party analyzer upgrade.

To edit a custom quality profile, you need the Administer Quality Profiles permission in your organization or be authorized to manage this particular profile. To delete a custom quality profile, you need the Administer Quality Profiles permission.

### Ensuring your quality profile has all relevant new rules <a href="#ensuring-quality-profile-has-relevant-new-rules" id="ensuring-quality-profile-has-relevant-new-rules"></a>

To ensure that your custom quality profile has all relevant new rules, you can check for the recently added rules and for the stagnant profiles. Stagnant profiles are custom profiles that have not been updated for more than one year.

#### In the Quality Profiles page <a href="#in-the-quality-profiles-page" id="in-the-quality-profiles-page"></a>

To check for recently added rules and stagnant profiles:

1. [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") and go to **Quality profiles**. The right-hand side of the **Quality Profiles** page shows the stagnant profiles and recently implemented rules.
2. To inspect a new rule, select it in the **Recently Added Rules** section.
3. To edit a stagnant profile, select it in the **Stagnant Profiles** section. The quality profile page opens. To add the new rules to your profile, you can now:
   * Either select **\<X> inactive rules** in the **Inheritance** section and then activate the new rules from the list of inactive rules.
   * Or compare the stagnant profile with the built-in profile.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-35e46fdac490182b4a049b0e0252ec5353ea588f%2F61c6cdc7126171fdf4d40b809e30e9735db85971.png?alt=media" alt="When maintaining your quality profile, pay particular attention to the Stagnant Profiles and Recently Added Rules section on the Quality Profiles page." width="563"><figcaption></figcaption></figure></div>

#### In the Rules page <a href="#in-the-rules-page" id="in-the-rules-page"></a>

To check for recently added rules:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Rules** page.
2. In **Filters**, set the **Available Since** criterion.

### Managing the deprecated rules in quality profiles <a href="#managing-deprecated-rues-in-quality-profiles" id="managing-deprecated-rues-in-quality-profiles"></a>

A deprecated rule is a rule that SonarQube will not be supported any more in the near future. A rule may be deprecated if it has become obsolete or if it has been replaced by one or several new rules. When a rule becomes deprecated, it will be deactivated in the corresponding language’s built-in profile and in the profile inheriting from it.

If your custom profile does not inherit from the built-in profile, you should regularly check your quality profiles for deprecated rules as follows:

1\. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page. On the right-hand side of the page, the **Deprecated Rules** section lists the quality profiles containing deprecated rules.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-afc0fc43cdcf13c8197d2a0563bdacb1a1fe842f%2F410ae8486444d9c853b7d9c5b0ad4504103feca1.png?alt=media" alt="When maintaining your quality profile, also pay attention to the Deprecated Rules section on the Quality Profiles page." width="563"><figcaption></figcaption></figure></div>

2\. To manage one of these profiles, select the **\<X> rules** hyperlink under the profile name. The list of deprecated rules in the profile is displayed.

3\. To deactivate a rule, select the respective **Deactivate** button. To deactivate all rules at a time, select **Bulk Change** > **Deacivate in <**&#x59;OUR PROFIL&#x45;**>** in the top tool bar.

### Deleting a quality profile <a href="#deleting-a-quality-profile" id="deleting-a-quality-profile"></a>

To delete a custom quality profile:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page and retrieve the custom quality profile you want to delete.
2. In the top right corner of the quality profile page, select the three-dot button and select **Delete** in the menu. A confirmation dialog opens.
3. Select **Delete**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention")
* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention")
* [creating-a-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile "mention")
* [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention")
* [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention")
* [changing-default-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/changing-default-quality-profile "mention")
* [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention")
* [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention")
