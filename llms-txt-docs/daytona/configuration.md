# Source: https://www.daytona.io/docs/en/configuration.md

## Configuration Methods

Daytona SDK supports multiple ways to configure your environment, in order of precedence:

1. [**Configuration in code**](#configuration-in-code)
2. [**Environment variables**](#environment-variables)
3. [**.env file**](#env-file)
4. [**Default values**](#default-values)

## Configuration in Code

Daytona SDK provides an option to configure settings using the `DaytonaConfig` class in Python and TypeScript. The `DaytonaConfig` class accepts the following parameters:

- `api_key`: Your Daytona [API Key](https://www.daytona.io/docs/api-keys.md)
- `api_url`: URL of your Daytona API
- `target`: Daytona Target to create the Sandboxes on.

```python
from daytona import DaytonaConfig

config = DaytonaConfig(
    api_key="your-api-key",
    api_url="your-api-url",
    target="us"
)

```
```typescript
import { DaytonaConfig } from '@daytonaio/sdk';

const config: DaytonaConfig = {
    apiKey: "your-api-key",          
    apiUrl: "your-api-url",     
    target: "us"                  
};
```


## Environment Variables

Daytona SDK supports environment variables for configuration. The SDK automatically looks for these environment variables:

| Variable              | Description                                | Optional |
| --------------------- | ------------------------------------------ | -------- |
| **`DAYTONA_API_KEY`** | Your Daytona API key.                      | No       |
| **`DAYTONA_API_URL`** | URL of your Daytona API.                   | Yes      |
| **`DAYTONA_TARGET`**  | Daytona Target to create the Sandboxes on. | Yes      |

Set environment variables in your shell:

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

You can also set these environment variables in a `.env` file.

## .env File

Create a `.env` file in your project root directory:

```bash
DAYTONA_API_KEY=your-api-key
DAYTONA_API_URL=https://your-api-url
DAYTONA_TARGET=us
```

The SDK will automatically read these values when initializing.

## Default Values

If no configuration is provided, Daytona SDK will use its built-in defaults:

| Option    | Default Value                       |
|-----------|-------------------------------------|
| API URL   | https://app.daytona.io/api          |
| Target    | Default region for the organization |