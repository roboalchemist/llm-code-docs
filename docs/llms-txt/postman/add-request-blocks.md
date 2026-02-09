# Add request blocks to your notebook

You can add API requests and reference their responses elsewhere in your notebook to create an interactive experience. For example, you can [add an input block](/docs/postman-api-network/showcase/publish/notebooks/draft/add-input-blocks/) for your API consumer's email address and use a request block to send them a welcome message.

## Add a request block

To add a request block, do the following:

1. Open your notebook or [create a new one](https://www.postman.com/notebook/new).
2. Place your cursor where you want to add the request block. Then, type a forward slash (\"/\"). Postman displays a block menu.
3. Choose ![Image 1: Request icon](https://assets.postman.com/postman-docs/aether-icons/entity-request-stroke.svg#icon) **Request Block**.
4. Search for your public request or paste its URL or UUID. Then, select it. Postman displays the request, any variables you or your API consumers may need to define, a way for you or your API consumer to define the request body, and a button to send the request.
5. Name your request block.
6. If necessary, define the variables. These may include query and path parameter values, or other values defined in the request.
7. (Optional) Define an override. This overrides the request's body.
8. Click ![Image 2: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Send**.

Postman sends the request and returns the response.

If the request changes, you can refresh the request block. To refresh it, next to the endpoint, click ![Image 3: Refresh icon](https://assets.postman.com/postman-docs/aether-icons/action-refresh-stroke.svg#icon) **Refresh**. To start over, click ![Image 4: Clear icon](https://assets.postman.com/postman-docs/aether-icons/action-clear-stroke.svg#icon) **Clear**.

## Reference your request block

You can reference your request block by name. For example, if you name your request block "getUser", you can reference its response in another request block with the syntax `{{getUser}}`. Or you can reference it in a [script runner block](/docs/postman-api-network/showcase/publish/notebooks/draft/add-code-runner-blocks/) with the syntax `$getUser`.

Furthermore, you can use dot notation to reference data within a response. For example, in another request block, you can reference the user's first email with the syntax `{{getUser.emails.0}}`. Or in a [script runner block](/docs/postman-api-network/showcase/publish/notebooks/draft/add-code-runner-blocks/), you can reference the same value with the syntax `$getUser.emails[0]`.

To reference your request block, do the following:

1. Open your notebook or [create a new one](https://www.postman.com/notebook/new).
2. Get your request block's name.
3. Reference your request block:

   - To reference your request block in an input or another request block, use the syntax `{{requestBlockName}}` or `{{requestBlockName.path.to.data}}`.
   - To reference your request block in a script runner block, use the syntax `$requestBlockName` or `$requestBlockName.path.to.data`.

## Send requests in sequence

If you can use the data from one response in the request of another, you can send those requests in sequence. For example, you can get a user's email from a response and use it to send a different request.

To send requests in sequence, do the following:

1. Open your notebook or [create a new one](https://www.postman.com/notebook/new).
2. In the first request block, click ![Image 5: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Send**.
3. In the second request block, reference the first request block with the syntax `{{requestBlockName.path.to.data}}`. Then, click ![Image 6: Run icon](https://assets.postman.com/postman-docs/aether-icons/action-run-stroke.svg#icon) **Send**.

Postman uses the first request's response to send the second request. You can add more requests to the sequence.

---

**Note:** Postman's Local Secret Protection is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

With the Secret Scanner's Local Secret Protection, [Team Admins](/docs/administration/roles-and-permissions/#team-roles) can configure where Postman stores the team's exposed secrets in the workspaces or types of workspaces you've defined.

When [enabled](#enable-local-secret-protection), Postman scans secrets in real time and takes action, storing exposed secrets, like API keys, JWT tokens, or auth tokens, in the [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/). The Postman Vault stores your exposed secrets securely on your device. The original secret value is replaced with a vault secret reference. This prevents your team's secrets from syncing to the Postman cloud and gives you greater control over your team's security posture and compliance requirements.

Postman's Local Secret Protection actively scans for secrets in the following Postman elements when changes are made:

- HTTP collections
- Environments variable values
- Global variable values

Local Secret Protection requires Postman version 11.71.3 or later.

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click ![Image 7: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 8: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

- To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
- To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** > **Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

- The total number of detected secrets automatically moved to the Postman Vault.
- The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

---

**Note:** You can't delete component files.

### View live documentation

Postman displays a live preview of your API's documentation as you edit your component file. To show the documentation preview, click ![Image 9: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Live preview** in the right sidebar. Click ![Image 10: Close icon](https://assets.postman.com/postman-docs/aether-icons/action-close-stroke.svg#icon) **Close** to hide the documentation preview.

### Validate a component file

Postman identifies syntax errors as you edit your component file. Syntax errors can include missing fields, malformed field names, wrong data types, wrong nesting, or other issues.

**Note:** Postman also identifies governance issues for components, but only once they're [referenced in your specification](#reference-a-component-in-a-specification).

## Version and publish a component file

Publish a version of a component file to share the latest changes to your reusable components with your team. Versioning component files is useful for publishing a new version of your reusable components, while still supporting earlier versions. You can't edit versions once they're published.

1. Click ![Image 11: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.
3. Click **Version & Publish** in the upper right corner.

![Image 12: Version and publish a component file](https://assets.postman.com/postman-docs/v11/component-library-publish-v11.png)

1. Enter a version number. The version number must be unique to the component file. The version number can only contain alphanumeric characters, periods, underscores, dashes, plus signs, and no spaces.
2. Click **Create Version & Publish**.

Once the component is published, your teammates can [reference the file's components](#reference-a-component-in-a-specification) in their specifications.

To publish a new version of your component, select **Draft** in the version dropdown list. [Edit the component file](#edit-a-component-file) and then publish a new version.

**Note:** You can't delete published versions of component files.

## Reference a component in a specification

Reference reusable components in your OpenAPI specifications using the URL to the component and its version. A component file must have a [published version](#version-and-publish-a-component-file) before you can reference its components in your specification.

1. Click ![Image 13: Docs icon](https://assets.postman.com/postman-docs/aether-icons/entity-docs-stroke.svg#icon) **Specs** in the sidebar, and open a specification.
2. Click ![Image 14: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification.
3. Click **Open Component Library**.
4. Search for a component file and select it in the left sidebar.
5. Choose a published version of the component file using the version dropdown list.
6. In the left sidebar, click ![Image 15: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy component link** next to a component. This copies the URL to the version of the component you select in the dropdown list.
7. Add the URL to a reference (`$ref`) in your specification.

**Note:** From a specification, you can also copy the URL to the latest version of a component. Click ![Image 16: Library icon](https://assets.postman.com/postman-docs/aether-icons/descriptive-library-stroke.svg#icon) **Components** in the lower right of the specification. Then hover over a component and click ![Image 17: Link icon](https://assets.postman.com/postman-docs/aether-icons/action-link-stroke.svg#icon) **Copy link**.

As you edit your specification, Postman displays autocomplete suggestions for published components in your team's component library. Enter a component name as the value of a reference (`$ref`) and select it from the suggestions list. The URL to the latest version is added as the value.

Postman also identifies governance issues for components referenced in your specification. Governance issues are violations of the [Postman API Governance](/docs/api-governance/api-governance-overview/) rules configured for your team. Learn more about [viewing rule violations in your specification](/docs/design-apis/specifications/validate-a-specification/#view-rule-violations-in-your-specification).

## Sync components between collections and specifications

Consider the following behavior when syncing changes to reusable components between collections and OpenAPI specifications.

- When you [generate a collection from a specification](/docs/design-apis/specifications/generate-collections/), Postman uses referenced components from your team's component library to populate relevant parts of the collection.
- When you [sync changes](/docs/design-apis/specifications/generate-collections/#sync-changes-to-a-specification) from the collection back to the specification, Postman preserves the original reference URL if the values are unchanged. If you change values in the collection that originated from a referenced component, syncing those updates causes Postman to replace the reference URL with the updated inline values.

Learn more about:

- [Creating organization teams and workspaces](/docs/administration/organization/create/)
- [Organization roles](/docs/administration/organization/roles/)
- [Organization settings](/docs/administration/organization/settings/)

---

**Note:** You can't delete component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your teams can continue to edit workspace details as their workspaces, collections, and APIs evolve.

To learn more, see [Edit workspace details](/docs/administration/managing-your-team/secret-scanner/how-secret-scanner-works).

---

**Note:** You can't delete published versions of component files.

### View live documentation

Postman displays a live preview of your API's documentation if you're editing an OpenAPI 3.0 or AsyncAPI 2.0 specification.

To view the documentation preview, do the following:

1. Under **Workspace description**, add a description.
2. Under **About**, add a summary.
3. Under **Tags**, add tags.

Your