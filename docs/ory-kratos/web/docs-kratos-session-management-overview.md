# Source: https://www.ory.com/docs/kratos/session-management/overview

Title: Overview of sessions, Ory Session Cookies, and Ory Session Tokens | Ory

URL Source: https://www.ory.com/docs/kratos/session-management/overview

Markdown Content:
Overview of sessions, Ory Session Cookies, and Ory Session Tokens | Ory

[Skip to main content](https://www.ory.com/docs/kratos/session-management/overview#__docusaurus_skipToContent_fallback)

[![Image 1: Ory](https://www.ory.com/docs/img/logos/logo-light-mode.svg)](https://www.ory.com/)[Start](https://www.ory.com/docs/getting-started/overview)

[Products](https://www.ory.com/docs/kratos/session-management/overview#)
*   [Ory Kratos Identities](https://www.ory.com/docs/identities)
*   [Ory Hydra OAuth2](https://www.ory.com/docs/oauth2-oidc)
*   [Ory Keto Permissions](https://www.ory.com/docs/keto)
*   [Ory Polis SAML](https://www.ory.com/docs/polis)
*   [Ory Oathkeeper Zero Trust](https://www.ory.com/docs/oathkeeper)
*   [Ory Enterprise License](https://www.ory.com/docs/self-hosted/oel)
*   [Ory Elements](https://www.ory.com/docs/elements)

[Manage](https://www.ory.com/docs/kratos/session-management/overview#)
*   [Platform](https://www.ory.com/docs/guides/operations)
*   [Troubleshooting](https://www.ory.com/docs/category/troubleshooting)
*   [Security and compliance](https://www.ory.com/docs/security-compliance/compliance-and-certifications)

[Reference](https://www.ory.com/docs/kratos/session-management/overview#)
*   [REST API](https://www.ory.com/docs/reference/api)
*   [Ory CLI](https://www.ory.com/docs/category/ory-cli-reference)
*   [Ory SDKs](https://www.ory.com/docs/sdk)
*   [Operations](https://www.ory.com/docs/category/operations-reference)

[Open Source](https://www.ory.com/docs/ecosystem/projects)

[Need Support?](https://www.ory.com/docs/kratos/session-management/overview#)
*   [Enterprise Support](https://www.ory.com/support)
*   [Search the docs](https://www.ory.com/docs/search)
*   [Ory Community Slack](https://slack.ory.com/)
*   [GitHub Discussions](https://github.com/orgs/ory/discussions)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/ory)
*   [Schedule a discovery call](https://www.ory.com/contact)

[GitHub](https://github.com/ory)

Search

*   [Go to Start Page](https://www.ory.com/docs/welcome)
*   [Introduction](https://www.ory.com/docs/identities)
*   [Get Started](https://www.ory.com/docs/identities/get-started) 
*   [Concepts](https://www.ory.com/docs/category/concepts) 
    *   [Cookie-based security](https://www.ory.com/docs/security-model)
    *   [Browser vs. native apps](https://www.ory.com/docs/identities/native-browser)
    *   [Browser redirects and flow completion](https://www.ory.com/docs/concepts/redirects)
    *   [Ory Actions](https://www.ory.com/docs/kratos/hooks/configure-hooks)

*   [Guides](https://www.ory.com/docs/category/guides) 
    *   [Authentication](https://www.ory.com/docs/guides/authentication) 
    *   [OpenID Connect SSO](https://www.ory.com/docs/guides/oauth2-oidc) 
    *   [Flows](https://www.ory.com/docs/kratos/self-service) 
    *   [Session](https://www.ory.com/docs/kratos/session-management/overview) 
        *   [Session management](https://www.ory.com/docs/kratos/session-management/list-revoke-get-sessions)
        *   [Check login session](https://www.ory.com/docs/identities/sign-in/check-session-token-cookie-api)
        *   [Session lifespan](https://www.ory.com/docs/kratos/session-management/session-lifespan)
        *   [Refresh sessions](https://www.ory.com/docs/kratos/session-management/refresh-extend-sessions)
        *   [Revoke sessions](https://www.ory.com/docs/kratos/session-management/revoke-sessions-hook)
        *   [Session to JWT](https://www.ory.com/docs/identities/session-to-jwt-cors)
        *   [Edge Sessions](https://www.ory.com/docs/concepts/cache)

    *   [Multi-factor authentication](https://www.ory.com/docs/kratos/mfa/overview) 
    *   [Emails and SMS](https://www.ory.com/docs/guides/email-sms) 
    *   [Ory Actions](https://www.ory.com/docs/guides/integrate-with-ory-cloud-through-webhooks) 
    *   [Search](https://www.ory.com/docs/kratos/session-management/overview#) 
    *   [Identity management](https://www.ory.com/docs/kratos/manage-identities/overview) 
    *   [Identity schema](https://www.ory.com/docs/kratos/manage-identities/identity-schema) 
    *   [User interface](https://www.ory.com/docs/kratos/bring-your-own-ui/custom-ui-overview) 

*   [Configuration](https://www.ory.com/docs/kratos/session-management/overview) 
    *   [Two-step registration](https://www.ory.com/docs/identities/sign-in/two-step-registration)
    *   [Identifier first authentication](https://www.ory.com/docs/identities/sign-in/identifier-first-authentication)
    *   [Login hints](https://www.ory.com/docs/identities/sign-in/login-hint)
    *   [Login and registration actions](https://www.ory.com/docs/identities/sign-in/actions)
    *   [Code submissions limit](https://www.ory.com/docs/identities/sign-in/code-submission-limit)

*   [Self-Hosted](https://www.ory.com/docs/kratos/quickstart) 
    *   [Installation](https://www.ory.com/docs/kratos/install)
    *   [Quickstart](https://www.ory.com/docs/kratos/quickstart)
    *   [Configuration](https://www.ory.com/docs/kratos/session-management/overview#) 
    *   [Guides](https://www.ory.com/docs/kratos/session-management/overview#) 
    *   [Reference](https://www.ory.com/docs/kratos/session-management/overview#) 

*   [Guides](https://www.ory.com/docs/category/guides)
*   Session

On this page

Overview
========

When a user authenticates, for example by signing in with their username and password, they receive a session. The session is proof that the user is authenticated and allows to interact with the system without the need to re-authenticate for every request.

Sessions can be issued in two formats:

*   **Ory Session Cookie** - when the system detects that the interaction is performed through a web browser, a cookie which represents the user's session is stored in the browser.
*   **Ory Session Token** - when the system detects that the interaction is performed by a client other than a web browser, for example a native mobile app, a session token is issued to the client.

You can also convert an Ory Session to a JWT, read more about this approach [here](https://www.ory.com/docs/kratos/session-management/overview#json-web-token-jwt-support).

note

For security reasons, you can't break the isolation between cookies and session tokens.

Ory session[​](https://www.ory.com/docs/kratos/session-management/overview#ory-session "Direct link to Ory session")
--------------------------------------------------------------------------------------------------------------------

This is a sample session:

`{  "active": true,  "authenticated_at": "2019-08-24T14:15:22Z",  "authentication_methods": [    {      "aal": "aal1",      "completed_at": "2019-08-24T14:15:22Z",      "method": "password"    }  ],  "authenticator_assurance_level": "aal1",  "devices": [    {      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",      "ip_address": "string",      "location": "string",      "user_agent": "string"    }  ],  "expires_at": "2019-08-24T14:15:22Z",  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",  "identity": {    "created_at": "2019-08-24T14:15:22Z",    "credentials": {      "property1": {        "config": {},        "created_at": "2019-08-24T14:15:22Z",        "identifiers": ["string"],        "type": "password",        "updated_at": "2019-08-24T14:15:22Z",        "version": 0      },      "property2": {        "config": {},        "created_at": "2019-08-24T14:15:22Z",        "identifiers": ["string"],        "type": "password",        "updated_at": "2019-08-24T14:15:22Z",        "version": 0      }    },    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",    "metadata_admin": {},    "metadata_public": {},    "recovery_addresses": [      {        "created_at": "2019-08-24T14:15:22Z",        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",        "updated_at": "2019-08-24T14:15:22Z",        "value": "string",        "via": "string"      }    ],    "schema_id": "string",    "schema_url": "string",    "state": "active",    "state_changed_at": "2019-08-24T14:15:22Z",    "traits": null,    "updated_at": "2019-08-24T14:15:22Z",    "verifiable_addresses": [      {        "created_at": "2014-01-01T23:28:56.782Z",        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",        "status": "string",        "updated_at": "2014-01-01T23:28:56.782Z",        "value": "string",        "verified": true,        "verified_at": "2019-08-24T14:15:22Z",        "via": "string"      }    ]  },  "issued_at": "2019-08-24T14:15:22Z"}`

| Property | Description |
| --- | --- |
| `active` | When set to `true`, the Ory Session is active and can be used to authenticate requests. |
| `expires_at` | Defines the time when the Session expires. This value depends on the session lifespan configuration. |
| `authenticated_at` | Indicates the time of the most recent successful authentication. This value is updated when: * The end-user authenticates with a second factor such as TOTP * The end-user refreshes their session using the [`/self-service/login/browser`](https://www.ory.com/docs/reference/api#operation/initializeSelfServiceLoginFlowForBrowsers) endpoint or [`/self-service/login/api`](https://www.ory.com/docs/reference/api#operation/initializeSelfServiceLoginFlowWithoutBrowser) endpoint and setting `refresh` to `true` |

### Using Ory Session Cookie[​](https://www.ory.com/docs/kratos/session-management/overview#using-ory-session-cookie "Direct link to Using Ory Session Cookie")

An Ory Session Cookie is issued when the user signs in through the browser-based login flow. To get the session payload, send a request to the `/sessions/whoami` endpoint.

note

Browser-based applications including single-page applications (SPAs) and server-side rendered apps should use session cookies instead of session tokens.

*   React
*   cURL

Checking current session

`import { Configuration, FrontendApi, Session } from "@ory/client"import { useEffect, useState } from "react"const frontend = new FrontendApi(  new Configuration({    basePath: "http://localhost:4000", // Use your local Ory Tunnel URL    baseOptions: {      withCredentials: true,    },  }),)export function checkSession() {  const [session, setSession] = useState<Session>(undefined)  useEffect(() => {    frontend      // the cookie is automatically sent with the request      .toSession()      .then(({ data: session }) => {        setSession(session)      })      .catch((error) => {        // The session could not be fetched        // This might occur if the current session has expired      })  }, [])  return session ? (    <table>      <tr>        <th>Session ID</th>        <th>Expires at</th>        <th>Authenticated at</th>      </tr>      <tr id={session.id}>        <td>{session.id}</td>        <td>{session.expires_at || ""}</td>        <td>{session.authenticated_at || ""}</td>      </tr>    </table>  ) : (    <div>Loading session data...</div>  )}`

`curl 'https://$PROJECT_SLUG.projects.oryapis.com/sessions/whoami' \-H 'Accept: application/json' \-H 'Cookie: ory_kratos_session=MTYzNDIyNzEzN3xEdi1CQkFFQ180SUFBUkFCRUFBQVJfLUNBQUVHYzNSeWFXNW5EQThBRFhObGMzTnBiMjVmZEc5clpXNEdjM1J5YVc1bkRDSUFJRTFDYWtvME5VNVlaVWxvYVZWeWJrUnZhSEF4YmxSV2VVRlhNMWwxVlVGenxXpsk2cL21Dclk3nCoXV41N6bFxvVJSt7CeICy_815Aw=='`

### Using Ory Session Token[​](https://www.ory.com/docs/kratos/session-management/overview#using-ory-session-token "Direct link to Using Ory Session Token")

An Ory Session Token is issued when the user authenticates through a client other than a web browser. To get the session payload, send a request to the `/sessions/whoami` endpoint.

note

Native applications such as desktop applications, mobile applications, or terminal-based apps that do not run inside a browser should use session tokens instead of session cookies.

*   Go
*   TypeScript
*   cURL

Checking current session

`package frontendimport (	"context"	"fmt"	"os"	"github.com/ory/client-go")type oryMiddleware struct {	ory *ory.APIClient}func init() {	cfg := client.NewConfiguration()	cfg.Servers = client.ServerConfigurations{		{URL: fmt.Sprintf("https://%s.projects.oryapis.com", os.Getenv("ORY_PROJECT_SLUG"))},	}	ory = client.NewAPIClient(cfg)}func CheckSession(ctx context.Context, sessionToken string) (session *client.Session, err error) {	session, _, err = ory.FrontendApi.ToSession(ctx).		XSessionToken(sessionToken).		Execute()	if err != nil {		// error revoking the session, for example due to expired token provided		return nil, err	}	return session, nil}`

Checking current session (Typescript SDK)

`import { Configuration, FrontendApi } from "@ory/client"const frontend = new FrontendApi(  new Configuration({    basePath: `https://${process.env.ORY_PROJECT_SLUG}.projects.oryapis.com`,  }),)export async function checkSession(sessionId: string, token: string) {  return await frontend.toSession({    xSessionToken: token,  })}`

`curl 'https://$PROJECT_SLUG.projects.oryapis.com/sessions/whoami' \ -H 'Accept: application/json' \ -H 'Authorization: Bearer BRFbGMzTnBiMjVmZEcEdjM1J5YVc1bkRDSUFvME5VNVlaVeWJrUnZhSEF4YmxSV2VVRlhNMWwxVlVGenxXpsk2cLXV41N6bFxvVJSt7CeICy'`

JSON Web Token (JWT) support[​](https://www.ory.com/docs/kratos/session-management/overview#json-web-token-jwt-support "Direct link to JSON Web Token (JWT) support")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sessions are by default not issued as JWTs for two main reasons:

1.   Sessions can end at any point in time, indicating that the user is no longer signed in. With JWTs, it's difficult to determine if a session is still valid before the token expires.
2.   Sessions can be updated and changed at any point in time, for example, when the user updates their profile. Such change can't be easily reflected in a JWT before it is refreshed.

Ory Network employs a session caching mechanism to reduce the latency for `toSession` / `/sessions/whoami` endpoint calls across the globe so that latency is not an issue for users. [Read more about session caching.](https://www.ory.com/docs/concepts/cache)

If you don't want to make repeated calls to `toSession` / `/sessions/whoami`, or you need to use JWTs in your setup, you have several options:

*   **Recommended**: Use [Session to JWT](https://www.ory.com/docs/identities/session-to-jwt-cors). Read more in the [Session to JWT](https://www.ory.com/docs/identities/session-to-jwt-cors) documentation.
*   Alternative: Convert sessions to JWTs on your entry point. You then have the option to add caching to further reduce the number of API calls made. More information on this approach is available in the [section below](https://www.ory.com/docs/kratos/session-management/overview#use-ory-oathkeeper-to-convert-sessions-to-jwts).

### Use Ory Oathkeeper to convert sessions to JWTs[​](https://www.ory.com/docs/kratos/session-management/overview#use-ory-oathkeeper-to-convert-sessions-to-jwts "Direct link to Use Ory Oathkeeper to convert sessions to JWTs")

[Ory Oathkeeper](https://www.ory.com/oathkeeper) is an API Gateway capable of converting sessions to JWTs.

[Edit this page](https://github.com/ory/docs/edit/master/docs/kratos/session-management/01_overview.mdx)

Last updated on **Oct 15, 2025** by **unatasha8**

[Previous User-facing errors](https://www.ory.com/docs/kratos/self-service/flows/user-facing-errors)[Next Session management](https://www.ory.com/docs/kratos/session-management/list-revoke-get-sessions)

*   [Ory session](https://www.ory.com/docs/kratos/session-management/overview#ory-session)
    *   [Using Ory Session Cookie](https://www.ory.com/docs/kratos/session-management/overview#using-ory-session-cookie)
    *   [Using Ory Session Token](https://www.ory.com/docs/kratos/session-management/overview#using-ory-session-token)

*   [JSON Web Token (JWT) support](https://www.ory.com/docs/kratos/session-management/overview#json-web-token-jwt-support)
    *   [Use Ory Oathkeeper to convert sessions to JWTs](https://www.ory.com/docs/kratos/session-management/overview#use-ory-oathkeeper-to-convert-sessions-to-jwts)

### Ory Network

The best way to manage identities, authentication, authorization, and access control—designed for speed, security, and compliance.

[Sign up for a free account](https://console.ory.sh/?mtm_campaign=Docs-SideCta&mtm_kwd=variant-0)

[Need Support?](https://www.ory.com/support)·[Search](https://www.ory.com/docs/search)·[Status](https://status.ory.com/)·[Privacy](https://www.ory.com/legal/privacy)·[Company](https://www.ory.com/legal/company)·[Terms of Service](https://www.ory.com/legal/tos)·[Schedule a discovery call](https://www.ory.com/contact)·Consent Preferences

[![Image 2: Ory logo in white](https://www.ory.com/docs/img/logos/logo-dark-mode.svg)](https://www.ory.com/)

Copyright © 2026 Ory Corp

![Image 3: Project Logo](https://www.ory.com/docs/img/kapa-logo.png)

Ask AI

![Image 4](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=bc9b501f-7f2b-49d7-8bc8-e26c4ac412ff&bo=1&sid=dbc7ed601d3e11f1ba3cdf8182e28acb&vid=dbc7d9401d3e11f19b75cb228939d326&vids=1&msclkid=N&gtm_tag_source=1&pi=918639831&lg=en-US&sw=800&sh=600&sc=24&tl=Overview%20of%20sessions,%20Ory%20Session%20Cookies,%20and%20Ory%20Session%20Tokens%20%7C%20Ory&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fkratos%2Fsession-management%2Foverview&r=&lt=736&evt=pageLoad&sv=2&cdb=AQAS&rn=910258)![Image 5](https://bat.bing.com/action/0?ti=97226771&tm=gtm002&Ver=2&mid=bc9b501f-7f2b-49d7-8bc8-e26c4ac412ff&bo=2&sid=dbc7ed601d3e11f1ba3cdf8182e28acb&vid=dbc7d9401d3e11f19b75cb228939d326&vids=0&msclkid=N&tpp=1&ea=Page%20View%20-%20All%20Pages%20(excluding%20console)&en=Y&p=https%3A%2F%2Fwww.ory.com%2Fdocs%2Fkratos%2Fsession-management%2Foverview&sw=800&sh=600&sc=24&evt=custom&cdb=AQAS&rn=701218)
