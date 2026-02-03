# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/managing-jit-mode.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-jit-mode.md

# Managing JIT provisioning

You need the global Administer System permission in SonarQube Server to perform this setup.

### Setting up the group synchronization <a href="#group-synchronization" id="group-synchronization"></a>

With the JIT provisioning mode, you can enable group synchronization. The group synchronization requires that you manually create the user groups in SonarQube Server: see below.

{% hint style="warning" %}
If you enable the group synchronization, you cannot manage group memberships manually and existing manually added group memberships of JIT-provisioned users are reset in SonarQube Server during synchronization.
{% endhint %}

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. On the far right of **App ID,** select **Edit**.
3. In the dialog, select or unselect the **Synchronize user groups** option.
4. Save.

<details>

<summary>Creating the user groups in SonarQube Server</summary>

To allow group synchronization, you must create in SonarQube Server a group for each GitLab group and subgroup you want to synchronize, see [user-groups](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-groups "mention").

You must name the SonarQube Server group according to the URL of the GitLab group or subgroup. Be aware that that name check is case-sensitive.

Examples:

* If the URL of the GitLab group is `https://gitlab.com/my-gitlab-group`, the name of the SonarQube Server group mus be `my-gitlab-group`.
* If the URL of the GitLab group is `https://gitlab.com/my-gitlab-group/sub-group`, the name of the SonarQube Server group must be `my-gitlab-group/sub-group.`

{% hint style="info" %}
To set the group permissions at the system level, see [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention").
{% endhint %}

</details>

### Setting the Allowed groups <a href="#allowed-groups" id="allowed-groups"></a>

Starting from the [Developer Edition](https://www.sonarsource.com/plans-and-pricing/developer/), you can restrict access to SonarQube Server by defining Allowed groups. An Allowed group is a GitLab root group (a group with no parent): only members of the Allowed group and all its subgroups can authenticate to SonarQube Server.

To set the Allowed groups:

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. In the **Provisioning** > **Just-in-Time provisioning > Allowed groups**, enter the root group slug as it appears in the GitLab URL. For instance, if the first Allowed group URL is `https://gitlab.com/my-root-group`, then enter `my-root-group`. A new text box is added underneath.
3. Enter the second Allowed group slug, etc.

### Blocking/Authorizing the sign-up of new users <a href="#sign-up-new-users" id="sign-up-new-users"></a>

You can block the signup of new users with SonarQube. This may be useful if you want to manage user provisioning through an API.

To block or authorize the sign-up of new users with SonarQube Server:

1. Go to **Administration** > **Configuration** > **General Settings** > **Authentication** > **GitLab**.
2. In the **Provisioning** > **Just-in-Time provisioning** section, unselect or select **Allow users to sign up**.

### Related pages <a href="#related-pages" id="related-pages"></a>

* [just-in-time](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/just-in-time "mention")
* [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")
* [setting-up](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up "mention")
* [user-permissions](https://docs.sonarsource.com/sonarqube-server/instance-administration/user-management/user-permissions "mention")
