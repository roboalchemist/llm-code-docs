# Source: https://docs.sonarsource.com/sonarqube-community-build/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/just-in-time.md

# Just-in-Time provisioning

With this mode, you can use the group synchronization and user access restriction features described below.

### Group synchronization <a href="#group-synchronization" id="group-synchronization"></a>

Groups are used in SonarQube Server to manage user permissions.

With the group synchronization:

* The synchronization occurs each time a user logs in to SonarQube Server with their GitLab credentials.
* If a matching group is found in SonarQube Server, the GitLab account’s memberships in that group are synchronized in SonarQube Server. The groups match if the SonarQube Server group name matches the GitLab group URL. For example, the SonarQube Server group `my-gitlab-group/sub-group` matches the GitLab group whose URL is `https://gitlab.com/my-gitlab-group/sub-group`. (The name check is case-sensitive; The default built-in `sonar-users` group is excluded from the synchronization.)
* Manually added group memberships of JIT-provisioned users are reset in SonarQube Server at synchronization time.

<figure><img src="broken-reference" alt="JIT&#x27;s group synchronization principles with GitLab"><figcaption></figcaption></figure>

### User access restriction (Allowed groups) <a href="#user-access-restriction" id="user-access-restriction"></a>

You can block the signup of new users with SonarQube. This may be useful if you want to manage user provisioning through an API.

Starting from the [Developer edition](https://www.sonarsource.com/plans-and-pricing/developer/), you can restrict access to SonarQube Server by defining Allowed groups. An Allowed group is a GitLab root group (a group with no parent): only members of the Allowed group and all its subgroups can authenticate to SonarQube Server.

{% hint style="info" %}
If group synchronization is enabled, only Allowed groups and subgroups are taken into account during synchronization.
{% endhint %}

### Related pages <a href="#related-pages" id="related-pages"></a>

* [#group-concept](https://docs.sonarsource.com/sonarqube-server/user-management/user-groups#group-concept "mention")
* [automatic](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic "mention")
* [setting-up](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up "mention")
* [managing-jit-mode](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-jit-mode "mention")
