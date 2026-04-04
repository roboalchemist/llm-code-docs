# Run a collection using the Postman CLI

You can use the [Postman CLI](/docs/postman-cli/postman-cli-overview/) to manually run collections to test the functionality of your API. You can also use the Postman CLI to automate collection runs in CI/CD pipelines.

> Postman supports running HTTP collections. You can't run multi-protocol collections.

When the Postman CLI runs a collection, the collection and its tests run locally, and the results are sent to the Postman cloud using an API call.

> The Postman CLI doesn't support OAuth 2.0 authentication. To learn how to use an OAuth 2.0 token with the Postman CLI, see [OAuth 2.0 overview](/docs/sending-requests/authorization/oauth-20/#oauth-20-overview).

## Run a collection locally with the Postman CLI

You can use the Postman CLI to run the requests in a [collection](/docs/collections/use-collections/create-collections/) or a [folder](/docs/collections/use-collections/manage-collections/#add-folders-to-a-collection).

1. [Download and install the Postman CLI](/docs/postman-cli/postman-cli-installation/).
2. Click **Collections** in the sidebar and select the collection or folder you want to run.
3. Click ![Image 1: Runner icon](https://assets.postman.com/postman-docs/icon-runner-v9.jpg#icon) **Run**.
4. ![Image 2: Select Run from the collection overview](https://assets.postman.com/postman-docs/v11/collection-runner-button-v11.jpg)
5. On the **Functional** tab, click **Automate runs via CLI**.
6. ![Image 3: Automate runs using the Postman CLI](https://assets.postman.com/postman-docs/v11/pcli-automate-cli-v11-19.jpg)

    If you're running a [collection linked to an API](/docs/design-apis/api-builder/develop-apis/adding-api-elements/) that's connected to a [Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/), replace the collection ID with the path to the collection file in your remote repository.

7. Under **Run on Postman CLI**, click **Add API Key**. Do one of the following:
    
    * Click **Generate Key** to create a new API key. Enter a name for the API key and click **Generate**. Click ![Image 4: Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy** to copy the key and save it somewhere safe.
    * Click **Use Existing Key** and enter a valid API key.
    
8. Click **Insert Key**.
9. Click ![Image 5: Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy** to copy the commands.
10. Paste and run the commands in your terminal. After running the commands, the Postman CLI outputs a run report and a link to the run results in Postman.

    In the run report, `test-scripts` refers to [post-response scripts](/docs/tests-and-scripts/write-scripts/test-scripts/).

11. Follow the link to check the results in Postman.

    ![Image 6: Postman CLI view collection run results](https://assets.postman.com/postman-docs/v11/postman-cli-view-run-data-v11-19.jpg)

## Run a collection in CI/CD

When the collection runs to your satisfaction, you can copy the commands into your CI/CD script to integrate them into your workflows. When adding the commands to your CI/CD script, you may want to replace the API key with a variable.

To run a collection in CI/CD, do the following:

1. Click **Collections** in the sidebar and select the collection or folder you want to run.
2. Click ![Image 7: Runner icon](https://assets.postman.com/postman-docs/icon-runner-v9.jpg#icon) **Run**.
3. ![Image 8: Select Run from the collection overview](https://assets.postman.com/postman-docs/v11/collection-runner-button-v11.jpg)
4. On the **Functional** tab, click **Automate runs via CLI**.
5. ![Image 9: Automate runs using the Postman CLI](https://assets.postman.com/postman-docs/v11/pcli-automate-cli-v11-19.jpg)

    If you're running a [collection linked to an API](/docs/design-apis/api-builder/develop-apis/adding-api-elements/) that's connected to a [Git repository](/docs/design-apis/api-builder/versioning-an-api/overview/), replace the collection ID with the path to the collection file in your remote repository.

6. Under **Run on CI/CD**, click **Configure command**.
7. Click a **Collection** to run during pipeline builds. You can also select an **Environment** to use.
8. If needed, click ![Image 10: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon) **Add Another Collection** to select more collections to run.
9. Click the **CI/CD Provider** and **Operating system** for your CI/CD pipeline.
10. To copy the Postman CLI configuration, click ![Image 11: Copy icon](https://assets.postman.com/postman-docs/aether-icons/action-copy-stroke.svg#icon) **Copy** or **Copy Postman CLI Command**.
11. Add the Postman CLI configuration to your CI/CD script. This process depends on your CI tool.

## Run a collection in a specific order

By default, when you generate the command to run a collection from the Collection Runner, a single Collection ID for the collection is specified. This runs the folders and requests in that collection in the sequence they're listed in the collection.

If you need to change the request order, select a request in the Collection Runner and drag it to its new location in the order. You can also remove an individual request from the run by clearing the checkbox next to its name.

When you change the folder and request sequence, the generated command also changes. In addition to the Collection ID, the generated command specifies a number of folder and request UIDs with the `-i` option. This runs each of the folders or requests in that specified order.

## Run a collection that uses test data files

The Postman CLI can't run requests that use files in your local [working directory](/docs/getting-started/installation/settings/#working-directory) to send [body data](/docs/sending-requests/create-requests/parameters/). If your collection has requests that use files, [upload your test data files](/docs/sending-requests/create-requests/test-data/) to make them available to the Postman CLI.

## Run a collection that uses packages

> Using the Postman CLI to run packages from your team's Postman Package Library is available with [Postman Professional and Enterprise plans](https://www.postman.com/pricing/).

You can use the Postman CLI to run collections with scripts that import packages from your team's [package library](/docs/tests-and-scripts/write-scripts/packages/package-library/). Learn how to [add packages](/docs/tests-and-scripts/write-scripts/packages/package-library/#add-a-package) to the package library, and [import packages](/docs/tests-and-scripts/write-scripts/packages/package-library/#import-a-package) into your scripts.

You can also use the Postman CLI to run collections that [import external packages](/docs/tests-and-scripts/write-scripts/packages/external-package-registries/) from npm or JSR package registries.

> Postman's Local Secret Protection is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

With the Secret Scanner's Local Secret Protection, [Team Admins](/docs/administration/roles-and-permissions/#team-roles) can configure where Postman stores the team's exposed secrets in the workspaces or types of workspaces you've defined.

When [enabled](#enable-local-secret-protection), Postman scans secrets in real time and takes action, storing exposed secrets, like API keys, JWT tokens, or auth tokens, in the [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/). The Postman Vault stores your exposed secrets securely on your device. The original secret value is replaced with a vault secret reference. This prevents your team's secrets from syncing to the Postman cloud and gives you greater control over your team's security posture and compliance requirements.

Postman's Local Secret Protection actively scans for secrets in the following Postman elements when changes are made:

* HTTP collections
* Environments variable values
* Global variable values

> Local Secret Protection requires Postman version 11.71.3 or later.

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 12: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 13: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 14: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 15: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 16: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 17: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 18: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3. Click **Save**.

![Image 19: Set default detection policies for workspace types](https://assets.postman.com/postman-docs/v11/local-secret-detection-set-default-policy-11-1.jpg)

To reset the policy for workspaces to their default, do the following:

1. Click **Set default policies**.
2. Click **Reset Workspaces**.
3. Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4. Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

* To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
* To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

    By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

> The policy you select is automatically applied to the selected workspaces.

## View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

* The total number of detected secrets automatically moved to the Postman Vault.
* The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

## Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1. Click **Team** in the Postman header, then select **Secret Scanner** in the left sidebar.
2. In **Secret Scanner**, select the **Local Protection** tab.
3. Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

> This only applies to workspaces created after you set a policy. To apply the policy to existing workspaces, [update their policy](#update-secret-protection-policies).

To set default policies by workspace types, do the following:

1. Click **Set default policies**.
2. Select **No policy**