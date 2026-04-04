# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/creating-a-quality-profile.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile.md

# Creating a quality profile

*This feature is only available in the Team and Enterprise plans. See* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") *for more information.*

The Sonar way profile is intended as a starting point. In many cases, you will want to adjust your quality profile later.

If you have multiple projects, you might also need to have different profiles for each. You might run into the following situations:

* You have different technical requirements from one project to another.
* You want to ensure stronger requirements for some of your projects than for others.

To create a quality profile, you need the Administer Quality Profiles permission. You can:

* Extend an existing quality profile (duplicate an existing profile with inheritance).
* Copy an existing quality profile (duplicate an existing profile without inheritance).
* Create a quality profile from scratch.
* Import a quality profile from another SonarQube instance.

We highly recommend that you customize your profiles by extending the Sonar way profile. This allows you to manage most use cases. Indeed, if your profiles inherit from the Sonar way profile, you will automatically benefit from:

* Newly implemented rules.
* Changes in a rule’s configuration.
* The deactivation of deprecated rules.

### Extending a quality profile <a href="#extending-a-quality-profile" id="extending-a-quality-profile"></a>

When you extend a profile, you create a child profile that inherits all the *activated* rules in the parent profile. You can then activate additional rules in the child, beyond those that are inherited. You can also deactivate rules that are activated in the parent.

For more information about inheritance, check out the [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention") page.

#### By using the Create button <a href="#by-using-the-create-button" id="by-using-the-create-button"></a>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, then go to the **Quality Profiles** page.
2. In the top right corner of the page, select **Create**. The **New Quality Profile** page opens.
3. In **Name**, enter the name of the new quality profile.
4. In **Language**, select the language of the new quality profile.
5. In **Parent**, select the quality profile you want to extend.
6. Select **Create**.

To change the created profile, see [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention").

#### From the parent profile’s menu <a href="#from-the-parent-profiles-menu" id="from-the-parent-profiles-menu"></a>

1. See the [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention") page to learn how to select the quality profile that you want to extend.
2. Select the three-dot button and select **Extend** in the menu. The **Extend Profile** dialog opens.
3. In **New name**, enter the name of the new quality profile.
4. Select **Extend**.

To change the created profile, see [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention").

### Copying a quality profile <a href="#copying-a-quality-profile" id="copying-a-quality-profile"></a>

1. See the [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention") page to learn how to select the quality profile that you want to copy.
2. Select the three-dot button and select **Copy** in the menu. The **Copy Profile** dialog opens.
3. In **Name**, enter the name of the new quality profile.
4. Select **Copy**.

To change the created profile, see the instructions on the [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention") page.

### Creating a quality profile from scratch <a href="#creating-a-quality-profile-from-scratch" id="creating-a-quality-profile-from-scratch"></a>

1. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") to access your organization, the go to the **Quality Profiles** page.
2. In the top right corner of the page, select **Create**. The **New Quality Profile** page opens.
3. In **Name**, enter the name of the new quality profile.
4. In **Language**, select the language of the new quality profile.
5. In **Parent**, select **None**.
6. Select **Create**.

To change the created profile, see the instructions on the [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention") page.

### Importing a quality profile from another SonarQube instance <a href="#importing-quality-profile-from-another-instance" id="importing-quality-profile-from-another-instance"></a>

You can export a custom quality profile to an XML file and import it from another SonarQube instance. SonarQube Server, Cloud, and SonarQube Community Build support this feature.

When you import the quality profile:

* If a quality profile with an identical name already exists, it will be updated. The update process involves adding any active rules from the backup that were not active in the existing profile. Existing active rules will not be updated.
* Otherwise, a new profile is created.

Any user can export a quality profile.You need the Administer Quality Profiles permission to import a quality profile.

To export a custom quality profile:

1. Go to **Quality Profiles**.
2. Locate the quality profile’s row and select the three-dot button in the far right of the row.
3. Select **Back up** in the menu.

To import a backed up quality profile:

1. Go to **Quality Profiles**.
2. In the top right corner of the page, select **Restore**. The **Restore File** dialog opens.
3. Select **Choose File** and find your XML file.
4. Select **Restore**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [understanding-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles "mention")
* [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention")
* [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention")
* [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention")
* [changing-default-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/changing-default-quality-profile "mention")
* [maintaining-your-custom-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/maintaining-your-custom-quality-profiles "mention")
* [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention")
* [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention")
