# Vercel Rest Api Documentation

Source: https://vercel.com/docs/rest-api/reference/llms-full.txt

---

# Create an access group project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/create-an-access-group-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{accessGroupIdOrName}/projects
Allows creation of an access group project



# Creates an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/creates-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups
Allows to create an access group



# Delete an access group project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/delete-an-access-group-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
Allows deletion of an access group project



# Deletes an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/deletes-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/access-groups/{idOrName}
Allows to delete an access group



# List access groups for a team, project or member
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-access-groups-for-a-team-project-or-member

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups
List access groups



# List members of an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-members-of-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/members
List members of an access group



# List projects of an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/list-projects-of-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}/projects
List projects of an access group



# Reads an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/reads-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{idOrName}
Allows to read an access group



# Reads an access group project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/reads-an-access-group-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
Allows reading an access group project



# Update an access group
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/access-groups/{idOrName}
Allows to update an access group metadata



# Update an access group project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/access-groups/update-an-access-group-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/access-groups/{accessGroupIdOrName}/projects/{projectId}
Allows update of an access group project



# Assign an Alias
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/assign-an-alias

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/deployments/{id}/aliases
Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.



# Delete an Alias
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/delete-an-alias

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v2/aliases/{aliasId}
Delete an Alias with the specified ID.



# Get an Alias
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/get-an-alias

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases/{idOrAlias}
Retrieves an Alias for the given host name or alias ID.



# List aliases
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-aliases

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/aliases
Retrieves a list of aliases for the authenticated User or Team. When `domain` is provided, only aliases for that domain will be returned. When `projectId` is provided, it will only return the given project aliases.



# List Deployment Aliases
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/list-deployment-aliases

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/deployments/{id}/aliases
Retrieves all Aliases for the Deployment with the given ID. The authenticated user or team must own the deployment.



# Update the protection bypass for a URL
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/update-the-protection-bypass-for-a-url

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /aliases/{id}/protection-bypass
Update the protection bypass for the alias or deployment URL (used for user access & comment access for deployments). Used as shareable links and user scoped access for Vercel Authentication and also to allow external (logged in) people to comment on previews for Preview Comments (next-live-mode).



# Check if a cache artifact exists
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/check-if-a-cache-artifact-exists

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v8/artifacts/{hash}
Check that a cache artifact with the given `hash` exists. This request returns response headers only and is equivalent to a `GET` request to this endpoint where the response contains no body.



# Download a cache artifact
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/download-a-cache-artifact

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/artifacts/{hash}
Downloads a cache artifact indentified by its `hash` specified on the request path. The artifact is downloaded as an octet-stream. The client should verify the content-length header and response body.



# Get status of Remote Caching for this principal
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/get-status-of-remote-caching-for-this-principal

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/artifacts/status
Check the status of Remote Caching for this principal. Returns a JSON-encoded status indicating if Remote Caching is enabled, disabled, or disabled due to usage limits.



# Query information about an artifact
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/query-information-about-an-artifact

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts
Query information about an array of artifacts.



# Record an artifacts cache usage event
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/record-an-artifacts-cache-usage-event

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/artifacts/events
Records an artifacts cache usage event. The body of this request is an array of cache usage events. The supported event types are `HIT` and `MISS`. The source is either `LOCAL` the cache event was on the users filesystem cache or `REMOTE` if the cache event is for a remote cache. When the event is a `HIT` the request also accepts a number `duration` which is the time taken to generate the artifact in the cache.



# Upload a cache artifact
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/artifacts/upload-a-cache-artifact

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/artifacts/{hash}
Uploads a cache artifact identified by the `hash` specified on the path. The cache artifact can then be downloaded with the provided `hash`.



# Create an Auth Token
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/create-an-auth-token

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v3/user/tokens
Creates and returns a new authentication token for the currently authenticated User. The `bearerToken` property is only provided once, in the response body, so be sure to save it on the client for use with API requests.



# Delete an authentication token
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/delete-an-authentication-token

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v3/user/tokens/{tokenId}
Invalidate an authentication token, such that it will no longer be valid for future HTTP requests.



# Get Auth Token Metadata
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/get-auth-token-metadata

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens/{tokenId}
Retrieve metadata about an authentication token belonging to the currently authenticated User.



# List Auth Tokens
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/list-auth-tokens

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/user/tokens
Retrieve a list of the current User's authentication tokens.



# SSO Token Exchange
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/authentication/sso-token-exchange

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/sso/token
During the autorization process, Vercel sends the user to the provider [redirectLoginUrl](https://vercel.com/docs/integrations/create-integration/submit-integration#redirect-login-url), that includes the OAuth authorization `code` parameter. The provider then calls the SSO Token Exchange endpoint with the sent code and receives the OIDC token. They log the user in based on this token and redirects the user back to the Vercel account using deep-link parameters included the redirectLoginUrl. Providers should not persist the returned `id_token` in a database since the token will expire. See [**Authentication with SSO**](https://vercel.com/docs/integrations/create-integration/marketplace-api#authentication-with-sso) for more details.



# Get cert by id
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/certs/get-cert-by-id

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/certs/{id}
Get cert by id



# Issue a new cert
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/certs/issue-a-new-cert

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v8/certs
Issue a new cert



# Remove cert
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/certs/remove-cert

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v8/certs/{id}
Remove cert



# Upload a cert
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/certs/upload-a-cert

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v8/certs
Upload a cert



# Creates a new Check
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/creates-a-new-check

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks
Creates a new check. This endpoint must be called with an OAuth2 or it will produce a 400 error.



# Get a single check
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/get-a-single-check

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks/{checkId}
Return a detailed response for a single check.



# Rerequest a check
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/rerequest-a-check

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
Rerequest a selected check that has failed.



# Retrieve a list of all checks
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/retrieve-a-list-of-all-checks

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/deployments/{deploymentId}/checks
List all of the checks created for a deployment.



# Update a check
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/update-a-check

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/checks/{checkId}
Update an existing check. This endpoint must be called with an OAuth2 or it will produce a 400 error.



# Configures Static IPs for a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/connect/configures-static-ips-for-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/shared-connect-links
Allows configuring Static IPs for a project



# Cancel a deployment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/cancel-a-deployment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v12/deployments/{id}/cancel
This endpoint allows you to cancel a deployment which is currently building, by supplying its `id` in the URL.



# Create a new deployment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/create-a-new-deployment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v13/deployments
Create a new deployment with all the required and intended data. If the deployment is not a git deployment, all files must be provided with the request, either referenced or inlined. Additionally, a deployment id can be specified to redeploy a previous deployment.



# Delete a Deployment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/delete-a-deployment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v13/deployments/{id}
This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments.



# Get a deployment by ID or URL
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-a-deployment-by-id-or-url

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v13/deployments/{idOrUrl}
Retrieves information for a deployment either by supplying its ID (`id` property) or Hostname (`url` property). Additional details will be included when the authenticated user or team is an owner of the deployment.



# Get deployment events
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-deployment-events

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/deployments/{idOrUrl}/events
Get the build logs of a deployment by deployment ID and build ID. It can work as an infinite stream of logs or as a JSON endpoint depending on the input parameters.



# Get Deployment File Contents
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/get-deployment-file-contents

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v8/deployments/{id}/files/{fileId}
Allows to retrieve the content of a file by supplying the file identifier and the deployment unique identifier. The response body will contain a JSON response containing the contents of the file encoded as base64.



# List Deployment Files
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployment-files

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments/{id}/files
Allows to retrieve the file structure of the source code of a deployment by supplying the deployment unique identifier. If the deployment was created with the Vercel CLI or the API directly with the `files` key, it will have a file tree that can be retrievable.



# List deployments
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/list-deployments

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/deployments
List deployments under the authenticated user or team. If a deployment hasn't finished uploading (is incomplete), the `url` property will have a value of `null`.



# Update deployment integration action
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/update-deployment-integration-action

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/deployments/{deploymentId}/integrations/{integrationConfigurationId}/resources/{resourceId}/actions/{action}
Updates the deployment integration action for the specified integration installation



# Upload Deployment Files
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/upload-deployment-files

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/files
Before you create a deployment you need to upload the required files for that deployment. To do it, you need to first upload each file to this endpoint. Once that's completed, you can create a new deployment with the uploaded files. The file content must be placed inside the body of the request. In the case of a successful response you'll receive a status code 200 with an empty body.



# Create a DNS record
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/create-a-dns-record

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/domains/{domain}/records
Creates a DNS record for a domain.



# Delete a DNS record
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/delete-a-dns-record

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v2/domains/{domain}/records/{recordId}
Removes an existing DNS record from a domain name.



# List existing DNS records
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/list-existing-dns-records

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/{domain}/records
Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options.



# Update an existing DNS record
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/dns/update-an-existing-dns-record

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/domains/records/{recordId}
Updates an existing DNS record for a domain name.



# Buy a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/buy
Buy a domain



# Buy multiple domains
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/buy
Buy multiple domains at once



# Get a domain order
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domain-order

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/orders/{orderId}
Get information about a domain order by its ID



# Get a domain's transfer status
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/transfer
Get the transfer status for a domain



# Get availability for a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/availability
Get availability for a specific domain. If the domain is available, it can be purchased using the [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain) endpoint or the [Buy multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains) endpoint.



# Get availability for multiple domains
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-multiple-domains

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/availability
Get availability for multiple domains. If the domains are available, they can be purchased using the [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain) endpoint or the [Buy multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains) endpoint.



# Get contact info schema
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/contact-info/schema
Some TLDs require additional contact information. Use this endpoint to get the schema for the tld-specific contact information for a domain.



# Get price data for a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/price
Get price data for a specific domain



# Get supported TLDs
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-supported-tlds

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/tlds/supported
Get a list of TLDs supported by Vercel



# Get the auth code for a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-the-auth-code-for-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/auth-code
Get the auth code for a domain. This is required to transfer a domain from Vercel to another registrar.



# Get TLD price data
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-tld-price-data

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/tlds/{tld}/price
Get price data for a specific TLD. This only reflects base prices for the given TLD. Premium domains may have different prices. Use the [Get price data for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain) endpoint to get the price data for a specific domain.



# Renew a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/renew-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/renew
Renew a domain



# Transfer-in a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/transfer
Transfer a domain in from another registrar



# Update auto-renew for a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/registrar/domains/{domain}/auto-renew
Update the auto-renew setting for a domain



# Update nameservers for a domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/registrar/domains/{domain}/nameservers
Update the nameservers for a domain. Pass an empty array to use Vercel's default nameservers.



# Add an existing domain to the Vercel platform
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/add-an-existing-domain-to-the-vercel-platform

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v7/domains
This endpoint is used for adding a new apex domain name with Vercel for the authenticating user. Note: This endpoint is no longer used for initiating domain transfers from external registrars to Vercel. For this, please use the endpoint [Transfer-in a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain).



# Check a Domain Availability (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/check-a-domain-availability-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/status
This endpoint is deprecated and replaced with the endpoint [Get availability for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-a-domain). Check if a domain name is available for purchase.



# Check the price for a domain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/check-the-price-for-a-domain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v4/domains/price
This endpoint is deprecated and replaced with the endpoint [Get price data for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain). Check the price to purchase a domain and how long a single purchase period is.



# Get a Domain's configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-a-domains-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v6/domains/{domain}/config
Get a Domain's configuration.



# Get domain transfer info (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-domain-transfer-info-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/domains/{domain}/registry
This endpoint is deprecated and replaced with the endpoint [Get a domain's transfer status](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domains-transfer-status). Fetch domain transfer availability or transfer status if a transfer is in progress.



# Get Information for a Single Domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/get-information-for-a-single-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains/{domain}
Get information for a single domain in an account or team.



# List all the domains
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/list-all-the-domains

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v5/domains
Retrieves a list of domains registered for the authenticated user or team. By default it returns the last 20 domains if no limit is provided.



# Purchase a domain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/purchase-a-domain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v5/domains/buy
This endpoint is deprecated and replaced with the endpoint [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain). Purchases the specified domain.



# Remove a domain by name
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/remove-a-domain-by-name

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v6/domains/{domain}
Delete a previously registered domain name from Vercel. Deleting a domain will automatically remove any associated aliases.



# Update or move apex domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains/update-or-move-apex-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v3/domains/{domain}
Update or move apex domain. Note: This endpoint is no longer used for updating auto-renew or nameservers. For this, please use the endpoints [Update auto-renew for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain) and [Update nameservers for a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-nameservers-for-a-domain).



# Create a new Drain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/create-a-new-drain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains
Create a new Drain with the provided configuration.



# Delete a drain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/delete-a-drain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/drains/{id}
Delete a specific Drain by passing the drain id in the URL.



# Find a Drain by id
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/find-a-drain-by-id

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/drains/{id}
Get the information for a specific Drain by passing the drain id in the URL.



# Retrieve a list of all Drains
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/retrieve-a-list-of-all-drains

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/drains
Allows to retrieve the list of Drains of the authenticated team.



# Update an existing Drain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/update-an-existing-drain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/drains/{id}
Update the configuration of an existing drain.



# Validate Drain delivery configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/drains/validate-drain-delivery-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/drains/test
Validate the delivery configuration of a Drain using sample events.



# Dangerously delete by tag
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-cache/dangerously-delete-by-tag

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-cache/dangerously-delete-by-tags
Marks a cache tag as deleted, causing cache entries associated with that tag to be revalidated in the foreground on the next request. Use this method with caution because one tag can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to cache stampede problem. A good use case for deleting the cache is when the origin has also been deleted, for example it returns a 404 or 410 status code.



# Invalidate by tag
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-cache/invalidate-by-tag

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-cache/invalidate-by-tags
Marks a cache tag as stale, causing cache entries associated with that tag to be revalidated in the background on the next request.



# Create an Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config
Creates an Edge Config.



# Create an Edge Config token
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/create-an-edge-config-token

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config/{edgeConfigId}/token
Adds a token to an existing Edge Config.



# Delete an Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/delete-an-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}
Delete an Edge Config by id.



# Delete an Edge Config's schema
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/delete-an-edge-configs-schema

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}/schema
Deletes the schema of existing Edge Config.



# Delete one or more Edge Config tokens
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/delete-one-or-more-edge-config-tokens

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/edge-config/{edgeConfigId}/tokens
Deletes one or more tokens of an existing Edge Config.



# Get all tokens of an Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-all-tokens-of-an-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/tokens
Returns all tokens of an Edge Config.



# Get an Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}
Returns an Edge Config.



# Get an Edge Config item
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-an-edge-config-item

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/item/{edgeConfigItemKey}
Returns a specific Edge Config Item.



# Get Edge Config backup
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backup

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups/{edgeConfigBackupVersionId}
Retrieves a specific version of an Edge Config from backup storage.



# Get Edge Config backups
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-backups

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/backups
Returns backups of an Edge Config.



# Get Edge Config items
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-items

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/items
Returns all items of an Edge Config.



# Get Edge Config schema
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-schema

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/schema
Returns the schema of an Edge Config.



# Get Edge Config token meta data
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-config-token-meta-data

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config/{edgeConfigId}/token/{token}
Return meta data about an Edge Config token.



# Get Edge Configs
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/get-edge-configs

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/edge-config
Returns all Edge Configs.



# Update an Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/update-an-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/edge-config/{edgeConfigId}
Updates an Edge Config.



# Update Edge Config items in batch
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-items-in-batch

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/edge-config/{edgeConfigId}/items
Update multiple Edge Config Items in batch.



# Update Edge Config schema
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/edge-config/update-edge-config-schema

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/edge-config/{edgeConfigId}/schema
Update an Edge Config's schema.



# Create a custom environment for the current project.
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/create-a-custom-environment-for-the-current-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/custom-environments
Creates a custom environment for the current project. Cannot be named 'Production' or 'Preview'.



# Create one or more shared environment variables
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/create-one-or-more-shared-environment-variables

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/env
Creates shared environment variable(s) for a team.



# Delete one or more Env Var
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/delete-one-or-more-env-var

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/env
Deletes one or many Shared Environment Variables for a given team.



# Disconnects a shared environment variable for a given project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/disconnects-a-shared-environment-variable-for-a-given-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env/{id}/unlink/{projectId}
Disconnects a shared environment variable for a given project



# Lists all Shared Environment Variables for a team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/lists-all-shared-environment-variables-for-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env
Lists all Shared Environment Variables for a team, taking into account optional filters.



# Remove a custom environment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/remove-a-custom-environment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
Remove a custom environment for the project. Must not be named 'Production' or 'Preview'.



# Retrieve a custom environment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/retrieve-a-custom-environment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
Retrieve a custom environment for the project. Must not be named 'Production' or 'Preview'.



# Retrieve custom environments
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/retrieve-custom-environments

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/custom-environments
Retrieve custom environments for the project. Must not be named 'Production' or 'Preview'.



# Retrieve the decrypted value of a Shared Environment Variable by id.
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/retrieve-the-decrypted-value-of-a-shared-environment-variable-by-id

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/env/{id}
Retrieve the decrypted value of a Shared Environment Variable by id.



# Update a custom environment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/update-a-custom-environment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/custom-environments/{environmentSlugOrId}
Update a custom environment for the project. Must not be named 'Production' or 'Preview'.



# Updates one or more shared environment variables
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/environment/updates-one-or-more-shared-environment-variables

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/env
Updates a given Shared Environment Variable for a Team.



# Connect integration resource to project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/connect-integration-resource-to-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/integrations/installations/{integrationConfigurationId}/resources/{resourceId}/connections
Connects an integration resource to a Vercel project. This endpoint establishes a connection between a provisioned integration resource (from storage APIs like `POST /v1/storage/stores/integration/direct`) and a specific Vercel project.



# Create integration store (free and paid plans)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/create-integration-store-free-and-paid-plans

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/storage/stores/integration/direct
Creates an integration store for both FREE and PAID billing plans. This simplified endpoint automatically provisions real integration storage resources while handling billing complexity behind the scenes. It supports both free and paid billing plans with automatic authorization creation for paid resources. ## How it works 1. Validates the integration configuration and product 2. For free resources: Auto-discovers available free billing plans 3. For paid resources: Creates billing authorization inline using provided billingPlanId 4. Provisions real resources through the Vercel Marketplace 5. Returns the created store with connection details ## Workflow Before using this endpoint, discover available products and billing plans: 1. List your configurations: `GET /v1/integrations/configurations` 2. Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Get billing plans for a product: `GET /integrations/integration/{integrationId}/products/{productId}/plans` 4. Review the `metadataSchema` for each product to understand required metadata 5. Create storage with discovered product: `POST /v1/storage/stores/integration/direct` ## Usage Patterns - **Free resources**: Omit `billingPlanId` - endpoint will auto-discover free plans - **Paid resources**: Provide `billingPlanId` from billing plans discovery - **Prepayment plans**: Also provide `prepaymentAmountCents` for variable amount plans ## Limitations - **Admin access required**: Only integration configuration admins can create stores - **Storage limits apply**: Subject to your team's storage quotas - **Payment method required**: For paid plans, ensure valid payment method is configured ## Error Responses - `400 Bad Request`: Invalid input, no plans available, or billing issues - `403 Forbidden`: Insufficient permissions (non-admin users) - `404 Not Found`: Integration configuration or product not found - `429 Too Many Requests`: Rate limit exceeded



# Delete an integration configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/delete-an-integration-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/integrations/configuration/{id}
Allows to remove the configuration with the `id` provided in the parameters. The configuration and all of its resources will be removed. This includes Webhooks, LogDrains and Project Env variables.



# Get configurations for the authenticated user or team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/get-configurations-for-the-authenticated-user-or-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configurations
Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results.



# List integration billing plans
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-integration-billing-plans

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/integration/{integrationIdOrSlug}/products/{productIdOrSlug}/plans
Get a list of billing plans for an integration and product.



# List products for integration configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/list-products-for-integration-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}/products
Lists all products available for an integration configuration. Use this endpoint to discover what integration products are available for your integration configuration. The returned product IDs or slugs can then be used with storage provisioning endpoints like `POST /v1/storage/stores/integration/direct`. ## Workflow 1. Get your integration configurations: `GET /v1/integrations/configurations` 2. **Use this endpoint**: Get products for a configuration: `GET /v1/integrations/configuration/{id}/products` 3. Create storage resource: `POST /v1/storage/stores/integration/direct` ## Response Returns an array of products with their IDs, slugs, names, supported protocols, and metadata requirements. Each product represents a different type of resource you can provision. The `metadataSchema` field contains a JSON Schema that defines: - **Required metadata**: Fields that must be provided during storage creation - **Optional metadata**: Fields that can be provided but are not mandatory - **Field validation**: Data types, allowed values, and constraints Use this schema to validate metadata before calling the storage creation endpoint.



# Retrieve an integration configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/integrations/retrieve-an-integration-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/integrations/configuration/{id}
Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it.



# Creates a Configurable Log Drain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-configurable-log-drain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/log-drains
Creates a configurable log drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed)



# Creates a new Integration Log Drain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-new-integration-log-drain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/integrations/log-drains
Creates an Integration log drain. This endpoint must be called with an OAuth2 client (integration), since log drains are tied to integrations. If it is called with a different token type it will produce a 400 error.



# Deletes a Configurable Log Drain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/deletes-a-configurable-log-drain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/log-drains/{id}
Deletes a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be deleted.



# Deletes the Integration log drain with the provided `id` (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/deletes-the-integration-log-drain-with-the-provided-`id`-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/integrations/log-drains/{id}
Deletes the Integration log drain with the provided `id`. When using an OAuth2 Token, the log drain can be deleted only if the integration owns it.



# Retrieves a Configurable Log Drain (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-configurable-log-drain-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains/{id}
Retrieves a Configurable Log Drain. This endpoint must be called with a team AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated team can be accessed.



# Retrieves a list of all the Log Drains (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-all-the-log-drains-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/log-drains
Retrieves a list of all the Log Drains owned by the account. This endpoint must be called with an account AccessToken (integration OAuth2 clients are not allowed). Only log drains owned by the authenticated account can be accessed.



# Retrieves a list of Integration log drains (deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-integration-log-drains-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/integrations/log-drains
Retrieves a list of all Integration log drains that are defined for the authenticated user or team. When using an OAuth2 token, the list is limited to log drains created by the authenticated integration.



# Get logs for a deployment
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logs/get-logs-for-a-deployment

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{projectId}/deployments/{deploymentId}/runtime-logs
Returns a stream of logs for a given deployment.



# Create Event
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-event

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/events
Partner notifies Vercel of any changes made to an Installation or a Resource. Vercel is expected to use `list-resources` and other read APIs to get the new state.<br/> <br/> `resource.updated` event should be dispatched when any state of a resource linked to Vercel is modified by the partner.<br/> `installation.updated` event should be dispatched when an installation's billing plan is changed via the provider instead of Vercel.<br/> <br/> Resource update use cases: <br/> <br/> - The user renames a database in the partner’s application. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource in Vercel’s datastores.<br/> - A resource has been suspended due to a lack of use. The partner should dispatch a `resource.updated` event to notify Vercel to update the resource's status in Vercel's datastores.<br/>



# Create one or multiple experimentation items
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/create-one-or-multiple-experimentation-items

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items
Create one or multiple experimentation items



# Delete an existing experimentation item
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/delete-an-existing-experimentation-item

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
Delete an existing experimentation item



# Delete Integration Resource
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/delete-integration-resource

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/installations/{integrationConfigurationId}/resources/{resourceId}
Delete a resource owned by the selected installation ID.



# Get Account Information
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-account-information

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/account
Fetches the best account or user’s contact info



# Get Integration Resource
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resource

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources/{resourceId}
Get a resource by its partner ID.



# Get Integration Resources
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-integration-resources

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/resources
Get all resources for a given installation ID.



# Get Invoice
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-invoice

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}
Get Invoice details and status for a given invoice ID.<br/> <br/> See Billing Events with Webhooks documentation on how to receive invoice events. This endpoint is used to retrieve the invoice details.



# Get Member Information
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-member-information

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/installations/{integrationConfigurationId}/member/{memberId}
Returns the member role and other information for a given member ID ("user_id" claim in the SSO OIDC token).



# Get the data of a user-provided Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/get-the-data-of-a-user-provided-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples head /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
When the user enabled Edge Config syncing, then this endpoint can be used by the partner to fetch the contents of the Edge Config.



# Import Resource
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/import-resource

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}
This endpoint imports (upserts) a resource to Vercel's installation. This may be needed if resources can be independently created on the partner's side and need to be synchronized to Vercel.



# Invoice Actions
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/invoice-actions

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices/{invoiceId}/actions
This endpoint allows the partner to request a refund for an invoice to Vercel. The invoice is created using the [Submit Invoice API](#submit-invoice-api).



# Patch an existing experimentation item
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/patch-an-existing-experimentation-item

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/items/{itemId}
Patch an existing experimentation item



# Push data into a user-provided Edge Config
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/push-data-into-a-user-provided-edge-config

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}/experimentation/edge-config
When the user enabled Edge Config syncing, then this endpoint can be used by the partner to push their configuration data into the relevant Edge Config.



# Submit Billing Data
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-billing-data

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing
Sends the billing and usage data. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.



# Submit Invoice
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-invoice

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/invoices
This endpoint allows the partner to submit an invoice to Vercel. The invoice is created in Vercel's billing system and sent to the customer. Depending on the type of billing plan, the invoice can be sent at a time of signup, at the start of the billing period, or at the end of the billing period.<br/> <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request. <br/> There are several limitations to the invoice submission:<br/> <br/> 1. A resource can only be billed once per the billing period and the billing plan.<br/> 2. The billing plan used to bill the resource must have been active for this resource during the billing period.<br/> 3. The billing plan used must be a subscription plan.<br/> 4. The interim usage data must be sent hourly for all types of subscriptions. See [Send subscription billing and usage data](#send-subscription-billing-and-usage-data) API on how to send interim billing and usage data.<br/>



# Submit Prepayment Balances
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/submit-prepayment-balances

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/installations/{integrationConfigurationId}/billing/balance
Sends the prepayment balances. The partner should do this at least once a day and ideally once per hour. <br/> Use the `credentials.access_token` we provided in the [Upsert Installation](#upsert-installation) body to authorize this request.



# Update Installation
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-installation

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}
This endpoint updates an integration installation.



# Update Resource
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/installations/{integrationConfigurationId}/resources/{resourceId}
This endpoint updates an existing resource in the installation. All parameters are optional, allowing partial updates.



# Update Resource Secrets
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/resources/{resourceId}/secrets
This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>



# Update Resource Secrets (Deprecated)
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/marketplace/update-resource-secrets-deprecated

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/installations/{integrationConfigurationId}/products/{integrationProductIdOrSlug}/resources/{resourceId}/secrets
This endpoint is deprecated and replaced with the endpoint [Update Resource Secrets](#update-resource-secrets). <br/> This endpoint updates the secrets of a resource. If a resource has projects connected, the connected secrets are updated with the new secrets. The old secrets may still be used by existing connected projects because they are not automatically redeployed. Redeployment is a manual action and must be completed by the user. All new project connections will use the new secrets.<br/> <br/> Use cases for this endpoint:<br/> <br/> - Resetting the credentials of a database in the partner. If the user requests the credentials to be updated in the partner’s application, the partner post the new set of secrets to Vercel, the user should redeploy their application and the expire the old credentials.<br/>



# Adds a new member to a project.
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/adds-a-new-member-to-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/members
Adds a new member to the project.



# List project members
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/list-project-members

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/members
Lists all members of a project.



# Remove a Project Member
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projectmembers/remove-a-project-member

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/members/{uid}
Remove a member from a specific project



# Accept project transfer request
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /projects/transfer-request/{code}
Accept a project transfer request initated by another team. <br/> The `code` is generated using the `POST /projects/:idOrName/transfer-request` endpoint.



# Add a domain to a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/add-a-domain-to-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/domains
Add a domain to the project by passing its domain name and by specifying the project by either passing the project `id` or `name` in the URL. If the domain is not yet verified to be used on this project, the request will return `verified = false`, and the domain will need to be verified according to the `verification` challenge via `POST /projects/:idOrName/domains/:domain/verify`. If the domain already exists on the project, the request will fail with a `400` status code.



# Batch remove environment variables
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/batch-remove-environment-variables

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/env
Delete multiple environment variables for a given project in a single batch operation.



# Create a new project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-a-new-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v11/projects
Allows to create a new project with the provided configuration. It only requires the project `name` but more configuration can be provided to override the defaults.



# Create one or more environment variables
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-one-or-more-environment-variables

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{idOrName}/env
Create one or more environment variables for a project by passing its `key`, `value`, `type` and `target` and by specifying the project by either passing the project `id` or `name` in the URL. If you include `upsert=true` as a query parameter, a new environment variable will not be created if it already exists but, the existing variable's value will be updated.



# Create project transfer request
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/create-project-transfer-request

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /projects/{idOrName}/transfer-request
Initiates a project transfer request from one team to another. <br/> Returns a `code` that remains valid for 24 hours and can be used to accept the transfer request by another team using the `PUT /projects/transfer-request/:code` endpoint. <br/> Users can also accept the project transfer request using the claim URL: `https://vercel.com/claim-deployment?code=<code>&returnUrl=<returnUrl>`. <br/> The `code` parameter specifies the project transfer request code generated using this endpoint. <br/> The `returnUrl` parameter redirects users to a specific page of the application if the claim URL is invalid or expired.



# Delete a Project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/delete-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}
Delete a specific project by passing either the project `id` or `name` in the URL.



# Edit an environment variable
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/edit-an-environment-variable

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/env/{id}
Edit a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.



# Find a project by id or name
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/find-a-project-by-id-or-name

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}
Get the information for a specific project by passing either the project `id` or `name` in the URL.



# Get a project domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/get-a-project-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/domains/{domain}
Get project domain by project id/name and domain name.



# Get client certificates for a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/get-client-certificates-for-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/client-cert
Retrieve client certificates configured for a project's mTLS egress authentication.



# Gets a list of aliases with status for the current promote
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/gets-a-list-of-aliases-with-status-for-the-current-promote

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{projectId}/promote/aliases
Get a list of aliases related to the last promote request with their mapping status



# Move a project domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/move-a-project-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/domains/{domain}/move
Move one project's domain to another project. Also allows the move of all redirects pointed to that domain in the same project.



# Pause a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/pause-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{projectId}/pause
Pause a project by passing its project `id` in the URL. If the project does not exist given the id then the request will fail with 400 status code. If the project disables auto assigning custom production domains and blocks the active Production Deployment then the request will return with 200 status code.



# Points all production domains for a project to the given deploy
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/points-all-production-domains-for-a-project-to-the-given-deploy

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v10/projects/{projectId}/promote/{deploymentId}
Allows users to promote a deployment to production. Note: This does NOT rebuild the deployment. If you need that, then call create-deployments endpoint.



# Remove a domain from a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/remove-a-domain-from-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/domains/{domain}
Remove a domain from a project by passing the domain name and by specifying the project by either passing the project `id` or `name` in the URL.



# Remove an environment variable
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/remove-an-environment-variable

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v9/projects/{idOrName}/env/{id}
Delete a specific environment variable for a given project by passing the environment variable identifier and either passing the project `id` or `name` in the URL.



# Retrieve a list of projects
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-a-list-of-projects

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects
Allows to retrieve the list of projects of the authenticated user or team. The list will be paginated and the provided query parameters allow filtering the returned projects.



# Retrieve project domains by project by id or name
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-project-domains-by-project-by-id-or-name

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v9/projects/{idOrName}/domains
Retrieve the domains associated with a given project by passing either the project `id` or `name` in the URL.



# Retrieve the decrypted value of an environment variable of a project by id
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-the-decrypted-value-of-an-environment-variable-of-a-project-by-id

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/env/{id}
Retrieve the environment variable for a given project.



# Retrieve the environment variables of a project by id or name
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/retrieve-the-environment-variables-of-a-project-by-id-or-name

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v10/projects/{idOrName}/env
Retrieve the environment variables for a given project by passing either the project `id` or `name` in the URL.



# Unpause a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/unpause-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{projectId}/unpause
Unpause a project by passing its project `id` in the URL. If the project does not exist given the id then the request will fail with 400 status code. If the project enables auto assigning custom production domains and unblocks the active Production Deployment then the request will return with 200 status code.



# Update a project domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-a-project-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}/domains/{domain}
Update a project domain's configuration, including the name, git branch and redirect of the domain.



# Update an existing project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-an-existing-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v9/projects/{idOrName}
Update the fields of a project using either its `name` or `id`.



# Update Protection Bypass for Automation
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-protection-bypass-for-automation

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/protection-bypass
Update the deployment protection automation bypass for a project



# Update the data cache feature
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-the-data-cache-feature

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/data-cache/projects/{projectId}
Update the data cache feature on a project.



# Upload client certificate for egress mTLS
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/upload-client-certificate-for-egress-mtls

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/client-cert
Upload a client certificate for mTLS authentication to external origins.



# Verify project domain
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/verify-project-domain

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v9/projects/{idOrName}/domains/{domain}/verify
Attempts to verify a project domain with `verified = false` by checking the correctness of the project domain's `verification` challenge.



# Complete the rolling release for the project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/complete-the-rolling-release-for-the-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/rolling-release/complete
Force-complete a Rolling Release. The canary deployment will begin serving 100% of the traffic.



# Delete rolling release configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/delete-rolling-release-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/projects/{idOrName}/rolling-release/config
Disable Rolling Releases for a project means that future deployments will not undergo a rolling release. Changing the config never alters a rollout that's already in-flight—it only affects the next production deployment. If you want to also stop the current rollout, call this endpoint to disable the feature, and then call either the /complete or /abort endpoint.



# Get rolling release billing status
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-billing-status

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/billing
Get the Rolling Releases billing status for a project. The team level billing status is used to determine if the project can be configured for rolling releases.



# Get rolling release configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/config
Get the Rolling Releases configuration for a project. The project-level config is simply a template that will be used for any future rolling release, and not the configuration for any active rolling release.



# Get the active rolling release information for a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-the-active-rolling-release-information-for-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release
Return the Rolling Release for a project, regardless of whether the rollout is active, aborted, or completed. If the feature is enabled but no deployment has occurred yet, null will be returned.



# Update the active rolling release to the next stage for a project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/update-the-active-rolling-release-to-the-next-stage-for-a-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{idOrName}/rolling-release/approve-stage
Advance a rollout to the next stage. This is only needed when rolling releases is configured to require manual approval.



# Update the rolling release settings for the project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/update-the-rolling-release-settings-for-the-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/rolling-release/config
Update (or disable) Rolling Releases for a project. Changing the config never alters a rollout that's already in-flight. It only affects the next production deployment. This also applies to disabling Rolling Releases. If you want to also stop the current rollout, call this endpoint to disable the feature, and then call either the /complete or /abort endpoint. Note: Enabling Rolling Releases automatically enables skew protection on the project with the default value if it wasn't configured already.



# Create System Bypass Rule
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/create-system-bypass-rule

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/security/firewall/bypass
Create new system bypass rules



# Put Firewall Configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/put-firewall-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /v1/security/firewall/config
Set the firewall configuration to provided rules and settings. Creates or overwrite the existing firewall configuration.



# Read active attack data
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-active-attack-data

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/attack-status
Retrieve active attack data within the last N days (default: 1 day)



# Read Firewall Actions by Project
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-actions-by-project

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/events
Retrieve firewall actions for a project



# Read Firewall Configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-firewall-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/config/{configVersion}
Retrieve the specified firewall configuration for a project. The deployed configVersion will be `active`



# Read System Bypass
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/read-system-bypass

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/security/firewall/bypass
Retrieve the system bypass rules configured for the specified project



# Remove System Bypass Rule
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/remove-system-bypass-rule

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/security/firewall/bypass
Remove system bypass rules



# Update Attack Challenge mode
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/update-attack-challenge-mode

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/security/attack-mode
Update the setting for determining if the project has Attack Challenge mode enabled.



# Update Firewall Configuration
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/security/update-firewall-configuration

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/security/firewall/config
Process updates to modify the existing firewall config for a project



# Create a Team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/create-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams
Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name.



# Delete a Team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}
Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent.



# Delete a Team invite code
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/delete-a-team-invite-code

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/invites/{inviteId}
Delete an active Team invite code.



# Get a Team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams/{teamId}
Get information for the Team specified by the `teamId` parameter.



# Get access request status
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/get-access-request-status

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/teams/{teamId}/request/{userId}
Check the status of a join request. It'll respond with a 404 if the request has been declined. If no `userId` path segment was provided, this endpoint will instead return the status of the authenticated user.



# Invite a user
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/invite-a-user

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members
Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user to be invited must be specified by email.



# Join a team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/join-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/members/teams/join
Join a team with a provided invite code or team ID.



# List all teams
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/list-all-teams

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/teams
Get a paginated list of all the Teams the authenticated User is a member of.



# List team members
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/list-team-members

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/teams/{teamId}/members
Get a paginated list of team members for the provided team.



# Remove a Team Member
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/remove-a-team-member

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/teams/{teamId}/members/{uid}
Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team.



# Request access to a team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/request-access-to-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams/{teamId}/request
Request access to a team as a member. An owner has to approve the request. Only 10 users can request access to a team at the same time.



# Update a Team
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-a-team

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v2/teams/{teamId}
Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team.



# Update a Team Member
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/update-a-team-member

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/teams/{teamId}/members/{uid}
Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team.



# Delete User Account
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/delete-user-account

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/user
Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process.



# Get the User
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/get-the-user

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/user
Retrieves information related to the currently authenticated User.



# List User Events
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/list-user-events

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v3/events
Retrieves a list of "events" generated by the User on Vercel. Events are generated when the User performs a particular action, such as logging in, creating a deployment, and joining a Team (just to name a few). When the `teamId` parameter is supplied, then the events that are returned will be in relation to the Team that was specified.



# Creates a webhook
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/creates-a-webhook

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/webhooks
Creates a webhook



# Deletes a webhook
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/deletes-a-webhook

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/webhooks/{id}
Deletes a webhook



# Get a list of webhooks
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/get-a-list-of-webhooks

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/webhooks
Get a list of webhooks



# Get a webhook
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/webhooks/get-a-webhook

https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/webhooks/{id}
Get a webhook



# Errors
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/errors

List of general and specific errors you may encounter when using the REST API.

## Generic Errors

These error codes are consistent for all endpoints.

### Forbidden

You're not authorized to use the endpoint. This usually happens due to missing an user token.

<Note>Similar to the HTTP 403 Forbidden error.</Note>

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "Not authorized"
  }
}
```

### Rate Limited

You exceeded the maximum allotted requests.

The limit of request is per endpoint basis so you could continue using another endpoints even if some of them give you this error.

```json error-response-rate-limited theme={"system"}
{
  "error": {
    "code": "rate_limited",
    "message": "The rate limit of 6 exceeded for 'api-www-user-update-username'. Try again in 7 days",
    "limit": {
      "remaining": 0,
      "reset": 1571432075,
      "resetMs": 1571432075563,
      "total": 6
    }
  }
}
```

### Bad Request

There was an error with the request, the `error.message` would contain information about the issue.

```json error-response-bad-request theme={"system"}
{
  "error": {
    "code": "bad_request",
    "message": "An english description of the error that just occurred"
  }
}
```

### Internal Server Error

This errors is similar to the HTTP 500 Internal Server Error error code.

```json error-response-internal-server-error theme={"system"}
{
  "error": {
    "code": "internal_server_error",
    "message": "An unexpected internal error occurred"
  }
}
```

### Resource Not Found

The requested resource could not be found

```json error-response-not-Found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "Could not find the RESOURCE: ID"
  }
}
```

### Method Unknown

The endpoint you're requesting does not handle the method you defined. The error message will contain the methods the endpoint responds to.

```json error-response-method-unknown theme={"system"}
{
  "error": {
    "code": "method_unknown",
    "message": "This endpoint only responds to METHOD"
  }
}
```

## Deployment Errors

These error codes can happen when using any [deployment related endpoint](/endpoints/deployments/get-deployment-events).

### Missing Files

Some of the files you defined when creating the deployment are missing.

```json error-response-missing-files theme={"system"}
{
  "error": {
    "code": "missing_files",
    "message": "Missing files",
    "missing": []
  }
}
```

### No Files in the Deployment

You tried to create an empty deployment.

```json error-response-no-files theme={"system"}
{
  "error": {
    "code": "no_files",
    "message": "No files in the deployment"
  }
}
```

### Too Many Environment Variables

The limit of environment variables per deployment is 100 and you defined more. The error message indicates the amount you define.

```json error-response-too-many-env-keys theme={"system"}
{
  "error": {
    "code": "env_too_many_keys",
    "message": "Too many env vars have been supplied (100 max allowed, but got #)"
  }
}
```

<Note>
  `#`is your number of variables.
</Note>

### Environment Variable Key with Invalid Characters

Some environment variable name contains an invalid character. The only valid characters are letters, digits and `_`.

The error message will contain the `KEY` with the problem.

```json error-response-env-key-invalid-characters theme={"system"}
{
  "error": {
    "code": "env_key_invalid_characters",
    "message": "The env key "KEY" contains invalid characters. Only letters, digits and \`_\` are allowed",
    "key": KEY
  }
}
```

### Environment Variable Key with a Long Name

An environment variable name is too long, the maximum permitted name is 256 characters.

The error message contains the environment `KEY`.

```json error-response-env-key-invalid-length theme={"system"}
{
  "error": {
    "code": "env_key_invalid_length",
    "message": "The env key "KEY" exceeds the 256 length limit",
    "key": KEY
  }
}
```

### Environment Variable Value with a Long Name

An environment variable value contains a value too long, the maximum permitted value is 65536 characters.

The error message contains the environment `KEY`.

```json error-response-env-value-invalid-length theme={"system"}
{
  "error": {
    "code": "env_value_invalid_length",
    "message": "The env value for "KEY" exceeds the 65536 length limit",
    "key": KEY,
    "value": VALUE
  }
}
```

### Environment Variable Value Is an Object without UID

The value of an environment variable is object but it doesn't have a `uid`.

The error message contains the environment `KEY` which has the error.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type_missing_uid",
    "message": "The env key "KEY" passed an object as a value with no \`uid\` key"
  }
}
```

### Environment Variable Value Is an Object with Unknown Props

The value of an environment variable is an object with unknown attributes, it only can have a `uid` key inside the object.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type_unknown_props",
    "message": "The env key "KEY" passed an object with unknown properties. Only \`uid\` is allowed when passing an object"
  }
}
```

### Environment Variable Value with an Invalid Type

An environment variable value passed is of an unsupported type.

The error message contains the environment `KEY`.

```json error-response-env-value-invalid-type theme={"system"}
{
  "error": {
    "code": "env_value_invalid_type",
    "message": "The env key "KEY" passed an unsupported type for its value",
    "key": KEY
  }
}
```

### Not Allowed to Access a Secret

You're trying to use a secret but you don't have access to it.

```json error-response-secret-forbidden theme={"system"}
{
  "error": {
    "code": "env_secret_forbidden",
    "message": "Not allowed to access secret \\"NAME\\"",
    "uid": UID
  }
}
```

### Missing Secret

You're trying to use a secret as an environment value and it doesn't exists.

```json error-response-secret-missing theme={"system"}
{
  "error": {
    "code": "env_secret_missing",
    "message": "Could not find a secret by uid "UID"",
    "uid": UID
  }
}
```

## Domain Errors

These error code could happen when using any [domains related endpoints](/endpoints/domains-registrar/buy-a-domain).

### Domain Forbidden

You don't have access to the domain, this usually mean this domains is owned by another account or team.

The domain is specified in the message and the `DOMAIN` key.

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "You don't have access to \\"DOMAIN\\"",
    "domain": DOMAIN
  }
}
```

### Domain Not Found

The domain name could not be found in our system. Try to [add it first](/endpoints/domains-registrar/transfer-in-a-domain).

```json error-response-not-found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "Domain name not found"
  }
}
```

### Missing Domain Name

The domain name wasn't specified in the URL. This means you tried to use an endpoint which require you to define the domain name in the URL but didn't defined it.

```json error-response-missing-name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "The URL was expected to include the domain name. Example: /domains/google.com"
  }
}
```

### Conflicting Aliases

You must [remove the aliases](/endpoints/aliases/delete-an-alias#delete-an-alias) described in the error before removing the domains.

The aliases are specified in the `ALIASES` key.

```json error-response-conflict-alias theme={"system"}
{
  "error": {
    "code": "conflict_aliases",
    "message": "The following aliases must be removed before removing the domain: ALIASES",
    "aliases": ALIASES
  }
}
```

### Not Modified

When trying to modify a domain nothing was required to change.

```json error-response-not-modified theme={"system"}
{
  "error": {
    "code": "not_modified",
    "message": "Nothing to do"
  }
}
```

### Missing Name for Domain

When trying to add a domain the name wasn't present in the request body.

```json error-response-missing-name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "The `name` field in the body was expected but is not present in the body payload. Example value: `example.com`"
  }
}
```

### Invalid Name for Domain

The domain name defined in the request body is invalid.

The name is specified in the error as the `NAME` key.

```json error-response-invalid-name theme={"system"}
{
  "error": {
    "code": "invalid_name",
    "message": "The \`name\` field contains an invalid domain name ("NAME")",
    "name": NAME
  }
}
```

### Custom Domain Needs a Plan Upgrade

In order to add a custom domain to your account or team you need to upgrade to a paid plan.

```json error-response-domain-needs-upgrade theme={"system"}
{
  "error": {
    "code": "custom_domain_needs_upgrade",
    "message": "Domain name creation requires a premium account."
  }
}
```

### Domain Already Exists

The domain name you're trying to add already exists.

The domain name and its current ID are received in the `NAME` and `DOMAIN_ID` keys.

```json error-response-not-modified theme={"system"}
{
  "error": {
    "code": "not_modified",
    "message": "The domain "NAME" already exists",
    "name": NAME,
    "uid": DOMAIN_ID
  }
}
```

### Can't Create the Domain

The domain name can't be created. Most probably it couldn't be verified.

```json error-response-forbidden theme={"system"}
{
  "error": {
    "code": "forbidden",
    "message": "You don't have permission to create a domain"
  }
}
```

### Failed to Add Domain after Purchase

We were able to purchase a domain for you but we had an error when trying to add it to your account. Please contact us on **[Contact Support](https://vercel.com/help)**.

```json error-response-failed-add-domain theme={"system"}
{
  "error": {
    "code": "failed_to_add_domain",
    "message": "The domain was bought but couldn't be added.
  }
}
```

### Unable to Determine the Domain Price

We're unable to determine the domain price of a domain.

```json error-response-service-unavailable theme={"system"}
{
  "error": {
    "code": "service_unavailable",
    "message": "Failed to determine the domain price"
  }
}
```

### Domain price mismatch

The `expectedPrice` supplied in the request body does not match the actual domain price, which is specified in the `actualPrice` key.

```json error-response-price-mismatch theme={"system"}
{
  "error": {
    "code": "price_mismatch",
    "message": "The expected price does not match the actual price",
    "price": ACTUAL_PRICE
  }
}
```

### Domain Is Not Available

The domain name is not available to be purchased.

```json error-response-not-available theme={"system"}
{
  "error": {
    "code": "not_available",
    "message": "Domain is not available"
  }
}
```

### Invalid Domain Name

The domain name or TLD is invalid or not supported.

```json error-response-invalid-domain theme={"system"}
{
  "error": {
    "code": "invalid_domain",
    "message": "Invalid domain or TLD"
  }
}
```

### Missing DNS Record Name

The DNS record key `name` is required and was not provided. It could be [any valid DNS record](https://en.wikipedia.org/wiki/List_of_DNS_record_types).

```json error-response-missing-type theme={"system"}
{
  "error": {
    "code": "missing_type",
    "message": "Missing `type` parameter"
  }
}
```

## DNS Errors

These error code could happen when using any [DNS related endpoint](/endpoints/dns/list-existing-dns-records).

### Missing DNS Record Name

The DNS record key `name` is required and was not provided. It should be either a subdomain or `@` for the domain itself.

```json error-response-missing-Name theme={"system"}
{
  "error": {
    "code": "missing_name",
    "message": "Missing `name` parameter"
  }
}
```

### Missing DNS Record Type

The DNS record key `name` is required and was not provided. It could be [any valid DNS record](https://en.wikipedia.org/wiki/List_of_DNS_record_types).

```json error-response-missing-type theme={"system"}
{
  "error": {
    "code": "missing_type",
    "message": "Missing `type` parameter"
  }
}
```

## OAuth2 errors

These errors could occur when using any [OAuth2 related endpoint](https://vercel.com/docs/integrations/vercel-api-integrations#create-an-access-token).

### Client Not Found

The OAuth2 client ID could not be found or doesn't exist.

```json error-response-not-found theme={"system"}
{
  "error": {
    "code": "not_found",
    "message": "OAuth client doesn't not found: CLIENT_ID"
  }
}
```


# Deployment Automation
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/deployments-automation

Learn how to use the Vercel SDK through real-life examples.

## Create a deployment

In this example, you will trigger a new deployment from a GitHub repository and then retrieve its status.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createAndCheckDeployment() {
  try {
    // Create a new deployment
    const createResponse = await vercel.deployments.createDeployment({
      requestBody: {
        name: 'my-project', //The project name used in the deployment URL
        target: 'production',
        gitSource: {
          type: 'github',
          repo: 'repo-name',
          ref: 'main',
          org: 'org-name', //For a personal account, the org-name is your GH username
        },
      },
    });

    console.log(
      `Deployment created: ID ${createResponse.id} and status ${createResponse.status}`,
    );
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createAndCheckDeployment();
```

## Create a deployment with alias

In this example, you will create a deployment, wait for it to complete, and then create an alias if successful.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createDeploymentAndAlias() {
  try {
    // Create a new deployment
    const createResponse = await vercel.deployments.createDeployment({
      requestBody: {
        name: 'my-project', //The project name used in the deployment URL
        target: 'production',
        gitSource: {
          type: 'github',
          repo: 'repo-name',
          ref: 'main',
          org: 'org-name', //For a personal account, the org-name is your GH username
        },
      },
    });

    const deploymentId = createResponse.id;

    console.log(
      `Deployment created: ID ${deploymentId} and status ${createResponse.status}`,
    );

    // Check deployment status
    let deploymentStatus;
    let deploymentURL;
    do {
      await new Promise((resolve) => setTimeout(resolve, 5000)); // Wait 5 seconds between checks

      const statusResponse = await vercel.deployments.getDeployment({
        idOrUrl: deploymentId,
        withGitRepoInfo: 'true',
      });

      deploymentStatus = statusResponse.status;
      deploymentURL = statusResponse.url;
      console.log(`Deployment status: ${deploymentStatus}`);
    } while (
      deploymentStatus === 'BUILDING' ||
      deploymentStatus === 'INITIALIZING'
    );

    if (deploymentStatus === 'READY') {
      console.log(`Deployment successful. URL: ${deploymentURL}`);

      const aliasResponse = await vercel.aliases.assignAlias({
        id: deploymentId,
        requestBody: {
          alias: `my-project-alias.vercel.app`,
          redirect: null,
        },
      });

      console.log(`Alias created: ${aliasResponse.alias}`);
    } else {
      console.log('Deployment failed or was canceled');
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createDeploymentAndAlias();
```


# Domain Management
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/domain-management

Learn how to use the Vercel SDK through real-life examples.

## Add a domain

In this example, you will add a new domain to a project and check its configuration.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function addAndReviewDomain() {
  const domain = 'www.example.com';

  try {
    // Add a new domain
    const addDomainResponse = await vercel.projects.addProjectDomain({
      idOrName: 'my-project', //The project name used in the deployment URL
      requestBody: {
        name: domain,
      },
    });

    console.log(`Domain added: ${addDomainResponse.name}`);
    console.log('Domain Details:', JSON.stringify(addDomainResponse, null, 2));
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

addAndReviewDomain();
```

## Add a domain, verify it and setup a redirect

In this example, you will add a custom domain, verify it, and set up a redirect from a subdomain to the main domain.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setupDomainWithRedirect() {
  const mainDomain = 'example.com';
  const subDomain = 'hello.example.com';
  const projectName = 'my-project'; //The project name used in the deployment URL

  try {
    // Add main domain
    const mainDomainResponse = await vercel.projects.addProjectDomain({
      idOrName: projectName,
      requestBody: {
        name: mainDomain,
      },
    });

    console.log(`Main domain added: ${mainDomainResponse.name}`);

    const checkConfiguration = await vercel.domains.getDomainConfig({
      domain: mainDomain,
    });

    if (mainDomainResponse.verified && !checkConfiguration.misconfigured) {
      // Add subdomain with 301 redirect to main domain
      const subDomainResponse = await vercel.projects.addProjectDomain({
        idOrName: projectName,
        requestBody: {
          name: subDomain,
          redirect: `https://${mainDomain}`,
          redirectStatusCode: 301,
        },
      });

      console.log(`Subdomain added and redirect set up: ${subDomain}`);
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

setupDomainWithRedirect();
```


# Environment Variables
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/environment-variables

Learn how to use the Vercel SDK through real-life examples.

## Add environment variables to a project

In this example, you will add new environment variables to a project and list the details of the added values.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const projectName = 'my-project'; //The project name used in the deployment URL

async function addAndListEnvVars() {
  try {
    // Add new environment variables
    const addResponse = await vercel.projects.createProjectEnv({
      idOrName: projectName,
      upsert: 'true',
      requestBody: [
        {
          key: 'API_KEY',
          value: 'secret_value',
          target: ['production', 'preview'],
          type: 'encrypted',
        },
        {
          key: 'DEBUG',
          value: 'true',
          target: ['development'],
          type: 'plain',
        },
      ],
    });
    console.log(
      'Added environment variables:',
      JSON.stringify(addResponse, null, 2),
    );
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

addAndListEnvVars();
```

## Manage variables across projects

In this example, you manage environment variables across multiple projects and environments.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import { OneTarget } from '@vercel/sdk/models/operations/createprojectenv';

const PROJECTS = ['project-id-1', 'project-id-2', 'project-id-3'];
const environments = ['development', 'preview', 'production'];
const VERCEL_TOKEN = process.env.VERCEL_TOKEN;

const vercel = new Vercel({
  bearerToken: VERCEL_TOKEN,
});

async function manageEnvironmentVariables() {
  try {
    const variables = [
      { key: 'API_URL', value: 'https://api.example.com' },
      { key: 'DEBUG', value: 'true', environments: ['development', 'preview'] },
      {
        key: 'SECRET_KEY',
        value: 'super-secret-key',
        encrypt: true,
        environments: ['production', 'preview'],
      },
    ];

    for (const projectId of PROJECTS) {
      console.log(`Managing environment variables for project: ${projectId}`);
      for (const variable of variables) {
        const targets =
          (variable.environments as OneTarget[]) ||
          (environments as OneTarget[]);

        const addEnv = await vercel.projects.createProjectEnv({
          idOrName: projectId,
          upsert: 'true',
          requestBody: {
            key: variable.key,
            value: variable.value,
            target: targets,
            type: variable.encrypt ? 'encrypted' : 'plain',
          },
        });
        console.log(addEnv.created);
      }
      const readEnvs = await vercel.projects.filterProjectEnvs({
        idOrName: projectId,
      });
      console.log(
        'Env Details for ',
        projectId,
        ':',
        JSON.stringify(readEnvs, null, 2),
      );
    }
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

manageEnvironmentVariables();
```


# Vercel WAF Management
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/firewall-management

Learn how to use the Vercel SDK through real-life examples.

## Add custom rules

In this example, you create a new custom rule to protect your application against SQL injection threats.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function insertCustomRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.insert",
      id: null, // null for new rules
      value: {
        active: true,
        name: "Block SQL Injection Attempts",
        description: "Block requests with SQL injection patterns in query parameters",
        conditionGroup: [
          {
            conditions: [
              {
                op: "inc", // Contains
                type: "query",
                value: "SELECT",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "deny",
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

insertCustomRule()
```

## Modify existing rules

In this example, you update an existing custom rule's configuration. This is useful When you need to programmatically adjust conditions, actions, or status of an existing rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateExistingRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.update",
      id: "existing-rule-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: {
        active: true,
        name: "Updated Rule Name",
        description: "Updated rule description",
        conditionGroup: [
          {
            conditions: [
              {
                op: "pre",
                type: "path",
                value: "/admin",
              },
            ],
          },
        ],
        action: {
          mitigate: {
            action: "challenge", // Changed from previous setting
            rateLimit: null,
            redirect: null,
            actionDuration: null,
          },
        },
      },
    },
  });
}

updateExistingRule()
```

## Delete custom rules

In this example, you delete an existing custom rule.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function deleteRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.remove",
      id: "rule-to-delete-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: null, // No value needed for deletion
    },
  });
}

deleteRule()
```

## Change rule priority

This parameter applies when you have more than one custom rule in your project. By default, the priority is determined based on the order in which the rules are added. You can change this in the Vercel dashboard by re-ordering the rules in the [Firewall Configure](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules#custom-rule-configuration) project page **or** by using the endpoint below.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function reorderRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", //Not required but sometimes needed if the endpoint requires that you authenticate as a specific team - your token should also have access to this scope
    requestBody: {
      action: "rules.priority",
      id: "rule-to-update-priority-id", //You can find the id by using the rules array of the Read Firewall Configuration endpoint
      value: 1, //Use the rules array of the Read Firewall Configuration endpoint to determine what array position you would like this rule to move to. The minimum is 0 and the maximum is the length of the array
    },
  });
}

reorderRules()

```

## Custom system bypass rule

The [WAF system bypass rules](https://vercel.com/docs/vercel-firewall/vercel-waf/system-bypass-rules) allow you to have specific IP addresses or CIDRs bypass the system-level mitigations such as [DDoS Mitigation](https://vercel.com/docs/vercel-firewall/ddos-mitigation). For more complex filters, you can use REST API directly.

For example, to allow mobile applications to bypass the system-level mitigations, use the following code to create a [Custom Rule](https://vercel.com/docs/vercel-firewall/vercel-waf/custom-rules) in your project. This condition will match mobile devices as well as other clients that emit mobile `user_agent` values.

<Note>
  Bypassing system-level mitigations with the API is currently in beta. Contact [support](https://vercel.com/help) if you would like to use it.
</Note>

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
});

async function run() {
  const result = await vercel.security.updateFirewallConfig({
    projectId: "<your_project_id>",
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
    requestBody: {
      action: "rules.insert",
      id: null,
      value: {
        name: "Mobile App Bypass Security Rule",
        description: "Custom system bypass rule targeting mobile applications",
        active: true,
        conditionGroup: [
          {
            conditions: [
              {
                type: "user_agent",
                op: "re",
                neg: false,
                value: "Mobile|Android|iPhone|iPad"
              }
            ]
          }
        ],
        action: {
          mitigate: {
            action: "bypass",
            bypassSystem: true
          }
        }
      }
    },
  });

  // Handle the result
  console.log(result);
}

run();
```

## Update an OWASP rule

In this example, you update a specific rule from the [OWASP ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) in your project using `crs.update`. You specify the rule to update by using its name in the `id` field.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateOwaspRule() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.update",
      id: "xss", // eg. "sd", "max", "lfi", "rfi", "rce", "php", "gen", "xss", "sqli", "sf", "java"
      value: {
        active: true, // Enable the rule
        action: "log", // e.g. "deny" | "log" 
      },
    },
  });
}

updateOwaspRule()
```

## Disable all OWASP rules

This example disables all [OWASP rules](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets#configure-owasp-core-ruleset) for the project. It is a shortcut equivalent to setting every OWASP rule to `active = false`.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function disableOWASPRules() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "crs.disable",
      id: null,
      value: null,
    },
  });
}

disableOWASPRules()
```

## Update a managed ruleset

Use `managedRules.update`  with the ruleset name as `id` to enable/disable the ruleset and update the firewall action for that [managed ruleset](https://vercel.com/docs/vercel-firewall/vercel-waf/managed-rulesets) for the project.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function updateManagedRuleset() {
  await vercel.security.updateFirewallConfig({
    projectId: "your-project-id",
    teamId: "your-team-id", // Not required in all cases
    requestBody: {
      action: "managedRules.update",
      id: "bot_protection", // eg. "owasp", "bot_protection", "ai_bots", "bot_filter"
      value: {
        active: true, // Enable the ruleset
        action: "log", // e.g. "deny" | "log" | "challenge"
      },
    },
  });
}

updateManagedRuleset()
```


# Integrations
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/integrations

Learn how to use the Vercel SDK through real-life examples.

## List integration information

In this example, you list the available integrations in your account.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function listAccountIntegrations() {
  try {
    // List available integrations in the account connected with the Vercel token
    const integrationsResponse = await vercel.integrations.getConfigurations({
      view: 'account',
    });

    integrationsResponse.forEach((config) => {
      console.log(
        `- ${config.slug}: ${
          config.installationType ? `${config.installationType}` : ``
        }integration installed in ${config.projects?.join(' ')}`,
      );
    });
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

listAccountIntegrations();
```


# Logs and Monitoring
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/logs-monitoring

Learn how to use the Vercel SDK through real-life examples.

## Get deployment logs and check status

In this example, you retrieve the deployment logs and check the deployment status.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function getLogsAndStatus() {
  try {
    // Get deployment logs
    const logsResponse = await vercel.deployments.getDeploymentEvents({
      idOrUrl: 'project-name-uniqueid.vercel.app',
    });
    if (Array.isArray(logsResponse)) {
      if ('deploymentId' in logsResponse[0]) {
        const deploymentID = logsResponse[0].deploymentId;
        const deploymentStatus = await vercel.deployments.getDeployment({
          idOrUrl: deploymentID,
        });
        console.log(
          `Deployment with id, ${deploymentID} status is ${deploymentStatus.status}`,
        );
      }
      //Display logs with log type, timestamp and text
      for (const item of result) {
        if ('text' in item) {
          console.log(
            `${item.type} at ${new Date(item.created).toLocaleTimeString()}: ${
              item.text
            }`,
          );
        }
      }
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

getLogsAndStatus();
```

## Aggregate logs and send alerts

Create a custom monitoring system that aggregates logs from multiple deployments, analyzes them for errors, and sends alerts if certain thresholds are exceeded.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';
import * as nodemailer from 'nodemailer';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});
const ALERT_EMAIL = 'alerts@example.com';

interface Log {
  type: string;
  created: number;
  text: string;
}

async function monitorDeployments() {
  try {
    // Get recent deployments
    const deploymentsResponse = await vercel.deployments.getDeployments({
      limit: 5,
      projectId: 'my-project', //The project name used in the deployment URL
    });

    let totalErrors = 0;
    let totalWarnings = 0;

    for (const deployment of deploymentsResponse.deployments) {
      console.log(`Analyzing deployment: ${deployment.uid}`);
      const logsResponse = await vercel.deployments.getDeploymentEvents({
        idOrUrl: deployment.uid,
      });

      if (Array.isArray(logsResponse)) {
        const logs = logsResponse as Log[];
        const errors = logs.filter((log) => log.type === 'error');
        const warnings = logs.filter((log) => log.type === 'warning');
        totalErrors += errors.length;
        totalWarnings += warnings.length;
        console.log(`Errors: ${errors.length}, Warnings: ${warnings.length}`);
        errors.forEach((error) => console.log(`Error: ${error.text}`));
      }
    }

    console.log(
      `Total Errors: ${totalErrors}, Total Warnings: ${totalWarnings}`,
    );

    // Send alert if thresholds are exceeded
    if (totalErrors > 10 || totalWarnings > 20) {
      const transporter = nodemailer.createTransport({
        host: 'smtp.example.com',
        port: 587,
        secure: false,
        auth: {
          user: 'your_email@example.com',
          pass: process.env.email_pwd,
        },
      });

      await transporter.sendMail({
        from: '"Vercel Monitor" <monitor@example.com>',
        to: ALERT_EMAIL,
        subject: 'Deployment Alert: High number of errors or warnings',
        text: `Alert: ${totalErrors} errors and ${totalWarnings} warnings detected in recent deployments.`,
      });

      console.log('Alert email sent');
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

monitorDeployments();
```


# Project Management
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/project-management

Learn how to use the Vercel SDK through real-life examples.

## Create a new project

In this example, you will create a new project and retrieve its details. You will use the following method:

* Create project

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function createAndGetProject() {
  try {
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'my-new-project',
        framework: 'nextjs',
      },
    });

    console.log(`Project created: ${createResponse.id}`);
    console.log('Project Details:', JSON.stringify(createResponse, null, 2));
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

createAndGetProject();
```

## Create a new project with additional setup

In this example, you will create a new project, add environment variables, and set up automatic GitHub deployments.

* Create project
* Create env

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setupProjectWithGitHub() {
  try {
    // Create a new project with GH integration
    const createResponse = await vercel.projects.createProject({
      requestBody: {
        name: 'advanced-project',
        framework: 'nextjs',
        gitRepository: {
          repo: 'your-username-or-orgname/your-repo-name', //The repository should have been created before and the GH account is connected to your Vercel account
          type: 'github',
        },
      },
    });

    console.log(`Project created: ${createResponse.id}`);

    const envResponse = await vercel.projects.createProjectEnv({
      idOrName: createResponse.id,
      upsert: 'true',
      requestBody: [
        {
          key: 'DATABASE_URL',
          value: 'postgresql://user:pass@host:5432/db',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production', 'preview'],
        },
        {
          key: 'API_KEY',
          value: 'your-api-key',
          type: 'encrypted', // Encrypted when saved and viewable in the Vercel dashboard with correct permissions
          target: ['production'],
        },
        {
          key: 'API_URL',
          value: 'your-api-url',
          type: 'plain',
          target: ['production', 'preview'],
        },
      ],
    });

    console.log('Environment variables added:', envResponse.created);
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

setupProjectWithGitHub();
```


# Rolling Releases Management
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/rolling-releases

Learn how to use the Vercel SDK to manage Rolling Releases through real-life examples.

## Updating your project's rolling release configuration

In this example, you configure rolling releases for your project with multiple stages. This allows you to gradually roll out deployments to production, starting with a small percentage of traffic and progressively increasing it.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function setRollingReleaseConfig() {
  const result = await vercel.rollingRelease.updateRollingReleaseConfig({
    idOrName: "your-project-id", // Can be project ID or URL-encoded project name
    teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional - required if your token is scoped to multiple teams
    slug: "my-team-url-slug", // Optional - alternative to teamId
    requestBody: {
      target: "production",
      stages: [
        {
          targetPercentage: 5,     // Start with 5% of traffic
          duration: 300           // Wait 5 minutes before next stage
        },
        {
          targetPercentage: 25,    // Then 25% of traffic
          duration: 600           // Wait 10 minutes
        },
        {
          targetPercentage: 50,    // Then 50% of traffic
          duration: 900           // Wait 15 minutes if approved
        },
        {
          targetPercentage: 100,   // Finally, 100% of traffic
        }
      ]
    }
  });

  console.log("Rolling Release Configuration Updated:", result.rollingRelease);
}

setRollingReleaseConfig();
```

## Approve the next stage of a rolling release

In this example, you manually approve advancing a rolling release to the next stage. This is useful when you have stages configured with `requireApproval: true` and want to control the rollout progression.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function approveNextStage() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status to understand the current state
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Next stage: ${rollingRelease.nextStage?.index} (${rollingRelease.nextStage?.targetPercentage}% traffic)`);

    if (!rollingRelease.nextStage) {
      console.log("Rolling release is already at the final stage");
      return;
    }

    if (!rollingRelease.nextStage.requireApproval) {
      console.log("Next stage does not require manual approval");
      return;
    }

    // Approve advancing to the next stage
    const approvalResult = await vercel.rollingRelease.approveRollingReleaseStage({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        nextStageIndex: rollingRelease.nextStage.index,
        canaryDeploymentId: rollingRelease.canaryDeployment?.id || "",
      },
    });

    console.log("✓ Rolling release stage approved successfully!");
    console.log(`Advanced to stage ${approvalResult.rollingRelease?.activeStage?.index} (${approvalResult.rollingRelease?.activeStage?.targetPercentage}% traffic)`);

    // Display updated rollout information
    if (approvalResult.rollingRelease?.nextStage) {
      console.log(`Next stage will be: ${approvalResult.rollingRelease.nextStage.index} (${approvalResult.rollingRelease.nextStage.targetPercentage}% traffic)`);
    } else {
      console.log("This was the final stage - rolling release will complete automatically");
    }

  } catch (error) {
    console.error("Failed to approve rolling release stage:", error);
  }
}

approveNextStage();
```

## Force completion of a rolling release

In this example, you force-complete an active rolling release, immediately promoting the canary deployment to serve 100% of traffic. This is useful for emergency situations or when you want to skip remaining stages.

```ts run.ts theme={"system"}
import { Vercel } from "@vercel/sdk";

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function forceCompleteRollingRelease() {
  const projectId = "your-project-id";

  try {
    // First, get the current rolling release status
    const currentStatus = await vercel.rollingRelease.getActiveRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
    });

    if (!currentStatus.rollingRelease || currentStatus.rollingRelease.state !== "ACTIVE") {
      console.log("No active rolling release found for this project");
      return;
    }

    const { rollingRelease } = currentStatus;

    console.log(`Current rolling release state: ${rollingRelease.state}`);
    console.log(`Current stage: ${rollingRelease.activeStage?.index} (${rollingRelease.activeStage?.targetPercentage}% traffic)`);
    console.log(`Canary deployment: ${rollingRelease.canaryDeployment?.name} (${rollingRelease.canaryDeployment?.id})`);

    if (!rollingRelease.canaryDeployment?.id) {
      console.error("No canary deployment found to complete");
      return;
    }

    // Confirm the action (in a real scenario, you might want additional checks)
    console.log("⚠️  WARNING: This will immediately promote the canary deployment to 100% traffic");
    console.log(`   Skipping ${rollingRelease.stages?.length - (rollingRelease.activeStage?.index || 0) - 1} remaining stages`);

    // Force complete the rolling release
    const completionResult = await vercel.rollingRelease.completeRollingRelease({
      idOrName: projectId,
      teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l", // Optional
      requestBody: {
        canaryDeploymentId: rollingRelease.canaryDeployment.id,
      },
    });

    console.log("✓ Rolling release completed successfully!");
    console.log(`Final state: ${completionResult.rollingRelease?.state}`);

    // The canary deployment is now the current deployment serving 100% traffic
    if (completionResult.rollingRelease?.currentDeployment) {
      console.log(`New production deployment: ${completionResult.rollingRelease.currentDeployment.name}`);
      console.log(`Production URL: ${completionResult.rollingRelease.currentDeployment.url}`);
    }

    // Log completion time
    if (completionResult.rollingRelease?.updatedAt) {
      const completedAt = new Date(completionResult.rollingRelease.updatedAt);
      console.log(`Completed at: ${completedAt.toISOString()}`);
    }

  } catch (error) {
    console.error("Failed to complete rolling release:", error);

    // Handle specific error cases
    if (error.response?.status === 404) {
      console.error("Project not found or no rolling release configuration exists");
    } else if (error.response?.status === 400) {
      console.error("Invalid request - check the canary deployment ID");
    } else if (error.response?.status === 403) {
      console.error("Insufficient permissions to complete rolling release");
    }
  }
}

forceCompleteRollingRelease();
```


# Team and User Management
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/examples/team-management

Learn how to use the Vercel SDK through real-life examples.

## Invite a user to a team

In this example, you will find your team id and invite a new member to that team with a specific role.

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: process.env.VERCEL_TOKEN,
});

async function inviteTeamMember() {
  try {
    // Invite a new team member
    const availableTeams = (await vercel.teams.getTeams({})).teams;
    const myTeam = availableTeams.filter(
      (team) => team.slug === 'my-team-slug',
    );
    if (myTeam.length > 0) {
      const teamid = myTeam[0].id;
      const inviteResponse = await vercel.teams.inviteUserToTeam({
        teamId: teamid,
        requestBody: {
          email: 'john@example.com',
          role: 'MEMBER',
        },
      });
      console.log(
        `User with role ${inviteResponse.role} invited: ${inviteResponse.username}`,
      );
    }
  } catch (error) {
    console.error(
      error instanceof Error ? `Error: ${error.message}` : String(error),
    );
  }
}

inviteTeamMember();
```


# Using the Vercel SDK
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/sdk

Interact programmatically with your Vercel account using the SDK.

The `@vercel/sdk` is a type-safe Typescript SDK that allows you to access the resources and methods of the Vercel REST API.

<Note>To view the methods for all endpoints, and explore code examples, see the [reference endpoints documentation](/endpoints).</Note>

## Installing Vercel SDK

To download and install Vercel SDK, run the following command:

<CodeGroup>
  ```bash pnpm theme={"system"}
  pnpm i @vercel/sdk
  ```

  ```bash npm theme={"system"}
  npm i @vercel/sdk
  ```

  ```bash yarn theme={"system"}
  yarn add @vercel/sdk
  ```
</CodeGroup>

### Authentication

Vercel Access Tokens are required to authenticate and use the Vercel SDK.

Once you have [created a token](/welcome#creating-an-access-token), you can use it to initialize the SDK as follows:

```ts run.ts theme={"system"}
import { Vercel } from '@vercel/sdk';

const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
```

### Troubleshooting

Make sure that you create a token with the correct Vercel [scope](https://vercel.com/docs/dashboard-features#scope-selector).
If you face permission (403) errors when you are already sending a token, it can be one of the following problems:

* The token you are using has expired. Check the expiry date of the token in the Vercel dashboard.
* The token does not have access to the correct scope, either not the right team or it does not have account level access.
* The resource or operation you are trying to use is not available for that team. For example, AccessGroups is an Enterprise only feature and you are using a token for a team on the pro plan.

### Examples

Learn how to use Vercel SDK through the following categories of examples:

* [Deployments Automation](/examples/deployments-automation)
* [Project Management](/examples/project-management)
* [Domain Management](/examples/domain-management)
* [Team Management](/examples/team-management)
* [Environment Variables](/examples/environment-variables)
* [Logs and Monitoring](/examples/logs-monitoring)
* [Integrations](/examples/integrations)


# Using the REST API
Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/welcome

Interact programmatically with your Vercel account using the SDK or direct HTTP requests.

<Note>To view all endpoints, and explore code examples with the SDK and direct API calls, see the [reference endpoints documentation](/endpoints).</Note>

You can deploy new versions of web applications, manage custom domains, retrieve information about deployments, and manage secrets and environment variables for projects.

The API supports any programming language or framework that can send HTTP requests.

To interact with the API, you can:

* [Use the Vercel SDK](/sdk) by first instantiating with your token
* Use the language of your choice by calling the endpoints directly and [providing your token](#authentication)

## API Basics

Our API is exposed as an HTTP/1 and HTTP/2 service over SSL. All endpoints live under the URL `https://api.vercel.com` and then generally follow the REST architecture.

### Server Specs

#### HTTP and TLS

The API supports HTTP versions 1, 1.1, and 2, although HTTP/2 is preferred.

TLS versions 1.2 and 1.3 are supported, with resumption.

For more information on TLS support, refer to the SSL Labs report.

### Content Type

All requests must be encoded as JSON with the Content-Type: application/json header. If not otherwise specified, responses from the Vercel API, including errors, are encoded exclusively as JSON as well.

### Authentication

Vercel Access Tokens are required to authenticate and use the Vercel API.

```js  theme={"system"}
  Authorization: Bearer <TOKEN>
```

#### Creating an Access Token

Access Tokens can be created and managed from inside your [account settings](https://vercel.com/account/tokens).

<img className="block dark:hidden" src="https://assets.vercel.com/image/upload/v1701697368/docs-assets/static/docs/rest-api/create-token-light.png" />

<img className="hidden  dark:block" src="https://assets.vercel.com/image/upload/v1701697369/docs-assets/static/docs/rest-api/create-token-dark.png" />

1. In the upper-right corner of your [dashboard](https://vercel.com/dashboard), click your profile picture, then select **Settings**
2. Select **Tokens** from the sidebar
3. Enter a descriptive name for the token
4. Choose the scope from the list of Teams in the drop-down menu. The scope ensures that only your specified Team(s) can use an Access Token
5. From the drop-down, select an expiration date for the Token
6. Click **Create Token**
7. Once you've created an Access Token, securely store the value as it will not be shown again.

#### Expiration

Setting an expiration date on an Access Token is highly recommended and is considered one of the standard security practices that helps keep your information secure. You can select from a default list of expiration dates ranging from 1 day to 1 year. You can view the expiration date of your Access Tokens on the [tokens page.](https://vercel.com/account/tokens)

#### Accessing Resources Owned by a Team

By default, you can access resources contained within your own user account (personal).

To access resources owned by a team, or create a project for a *specific* team, you must first find the [Team ID](https://vercel.com/docs/teams-and-accounts/create-or-join-a-team#find-your-team-id).

After you obtained the Team ID, append it as a query string at the end of the API endpoint URL:

```js  theme={"system"}
https://api.vercel.com/v6/deployments?teamId=[teamID]
```

#### Failed Authentication

If authentication is unsuccessful for a request, the [error status code](#errors) **403** is returned.

## Types

The following is a list of the types of data used within the Vercel API:

| Name        | Definition                                                             | Example                      |
| ----------- | ---------------------------------------------------------------------- | ---------------------------- |
| **ID**      | A unique value used to identify resources.                             | `"V0fra8eEgQwEpFhYG2vTzC3K"` |
| **String**  | A string is a sequence of characters used to represent text.           | `"value"`                    |
| **Integer** | An integer is a number without decimals.                               | `1234`                       |
| **Float**   | A float is a number with decimals.                                     | `12.34`                      |
| **Map**     | A data structure with a list of values assigned to a unique key.       | `{ "key": "value" }`         |
| **List**    | A data structure with only a list of values separated by a comma.      | `["value", 1234, 12.34]`     |
| **Enum**    | An Enum is a String with only a few possible valid values.             | `A` or `B`                   |
| **Date**    | An Integer representing a date in milliseconds since the UNIX epoch.   | `1540095775941`              |
| **IsoDate** | A String representing a date in the 8601 format.                       | `YYYY-MM-DDTHH:mm:ssZ`       |
| **Boolean** | A Boolean is a type of two possible values representing true or false. | `true`                       |

## Pagination

When the API response includes an array of records, a pagination object is returned when the total number of records present is greater than the limit per request. The default value of this limit is 20 but it can be changed by passing a value to the query parameter `limit` when the request is made. The maximum possible value of `limit` is 100.

You can then use the pagination object to make additional requests and obtain all the records.

The pagination object is structured as shown in the example below:

```json pagination-structure theme={"system"}
{
  "pagination": {
    "count": 20, //Amount of items in the current page.
    "next": 1555072968396, //Timestamp that must be used to request the next page.
    "prev": 1555413045188 //Timestamp that must be used to request the previous page.
  }
}
```

In order to obtain the records for the next batch, perform the following actions:

1. Send a request to the same API endpoint
2. Include the query parameter `until` with a value equal to the timestamp value of `next` returned in the previous request
3. Repeat this sequence until the pagination object has a `next` value of `null`

This is an example of applying this sequence with `Node.js` to save all the projects in your personal account to a `json` file:

```js pagination-example.js theme={"system"}
const axios = require('axios');
const fs = require('fs');
const vercelToken = 'yourtokenvalue'; //Replace with your token
const apiEndPt = 'https://api.vercel.com/v9/projects';

let config = {
  method: 'get',
  url: apiEndPt,
  headers: {
    Authorization: 'Bearer ' + vercelToken,
  },
};
let results = [];

(function loop() {
  axios(config)
    .then(function (response) {
      results.push(...response.data.projects);
      if (response.data.pagination.next !== null) {
        config.url = `${apiEndPt}?until=${response.data.pagination.next}`;
        loop();
      } else {
        //you can use the final results object and for example save it to a json file
        fs.writeFileSync('projects.json', JSON.stringify(results));
      }
    })
    .catch(function (error) {
      console.log(error);
    });
})();
```

## Rate Limits

We limit the number of calls you can make over a certain period of time.
Rate limits vary and are specified by the following header in all responses:

| Header                  | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| `X-RateLimit-Limit`     | The maximum number of requests that the consumer is permitted to make.       |
| `X-RateLimit-Remaining` | The number of requests remaining in the current rate limit window.           |
| `X-RateLimit-Reset`     | The time at which the current rate limit window resets in UTC epoch seconds. |

When the rate limit is **exceeded**, an error is returned with the status "**429 Too Many Requests**":

```json error-response theme={"system"}
{
  "error": {
    "code": "too_many_requests",
    "message": "Rate limit exceeded"
  }
}
```

<Note>
  You can find the complete list of rate limits in the [limits
  documentation](https://vercel.com/docs/limits#rate-limits).
</Note>

## Versioning

All endpoints and examples are designated with a specific version. Versions vary per endpoint and are not global.

The response shape of a certain endpoint is not guaranteed to be fixed over time. In particular, we might add new keys to responses without bumping a version endpoint, which will be noted in the changelog.

To ensure the security and correctness of your application, make sure to only read the keys from the response that your application needs. Don't proxy entire responses to third-parties without validation.

Old versions of each endpoint are supported for as long as possible. When we intend to deprecate, we will notify users in the changelog section.

Endpoint versions follow the base URL and come before the endpoint. For example:

```js version-endpoint theme={"system"}
https://api.vercel.com/v6/deployments`
```

This examples uses version `6` of the [deployments
endpoint](/endpoints/deployments/get-deployment-events).


