# Optimize your Mattermost workspace

With workspace optimizations, system admins can review their workspace
health and growth scores, then take advantage of recommended actions for
ensuring their workspace is running smoothly and teams are maximizing
productivity.

System admins can access their workspace optimization page in the System
Console by selecting the **Product**
[\|product-list\|](##SUBST##|product-list|) menu, selecting **System
Console**, and going to **Reporting \> Workspace Optimization**.

![Review your workspace health and growth scores, then take advantage of recommended optimizations.](../../images/workspace-optimization.png)

## How is the overall score calculated?

The highest score possible is 100. Your score is calculated based on the
type of issue reported and the level of potential security risk
introduced to your Mattermost deployment if ignored.

Each item on the dashboard is calculated based on its individual impact
score. These differ depending on whether they\'re problems, warnings, or
suggestions. For example, if SSL encryption isn\'t configured in your
workspace, Mattermost reports that as a problem, which reduces your
score until it\'s addressed.

Warnings impact your score less than problems, and suggestions have the
least impact on your score.

Want to improve your overall workspace optimization score? Take action
towards the problems, warnings, and suggestions reported on this
dashboard. We recommend the following workspace optimizations.

## Recommendations

The following optimization areas can alert you to workspace suggestions,
warnings, or problems that may require your attention:

+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Optimization   | Suggestions, Warnings, | Additional Information                                                                                                               |
| category       | or Problems Detected   |                                                                                                                                      |
+================+========================+======================================================================================================================================+
| Mattermost     | Are you on the latest  | You\'re notified when updates are available. See the                                                                                 |
| release        | Mattermost release?    | `Upgrade Mattermost </administration-guide/upgrade/upgrading-mattermost-server>`{.interpreted-text role="doc"} product documentation |
|                |                        | for details on upgrading your workspace.                                                                                             |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Configuration  | - **SSL**: Should your | See the product documentation to learn more:                                                                                         |
| issues         |   workspace be more    |                                                                                                                                      |
|                |   secure with SSL?     | - `Set up SSL </administration-guide/onboard/ssl-client-certificate>`{.interpreted-text role="doc"}                                  |
|                | - **Session Length**:  | - `Configure session length <administration-guide/configure/environment-configuration-settings:session lengths>`{.interpreted-text   |
|                |   The default value    |   role="ref"}                                                                                                                        |
|                |   may not provide an   | - `Configure file storage <administration-guide/configure/environment-configuration-settings:file storage>`{.interpreted-text        |
|                |   optimal user         |   role="ref"}                                                                                                                        |
|                |   experience.          |                                                                                                                                      |
|                | - **File Storage**:    |                                                                                                                                      |
|                |   Write access to the  |                                                                                                                                      |
|                |   configured file      |                                                                                                                                      |
|                |   storage location is  |                                                                                                                                      |
|                |   required.            |                                                                                                                                      |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Workspace      | Is the Mattermost      | If your web server settings don\'t pass a live URL test, your workspace may not be accessible to others. See the                     |
| access         | workspace accessible   | `Web server configuration settings <administration-guide/configure/environment-configuration-settings:web server>`{.interpreted-text |
|                | to users?              | role="ref"} product documentation to learn more:                                                                                     |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Search         | As your user base      | See the `Enterprise search </administration-guide/scale/enterprise-search>`{.interpreted-text role="doc"} product documentation to   |
| performance    | grows, is search       | learn more.                                                                                                                          |
|                | getting slower?        |                                                                                                                                      |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Data privacy   | Do you need more       | See the product documentation to learn more:                                                                                         |
|                | control and insights   |                                                                                                                                      |
|                | into your data?        | - `Data Retention </administration-guide/comply/data-retention-policy>`{.interpreted-text role="doc"}                                |
|                |                        | - `Compliance Export </administration-guide/comply/compliance-export>`{.interpreted-text role="doc"}                                 |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| User           | - **AD/LDAP**: As your | See the product documentation to learn more:                                                                                         |
| authentication |   user base grows,     |                                                                                                                                      |
|                |   would you benefit    | - `AD/LDAP <administration-guide/configure/authentication-configuration-settings:ad/ldap>`{.interpreted-text role="ref"}             |
|                |   from easier          | - `Guest accounts </administration-guide/onboard/guest-accounts>`{.interpreted-text role="doc"}                                      |
|                |   onboarding,          |                                                                                                                                      |
|                |   automated            |                                                                                                                                      |
|                |   deactivations, and   |                                                                                                                                      |
|                |   role assignments?    |                                                                                                                                      |
|                | - **Guest accounts**:  |                                                                                                                                      |
|                |   Do you want to       |                                                                                                                                      |
|                |   control user access  |                                                                                                                                      |
|                |   to channels and      |                                                                                                                                      |
|                |   teams with guest     |                                                                                                                                      |
|                |   accounts?            |                                                                                                                                      |
+----------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
