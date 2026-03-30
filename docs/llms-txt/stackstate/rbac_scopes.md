# Source: https://archivedocs.stackstate.com/5.1/configure/security/rbac/rbac_scopes.md

# Source: https://archivedocs.stackstate.com/self-hosted-setup/security/rbac/rbac_scopes.md

# Scopes

## How do scopes work?

The scope is an [STQL query](https://archivedocs.stackstate.com/reference/k8sts-stql_reference) that's added as a prefix to every query executed in StackState. Whenever a user wants to select a view or pass a query in StackState, this prefix query is executed as a part of the user's query. This limits the results accordingly to match the user's role.

Note: Please note that function calls like `withCauseOf` and `withNeighborsOf` aren't supported as they would not be performant in this context.

If a user belongs to multiple groups, then this user can have multiple scopes, which translates to multiple prefixes. In this situation, the prefix is executed as an OR of all scopes that this user has.

Users need to log out and authenticate again to StackState whenever any changes to roles or permissions are made.

## Why scopes?

Scopes are introduced as a security feature that's mandatory for every subject within StackState. The predefined StackState users Administrator, Power User and Guest roles have no scope defined.

It's possible to specify a scope as a query wildcard, however, this will result in access to everything and isn't recommended. If there is a need for access without a scope, it's recommended to use one of the [predefined roles](https://archivedocs.stackstate.com/self-hosted-setup/security/rbac_permissions#predefined-roles) instead.

## Examples

The below example shows the same topology view called "All Infrastructure" for four users with different permission levels.

### This user is a part of StackState Admin group, so there is no scope:

![Full view permissions](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-55fae73c031512f7eaaad32e1b2dd8fd0d2461f4%2Fv51_allperm.png?alt=media)

The query for this view is the same as for the others, but without any prefix:

```
'layer = "Infrastructure" AND domain IN ("Customer1", "Customer2")'
```

### Below user is in a group with configured subject X with the following scope:

```
'domain = "Customer1"'
```

![Limited view](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-f41c3daf70c1292bed4bcdae48fa5a4a038a925a%2Fv51_esx1perm.png?alt=media)

Query with the prefix for this view is:

```
'(domain = "Customer1") AND (layer = "Infrastructure" AND domain IN ("Customer1", "Customer2"))'
```

### Another user who is a part of a group with a configured subject Y that has the following scope:

```
'domain = "Customer2"'
```

gets this topology:

![Limited view](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-1e9d59b3b686aa4975addc20059b84aaef0866a1%2Fv51_esx2perm.png?alt=media)

Query with the prefix for this view is:

```
'(domain = "Customer2") AND (layer = "Infrastructure" AND domain IN ("Customer1", "Customer2"))'
```

### User with multiple prefixes

It's possible to assign a subject to more than just one group. In this example, you can see an Infrastructure Manager who can see the whole view presented above. This user has to be in both groups that have configured subjects as X and Y. In this case, the prefix for the user query will look like the following:

```
'(domain = "Customer1" OR domain = "Customer2")'
```

Query with prefix for this user is then:

```
'(domain = "Customer1" OR domain = "Customer2") AND (layer = "Infrastructure" AND domain IN ("Customer1", "Customer2"))'
```

Which results in a following view:

![Full view permissions](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-55fae73c031512f7eaaad32e1b2dd8fd0d2461f4%2Fv51_allperm.png?alt=media)
