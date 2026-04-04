# Source: https://docs.apify.com/api/v2/act-versions-post.md

# Create version


```
POST 
https://api.apify.com/v2/acts/:actorId/versions
```


Creates a version of an Actor using values specified in a  passed as JSON in the POST payload.

The request must specify `versionNumber` and `sourceType` parameters (as strings) in the JSON payload and a `Content-Type: application/json` HTTP header.

Each `sourceType` requires its own additional properties to be passed to the JSON payload object. These are outlined in the  table below and in more detail in the [Apify documentation](https://docs.apify.com/platform/actors/development/deployment/source-types).

For example, if an Actor's source code is stored in a [GitHub repository](https://docs.apify.com/platform/actors/development/deployment/source-types#git-repository), you will set the `sourceType` to `GIT_REPO` and pass the repository's URL in the `gitRepoUrl` property.


```
{
    "versionNumber": "0.1",
    "sourceType": "GIT_REPO",
    "gitRepoUrl": "https://github.com/my-github-account/actor-repo"
}
```


The response is the  as returned by the  endpoint.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
