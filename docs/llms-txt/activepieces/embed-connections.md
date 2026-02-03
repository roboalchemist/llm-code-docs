# Source: https://www.activepieces.com/docs/embedding/embed-connections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

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
      <img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=9382f3f1a86808f5ed0bc606a35e45e5" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=3303f2e34f6c26c12fcdb56005df0943 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=22ee05e3a93b273c8c819a607f2bdfb9 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=f2d66a1b1c9d2e10ae7b9d2b9ec62cf3 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=e8c2e1cde3c3a529213eed31cb71206a 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=bef8be950ee1c0ce2f39d58293f269d0 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=78986f41685be71b8983da0980e56554 2500w" />
      <img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=c422128afe4962d0ab2bc573ba6f1611" alt="Connections in Builder" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/connections-piece-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=774b8c071b5cce60912d70b0b2c838e8 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=f3b6d120935350d9f38601d8176d3ae9 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=f5e4500bf2967c2612bcc9434fc5684d 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=c141e3920da8c05b9ac54af9729052cf 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=bead38d253e5c33e26297c2d26b82823 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/connections-piece-usage.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=5f4f2ee7c3338ae41ac03ca8f734d8b7 2500w" />
    </Tip>
  </Step>
</Steps>
