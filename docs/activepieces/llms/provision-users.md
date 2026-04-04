# Source: https://www.activepieces.com/docs/embedding/provision-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Provision Users

> Automatically authenticate your SaaS users to your Activepieces instance

<Snippet file="enterprise-feature.mdx" />

## Overview

In Activepieces, there are **Projects** and **Users**. Each project is provisioned with their corresponding workspace, project, or team in your SaaS. The users are then mapped to the respective users in Activepieces.

To achieve this, the backend will generate a signed token that contains all the necessary information to automatically create a user and project. If the user or project already exists, it will skip the creation and log in the user directly.

<Steps>
  <Step title="Step 1: Obtain Signing Key">
    You can generate a signing key by going to **Platform Settings -> Signing Keys -> Generate Signing Key**.

    This will generate a public and private key pair. The public key will be used by Activepieces to verify the signature of the JWT tokens you send. The private key will be used by you to sign the JWT tokens.

        <img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=734855a5e44c784405ce5d0d7cb015db" alt="Create Signing Key" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/create-signing-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=671a50f3e1333da45fbc3321dde23219 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=c9d3497892800c2d3ac19ce545a7a599 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=59d0c3fb6a62988df0dfe2f711a0ac0b 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=75308632056e621a7c858029af6d1c3a 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=0ae148ad75be0ac2d58060988f06d64c 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/screenshots/create-signing-key.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=979139e06bf803a368f38dbd356d8d52 2500w" />

    <Warning>
      Please store your private key in a safe place, as it will not be stored in Activepieces.
    </Warning>
  </Step>

  <Step title="Step 2: Generate a JWT">
    The signing key will be used to generate JWT tokens for the currently logged-in user on your website, which will then be sent to the Activepieces Iframe as a query parameter to authenticate the user and exchange the token for a longer lived token.

    To generate these tokens, you will need to add code in your backend to generate the token using the RS256 algorithm, so the JWT header would look like this:

    <Tip>
      To obtain the `SIGNING_KEY_ID`, refer to the signing key table and locate the value in the first column.
      <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=eca571e6dfe3d25b77160cc1dbdc8ef2" alt="Signing Key ID" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/signing-key-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4de4fb23fce778d2fd81d5eebef73916 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=91a481030a9371be81bb5ddd35fb6e81 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=01a918cf7d5cd470f1e3dcc07304166b 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=5aed025f8dfd1f8330ba0f7eee2c4f87 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=1886a1e1fb482dbc6ae6aa8955025eb3 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/signing-key-id.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=e4fbadf85aa80f878a53f3e39f6ac591 2500w" />
    </Tip>

    ```json  theme={null}
    {
      "alg": "RS256",
      "typ": "JWT",
      "kid": "SIGNING_KEY_ID"
    }
    ```

    The signed tokens must include these claims in the payload:

    ```json  theme={null}
    {
      "version": "v3",
      "externalUserId": "user_id",
      "externalProjectId": "user_project_id",
      "firstName": "John",
      "lastName": "Doe",
      "role": "EDITOR",
      "piecesFilterType": "NONE",
      "exp": 1856563200,
      "tasks": 50000,
      "aiCredits": 250
    }
    ```

    | Claim              | Description                                                                            |
    | ------------------ | -------------------------------------------------------------------------------------- |
    | externalUserId     | Unique identification of the user in **your** software                                 |
    | externalProjectId  | Unique identification of the user's project in **your** software                       |
    | projectDisplayName | Display name of the user's project                                                     |
    | firstName          | First name of the user                                                                 |
    | lastName           | Last name of the user                                                                  |
    | role               | Role of the user in the Activepieces project (e.g., **EDITOR**, **VIEWER**, **ADMIN**) |
    | exp                | Expiry timestamp for the token (Unix timestamp)                                        |
    | piecesFilterType   | Customize the project pieces, check [customize pieces](/embedding/customize-pieces)    |
    | piecesTags         | Customize the project pieces, check [customize pieces](/embedding/customize-pieces)    |
    | tasks              | Customize the tasks limit for your user's project                                      |
    | aiCredits          | Customize the ai credits limit for your user's project                                 |

    You can use any JWT library to generate the token. Here is an example using the jsonwebtoken library in Node.js:

    <Tip>
      **Friendly Tip #1**: You can also use this [tool](https://dinochiesa.github.io/jwt/) to generate a quick example.
    </Tip>

    <Tip>
      **Friendly Tip #2**: Make sure the expiry time is very short, as it's a temporary token and will be exchanged for a longer-lived token.
    </Tip>

    ```javascript Node.js theme={null}
    const jwt = require('jsonwebtoken');

    // JWT NumericDates specified in seconds:
    const currentTime = Math.floor(Date.now() / 1000);
    let token = jwt.sign(
      {
        version: "v3",
        externalUserId: "user_id",
        externalProjectId: "user_project_id",
        firstName: "John",
        lastName: "Doe",
        role: "EDITOR",
        piecesFilterType: "NONE",
        exp: currentTime + (60 * 60), // 1 hour from now
      },
      process.env.ACTIVEPIECES_SIGNING_KEY,
      {
        algorithm: "RS256",
        header: {
          kid: signingKeyID, // Include the "kid" in the header
        },
      }
    );
    ```

    Once you have generated the token, please check the embedding docs to know how to embed the token in the iframe.
  </Step>
</Steps>
