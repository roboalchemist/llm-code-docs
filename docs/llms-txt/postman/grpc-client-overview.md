# grpc-client-overview

Manage gRPC APIs using Postman
=============================

Postman can make requests using _gRPC_, a schema-driven Remote Procedure Call (RPC) framework often used to enable inter-service communication. Using a gRPC request, you can view supported services and methods (with a service definition), invoke the method of your interest, send a message payload, view the response from the server, and save example responses without entering commands in the terminal or writing any code.

Because it's RPC-based, gRPC facilitates client-server communication over a function call and provides easier abstraction than HTTP, support across multiple languages, and high performance.

gRPC uses [protobuf (protocol buffers)](https://developers.google.com/protocol-buffers/docs/overview) as the Interface Definition Language (IDL) to define the API interface (service definition). This definition serves as a contract between the client and the server that specifies the supported services and methods.

Postman's [gRPC client interface](/docs/sending-requests/grpc/grpc-request-interface/) enables you to use and test your gRPC requests. You can also [manage your service definitions](/docs/sending-requests/grpc/using-service-definition/) and [save gRPC example request-response pairs](/docs/sending-requests/grpc/using-grpc-examples/) for testing and demonstration purposes.

Postman also enables you to use scripts to write API tests, debug your gRPC requests, and dynamically read or update the values of variables. For more information, see [Test and debug values in gRPC requests using JavaScript in Postman](/docs/sending-requests/grpc/scripting-in-grpc-request/). You can also [use a mock server](/docs/sending-requests/grpc/using-grpc-mock/) to simulate the behavior of a real API by returning sample data for gRPC requests to the API endpoints.

### Postman Vault integrations

**[Postman Vault integrations are available with Postman Enterprise plans with the Advanced Security Administration add-on.](https://www.postman.com/pricing/)**

[Postman Vault integrations](/docs/sending-requests/postman-vault/postman-vault-integrations/) enable you to link vault secrets with secrets that are stored in an external vault. You can then reference vault secrets in your Postman team, and retrieve the value of external vault secrets using end-to-end encryption when you send HTTP requests. You can [manage and update](/docs/sending-requests/postman-vault/manage-postman-vault-integrations/) your Postman Vault integrations.

Postman supports the following Postman Vault integrations:

*   [1Password](/docs/sending-requests/postman-vault/1password/)
*   [AWS Secrets Manager](/docs/sending-requests/postman-vault/aws-secrets-manager/)
*   [Azure Key Vault](/docs/sending-requests/postman-vault/azure-key-vault/)
*   [HashiCorp Vault](/docs/sending-requests/postman-vault/hashicorp-vault/)

You can create Postman Vault integrations from the [Postman desktop app](/docs/getting-started/installation/installation-and-updates/#use-the-postman-desktop-app).

### Feature availability

The following features require the Postman desktop app:

*   **Open Postman Vault from public workspaces** - You must use the Postman desktop app to open your Postman Vault from a [public workspace](/docs/collaborating-in-postman/using-workspaces/public-workspaces/).
*   **Create and manage Postman Vault integrations** ([Enterprise teams only](https://www.postman.com/pricing/))
*   **Create and manage Postman Vault integrations** ([Enterprise teams only](https://www.postman.com/pricing/))

### Troubleshoot vault secrets

Postman's Local Secret Protection is available with [Postman Enterprise plans](https://www.postman.com/pricing/).

With the Secret Scanner's Local Secret Protection, [Team Admins](/docs/administration/roles-and-permissions/#team-roles) can configure where Postman stores the team's exposed secrets in the workspaces or types of workspaces you've defined.

When [enabled](#enable-local-secret-protection), Postman scans secrets in real time and takes action, storing exposed secrets, like API keys, JWT tokens, or auth tokens, in the [Postman Vault](/docs/sending-requests/postman-vault/postman-vault-secrets/). The Postman Vault stores your exposed secrets securely on your device. The original secret value is replaced with a vault secret reference. This prevents your team's secrets from syncing to the Postman cloud and gives you greater control over your team's security posture and compliance requirements.

Postman's Local Secret Protection actively scans for secrets in the following Postman elements when changes are made:

*   HTTP collections
*   Environments variable values
*   Global variable values

Local Secret Protection requires Postman version 11.71.3 or later.

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Select **No policy** or the **Move to vault** policy for the **Public**, **Partner**, and **Internal** workspace types.
3.  Click **Save**.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces, and all new workspaces automatically inherit the policy you choose.

You can reset the policy for workspaces to their default, do the following:

1.  Click **Set default policies**.
2.  Click **Reset Workspaces**.
3.  Review the listed changes to each workspace type (**Public**, **Partner**, and **Internal**).
4.  Click **Apply to all** to confirm your changes. This resets all workspaces to use the default policy for the displayed workspace types and removes any custom overrides.

### Update secret protection policies

To update a workspace's secret protection policy, do one of the following:

*   To update the policy of a single workspace, select a policy from the **Policy** dropdown list next to the workspace.
*   To update the policy of multiple workspaces, select the workspaces or select the checkbox next to the **Workspace** column, then select a policy from **Select policy** dropdown list.

By default, only the first 50 workspaces are listed. To select all workspaces or workspaces of the selected type, click **Select all workspaces within team**.

The policy you select is automatically applied to the selected workspaces.

### View secret scan metrics

The **Local Protection** report in the Secret Scanner's **Reports** dashboard enables your Team Admins to view Local Secret Protection metrics. This includes automatic resolutions and user-requested overrides.

To access the report, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Reports** tab.

The report provides metrics about the Secret Scanner's real-time secret management in a given period of time, such as:

*   The total number of detected secrets automatically moved to the Postman Vault.
*   The total number of user Secret Scanner policy overrides. Team Admins can click the number of overrides in the **Secrets Count** column to view details about override justifications created by users.

Learn more about [the Secret Scanner dashboard](/docs/reports/secret-scanner-reports/).

### Enable Local Secret Protection

To enable Local Secret Protection in Postman, do the following:

1.  Click **Team > Team Settings** in the Postman header, then click **Secret Scanner** in the left sidebar.
2.  In **Secret Scanner**, select the **Local Protection** tab.
3.  Turn on **Local secret protection**.

Once enabled, you can configure how Postman stores exposed secrets in your team's workspaces. By default, all workspaces use the **No policy** option and store detected secrets in the Postman cloud. However, Team Admins can change the [default storage behavior](#set-default-protection-policies-for-new-workspaces).

Users can't turn off secret policies, but can submit justifications to Team Admins to override any detected secrets.

### Set default protection policies for new workspaces

You can customize how Local Secret Protection manages exposed secrets in your team's workspaces. Define a policy for specific types of workspaces