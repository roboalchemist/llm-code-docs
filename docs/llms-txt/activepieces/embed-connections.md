# Source: https://www.activepieces.com/docs/embedding/embed-connections.md

# Create/Update Connections

<Info>
  **Requirements:**

  * Activepieces version 0.34.5 or higher
  * SDK version 0.3.2 or higher
</Info>

<Snippet file="replace-oauth2-apps.mdx" />

<Info>
  "connectionName" is the externalId of the connection (you can get it by hovering the connection name in the connections table).  <br />
  We kept the same parameter name for backward compatibility, anyone upgrading their instance from \< 0.35.1, will not face issues in that regard.
</Info>

<Warning>
  **Breaking Change:** <br /><br /> If your Activepieces instance version is \< 0.45.0 and (you are using the connect method from the embed sdk, and need the connection externalId to be returned after the user creates it OR if you want to reconnect a specific connection with an externalId), you must upgrade your instance to >= 0.45.0
</Warning>

* You can use the embedded SDK in your SaaS to allow your users to create connections and store them in Activepieces.

<Steps>
  <Step title="Initialize the SDK">
    Follow the instructions in the [Embed Builder](./embed-builder).
  </Step>

  <Step title="Call Connect Method">
    After initializing the SDK, you will have access to a property called `activepieces` inside your `window` object. Call its `connect` method to open a new connection dialog as follows.

    ```html  theme={null}
    <script> 
    activepieces.connect({pieceName:'@activepieces/piece-google-sheets'});
    </script>
    ```

    **Connect Parameters:**

    | Parameter Name | Required | Type                                                              | Description                                                                                                                                                                                                   |
    | -------------- | -------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | pieceName      | ✅        | string                                                            | The name of the piece you want to create a connection for.                                                                                                                                                    |
    | connectionName | ❌        | string                                                            | The external Id of the connection (you can get it by hovering the connection name in the connections table), when provided the connection created/upserted will use this as the external Id and display name. |
    | newWindow      | ❌        | \{ width?: number, height?: number, top?: number, left?: number } | If set the connection dialog will be opened in a new window instead of an iframe taking the full page.                                                                                                        |

    **Connect Result**

    The `connect` method returns a `promise` that resolves to the following:

    ```ts  theme={null}
    {
        connection?: {
            id: string,
            name: string
        }
    }
    ```

    <Info>
      `name` is the externalId of the connection.
      `connection` is undefined if the user closes the dialog and doesn't create a connection.
    </Info>

    <Tip>
      You can use the `connections` piece in the builder to retrieve the created connection using its name.
      <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c8d14d795364249e9d64fd48c8e2d484" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=4a5f42ec16c8293fd15825e2c94ad8ca 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=51f4632b11ce07e408de35aff0a59f6b 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=8b69d0a232717898fa91b8e3e6f5d185 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=75bf08645aa881589852c475ec2d2511 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=256226de97f2f5f0e956aa51a2e93fcf 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=110fab4a94a0ce9ae11db921b90b2cbc 2500w" />
      <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=402d7a7e10ef1f72517a6618d99ea3c8" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=d7cb20b21c1830e162bb40b14807dd79 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e1c8b2b823c90d3f84757b667b109b41 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=e28b5f05c90d7d4b95b853ea4977f95e 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=f3439d8a86f3c8dcb021fa76e4710920 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=920cb29c9b9b24c577431f5842cae52a 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/connections-piece-usage.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3a5c9dbbe461c92f0ae6efd07a409d7d 2500w" />
    </Tip>
  </Step>
</Steps>
