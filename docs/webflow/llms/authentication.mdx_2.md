# Source: https://developers.webflow.com/cli/authentication.mdx

***

title: Authenticate with Webflow
slug: authentication
description: Learn about authentication options for the Webflow CLI.
hidden: false
subtitle: Learn about authentication options for the Webflow CLI.
-----------------------------------------------------------------

To access some Webflow resources via the CLI, you'll need to authenticate with your Webflow account.

The Webflow CLI supports two types of authentication for different products:

| Authentication method        | Description                                                                          | Supported products         |
| ---------------------------- | ------------------------------------------------------------------------------------ | -------------------------- |
| **Site authentication**      | Authenticate a single site. This is the default CLI method.                          | DevLink<br />Webflow Cloud |
| **Workspace authentication** | Authenticate with your Webflow workspace to deploy components to a single workspace. | Code Components            |

## Site authentication

Authenticate with your Webflow account to access site-specific resources:

```bash
webflow auth login
```

This command opens your browser to authenticate with Webflow, where you can grant access to one or more sites.

After you've authenticated, the CLI will prompt you in your terminal to select a specific site for your current project. It will then create or update an `.env` file in your project's root with the `WEBFLOW_SITE_ID` and `WEBFLOW_API_TOKEN` for the site you selected.

```bash title=".env"
WEBFLOW_SITE_ID=your-site-id
WEBFLOW_SITE_API_TOKEN=your-api-token
```

<Accordion title="Can I use site authentication for multiple sites?">
  No, you can only use site authentication for a single site. If you need to authenticate with multiple sites, you'll need to re-authenticate for each site.
</Accordion>

## Workspace authentication

<Warning title="Workspace authentication is only available for Code Components" />

On initial deployment of a Code Component library, you'll be prompted to authenticate with Webflow to deploy components to a single workspace.

```bash
webflow library share
```

If not already authenticated, this command will open a browser window to authenticate your Webflow workspace. After you grant access, the CLI will create or update a `.env` file in your project's root with the `WEBFLOW_WORKSPACE_ID` and `WEBFLOW_WORKSPACE_API_TOKEN`.

```bash title=".env"
WEBFLOW_WORKSPACE_ID=your-workspace-id
WEBFLOW_WORKSPACE_API_TOKEN=your-api-token
```

<Warning title="Include .env in your .gitignore file">
  Never commit your `.env` file to version control. Be sure to add `.env` to your `.gitignore` file.
</Warning>

### Non-Interactive authentication (for CI/CD)

For automated environments like CI/CD pipelines, you can authenticate non-interactively by passing a Workspace API token directly with the `--api-token` flag. This method bypasses the standard `webflow auth login` flow and is primarily used with the `webflow library share` command.

To deploy a component library to multiple workspaces, generate a unique Workspace API token for each one from your Workspace settings. Then, run the `share` command for each workspace, passing the corresponding token.

**Examples**

```bash
# Deploy to a single workspace using a token
webflow library share --api-token <WORKSPACE_1_API_TOKEN> --no-input

# Deploy the same library to a different workspace
webflow library share --api-token <WORKSPACE_2_API_TOKEN> --no-input
```

<Accordion title="Can I authenticate multiple workspaces?">
  To authenticate with multiple workspaces, you'll need to create your own Workspace API token for each workspace. Then you can use the `--api-token` option to share your library to each workspace.
</Accordion>

<Accordion title="Who can authenticate a workspace?">
  Any user within the workspace can authenticate via the CLI to deploy components to the workspace. However, only Workspace Admins can create a Workspace API token from the settings page in the Workspace dashboard.
</Accordion>

<Accordion title="What is a Workspace API token?">
  [Workspace API tokens](/data/reference/authentication/workspace-token) provide access to workspace-specific resources via the Webflow Data API. They're used to authenticate the CLI when running the `webflow library share` command.
</Accordion>
