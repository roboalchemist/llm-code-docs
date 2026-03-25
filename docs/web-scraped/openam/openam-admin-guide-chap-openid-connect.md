# Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect

Title: Managing OpenID Connect 1.0 Authorization :: Open Identity Platform Documentation

URL Source: https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect

Markdown Content:
This chapter covers OpenAM support for OpenID Connect 1.0. [OpenID Connect](http://openid.net/connect/) 1.0 is an authentication layer built on OAuth 2.0. OpenID Connect 1.0 is a specific implementation of OAuth 2.0 where the identity provider that runs the authorization server also holds the protected resource that the third-party application aims to access. This resource is the _UserInfo_, information about the authenticated end user expressed in a standard format. In this way, OpenID Connect 1.0 allows relying parties both to verify the identity of the end user and also to obtain user information using REST. This contrasts with OAuth 2.0, which only defines the authorization mechanism. The names used in OpenID Connect 1.0 differ from those used in OAuth 2.0. In OpenID Connect 1.0, the key entities are the following:

*   The _end user_ (OAuth 2.0 resource owner) whose user information the application needs to access.

The end user wants to use an application through existing identity provider account without signing up to and creating credentials for yet another web service.

*   The _Relying Party_ (RP) (OAuth 2.0 client) needs access to the end user’s protected user information.

For example, an online mail application needs to know which end user is accessing the application in order to present the correct inbox.

As another example, an online shopping site needs to know which end user is accessing the site in order to present the right offerings, account, and shopping cart.

*   The _OpenID Provider_ (OP) (OAuth 2.0 authorization server and also resource server) that holds the user information and grants access.

OpenAM can play this role in an OpenID Connect deployment.

The OP effectively has the end user’s consent to providing the RP with access to some of its user information. As OpenID Connect 1.0 defines unique identification for an account (subject identifier + issuer identifier), the RP can use this as a key to its own user profile.

In the case of the online mail application, this key could be used to access the mailboxes and related account information. In the case of the online shopping site, this key could be used to access the offerings, account, shopping cart and so forth. The key makes it possible to serve users as if they had local accounts.

In OpenID Connect, the relying party can verify claims about the identity of the end user, and log the user out at the end of a session. OpenID Connect also makes it possible to discover the OpenID Provider for an end user, and to register relying party client applications dynamically. OpenID connect services are built on OAuth 2.0, JSON Web Token (JWT), WebFinger and Well-Known URIs.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#about-openid-connect-support)About OpenID Connect 1.0 Support in OpenAM
------------------------------------------------------------------------------------------------------------------------------------------------------

In its role as OpenID Provider, OpenAM lets OpenID Connect relying parties (clients) discover its capabilities, handles both dynamic and static registration of OpenID Connect relying parties, responds to relying party requests with authorization codes, access tokens, and user information according to the Authorization Code and Implicit flows of OpenID Connect, and manages sessions.

This section describes how OpenAM fits into the OpenID Connect picture in terms of the roles that it plays in the authorization code and implicit flows, provider discovery, client registration, and session management.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-basic-client-profile)OpenID Connect Authorization Code Flow

The OpenID Connect Authorization Code Flow specifies how the relying party interacts with the OpenID Provider, in this case OpenAM, based on use of the OAuth 2.0 authorization grant. The following sequence diagram shows successful processing from the authorization request, through grant of the authorization code, access token, and ID token, and optional use of the access token to get information about the end user.

![Image 1: openid connect basic](https://doc.openidentityplatform.org/openam/_images/openid-connect-basic.svg)

In addition to what OAuth 2.0 specifies, OpenID Connect uses an ID token so the relying party can validate claims about the end user. It also defines how to get user information, such as profile, email, address, and phone details from the UserInfo endpoint with a valid access token.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-implicit-client-profile)OpenID Connect Implicit Flow

The OpenID Connect Implicit Flow specifies how the relying party interacts with the OpenID Provider, in this case OpenAM, based on use of the OAuth 2.0 implicit grant. The following sequence diagram shows successful processing from the authorization request, through grant of the access and ID tokens, and optional use of the access token to get information about the end user.

![Image 2: openid connect implicit](https://doc.openidentityplatform.org/openam/_images/openid-connect-implicit.svg)

As for the Authorization Code Flow, the Implicit Flow specifies an ID token so that the relying party can validate claims about the end user. It also defines how to get user information, such as profile, email, address, and phone details from the UserInfo endpoint with a valid access token.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-discovery)OpenID Connect Discovery

OpenID Connect defines how a relying party can discover the OpenID Provider and corresponding OpenID Connect configuration for an end user. The discovery mechanism relies on WebFinger to get the information based on the end user’s identifier. The server returns the information in JSON Resource Descriptor (JRD) format.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-client-registration)OpenID Connect Relying Party Registration

OpenID Connect relying parties register OAuth 2.0 client profiles with OpenAM. Relying parties can register with OpenAM as a provider both statically, as for other OAuth 2.0 clients, and also dynamically, as specified by OpenID Connect Discovery. To allow dynamic registration, you register an initial OAuth 2.0 client that other relying parties can use to get access tokens for registration.

You can also enable OpenID Connect relying parties to register dynamically without having to provide an access token. For details, see the documentation on the advanced server property, `org.forgerock.openam.openidconnect.allow.open.dynamic.registration`, in ["Advanced"](https://doc.openidentityplatform.org/openam/reference/chap-config-ref#servers-advanced-configuration) in the _Reference_. Take care to limit or throttle dynamic registration if you enable this capability on production systems.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-session-management)OpenID Connect Session Management

OpenID Connect lets the relying party track whether the end user is logged in at the provider, and also initiate end user logout at the provider. The specification has the relying party monitor session state using an invisible iframe and communicate status using the HTML 5 postMessage API.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#configure-openid-connect-provider)Configuring OpenAM As OpenID Connect Provider
--------------------------------------------------------------------------------------------------------------------------------------------------------------

You can configure OpenAM’s OAuth 2.0 provider service to double as an OpenID Connect provider service.

To Set Up the OAuth 2.0 Provider Service for OpenID Connect

Follow the steps in this procedure to set up the OAuth2 provider service with OpenID Connect defaults by using the Configure OAuth Provider wizard:

When you create the service with the Configure OAuth Provider wizard, the wizard also creates a standard policy in the Top Level Realm (/) to protect the authorization endpoint. In this configuration, OpenAM serves the resources to protect, and no separate application is involved. OpenAM therefore acts both as the policy decision point and policy enforcement point that protects the OAuth 2.0 authorization endpoint used by OpenID Connect.

There is no requirement to use the wizard or to create the policy in the Top Level Realm. However, if you create the OAuth 2.0 provider service without the wizard, then you must set up the policy independently, if required. The policy must appear in a policy set of type `iPlanetAMWebAgentService`. When configuring the policy allow all authenticated users to perform HTTP GET and POST requests on the authorization endpoint. The authorization endpoint is described in ["OAuth 2.0 Client and Resource Server Endpoints"](https://doc.openidentityplatform.org/openam/dev-guide/chap-client-dev#rest-api-oauth2-client-endpoints) in the _Developer’s Guide_. For details on creating policies, see ["Defining Authorization Policies"](https://doc.openidentityplatform.org/openam/admin-guide/chap-authz-policy#chap-authz-policy).

1.   In the OpenAM console, select Realms >_Realm Name_> Dashboard > Configure OAuth Provider > Configure OpenID Connect.

2.   On the Configure OAuth2/OpenID Connect Service page, select the Realm for the provider service.

3.   (Optional) If necessary, adjust the lifetimes for authorization codes, access tokens, and refresh tokens.

4.   (Optional) Select Issue Refresh Tokens unless you do not want the authorization service to supply a refresh token when returning an access token.

5.   (Optional) Select Issue Refresh Tokens on Refreshing Access Tokens if you want the authorization service to supply a new refresh token when refreshing an access token.

6.   (Optional) If you have a custom scope validator implementation, put it on the OpenAM classpath, for example `/path/to/tomcat/webapps/openam/WEB-INF/lib/`, and specify the class name in the Scope Implementation Class field. For an example, see ["Customizing OAuth 2.0 Scope Handling"](https://doc.openidentityplatform.org/openam/dev-guide/chap-customizing#sec-oauth2-scopes) in the _Developer’s Guide_.

7.   Click Create to save your changes.

OpenAM creates an OAuth2 provider service, with OpenID Connect default parameter values, and a policy to protect the OAuth2 authorization endpoints.

If an OAuth2 provider service already exists, it will be overwritten with the new OpenID Connect parameter values. 
8.   To access the provider service configuration in the OpenAM console, browse to Realms >_Realm Name_> Services, and then click OAuth2 Provider.

For OpenID Connect providers you may want to configure the following settings:

    *   The optional Remote JSON Web Key URL field allows you to set a URL to a [JSON Web Key set](https://tools.ietf.org/html/rfc7517) with the public key(s) for the provider.

If this setting is not configured, then OpenAM provides a local URL to access the public key of the private key used to sign ID tokens.

    *   The Subject Types supported map allows you to support pairwise subject types as described in the OpenID Connect core specification section concerning [Subject Identifier Types](http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes).

    *   The ID Token Signing Algorithms supported list allows you to change the list of algorithms used to sign ID Tokens.

    *   The Supported Claims list allows you to restrict the claims supported by OpenAM’s userinfo endpoint.

For more information, see ["Understanding OpenID Connect Scopes and Claims"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#understanding-openid-connect-scopes-and-claims).

    *   The Alias of ID Token Signing Key alias allows you to set the key pair alias for the key used to sign ID Tokens when using a signing algorithm that involves asymmetric keys.

    *   The Allow Open Dynamic Client Registration checkbox enables relying parties to register without using an access token.

    *   The Generate Registration Access Tokens checkbox has OpenAM generate Registration Access Tokens for dynamic client registration when Allow Open Dynamic Client Registration is enabled. This allows the client to view and update its registration.

9.   Click Save to complete the process.

If your provider is part of a GSMA Mobile Connect deployment, see ["Configuring OpenAM as an OP for Mobile Connect"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#mobile-connect-configure).

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#understanding-openid-connect-scopes-and-claims)Understanding OpenID Connect Scopes and Claims

This section explains how scopes and claims can be used when OpenAM is acting as an OpenID Connect provider.

When OpenAM is configured as an OAuth 2.0 provider, a scope is considered to be a concept, rather than directly relating to a piece of data in the user profile. For example, Facebook has an OAuth 2.0 scope named `read_stream`. OpenAM returns whether the scope is allowed or not, with no associated data.

When OpenAM is configured as an OpenID Connect provider, scopes can relate to data in a user profile by making use of one or more claims. Each claim maps directly to an attribute in the user profile.

For example, OpenAM supports a scope named `profile` when configured as an OpenID Connect provider, which by default is made up of the following claims:

OpenID Connect Scope Default Claim Mappings| Claim | User profile attribute |
| --- | --- |
| `given_name` | `givenname` |
| `zoneinfo` | `preferredtimezone` |
| `family_name` | `sn` |
| `locale` | `preferredlocale` |
| `name` | `cn` |

The mappings between scopes, claims, and user profile attributes are controlled by the OIDC Claims Script specified in the OAuth 2.0 provider. For more information, see ["Using the Default Scripts"](https://doc.openidentityplatform.org/openam/dev-guide/chap-scripting#sec-scripting-default-scripts) in the _Developer’s Guide_.

As each claim represents a piece of information from the user profile, OpenAM displays the actual data the relying party is given if the user clicks Allow:

![Image 3: openid consent](https://doc.openidentityplatform.org/openam/_images/openid-consent.png)

You can configure OpenAM to support requests for individual claims as query parameters, as described in [section 5.5 of the OpenID Connect specification](http://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter), by enabling the `claims_parameter_supported` option.

In section 5.6 of the specification, OpenAM supports _Normal Claims_. The optional _Aggregated Claims_ and _Distributed Claims_ representations are not supported by OpenAM.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#configure-openid-connect-discovery)Configuring OpenAM For OpenID Connect Discovery
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to allow relying parties to discover the OpenID Connect Provider for an end user, OpenAM supports OpenID Connect Discovery 1.0. In addition to discovering the OpenID Provider for an end user, the relying party can also request the OpenID Provider configuration.

OpenAM as OpenID Connect provider exposes two endpoints for discovery:

*   `/oauth2/.well-known/webfinger`

*   `/oauth2/.well-known/openid-configuration` A relying party needs to be able to discover the OpenID Connect provider for an end user. In this case you should consider redirecting requests to URIs at the server root, such as `http://www.example.com/.well-known/webfinger` and `http://www.example.com/.well-known/openid-configuration`, to these Well-Known URIs in OpenAM’s space.

Discovery relies on [WebFinger](http://tools.ietf.org/html/draft-ietf-appsawg-webfinger), a protocol to discover information about people and other entities using standard HTTP methods. WebFinger uses [Well-Known URIs](http://tools.ietf.org/html/rfc5785), which defines the path prefix `/.well-known/` for the URLs defined by OpenID Connect Discovery.

Unless you deploy OpenAM in the root context of a container listening on port 80 on the primary host for your domain, relying parties need to find the right _host:port/deployment-uri_ combination to locate the well-known endpoints. Therefore you must manage the redirection to OpenAM. If you are using WebFinger for something else than OpenID Connect Discovery, then you probably also need proxy logic to route the requests.

OpenID Connect Discovery requires an OAuth 2.0 provider service to be configured within OpenAM. The service must have `openid` as a supported scope in order to use the `/oauth2/.well-known/openid-configuration` endpoint. For information on configuring an OAuth 2.0 provider service for OpenID Connect in OpenAM, see ["Configuring OpenAM As OpenID Connect Provider"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#configure-openid-connect-provider).

To retrieve the OpenID Connect provider for an end user, the relying party needs the following:

`host`
The server where the relying party can access the WebFinger service.

Notice that this is a host name rather than a URL to the endpoint, which is why you might need to redirect relying parties appropriately as described above.

`resource`
Identifies the end user that is the subject of the request.

The relying party must percent-encode the resource value when using it in the query string of the request, so when using the `acct` URI scheme and the resource is `acct:user@example.com`, then the value to use is `acct%3Auser%40example.com`.

`rel`
URI identifying the type of service whose location is requested.

In this case `http://openid.net/specs/connect/1.0/issuer`, which is `http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer`.

If you have not set up the redirection to the root of the domain yet, you can test the endpoint for the demo user account with the following curl:

```
$ curl \
 "https://openam.example.com:8443/openam/oauth2/.well-known/webfinger\
?resource=acct%3Ademo%40example.com\
&rel=http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer"
{
  "subject": "acct:demo@example.com",
  "links": [
    {
      "rel": "http://openid.net/specs/connect/1.0/issuer",
      "href": "https://openam.example.com:8443/openam"
    }
  ]
}
```

The example shows that the OpenID Connect provider for the OpenAM demo user is indeed the OpenAM server.

The relying party can also discover the OpenID Connect provider configuration. If you have not set up the redirection to the root of the domain yet, you can test this making the following curl call:

```
$ curl https://openam.example.com:8443/openam/oauth2/.well-known/openid-configuration
{
    "response_types_supported": [
        "token id_token",
        "code token",
        "code token id_token",
        "token",
        "code id_token",
        "code",
        "id_token"
    ],
    "registration_endpoint": "https://openam.example.com:8443/openam/oauth2/connect/register",
    "token_endpoint": "https://openam.example.com:8443/openam/oauth2/access_token",
    "end_session_endpoint": "https://openam.example.com:8443/openam/oauth2/connect/endSession",
    "version": "3.0",
    "userinfo_endpoint": "https://openam.example.com:8443/openam/oauth2/userinfo",
    "subject_types_supported": [
        "public"
    ],
    "issuer": "https://openam.example.com:8443/openam",
    "jwks_uri": "https://openam.example.com:8443/openam/oauth2/connect/jwk_uri?realm=/",
    "id_token_signing_alg_values_supported": [
        "HS256",
        "HS512",
        "RS256",
        "HS384"
    ],
    "check_session_iframe": "https://openam.example.com:8443/openam/oauth2/connect/checkSession",
    "claims_supported": [
        "phone",
        "email",
        "address",
        "openid",
        "profile"
    ],
    "authorization_endpoint": "https://openam.example.com:8443/openam/oauth2/authorize"
}
```

When the OpenID Connect provider is configured in a subrealm, then relying parties can get the configuration by passing the realm as a query string parameter, as in `https://openam.example.com:8443/openam/oauth2/.well-known/openid-configuration?realm=realm-name`.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#configure-base-url-source)Configuring the Base URL Source Service
------------------------------------------------------------------------------------------------------------------------------------------------

In many deployments, OpenAM determines the base URL of a provider using the incoming HTTP request. However, there are often cases when the base URL of a provider cannot be determined from the incoming request alone, especially if the provider is behind some proxying application. For example, if an OpenAM instance is part of a site where the external connection is over SSL but the request to the OpenAM instance is over plain HTTP, then OpenAM would have difficulty in reconstructing the base URL of the provider.

In these cases, OpenAM supports a provider service that allows a realm to have a configured option for obtaining the base URL including protocol for components that need to return a URL to the client.

To Configure the Base URL Source Service

1.   Log in to the OpenAM console as an administrative user, such as `amAdmin`, and then navigate to Realms >_Realm Name_> Services.

2.   Click Add a Service, select Base URL Source, and then click Create.

3.   For Base URL Source, select one of the following options:

Base URL Source Options| Option | Description |
| --- | --- |
| Extension class | Click the Extension class to return a base URL from a provided `HttpServletRequest` object. In the Extension class name field, enter `org.forgerock.openam.services.baseurl.BaseURLProvider`. |
| Fixed value | Click Fixed value to enter a specific base URL value. In the Fixed value base URL field, enter the base URL. |
| Forwarded header | Click Forwarded header to retrieve the base URL from the `Forwarded` header field in the HTTP request. The Forwarded HTTP header field is standardized and specified in [RFC 7239](http://tools.ietf.org/html/rfc7239). |
| Host/protocol from incoming request (default) | Click Host/protocol from incoming request to get the hostname, server name, and port from the HTTP request. |
| X-Forwarded-* headers | Click X-Forwarded-* headers to use non-standard header fields, such as `X-Forwarded-For`, `X-Forwarded-By`, and `X-Forwarded-Proto`. |
4.   In the Context path, enter the context path for the base URL. If provided, the base URL includes the deployment context path appended to the calculated URL. For example, `/openam`.

5.   Click Finish to save your configuration.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#register-openid-connect-clients)Registering OpenID Connect Relying Parties
---------------------------------------------------------------------------------------------------------------------------------------------------------

OpenID Connect relying parties can register with OpenAM both statically through OpenAM console for example, and also dynamically using OpenID Connect 1.0 Dynamic Registration.

To Register a Relying Party With OpenAM Console

Registering a relying party by using the OpenAM console consists of first creating an OAuth 2.0 Client agent profile, and then editing the profile for the settings pertinent to OpenID Connect 1.0.

1.   In the OpenAM console under Realms >_Realm Name_> Agents > OAuth 2.0/OpenID Connect Client > Agent, click New…​, then provide the client identifier and client password, and finally click Create to create the profile.

2.   To edit the profile to match the relying party configuration, follow the hints in ["Configuring OAuth 2.0 and OpenID Connect 1.0 Clients"](https://doc.openidentityplatform.org/openam/admin-guide/chap-agents#configure-oauth2-client) .

In order to read and edit the relying party profile dynamically later without using OpenAM console, be sure to set an access token in the Access Token field.

To Register a Relying Party Dynamically

For dynamic registration you need the relying party profile data, and an access token to write the configuration to OpenAM by HTTP POST. To obtain the access token, register an initial client statically after creating the provider, as described in ["To Register a Relying Party With OpenAM Console"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#register-openid-connect-client-static). Relying parties can then use that client to obtain the access token needed to perform dynamic registration.

As described in ["OpenID Connect Relying Party Registration"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-client-registration), you can allow relying parties to register without having an access token by setting the advanced server property, `org.forgerock.openam.openidconnect.allow.open.dynamic.registration`, to `true`. When using that setting in production systems, take care to limit or throttle dynamic registration.

On successful registration, OpenAM responds with information including an access token to allow the relying party subsequently to read and edit its profile:

1.   Register an initial OAuth 2.0 client statically with a client ID, such as `masterClient` and client secret like `password`.

2.   Obtain an access token using the client you registered.

For example, if you created the client as described in the previous step, and OpenAM administrator `amadmin` has password `password`, you can use the OAuth 2.0 resource owner password grant as in the following example:

```
$ curl \
 --request POST \
 --user "masterClient:password" \
 --data "grant_type=password&username=amadmin&password=password" \
 https://openam.example.com:8443/openam/oauth2/access_token
{
    "expires_in": 59,
    "token_type": "Bearer",
    "refresh_token": "26938cd0-6870-4e31-ade9-df31afc37ee1",
    "access_token": "515d6551-4512-4279-98b6-c0ef3f03a722"
}
``` 
3.   HTTP POST the relying party registration profile to the `/oauth2/connect/register` endpoint, using bearer token authorization with the access token you obtained from OpenAM.

Ensure that you provide a `client_name` when registering the client. Without the `client_name` value the auto-generated `client_id` will be used on consent screens. The client ID is a UUID string and may not be desirable on end-user facing pages.

For an example written in JavaScript, see the registration page in the [OpenID Connect examples](https://github.com/OpenIdentityPlatform/openam-openid). Successful registration shows a response that includes the client ID and client secret. Lines are folded in the following example:

```
{
  "issued_at": 1392364349,
  "expires_at": 0,
  "client_secret": "7f446ca9-3f1f-48fb-bf8c-150b9e643f29",
  "client_name": "Example.com OpenID Connect Client",
  "redirect_uris": [
    "https://openam.example.com:8443/openid/cb-basic.html",
    "https://openam.example.com:8443/openid/cb-implicit.html"
  ],
  "registration_access_token": "515d6551-4512-4279-98b6-c0ef3f03a722",
  "client_id": "6e4abd50-3f03-41dc-b807-c6705c3e45d7",
  "registration_client_uri":
     "https://openam.example.com:8443/openam/oauth2/connect/register
     ?client_id=6e4abd50-3f03-41dc-b807-c6705c3e45d7"
}
```

json 

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#manage-sessions-openid-connect)Managing OpenID Connect User Sessions
---------------------------------------------------------------------------------------------------------------------------------------------------

OpenID Connect Session Management 1.0 allows the relying party to manage OpenID Connect sessions, making it possible to know when the end user should be logged out.

As described in the [OpenID Connect Session Management 1.0](http://openid.net/specs/openid-connect-session-1_0.html) specification, OpenAM’s OpenID Provider exposes both a `check_session_iframe` URL that allows the relying party to receive notifications when the end user’s session state changes at the provider, and also an `end_session_endpoint` URL to which to redirect an end user for logout.

When registering your relying party that uses session management, you set the OAuth 2.0 client agent profile properties Post Logout Redirect URI and Client Session URI, described in ["Configuring OAuth 2.0 and OpenID Connect 1.0 Clients"](https://doc.openidentityplatform.org/openam/admin-guide/chap-agents#configure-oauth2-client). The Post Logout Redirect URI is used to redirect the end user user-agent after logout. The Client Session URI is the relying party URI where OpenAM sends notifications when the end user’s session state changes.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openid-connect-examples)Relying Party Examples
-----------------------------------------------------------------------------------------------------------------------------

OpenID Connect Authorization Code Flow and Implicit Flow define how clients interact with the provider to obtain end user authorization and profile information. Although you can run the simple example relying parties that are mentioned in this section without setting up Transport Layer Security, do not deploy relying parties in production without securing the transport.

Code for the relying party examples shown here is [available online](https://github.com/OpenIdentityPlatform/openam-openid). Clone the example project to deploy it in the same web container as OpenAM. Edit the configuration at the outset of the `.js` files in the project, register a corresponding profile for the example relying party as described in ["Registering OpenID Connect Relying Parties"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#register-openid-connect-clients), and browse the deployment URL to see the initial page.

![Image 4: openid connect example start page](https://doc.openidentityplatform.org/openam/_images/openid-connect-example-start-page.png)

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openid-basic-profile-example)Authorization Code Flow Example

OpenID Connect Authorization Code Flow is designed for web-based relying parties that use the OAuth 2.0 Authorization Code grant type. This grant type makes it possible for the relying party to get the access code by using the authorization code directly, without passing through the end user’s browser. To protect its client secret (password), part of the relying party must run on a server.

In the example, the Basic Client Profile Start Page describes the prerequisite configuration, which must be part of the relying party profile that is stored in the OpenAM realm where you set up the OpenID Provider. In OpenAM console, check that the OAuth 2.0 client profile matches the settings described.

![Image 5: openid connect basic start page](https://doc.openidentityplatform.org/openam/_images/openid-connect-basic-start-page.png)

Log out of OpenAM, and click the link at the bottom of the page to request authorization. The link sends an HTTP GET request asking for `openid profile` scopes to the OpenID Provider authorization URI.

If everything is configured correctly, OpenAM’s OpenID Provider has you authenticate as an end user, such as the demo user with username `demo` and password `changeit`, and grant (Allow) the relying party access to your profile.

If you successfully authenticate and allow the example relying party access to your profile, OpenAM returns an authorization code to the example relying party. The example relying party then uses the authorization code to request an access token and an ID token. It shows the response to that request. It also validates the ID token signature using the default (HS256) algorithm, and decodes the ID token to validate its content and show it in the output. Finally, it uses the access token to request information about the end user who authenticated, and displays the result.

![Image 6: openid connect basic response page](https://doc.openidentityplatform.org/openam/_images/openid-connect-basic-response-page.png)

Notice that in addition to the standard payload, the ID token indicates the end user’s OpenAM realm, in this case `"realm": "/"`.

### [](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openid-implicit-profile-example)Implicit Flow Example

OpenID Connect Implicit Flow is designed for relying parties that use the OAuth 2.0 Implicit grant type. This grant type is designed for relying parties implemented in a browser. Rather than protect a client secret, the client profile must register a protected redirect URI in advance with the OpenID Provider.

In the example, the Implicit Client Profile Start Page describes the prerequisite configuration, which must be part of the relying party profile that is stored in the OpenAM realm where you set up the OpenID Provider. In OpenAM console, check that the OAuth 2.0 client profile matches the settings described. If you have already configured the agent profile for the Authorization Code Flow example, then you still need to add the redirect URI for the Implicit Flow.

![Image 7: openid connect implicit start page](https://doc.openidentityplatform.org/openam/_images/openid-connect-implicit-start-page.png)

Log out of OpenAM, and click the link at the bottom of the page to request authorization. The link sends an HTTP GET request asking for `id_token token` response types and `openid profile` scopes to the OpenID Provider authorization URI.

If everything is configured correctly, OpenAM’s OpenID Provider has you authenticate as an end user, such as the demo user with username `demo` and password `changeit`, and grant (Allow) the relying party access to your profile.

If you successfully authenticate and allow the example relying party access to your profile, OpenAM returns the access token and ID token directly in the fragment (after `#`) of the redirect URI. The relying party does not get an authorization code. The relying party shows the response to the request. It also validates the ID token signature using the default (HS256) algorithm, and decodes the ID token to validate its content and show it in the output. Finally, the relying party uses the access token to request information about the end user who authenticated, and displays the result.

![Image 8: openid connect implicit response page](https://doc.openidentityplatform.org/openam/_images/openid-connect-implicit-response-page.png)

As for the Authorization Code Flow example, the ID Token indicates the end user’s OpenAM realm and OpenAM token ID in addition to the standard information.

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#mobile-connect)Using OpenAM with Mobile Connect
------------------------------------------------------------------------------------------------------------------------------

[GSMA Mobile Connect](http://www.gsma.com/personaldata/mobile-connect) is an application of OpenID Connect (OIDC). Mobile Connect builds on OIDC to facilitate use of mobile phones as authentication devices independently of the service provided and independently of the device used to consume the service. Mobile Connect thus offers a standard way for Mobile Network Operators to act as general-purpose identity providers, providing a range of levels of assurance and profile data to Mobile Connect-compliant Service Providers. This section includes an overview, as well as the following:

*   ["Authorization Request Parameters"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#mobile-connect-table-auth-request-params)

*   ["ID Token Properties"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#mobile-connect-table-id-token-properties)

*   ["Configuring OpenAM as an OP for Mobile Connect"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#mobile-connect-configure)

In a Mobile Connect deployment, OpenAM can play the OpenID Provider role, implementing the Mobile Connect Profile as part of the Service Provider - Identity Gateway interface.

OpenAM can also play the Authenticator role as part of the Identity Gateway - Authenticators interface. In this role, OpenAM serves to authenticate users at the appropriate Level of Assurance (LoA). In Mobile Connect, LoAs represent the authentication level achieved. A Service Provider can request LoAs without regard to the implementation, and the Identity Gateway includes a claim in the ID Token that indicates the LoA achieved.

In OpenAM, Mobile Connect LoAs map to an authentication mechanism. Service Providers acting as OpenID Relying Parties (RP) request an LoA by using the `acr_values` field in an OIDC authentication request. In OIDC, `acr_values` specifies Authentication Context Class Reference values. The RP sets `acr_values` as part of the OIDC Authentication Request. OpenAM returns the corresponding `acr` claim in the Authentication Response as the value of the ID Token `acr` field.

OpenAM as OP supports LoAs 1 (low - little or no confidence), 2 (medium - some confidence, as in single-factor authentication), and 3 (high - high confidence, as in multi-factor authentication), though out of the box it does not include support for 4, which involves digital signatures.

As Mobile Connect OP, OpenAM supports mandatory request parameters, and a number of optional request parameters:

Authorization Request Parameters| Request Parameter | Support | Description |
| --- | --- | --- |
| `response_type` | Supported | OAuth 2.0 grant type to use. Set this to `code` for the authorization grant. |
| `client_id` | Supported | Set this to the client identifier. |
| `scope` | Supported | Space delimited OAuth 2.0 scope values. Required: `openid` Optional: `profile`, `email`, `address`, `phone`, `offline_access` |
| `redirect_uri` | Supported | OAuth 2.0 URI where the authorization request callback should go. Must match the `redirect_uri` in the client profile that you registered with OpenAM. |
| `state` | Supported | Value to maintain state between the request and the callback. Required for Mobile Connect. |
| `nonce` | Supported | String value to associate the client session with the ID Token. Optional in OIDC, but required for Mobile Connect. |
| `display` | Supported | String value to specify the user interface display. |
| `login_hint` | Supported | String value indicating the the ID to use for login. When provided as part of the OIDC Authentication Request, the `login_hint` is set as the value of a cookie named `oidcLoginHint`, which is an HttpOnly cookie (only sent over HTTPS). Authentication modules can then retrieve the cookie's value. |
| `acr_values` | Supported | Authentication Context class Reference values used to communicate acceptable LoAs. When the OIDC relying party on the server provider supplies `acr_values` in the authorization request, OpenAM uses the OP configuration to map the values to authentication chains. It runs through the list of `acr_values` in order, attempting to use the first authentication chain that matches. OpenAM then returns the authentication chain used as the value of the ID token `acr` claims property. In this way the relying part on the service provider can determine the LoA achieved during authentication. |
| `dtbs` | Not supported | Data To Be Signed At present OpenAM does not support LoA 4. |

As Mobile Connect OP, OpenAM responds to a successful authorization request with a response containing all the required fields, and also the optional `expires_in` field. OpenAM supports the mandatory ID Token properties, though the relying party is expected to use the `expires_in` value, rather than specifying `max_age` as a request parameter:

ID Token Properties| Request Parameter | Support | Description |
| --- | --- | --- |
| `iss` | Supported | Issuer identifier |
| `sub` | Supported | Subject identifier By default OpenAM returns the identifier from the user profile. |
| `aud` | Supported | Audience, an array including the `client_id`. |
| `exp` | Supported | Expiration time in seconds since the epoch. |
| `iat` | Supported | Issued at time in seconds since the epoch. |
| `nonce` | Supported | The nonce supplied in the request. |
| `at_hash` | Supported. | Base64url-encoding of the SHA-256 hash of the "access_token" value. |
| `acr` | Supported | Authentication Context class Reference for the LoA achieved. For example, if the request specifies `acr_values=loa-3 loa-2` and OpenAM achieves LoA 2, then the ID token includes `"acr": "loa-2"`. |
| `amr` | Supported | Authentication Methods Reference to indicate the authentication method. OpenAM maps these to authentication modules. Suggested values include the following: `OK, DEV_PIN, SIM_PIN, UID_PWD, BIOM, HDR, OTP`. |
| `azp` | Supported | Authorized party identifier, which is the `client_id`. |

In addition to the standard OIDC user information returned with `userinfo`, OpenAM as OP for Mobile Connect returns the `updated_at` property, representing the time last updated as seconds since the epoch.

Configuring OpenAM as an OP for Mobile Connect

You configure OpenAM as an OpenID Connect provider for Mobile Connect by changing the OAuth2 Provider configuration. Follow the steps in this procedure to set up the OAuth2 provider service with Mobile Connect defaults by using the Configure OAuth Provider wizard.

When you create the OAuth2 provider service with the Configure OAuth Provider wizard, the wizard also creates a standard policy in the Top Level Realm (/) to protect the authorization endpoint. In this configuration, OpenAM serves the resources to protect, and no separate application is involved. OpenAM therefore acts both as the policy decision point and policy enforcement point that protects the OAuth 2.0 authorization endpoint used by OpenID Connect.

There is no requirement to use the wizard or to create the policy in the Top Level Realm. However, if you create the OAuth 2.0 provider service without the wizard, then you must set up the policy independently as well. The policy must appear in a policy set of type `iPlanetAMWebAgentService`. When configuring the policy allow all authenticated users to perform HTTP GET and POST requests on the authorization endpoint. The authorization endpoint is described in ["OAuth 2.0 Client and Resource Server Endpoints"](https://doc.openidentityplatform.org/openam/dev-guide/chap-client-dev#rest-api-oauth2-client-endpoints) in the _Developer’s Guide_. For details on creating policies, see ["Defining Authorization Policies"](https://doc.openidentityplatform.org/openam/admin-guide/chap-authz-policy#chap-authz-policy).

1.   In the OpenAM console, select Realms >_Realm Name_> Dashboard > Configure OAuth Provider > Configure Mobile Connect.

2.   On the Configure Mobile Connect page, select the Realm for the provider service.

3.   (Optional) If necessary, adjust the lifetimes for authorization codes, access tokens, and refresh tokens.

4.   (Optional) Select Issue Refresh Tokens unless you do not want the authorization service to supply a refresh token when returning an access token.

5.   (Optional) Select Issue Refresh Tokens on Refreshing Access Tokens if you want the authorization service to supply a refresh token when refreshing an access token.

6.   (Optional) If you have a custom scope validator implementation, put it on the OpenAM classpath, for example `/path/to/tomcat/webapps/openam/WEB-INF/lib/`, and specify the class name in the Scope Implementation Class field. For an example, see ["Customizing OAuth 2.0 Scope Handling"](https://doc.openidentityplatform.org/openam/dev-guide/chap-customizing#sec-oauth2-scopes) in the _Developer’s Guide_.

7.   Click Create to save your changes.

OpenAM creates an OAuth2 provider service with Mobile Connect default parameter values, as well as a policy to protect the OAuth2 authorization endpoints.

If an OAuth2 provider service already exists, it will be overwritten with the new Mobile Connect parameter values. 
8.   To access the provider service configuration in the OpenAM console, browse to Realms >_Realm Name_> Services, and then click OAuth2 Provider.

For Mobile Connect providers you may want to configure the following settings:

    1.   For the OpenID Connect acr_values to Auth Chain Mapping, configure the mapping between `acr_values` in the authorization request and OpenAM authentication chains.

For example, if the relying party request includes `acr_values=loa-3 loa-2` and the map includes `[loa-2]=ldapService`, and `[loa-3]=msisdnAndHotpChain`, then the authentication chain for the request is `msisdnPlusHotpChain`.

The `ssoadm` attribute is `forgerock-oauth2-provider-loa-mapping`.

    2.   For the OpenID Connect default acr claim, set the "acr" claim value to return in the ID Token when falling back to the default authentication chain.

The `ssoadm` attribute is `forgerock-oauth2-provider-default-acr`.

    3.   For the OpenID Connect id_token amr values to Auth Module mappings, set the "amr" values to return in the ID Token after successfully authenticating with specified authentication modules.

For example, you could set `[UID_PWD]=LDAP` to return `"amr": [ "UID_PWD" ]` in the ID Token after authenticating with the LDAP module.

The `ssoadm` attribute is `forgerock-oauth2-provider-amr-mappings`.

    4.   Configure the identity Data Store attributes used to return `updated_at` values in the ID Token.

For Mobile Connect clients, the user info endpoint returns `updated_at` values in the ID Token. If the user profile has never been updated `updated_at` reflects creation time.

The `updated_at` values are read from the profile attributes you specify. When using OpenDJ directory server as an identity Data Store, the value is read from the `modifyTimestamp` attribute, or the `createTimestamp` attribute for a profile that has never been modified.

The `ssoadm` attribute for Modified Timestamp attribute name is `forgerock-oauth2-provider-modified-attribute-name`.

The `ssoadm` attribute is for Created Timestamp attribute name is `forgerock-oauth2-provider-created-attribute-name`.

In addition, you must also add these attributes to the list of LDAP User Attributes for the data store. Otherwise, the attributes are not returned when OpenAM reads the user profile. To edit the list in OpenAM console, browse to Realms >_Realm Name_> Data Stores >_Data Store Name_> LDAP User Attributes.

9.   Click Save to complete the process.

A simple, non-secure GSMA Mobile Connect relying party example is [available online](https://github.com/OpenIdentityPlatform/openam-openid).

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#stateless-oidc)Stateless OpenID Connect 1.0 Access and Refresh Tokens
----------------------------------------------------------------------------------------------------------------------------------------------------

OpenAM supports _stateless_ access and refresh tokens for OpenID Connect 1.0 (OIDC). Stateless tokens allow clients to directly validate the tokens without storing session information in an external CTS data store. This feature also allows any OpenAM instance in the issuing cluster to validate an OIDC tokens without cross-talk.

To Configure Stateless OpenID Connect 1.0 Access and Refresh

1.   Open the OpenAM console.

2.   Under Realms, select the realm that you are working with.

3.   Click Services, and then select OAuth2 Provider.

4.   Enable Use Stateless Access & Refresh Tokens.

5.   Enable Issue Refresh Tokens.

6.   Enable Issue Refresh Tokens on Refreshing Access Tokens.

7.   Generate some OIDC tokens using the REST API. Notice how each token is larger than a non-stateless example:

```
$ curl --request POST --user "MyClient:password" \
--data "grant_type=password&username=demo&password=changeit&scope=cn%20openid%20profile"\
http://openam.example.com:8080/openam/oauth2/access_token
{
   "scope":"cn openid profile",
   "expires_in":5998,
   "token_type":"Bearer",
   "refresh_token":"eyAidHlwIjogIkpXVCIsICJhbGciOiAiSFMyNTYiIH0.eyAidG9rZW5OYW1l
     IjogInJlZnJlc2hfdG9rZW4iLCAic3ViIjogImRlbW8iLCAic2NvcGUiOiBbICJjbiIsICJvcGV
     uaWQiLCAicHJvZmlsZSIgXSwgImF1dGhHcmFudElkIjogIjU2Y2VhYzM2LTZjNTItNGQ2NS05MT
     hiLTY4ZmY3MThiOTAzMyIsICJuYmYiOiAxNDY1NDE4OTc5LCAiaXNzIjogImh0dHA6Ly9vcGVuY
     W0uZXhhbXBsZS5jb206ODA4MC9vcGVuYW0vb2F1dGgyIiwgImV4cGlyZXNfaW4iOiA2MDAwMDAw
     LCAiaWF0IjogMTQ2NTQxODk3OSwgImV4cCI6IDE0NjU0MjQ5NzksICJhdWRpdFRyYWNraW5nSWQ
     iOiAiZGU4NjM4ZDUtMzhjNC00N2E1LWE5ODMtZDBjNDMzMTQyYTRhIiwgInJlYWxtIjogIi8iLC
     AiYXVkIjogIk15Q2xpZW50IiwgImp0aSI6ICJlNjY0YjgwZS03ZmY0LTRjMGEtOGVlZC01ZTViM
     2QwNGU4YWEiLCAidG9rZW5fdHlwZSI6ICJCZWFyZXIiIH0.VhXDFhI7K7BhouirMNgWQbeQvtrJ
     9IZg4MUH4bAOO3M",
   "id_token":"eyAidHlwIjogIkpXVCIsICJhbGciOiAiUlMyNTYiLCAia2lkIjogIlN5bExDNk5qd
     DFLR1FrdEQ5TXQrMHpjZVFTVT0iIH0.eyAidG9rZW5OYW1lIjogImlkX3Rva2VuIiwgImF6cCI6
     ICJNeUNsaWVudCIsICJzdWIiOiAiZGVtbyIsICJhdF9oYXNoIjogIkNIb0VDUzF1V3VRUS1RM1F
     rMUdMdnciLCAiaXNzIjogImh0dHA6Ly9vcGVuYW0uZXhhbXBsZS5jb206ODA4MC9vcGVuYW0vb2
     F1dGgyIiwgIm9yZy5mb3JnZXJvY2sub3BlbmlkY29ubmVjdC5vcHMiOiAiNzE5MzVjNDUtOTk4Z
     S00NzBjLWFjMDQtMGMzNTM0NGRmYzNmIiwgImlhdCI6IDE0NjU0MTg5NzksICJhdXRoX3RpbWUi
     OiAxNDY1NDE4OTc5LCAiZXhwIjogMTQ2NTQyNDk3OSwgInRva2VuVHlwZSI6ICJKV1RUb2tlbiI
     sICJyZWFsbSI6ICIvIiwgIm5hbWUiOiAiZGVtbyIsICJhdWQiOiAiTXlDbGllbnQiLCAiZmFtaW
     x5X25hbWUiOiAiZGVtbyIgfQ.RpWyfifklukI_YmNASbexM-tLUw4-RGlDouo8vAe5BTQbYdjAC
     HPDfngq0iFFVUVnJHhCIlJeo7GBn459lNR7boefgkaglTz2Q9wYo7TGX-B7ioV0qMnkYsZniTvx
     X2qQc5le_BJnp_2BJOfzzK83WnW93d9A4JGEAKCrfojrXI",
   "access_token":"eyAidHlwIjogIkpXVCIsICJhbGciOiAiSFMyNTYiIH0.eyAidG9rZW5OYW1lI
     jogImFjY2Vzc190b2tlbiIsICJzdWIiOiAiZGVtbyIsICJzY29wZSI6IFsgImNuIiwgIm9wZW5p
     ZCIsICJwcm9maWxlIiBdLCAiYXV0aEdyYW50SWQiOiAiNTZjZWFjMzYtNmM1Mi00ZDY1LTkxOGI
     tNjhmZjcxOGI5MDMzIiwgIm5iZiI6IDE0NjU0MTg5NzksICJpc3MiOiAiaHR0cDovL29wZW5hbS
     5leGFtcGxlLmNvbTo4MDgwL29wZW5hbS9vYXV0aDIiLCAiZXhwaXJlc19pbiI6IDYwMDAwMDAsI
     CJpYXQiOiAxNDY1NDE4OTc5LCAiZXhwIjogMTQ2NTQyNDk3OSwgImF1ZGl0VHJhY2tpbmdJZCI6
     ICI2ZTI2MzA4ZC05YzY2LTRkNjQtODE2Zi1iZTdmYTcyMDc2MTgiLCAicmVhbG0iOiAiLyIsICJ
     hdWQiOiAiTXlDbGllbnQiLCAianRpIjogImY4MDEwZjE2LWZiYTQtNDg1ZS04NGM1LWM2OGU2Mj
     k2ZjIxYyIsICJ0b2tlbl90eXBlIjogIkJlYXJlciIgfQ.JOAG50dLwfB6lKQr4fdKB1zRdKZyfY
     5bRRof61knJDs"
}
``` 
8.   Decode the stateless access token to view its contents:

```
$ curl http://openam.example.com:8080/openam/oauth2/tokeninfo?access_token=eyAid...1knJDs
{
     "tokenName":"access_token",
     "sub":"demo",
     "scope":["cn","openid","profile"],
     "iss":"http://openam.example.com:8080/openam/oauth2",
     "nbf":1465418979,
     "authGrantId":"56ceac36-6c52-4d65-918b-68ff718b9033",
     "expires_in":6000000,
     "iat":1465418979,
     "exp":1465424979,
     "auditTrackingId":"6e26308d-9c66-4d64-816f-be7fa7207618",
     "cn":"demo",
     "realm":"/",
     "aud":"MyClient",
     "openid":"",
     "jti":"f8010f16-fba4-485e-84c5-c68e6296f21c",
     "token_type":"Bearer",
     "access_token":"eyAid...1knJDss",
     "profile":""
 }
``` 

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openid-connect-security-considerations)Security Considerations
---------------------------------------------------------------------------------------------------------------------------------------------

OpenAM provides security mechanisms to ensure that OpenID Connect 1.0 ID tokens are properly protected against malicious attackers: TLS, digital signatures, and token encryption.

While designing a security mechanism, you can also take into account the points developed in the section on [Security Considerations](http://openid.net/specs/openid-connect-core-1_0.html#Security) in the OpenID Connect Core 1.0 incorporating errata set 1 specification.

All OpenID Connect 1.0 require the protection of network messages with Transport Layer Security (TLS). For information about protecting traffic the web container in which OpenAM runs, see ["Managing Certificates and Keystores"](https://doc.openidentityplatform.org/openam/admin-guide/chap-certs-keystores#chap-certs-keystores).

OpenAM supports digital signatures for OAuth 2.0 and OpenID Connect 1.0 tokens. To configure the signatures, see ["Configuring Digital Signatures"](https://doc.openidentityplatform.org/openam/admin-guide/chap-oauth2#oauth2-oidc-digital-signatures).

[](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#encrypting-oidc-idtokens)Encrypting OpenID Connect ID Tokens
-------------------------------------------------------------------------------------------------------------------------------------------

OpenAM supports the ability to encrypt OpenID Connect 1.0 ID tokens, which are JSON Web Tokens (JWT). OpenAM uses RSAES-PKCS1-v1_5, which is an encryption and decryption scheme in version 1.5 of PKCS #1, as the encryption algorithm for the ID token.

The supported encryption methods are A256CBC-HS512, which specifies the AES_256_CBC_HMAC_SHA_512 authenticated encryption algorithm (512-bit key), and A128CBC-HS256, which specifies the AES_128_CBC_HMAC_SHA_256 authenticated encryption algorithm (256-bit key).

To Configure OpenID Connect ID Token Encryption

1.   Start the OpenAM console, and select the realm that you are working with.

2.   Click Dashboard > Configure OAuth Provider > Configure OpenID Connect, and then click Create.

3.   Click Agents > OAuth 2.0/OpenID Connect Client.

4.   Under Agent, click New, configure the Name and Password fields for the agent, and then click Create.

5.   On the OAuth 2.0/OpenID Connect Client page, click the agent you just created, and add the `openid` scope.

6.   Select the Enabled checkbox for Enable ID Token Encryption.

7.   Run Java code to generate an encoded public client encryption key. An example snippet is presented below:

```
KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
keyPairGenerator.initialize(1024);
StringWriter writer = new StringWriter();
PEMWriter pemWriter = new PEMWriter(writer);
pemWriter.writeObject(keyPairGenerator.generateKeyPair().getPublic());
pemWriter.flush();
return writer.toString();
```

java 
8.   Copy and paste the encoded public client key generated in the previous step into the Client ID Token Public Encryption Key field. This encoded public key will be used for encrypting ID tokens.

9.   Run through the authorization OpenID Connect code flow to generate the encrypted ID token. For more information, see ["OpenID Connect Authorization Code Flow"](https://doc.openidentityplatform.org/openam/admin-guide/chap-openid-connect#openam-openid-basic-client-profile).
