# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/system-functions/notifications/email.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/managing-your-account/subscribing-to-notifications/email.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/email.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/managing-your-account/subscribing-to-notifications/email.md

# Subscribing to email notifications

{% hint style="info" %}
You’re automatically notified in the following cases:

* When one of your tokens is about to expire.
* As a Quality Profile Administrator, when a built-in quality profile is modified (after a SonarQube Server or analyzer update).
  {% endhint %}

### List of notifications subject to subscription <a href="#list-of-notifications" id="list-of-notifications"></a>

The notifications you can subscribe to are listed below.

<details>

<summary>Overall notifications (for any project)</summary>

| **Notification**                                        | **Description**                                                                                                  |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Background tasks in failure on my administered projects | You are notified of any background task failure for any project you’re an admin of.                              |
| Changes in issues/hotspots assigned to me               | You are notified of any change performed by another user on any issue or hotspot assigned to you on any project. |
| Quality gate changes on all available projects          | You are notified of any status change for any project you have access.                                           |
| My new issues                                           | You are notified if new issues are assigned to you for the specific project.                                     |

</details>

<details>

<summary>Notifications per project</summary>

| **Notification**                              | **Description**                                                                                                            |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Background tasks in failure                   | You are notified of any background task failure on the specific project.                                                   |
| Changes in issues/hotspots assigned to me     | You are notified of any change performed by another user on any issue or hotspot assigned to you for the specific project. |
| Quality gate changes                          | You are notified of any quality gate status change for the specific project.                                               |
| Issues resolved as false positive or accepted | You are notified if issues have been marked as False Positive or Accepted in an analysis of the specific project.          |
| New issues                                    | You are notified of any new issues introduced by your code for the specific project.                                       |
| My new issues                                 | You are notified if new issues are assigned to you for the specific project.                                               |

</details>

### Subscribing to overall notifications <a href="#overall" id="overall"></a>

1. In the upper right corner, select your account menu icon.
2. In the menu, select **My Account**.
3. In the account page’s navigation bar, select **Notifications**.
4. In the **Email** column, select or unselect the check box to enable or disable a notification.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/VrPmOxxqesI39oMhxwgp/sonarqube-server-issues-notifications.png" alt="Subscribing to notifications in SonarQube." width="563"><figcaption></figcaption></figure></div>

### Subscribing to notifications for a project <a href="#project" id="project"></a>

1. In the upper right corner, select your account menu icon.
2. In the menu, select **My Account**.
3. In the account page’s navigation bar, select **Notifications**.
4. If the project is not listed in the **Notifications per project** section, then add it as follows:
   1. Select **Add project** to add the project you want to configure. The Add a project dialog opens.
   2. Enter the first letters of the project, select the project, and select **Add**.
5. In the list of projects, extend the project.
6. In the **Email** column, select or unselect the check box to enable or disable a notification.

### Related pages <a href="#related-pages" id="related-pages"></a>

[email](https://docs.sonarsource.com/sonarqube-server/instance-administration/system-functions/notifications/email "mention")
