# Source: https://www.ory.com/docs/kratos/self-service

Title: Self-service flows | Ory

URL Source: https://www.ory.com/docs/kratos/self-service

Markdown Content:
Ory Identities implements flows that users perform themselves as opposed to administrative intervention. Facebook and Google both provide self-service registration and profile management features as you are able to make changes to your profile and sign up yourself.

Most believe that user management systems are easy to implement because picking the right password hashing algorithm and sending an account verification code is a solvable challenge. The real complexity however hides in the details and attack vectors of self-service flows. Most data leaks happen because someone is able to exploit

*   registration: with attack vectors such as account enumeration, ...;
*   login: phishing, account enumeration, leaked password databases, brute-force, ...;
*   user settings: account enumeration, account takeover, ...;
*   account recovery: social engineering attacks, account takeover, spoofing, and so on.

There are also many other areas you need to think about, such as:

*   Mobile, Smart TV, ... authentication
*   Linking and unlinking social profiles (for example "Sign in with Google" or "Connect with Google") to existing accounts

Ory Identities applies best practices established by experts (National Institute of Sciences NIST, Internet Engineering Task Force IETF, Microsoft Research, Google Research, Troy Hunt, ...) and implements the following flows:

*   [Registration](https://www.ory.com/docs/kratos/self-service/flows/user-registration)
*   [Login](https://www.ory.com/docs/kratos/self-service/flows/user-login)
*   [Logout](https://www.ory.com/docs/kratos/self-service/flows/user-logout)
*   [User Settings](https://www.ory.com/docs/kratos/self-service/flows/user-settings)
*   [Account Recovery](https://www.ory.com/docs/kratos/self-service/flows/account-recovery-password-reset)
*   [Address Verification](https://www.ory.com/docs/kratos/self-service/flows/verify-email-account-activation)
*   [User-Facing Error](https://www.ory.com/docs/kratos/self-service/flows/user-facing-errors)
*   2FA / MFA

Some flows break down into "flow methods" which implement some of the flow's business logic:

*   The `password` method implements the login and registration with "email or/and username and password" method, and "change your password" user settings method.
*   The `oidc` (OpenID Connect, OAuth2, Social Sign In) method implements "Sign in with ..." login and registration method and "un/link another social account" user settings method.
*   The `profile` method implements the "update your profile", "change your first/last name, ..." user settings method).
*   The `code` method implements a one-time-password sent to the user via their recovery addresses (Email, SMS, etc.)
*   The `link` method implements the "click this link to reset your password" account recovery method.

Some flows implement the ability [to run hooks](https://www.ory.com/docs/kratos/hooks/configure-hooks) which allow users to be immediately signed in after registration, notify another system on successful registration (such as Mailchimp), and so on.

Performing login, registration, settings, ... flows[​](https://www.ory.com/docs/kratos/self-service#performing-login-registration-settings--flows "Direct link to Performing login, registration, settings, ... flows")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two flow types supported in Ory Identities:

*   Flows where the user sits in front of the Browser and the application is
    *   a server-side application (Node.js, Java, ...)
    *   a client-side application (React.js, Angular, ...)

*   Flows where API interaction is required (mobile app, Smart TV, ...)

All Self-Service Flows ([User Login](https://www.ory.com/docs/kratos/self-service/flows/user-login), [User Registration](https://www.ory.com/docs/kratos/self-service/flows/user-registration), [Profile Management](https://www.ory.com/docs/kratos/self-service/flows/user-settings), [Account Recovery](https://www.ory.com/docs/kratos/self-service/flows/account-recovery-password-reset), [Email or Phone verification](https://www.ory.com/docs/kratos/self-service/flows/verify-email-account-activation)) support these two flow types and use the same data models but do use different API endpoints.

##### DANGER

Never use API flows to implement Browser applications! Using API flows in Single-Page-Apps as well as server-side apps opens up several potential attack vectors, including Login and other CSRF attacks.

Browser flows for server-side apps: Node.js, PHP, Java, ...[​](https://www.ory.com/docs/kratos/self-service#browser-flows-for-server-side-apps-nodejs-php-java- "Direct link to Browser flows for server-side apps: Node.js, PHP, Java, ...")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Browser-based flows for server-side apps make use of three core HTTP technologies:

*   HTTP Redirects
*   HTTP POST (`application/x-www-urlencoded`) and REST GET requests.
*   HTTP Cookies to prevent CSRF and Session Hijacking attack vectors.

Ory Identities takes care of all required session and CSRF cookies and ensures that all security requirements are fulfilled.

The browser flow has three stages:

*   Initialization and redirect to UI;
*   Form rendering;
*   Form submission and payload validation.

note

All examples use the "Playground" project in Ory Network. Please be aware that everyone can see the data you enter there. You can replace the URL with a locally hosted Ory Identities as well.

The _Authentication UI_ (**your application!**) is responsible for rendering the actual Login and Registration HTML Forms. You can of course implement one app for rendering all the Login, Registration, ... screens, and another app (think "Service Oriented Architecture", "Micro-Services" or "Service Mesh") is responsible for rendering your Dashboards, Management Screens, and so on.

### Initialization and redirect to UI[​](https://www.ory.com/docs/kratos/self-service#initialization-and-redirect-to-ui "Direct link to Initialization and redirect to UI")

First, the Browser opens the flow's initialization endpoint (for example`/self-service/login/browser`, `/self-service/registration/browser`, ...):

`curl -s -i -X GET \    -H "Accept: text/html" \    https://playground.projects.oryapis.com/self-service/login/browserHTTP/2 303date: Fri, 09 Jul 2021 10:23:52 GMTcontent-type: text/html; charset=utf-8content-length: 121location: https://playground.projects.oryapis.com/hosted/login?flow=3fc63726-8461-43f4-974a-5579ff4174f1cache-control: private, no-cache, no-store, must-revalidateset-cookie: aHR0cHM6Ly9wbGF5Z3JvdW5kLnByb2plY3RzLm9yeWFwaXMuY29tL2FwaS9rcmF0b3MvcHVibGlj_csrf_token=Lk9swSOlimGS9LI5HslOyEKGL4hMQzWHnwnQpm9HGAA=; Path=/api/kratos/public; Domain=playground.projects.oryapis.com; Max-Age=31536000; HttpOnly; Secure; SameSite=Nonevary: Originvary: Cookiestrict-transport-security: max-age=15724800; includeSubDomains<a href="https://playground.projects.oryapis.com/hosted/login?flow=3fc63726-8461-43f4-974a-5579ff4174f1">See Other</a>.`

The initialization endpoint creates a flow object and stores it in the database. The flow object has an ID and contains additional information about the flow such as the login methods (for example "username/password" and "Sign in with Google") and their form data.

##### INFO

Ory and your UI must be hosted on the same top level domain. You can't host Ory and your UI on separate top level domains:

*   `ory.bar.com` and `app.bar.com` will work;
*   `ory.bar.com` and `bar.com` will work;
*   `ory.bar.com` and `not-bar.com` will not work.

Once stored, the Browser is HTTP 303 redirected to the flow's configured UI URL (for example `selfservice.flows.login.ui_url`), appending the flow ID as the `flow` URL Query Parameter. Also included are HTTP cookies such as Anti-CSRF cookies.

### Form rendering[​](https://www.ory.com/docs/kratos/self-service#form-rendering "Direct link to Form rendering")

The Browser follows the link and opens

`https://playground.projects.oryapis.com/hosted/login?flow=36c3246f-8e40-4f45-8721-c246576a8bc3`

which renders the HTML form which for example shows the "username and password" field, the "Update your email address" field, or other flow forms. This HTML form is rendered by the self-service UI, which you fully control.

The endpoint responsible for the UI URL uses the `flow` URL Query Parameter (here `...?flow=36c3246f-8e40-4f45-8721-c246576a8bc3`) to call the flow information endpoint, for example: `https://playground.projects.oryapis.com/self-service/login/flows?id=36c3246f-8e40-4f45-8721-c246576a8bc3`

note

Calling the flow endpoint without the correct CSRF cookies will result in a failure!

The endpoint returns the flow data - so for example the login form and any validation errors. Let's take a look at an example using CURL:

`# A cookie jar for storing the CSRF tokenscookieJar=$(mktemp)flowId=$(curl -s -X GET \    --cookie-jar $cookieJar --cookie $cookieJar \    -H "Accept: application/json" \    https://playground.projects.oryapis.com/self-service/login/browser | jq -r '.id')# The endpoint uses Ory Identities' REST API to fetch information about the requestcurl -s -X GET \    --cookie-jar $cookieJar --cookie $cookieJar \    -H "Accept: application/json" \    "https://playground.projects.oryapis.com/self-service/login/flows?id=$flowId" | jq`

The response includes login methods, their fields, and additional information about the flow:

`{  "id": "33f6079a-ef14-4084-af13-34a91e53cd6c",  "type": "browser",  "expires_at": "2021-07-09T10:08:08.856735Z",  "issued_at": "2021-07-09T09:08:08.856735Z",  "request_url": "http://playground.projects.oryapis.com/self-service/login/browser",  "ui": {    "action": "https://playground.projects.oryapis.com/self-service/login?flow=33f6079a-ef14-4084-af13-34a91e53cd6c",    "method": "POST",    "nodes": [      {        "type": "input",        "group": "default",        "attributes": {          "name": "csrf_token",          "type": "hidden",          "value": "XmG3qwTYSV0oWIyNGTugvtNOKMxWPYHd7dNX7BYK5lL79P0iUdq5jVmRUKwwm8RLcAGN7eF7iYraAiTSOdamuQ==",          "required": true,          "disabled": false        },        "messages": [],        "meta": {}      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "identifier",          "type": "text",          "value": "",          "required": true,          "disabled": false        },        "messages": [],        "meta": {          "label": {            "id": 1070004,            "text": "ID",            "type": "info"          }        }      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "password",          "type": "password",          "required": true,          "disabled": false        },        "messages": [],        "meta": {          "label": {            "id": 1070001,            "text": "Password",            "type": "info"          }        }      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "method",          "type": "submit",          "value": "password",          "disabled": false        },        "messages": [],        "meta": {          "label": {            "id": 1010001,            "text": "Sign in",            "type": "info",            "context": {}          }        }      }    ],    "messages": [      {        "id": 4010002,        "text": "Couldn't find a strategy to log you in with. Did you fill out the form?",        "type": "error"      }    ]  },  "created_at": "2021-07-09T09:08:08.857959Z",  "updated_at": "2021-07-09T09:08:08.857959Z",  "forced": false}`

For more details, check out the individual flow documentation.

The flow UI then renders the given methods. For the example above, a suitable HTML Form would look along the lines of:

`<form action="https://playground.projects.oryapis.com/self-service/login?flow=f6209031-38d5-48bc-b6a5-118e8a24d1fe" method="POST">  <input    name="csrf_token"    type="hidden"    value="XmG3qwTYSV0oWIyNGTugvtNOKMxWPYHd7dNX7BYK5lL79P0iUdq5jVmRUKwwm8RLcAGN7eF7iYraAiTSOdamuQ=="  />  <fieldset>    <label>      <input name="identifier" type="text" value="" placeholder="ID" />      <span>ID</span>    </label>  </fieldset>  <fieldset>    <label>      <input name="password" type="password" value="" placeholder="Password" />      <span>Password</span>    </label>  </fieldset>  <button name="method" type="submit" value="password">Sign in</button></form>`

### Form submission and payload validation[​](https://www.ory.com/docs/kratos/self-service#form-submission-and-payload-validation "Direct link to Form submission and payload validation")

The user completes the flow by submitting the form. The form action always points to Ory Identities directly. The business logic for the flow method will then validate the form payload and return to the UI URL on validation errors. The UI then fetches the information about the flow again

`# The endpoint uses Ory Identities' REST API to fetch information about the requesttheFlowID=...curl -s -i -X GET \    -H "Accept: application/json"  \    'https://playground.projects.oryapis.com/self-service/login/flows?id=$theFlowID' | jq`

which now includes validation errors and other potential messages:

`{  id: "36c3246f-8e40-4f45-8721-c246576a8bc3",  type: "browser",  expires_at: "2021-04-28T09:00:57.10254633Z",  issued_at: "2021-04-28T08:50:57.10254633Z",  request_url: "https://playground.projects.oryapis.com/self-service/login/browser",  ui: {    action: "https://playground.projects.oryapis.com/self-service/login?flow=36c3246f-8e40-4f45-8721-c246576a8bc3",    method: "POST",    nodes: [      // ...      {        type: "input",        group: "password",        attributes: {          name: "identifier",          type: "text",          value: "",          required: true,          disabled: false,        },        messages: [          {            id: 4000001,            text: "length must be >= 1, but got 0",            type: "error",          },        ],        meta: {          label: {            id: 1070004,            text: "ID",            type: "info",          },        },      },      {        type: "input",        group: "password",        attributes: {          name: "password",          type: "password",          required: true,          disabled: false,        },        messages: [          {            id: 4000001,            text: "length must be >= 1, but got 0",            type: "error",          },        ],        meta: {          label: {            id: 1070001,            text: "Password",            type: "info",          },        },      },      // ...    ],  },  forced: false,}`

If a system error (for example broken configuration file) occurs, the browser is redirected to the [Error UI](https://www.ory.com/docs/kratos/self-service/flows/user-facing-errors).

If the form payload is valid, the flow completes with a success. The result here depends on the flow itself - the login flow for example redirects the user to a specified redirect URL and sets a session cookie. The registration flow also redirects to a specified redirect URL but only creates the user in the database and might issue a session cookie if configured to do so.

Browser flows for client-side apps: Single-Page-Apps, React.js, Angular, Next.js, ...[​](https://www.ory.com/docs/kratos/self-service#browser-flows-for-client-side-apps-single-page-apps-reactjs-angular-nextjs- "Direct link to Browser flows for client-side apps: Single-Page-Apps, React.js, Angular, Next.js, ...")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Browser-based flows also support client-side applications such as Single-Page-Apps (React.js, Angular, Next.js, ...) that use AJAX to perform requests.

info

Ory Identities and your UI must be hosted on same top level domain! You can't host Ory Identities and your UI on separate top level domains:

*   `kratos.bar.com` and `ui.bar.com` will work;
*   `kratos.bar.com` and `bar.com` will work;
*   `kratos.bar.com` and `not-bar.com` won't work.

Ory Identities identifies SPA requests by checking if the `Accept` HTTP Header is set to `application/json`.

If it is, these flows act like an API flow and respond with JSON instead of HTTP redirects while still setting and requiring the necessary cookies for CSRF, sessions, and more:

*   Initialization **without redirect** using an AJAX request;
*   Form rendering using HTML;
*   Form submission as `application/json` and payload validation.

The high-level sequence diagram for API flows looks as follows:

%%{init: {'theme':'neutral'}}%% sequenceDiagram participant B as AJAX Client participant K as Ory Kratos B->>K: REST GET /self-service/[login|registration|settings|...]/browser K-->>K: Create and store new login, registration, settings, ... flow K->>B: HTTP 200 OK with flow as application/json payload B-->>B: Render form using HTML input elements B-->>B: User fills out forms, clicks e.g. Log in, Sign Up, Update Email, ... B->>K: REST POST to e.g. /self-service/[login|registration|settings|...]?flow=[flow-id] K-->>K: Validates and processes payload alt Form payload is valid K->>B: Perform flow-specific action (e.g. create user, set session cookie, ...) else Form payload invalid K-->>K: Update and store flow (e.g. add form validation errors) K->>B: Respond with e.g. HTTP 400 Bad Request and updated flow as payload B-->>B: Render form and validation errors using HTML input elements B-->>K: Repeat flow with input data, submit, validate, ... end

### Initialization[​](https://www.ory.com/docs/kratos/self-service#initialization "Direct link to Initialization")

The AJAX client (for example Next.js app) makes a request to the flow's initialization endpoint (for example`/self-service/login/browser`, `/self-service/registration/browser`, ...):

`curl -v -s -X GET \    -H "Accept: application/json"  \    https://playground.projects.oryapis.com/self-service/login/browser | jq> GET /self-service/login/browser HTTP/2> Host: playground.projects.oryapis.com> User-Agent: curl/7.64.1> Accept: application/json< HTTP/2 200< date: Fri, 09 Jul 2021 10:25:12 GMT< content-type: application/json; charset=utf-8< content-length: 1359< cache-control: private, no-cache, no-store, must-revalidate< set-cookie: aHR0cHM6Ly9wbGF5Z3JvdW5kLnByb2plY3RzLm9yeWFwaXMuY29tL2FwaS9rcmF0b3MvcHVibGlj_csrf_token=UlKMcLe00G8B9GjC7D1I5rvQ6P79Q0YpzKb4lo7uLtw=; Path=/api/kratos/public; Domain=playground.projects.oryapis.com; Max-Age=31536000; HttpOnly; Secure; SameSite=None< vary: Origin< vary: Cookie< strict-transport-security: max-age=15724800; includeSubDomains{  "id": "ff0c97c4-a7bb-49a5-a8a6-ebf174877fa5",  "type": "browser",  "expires_at": "2021-07-09T11:25:12.136099226Z",  "issued_at": "2021-07-09T10:25:12.136099226Z",  "request_url": "http://playground.projects.oryapis.com/self-service/login/browser",  "ui": {    "action": "https://playground.projects.oryapis.com/self-service/login?flow=ff0c97c4-a7bb-49a5-a8a6-ebf174877fa5",    "method": "POST",    "nodes": [ /* ... */ ]  },  "created_at": "2021-07-09T10:25:12.137554Z",  "updated_at": "2021-07-09T10:25:12.137554Z",  "forced": false}`

The initialization endpoint creates a flow object and stores it in the database. The flow object has an ID and contains additional information about the flow such as the login methods (for example "username/password" and "Sign in with Google") and their form data.

### Form rendering[​](https://www.ory.com/docs/kratos/self-service#form-rendering-1 "Direct link to Form rendering")

Form rendering works the same way as the flows for server-side browser apps.

### Form submission and payload validation[​](https://www.ory.com/docs/kratos/self-service#form-submission-and-payload-validation-1 "Direct link to Form submission and payload validation")

To submit the form, it's recommended to intercept the submission and send the form as JSON using `fetch` (see ["Submit HTML Forms to JSON APIs"](https://dev.to/amjadmh73/submit-html-forms-to-json-apis-easily-137l)) or the [SDK](https://www.ory.com/docs/sdk).

The response depends on the result (sign up success, account recovery success, form validation error, ...). If a form validation error occurs, the following response could be sent:

`{  id: "f6209031-38d5-48bc-b6a5-118e8a24d1fe",  type: "browser",  expires_at: "2021-04-28T09:00:57.10254633Z",  issued_at: "2021-04-28T08:50:57.10254633Z",  request_url: "https://playground.projects.oryapis.com/self-service/login/browser",  ui: {    action: "https://playground.projects.oryapis.com/self-service/login?flow=f6209031-38d5-48bc-b6a5-118e8a24d1fe",    method: "POST",    nodes: [      // ...      {        type: "input",        group: "password",        attributes: {          name: "identifier",          type: "text",          value: "",          required: true,          disabled: false,        },        messages: [          {            id: 4000001,            text: "length must be >= 1, but got 0",            type: "error",          },        ],        meta: {          label: {            id: 1070004,            text: "ID",            type: "info",          },        },      },      {        type: "input",        group: "password",        attributes: {          name: "password",          type: "password",          required: true,          disabled: false,        },        messages: [          {            id: 4000001,            text: "length must be >= 1, but got 0",            type: "error",          },        ],        meta: {          label: {            id: 1070001,            text: "Password",            type: "info",          },        },      },      // ...    ],  },  forced: false,}`

API flows: Native Mobile & Desktop Apps, Command Line Interfaces, Smart TVs and more[​](https://www.ory.com/docs/kratos/self-service#api-flows-native-mobile--desktop-apps-command-line-interfaces-smart-tvs-and-more "Direct link to API flows: Native Mobile & Desktop Apps, Command Line Interfaces, Smart TVs and more")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

##### DANGER

Never use API flows to implement Browser applications! Using API flows in Single-Page-Apps as well as server-side apps opens up several potential attack vectors, including Login and other CSRF attacks.

API flows have three stages:

*   Initialization without redirect and cookies;
*   Form rendering using for example native iOS, Android, ... components;
*   Form submission as `application/json` and payload validation.

The high-level sequence diagram for API flows looks as follows:

%%{init: {'theme':'neutral'}}%% sequenceDiagram participant B as API Client participant K as Ory Kratos B->>K: REST GET /self-service/[login|registration|settings|...]/api K-->>K: Create and store new login, registration, settings, ... flow K->>B: HTTP 200 OK with flow as application/json payload B-->>B: Render form using e.g. Native iOS UI Elements B-->>B: User fills out forms, clicks e.g. Log in, Sign Up, Update Email, ... B->>K: REST POST to e.g. /self-service/[login|registration|settings|...]?flow=...> K-->>K: Validates and processes payload alt Form payload is valid K->>B: Perform flow-specific action (e.g. create user, set session cookie, ...) else Form payload invalid K-->>K: Update and store flow (e.g. add form validation errors) K->>B: Respond with e.g. HTTP 400 Bad Request and updated flow as payload B-->>B: Render form and validation errors using e.g. Native iOS UI Elements B-->>K: Repeat flow with input data, submit, validate, ... end

### Initialization[​](https://www.ory.com/docs/kratos/self-service#initialization-1 "Direct link to Initialization")

The client (for example mobile application) makes a request to the flow's initialization endpoint (for example`/self-service/login/api`, `/self-service/registration/api`, ...):

`curl -s -X GET \    -H "Accept: application/json"  \    https://playground.projects.oryapis.com/self-service/login/api | jq{  "id": "9d17f37b-b60b-44f5-9812-4829a89810f7",  "type": "api",  "expires_at": "2021-07-09T11:26:04.019418543Z",  "issued_at": "2021-07-09T10:26:04.019418543Z",  "request_url": "http://playground.projects.oryapis.com/self-service/login/api",  "ui": {    "action": "https://playground.projects.oryapis.com/self-service/login?flow=9d17f37b-b60b-44f5-9812-4829a89810f7",    "method": "POST",    "nodes": [ /* ... */ ]  }}`

The initialization endpoint creates a flow object and stores it in the database. The flow object has an ID and contains additional information about the flow such as the login methods and their form data.

### Form rendering[​](https://www.ory.com/docs/kratos/self-service#form-rendering-2 "Direct link to Form rendering")

While the Browser flow redirects the client and uses cookies to protect against CSRF and session hijacking attacks, the API flow answers with a fresh flow formatted as `application/json` right away. The client would then use that information to render the UI. In React Native, this may look like the following snippet:

`import React, { useState, useEffect } from 'react'import { Text, TextInput, View } from 'react-native'import { Configuration, FrontendApi, LoginFlow } from '@ory/client'const kratos = new FrontendApi(  new Configuration({ basePath: 'https://playground.projects.oryapis.com/api/kratos/public' }))export default function Login () {  const [flow, setFlow] = useState<LoginFlow | undefined>(undefined)  useEffect(() => {    kratos.initializeSelfServiceLoginFlowWithoutBrowser().then(({ data: flow }) => {      setFlow(flow)    })  }, [])  if (!flow) {    return null  }  // This is a non-functional, code example. It's missing state management and so on.  // The idea is to show how initializing such a flow would look like in an API scenario.  return (    <View>      <Text>Login</Text>      {flow.ui.nodes.map((node) => {        switch (node.type) {          case 'input':            return <TextInput value={node.attributes.value} /* placeholder, name, ... *//>          default:            // ...        }      })}    </>  )}`

If needed, the client can re-request the flow using the same HTTP Request as the browser flow at the Public API endpoint:

`curl -s -X GET \    -H "Accept: application/json" \    "https://playground.projects.oryapis.com/self-service/login/flows?id=<the-flow-id>" | jq{  "id": "41ebf1e9-79f5-4b97-b643-04bfc405f8ad",  "type": "api",  # ...`

### Form submission and payload validation[​](https://www.ory.com/docs/kratos/self-service#form-submission-and-payload-validation-2 "Direct link to Form submission and payload validation")

The request is then completed by sending the form formatted as `application/json` to the action endpoint

`flow=$(curl -s -X GET -H "Accept: application/json" "https://playground.projects.oryapis.com/self-service/login/api")actionUrl=$(echo $flow | jq -r '.ui.action')echo $actionUrl# https://playground.projects.oryapis.com/self-service/login?flow=6394ffa4-235f-4c1a-a200-e62f89862015curl -s -X POST -H  "Accept: application/json" -H "Content-Type: application/json" \    -d '{"identifier": "i-do-not-exist@user.org", "password": "the-wrong-password", "method": "password"}' \    "$actionUrl" | jq`

which in this case fails with a 400 Bad Request error and the following payload:

`{  "id": "6394ffa4-235f-4c1a-a200-e62f89862015",  "type": "api",  "expires_at": "2021-04-28T09:12:48.462374732Z",  "issued_at": "2021-04-28T09:02:48.462374732Z",  "request_url": "https://playground.projects.oryapis.com/self-service/login/api",  "ui": {    "action": "https://playground.projects.oryapis.com/self-service/login?flow=6394ffa4-235f-4c1a-a200-e62f89862015",    "method": "POST",    "messages": [      {        "id": 4000006,        "text": "The provided credentials are invalid, check for spelling mistakes in your password or username, email address, or phone number.",        "type": "error",        "context": {}      }    ],    "nodes": [      {        "type": "input",        "group": "default",        "attributes": {          "name": "csrf_token",          "type": "hidden",          "value": "",          "required": true,          "disabled": false        },        "messages": null,        "meta": {}      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "identifier",          "type": "text",          "value": "i-do-not-exist@user.org",          "required": true,          "disabled": false        },        "messages": null,        "meta": {          "label": {            "id": 1070004,            "text": "ID",            "type": "info"          }        }      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "password",          "type": "password",          "required": true,          "disabled": false        },        "messages": null,        "meta": {          "label": {            "id": 1070001,            "text": "Password",            "type": "info"          }        }      },      {        "type": "input",        "group": "password",        "attributes": {          "name": "method",          "type": "submit",          "value": "password",          "disabled": false        },        "messages": null,        "meta": {          "label": {            "id": 1010001,            "text": "Sign in",            "type": "info",            "context": {}          }        }      }    ]  },  "forced": false}`

On success, that endpoint would typically return a HTTP 200 Status OK response with the success `application/json` response payload in the body.
