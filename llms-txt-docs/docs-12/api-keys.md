# Source: https://docs.baseten.co/observability/api-keys.md

# Best practices for API keys

> Securely access your Baseten models

API keys enable secure access to Baseten models for:

* **Model deployment** via Truss CLI
* **Inference API calls** (`truss predict`, `/wake` requests)
* **Model management** via the [management API](/reference/management-api/overview)
* **Metrics export** via the `/metrics` endpoint

You can create and revoke API keys from your [Baseten account](https://app.baseten.co/settings/api_keys).

## API key scope: Personal vs Workspace

There are two types of API keys on Baseten:

**Personal API Keys:**

* Tied to a user account.
* Inherit full workspace permissions.
* Actions are linked to the specific user.

**Workspace API Keys:**

* Shared across a workspace.
* Can have full access or be restricted to specific models.

<Note>Use personal keys for testing and workspace keys for automation and production.</Note>

## Using API keys with Truss

Add your API key to `~/.trussrc` for authentication:

```sh ~/.trussrc theme={"system"}
[baseten]
remote_provider = baseten
api_key = abcdefgh.1234567890ABCDEFGHIJKL1234567890
remote_url = https://app.baseten.co
```

If rotating keys, update the file with the new key.

### Using API keys with endpoints

Include the API key in request headers:

```sh  theme={"system"}
curl -X POST https://app.baseten.co/models/MODEL_ID/predict \
-H 'Authorization: Api-Key abcdefgh.1234567890ABCDEFGHIJKL1234567890' \
-d 'MODEL_INPUT'
```

Or in Python:

```python  theme={"system"}
headers = {"Authorization": "Api-Key abcdefgh.1234567890ABCDEFGHIJKL1234567890"}
```

## Tips for managing API keys

Best practices for API key use apply to your Baseten API keys:

* Always store API keys securely.
* Never commit API keys to your codebase.
* Never share or leak API keys in notebooks or screenshots.
* Name your API keys to keep them organized.

The [API key list on your Baseten account](https://app.baseten.co/settings/api_keys) shows when each key was first created and last used. Rotate API keys regularly and remove any unused API keys to reduce the risk of accidental leaks.
