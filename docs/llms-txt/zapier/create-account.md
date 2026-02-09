# Source: https://docs.zapier.com/powered-by-zapier/api-reference/accounts/create-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Account

> Create a new user and obtain an access token. See our Quick Account Creation guide to get started.

⚠️ *This is not a regular API endpoint that returns JSON.*

👉 **It is a flow that includes account creation and OAuth authorization**.

This URL should be opened in a popup window. See the [Quick Account
Creation](/powered-by-zapier/managed-authentication/quick-account-creation) page
for more information about allowing your customers to sign up for Zapier easily.

## Main page example

Start with this example code in order to build a correct `/v2/authorize` API
call in a well-sized popup window and `await` the completion of the flow. Then
you can use the other API endpoints to retrieve your needed information.

**zapier.js**

```js  theme={null}
/**
 * Ensure the user has a Zapier account and has authorized this
 * site to access it. If not, a log in form or sign up form
 * will be shown to the user along the way.
 *
 * @param {Object} options
 * @param {String} options.clientId - The OAuth client ID
 * @param {String} options.signUpEmail - The user's email to use for pre-filling the sign up form.
 * @param {String} options.signUpFirstName - The user's first name to use for pre-filling the sign up form.
 * @param {String} options.signUpLastName - The user's last name to use for pre-filling the sign up form.
 */
export async function zapierAuthorize(options) {
  const root = "https://api.zapier.com";
  const url = new URL("/v2/authorize", root);
  const params = url.searchParams;
  params.set("client_id", options.clientId);
  params.set("redirect_uri", location.href);
  params.set("response_type", "code");
  const scopes = ["zap", "profile"];
  params.set("scope", scopes.join(" "));
  //
  // These parameters are optional but highly recommended.
  // Users will receive a prefilled sign up form,
  // allowing them to continue with a single click
  // (or edit the values).
  //
  params.set("sign_up_email", options.signUpEmail);
  params.set("sign_up_first_name", options.signUpFirstName);
  params.set("sign_up_last_name", options.signUpLastName);

  // Navigate to the /v2/authorize API, which will eventually
  // redirect back to `location.href` but with `?code=<CODE>`
  // in the URL parameters. At this point you will need to
  // exchange the OAuth code for an OAuth token.
  const popup = window.open(
    url.href,
    // If you give an opened window a name, it will prevent there
    // from being more than one window open at the same time with
    // that name. The new URL supplied to `open` will navigate
    //  existing window.
    "zapier-authorize",
    // Ensure a comfortable amount of space in the popup
    "width=1024,height=1280",
  );
  if (!popup) {
    alert("Failed to open popup window. Please allow popups and try again.");
  }
  const data = await waitForPopupClose(popup);
}

/**
 * Waits for the given popup window to close,
 * or for it to send a message that passes the `callback` function supplied.
 *
 * @param {Window} popup - The popup window created by `window.open`
 */
async function waitForPopupClose(popup) {
  return await new Promise((resolve) => {
    function onMessage(event) {
      if (
        typeof event.data === "object" &&
        event.data &&
        event.data.type === "zapier.popup.close"
      ) {
        popup.close();
        finishAndCleanUp(event.data);
      } else {
        console.warn("unhandled message event: (data)", event.data);
      }
    }
    function finishAndCleanUp() {
      resolve(undefined);
      removeEventListener("message", onMessage);
      clearInterval(interval);
    }
    // Wait for `postMessage` event
    addEventListener("message", onMessage);
    // Wait for popup to be closed if the message wasn't received
    const interval = setInterval(() => {
      if (popup.closed) {
        // The interval may have run after the popup closed and before onMessage
        // had a chance to process messages. This prevents a frequent race
        // condition in Firefox, where finishAndCleanUp was called here before
        // onMessage could call finishAndCleanUp.
        setTimeout(() => {
          finishAndCleanUp(undefined);
        });
      }
    });
  });
}
```

## Redirect URI page example

The redirect URI page must exchange the OAuth code for an OAuth token within 2
minutes. The resulting token MAY NOT be stored in an insecure manner. The
suggested location is in your application's database, in a data model for the
current user.

See the [OAuth 2.0 Token
Exchange](https://datatracker.ietf.org/doc/html/rfc8693) RFC for more detail.

```js  theme={null}
const url = new URL(request.url);
const code = url.searchParams.get("code");
const token = await EXCHANGE_CODE_FOR_TOKEN(code);
await SAVE_TOKEN_TO_DATABASE(CURRENT_USER_ID, token);
```


## OpenAPI

````yaml https://api.zapier.com/schema get /v2/authorize
openapi: 3.1.0
info:
  title: Partner API
  version: 2024.11.0
  description: >

    ## Introduction


    The Partner API is the best tool for complete style control over a user's
    Zapier experience within your app.

    Essentially, it lets you customize how you present Zapier within your
    product without sacrificing your app's look,

    feel, and flow.


    Think of it as a native Zapier integration, helping you showcase your best
    Zapier-powered workflows where it's most

    helpful to your users (within the flow of your tool). You can customize
    styling, streamline Zap set-up for users,

    expose relevant Zap information, and more!


    With the Partner API, you can:


    - Get a list of all the apps available in Zapier's app directory so you can
    power your app directory and show your

    users all the integration possibilities with your Zapier integration.

    - Have complete style control over how you present Zap templates in your
    product. The Partner API gives you access

    to the raw Zap Template data so you can give your users access to your Zap
    template with your product's style, look

    and feel.

    - Get access to all your Zap templates and give your users the ability to
    search to quickly find the one they need.

    - Streamline Zap setup by pre-filling fields on behalf of your users.

    - Show users the Zaps they have set up from right within your product
    keeping them on your site longer and giving them

    complete confidence in their Zapier integration.

    - Embed our Zapier Editor to allow your users to create new Zaps and modify
    existing ones, without needing to leave

    your product.


    ## Authentication


    There are two ways to authenticate with the Partner API.


    1. Your application's `client_id` which you will receive once you are
    approved for access to the API

    (Client ID Authentication)

    2. A user's access token (Access Token Authentication).


    Which authentication method you should use depends on which endpoint(s) you
    are using.

    Review each endpoint's documentation to understand which parameters are
    required.


    > Note: while we do generate a `client_secret`, the type of grant we use
    (implicit) doesn't

    need it so it's not something we provide.'


    ## Learn more


    See the [Workflow API
    documentation](https://docs.zapier.com/partner-solutions/workflow-api/intro)
    for more information.
  contact:
    name: Zapier
    url: https://developer.zapier.com/contact
servers:
  - url: https://api.zapier.com
security: []
tags:
  - name: Accounts
    description: Refers to resources interacting with 'Accounts' associated resources
  - name: Actions
    description: Refers to resources interacting with 'Actions' associated resources
  - name: Apps
    description: Refers to resources interacting with 'Apps' associated resources
  - name: Authentications
    description: >-
      Refers to resources interacting with 'Authentications' associated
      resources
  - name: Categories
    description: Refers to resources interacting with 'Categories' associated resources
  - name: Experimental
    description: Refers to resources interacting with 'Experimental' associated resources
  - name: Inputs
    description: Refers to resources interacting with 'Inputs' associated resources
  - name: Outputs
    description: Refers to resources interacting with 'Outputs' associated resources
  - name: Zaps
    description: Refers to resources interacting with 'Zaps' associated resources
  - name: Zap Templates
    description: Refers to resources interacting with 'Zap Templates' associated resources
paths:
  /v2/authorize:
    get:
      tags:
        - Accounts
      summary: Create Account
      description: >-
        Create a new user and obtain an access token. See our Quick Account
        Creation guide to get started.
      operationId: v2_authorize_list
      parameters:
        - in: query
          name: client_id
          schema:
            type: string
            minLength: 1
          description: Your application Client ID.
          required: true
        - in: query
          name: redirect_uri
          schema:
            type: string
            minLength: 1
          description: The page the user will be redirect to after OAuth flow.
          required: true
        - in: query
          name: referer
          schema:
            type: string
            minLength: 1
        - in: query
          name: response_type
          schema:
            type: string
            minLength: 1
          description: Only OAuth response type `code` is supported
          required: true
        - in: query
          name: scope
          schema:
            type: string
            minLength: 1
          description: Space (`%20`) separated values
          required: true
        - in: query
          name: sign_up_email
          schema:
            type: string
            format: email
            minLength: 1
          description: Email of the user signing up.
        - in: query
          name: sign_up_first_name
          schema:
            type: string
            minLength: 1
          description: First name of the user signing up.
        - in: query
          name: sign_up_last_name
          schema:
            type: string
            minLength: 1
          description: Last name of the user signing up.
        - in: query
          name: utm_campaign
          schema:
            type: string
            default: workflow_api
            minLength: 1
        - in: query
          name: utm_content
          schema:
            type: string
            minLength: 1
        - in: query
          name: utm_medium
          schema:
            type: string
            default: embed
            minLength: 1
        - in: query
          name: utm_source
          schema:
            type: string
            default: partner
            minLength: 1
      responses:
        '302':
          description: Redirect to authorization URL
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                MalformedRequest.:
                  value:
                    errors:
                      - status: 400
                        code: parse_error
                        title: ParseError
                        detail: Malformed request.
                        source: null
                        meta:
                          source: ZAPIER
                          full_details:
                            message: Malformed request.
                            code: parse_error
                  summary: Malformed request.
          description: This schema can be expected for 4xx 'Malformed request.' errors
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 401 Response
        '403':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 403 Response
        '409':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 409 Response
        '429':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 429 Response
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                AServerErrorOccurred.:
                  value:
                    errors:
                      - status: 500
                        code: error
                        title: APIException
                        detail: A server error occurred.
                        source: null
                        meta:
                          source: ZAPIER
                          full_details:
                            message: A server error occurred.
                            code: error
                  summary: A server error occurred.
          description: >-
            This schema can be expected for 5xx 'A server error occurred.'
            errors
        '503':
          headers:
            Retry-After:
              schema:
                type: string
                format: uri
              description: Indicates when to retry the request
            X-RateLimit-Limit:
              schema:
                type: string
                format: uri
              description: >-
                The maximum number of requests you're permitted to make per
                hour.
            X-RateLimit-Remaining:
              schema:
                type: string
                format: uri
              description: >-
                The number of requests remaining in the current rate limit
                window.
            X-RateLimit-Reset:
              schema:
                type: string
                format: uri
              description: >-
                The time at which the current rate limit window resets in UTC
                epoch seconds.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 503 Response
        '504':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
          description: 504 Response
      security:
        - ClientIDAuthentication: []
components:
  schemas:
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: An array of error objects.
      required:
        - errors
    Error:
      type: object
      description: Base Error definition
      properties:
        status:
          type: integer
          description: The HTTP status code applicable to this problem.
        code:
          type: string
          description: A unique identifier for this particular occurrence of the problem.
        title:
          type: string
          description: A short summary of the problem.
        detail:
          type: string
          description: >-
            A human-readable explanation specific to this occurrence of the
            problem.
        source:
          oneOf:
            - $ref: '#/components/schemas/ErrorSource'
            - type: 'null'
          description: An object containing references to the primary source of the error.
        meta:
          type:
            - object
            - 'null'
          additionalProperties: {}
          description: Freeform metadata about the error
    ErrorSource:
      type: object
      description: Populates the `source` object inside our error responses.
      properties:
        pointer:
          type: string
          description: >-
            Pointer to the value in the request document that caused the error
            e.g. `/actions`.
        parameter:
          type: string
          description: A string indicating which URI query parameter caused the error.
        header:
          type: string
          description: >-
            A string indicating the name of a single request header which caused
            the error.
  securitySchemes:
    ClientIDAuthentication:
      type: apiKey
      in: query
      name: client_id
      description: See our authentication documentation for how to find your Client ID
      x-zapier-auth-scheme-exempt: true

````