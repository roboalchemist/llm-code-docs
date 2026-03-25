# Source: https://docs.xano.com/xano-cli/releases.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Releases

> Create, manage, and deploy releases from the CLI

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

Releases are versioned snapshots of a workspace branch that can be deployed to tenants. They enable controlled rollouts and version management across your tenant infrastructure.

<Note>
  Release commands require a workspace ID, either from your profile or via the `-w` flag. All release commands use **release names** (e.g., `v1.0`), not IDs.
</Note>

## List Releases

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release list
  ```
</BrowserFrame>

Use `-o json` for the full JSON response.

## Get Release Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release get v1.0
  ```
</BrowserFrame>

## Create a Release

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release create -n "v1.0" -b v1
  ```
</BrowserFrame>

| Flag          | Description                                  |
| ------------- | -------------------------------------------- |
| `-n`          | Release name (required)                      |
| `-b`          | Branch to create the release from (required) |
| `-d`          | Release description                          |
| `--hotfix`    | Mark as a hotfix release                     |
| `--table-ids` | Comma-separated table IDs to include         |
| `-w`          | Workspace ID                                 |
| `-o`          | Output format: `summary` or `json`           |

## Edit a Release

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release edit v1.0 -n "v1.0-final" -d "Updated description"
  ```
</BrowserFrame>

## Delete a Release

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release delete v1.0
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.

<Warning>
  Deleting a release is permanent and cannot be undone.
</Warning>

## Export a Release

Download a release as a `.tar.gz` file:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release export v1.0
  ```
</BrowserFrame>

By default, the file is saved in the current directory. Specify a custom path with `--output`:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release export v1.0 --output ./backups/my-release.tar.gz
  ```
</BrowserFrame>

## Import a Release

Import a previously exported release file into a workspace:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release import --file ./my-release.tar.gz
  ```
</BrowserFrame>

***

## Pull & Push

You can pull a release down as local XanoScript files, or push local files as a new release. This works the same way as [workspace pull & push](/xano-cli/push-pull), but targets a specific release instead of a branch.

### Pull a Release

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release pull ./my-release -r v1.0
  ```
</BrowserFrame>

| Flag        | Description                   |
| ----------- | ----------------------------- |
| `-r`        | Release name (required)       |
| `--env`     | Include environment variables |
| `--records` | Include database records      |
| `-w`        | Workspace ID                  |

### Push as a New Release

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano release push ./my-release -n "v2.0"
  ```
</BrowserFrame>

| Flag           | Description                  |
| -------------- | ---------------------------- |
| `-n`           | Release name (required)      |
| `-d`           | Release description          |
| `--hotfix`     | Mark as a hotfix release     |
| `--no-records` | Skip importing table records |
| `--no-env`     | Skip environment variables   |
| `-w`           | Workspace ID                 |


Built with [Mintlify](https://mintlify.com).