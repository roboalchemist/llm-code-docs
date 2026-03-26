# Source: https://momentic.ai/docs/mobile-cli/commands/install-browsers.md

# Source: https://momentic.ai/docs/cli/commands/install-browsers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# install-browsers

Install browsers for your Momentic tests. Here are the
[supported browsers](/browsers).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers [options] [browsers...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers [options] [browsers...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers [options] [browsers...]
  ```
</CodeGroup>

* **\[browsers...]**: The browsers to install. You can specify multiple browsers
  separated by spaces. Available browsers are `chromium`, `chrome`, and
  `chrome-for-testing`. You can review the differences between each browser
  [here](/browsers).

## Options

### `--force`

Force the installation of the specified browsers, even if they are already
installed.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers chromium --force
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers chromium --force
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers chromium --force
  ```
</CodeGroup>

### `--all`

Install all supported browsers. This is equivalent to specifying `chromium`,
`chrome`, and `chrome-for-testing`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers --all
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers --all
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers --all
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).