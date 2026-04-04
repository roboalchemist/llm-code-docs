# Source: https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-profiles/understanding-quality-profiles.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/understanding-quality-profiles.md

# Understanding quality profiles

### Quality profile set assigned to a language <a href="#quality-profile-set-assigned-to-a-language" id="quality-profile-set-assigned-to-a-language"></a>

Several quality profiles can be assigned to a language in your organization:

* A built-in profile is provided and is called the Sonar way profile. You cannot edit this profile.
* From the Team plan, you can create custom quality profiles to meet your coding analysis needs.\
  The Sonar way profile is designed to be broadly suitable for most projects, but it is intended only as a starting point.

In the quality profile set of a language, a profile is defined as the default profile. The default profile is used for the analysis of a project if no profile is explicitly defined for that project.

The figure below shows a quality profile set example of the Java language. In this example, the built-in profile is the default profile and one custom profile has been added.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-da26c9f66e19f924b930e55840c0dd12b32b6274%2Fae9a1d35e1672e65c6a439dd8f9ecf9ca1daaab9.png?alt=media" alt="The image shows the BUILT-IN SonarQube Cloud quality profile and one custom quality profile for the Java language."><figcaption></figcaption></figure></div>

A user with the Administer Quality Profiles permission in the organization can create and edit any custom profile and change the default profile of a set. These users can also give other users permission to edit a given custom profile.

### Quality profile definition <a href="#quality-profile-definition" id="quality-profile-definition"></a>

In your organization, a quality profile:

* Relates to a given programming language.
* Is based on the set of coding rules supported for this language.
* Defines which rules of this set are active in the profile, it means which rules will be taken into account during the code analysis.

A custom quality profile may customize, for a given rule, configurable parameters. For example, rules that verify conditions against a threshold might allow customization of the threshold value. The customization applies only within the quality profile.

### Quality profile inheritance <a href="#quality-profile-inheritance" id="quality-profile-inheritance"></a>

The inheritance feature allows you to define a parent/child relationship between two quality profiles within the profile set of a language. This way, changes in the parent profile are dynamically reported to the child profile. Note that a child profile can only be a custom quality profile.

The figure below shows the Java’s profile set example with a custom profile inheriting from the built-in Sonar way profile.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-20e0ee4e6f557721b8461f7706ebddee9e772c61%2F0f4602f4ac54a996d9d9da2ca130016b1804ec01.png?alt=media" alt="The image shows one custom quality profile in SonarQube that inherits it&#x27;s rule list from the Sonar way quality profile.."><figcaption></figcaption></figure>

By inheriting from the built-in quality profile Sonar way, you ensure that you automatically benefit from:

* Newly implemented rules.
* Changes in a rule’s configuration.
* The deactivation of deprecated rules.

You can also create a quality profile hierarchy: a change in a parent profile is reflected in all its child profiles on all hierarchy levels.

The following principles govern the quality profile inheritance:

* The inheritance relationship can be established or removed according to the following:
  * A parent profile can be assigned to a child profile during the child profile creation or at any time during the lifecycle of a custom profile.
  * The inheritance relationship can be removed at any time.
  * A child profile can change to another parent at any time.
  * A parent profile may be a built-in or a custom profile (A child profile is always a custom profile.).
* When an inheritance relationship is established:
  * The child quality profile inherits its parent’s active rules.
  * Active rules existing already in the child profile are not changed.
* A change in a parent profile is automatically reflected in all its child profiles (note that if a child profile changes to another parent, this is considered a change in the parent profile). It means that:
  * A rule activation or deactivation in the parent profile is reflected in the child profiles whatever the status (active or inactive) of the rule in the child profile.
  * A rule parameter change in the parent profile is reflected in the child profiles if the rule is not overridden in the child profile.
* A child quality profile can be changed as follows:
  * An inactive rule can be activated.
* An active rule can be deactivated.
* A rule’s configurable parameters can be modified compared to the parent profile. In that case, the rule is considered *overridden*.

{% hint style="info" %}
The principles described above are the same whether the parent profile is a built-in or a custom profile.
{% endhint %}

### Quality profile association with projects <a href="#quality-profile-association-with-projects" id="quality-profile-association-with-projects"></a>

The default quality profile of a language’s profile set is used for a project if the project is not explicitly associated with another profile for this language.

By default, the built-in profile is the organization’s default profile for every language. With the Administer Quality Profiles permission, you can change the default profile of a given language in your organization.

As a project administrator, you can assign quality profiles to your project. With the Administer Quality Profiles permission, you can assign a quality profile to a list of projects in your organization.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [viewing-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/viewing-quality-profiles "mention")
* [creating-a-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/creating-a-quality-profile "mention")
* [editing-a-custom-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/editing-a-custom-quality-profile "mention")
* [associating-a-quality-profile-with-projects](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/associating-a-quality-profile-with-projects "mention")
* [changing-default-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/changing-default-quality-profile "mention")
* [maintaining-your-custom-quality-profiles](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/maintaining-your-custom-quality-profiles "mention")
* [authorizing-other-users-to-manage-quality-profile](https://docs.sonarsource.com/sonarqube-cloud/standards/managing-quality-profiles/authorizing-other-users-to-manage-quality-profile "mention")
* [quality-profile-association](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/project-analysis/quality-profile-association "mention")
