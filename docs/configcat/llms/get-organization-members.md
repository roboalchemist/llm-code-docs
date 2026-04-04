# Source: https://configcat.com/docs/api/reference/get-organization-members.md

# List Organization Members

Copy page

deprecated

This endpoint has been deprecated and may be replaced or removed in future versions of the API.

This endpoint returns the list of Members that belongs to the given Organization, identified by the `organizationId` parameter.

The results may vary based on the access level of the user who calls the endpoint:

* When it's called with Organization Admin privileges, the result will contain each member in the Organization.
* When it's called without Organization Admin privileges, the result will contain each Organization Admin along with members of those products where the caller has `Team members and permission groups` (`canManageMembers`) permission.

## Request[​](#request "Direct link to Request")

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404
* 429

Bad request.

Not found.

Too many requests. In case of the request rate exceeds the rate limits.
