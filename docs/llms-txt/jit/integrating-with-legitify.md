# Source: https://docs.jit.io/docs/integrating-with-legitify.md

# Legitify Integration

Integrating with Legitify

Integrating with Legitify enables you to:

## Requirements

* Personal Access Token (PAT) for your GitHub account.
* Permissions:
  * admin:org
  * read:enterprise
  * admin:org\_hook
  * read:org
  * repo
  * read:repo\_hook

## Configuration

1. Create the [PAT](https://github.com/settings/tokens/new).
2. Copy the generated **PAT**.
3. Go to **Integrations** and click **Legitify**.\
   Screenshot.
4. Paste the **PAT** into the [Secret field](https://dash.readme.com/project/jitsecurity/v4.4.8/docs/secrets)and click **Create Secret**. You can now enable [GitHub Misconfiguration Detection](https://dash.readme.com/project/jitsecurity/v4.4.8/docs/github-misconfiguration-detection).