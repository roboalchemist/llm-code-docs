# Source: https://docs.mage.ai/integrations/airbyte.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Airbyte in Mage

> Trigger a connection sync in Airbyte.

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

# Airbyte cloud

<ProOnly source="airbyte" />

## Configuration

Mage Pro supports triggering **Airbyte Cloud** connection syncs directly from your data pipelines. To connect to Airbyte Cloud, you need to configure the following keyword arguments.

| Keyword argument | Description                              | Default value |
| ---------------- | ---------------------------------------- | ------------- |
| `use_cloud`      | Whether to use Airbyte Cloud             | `False`       |
| `client_id`      | Airbyte cloud application client\_id     | `None`        |
| `client_secret`  | Airbyte cloud application client\_secret | `None`        |

Refer to the [Airbyte documentation](https://docs.airbyte.com/using-airbyte/configuring-api-access#step-1-create-an-application) to retrieve your `client_id` and `client_secret`.

## Example data loader

You can either explicitly hard code the `connection_id` in the data loader block
or you can add the value of the `connection_id`
as a [runtime variable](/getting-started/runtime-variable#creating-runtime-variables-in-editor).

from mage\_ai.services.airbyte import Airbyte

```python  theme={"system"}
from mage_ai.services.airbyte import Airbyte


@data_loader
def load_data(*args, **kwargs):
    connection_id = kwargs['connection_id']
    client = Airbyte(
        use_cloud=True,
        client_id='client_id',
        client_secret='client_secret',
    )
    job = client.run_sync(connection_id, poll_interval=2)

    return job
```

# Open source

## Configuration

Here are the following keyword arguments that can be used to configure `Airbyte`:

| Keyword argument | Description                            | Default value          |
| ---------------- | -------------------------------------- | ---------------------- |
| `api_version`    | API version                            | `v1`                   |
| `host`           | Airbyte server host                    | `host.docker.internal` |
| `password`       | Password to log into Airbyte           | `password`             |
| `port`           | Airbyte server port                    | `8000`                 |
| `use_ssl`        | If `True`, then service will use HTTPS | `False`                |
| `username`       | Username to log into Airbyte           | `airbyte`              |

## Example code

```python  theme={"system"}
from mage_ai.services.airbyte import Airbyte


client = Airbyte(
    api_version='v1',
    host='host.docker.internal',
    password='password',
    port=8000,
    use_ssl=False,
    username='airbyte',
)
job = client.run_sync('7a749f2f-74b4-492e-9d13-30a3f390d111', poll_interval=2)
```

Sample result:

```json  theme={"system"}
{
  "connection_id": "7a749f2f-74b4-492e-9d13-30a3f390d111",
  "connection_status": "active",
  "job": {
    "id": 9,
    "configType": "sync",
    "configId": "7a749f2f-74b4-492e-9d13-30a3f390d111",
    "createdAt": 1671909838,
    "updatedAt": 1671909843,
    "status": "succeeded"
  }
}
```

## Example data loader

You can either explicitly hard code the `connection_id` in the data loader block
or you can add the value of the `connection_id`
as a [runtime variable](/getting-started/runtime-variable#creating-runtime-variables-in-editor).

```python  theme={"system"}
from mage_ai.services.airbyte import Airbyte


@data_loader
def load_data(*args, **kwargs):
    connection_id = kwargs['connection_id']
    client = Airbyte(
        host='host.docker.internal',
        password='password',
        username='airbyte',
    )
    job = client.run_sync(connection_id, poll_interval=2)

    return job
```


Built with [Mintlify](https://mintlify.com).