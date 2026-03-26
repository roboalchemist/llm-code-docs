# Source: https://docs.debricked.com/tips-and-tricks/workarounds/configuring-user-access-using-api.md

# Configuring user access using API

An admin can update the user roles of their repositories by using the API endpoint: `https://debricked.com/api/1.0/open/admin/rbac/update-user-roles-by-repo`. This endpoint allows us to assign roles for multiple repositories, to multiple users at the same time.

> When assigning roles to multiple users, each user will receive the same set of roles for the specified repositories.

### Sample script

Let us consider a scenario where two team members (id's 1125 and 1126) who are assigned as maintainers (roleId=4) have moved from one project (repoId=5) to the same roles in another project (repoId=6) and we wish to re-assign their access to the new project, while at the same time revoking the access to the previous one.

```
curl -X 'POST' \
  'https://debricked.com/api/1.0/open/admin/rbac/update-user-roles-by-repo' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "userIds": [
    1125,1126
  ],
  "access": [
    {
      "repoId": 6,
      "roleId": 4
    }
  ],
  "noAccess": [
    {
      "repoId": 5,
      "roleId": 4
    }
  ]
}'
```

In the payload of the API, there are 3 main sections:

1. `userIds`
   1. An array of user IDs
   2. All the users in the array will receive or lose the same set of role or repo mapping.
2. `Access`
   1. Type: Array
   2. This field can be used to provide role access to a certain repository.
   3. Each array item will contain a repo ID and a role ID.
3. `noAccess`
   1. Type: Array
   2. This field can be used to revoke role access to a certain repository.
   3. Each item in an array will contain a repoId and roleId.

**Note:**

1. To get the repository IDs, you can use the below API endpoint: `api/{version}/open/repositories/get-repositories-names-links`
2. To get the user ID, use `/api/{version}/open/admin/users`
3. To get the role ID, see table below:

| Roles            | ID |
| ---------------- | -- |
| Viewer           | 1  |
| Developer        | 2  |
| Reviewer         | 3  |
| Maintainer       | 4  |
| Repository Admin | 5  |
| Company Admin    | 6  |
