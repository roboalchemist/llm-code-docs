# Source: https://docs.sonarsource.com/sonarqube-server/10.7/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Source: https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/provisioning-modes/automatic.md

# Automatic provisioning

You can enable the GitLab automatic provisioning mode in SonarQube Server and benefit from:

* Automatic user and group provisioning and de-provisioning.
* Automatic synchronization of users’ group memberships.
* Automatic synchronization of user permissions on projects.
* Automatic project visibility synchronization.

### Limitations <a href="#limitations" id="limitations"></a>

The permission synchronization concerns only the project-level permissions. It means that you must still configure the global permissions manually.

Automatic provisioning can only be enabled with a single identity provider. When enabled, this mechanism becomes the sole method for creating new users in your instance. For more information, see [#automatic-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/overview#automatic-provisioning "mention").

### User and group provisioning <a href="#user-and-group-provisioning" id="user-and-group-provisioning"></a>

The user and group provisioning is restricted to predefined GitLab root groups (groups with no parent): only members of these groups and all their subgroups are provisioned. These groups and subgroups are called *Allowed* groups.

On an hourly basis:

* SonarQube Server provisions and de-provisions the groups as follows:
  * For each Allowed group that doesn’t exist yet in SonarQube Server, it creates the corresponding group: see **Group creation** below.
  * It removes any existing group in SonarQube Server that doesn’t belong to the Allowed groups.
* SonarQube Server provisions and de-provisions the users as follows:
  * It creates a user account for any member of an Allowed group who doesn’t have yet an account in SonarQube Server.
  * It removes any user account that doesn’t belong to any Allowed groups.
* SonarQube Server synchronizes the users with GitLab regarding:
  * Group memberships.
  * Project permissions: see **Project permissions synchronization** below.
* SonarQube Server synchronizes the visibility (public/private) of each project with its bound repository’s associated project in GitLab.

In addition, if enabled, SonarQube Server synchronizes the group memberships of any existing auto-provisioned user at authentication time (Just-in-Time (JIT) synchronization).

<figure><img src="broken-reference" alt="Automatic user and group provisioning principles with GitLab"><figcaption></figcaption></figure>

{% hint style="info" %}
Automatic synchronization won’t set or update emails (This is done at each user login.).
{% endhint %}

### Group creation <a href="#group-creation" id="group-creation"></a>

Since SonarQube Server doesn’t support the group hierarchy (there is no subgroup concept), the corresponding groups and subgroups are all created in SonarQube Server as groups.

The following naming convention is used for a group:\
`<rootGroup>/<subgroup_1>/<subgroup_2>`\
where:

* `rootGroup`: is the name of the root group (group without parent) in GitLab.
* `subgroup_i`: is the level\_i’s subgroup name in GitLab.

For example, if the GitLab group URL is `https://gitlab.com/my-gitlab-group/my-subgroup`, the group name in SonarQube Server will be `my-gitlab-group/my-subgroup`.

### Project permissions synchronization <a href="#permissions-synchronization" id="permissions-synchronization"></a>

With the automatic provisioning mode, the user permissions on projects are also synchronized: for each project, the permissions of auto-provisioned users are synchronized in SonarQube Server based on the highest GitLab user role applying to the repository in GitLab and according to the configured role permission mapping. A default mapping is provided but you can change it to adapt it to your needs. In addition, if you manage [GitLab custom roles](https://docs.gitlab.com/ee/user/custom_roles.html) (with GitLab Ultimate), you can configure the permission mapping of the custom rules in SonarQube Server.

{% hint style="info" %}
With this feature:

* Project permissions are set at the user level only (not at the group level).
* Project permissions cannot be edited in SonarQube Server (Manually edited project permissions of existing auto-provisioned accounts get reset in SonarQube Server.).
* The application of default permissions for new projects through permission templates is not supported.
  {% endhint %}

<details>

<summary>Default role permission mapping</summary>

The table below shows how a GitLab role is mapped by default to a SonarQube Server permission at the project level. For more information about project permissions, see [#permissions-related-to-a-project](https://docs.sonarsource.com/sonarqube-server/user-management/user-permissions#permissions-related-to-a-project "mention").

| GitLab role | Browse Project | See source Code | Administer Issues | Administer Security Hotspots | Execute Analysis | Administer Project |
| ----------- | -------------- | --------------- | ----------------- | ---------------------------- | ---------------- | ------------------ |
| Guest       | x              | <p><br></p>     | <p><br></p>       | <p><br></p>                  | <p><br></p>      | <p><br></p>        |
| Reporter    | x              | x               | <p><br></p>       | <p><br></p>                  | <p><br></p>      | <p><br></p>        |
| Developer   | x              | x               | x                 | x                            | x                | <p><br></p>        |
| Maintainer  | x              | x               | x                 | x                            | x                | x                  |
| Owner       | x              | x               | x                 | x                            | x                | x                  |

</details>

<details>

<summary>Custom GitLab roles</summary>

You can define the mapping of your custom GitLab roles to SonarQube Server permissions. If no mapping is defined for a custom role, SonarQube Server will perform the permission mapping based on the custom role’s inherited base role.

</details>

### Project visibility synchronization <a href="#project-visibility-synch" id="project-visibility-synch"></a>

With the automatic provisioning mode, the SonarQube Server project visibility is synchronized with the visibility of the project associated with the corresponding repository in GitLab according to the mapping table below.

<table><thead><tr><th width="253">GitLab project visibility</th><th>SonarQube Server project visibility</th></tr></thead><tbody><tr><td>Private</td><td>Private</td></tr><tr><td>Internal</td><td>Private</td></tr><tr><td>Public</td><td>Public</td></tr></tbody></table>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [#group-concept](https://docs.sonarsource.com/sonarqube-server/user-management/user-groups#group-concept "mention")
* [setting-up](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/setting-up "mention")
* [managing-automatic-provisioning](https://docs.sonarsource.com/sonarqube-server/instance-administration/authentication/gitlab/managing-automatic-provisioning "mention")
* [#permission-templates](https://docs.sonarsource.com/sonarqube-server/user-management/user-permissions#permission-templates "mention")
