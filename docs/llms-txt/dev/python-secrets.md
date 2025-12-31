# Source: https://dev.writer.com/agent-builder/python-secrets.md

# Access secrets in Python code

Agent Builder provides **Vault**, which is a secure way to store and use secrets in your agents. Use Vault to store sensitive information like API keys, passwords, and other credentials that you don't want to expose in your code. Secrets are available in [blueprint blocks](/agent-builder/secrets#use-a-secret) and within Python code.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=33a4c1f34a0ea1cde51abe05f46f875b" alt="Vault overview" data-og-width="3456" width="3456" data-og-height="1802" height="1802" data-path="images/agent-builder/vault-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3e0abcc1b9967069f0433812e10bb19d 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6a564527da152a1f2e71f12508ae2bed 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=88cc23749f5845ceaa489ba436b7b19b 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=35d2ab4d37f68fba5470a6496942bc34 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dbcd039c17bcfb507431a4d220c2b28b 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e5094d1e66358b82c79b122916f81189 2500w" />

## Create a secret

Secrets are strings stored as key-value pairs. To create a secret, go to the **Vault** tab in the Agent Builder UI and click **+Add a pair**.

The example below creates a secret with the name `WRITER_API_KEY`. When you type the value, it's masked in the UI.

Click **Save** to store the secret.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1537e604f2e50506eacb0c1dc1aa3bcb" alt="Add a secret" data-og-width="964" width="964" data-og-height="618" height="618" data-path="images/agent-builder/vault-add-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=19a12076120d71ef6d1e4489e41ae561 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c79a2e7e9623c0fe355e5d2fd01d26ff 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=4fd9f60e1bbb5eea13f3435f483ba9c2 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b66edd2bdd42ff870f7e1e1f0f811493 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d174a98844576a825259f4f34b889421 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d362bb87f81d1666f9a71b4537510ce5 2500w" />

You can also delete and update secrets from the **Vault** tab.

## Where secrets are available

Within Python code, Vault is a runtime-only feature that's injected into specific execution contexts, not into the main module scope. It isn't a global variable and is only available in the execution context of the blueprint. This design provides security benefits:

* Secrets are only loaded when needed
* Access is limited to proper execution contexts
* No global exposure of sensitive data

The vault is only available in these specific contexts:

* **Event handlers and blueprint code blocks**: Secrets are injected into event handlers and blueprint code blocks when they run. This includes:
  * Button click handlers
  * Form submission handlers
  * Page load handlers
  * Custom event handlers
* **Blueprint execution environment**: Secrets are injected into the blueprint execution environment when the blueprint runs and can be referenced from any blueprint block.

### Access your Writer API key

Each Agent Builder agent in the online editor has a Writer API key set as an environment variable called `WRITER_API_KEY`. If you want to use this API key with other Writer API calls, you can access it with `os.getenv('WRITER_API_KEY')`. This allows you to access the API key outside of event handlers and blueprint code blocks, and means you don't need to set a new secret in Vault for your API key.

```python  theme={null}
import os

api_key = os.getenv('WRITER_API_KEY')
```

## Examples

### Secrets in Python code blocks

You can reference secrets in [Python code blocks](/blueprints/pythoncode) within blueprints using the `vault` object. `vault` is a dictionary that contains all the secrets in your blueprint.

For example, to access a secret called `ACME_API_KEY` and use it in an HTTP request, you would use the following code:

```python  theme={null}
headers = {
    "Authorization": f"Bearer {vault['ACME_API_KEY']}"
}
```

### Event handler with vault access

Vault is also provided as an argument to event handlers. Here's an example of an event handler that's triggered when a button is clicked and accesses the vault.

```python  theme={null}
def handle_button_click(state, payload, context, session, ui, blueprint_runner, vault):
    # Access vault secrets
    api_key = vault.get('ACME_API_KEY')
    
    # Use the secret
    headers = {"Authorization": f"Bearer {api_key}"} 
```

<feedback />
