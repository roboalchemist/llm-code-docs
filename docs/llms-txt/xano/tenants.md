# Source: https://docs.xano.com/xano-cli/tenants.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenants

> Manage tenants, deployments, environments, and backups from the CLI

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

Tenants are isolated environments within a workspace, each with their own infrastructure, data, and configuration. The CLI provides full lifecycle management for tenants and their backups.

<Note>
  Tenant commands require a workspace ID, either from your profile or via the `-w` flag. Most tenant commands identify tenants by their **name** (e.g., `t1234-abcd-xyz1`), not a numeric ID.
</Note>

## CRUD

### List Tenants

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant list
  ```
</BrowserFrame>

Use `-o json` for the full JSON response.

### Get Tenant Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant get TENANT_NAME
  ```
</BrowserFrame>

### Create a Tenant

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant create "My Tenant"
  ```
</BrowserFrame>

| Argument / Flag  | Description                                        |
| ---------------- | -------------------------------------------------- |
| `display`        | Display name (required, positional)                |
| `-d`             | Description                                        |
| `--license`      | License tier: `tier1` (default), `tier2`, `tier3`  |
| `--cluster_id`   | Cluster ID (required for tier2/tier3)              |
| `--platform_id`  | Platform ID to use                                 |
| `--domain`       | Custom domain                                      |
| `--ephemeral`    | Mark tenant as ephemeral (allows push operations)  |
| `--[no-]ingress` | Enable/disable ingress (default: enabled)          |
| `--[no-]tasks`   | Enable/disable background tasks (default: enabled) |
| `-w`             | Workspace ID                                       |
| `-o`             | Output format: `summary` or `json`                 |

### Edit a Tenant

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant edit TENANT_NAME --display "New Name" -d "Updated description"
  ```
</BrowserFrame>

Additional flags: `--domain`, `--proxy`, `--[no-]ingress`, `--[no-]tasks`, `--[no-]rbac`.

### Delete a Tenant

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant delete TENANT_NAME
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.

<Warning>
  Deleting a tenant destroys all associated infrastructure and data. This cannot be undone.
</Warning>

***

## Impersonate

Open a tenant's dashboard in your browser, or retrieve the impersonation URL for scripting.

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant impersonate TENANT_NAME
  ```
</BrowserFrame>

Print the URL without opening the browser:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant impersonate TENANT_NAME --url-only
  ```
</BrowserFrame>

Output credentials as JSON:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant impersonate TENANT_NAME -o json
  ```
</BrowserFrame>

***

## Pull & Push

You can pull a tenant's content down as local XanoScript files, or push local files to a tenant. This works the same way as [workspace pull & push](/xano-cli/push-pull), but targets a specific tenant.

### Pull a Tenant

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant pull ./my-tenant -t TENANT_NAME
  ```
</BrowserFrame>

| Flag        | Description                         |
| ----------- | ----------------------------------- |
| `-t`        | Tenant name (required)              |
| `--env`     | Include environment variables       |
| `--records` | Include database records            |
| `--draft`   | Include draft versions of resources |
| `-w`        | Workspace ID                        |

### Push to a Tenant

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant push ./my-tenant -t TENANT_NAME
  ```
</BrowserFrame>

| Flag           | Description                                 |
| -------------- | ------------------------------------------- |
| `-t`           | Tenant name (required)                      |
| `--no-records` | Skip importing table records                |
| `--no-env`     | Skip overwriting environment variables      |
| `--truncate`   | Truncate all table records before importing |
| `-w`           | Workspace ID                                |

***

## Deployments

### Deploy a Release

Deploy a release to a tenant by name:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant deploy_release TENANT_NAME --release v1.0
  ```
</BrowserFrame>

### Deploy a Platform

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant deploy_platform TENANT_NAME --platform_id 5
  ```
</BrowserFrame>

***

## Tenant License

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  # Get tenant license
  xano tenant license get TENANT_NAME

  # Set tenant license
  xano tenant license set TENANT_NAME --license tier2
  ```
</BrowserFrame>

***

## Tenant Environment Variables

Manage environment variables on a per-tenant basis.

### List Env Var Keys

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env list TENANT_NAME
  ```
</BrowserFrame>

### Get a Single Env Var

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env get TENANT_NAME --name DATABASE_URL
  ```
</BrowserFrame>

### Set an Env Var

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env set TENANT_NAME --name DATABASE_URL --value "postgres://..."
  ```
</BrowserFrame>

### Delete an Env Var

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env delete TENANT_NAME --name DATABASE_URL
  ```
</BrowserFrame>

### Export All Env Vars

Export all environment variables to a YAML file:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env get_all TENANT_NAME
  xano tenant env get_all TENANT_NAME --file ./env.yaml
  ```
</BrowserFrame>

### Import All Env Vars

Import environment variables from a YAML file (replaces existing):

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant env set_all TENANT_NAME
  xano tenant env set_all TENANT_NAME --file ./env.yaml --clean
  ```
</BrowserFrame>

***

## Tenant Backups

### List Backups

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup list TENANT_NAME
  ```
</BrowserFrame>

Use `--page` for pagination.

### Create a Backup

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup create TENANT_NAME
  ```
</BrowserFrame>

### Restore from a Backup

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup restore TENANT_NAME --backup_id 10
  ```
</BrowserFrame>

You'll be asked to confirm before the restore proceeds. Use `-f` to skip confirmation.

<Warning>
  Restoring a backup replaces the current tenant data entirely.
</Warning>

### Export a Backup

Download a backup as a `.tar.gz` file:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup export TENANT_NAME --backup_id 10
  ```
</BrowserFrame>

Specify a custom output path with `--output`:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup export TENANT_NAME --backup_id 10 --output ./backups/my-backup.tar.gz
  ```
</BrowserFrame>

### Import a Backup

Import a backup file into a tenant:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup import TENANT_NAME --file ./my-backup.tar.gz
  ```
</BrowserFrame>

### Delete a Backup

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant backup delete TENANT_NAME --backup_id 10
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.

***

## Clusters

Manage tenant clusters for multi-tenant deployments.

### List Clusters

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant cluster list
  ```
</BrowserFrame>

### Get Cluster Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant cluster get CLUSTER_ID
  ```
</BrowserFrame>

### Create a Cluster

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant cluster create --name "us-east-1" --credentials_file ./kubeconfig.yaml
  ```
</BrowserFrame>

| Flag                 | Description                  |
| -------------------- | ---------------------------- |
| `--name`             | Cluster name (required)      |
| `--credentials_file` | Path to kubeconfig YAML file |
| `--type`             | Cluster type (e.g., `run`)   |
| `-d`                 | Description                  |

### Edit a Cluster

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant cluster edit CLUSTER_ID --name "us-east-1" -d "Updated" --domain "us-east.xano.io"
  ```
</BrowserFrame>

### Delete a Cluster

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano tenant cluster delete CLUSTER_ID
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.

### Cluster License (Kubeconfig)

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  # Get cluster kubeconfig
  xano tenant cluster license get CLUSTER_ID

  # Set cluster kubeconfig
  xano tenant cluster license set CLUSTER_ID --file ./kubeconfig.yaml
  ```
</BrowserFrame>


Built with [Mintlify](https://mintlify.com).