# Source: https://www.daytona.io/docs/en/configuration.md

Daytona supports multiple options to configure your environment, in order of precedence:

1. [Configuration in code](#configuration-in-code)
2. [Environment variables](#environment-variables)
3. [.env file](#env-file)
4. [Default values](#default-values)

## Configuration in code

To configure your environment in code, use the `DaytonaConfig` class. The `DaytonaConfig` class accepts the following parameters:

- `api_key`: Your Daytona [API Key](https://www.daytona.io/docs/api-keys.md)
- `api_url`: URL of your Daytona API
- `target`: Target region to create the Sandboxes on (e.g. `us`)


```python
from daytona import DaytonaConfig

config = DaytonaConfig(
    api_key="your-api-key",
    api_url="your-api-url",
    target="us"
)
```


```typescript
import { DaytonaConfig } from '@daytonaio/sdk'

const config: DaytonaConfig = {
  apiKey: 'your-api-key',
  apiUrl: 'your-api-url',
  target: 'us',
}
```


```ruby
require 'daytona'

config = Daytona::Config.new(
  api_key: 'your-api-key',
  api_url: 'your-api-url',
  target: 'us'
)
```


For more information, see the [Python SDK](https://www.daytona.io/docs/en/python-sdk/daytona.md), [TypeScript SDK](https://www.daytona.io/docs/en/typescript-sdk/daytona.md), and [Ruby SDK](https://www.daytona.io/docs/en/ruby-sdk/daytona.md) references:

> [**DaytonaConfig (Python SDK)**](https://www.daytona.io/docs/en/python-sdk/sync/daytona.md#daytonaconfig)
>
> [**DaytonaConfig (TypeScript SDK)**](https://www.daytona.io/docs/en/typescript-sdk/daytona.md#daytonaconfig)
>
> [**Config (Ruby SDK)**](https://www.daytona.io/docs/en/ruby-sdk/daytona.md#config)

## Environment variables

Daytona supports environment variables for configuration. The SDK automatically looks for these environment variables:

| Variable              | Description                                | Required |
| --------------------- | ------------------------------------------ | -------- |
| **`DAYTONA_API_KEY`** | Your Daytona API key.                      | Yes      |
| **`DAYTONA_API_URL`** | URL of your Daytona API.                   | No       |
| **`DAYTONA_TARGET`**  | Daytona Target to create the sandboxes on. | No       |

### Shell

To set environment variables in your shell, use the following commands:


    ```bash
    export DAYTONA_API_KEY=your-api-key
    export DAYTONA_API_URL=https://your-api-url
    export DAYTONA_TARGET=us
    ```


    ```bash
    $env:DAYTONA_API_KEY="your-api-key"
    $env:DAYTONA_API_URL="https://your-api-url"
    $env:DAYTONA_TARGET="us"
    ```


### .env file

To set environment variables in a `.env` file, use the following syntax:

```bash
DAYTONA_API_KEY=YOUR_API_KEY
DAYTONA_API_URL=https://your_api_url
DAYTONA_TARGET=us
```

## Default values

If no configuration is provided, Daytona will use its built-in default values:

| Option  | Value                               |
| ------- | ----------------------------------- |
| API URL | https://app.daytona.io/api          |
| Target  | Default region for the organization |