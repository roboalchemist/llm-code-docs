# Audit | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit

[API Reference][Accounts][Logs]
# Audit

##### [Get account audit logs (Version 2)]
GET/accounts/{account_id}/logs/audit
##### ModelsExpand Collapse
AuditListResponse  { id, account, action, 4 more } id: optional string
A unique identifier for the audit log entry.
maxLength32[]account: optional  { id, name }
Contains account related information.
id: optional string
A unique identifier for the account.
[]name: optional string
A string that identifies the account name.
[][]action: optional  { description, result, time, type }
Provides information about the action performed.
description: optional string
A short description of the action performed.
[]result: optional string
The result of the action, indicating success or failure.
[]time: optional string
A timestamp indicating when the action was logged.
formatdate-time[]type: optional string
A short string that describes the action that was performed.
[][]actor: optional  { id, context, email, 4 more }
Provides details about the actor who performed the action.
id: optional string
The ID of the actor who performed the action. If a user performed the action, this will be their User ID.
[]context: optional "api_key" or "api_token" or "dash" or 2 moreOne of the following:"api_key"[]"api_token"[]"dash"[]"oauth"[]"origin_ca_key"[][]email: optional string
The email of the actor who performed the action.
formatemail[]ip_address: optional string
The IP address of the request that performed the action.
[]token_id: optional string
The API token ID when the actor context is an api_token or oauth.
[]token_name: optional string
The API token name when the actor context is an api_token or oauth.
[]type: optional "account" or "cloudflare_admin" or "system" or "user"
The type of actor.
One of the following:"account"[]"cloudflare_admin"[]"system"[]"user"[][][]raw: optional  { cf_ray_id, method, status_code, 2 more }
Provides raw information about the request and response.
cf_ray_id: optional string
The Cloudflare Ray ID for the request.
[]method: optional string
The HTTP method of the request.
[]status_code: optional number
The HTTP response status code returned by the API.
[]uri: optional string
The URI of the request.
[]user_agent: optional string
The client’s user agent string sent with the request.
[][]resource: optional  { id, product, request, 3 more }
Provides details about the affected resource.
id: optional string
The unique identifier for the affected resource.
[]product: optional string
The Cloudflare product associated with the resource.
[]request: optional unknown[]response: optional unknown[]scope: optional unknown
The scope of the resource.
[]type: optional string
The type of the resource.
[][]zone: optional  { id, name }
Provides details about the zone affected by the action.
id: optional string
A string that identifies the zone id.
[]name: optional string
A string that identifies the zone name.
[][][]