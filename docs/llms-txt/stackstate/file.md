# Source: https://archivedocs.stackstate.com/5.1/configure/security/authentication/file.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/file.md

# File-based

## Overview

In case no external authentication provider can be used, you can use file based authentication. This will require every StackState user to be pre-configured in the configuration file. For every change made to a user in the configuration, StackState will automatically restart after applying the changes with Helm.

StackState includes a number of default roles, see the example configuration below. The permissions assigned to each default role and instructions on how to create other roles can be found in the [Role based access control (RBAC) documentation](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/role_based_access_control).

## Set up file based authentication

### Kubernetes

To configure file based authentication on Kubernetes, StackState users need to be added to the `authentication.yaml` file. For example:

{% tabs %}
{% tab title="authentication.yaml" %}

```yaml

stackstate:
  authentication:
    file:
      logins:
        - username: admin
          passwordHash: 5f4dcc3b5aa765d61d8327deb882cf99
          roles: [ stackstate-admin ]
        - username: platformadmin
          passwordHash: 5f4dcc3b5aa765d61d8327deb882cf99
          roles: [ stackstate-platform-admin ]
        - username: guest
          passwordHash: 5f4dcc3b5aa765d61d8327deb882cf99
          roles: [ stackstate-guest ]
        - username: power-user
          passwordHash: 5f4dcc3b5aa765d61d8327deb882cf99
          roles: [ stackstate-power-user ]
        - username: troubleshooter
          passwordHash: 5f4dcc3b5aa765d61d8327deb882cf99
          roles: [ stackstate-k8s-troubleshooter ]
```

{% endtab %}
{% endtabs %}

Follow the steps below to configure users and apply changes:

1. In `authentication.yaml` - add users. The following configuration should be added for each user (see the example above):
   * **username** - the username used to log into StackState.
   * **passwordHash** - the password used to log into StackState. Passwords are stored as a bcrypt hash.
   * **roles** - the list of roles that the user is a member of. The [default StackState roles](https://archivedocs.stackstate.com/self-hosted-setup/rbac/rbac_permissions#predefined-roles) are `stackstate-admin`,`stackstate-platform-admin`, `stackstate-power-user` and `stackstate-guest`, for details on how to create other roles, see [RBAC roles](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_roles).
2. Store the file `authentication.yaml` together with the file `values.yaml` from the StackState installation instructions.
3. Run a Helm upgrade to apply the changes:

   ```
    helm upgrade \
      --install \
      --namespace stackstate \
      --values values.yaml \
      --values authentication.yaml \
    stackstate \
    stackstate/stackstate-k8s
   ```

{% hint style="info" %}
**Note:**

* A bcrypt password hash can be generated using the following command line `htpasswd -bnBC 10 "" <password> | tr -d ':\n'` or using an online tool.
* The first run of the helm upgrade command will result in pods restarting, which may cause a short interruption of availability.
* Include `authentication.yaml` on every `helm upgrade` run.
* The authentication configuration is stored as a Kubernetes secret.
  {% endhint %}

Follow the steps below to configure users and apply changes:

1. In `authentication.yaml` - add users. The following configuration should be added for each user (see the example above):
   * **username** - the username used to log into StackState.
   * **password** - the password used to log into StackState. Passwords are stored as either an MD5 hash or a bcrypt hash.
   * **roles** - the list of roles that the user is a member of. The [default StackState roles](https://archivedocs.stackstate.com/self-hosted-setup/rbac/rbac_permissions#predefined-roles) are `stackstate-admin`, `stackstate-platform-admin`, `stackstate-power-user`, `stackstate-k8s-troubleshooter` and `stackstate-guest`, for details on how to create other roles, see [RBAC roles](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_roles).
2. Restart StackState to apply the changes.

{% hint style="info" %}
**Note:**

* An MD5 password hash can be generated using the `md5sum` or `md5` command line applications on Linux and Mac.
* A bcrypt password hash can be generated using the following command line `htpasswd -bnBC 10 "" <password> | tr -d ':\n'` or using an online tool.
  {% endhint %}

## See also

* [Authentication options](https://archivedocs.stackstate.com/self-hosted-setup/security/authentication/authentication_options)
* [Permissions for predefined StackState roles](https://archivedocs.stackstate.com/self-hosted-setup/rbac/rbac_permissions#predefined-roles)
* [Create RBAC roles](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_roles)
