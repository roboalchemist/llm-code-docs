# Source: https://docs.debricked.com/product/vulnerability-management/pull-requests/solve-vulnerabilities-using-pull-requests-pr-via-the-api.md

# Solve vulnerabilities using Pull Requests (PR) via API

Assume there is a repository with huge number of vulnerabilities. It will take time to go through each one of them and potentially fix them. OpenText Core SCA offers the ability to open a pull request where it tries to solve many vulnerabilities at once.

### Endpoints

/api/{version}/open/repository/{repositoryId}/pull-request/branch/{branchId}/{notify}/{includeUnaffected}

/api/{version}/open/repository/{repositoryId}/get-branches

OpenText Core SCA can generate a new bulk pull request for the repository, with ID 15707 in this case (shown in the URL). The branch ID is found using the get-branches endpoint.

Example:&#x20;

First, OpenText Core SCA gets the branch ID

```
curl -X 'GET' \  'https://debricked.com/api/1.0/open/repository/15707/get-branches' \  -H 'accept: */*' \  -H 'Authorization: Bearer <token>
```

then, a new pull request is created on branch ID 2, enabling notification, not including unaffected dependencies in the PR.

```
curl -X 'GET' \  'https://debricked.com/api/1.0/open/repository/15707/pull-request/branch/2/1/0' \  -H 'accept: */*' \  -H 'Authorization: Bearer <token>
```
