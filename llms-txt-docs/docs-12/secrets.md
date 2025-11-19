# Source: https://docs.baseten.co/observability/secrets.md

# Source: https://docs.baseten.co/development/model/secrets.md

# Security and secrets

> Using secrets securely in your ML models

Truss allows you to securely manage **API keys**, **access tokens**, **passwords**, **and other secrets** without exposing them in code.

## 1. Define Secrets in `config.yaml`

Add secrets with **placeholder** values in `config.yaml`:

```yaml  theme={"system"}
secrets:
  hf_access_token: null
```

<Warning>Never store actual secret values in `config.yaml`. Store secrets in the [workspace settings](https://app.baseten.co/settings/secrets).</Warning>

## 2. Access Secrets in `model.py`

Secrets are passed as **keyword arguments** to the `Model` class:

```python  theme={"system"}
def __init__(self, **kwargs):
    self._secrets = kwargs["secrets"]
```

Use secrets inside load or predict:

```python  theme={"system"}
def load(self):
    self._model = pipeline(
        "fill-mask",
        model="baseten/docs-example-gated-model",
        use_auth_token=self._secrets["hf_access_token"]
    )
```

## 3. Store Secrets on Your Remote

* On **Baseten**, add secrets in the [workspace settings](https://app.baseten.co/settings/secrets).
* Use the **exact name** from `config.yaml` (case-sensitive).

## 4. Deploying with Secrets

By default, models have access to any secrets on a workspace.
