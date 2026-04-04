# Source: https://docs.base44.com/developers/references/cli/commands/site-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# site deploy

> Deploy built site files to Base44 hosting

Deploy your built frontend app to Base44's hosting platform. The command uploads your build output to Base44, making your site available at your app's URL.

Before running this command, ensure that your built frontend files are in the directory specified by `site.outputDirectory` in your [`config.jsonc`](/developers/backend/overview/project-structure#config-jsonc) file.

## Usage

```bash  theme={null}
base44 site deploy
```

## Flags

| Flag        | Description                  |
| ----------- | ---------------------------- |
| `-y, --yes` | Skip the confirmation prompt |

## Configuration

The `site.outputDirectory` in your [`base44/config.jsonc`](/developers/backend/overview/project-structure) tells the CLI where your build tool outputs the compiled frontend files so that it knows which files to deploy to Base44 hosting.

```jsonc  theme={null}
{
  "name": "my-project",
  "site": {
    "outputDirectory": "./dist"
  }
}
```

## See also

* [`site open`](/developers/references/cli/commands/site-open): Open the deployed site in your browser
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [Quickstart - React](/developers/backend/quickstart/templates/quickstart-react-template): Build a full-stack React app with Base44


Built with [Mintlify](https://mintlify.com).