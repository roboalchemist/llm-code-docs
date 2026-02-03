# Source: https://www.activepieces.com/docs/embedding/customize-pieces.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Show/Hide Pieces

<Snippet file="enterprise-feature.mdx" />

<Snippet file="replace-oauth2-apps.mdx" />

If you would like to only show specific pieces to your embedding users, we recommend you do the following:

<Steps>
  <Step title="Tag Pieces">
    Tag the pieces you would like to show to your user by going to **Platform Admin -> Setup -> Pieces**, selecting the pieces you would like to tag and hit **Apply Tags**

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c29f36ab63e2a3165877f29f600f5634" alt="Bulk Tag" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/tag-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=21126e13a25befa7c1cec784d02842b1 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=1de546ab4a94815ab798c66ed5603a3d 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=b8c0060d77780c59571ab21f399fc492 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=4f24e64dbea47d78b326893d71a3e71b 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=d2fe8b033cb83170648ac7b520fd5dd7 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/tag-pieces.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=3a225095e3c85e8aaac53f6c0fad62ff 2500w" />
  </Step>

  <Step title="Add Tags to Provision Token">
    You need to specify the tags of pieces in the token, check how to generate token in [provisioning users](./provision-users).

    You should specify the `pieces` claim like this:

    ```json  theme={null}
    {
        /// Other claims
        "piecesFilterType": "ALLOWED",
        "piecesTags": [ "free" ]
    }
    ```

    Each time the token is used by the embedding SDK, it will sync all pieces with these tags to the token's project.
    The project will only contain the pieces that contain these tags.
  </Step>
</Steps>
