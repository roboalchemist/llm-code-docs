# Source: https://docs.hypermode.com/apps/connect-app.md

# Connect Your App

> Integrate your App with external services and databases

Apps become powerful when they can connect to external systems. Hypermode
supports connecting your app to APIs, databases, and model providers through
secure, manageable integrations.

## Connection Examples

### OpenAI API connection

Connect to OpenAI for language models:

```json modus.json
{
  "models": {
    "text-generator": {
      "sourceModel": "gpt-4o-mini",
      "connection": "openai",
      "path": "v1/chat/completions"
    }
  },
  "connections": {
    "openai": {
      "type": "http",
      "baseUrl": "https://api.openai.com/",
      "headers": {
        "Authorization": "Bearer {{API_KEY}}"
      }
    }
  }
}
```

### PostgreSQL database

Connect to a PostgreSQL database:

```json modus.json
{
  "connections": {
    "postgres": {
      "type": "postgresql",
      "connStr": "{{DATABASE_URL}}"
    }
  }
}
```

### Dgraph database

Connect to a Dgraph database for graph operations:

```json modus.json
{
  "connections": {
    "dgraph": {
      "type": "dgraph",
      "grpcTarget": "{{DGRAPH_ENDPOINT}}"
    }
  }
}
```

## Environment variables

### Naming convention

Hypermode uses a consistent naming pattern for environment variables:
`MODUS_<CONNECTION_NAME>_<PLACEHOLDER>`

For a connection named `openai` with placeholder `{{API_KEY}}`:

* Environment variable: `MODUS_OPENAI_API_KEY`

### Local development

Set environment variables in `.env.dev.local`:

```text .env.dev.local
MODUS_OPENAI_API_KEY="your_openai_api_key"
MODUS_POSTGRES_DATABASE_URL="postgresql://localhost:5432/mydb"
MODUS_DGRAPH_DGRAPH_ENDPOINT="localhost:9080"
```

### Production environment

Configure production environment variables in the Hypermode console:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=22bd445f7ea0cf99d91f70029b057479" alt="Environment variables configuration panel" width="2684" height="1890" data-path="images/apps/console-envs.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=064da9f2447b6a6933619a559c676c81 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=aa8407a9d1c73725a85d75c00faef0b3 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=451d4f70f680e092c0ec821423a4e68c 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4ccf63592d586c7cea1a07249b5fcbea 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ac153c77191796b5b5565a1ba319133f 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/apps/console-envs.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3d5cc5d919d1ea27a212b53bf1e53453 2500w" data-optimize="true" data-opv="2" />

1. Navigate to your app in the console
2. Click on the **Environment Variables** tab
3. Add your environment variables with the proper naming convention
4. Save the configuration

## Testing connections

### Local testing

Test connections during development:

```bash
# Start development server
modus dev

# Test connections in the API Explorer
# Navigate to http://localhost:8686/explorer
```

### Production testing

Verify connections in production:

```bash
# Test your deployed app's connections
curl -X POST https://your-app-endpoint.hypermode.app/graphql \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ testConnection }"}'
```

## Best practices

* **Never commit secrets**: Use environment variables for all sensitive data
* **Use least privilege**: Grant minimal necessary permissions to API tokens
* **Test locally first**: Use `modus dev` to debug connection issues before
  deploying
* **Monitor usage**: Track API calls and database connections in production

Your app can now securely connect to external services and databases.
