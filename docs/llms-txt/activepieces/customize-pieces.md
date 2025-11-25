# Source: https://www.activepieces.com/docs/embedding/customize-pieces.md

# Show/Hide Pieces

<Snippet file="enterprise-feature.mdx" />

<Snippet file="replace-oauth2-apps.mdx" />

If you would like to only show specific pieces to your embedding users, we recommend you do the following:

<Steps>
  <Step title="Tag Pieces">
    Tag the pieces you would like to show to your user by going to **Platform Admin -> Setup -> Pieces**, selecting the pieces you would like to tag and hit **Apply Tags**

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2cb4bd65c2a93d5680fb877d8add35d6" alt="Bulk Tag" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/tag-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1fdf24f613938a6149c3d18f12476d3f 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=3bafd772b35a2a39f87bbb9f41f2a04d 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=2c7712ea0a1ba76fe15933f3852b13fb 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=20baa4b9210a32bd3274e80465afd440 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b9f2c83196e8b5ce48da8110828e5ab5 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/tag-pieces.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=fe1eb1911ea54eeed58ba48705faefa5 2500w" />
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
