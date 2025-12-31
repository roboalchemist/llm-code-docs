# Source: https://mintlify.com/docs/installation.md

# CLI installation

> Use the CLI to preview docs locally, test changes in real-time, and catch issues before deploying your documentation site.

<img className="block dark:hidden my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ffd8bc88d87fc00fe1919a33a292fa01" alt="Decorative graphic representing the CLI." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/installation/local-development-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=511ef7cd18fd4fb900f2701d062ca11b 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3d88dd1c1b9502ecf779bae2a125bfa0 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b5c7231e4a48c366bc9fadc00ad67fc2 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=43e8d5fa61bcd586ccece993dc0c3f4d 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c06a3f73ae2ed6cc36cfc6a15a539baf 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6a946dbec95af5df7dc3f71daf25fed5 2500w" />

<img className="hidden dark:block my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ef0bb527eb258f8d720180d106ea6625" alt="Decorative graphic representing the CLI." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/installation/local-development-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b6ab6647def97748df5303d2add7877c 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=83a49f961c12baf9aa9755d972160915 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9f44e898560aaa47af54ff0f6079ca6e 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1bc3413b87f72bb848de2a518cf16c3a 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9b79a51b960489e0d41ffd61b9d7120d 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/installation/local-development-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=db35248ff88939a314d4ecc547ffd463 2500w" />

Use the CLI to preview your documentation locally as you write and edit. View changes in real-time before deploying, test your documentation site's appearance and functionality, and catch issues like broken links or accessibility problems.

The CLI also has utilities for maintaining your documentation, including commands to rename files, validate OpenAPI specifications, and migrate content between formats.

## Install the CLI

<Info>
  **Prerequisite**: The CLI requires [Node.js](https://nodejs.org/en) v19 through v24. LTS versions are preferred.
</Info>

Run the following command to install the [CLI](https://www.npmjs.com/package/mint):

<CodeGroup>
  ```bash npm theme={null}
  npm i -g mint
  ```

  ```bash pnpm theme={null}
  pnpm add -g mint
  ```
</CodeGroup>

## Preview locally

To generate a local preview, navigate to your documentation directory (where your `docs.json` file is located) and run the following command:

```bash  theme={null}
mint dev
```

A local preview of your documentation is available at `http://localhost:3000`.

Alternatively, if you do not want to install the CLI globally, you can run a one-time script:

```bash  theme={null}
npx mint dev
```

### Custom ports

By default, the CLI uses port 3000. You can customize the port using the `--port` flag. To run the CLI on port 3333, for instance, use this command:

```bash  theme={null}
mint dev --port 3333
```

If you attempt to run on a port that is already in use, it will use the next available port:

```mdx  theme={null}
Port 3000 is already in use. Trying 3001 instead.
```

### Preview as a specific group

If you use partial authentication to restrict access to your documentation, you can preview as a specific authentication group by using the `--groups [groupname]` flag.

For example, if you have a group named `admin`, you can preview as a member of that group with the command:

```bash  theme={null}
mint dev --groups admin
```

## Create a new project

To create a new documentation project, run the following command:

```bash  theme={null}
mint new [directory]
```

This command clones the [starter kit](https://github.com/mintlify/starter) into a specified directory. If no directory is specified, the CLI tool prompts you to create a new subdirectory or overwrite the current directory.

<Warning>
  If you overwrite the current directory, any existing files in the directory will be deleted.
</Warning>

The CLI tool prompts you for a project name and [theme](/customize/themes) to finish setting up your project.

You can run `mint new` with the following flags:

* `--theme`: Set the theme of the new project.
* `--name`: Set the name of the new project.
* `--force`: Overwrite the current directory if it already exists.

For example, to create a new project in the `docs` directory with the name `my-project` and the theme `linden`, run the following command:

```bash  theme={null}
mint new docs --name my-project --theme linden
```

## Update the CLI

If your local preview is out of sync with what you see on the web in the production version, update your local CLI:

```bash  theme={null}
mint update
```

If this `mint update` command is not available on your local version, re-install the CLI with the latest version:

<CodeGroup>
  ```bash npm theme={null}
  npm i -g mint@latest
  ```

  ```bash pnpm theme={null}
  pnpm add -g mint@latest
  ```
</CodeGroup>

## Additional commands

### Find broken links

Identify any broken internal links with the following command:

```bash  theme={null}
mint broken-links
```

### Find accessibility issues

Test the color contrast ratios and search for missing alt text on images and videos in your documentation with the following command:

```bash  theme={null}
mint a11y
```

### Check OpenAPI spec

Check your OpenAPI file for errors with the following command:

```bash  theme={null}
mint openapi-check <OpenAPI filename or URL>
```

Pass a filename (for example, `./openapi.yaml`) or a URL (for example, `https://petstore3.swagger.io/api/v3/openapi.json`).

### Rename files

Rename and update all references to files with the following command:

```bash  theme={null}
mint rename <path/to/old-filename> <path/to/new-filename>
```

### Migrate MDX endpoint pages

Migrate MDX endpoint pages to autogenerated pages from your OpenAPI specification with the following command:

```bash  theme={null}
mint migrate-mdx
```

This command converts individual MDX endpoint pages to autogenerated pages defined in your `docs.json`, moves MDX content to the `x-mint` extension in your OpenAPI specification, and updates your navigation. See [Migrating from MDX](/guides/migrating-from-mdx) for detailed information.

## Formatting

While developing locally, we recommend using extensions in your IDE to recognize and format `MDX` files.

If you use Cursor, Windsurf, or VS Code, we recommend the [MDX VS Code extension](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx) for syntax highlighting, and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for code formatting.

If you use JetBrains, we recommend the [MDX IntelliJ IDEA plugin](https://plugins.jetbrains.com/plugin/14944-mdx) for syntax highlighting, and setting up [Prettier](https://prettier.io/docs/webstorm) for code formatting.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error: Could not load the &#x22;sharp&#x22; module using the darwin-arm64 runtime">
    This may be due to an outdated version of node. Try the following:

    1. Remove the currently-installed version of the mint CLI: `npm uninstall -g mint`
    2. Upgrade to Node.js.
    3. Reinstall the mint CLI: `npm install -g mint`
  </Accordion>

  <Accordion title="Issue: Encountering an unknown error">
    **Solution**: Go to the root of your device and delete the `~/.mintlify` folder. Afterwards, run `mint dev` again.
  </Accordion>

  <Accordion title="Error: permission denied">
    This is due to not having the required permissions to globally install node packages.

    **Solution**: Try running `sudo npm i -g mint`. You will be prompted for your password, which is the one you use to unlock your computer.
  </Accordion>

  <Accordion title="The local preview doesn't look the same as my docs do on the web">
    This is likely due to an outdated version of the CLI.

    **Solution:** Run `mint update` to get the latest changes.
  </Accordion>

  <Accordion title="mintlify vs. mint package">
    If you have any problems with the CLI package, you should first run `npm ls -g`. This command shows what packages are globally installed on your machine.

    If you don't use npm or don't see it in the -g list, try `which mint` to locate the installation.

    If you have a package named `mint` and a package named `mintlify` installed, you should uninstall `mintlify`.

    1. Uninstall the old package:

    ```bash  theme={null}
      npm uninstall -g mintlify
    ```

    2. Clear your npm cache:

    ```bash  theme={null}
      npm cache clean --force
    ```

    3. Reinstall the new package:

    ```bash  theme={null}
    npm i -g mint
    ```
  </Accordion>
</AccordionGroup>
