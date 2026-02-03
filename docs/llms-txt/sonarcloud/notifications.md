# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/instance-administration/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-account/notifications.md

# Subscribing to email notifications

You can choose to receive email notifications on specific events.

### List of notifications <a href="#list" id="list"></a>

The notifications you can subscribe to are listed below.

{% hint style="info" %}

* Notifications can only be sent on events occurring on the main branch and long-lived branches.
* Notifications are not sent on new issues if the issue creation date has been backdated.
  {% endhint %}

<details>

<summary>Overall notifications (for any project)</summary>

| **Notification**                                        | **Description**                                                                                                  |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Background tasks in failure on my administered projects | You are notified of any background task failure for any project you’re an admin of.                              |
| Changes happen in issues/hotspots assigned to me        | You are notified of any change performed by another user on any issue or hotspot assigned to you on any project. |
| My new issues                                           | You are notified of any new issues introduced by your code for any project.                                      |

</details>

<details>

<summary>Project notifications (for a specific project)</summary>

| **Notification**                                 | **Description**                                                                                                            |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Background tasks fail                            | You are notified of any background task failure on the specific project.                                                   |
| Changes happen in issues/hotspots assigned to me | You are notified of any change performed by another user on any issue or hotspot assigned to you for the specific project. |
| New Quality Gate status                          | You are notified of any quality gate status change for the specific project.                                               |
| Issues resolved as false positive or accepted    | You are notified if issues have been marked as False Positive or Accepted in an analysis of the specific project.          |
| New issues are assigned to me                    | You are notified if new issues are assigned to you for the specific project.                                               |
| My new issues                                    | You are notified of any new issues introduced by your code for the specific project.                                       |

</details>

### Subscribing to overall notifications <a href="#overall" id="overall"></a>

1. Select your account menu in the top right corner of the SonarQube Cloud interface.
2. In the menu, select **My Account**, and then **Notifications**.
3. In the **Overall Notifications** section, select the checkbox corresponding to the kind of notification you want to subscribe to. See **Overall notifications** above.

### Subscribing to notifications on a specific project <a href="#project" id="project"></a>

You can perform this configuration either from your account menu or from your project page.

<details>

<summary>From your account menu</summary>

1. Select your account menu in the top right corner of the SonarQube Cloud interface.
2. In the menu, select **My Account**; then select **Notifications**.
3. In the **Project Notifications** section, select **Add a project**, and select the project.
4. For the added project, select the checkbox corresponding to the kind of notification you want to subscribe to. See **Project notifications** above.

</details>

<details>

<summary>From your project page</summary>

1. Check the [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") page for information about accessing your project.
2. In the left sidebar, select **Information**.
3. In the **Notifications** section, select the checkbox corresponding to the kind of notification you want to subscribe to. See **Project notifications** above.

</details>
