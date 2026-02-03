# Source: https://docs.zapier.com/powered-by-zapier/authentication/methods/app-access-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# App Access Token

> How to authenticate with an App Access Token

### Prerequisites

* Your app needs to be published as a [public integration](https://platform.zapier.com/quickstart/private-vs-public-integrations) in Zapier's App Directory.

### Retrieving and Using an App Access Token

While many API endpoints require a user access token to perform actions on behalf of a user, some (like [unenrolling a user from a promotion](https://docs.zapier.com/powered-by-zapier/api-reference/promotions/delete-enrollment)) require an App Access Token.

<Steps>
  <Step title="Get your Client ID and Client Secret">
    You can find your Client ID and Client Secret in the [Zapier Developer Platform](https://developer.zapier.com/) under `Embed` → `Settings` → `Credentials`

    <Frame>
      ![Client ID and Secret](https://cdn.zappy.app/cb3660c17a3d26b36f438ab80c0860d5.png)
    </Frame>

    <Warning>
      Your application's **Client ID** and **Client Secret** are only available after you've published your app as a [public integration in Zapier's App Directory](https://platform.zapier.com/quickstart/private-vs-public-integrations).
    </Warning>

    <Info>
      Regenerating your client secret will invalidate any previous secret.
    </Info>
  </Step>

  <Step title="Determine which OAuth scopes are required for your use case">
    The various endpoints of the Zapier Workflow API require different OAuth scopes. Information on specific scopes required is included within the API reference for each endpoint.

    <Frame>
      ![](https://cdn.zappy.app/173f199893095dba32f29e364f7a889e.png)
    </Frame>
  </Step>

  <Step title="Retrieve the App Access Token">
    The final step is to exchange the **client credentials** for an **access token** that can be used to make authorized requests to the Zapier Workflow API. You make the exchange with a `POST` request to Zapier's token endpoint `https://zapier.com/oauth/token/`.

    Below is an example of a request that can be used to do the exchange.

    <CodeGroup>
      ```sh cURL theme={null}
      curl -v -u {CLIENT_ID}:{CLIENT_SECRET} \
      -H "Content-Type: multipart/form-data" \
      -F grant_type=client_credentials \
      -F scope="{SCOPE}" \
      https://zapier.com/oauth/token/
      ```

      ```python Python theme={null}
      import requests

      data = 'grant_type=client_credentials&scope={SCOPE}'

      response = requests.post('https://zapier.com/oauth/token/', headers=headers, data=data, auth=('{CLIENT_ID}', '{CLIENT_SECRET}'))
      ```

      ```js Javascript theme={null}
      fetch('https://zapier.com/oauth/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Basic ' + btoa('{CLIENT_ID}:{CLIENT_SECRET}')
        },
        body: 'grant_type=client_credentials&scope={SCOPE}'
      });
      ```

      ```php PHP theme={null}
      <?php
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_URL, 'https://zapier.com/oauth/token/');
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
      curl_setopt($ch, CURLOPT_HTTPHEADER, [
          'Content-Type: multipart/form-data',
      ]);
      curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
      curl_setopt($ch, CURLOPT_USERPWD, '{CLIENT_ID}:{CLIENT_SECRET}');
      curl_setopt($ch, CURLOPT_POSTFIELDS, 'grant_type=client_credentials&scope={SCOPE}');

      $response = curl_exec($ch);

      curl_close($ch);
      ```
    </CodeGroup>

    | Parameter       | Meaning                                                                                                                                   |
    | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
    | `CLIENT_ID`     | This will be same client id that you retrieved in step #1.                                                                                |
    | `CLIENT_SECRET` | This is a secret known only to your application and the authorization server. It will be the client secret that you retrieved in step #1. |
    | `SCOPE`         | This is the one or more scope(s) needed from step #2, separated by spaces.                                                                |

    Note that, in addition to client id and secret being passed as a Basic Authentication header as above, they can be
    passed as part of the body, using the keys `client_id` and `client_secret`.

    You'll recieve a response that looks like this:

    ```js  theme={null}
    HTTP/1.1 200 OK
    Content-Type: multipart/form-data
    Cache-Control: no-store
    Pragma: no-cache

    {
      "access_token": "jk8s9dGJK39JKD93jkd03JD",
      "expires_in": 36000,
      "token_type": "Bearer",
      "scope": "promotions:read promotions:write"
    }
    ```

    <Check>
      This response contains the `access_token` that you'll use to make API request on your app's behalf.
    </Check>

    <Warning>
      The access token **MUST** be stored securely on your server, to protect your app's security and your users' privacy. It **MAY NOT** be used in browser (frontend) requests.
    </Warning>
  </Step>

  <Step title="Using the access token">
    The access token should be passed with requests as an `Authorization` header. For example:

    ```
    Authorization: Bearer jk8s9dGJK39JKD93jkd03JD
    ```
  </Step>
</Steps>
