# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-automatic-provisioning.md

# Managing automatic provisioning

You can enable the automatic user and group provisioning and benefit from:

* Automatic user and group provisioning and de-provisioning.
* Automatic synchronization of users’ group memberships.
* Automatic synchronization of user permissions on projects.
* Automatic project visibility synchronization.

For more information, see [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention").

{% hint style="warning" %}
With the automatic provisioning mode, the actions you can perform on local users are restricted (The local users are all the users who are not managed by the automatic provisioning process.): see [#limitations](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/provisioning-modes/automatic#limitations "mention").
{% endhint %}

{% hint style="info" %}
The automatic provisioning process does not synchronize the global permissions. You must still set them manually. See [#global-permissions](https://docs.sonarsource.com/sonarqube-server/user-management/user-permissions#global-permissions "mention").
{% endhint %}

### Enabling the automatic provisioning <a href="#enabling" id="enabling"></a>

You can enable the automatic provisioning mode once you’ve set up the Gitlab authentication and provisioning (The automatic mode is disabled by default.).

{% hint style="warning" %}

* The first user and group provisioning run happens immediately when you enable the feature.
* During the first synchronization, existing manually added group memberships and permissions of auto-provisioned accounts are reset in SonarQube.
  {% endhint %}

To enable the automatic provisioning mode:

1. In GitLab, create the GitLab token that will be used by SonarQube Server to access and synchronize with the GitLab server. You can use either a group or a personal access token, as long as it has visibility on the allowed GitLab groups (see **Setting the allowed GitLab groups** below) . The token’s scope must include `read_api`.
2. In SonarQube Server, go to **Administration > Configuration > General Settings > Authentication > GitLab**.
3. In the **Provisioning** section, select **Automatic user, group, and permission provisioning.**
4. In **Provisioning token**, enter the GitLab token created in the first step.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/3ksEKqhudPuUmJ7jnu2O/f1fc984304a5017290561b3e37a0367bc032b007.png" alt="Enable the automatic provisioning in SonarQube Server by entering the GitLab token"><figcaption></figcaption></figure>

5. In **Allowed groups**, enter the GitLab root groups (groups with no parent) to be provisioned in SonarQube Server: see below.
6. If you want to change the role permission mapping, select the **Edit mapping** button in **Role permission mapping**. See **Editing the role permission mapping** below.

### Setting the allowed GitLab groups <a href="#allowed-groups" id="allowed-groups"></a>

When using the GitLab automatic provisioning mode in SonarQube Server, you must define which GitLab root groups (groups with no parent) will be provisioned: only members of these *Allowed* groups and all their subgroups will be provisioned. For more information, see [#user-and-group-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/provisioning-modes/automatic#user-and-group-provisioning "mention").

To set or change the allowed GitLab groups:

1. Go to **Administration > Configuration > General Settings > Authentication > GitLab**.
2. In **Automatic user and group provisioning > Allowed groups,** enter the root group slug as it appears in the GitLab URL. For instance, if the first group URL is `https://gitlab.com/my-root-group`, then enter `my-root-group`. A new text box is added underneath.
3. Enter the second root group slug, etc.

<div align="left"><figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/hRWHCGeok09dpeisKsG4/19f5ed3c9610d8e632555ddf217dec9c79dea34b.png" alt="Enter the root group URL of the allowed groups in GitLab" width="464"><figcaption></figcaption></figure></div>

### Editing the role permission mapping <a href="#edit-role-mapping" id="edit-role-mapping"></a>

SonarQube Server synchronizes the project permissions of auto-provisioned users based on the configured role permission mapping. You can change the mapping provided by default, and if you use custom rules in GitLab, you can configure their mapping to SonarQube Server project permissions. For more information, see [#permissions-synchronization](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/provisioning-modes/automatic#permissions-synchronization "mention").

To edit the mapping of GitLab roles with SonarQube Server permissions:

1. Go to **Administration > Configuration > General Settings > Authentication > GitLab**.
2. In **Provisioning > Role permission mapping**, select **Edit mapping**. The **Global GitLab role mapping** dialog opens.
3. Select or unselect a checkbox to modify the permissions of the different roles.
4. To add a custom role:
   * In the **Add custom role** section, enter the exact name of the custom role.
   * Select **Add**. The custom role is added below the section.
   * Configure the permissions of the custom role.
5. To remove a custom role, select the dustbin icon near the custom role name.
6. Select **Close**. The dialog closes and the changes are saved.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/XDYGYDbPnWgZOdhfZkld/8b9f95aa0fa3029ca7ffd5c2b7fb08a2fe8e5618.png" alt="To add a GitLab custom role to the mapping table, enter the name and select Add"><figcaption></figcaption></figure>

### Enabling/disabling the Just-in-Time group membership synchronization <a href="#jit-group-synchronization" id="jit-group-synchronization"></a>

In addition to the hourly synchronization, you can enable SonarQube Server to synchronize the group memberships of any existing auto-provisioned user at authentication time (Just-in-Time (JIT) synchronization).

To enable or disable the JIT group membership synchronization:

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. On the far right of **App ID**, select **Edit**. The **Edit GitLab Configuration** dialog opens.
3. Select or unselect the **Synchronize user groups** option.
4. Select **Save configuration**.

### Monitoring the synchronization <a href="#monitoring-synchronization" id="monitoring-synchronization"></a>

You can check the status and possible errors of the last synchronization between GitLab and SonarQube Server, with statistics on the number of users and groups synchronized from GitLab, and the number of projects for which user permissions have been synchronized.

To monitor the synchronization:

* Go to **Administration > Configuration > General Settings > Authentication > GitLab**. The synchronization message is shown in the **Automatic user, group, and permission provisioning** section. If a synchronization is in progress, "Synchronization is pending" is displayed.

<figure><img src="https://content.gitbook.com/content/LWhbesChsC4Yd1BbhHhS/blobs/4aHJAHKLQcRxymMS6GYB/8dc38a60d652972c71f0a817db62509268300eb0.png" alt="Select the Synchronize now button to start a manual synchronization"><figcaption></figcaption></figure>

### Manually starting a synchronization <a href="#starting-synchronization" id="starting-synchronization"></a>

Synchronization is started automatically every hour. If necessary, you can start a synchronization manually. The next automatic synchronization will happen one hour after the last synchronization.

To start a synchronization:

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. In the **Automatic user, group, and permission provisioning** section, select the **Synchronize now** button.

### Changing the provisioning token <a href="#modifying-token" id="modifying-token"></a>

1. In GitLab, create the new GitLab token that will be used by SonarQube Server to access and synchronize with the GitLab server. You can use either a group or a personal access token, as long as it has visibility on the allowed GitLab groups (see **Setting the allowed GitLab groups** above). The token’s scope must include `read_api`.
2. In SonarQube Server, go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
3. In **Automatic user, group, and permission provisioning** > Provisioning token, select the **Update field value** button.
4. Copy-paste the new token.
5. Select **Save**.

### Disabling the automatic provisioning <a href="#disabling" id="disabling"></a>

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. In the **Provisioning** section, select the **Just-in-time user provisioning** option.
3. Select the **Save** button.
4. To manage the JIT provisioning mode, see [managing-jit-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-jit-mode "mention").

### Related pages <a href="#related-pages" id="related-pages"></a>

* [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")
* [setting-up](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up "mention")
