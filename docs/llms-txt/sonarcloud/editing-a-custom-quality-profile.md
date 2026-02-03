# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/editing-a-custom-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile.md

# Editing a quality profile

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

Those with the Administer Quality Profiles permission and Users authorized to manage a particular profile have full control of the quality profile's definition. These users can rename a profile, change its parent, activate and deactivate rules, as well as customize a rule's parameters within that quality profile.

### Activating rules in a quality profile <a href="#activating-rules-in-quality-profile" id="activating-rules-in-quality-profile"></a>

You can activate rules in any custom quality profile.

#### Activating a single rule <a href="#activating-a-single-rule" id="activating-a-single-rule"></a>

When you activate a single rule, you can customize the rule configurable parameters (if any) in the quality profile.

To activate a single rule in a custom quality profile (from the quality profile’s page):

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page.
2. Locate the quality profile’s row and display the list of available rules as follows:
   * Either select the three-dot button in the far right of the row, and select **Activate more rules** in the menu.
   * Or select the profile and, in the profile page, select the **Activate more** button at the bottom of the **Rule breakdown** section.
3. To activate a single rule, select **Activate** at the far right of the rule row. The **Activate in Quality Profile** dialog opens.
4. If necessary, customize the rule parameters.
5. Select **Activate**.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-68c14ca854bac275f64f1a5522af58220169e482%2F7db33ece7aa59d56db2e4c4d89538b14522c4121.png?alt=media" alt="To add a rule to your quality profile in SonarQube Cloud, select Activate from any rule in your list of Inactive rule rules." width="563"><figcaption></figcaption></figure></div>

To activate a single rule in a custom quality profile (from the rule’s page):

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Rules** page and retrieve your rule.
2. On the **Rules** page, navigate to the bottom to the **Quality Profiles** section.
3. In front of **Quality Profiles**, select **Activate**. The **Activate rule in Quality Profile** dialog opens.
4. In **Quality Profile**, select the quality profile. Note that if the rule is active in all profiles except one, this profile will be automatically selected in the dialog.
5. Customize the rule parameters if applicable and necessary.
6. Select **Activate**.

#### Activating all inactive rules <a href="#activating-all-inactive-rules" id="activating-all-inactive-rules"></a>

To activate all inactive rules in a custom quality profile:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page and retrieve your quality profile.
2. At the bottom of the **Rule breakdown** section, select **Activate more**. The list of inactive rules is displayed.
3. In the top tool bar, select **Bulk Change** > **Activate in <**&#x59;OUR PROFIL&#x45;**>**. A confirmation dialog opens.
4. Confirm.

#### Activating rules from a profile comparison <a href="#activating-rules-from-a-profile-comparison" id="activating-rules-from-a-profile-comparison"></a>

When you compare two profiles, you can activate a rule from the comparison results. See the [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention") to learn about comparing profiles.

### Deactivating rules in a quality profile <a href="#deactivating-rules-in-a-quality-profile" id="deactivating-rules-in-a-quality-profile"></a>

You can deactivate rules in any custom quality profile.

To deactivate rules in a custom quality profile (from the quality profile’s page):

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page and retrieve your quality profile.
2. In the **Inheritance** section, select the **X active rules** hyperlink. The list of active rules displayed.
3. To deactivate a single rule, select **Deactivate** at the far right of the rule row.
4. To deactivate all active rules, select **Bulk Change** > **Deactivate in <**&#x59;OUR PROFIL&#x45;**>** in the top tool bar.

To deactivate a single rule in a custom quality profile (from the rule’s page):

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Rules** page and retrieve your rule.
2. On the rule page, navigate to the bottom, in the **Quality Profiles** section.
3. In front of the custom quality profile, select **Deactivate**.

### Customizing a rule’s parameters in a quality profile <a href="#customizing-rule-parameters" id="customizing-rule-parameters"></a>

In a custom quality profile, you can customize the rule’s configurable parameters (if any). If the quality profile inherits from a parent profile, the rule is considered *overridden*.

You can perform this operation during the rule activation in the quality profile or later as explained below:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Rules** page and retrieve your rule.
2. On the **Rules** page, navigate to the bottom to the **Quality Profiles** section.
3. In front of the custom quality profile, select **Change**. The Change details of quality profile dialog opens.
4. Change the parameter value(s).
5. Select **Save**.

### Renaming a quality profile <a href="#renaming-a-quality-profile" id="renaming-a-quality-profile"></a>

You can rename any custom quality profile.

To rename a quality profile:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page and retrieve your quality profile.
2. Select the three-dot button.
3. Select **Rename**. the **Rename Profile** dialog opens.
4. Enter the new name and select **Rename**.

### Changing the parent of a quality profile <a href="#changing-parent-of-quality-profile" id="changing-parent-of-quality-profile"></a>

You can change or remove the existing parent, or you can add a parent to a custom quality profile. To do so:

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page and retrieve your quality profile.
2. In the **Inheritance** section of the quality profile, select **Change parent**. The **Change Parent** dialog opens.
3. In the dialog, select the new parent or **None** to remove the inheritance.
4. Select **Change**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention")
* [creating-a-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile "mention")
* [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention")
* [changing-default-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/changing-default-quality-profile "mention")
* [maintaining-your-custom-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/maintaining-your-custom-quality-profiles "mention")
* [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention")
* [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention")
