# Source: https://docs.port.io/api-reference/change-scorecards.md

# Change scorecards

```
PUT 
/v1/blueprints/:blueprint_identifier/scorecards
```

This route allows you to modify one or more scorecards of a given blueprint. A scorecard is a set of rules that define the quality of a blueprint.<br /><br />To learn more about scorecards, check out the [documentation](https://docs.port.io/scorecards/overview).

## Request[â](#request "Direct link to Request")

## Responses[â](#responses "Direct link to Responses")

* 401
* 404
* 413
* 422

Default Response

A resource with the provided identifier was not found

Request body is too large (limit is 1MiB)

The json provided does not match the route's schema
