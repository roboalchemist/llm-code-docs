# Source: https://docs.zapier.com/powered-by-zapier/authentication/methods/client-id.md

# Client ID

> How to authenticate with your Client ID

Most endpoints require app or user access token authentication. However, a smaller number of endpoints require only a valid Client ID in order to be accessed.

### Prerequisites

* Your app needs to be published as a [public integration](https://platform.zapier.com/quickstart/private-vs-public-integrations) in Zapier's App Directory.

### Retrieving and Using your Client ID

<Steps>
  <Step title="Get your Client ID">
    You can find your Client ID in the [Zapier Developer Platform](https://developer.zapier.com/) under `Embed` → `Settings` → `Credentials`

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

  <Step title="Pass the Client ID as a query parameter">
    From there, simply pass your `client_id` as a query param to any V1 endpoints that require it.

    ```js Example for Zap-templates theme={null}
        https://api.zapier.com/v1/zap-templates?client_id={YOUR_CLIENT_ID}
    ```
  </Step>
</Steps>
