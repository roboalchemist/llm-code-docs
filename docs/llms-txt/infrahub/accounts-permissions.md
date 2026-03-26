# Source: https://docs.infrahub.app/guides/accounts-permissions.md

# Creating accounts, groups, roles, and permissions

In Infrahub, managing access and control starts with creating accounts, assigning them to groups, and managing their roles and permissions. This guide outlines how to create new accounts, accounts groups, and assign roles and permissions.

For more information on roles and permissions, see the [Roles and Permissions](/topics/permissions-roles.md) topic.

## Creating a new account[​](#creating-a-new-account "Direct link to Creating a new account")

* Via the Web Interface
* Via the GraphQL Interface

### Via the Web Interface[​](#via-the-web-interface "Direct link to Via the Web Interface")

1. Log in to the Infrahub UI as an administrator.
2. Go to **Admin > Role Management** in the left side menu.
3. In the **Accounts** tab, click on **Create Account**.
4. Fill in the account's details (name, email, and password).
5. Optionally, assign the account to a group.
6. Click **Create** to create the account.

![New Account](/assets/images/permissions_account-8e8426b2e619ea4d75eeebd2e495363b.png)

### Via the GraphQL Interface[​](#via-the-graphql-interface "Direct link to Via the GraphQL Interface")

In the GraphQL sandbox, execute the following mutation to create a new account, replacing the appropriate values as needed:

```
mutation AddAccount {
  CoreAccountCreate(
    data: {
      name: {value: "<ACCOUNT-NAME>"},
      password: {value: "<ACCOUNT-PASSWORD>"}
      # Optional - Assign the account to an existing group
      member_of_groups: [{hfid: "Infrahub Users"}]
    }
  ) {
    ok
    object {
      hfid
    }
  }
}
```

## Creating a new account group[​](#creating-a-new-account-group "Direct link to Creating a new account group")

* Via the Web Interface
* Via the GraphQL Interface

### Via the Web Interface[​](#via-the-web-interface-1 "Direct link to Via the Web Interface")

1. Log in to the Infrahub UI as an administrator.
2. Go to **Admin > Role Management** in the left side menu.
3. In the **Groups** tab, click on **Create Account Group**.
4. Enter a name for the group.
5. Optionally, assign roles to the group.
6. Click **Create** to create the group.

![New Group](/assets/images/permissions_group-0217fdf7a62e4f9a4bacd61ce5148056.png)

### Via the GraphQL Interface[​](#via-the-graphql-interface-1 "Direct link to Via the GraphQL Interface")

In the GraphQL sandbox, execute the following mutation to create a new group:

```
mutation AddGroup {
  CoreAccountGroupCreate(
    data: {
      name: {value: "<GROUP-NAME>"},
      # Optional - Assign existing roles
      roles: [{hfid: "General Access"}]
    }
  ) {
    ok
    object {
      hfid
    }
  }
}
```

## Creating and assigning roles[​](#creating-and-assigning-roles "Direct link to Creating and assigning roles")

* Via the Web Interface
* Via the GraphQL Interface

### Via the Web Interface[​](#via-the-web-interface-2 "Direct link to Via the Web Interface")

1. Log in to the Infrahub UI as an administrator.
2. Go to **Admin > Role Management** in the left side menu.
3. In the **Roles** tab, click on **Create Account Role**.
4. Provide a name for the role.
5. Select the permissions you wish to assign to the role.
6. Optionally, assign the role to an existing group.
7. Click **Create** to create the role.

![New Role](/assets/images/permissions_role-a5d527b5c9182c417f093a8ec96d9f45.png)

### Via the GraphQL Interface[​](#via-the-graphql-interface-2 "Direct link to Via the GraphQL Interface")

In the GraphQL sandbox, execute the following mutation to create a new role:

```
mutation AddRole {
  CoreAccountRoleCreate(
    data: {
      name: {value: "test role"},
      # Optional - Assign the role to an existing group
      groups: [{hfid: "Infrahub Users"}]
    }
  ) {
    ok
    object {
      hfid
    }
  }
}
```

## Managing permissions[​](#managing-permissions "Direct link to Managing permissions")

Permissions can be managed through roles assigned to users or groups. Infrahub supports **Global** and **Object-specific** permissions, allowing fine-grained control over what users can do within the system. For a complete list of available global and object permissions, see the [Roles and Permissions documentation](/reference/permissions.md).

### Creating and global permissions[​](#creating-and-global-permissions "Direct link to Creating and global permissions")

* Via the Web Interface
* Via the GraphQL Interface

### Via the Web Interface[​](#via-the-web-interface-3 "Direct link to Via the Web Interface")

1. Log in to the Infrahub UI as an administrator.
2. Go to **Admin > Role Management** in the left side menu.
3. In the **Global Permissions** tab, click on **Create Global Permission**.
4. Select the action you which to use.
5. Select the decision for this action.
6. Optionally, assign the permission to an existing role.
7. Click **Create** to create the permission.

### Via the GraphQL Interface[​](#via-the-graphql-interface-3 "Direct link to Via the GraphQL Interface")

In the GraphQL sandbox, execute the following mutation to create a new global permission:

```
mutation AddGlobalPermissions {
  CoreGlobalPermissionCreate(
    data: {
      action: {value: "manage_accounts"},
      # 6 is the enum value for "allow"
      decision: {value: 6}
    }
  ) {
    ok
    object {
      identifier {
        value
      }
    }
  }
}
```

### Creating and objects permissions[​](#creating-and-objects-permissions "Direct link to Creating and objects permissions")

* Via the Web Interface
* Via the GraphQL Interface

### Via the Web Interface[​](#via-the-web-interface-4 "Direct link to Via the Web Interface")

1. Log in to the Infrahub UI as an administrator.
2. Go to **Admin > Role Management** in the left side menu.
3. In the **Objects Permissions** tab, click on **Create Object Permission**..
4. Provide the namespace and name of the object(s) you want to interact with.
5. Select the action and decision you wish to use for this permission.
6. Optionally, assign the permission to an existing role.
7. Click **Create** to create the permission.

### Via the GraphQL Interface[​](#via-the-graphql-interface-4 "Direct link to Via the GraphQL Interface")

In the GraphQL sandbox, execute the following mutation to create a new global permission:

```
mutation AddObjectPermissions {
  CoreObjectPermissionCreate(
    data: {
      namespace: {value: "Builtin"},
      name: {value: "Tag"},
      action: {value: "view"},
      # 4 is the enum value for "allow_other"
      decision: {value: 4 }
    }
  ) {
    ok
    object {
      identifier {
        value
      }
    }
  }
}
```
