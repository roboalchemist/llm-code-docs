# Source: https://redocly.com/docs/realm/content/api-docs/openapi-extensions/x-rbac.md

# Source: https://redocly.com/docs/realm/content/api-docs/asyncapi-extensions/x-rbac.md

# AsyncAPI extension: `x-rbac`

The `x-rbac` option allows you to control access to various AsyncAPI objects based on the [teams](/docs/realm/reunite/organization/teams) in your organization.

## Location

Add `x-rbac` to any AsyncAPI object, such as an `Channel`, `Operation`, or `Schema`.
If the current user is not in a team with access, the object is not rendered in the documentation.
Objects restricted by `x-rbac` are excluded from the downloadable AsyncAPI file, ensuring consistent access control across all representations of the API documentation.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| x-rbac | Map[string, string] | Map of team names to [project roles](/docs/realm/access/roles#project-roles).
Team names come from the identity provider or teams associated with the Redocly login.
Additionally, there are automated team names `anonymous` (meaning all users who are not logged in), `authenticated` (meaning any user who is logged in).
Learn more about mapping group names that come from the identity provider through the [single-sign-on (SSO) configuration to either Redocly default teams or project RBAC teams](/docs/realm/reunite/organization/sso/add-idp#team-mapping).
In addition, the team name `*` represents the rest of the teams not defined in sibling properties including `anonymous` and `authenticated`.
Possible values of roles: `none`, `read`, `write`, `triage`, `maintain`, or `admin`. |


## Example

The following example shows how to enable access to the `User Ratings Topic` to only those users who are authenticated.


```yaml
asyncapi: 3.0.0
...
channels:
  ratings:
    address: ratings-{ratingDirection}
    title: User Ratings Topic
    summary: Event stream of driver and passenger ratings
    description: Topic for collecting and processing user experience ratings submitted by drivers and passengers.
    servers:
      - $ref: '#/servers/production'
    x-rbac:
        authenticated: read
    messages:
      driverRating:
        $ref: '#/components/messages/driverRating'
```

## Resources

- **[Role-based access control concepts](/docs/realm/access/rbac)** - Learn about RBAC fundamentals and how it integrates with AsyncAPI documentation
- **[Supported AsyncAPI extensions](/docs/realm/content/api-docs/asyncapi-extensions)** - Complete list of all AsyncAPI extensions supported by Redocly for enhanced API documentation