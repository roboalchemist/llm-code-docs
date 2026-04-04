# Source: https://docs.baseten.co/organization/api-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# API keys

> Authenticate requests to Baseten for deployment, inference, and management.

API keys authenticate your requests to Baseten. You need an API key to:

* Deploy models, Chains, and training projects with the Truss CLI.
* Call model endpoints for inference.
* Use the management API.

## API key types

Baseten supports two types of API keys:

**Personal API keys** are tied to your user account. Actions performed with a personal key are attributed to you. Use personal keys for local development and testing.

**Team API keys** are not tied to an individual user. When your organization has [teams](/organization/teams) enabled, team keys can be scoped to a specific team. Team keys can have different permission levels:

* **Full access** - Deploy models, call endpoints, and manage resources.
* **Inference only** - Call model endpoints but cannot deploy or manage.
* **Metrics only** - Export metrics but cannot deploy or call models.

Use team keys for CI/CD pipelines, production applications, and shared automation.

<Note>
  If your organization uses [teams](/organization/teams), Team Admins can create team API keys scoped to their team. See [Teams](/organization/teams) for more information.
</Note>

## Create an API key

To create an API key:

1. Navigate to [API keys](https://app.baseten.co/settings/api_keys) in your account settings.
2. Select **Create API key**.
3. Choose **Personal** or **Team** key type.
4. Enter a name for the key (lowercase letters, numbers, and hyphens only).
5. For team keys, select the permission level.
6. Select **Next**.

Copy the key immediately, you won't be able to view it again.

## Use API keys with the CLI

The first time you run `truss push`, the CLI prompts you for your API key and saves it to `~/.trussrc`:

```
$ truss push --watch
💻 Let's add a Baseten remote!
🤫 Quietly paste your API_KEY:
💾 Remote config `baseten` saved to `~/.trussrc`.
```

To manually configure or update your API key, edit `~/.trussrc`:

```sh  theme={"system"}
[baseten]
remote_provider = baseten
api_key = YOUR_API_KEY
```

## Use API keys with endpoints

To call model endpoints with your API key, see [Call your model](/inference/calling-your-model).

## Manage API keys

The [API keys page](https://app.baseten.co/settings/api_keys) shows all your keys with their creation date and last used timestamp. Use this information to identify unused keys.

To rename a key, select the pencil icon next to the key name.

To rotate a key, create a new key, update your applications to use it, then revoke the old key.

To revoke a key, select the trash icon next to the key. Revoked keys cannot be restored.

You can also manage API keys programmatically with the [REST API](/reference/management-api/api-keys/creates-an-api-key).

### Security recommendations

* Store API keys in environment variables or secret managers, not in code.
* Never commit API keys to version control.
* Use team keys with minimal permissions for production applications.
* Rotate keys periodically and revoke unused keys.
