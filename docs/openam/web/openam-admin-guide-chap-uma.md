# Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-uma

Title: Managing UMA Authorization :: Open Identity Platform Documentation

URL Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-uma

Markdown Content:
[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#sec-uma-intro)OpenAM and the UMA Workflow
-------------------------------------------------------------------------------------------------------------

UMA defines a workflow for allowing resource owners to manage access to their protected resources by creating authorization policies on a centralized authorization server, such as OpenAM.

![Image 1: uma workflow overview](https://doc.openidentityplatform.org/openam/_images/uma-workflow-overview.png)

The actions that form the UMA workflow are as follows:

Manage
The resource owner manages their resources on the resource server.

Protect
The resource owner links their resource server and chosen authorization server, for example an OpenAM instance.

The authorization server provides a protection API so that the resource server can register sets of resources. Use of the protection API requires a protection API token (PAT) - an OAuth 2.0 token with a specific scope.

For more information, see ["Managing UMA Resource Sets"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets).

Control
The resource owner controls who has access to their registered resources by creating policies on the authorization server.

For more information, see ["Managing UMA Policies"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#sec-uma-policies).

Authorize
The client, acting on behalf of the requesting party, uses the authorization server’s authorization API to acquire a requesting party token (RPT). The requesting party or client may need further interaction with the authorization server at this point, for example to supply identity claims. Use of the authorization API requires an authorization API token (AAT) - an OAuth 2.0 token with a specific scope.

For more information, see ["Accessing UMA-Protected Resources"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#accessing-uma-protected-resources).

Access
The client presents the RPT to the resource server, which verifies its validity with the authorization server and, if both valid and containing sufficient permissions, returns the protected resource to the requesting party.

For more information, see ["Accessing UMA-Protected Resources"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#accessing-uma-protected-resources).

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#sec-uma-users)Using OpenAM for UMA
------------------------------------------------------------------------------------------------------

This section explains how to use the UMA features the OpenAM provides for end users.

The functionality covered is described in the following procedures:

*   ["To Share UMA Resources"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-share-uma-resources)

*   ["To Apply User Labels to a Resource"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-apply-user-labels-to-resource-sets)

*   ["To Mark a Resource as a Favorite"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-apply-star-label-to-resource-set)

To Apply User Labels to a Resource

To apply labels to a resource:

1.   Log in to OpenAM as a user. The profile page is displayed.

2.   Navigate to Shares > Resources > My Resources, and then click the name of the resource to add labels to.

3.   On the resource details page, click Edit Labels.

In the edit box that appears, you can:

    *   Enter the label you want to add to the resource, and then press **Enter**.

If you enter a label containing forward slash (**/**) characters, a hierarchy of each component of the label is created. The resource only appears in the last component of the hierarchy.

For example, the screenshot below shows the result of the label: `2015/October/Bristol`:

![Image 2: uma resource label hierarchy](https://doc.openidentityplatform.org/openam/_images/uma-resource-label-hierarchy.png) 
    *   Click an existing label, and then press **Delete** or **Backspace** to delete the label from the resource.

4.   When you have finished editing labels you can:

    *   Click the checkmark button to save any changes made.

    *   Click the X button to cancel any changes made.

To Mark a Resource as a Favorite

Mark resources as favorites to have them appear on the Starred page.

1.   Log in to OpenAM as a user. The profile page is displayed.

2.   Navigate to Shares > Resources > My Resources, and then click the name of the resource to add to the list of favorites.

3.   On the resource details page, click the star icon, as shown below:

![Image 3: uma resource label star](https://doc.openidentityplatform.org/openam/_images/uma-resource-label-star.png) 
To view the list of favorite resources, click Starred.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#configure-uma)Configuring OpenAM for UMA
------------------------------------------------------------------------------------------------------------

This section explains how to setup OpenAM as an authorization server in the User-Managed Access (UMA) workflow.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#configure-uma-provider)Configuring the UMA Provider Service

To enable OpenAM to act as an authorization server in the UMA workflow, you must create an UMA Provider service.

To Configure the UMA Provider Service

1.   In the OpenAM console, select Realms >_Realm Name_> Dashboard > Configure OAuth Provider > Configure User Managed Access.

2.   On the Configure UMA page, select the Realm for the provider service.

3.   (Optional) If necessary, adjust the lifetimes for authorization codes, access tokens, and refresh tokens.

4.   (Optional) Select Issue Refresh Tokens unless you do not want the authorization service to supply a refresh token when returning an access token.

5.   (Optional) Select Issue Refresh Tokens on Refreshing Access Tokens if you want the authorization service to supply a new refresh token when refreshing an access token.

6.   (Optional) If you have a custom scope validator implementation, put it on the OpenAM classpath, for example `/path/to/tomcat/webapps/openam/WEB-INF/lib/`, and specify the class name in the Scope Implementation Class field. For an example, see ["Customizing OAuth 2.0 Scope Handling"](https://doc.openidentityplatform.org/openam/dev-guide/chap-customizing#sec-oauth2-scopes) in the _Developer’s Guide_.

7.   Click Create to save your changes. OpenAM creates the following:

    *   An UMA provider service.

    *   An OAuth2 provider service that supports OpenID Connect.

    *   A policy to protect the OAuth2 authorization endpoints.

If an UMA provider service already exists, it will be overwritten with the new UMA parameter values.

8.   To access the provider service configuration in the OpenAM console, browse to Realms >_Realm Name_> Services, and then click UMA Provider.

For information about the available attributes, see ["UMA Provider"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#uma-provider-configuration) in the _Reference_.

To complete the configuration, click Save Changes.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#configure-uma-storage)Configuring UMA Stores

OpenAM stores information about registered resource sets, and also audit information generated when users manage access to their protected resources. OpenAM provides a default store, or you can configure external stores to maintain this information.

To Configure the UMA Resource Sets Store

Resource Sets Store properties are inherited from the defaults. For more information about inherited properties, see ["Configuring Servers"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-configuration) in the _Reference_

1.   Log in to the OpenAM console as an OpenAM administrator, for example `amadmin`.

2.   Navigate to Deployment > Servers >_Server Name_> UMA > Resource Sets Store.

    *   Unlock the Store Mode property and choose External Token Store.

    *   Unlock the Root Suffix property and enter the base DN of the store. For example `dc=uma-rs,dc=example,dc=com`.

    *   Save your work.

3.   Navigate to Deployment > Servers >_Server Name_> UMA > External Resource Sets Store Configuration.

    *   Enter the properties for the store. For information about the available settings, see ["UMA"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-uma) in the _Reference_.

    *   Save your work.

To Configure UMA Audit Storage

UMA Audit Store properties are inherited from the defaults. For more information about inherited properties, see ["Configuring Servers"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-configuration) in the _Reference_

1.   Log in to the OpenAM console as an OpenAM administrator, for example `amadmin`.

2.   Navigate to Deployment > Servers >_Server Name_> UMA > UMA Audit Store.

    *   Unlock the Store Mode property and choose External Token Store.

    *   Unlock the Root Suffix property and enter the base DN of the store. For example `dc=uma-rs,dc=example,dc=com`.

    *   Save your work.

3.   Navigate to Deployment > Servers >_Server Name_> UMA > External UMA Audit Store Configuration.

    *   Enter the properties for the store. For information about the available settings, see ["UMA"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-uma) in the _Reference_.

    *   Save your work.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#configure-uma-discovery)Configuring OpenAM For UMA Discovery

OpenAM exposes an endpoint for discovering information about UMA Provider configuration.

To use the endpoint, you must first create both an OAuth 2.0 Provider service, and an UMA Provider service in OpenAM. For more information on creating these services, see ["Configuring the OAuth 2.0 Authorization Service"](https://doc.openidentityplatform.org/openam/admin-guide/chap-oauth2#configure-oauth2-authz) and ["Configuring the UMA Provider Service"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#configure-uma-provider).

A resource server or client can perform an HTTP GET on `/uma/{realm}/.well-known/uma-configuration` to retrieve a JSON object indicating the UMA Provider configuration for _realm_ if specified, or the Top Level Realm if not.

Resource servers and clients need to be able to discover the UMA provider for a resource owner. You should consider redirecting requests to URIs at the server root, such as `http://www.example.com/.well-known/uma-configuration`, to the well-known URIs in OpenAM’s space: `http://www.example.com/openam/uma/.well-known/uma-configuration`.

OpenAM supports a provider service that allows a realm to have a configured option for obtaining the base URL (including protocol) for components that need to return a URL to the client. This service is used to provide the URL base that is used in the `.well-known` endpoints used in OpenID Connect 1.0 and UMA.

The following is an example of a GET request to the UMA configuration discovery endpoint for the Top Level Realm:

```
$ curl \
 --request GET \
 https://openam.example.com:8443/openam/uma/.well-known/uma-configuration
{
 "version": "1.0",
 "issuer": "openam.example.com",
 "pat_profiles_supported": [
  "bearer"
 ],
 "aat_profiles_supported": [
     "bearer"
 ],
 "rpt_profiles_supported": [
     "bearer"
 ],
 "pat_grant_types_supported": [
     "authorization_code"
 ],
 "aat_grant_types_supported": [
     "authorization_code"
 ],
 "token_endpoint": "https://openam.example.com:8443/openam/oauth2/access_token",
 "authorization_endpoint": "https://openam.example.com:8443/openam/oauth2/authorize",
 "introspection_endpoint": "https://openam.example.com:8443/openam/oauth2/introspect",
 "resource_set_registration_endpoint": "https://openam.example.com:8443/openam/oauth2/resource_set",
 "permission_registration_endpoint": "https://openam.example.com:8443/openam/uma/permission_request",
 "rpt_endpoint": "https://openam.example.com:8443/openam/uma/authz_request",
 "dynamic_client_endpoint": "https://openam.example.com:8443/openam/oauth2/connect/register"
}
```

The JSON object returned includes the following configuration information:

`version`
The supported UMA core protocol version.

`issuer`
The URI of the issuing authorization server.

`pat_profiles_supported`
The supported OAuth token types used for issuing Protection API Tokens (PATs).

`aat_profiles_supported`
The supported OAuth token types used for issuing Authorization API Tokens (AATs).

`rpt_profiles_supported`
The supported Requesting Party Token (RPT) profiles.

`pat_grant_types_supported`
The supported OAuth grant types used for issuing PATs.

`aat_grant_types_supported`
The supported OAuth grant types used for issuing AATs.

`token_endpoint`
The URI to request a PAT or AAT.

`authorization_endpoint`
The URI to request authorization for issuing a PAT or AAT.

`introspection_endpoint`
The URI to introspect an RPT.

`resource_set_registration_endpoint`
The URI for a resource server to register a resource set.

For more information, see ["Managing UMA Resource Sets"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets).

`permission_registration_endpoint`
The URI for a resource server to register a requested permission.

For more information, see ["To Register an UMA Permission Request"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-register-an-uma-permission-request).

`rpt_endpoint`
The URI for the client to request authorization data.

For more information, see ["To Acquire a Requesting Party Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-rpt).

`dynamic_client_endpoint`
The URI for registering a dynamic client.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets)Managing UMA Resource Sets
-------------------------------------------------------------------------------------------------------------------------

UMA resource servers register resource sets with the resource owner’s chosen authorization server. Registered resources can then be protected, and are available for user-created policies.

OpenAM supports optional _system_ labels when registering resource sets to help resource owners organize their resources. For information on labelling resources, see ["Managing UMA Labels"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-set-labels).

OpenAM provides two REST endpoints for managing resource sets, as described in the sections below:

*   ["UMA Resource Set Endpoint for Resource Servers"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets-with-REST-resource-servers)

*   ["UMA Resource Set Endpoint for Users"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets-with-REST-users)

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets-with-REST-resource-servers)UMA Resource Set Endpoint for Resource Servers

OpenAM provides the `/oauth2/resource_set` REST endpoint, as described in the [OAuth 2.0 Resource Set Registration](https://docs.kantarainitiative.org/uma/draft-oauth-resource-reg.html) specification, to allow UMA resource servers to register and manage resource sets.

The endpoint requires a _Protection API Token_ (PAT), which is an OAuth 2.0 access token with a scope of `uma_protection`. A resource server must acquire a PAT in order to use the resource set endpoint. For more information, see ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

After acquiring a PAT, use the `/oauth2/resource_set` REST endpoint for the following operations:

*   ["To Register an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-register-an-uma-resource-set)

*   ["To List Registered UMA Resource Sets"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-list-uma-resource-sets)

*   ["To Read an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-read-an-uma-resource-set)

*   ["To Update an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-update-an-uma-resource-set)

*   ["To Delete an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-delete-an-uma-resource-set)

To Acquire a Protection API Token

You must have first ["Registering OAuth 2.0 Clients With the Authorization Service"](https://doc.openidentityplatform.org/openam/admin-guide/chap-oauth2#register-oauth2-client) with a name, such as _UMA-Resource-Server_ and a client password, such as _password_. Ensure that `uma_protection` is in the list of available scopes in the client, and a redirection URI is configured:

1.   Direct the resource owner to the authorization server to obtain a PAT token. The URL should specify the client name registered above, the redirect URI, and request the `uma_protection` scope, as shown in the example below:

`https://openam.example.com:8443/openam/oauth2/authorize?client_id=UMA-Resource-Server&redirect_uri=http://openam.example.com:8080&response_type=code&scope=uma_protection`

This example uses the OAuth 2.0 code grant, however the UMA resource server can use any of the OAuth 2.0 grants to obtain the access token.

2.   After logging in, the consent screen asks the resource owner to allow or deny the requested scopes.

![Image 4: uma resource server auth request](https://doc.openidentityplatform.org/openam/_images/uma-resource-server-auth-request.png)

1.   If the resource owner allows access, they are sent to the configured redirection URL, which will have a `code` query string parameter added, which is used to request the PAT.

2.   Create a POST request to the `/oauth2/access_token` endpoint, with the client credentials registered earlier, a grant type of `authorization_code`, a redirect URL, and the value of the `code` query string parameter returned in the previous step, as shown below:

```
$ curl \
 --request POST \
 --data 'client_id=UMA-Resource-Server' \
 --data 'client_secret=password' \
 --data 'grant_type=authorization_code' \
 --data 'code=c1bb2b94-038b-4ab2-beb1-a1ee14790c6b' \
 --data 'redirect_uri=http%3A%2F%2Fopenam.example.com%3A8080' \
 http://openam.example.com:8080/openam/oauth2/access_token

{
 "scope": "uma_protection read",
 "expires_in": 599,
 "token_type": "Bearer",
 "refresh_token": "f9873041-885a-4522-836c-9fa71aaad3e4",
 "access_token": "983e1d96-20a7-437c-8432-cfde52076714"
}
``` 
The value returned in `access_token` is the PAT bearer token, used in the following procedures.

To Register an UMA Resource Set

To register a resource set, the resource server must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT bearer token, you can access the `/oauth2/resource_set` endpoint to register resources, as shown in the following steps.

*   Create a POST request to the resource_set endpoint, including the PAT bearer token in an Authorization header.

The following example uses a PAT bearer token to register a photo album resource set and a pair of system labels:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 --data \
 '{
     "name" : "Photo Album",
     "icon_uri" : "http://www.example.com/icons/flower.png",
     "scopes" : [
         "http://photoz.example.com/dev/scopes/view",
         "http://photoz.example.com/dev/scopes/all"
     ],
     "labels" : [
         "3D",
         "VIP"
     ],
     "type" : "http://www.example.com/rsets/photoalbum"
 }' \
 https://openam.example.com:8443/openam/oauth2/resource_set/
{
    "_id": "43225628-4c5b-4206-b7cc-5164da81decd0",
    "user_access_policy_uri":
 "https://openam.example.com:8443/openam/XUI/#uma/share/43225628-4c5b-4206-b7cc-5164da81decd0/"
}
``` 
The resource owner can then visit the user access policy URI in order to manage access to the resource set.

To List Registered UMA Resource Sets

To list registered resource sets, you must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT token, you can access the `/oauth2/resource_set` endpoint to list resource sets, as shown below:

*   Create a GET request to the resource_set endpoint, including the PAT bearer token in an Authorization header.

The following example uses a PAT bearer token to list the registered resource sets:

```
$ curl \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 https://openam.example.com:8443/openam/oauth2/resource_set
[
    "43225628-4c5b-4206-b7cc-5164da81decd0",
    "3a2fe6d5-67c8-4a5a-83fb-09734f1dd5b10",
    "8ed24623-fcb5-46b8-9a64-18ee1b9b7d5d0"
 ]
``` 
On success, an array of the registered resource set IDs is returned. Use the ID to identify a resource set in the following procedures:

    *   ["To Read an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-read-an-uma-resource-set)

    *   ["To Update an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-update-an-uma-resource-set)

    *   ["To Delete an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-delete-an-uma-resource-set)

To Read an UMA Resource Set

To read a resource set, you must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT token, you can access the `/oauth2/resource_set` endpoint to read resources, as shown below:

*   Create a GET request to the resource_set endpoint, including the PAT bearer token in an Authorization header.

You must provide the ID of the resource set to read, specified at the end of the request, as follows: `https://openam.example.com:8443/openam/oauth2/resource_set/resource_set_ID`. 
The following example uses a PAT bearer token and a resource set ID to read a specific resource set:

```
$ curl \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 https://openam.example.com:8443/openam/oauth2/resource_set/43225628-4c5b-4206-b7cc-5164da81decd0
{
  "scopes": [
    "http://photoz.example.com/dev/scopes/view",
    "http://photoz.example.com/dev/scopes/all"
  ],
  "_id": "43225628-4c5b-4206-b7cc-5164da81decd0",
  "name": "Photo Album",
  "icon_uri": "http://www.example.com/icons/flower.png",
  "type": "http://www.example.com/rsets/photoalbum",
  "user_access_policy_uri":
    "https://openam.example.com:8443/openam/XUI/#uma/share/43225628-4c5b-4206-b7cc-5164da81decd0"
}
``` 
On success, an HTTP 200 OK status code is returned, as well as a header containing the current ETag value, for example: `W/"123401234"`. Use this ETag value when updating a resource set. See ["To Update an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-update-an-uma-resource-set).

Add the `-i` option to curl commands to show the returned headers. For example:

```
$ curl -i \
 --header "Authorization: Bearer 515d6551-4512-4279-98b6-c0ef3f03a722" \
https://openam.example.com:8443/openam/oauth2\
/resource_set/43225628-4c5b-4206-b7cc-5164da81decd0
HTTP/1.1 200 OK
 ETag: W/"123401234"
 Date: Tue, 10 Feb 2015 11:57:35 GMT
 Accept-Ranges: bytes
 Server: Restlet-Framework/2.1.7
 Vary: Accept-Charset, Accept-Encoding, Accept-Language, Accept
 Content-Type: application/json;charset=UTF-8
 Transfer-Encoding: chunked

 {
     "scopes": [
         "http://photoz.example.com/dev/scopes/view",
         "http://photoz.example.com/dev/scopes/all"
     ],
     "_id": "myPhotoAlbum001",
     "name": "Photo Album",
     "icon_uri": "http://www.example.com/icons/flower.png",
     "type": "http://www.example.com/rsets/photoalbum",
     "user_access_policy_uri":
         "https://openam.example.com:8443/openam/XUI/#uma
              /share/43225628-4c5b-4206-b7cc-5164da81decd0"
 }
``` 
If the resource set ID does not exist, an HTTP 404 Not Found status code is returned, as follows:

```
{
    "error": "not_found",
    "error_description":
        "Resource set corresponding to id: 43225628-4c5b-4206-b7cc-5164da81decd0 not found"
}
``` 

To Update an UMA Resource Set

To update a resource set, you must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT token, you can access the `/oauth2/resource_set` endpoint to update resources, as shown below:

*   Create a PUT request to the resource_set endpoint, including the PAT bearer token in a header named `Authorization`, and any new or changed parameters.

The only difference between creating a resource set and updating one is the presence of an `If-Match` header when updating. This should contain the value of the ETag header returned when creating, updating, or reading a resource set.

You must provide the ID of the resource set to update, specified at the end of the request, as follows: `https://openam.example.com:8443/openam/oauth2/resource_set/resource_set_ID`. 
The following example uses a PAT bearer token, a resource set ID and an If-Match header to update a specific resource set:

```
$ curl \
 --request PUT \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 --header "If-Match: "123401234"" \
 --data \
 '{
     "name" : "Photo Album 2.0",
     "icon_uri" : "http://www.example.com/icons/camera.png",
     "scopes" : [
         "http://photoz.example.com/dev/scopes/view",
         "http://photoz.example.com/dev/scopes/edit",
         "http://photoz.example.com/dev/scopes/all"
     ],
     "type" : "http://www.example.com/rsets/photoalbum"
 }' \
 https://openam.example.com:8443/openam/oauth2/resource_set/43225628-4c5b-4206-b7cc-5164da81decd0
 {
  "_id": "43225628-4c5b-4206-b7cc-5164da81decd0",
  "user_access_policy_uri":
  "https://openam.example.com:8443/openam/XUI/#uma/share/43225628-4c5b-4206-b7cc-5164da81decd0"
  }
``` 
On success, an HTTP 200 OK status code is returned, with the resource set ID, and a user access policy URI that the resource owner can visit in order to manage access to the resource set.

If the resource set ID is not found, an HTTP 404 Not Found status code is returned, as follows:

```
{
    "error": "not_found",
    "error_description":
        "ResourceSet corresponding to id: 43225628-4c5b-4206-b7cc-5164da81decd0 not found"
}
``` 
If the `If-Match` header is missing, or does not match the current version of the resource set, an HTTP 412 Precondition Failed status code is returned, as follows:

```
{
 "error": "precondition_failed"
}
``` 

To Delete an UMA Resource Set

To delete a resource set, you must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT token, you can access the `/oauth2/resource_set` endpoint to delete resources, as shown below:

*   Create a DELETE request to the resource_set endpoint, including the PAT bearer token in a header named `Authorization`.

Add an `If-Match` header containing the value of the ETag header returned when creating, updating, or reading a resource set.

You must provide the ID of the resource set to read, specified at the end of the request, as follows: `https://openam.example.com:8443/openam/oauth2/resource_set/resource_set_ID`. 
The following example uses a PAT bearer token, a resource set ID and an If-Match header to delete a specific resource set:

```
$ curl \
 --request DELETE \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 --header "If-Match: "123401234"" \
 https://openam.example.com:8443/openam/oauth2/resource_set/43225628-4c5b-4206-b7cc-5164da81decd0
 {}
``` 
On success, an HTTP 204 No Content status code is returned, as well as an empty response body.

If the resource set ID does not exist, an HTTP 404 Not Found status code is returned, as follows:

```
{
  "error": "not_found",
  "error_description":
  "Resource set corresponding to id: 43225628-4c5b-4206-b7cc-5164da81decd0 not found"
 }
``` 
If the `If-Match` header is missing, or does not match the current version of the resource set, an HTTP 412 Precondition Failed status code is returned, as follows:

```
{
 "error": "precondition_failed"
}
``` 

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets-with-REST-users)UMA Resource Set Endpoint for Users

OpenAM provides the `/json/users/username/oauth2/resources/sets` REST endpoint for managing resource sets belonging to a user.

Specify the `username` in the URL, and provide the SSO token of that user in the `iPlanetDirectoryPro` header, as shown below.

To Manage Resource Sets for a User by using REST

1.   To query resource sets for a user, create a GET request including `_queryFilter=resourceOwnerId eq "username"` in the query string. The query string should be URL-encoded, as shown below:

```
$ curl \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 https://openam.example.com:8443/json/users/demo/oauth2/resources/sets?_queryFilter=resourceOwnerId+eq+%22demo%22
 {
   "result": [
     {
       "scopes": [
         "View Photos",
         "Edit Photos"
       ],
       "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d47",
       "resourceServer": "UMA-Resource-Server",
       "labels": [],
       "name": "My Nature Photos",
       "icon_uri": "http://www.example.com/icons/flower.png",
       "resourceOwnerId": "demo",
       "type": "Photo Album"
     }
   ],
   "resultCount": 1,
   "pagedResultsCookie": null,
   "totalPagedResultsPolicy": "NONE",
   "totalPagedResults": -1,
   "remainingPagedResults": 0
 }
``` 
On success, an HTTP 200 OK status code is returned, as well as a JSON representation of the resource sets assigned to the specified user.

2.   To read a specific resource set for a user, create a GET request including the ID of the resource set in the URL, as shown below:

```
$ curl \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 https://openam.example.com:8443/json/users/demo/oauth2/resources/sets/46a3392f-1d2f-4643-953f-d51ecdf141d47
 {
   "scopes": [
     "View Photos",
     "Edit Photos"
   ],
   "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d47",
   "resourceServer": "UMA-Resource-Server",
   "labels": [],
   "name": "My Nature Photos",
   "icon_uri": "http://www.example.com/icons/flower.png",
   "resourceOwnerId": "demo",
   "type": "Photo Album"
 }
``` 
On success, an HTTP 200 OK status code is returned, as well as a JSON representation of the specified resource set.

3.   To update the user labels assigned to a resource set for a user, create a PUT request including the ID of the resource set in the URL, the full JSON representation of the resource set, and the additional user label IDs in the `labels` array in the body of the JSON data, as shown below:

```
$ curl \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 --data \
 '{
     "scopes": [
         "View Photos",
         "Edit Photos"
     ],
     "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d47",
     "resourceServer": "UMA-Resource-Server",
     "labels": ["257ee30a-b989-4fe6-9e70-a87a050f6a4a4"],
     "name": "My Nature Photos",
     "icon_uri": "http://www.example.com/icons/flower.png",
     "resourceOwnerId": "demo",
     "type": "Photo Album"
 }' \
 https://openam.example.com:8443/json/users/demo/oauth2/resources/sets/46a3392f-1d2f-4643-953f-d51ecdf141d47
 {
       "scopes": [
           "View Photos",
           "Edit Photos"
       ],
       "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d47",
       "resourceServer": "UMA-Resource-Server",
       "labels": [
           "257ee30a-b989-4fe6-9e70-a87a050f6a4a4"
       ],
       "name": "My Nature Photos",
       "icon_uri": "http://www.example.com/icons/flower.png",
       "resourceOwnerId": "demo",
       "type": "Photo Album"
 }
``` 
On success, an HTTP 200 OK status code is returned, as well as a JSON representation of the updated resource set.

Only the `labels` field can be updated by using PUT. All other fields are read-only but must still be included in the JSON body of the request. 

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-set-labels)Managing UMA Labels
------------------------------------------------------------------------------------------------------------------------

Apply labels to resources to help organize and locate them more easily. Resources can have multiple labels applied to them, and labels can apply to multiple resources.

Resources support three types of label:

User Labels

*   Managed by the resource owner after the resource set has been registered to them.

*   Can be created and deleted. Deleting a label does not delete the resources to which it was applied.

*   Support nested hierarchies. Separate levels of the hierarchy with forward slashes (**/**) when creating a label. For example `Top Level/Second Level/My Label`.

*   Are only visible to the user who created them.

You can manage user labels by using the OpenAM console, or by using a REST interface. For more information, see ["UMA Labels Endpoint for Users"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-labels-with-REST-users) and ["To Apply User Labels to a Resource"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-apply-user-labels-to-resource-sets).

System Labels

*   Created by the resource server when registering a resource set.

*   Cannot be deleted.

*   Do not support a hierarchy of levels.

*   Are only visible to the owner of the resource.

Each resource set is automatically assigned a system label containing the name of the resource server that registered it, as well as a system label allowing users to add the resource to a list of favorites.

For information on creating system labels, see ["To Register an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-register-an-uma-resource-set).

Favourite Labels
Each user can assign the builtin _star_ label to a resource to mark it as a favorite.

For more information, see ["To Mark a Resource as a Favorite"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-apply-star-label-to-resource-set).

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-labels-with-REST-users)UMA Labels Endpoint for Users

OpenAM provides the `/json/users/username/oauth2/resources/labels` REST endpoint to allow users to manage user labels.

Specify the `username` in the URL, and provide the SSO token of that user in the `iPlanetDirectoryPro` header.

Use the `/json/users/username/oauth2/resources/labels` REST endpoint for the following operations:

*   ["To Create User Labels by using REST"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-resource-set-labels-for-a-user-with-REST)

*   ["To Query User Labels by using REST"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-query-resource-set-labels-for-a-user-with-REST)

*   ["To Delete User Labels by using REST"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-delete-resource-set-labels-for-a-user-with-REST)

To Create User Labels by using REST

*   To create a new user label, create a POST request with the name of the new user label and the type, `USER`, as shown below:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 --data \
 '{
     "name" : "New Resource Set Label",
     "type" : "USER"
     ]
 }' \
 https://openam.example.com:8443/openam/json/users/demo/oauth2/resources/labels?_action=create
 {
   "_id": "db2161c0-167e-4195-a832-92b2f578c96e3",
   "name": "New Resource Set Label",
   "type": "USER"
 }
``` 
On success, an HTTP 201 Created status code is returned, as well as the unique identifier of the new user label in the `_id` property in the JSON-formatted body. Note that the user label is not yet associated with a resource set. To apply the new label to a resource set, see ["To Manage Resource Sets for a User by using REST"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-manage-resource-sets-for-a-user-with-REST).

To Query User Labels by using REST

*   To query the labels belonging to a user, create a GET request including `_queryFilter=true` in the query string, as shown below:

```
$ curl \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 https://openam.example.com:8443/json/users/demo/oauth2/resources/labels?_queryFilter=true
 {
   "result": [
     {
       "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d44",
       "name": "2015/October/Bristol",
       "type": "USER"
     },
     {
       "_id": "60b785c2-9510-40f5-85e3-9837ac272f1b1",
       "name": "Top Level/Second Level/My Label",
       "type": "USER"
     },
     {
       "_id": "ed5fad66-c873-4b80-93bb-92656eb06deb0",
       "name": "starred",
       "type": "STAR"
     },
     {
       "_id": "db2161c0-167e-4195-a832-92b2f578c96e3",
       "name": "New Resource Set Label",
       "type": "USER"
     }
   ],
   "resultCount": 4,
   "pagedResultsCookie": null,
   "totalPagedResultsPolicy": "NONE",
   "totalPagedResults": -1,
   "remainingPagedResults": -1
 }
``` 

To Delete User Labels by using REST

*   To delete a user label belonging to a user, create a DELETE request including the ID of the user label to delete in the URL, as shown below:

```
$ curl \
 --request DELETE \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 https://openam.example.com:8443/json/users/demo/oauth2/resources/labels/46a3392f-1d2f-4643-953f-d51ecdf141d44
 {
   "_id": "46a3392f-1d2f-4643-953f-d51ecdf141d44",
   "name": "2015/October/Bristol",
   "type": "USER"
 }
``` 
On success, an HTTP 200 OK status code is returned, as well as a JSON representation of the user label that was removed.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#sec-uma-policies)Managing UMA Policies
----------------------------------------------------------------------------------------------------------

UMA authorization servers must manage the resource owner’s authorization policies, so that registered resource sets can be protected.

OpenAM provides the `/json/users/{user}/uma/policies/` REST endpoint for creating and managing user-managed authorization policies.

Managing UMA policies requires that a resource set is registered to the user in the URL. For information on registering resource sets, see ["Managing UMA Resource Sets"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-uma-resource-sets).

Once a resource set is registered to the user, use the `/json/users/{user}/uma/policies/` REST endpoint for the following operations:

*   ["To Create an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-an-uma-policy)

*   ["To Read an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-read-an-uma-policy)

*   ["To Update an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-update-an-uma-policy)

*   ["To Delete an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-delete-an-uma-policy)

*   ["To Query UMA Policies"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-query-uma-policies)

To Create an UMA Policy

To create a policy, the resource owner must be logged in to the authorization server and have an SSO token issued to them, and must also know the ["To Register an UMA Resource Set"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-register-an-uma-resource-set) to be protected. This information is used when creating policies.

Only the resource owner can create a policy to protect a resource set. Administrator users such as `amadmin` cannot create policies on behalf of a resource owner.

*   Create a POST request to the policies endpoint, including the SSO token in a header based on the configured session cookie name (default: `iPlanetDirectoryPro`), and the resource set ID as the value of `policyId` in the body.

The SSO token must have been issued to the user specified in the URL. In this example, the user is `demo`. 
The following example uses an SSO token to create a policy to share a resource set belonging to user _demo_ with two subjects, with different scopes for each:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 --data \
 '{
     "policyId": "43225628-4c5b-4206-b7cc-5164da81decd0",
     "permissions":
     [
         {
             "subject": "user.1",
             "scopes": ["http://photoz.example.com/dev/scopes/view"]
         },
         {
             "subject": "user.2",
             "scopes": [
                 "http://photoz.example.com/dev/scopes/view",
                 "http://photoz.example.com/dev/scopes/all"
             ]
         }
     ]
 }' \
 https://openam.example.com:8443/openam/json/users/demo/uma/policies?_action=create
{}
``` 
On success, an HTTP 201 Created status code is returned, with an empty JSON body as the response.

If the permissions are not correct, an HTTP 400 Bad Request status code is returned, for example:

```
{
     "code": 400,
     "reason": "Bad Request",
     "message": "Invalid UMA policy permission. Missing required attribute, 'subject'."
 }
``` 

To Read an UMA Policy

To read a policy, the resource owner or an administrator user must be logged in to the authorization server and have an SSO token issued to them. The ["To Create an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-an-uma-policy) to read must also be known.

The ID used for a policy is always identical to the ID of the resource set it protects.

*   Create a GET request to the policies endpoint, including the SSO token in a header based on the configured session cookie name (default: `iPlanetDirectoryPro`), and the resource set ID as part of the URL.

The SSO token must have been issued to the user specified in the URL, or to an administrative user such as `amadmin`. In this example, the user is `demo`. 
The following example uses an SSO token to read a specific policy with ID `43225628-4c5b-4206-b7cc-5164da81decd0` belonging to user _demo_:

```
$ curl \
--header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
https://openam.example.com:8443/openam/json/users/demo\
/uma/policies/43225628-4c5b-4206-b7cc-5164da81decd0
{
 "policyId": "43225628-4c5b-4206-b7cc-5164da81decd0",
 "name": "Photo Album",
 "permissions": [
     {
         "subject": "user.1",
         "scopes": [
             "http://photoz.example.com/dev/scopes/view"
         ]
     },
     {
         "subject": "user.2",
         "scopes": [
             "http://photoz.example.com/dev/scopes/view",
             "http://photoz.example.com/dev/scopes/all"
         ]
     }
 ]
}
``` 
On success, an HTTP 200 OK status code is returned, with a JSON body representing the policy.

If the policy ID does not exist, an HTTP 404 Not Found status code is returned, as follows:

```
{
     "code": 404,
     "reason": "Not Found",
     "message": "UMA Policy not found, 43225628-4c5b-4206-b7cc-5164da81decd0"
}
``` 

To Update an UMA Policy

To update a policy, the resource owner or an administrator user must be logged in to the authorization server and have an SSO token issued to them. The ["To Create an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-an-uma-policy) to read must also be known.

The ID used for a policy is always identical to the ID of the resource set it protects.

*   Create a PUT request to the policies endpoint, including the SSO token in a header based on the configured session cookie name (default: `iPlanetDirectoryPro`), and the resource set ID as both the value of `policyId` in the body and also as part of the URL.

The SSO token must have been issued to the user specified in the URL. In this example, the user is `demo`. 
The following example uses an SSO token to update a policy with ID `43225628-4c5b-4206-b7cc-5164da81decd0` belonging to user _demo_ with a new scope for one of the subjects:

```
$ curl \
 --request PUT \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 --data \
 '{
     "policyId": "43225628-4c5b-4206-b7cc-5164da81decd0",
     "permissions":
     [
         {
             "subject": "user.1",
             "scopes": [
                 "http://photoz.example.com/dev/scopes/view",
                 "http://photoz.example.com/dev/scopes/all"
             ]
         },
         {
             "subject": "user.2",
             "scopes": [
                 "http://photoz.example.com/dev/scopes/view",
                 "http://photoz.example.com/dev/scopes/all"
             ]
         }
     ]
 }' \
https://openam.example.com:8443/openam/json/users/demo\
/uma/policies/43225628-4c5b-4206-b7cc-5164da81decd0
 {}
``` 
On success, an HTTP 204 Empty status code is returned, with an empty JSON body as the response.

If the policy ID does not exist, an HTTP 404 Not Found status code is returned, as follows:

```
{
    "code": 404,
    "reason": "Not Found",
    "message": "UMA Policy not found, 43225628-4c5b-4206-b7cc-5164da81decd0"
 }
``` 
If the permissions are not correct, an HTTP 400 Bad Request status code is returned, for example:

```
{
    "code": 400,
    "reason": "Bad Request",
    "message": "Invalid UMA policy permission. Missing required attribute, 'subject'."
 }
``` 
If the policy ID in the URL does not match the policy ID used in the sent JSON body, an HTTP 400 Bad Request status code is returned, for example:

```
{
    "code": 400,
    "reason": "Bad Request",
    "message": "Policy ID does not match policy ID in the body."
 }
``` 

To Delete an UMA Policy

To delete a policy, the resource owner or an administrator user must be logged in to the authorization server and have an SSO token issued to them. The ["To Create an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-an-uma-policy) to read must also be known.

The ID used for a policy is always identical to the ID of the resource set it protects.

*   Create a DELETE request to the policies endpoint, including the SSO token in a header based on the configured session cookie name (default: `iPlanetDirectoryPro`), and the resource set ID as part of the URL.

The SSO token must have been issued to the user specified in the URL. In this example, the user is `demo`. 
The following example uses an SSO token to delete a policy with ID `43225628-4c5b-4206-b7cc-5164da81decd0` belonging to user _demo_:

```
$ curl \
--request DELETE \
--header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
https://openam.example.com:8443/openam/json/users/demo\
/uma/policies/43225628-4c5b-4206-b7cc-5164da81decd0
 {}
``` 
On success, an HTTP 200 OK status code is returned, with an empty JSON body as the response.

If the policy ID does not exist, an HTTP 404 Not Found status code is returned, as follows:

```
{
     "code": 404,
     "reason": "Not Found",
     "message": "UMA Policy not found, 43225628-4c5b-4206-b7cc-5164da81decd0"
 }
``` 

To Query UMA Policies

To query policies, the resource owner or an administrator user must be logged in to the authorization server and have an SSO token issued to them. The ["To Create an UMA Policy"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-create-an-uma-policy) to read must also be known.

*   Create a GET request to the policies endpoint, including the SSO token in a header based on the configured session cookie name (default: `iPlanetDirectoryPro`).

The SSO token must have been issued to the user specified in the URL, or to an administrative user such as `amadmin`. In this example, the user is `demo`. 
Use the following query string parameters to affect the returned results:

`_sortKeys=[+-]field[,field…​]`
Sort the results returned, where _field_ represents a field in the JSON policy objects returned.

For UMA policies, only the `policyId` and `name` fields can be sorted.

Optionally use the `+` prefix to sort in ascending order (the default), or `-` to sort in descending order.

`_pageSize=integer`
Limit the number of results returned.

`_pagedResultsOffset=integer`
Start the returned results from the specified index.

`_queryFilter`
The _queryFilter parameter can take `true` to match every policy, `false` to match no policies, or a filter of the following form to match field values: `field operator value` where _field_ represents the field name, _operator_ is the operator code, _value_ is the value to match, and the entire filter is URL-encoded. Only the equals (`eq`) operator is supported by the `/uma/policies` endpoint.

The _field_ value can take the following values:

    *   `resourceServer` - the resource server that created the resource set.

    *   `permissions/subject` - the list of subjects that are assigned scopes in the policy.

Filters can be composed of multiple expressions by a using boolean operator `AND`, and by using parentheses, `(expression)`, to group expressions.

You must URL-encode the filter expression in `_queryFilter=filter`. So, for example, the following filter: `resourceServer eq "UMA-Resource-Server" AND permissions/subject eq "user.1"` When URL-encoded becomes: `resourceServer+eq+%22UMA-Resource-Server%22+AND+permissions%2Fsubject+eq+%22user.1%22`

The following example uses an SSO token to query the policies belonging to user _demo_, which have a subject `user.1` in the permissions:

```
$ curl \
 --header "iPlanetDirectoryPro: AQIC5wM2LY4S...Q4MTE4NTA2*" \
 --get \
 --data-urlencode '_sortKeys=policyId,name' \
 --data-urlencode '_pageSize=1' \
 --data-urlencode '_pagedResultsOffset=0' \
 --data-urlencode \
  '_queryFilter=permissions/subject eq "user.1"' \
 https://openam.example.com:8443/openam/json/users/demo/uma/policies
{
     "result": [
         {
         "policyId": "52645907-e20b-4351-8e0c-523ebe0d44710",
         "name": "Photo Album",
         "permissions": [
             {
                 "subject": "user.1",
                 "scopes": [
                     "http://photoz.example.com/dev/scopes/view"
                 ]
             },
             {
                 "subject": "user.2",
                 "scopes": [
                     "http://photoz.example.com/dev/scopes/all",
                     "http://photoz.example.com/dev/scopes/view"
                 ]
             }
         ]
     }
 ],
 "resultCount": 1,
 "pagedResultsCookie": null,
 "remainingPagedResults": 0
}
```

On success, an HTTP 200 OK status code is returned, with a JSON body representing the policies that match the query.

If the query is not formatted correctly, for example, an incorrect field is used in the `_queryFilter`, an HTTP 500 Server Error is returned, as follows:

```
{
    "code": 500,
    "reason": "Internal Server Error",
    "message": "'/badField' not queryable"
}
```

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#accessing-uma-protected-resources)Accessing UMA-Protected Resources
---------------------------------------------------------------------------------------------------------------------------------------

To access an UMA-protected resource, a client must provide the resource server with a Requesting Party Token (RPT) obtained from OpenAM, which is acting as the authorization server.

In order to obtain access to an UMA-protected resource, the following actions take place:

![Image 5: uma rpt flow](https://doc.openidentityplatform.org/openam/_images/uma-rpt-flow.svg)

*   A requesting party, using a client application, requests access to an UMA-protected resource (labeled **1** in the diagram above).

*   The resource server registers a permission request with OpenAM on behalf of the client (**2**), which contains the ID of the resource set to access, and the requested scopes. A permission ticket is returned (**3**), which the resource server provides to the client (**4**).

For more information about registering permission requests, see ["To Register an UMA Permission Request"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#to-register-an-uma-permission-request).

*   The client uses the permission ticket, and an Authorization API Token (AAT) to acquire an RPT from OpenAM (**5**).

For more information about acquiring an RPT, see ["To Acquire a Requesting Party Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-rpt).

*   OpenAM makes a policy decision using the requested scopes, the scopes permitted in the registered resource set, and the user-created policy, and if successful returns an RPT (**6**).

*   The client presents the RPT to the resource server (**7**) which must verify the token is valid using the OpenAM introspection endpoint (**8**).

If the RPT is confirmed to be valid, and non-expired (**9**) the resource server can return the protected resource to the requesting party (**10**).

To Register an UMA Permission Request

OpenAM provides the `/uma/permission_request` REST endpoint for a resource server to register an access request on behalf of a client.

To register a permission request, the resource server must first acquire a PAT token, as described in ["To Acquire a Protection API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-pat).

Once you have the PAT bearer token, you can access the `/uma/permission_request` endpoint to register a permission request, as shown below:

*   Create a POST request to the permission_request endpoint, including the PAT bearer token in a header named `Authorization`:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --header "Authorization: Bearer 515d6551-6512-5279-98b6-c0ef3f03a723" \
 --data \
 '{
     "resource_set_id" : "43225628-4c5b-4206-b7cc-5164da81decd0",
     "scopes" : [
         "http://photoz.example.com/dev/scopes/view",
         "http://photoz.example.com/dev/scopes/all"
     ]
 }' \
 https://openam.example.com:8443/openam/uma/permission_request
 {
    "ticket": "dc630c21-7d55-45bf-958d-24d624441138"
 }
``` 
On success, an HTTP 201 Created status code is returned, as well as a `ticket` property in the JSON-formatted body, which can be used by the client to acquire a requesting party token. For more information, see ["To Acquire a Requesting Party Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-rpt).

If the resource set does not allow the requested scopes, an error is returned, as follows:

```
{
    "error_description": "Requested scopes are not in allowed scopes for resource set.",
    "error": "invalid_scope"
}
``` 

To Acquire an Authorization API Token

You must have first ["Registering OAuth 2.0 Clients With the Authorization Service"](https://doc.openidentityplatform.org/openam/admin-guide/chap-oauth2#register-oauth2-client) with a name, such as _UMA-Client_ and a client password, such as _password_. Ensure that `uma_authorization` is in the list of available scopes in the client, and a redirection URI is configured:

1.   Direct the requesting party to the authorization server to obtain an AAT token. The URL should specify the client name registered above, the redirect URI, and request the `uma_authorization` scope, as shown in the example below:

`https://openam.example.com:8443/openam/oauth2/authorize?client_id=UMA-Client&redirect_uri=http://openam.example.com:8080&response_type=code&scope=uma_authorization`

This example uses the OAuth 2.0 code grant, however the UMA client can use any of the OAuth 2.0 grants to obtain the access token.

2.   After logging in, the consent screen asks the requesting party to allow or deny the requested scopes.

![Image 6: uma client auth request](https://doc.openidentityplatform.org/openam/_images/uma-client-auth-request.png)

1.   If the requesting party allows access, they are sent to the configured redirection URL, which will have a `code` query string parameter added, which is used to request the AAT.

2.   Create a POST request to the `/oauth2/access_token` endpoint, with the client credentials registered earlier, a grant type of `authorization_code`, a redirect URL, and the value of the `code` query string parameter returned in the previous step, as shown below:

```
$ curl \
 --request POST \
 --data 'client_id=UMA-Client' \
 --data 'client_secret=password' \
 --data 'grant_type=authorization_code' \
 --data 'code=2b911969-5b8e-4d07-bf34-612917a37c9d' \
 --data 'redirect_uri=http%3A%2F%2Fopenam.example.com%3A8080' \
 http://openam.example.com:8080/openam/oauth2/access_token

{
 "scope": "uma_authorization print",
 "expires_in": 599,
 "token_type": "Bearer",
 "refresh_token": "e77fac0e-0dc6-40c3-a600-3309451bd6ee",
 "access_token": "d47c2278-460b-41e8-bf98-a8a1206e2c58"
}
``` 
The value returned in `access_token` is the AAT bearer token, used in the following procedures.

To Acquire a Requesting Party Token

OpenAM provides the `/uma/authz_request` REST endpoint for acquiring a Requesting Party Token (RPT).

The endpoint is protected - access requires a Authorization API Token (AAT) - an OAuth 2.0 token with a scope of `uma_authorization`. A client must acquire an AAT in order to use the authorization request endpoint. For more information, see ["To Acquire an Authorization API Token"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#uma-acquire-aat).

Once the client has an AAT bearer token, it can access the `/uma/authz_request` endpoint to acquire an RPT, as shown below:

*   Create a POST request to the authz_request endpoint, including the AAT bearer token in a header named `Authorization`, and the permission token in the JSON body of the request, as follows:

```
$ curl \
 --request POST \
 --header "Content-Type: application/json" \
 --header "Authorization: Bearer 3b08e99c-b09d-4a65-9780-ea0c9e1f0f52" \
 --data \
 '{
  "ticket": "dc630c21-7d55-45bf-958d-24d624441138"
 }' \
 https://openam.example.com:8443/openam/uma/authz_request
 {
     "rpt": "162d6137-68a4-4e8e-950d-edd834589eb73"
 }
``` 
On success, an HTTP 201 Created status code is returned, as well as the `rpt` property in the JSON-formatted body.

If the resource owner has not shared the resource with the requesting party, an HTTP 403 Forbidden is returned. If OpenAM is configured to email the resource owner upon pending request creation as described in ["UMA Provider"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#uma-provider-configuration) in the _Reference_, the JSON body returned includes a message that the resource owner will be notified to allow or deny access to the resource, as shown below:

```
{
  "error": "request_submitted",
  "error_description": "The client is not authorised to access the requested resource set.
   A request has been submitted to the resource owner requesting access to the resource"
}
``` 
For more information, see ["Managing Pending UMA Permission Requests"](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-pending-uma-requests)

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-uma#managing-pending-uma-requests)Managing Pending UMA Permission Requests

OpenAM supports an UMA workflow in which a user can request access to a resource that has not been explicitly shared with them. The resource owner receives a notification of the request and can choose to allow or deny access.

To View and Manage Pending Access Requests

Manage pending requests for access to resources by using the steps below:

1.   Login to OpenAM as the resource owner, and then navigate to Shares > Requests.

The Requests page is displayed:

![Image 7: uma pending requests](https://doc.openidentityplatform.org/openam/_images/uma-pending-requests.png)

1.   Review the pending request, and take one of the following actions:

    *   Click Allow to approve the request.

You can remove permissions from the request by clicking the permission, and then press either **Delete** or **Backspace**. Select the permission from the drop-down list to return it to the permissions granted to the resource owner. 
The required UMA policy will be created, and optionally the requesting party will be notified that they can now access the resource.

The requesting party can view a list of resources to which they have access by navigating to Shares > Resources > Shared with me.

    *   Click Deny to prevent the requesting party from accessing the resource. The pending request is removed, and the requesting party will not be notified.

2.   After allowing or denying access to a resource, an entry is created in the History page.

To view a list of actions that have occurred, navigate to Shares > History.
