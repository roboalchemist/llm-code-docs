# Source: https://www.activepieces.com/docs/build-pieces/sharing-pieces/private.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

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

        <img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=567001cb8e4a99373514c6e35453ed45" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/install-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=13a2d9202e3d27a6653499eedd717f66 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=7f98222dc723b6786e104cd7f1f72826 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=3b323ddcc2764d10ca5564ce4d585ed6 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c2e892899dccaa0d3b782e5f081efbbf 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=638f1e658e06f1d855f5b19a0ccff76d 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=f0d73c60a5077685d90f537a4f8a4ec1 2500w" />
  </Step>
</Steps>
