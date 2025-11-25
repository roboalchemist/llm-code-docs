# Source: https://www.activepieces.com/docs/developers/sharing-pieces/private.md

# Private

> Learn how to share your pieces privately.

<Snippet file="enterprise-feature.mdx" />

This guide assumes you have already created a piece and created a private fork of our repository, and you would like to package it as a file and upload it.

<Tip>
  Friendly Tip: There is a CLI to easily upload it to your platform. Please check out [Publish Custom Pieces](../misc/publish-piece).
</Tip>

<Steps>
  <Step title="Build Piece">
    Build the piece using the following command. Make sure to replace `${name}` with your piece name.

    ```bash  theme={null}
    npm run pieces -- build --name=${name}
    ```

    <Info>
      More information about building pieces can be found [here](../misc/build-piece).
    </Info>
  </Step>

  <Step title="Upload Tarball">
    Upload the generated tarball inside `dist/packages/pieces/${name}`from Activepieces Platform Admin -> Pieces

        <img src="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=1106164b9b77b33e96ccdcd4df789948" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/install-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=280&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c9009ba8db60863675f21036a561f4ce 280w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=560&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=c7ad50fd4c721848169fe6c9c2c6af0b 560w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=840&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=6cfedfb7edde2f9311a1af6b783520cf 840w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1100&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=615c3b9f24457a4384ede39ed276d50a 1100w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=1650&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=44499b6321130356ec94bc0826eb19fd 1650w, https://mintcdn.com/activepieces/qsnvmsFqox1HAfY0/resources/screenshots/install-piece.png?w=2500&fit=max&auto=format&n=qsnvmsFqox1HAfY0&q=85&s=b7cfc85def669ee351fef9150f4c3bce 2500w" />
  </Step>
</Steps>
