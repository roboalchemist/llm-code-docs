# Source: https://docs.debricked.com/product/license-risk-management/set-up-a-use-case/set-up-a-use-case-using-the-api.md

# Set up a use case using API

The first time you visit the License view; you willl notice that the value in the risk column is set to *Unknown* for all licenses. This is because you have not yet configured any use cases for your repositories. You can select a use case through the API using the endpoint:

```
/api/{version}/open/repository-settings/repositories/{repositoryId}/select-use-case
```

To do so, send a JSON containing a choice of the use case, for example:

```
"useCase": 2
```

Here, the *useCase* can be one of the following integers:&#x20;

* 0/null - Unknown
* 1 - Non-distributed internal
* 2 - Non-distributed public
* 3 - Distributed generic
* 4 - Distributed electronics

Here’s an example showing you how to set the use case to “Non-distributed public” for a repository with ID = 1337:

```
curl -X 'POST' \  'https://debricked.com/api/1.0/open/repository-settings/repositories/1337/select-use-case' \  -H 'accept: */*' \  -H 'Authorization: Bearer <token> \  -H 'Content-Type: application/json' \  -d '{ "useCase": 2 }'
```
