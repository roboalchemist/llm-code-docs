# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/advanced-security/managing-license-profiles-and-policies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/advanced-security/managing-license-profiles-and-policies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/advanced-security/managing-license-profiles-and-policies.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/advanced-security/managing-license-profiles-and-policies.md

# Source: https://docs.sonarsource.com/sonarqube-server/advanced-security/managing-license-profiles-and-policies.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-security/managing-license-profiles-and-policies.md

# Managing license profiles and policies

Advanced Security is an add-on that requires a separate subscription to your SonarQube Cloud's [Enterprise plan](https://www.sonarsource.com/plans-and-pricing/#sonarqube-cloud-features).

To reduce legal risk and maintain a high level of security for your software, it’s important to ensure your project’s dependencies use licenses that comply with your organization’s policies.

### About license profiles <a href="#about-license-profiles" id="about-license-profiles"></a>

A license profile is a collection of policies that define which licenses are allowed or prohibited for the dependencies used in your projects.

Once configured, analysis will raise a dependency risk when a dependency with a prohibited license is detected in your projects.

Depending on how your software is built, deployed, and delivered to your users, you may have different licensing requirements for different projects in your organization. You can create multiple license profiles based on the needs of your applications, and assign projects to each individual profile as needed.

#### How Sonar analyzes license combinations <a href="#how-sonar-analyzes-license-combinations" id="how-sonar-analyzes-license-combinations"></a>

Sonar proactively analyzes license combinations to give you the most accurate results according to your policy.

For example, if your policy allows MIT, but disallows LGPL-2.0:

* software that is licensed as "MIT AND LGPL-2.0" will generate a dependency risk, as a portion of it uses a license that you have not allowed.
* software that is licensed as "MIT OR LGPL-2.0" will *not* generate a dependency risk, as you can use it under the MIT license.

### Creating a license profile <a href="#creating-a-license-profile" id="creating-a-license-profile"></a>

To define which licenses are allowed or prohibited, you must create a license profile. Note that you need the **Administer Quality Profiles** permission to perform this task.

When you create a license profile, you choose if it applies:

* to only the projects you select
* to all the existing and future projects of your instance, except the projects already assigned to a different profile.

To create a license profile:

1. Go to **License profiles** > **Create profile.**
2. Give your license profile a name.
3. Select the scope of your license profile:
   1. To use it only on certain projects, choose **Only the projects I select.**
   2. To create a default profile that applies to all projects, choose **Every project I should use should use this project by default.**

### Managing license profiles <a href="#managing-license-profiles" id="managing-license-profiles"></a>

You can edit your license profiles under **License profiles** > *your license profile.*

If your profile is applied to selected projects only, go to **Projects using this profile** > **Manage** to edit the list of projects that use this license profile.

### Viewing the list of licenses <a href="#viewing-the-list-of-licenses" id="viewing-the-list-of-licenses"></a>

Licenses used in your projects are listed in the **License profiles** > **Licenses** section. You can search for licenses and filter them by category.

Each license in the list has a display name and an SPDX identifier based on the [SPDX License List](https://spdx.org/licenses/), a listing of common open source licenses.

By default, all the licenses are prohibited, see “Configuring license policies” below for more information.

#### About license categories <a href="#about-license-categories" id="about-license-categories"></a>

Each license has a category determined by Sonar based on [Blue Oak Council’s](https://blueoakcouncil.org/copyleft) categorization of licenses. The categories are as follows:

| **License category**    | **Description**                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard permissive     | <p>The most commonly used permissive licenses. They grant broad permissions to use and modify with very minimal obligations (primarily attribution) and have all the essential elements of permissive open source licenses.<br><br>Examples: MIT and Apache software licenses.</p>                                                                                                                  |
| Non-standard permissive | <p>Permissive licenses that lack one or more essential elements of modern permissive open source licenses, or impose complex or confusing requirements.</p><p>Many use unclear, jocular, or incomplete language and can be considered less legally predictable to use.<br><br>Examples: Artistic 1.0 and the WTFPL software licenses.</p>                                                           |
| Weak copyleft           | <p>Weak copyleft licenses require sharing your changes and additions to the licensed software when you give copies to others.</p><p>Examples: GNU LGPL and the Mozilla Public License software licenses.</p>                                                                                                                                                                                        |
| Strong copyleft         | <p>In addition to the requirements of the weak copyleft licenses, strong copyleft licenses require you to share larger programs that you build with the licensed software when you give copies to others.</p><p>Example: the GNU GPL license.</p>                                                                                                                                                   |
| Network copyleft        | <p>In addition to the requirements of strong copyleft licenses, network copyleft licenses require you to share larger programs that you build with the licensed software not just when you give copies to others, but also when you run the software for others to use over the Internet or another network.</p><p>Examples: the GNU AGPL and the Server-Side-Public License software licenses.</p> |
| Maximal copyleft        | <p>Maximal copyleft licenses answer the question “When does the license require you to share?” differently than other families. Maximal copyleft licenses require you to share software you make with others, and to license that software alike when you do.</p><p>Example: the Parity and Reciprocal software licenses.</p>                                                                       |
| Other                   | <p>Many detectable licenses do not fall into one of the standard categories, usually because they have non-standard requirements.</p><p>Any license in the ‘Other’ category needs to be individually reviewed and configured based on the specific license terms and use case.</p>                                                                                                                  |

### Configuring license policies <a href="#configuring-license-policies" id="configuring-license-policies"></a>

Once your license profile is created, you can configure license policies to define which licenses are allowed or prohibited in your license profile.

By default, all licenses are prohibited.

From the **Licenses** section, you can configure:

* *individual policies,* by assigning the **Allowed** or **Prohibited** policy to each license.
* *default policies*, by mapping each license category to the **Allowed** or **Prohibited** policy. Default policies don’t apply to 'Other' licenses.

To set default policies, go to **Default policies** > **Manage** and select **Allowed** or **Prohibited** for each license category.

It’s possible to override default policies with individual policies for each license.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [Reviewing and fixing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/reviewing-and-fixing-dependency-risks)
* [Analyzing projects for dependencies](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/analyzing-projects-for-dependencies-sca)
* [Troubleshooting](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/troubleshooting-the-dependency-analysis)
* [Best practices for managing dependency risks](https://docs.sonarsource.com/sonarqube-cloud/advanced-security/best-practices-for-managing-dependency-risks)
