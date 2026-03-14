# Source: https://docs.mage.ai/integrations/databases/PowerBI.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Power BI

export const ProOnly = ({button = 'Get started for free', description = 'Try our fully managed solution to access this advanced feature.', source = 'documentation', title = 'Only in Mage Pro.'}) => <a href={`https://cloud.mage.ai/sign-up?source=${source}`} className="block my-4 px-5 py-4 overflow-hidden rounded-xl flex gap-3 border border-emerald-500/20 bg-emerald-50/50 dark:border-emerald-500/30 dark:bg-emerald-500/10" target="_blank">
    <div style={{
  display: 'flex',
  alignItems: 'center',
  width: '100%'
}}>
      <div className="text-sm prose min-w-0 text-emerald-900 dark:text-emerald-200" style={{
  flex: 1
}}>
        {title}
        <p className="normal">{description}</p>
      </div>

      <div> </div>

      <div>
        <ProButton label={button} href={`https://cloud.mage.ai/sign-up?source=${source}`} />
      </div>
    </div>
  </a>;

export const ProButton = ({href, label = 'Get started with Mage Pro for free', source = 'documentation'}) => <div style={{
  height: 32,
  position: 'relative'
}}>
    <a target="_blank" className="group px-4 py-1.5 relative inline-flex items-center text-sm font-medium rounded-full" href={href ?? `https://cloud.mage.ai/sign-up?source=${source}`}>
      <span className="absolute inset-0 bg-primary-dark dark:bg-primary-light/10 border-primary-light/30 rounded-full dark:border group-hover:opacity-[0.9] dark:group-hover:border-primary-light/60">
      </span>

      <div className="mr-0.5 space-x-2.5 flex items-center">
        <span class="z-10 text-white dark:text-primary-light">
          {label}
        </span>

        <svg width="3" height="24" viewBox="0 -9 3 24" class="h-5 rotate-0 overflow-visible text-white/90 dark:text-primary-light">
          <path d="M0 0L3 3L0 6" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path>
        </svg>
      </div>
    </a>
  </div>;

<ProOnly source="powerbi" />

## Add credentials

1. Create a new pipeline or open an existing pipeline.
2. Expand the left side of your screen to view the file browser.
3. Scroll down and click on a file named `io_config.yaml`.
4. Enter the following keys and values under the key named `default` (you can
   have multiple profiles, add it under whichever is relevant to you)

**Required:** Azure subscription ID and Power BI workspace ID. For authentication you can use either Azure AD (service principal) or default credentials.

```yaml  theme={"system"}
version: 0.1.1
default:
  AZURE_SUBSCRIPTION_ID: your_azure_subscription_id
  POWER_BI_WORKSPACE_ID: your_power_bi_workspace_id

  # Optional: Service principal (if not using DefaultAzureCredential)
  AZURE_CLIENT_ID: ...
  AZURE_CLIENT_SECRET: ...
  AZURE_TENANT_ID: ...
```

If `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, and `AZURE_TENANT_ID` are omitted, the client uses `DefaultAzureCredential` (e.g. Azure CLI login or managed identity). The service principal or user must have access to the Power BI workspace and the **Power BI Service** API.

<br />

## Using Python block

1. Create a new pipeline or open an existing pipeline.
2. Add a data loader, transformer, or data exporter block.
3. Select `Generic (no template)`.
4. Enter this code snippet (note: change the `config_profile` from `default` if
   you have a different profile):

### Trigger a dataset refresh

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.power_bi import PowerBI
from os import path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def trigger_power_bi_refresh(**kwargs):
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    dataset_id = '...'  # Your Power BI dataset ID

    client = PowerBI.with_config(ConfigFileLoader(config_path, config_profile))
    client.load(dataset_id)
```

### Export data to a Power BI dataset

```python  theme={"system"}
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.power_bi import PowerBI
from os import path
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_power_bi(df: DataFrame, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    dataset_id = '...'

    client = PowerBI.with_config(ConfigFileLoader(config_path, config_profile))
    client.export(df, dataset_id=dataset_id)
```

### Check if a dataset exists

```python  theme={"system"}
client = PowerBI.with_config(ConfigFileLoader(config_path, config_profile))
exists = client.exists('your-dataset-id')
```

## Permissions

* Your Azure AD app or user needs the **Power BI Service** scope (e.g. `https://analysis.windows.net/powerbi/api/.default`).
* The app or user must have access to the specified Power BI workspace and dataset (e.g. Admin, Member, or Contributor on the workspace).


Built with [Mintlify](https://mintlify.com).