# Source: https://www.activepieces.com/docs/admin-guide/guides/manage-pieces.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Manage Pieces

> Control which integrations are available to your users

<Snippet file="enterprise-feature.mdx" />

## Overview

**Pieces** are the building blocks of Activepieces — they are integrations and connectors (like Google Sheets, Slack, OpenAI, etc.) that users can use in their automation flows.

As a platform administrator, you have full control over which pieces are available to your users. This allows you to:

* **Enforce security policies** by restricting access to certain integrations
* **Simplify the user experience** by showing only relevant pieces for your use case
* **Deploy custom/private pieces** that are specific to your organization

There are **two levels** of piece management:

| Level              | Who Can Manage | Scope                                         |
| ------------------ | -------------- | --------------------------------------------- |
| **Platform Level** | Platform Admin | Install and remove across the entire platform |
| **Project Level**  | Project Admin  | Show/hide specific pieces for specfic project |

***

## Platform-Level Management

Platform administrators can manage pieces for the entire Activepieces instance from **Platform Admin → Setup → Pieces**.

## Project-Level Management

Project administrators can further restrict which pieces are available within their specific project. This is useful when different teams or projects need access to different integrations.

### Show/Hide Pieces in a Project

<Steps>
  <Step title="Open Project Settings">
    Navigate to your project and go to **Settings → Pieces**.
  </Step>

  <Step title="Configure Visibility">
    You'll see a list of all pieces installed on the platform. Toggle the visibility for each piece:

    * **Enabled**: Users in this project can use the piece
    * **Disabled**: The piece is hidden from users in this project
  </Step>

  <Step title="Save Changes">
    Changes take effect immediately — users will only see the enabled pieces when building their flows.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=540db43cc2af946e0459d0e991f62f8a" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-pieces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=360ff34ac2a923cc117b8469e2be25d8 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=e2006953bea8e326a6f78c9abf872af3 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=f12bb52097f7faeb38f4057d05a52897 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=84828ce9235240b2e228924a379ab7a4 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=be51be697fdc5120c9251bf55f4e20d0 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=ea899782b139f0fa2f5d2a2d481ef256 2500w" />
<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=6701c9458d14e2da3d158f2adc783820" alt="Manage Pieces" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/manage-pieces-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=9be461917866f1c74fe2ffb0dc124d6f 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=e6245bd4d55d595ad9e40da2496b4c47 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c12d3839d562f7e32eea69295d1c780a 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=2fa98a8fd482c1cd0ae07cdb8fd6d653 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=0c78c26a3551120e08ebea3cb66e681d 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/manage-pieces-2.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=3e0a74e89a61b988c3f8e84099f8a3a1 2500w" />

<Note>
  Project-level settings can only **hide** pieces that are installed at the platform level. You cannot add pieces at the project level that aren't already installed on the platform.
</Note>

### Install Private Pieces

<Tip>
  For detailed instructions on building custom pieces, check the [Building Pieces](/build-pieces/building-pieces/overview) documentation.
</Tip>

If you've built a custom piece for your organization, you can upload it directly as a tarball (`.tgz`) file.

<Steps>
  <Step title="Build Your Piece">
    Build your piece using the Activepieces CLI:

    ```bash  theme={null}
    npm run pieces -- build --name=your-piece-name
    ```

    This generates a tarball in `dist/packages/pieces/your-piece-name`.
  </Step>

  <Step title="Navigate to Pieces Settings">
    Go to **Platform Admin → Setup → Pieces** and click **Install Piece**.
  </Step>

  <Step title="Select File Upload">
    Choose **Upload File** as the installation source.
  </Step>

  <Step title="Upload the Tarball">
    Select the `.tgz` file from your build output and upload it.
  </Step>
</Steps>

<img src="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=567001cb8e4a99373514c6e35453ed45" alt="Install Piece" data-og-width="1420" width="1420" data-og-height="900" height="900" data-path="resources/screenshots/install-piece.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=280&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=13a2d9202e3d27a6653499eedd717f66 280w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=560&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=7f98222dc723b6786e104cd7f1f72826 560w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=840&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=3b323ddcc2764d10ca5564ce4d585ed6 840w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=1100&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=c2e892899dccaa0d3b782e5f081efbbf 1100w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=1650&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=638f1e658e06f1d855f5b19a0ccff76d 1650w, https://mintcdn.com/activepieces/uHZ35vXyxX7goNO-/resources/screenshots/install-piece.png?w=2500&fit=max&auto=format&n=uHZ35vXyxX7goNO-&q=85&s=f0d73c60a5077685d90f537a4f8a4ec1 2500w" />
