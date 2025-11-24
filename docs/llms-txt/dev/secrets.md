# Source: https://dev.writer.com/agent-builder/secrets.md

# Store secrets with Vault

> Store API keys, passwords, and credentials securely with Vault in Agent Builder. Reference secrets in blueprints and Python code.

Agent Builder provides **Vault**, which is a secure way to store and use secrets in your agents. Use Vault to store sensitive information like API keys, passwords, and other credentials.

You can reference secrets in any block in your blueprint and [within Python code](/agent-builder/python-secrets).

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=33a4c1f34a0ea1cde51abe05f46f875b" alt="Vault overview" data-og-width="3456" width="3456" data-og-height="1802" height="1802" data-path="images/agent-builder/vault-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3e0abcc1b9967069f0433812e10bb19d 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=6a564527da152a1f2e71f12508ae2bed 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=88cc23749f5845ceaa489ba436b7b19b 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=35d2ab4d37f68fba5470a6496942bc34 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=dbcd039c17bcfb507431a4d220c2b28b 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-overview.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e5094d1e66358b82c79b122916f81189 2500w" />

## Create a secret

Secrets are strings stored as key-value pairs. To create a secret, go to the **Vault** tab in the Agent Builder UI and click **+Add a pair**.

The example below creates a secret with the name `WRITER_API_KEY`. When you type the value, it's masked in the UI.

Click **Save** to store the secret.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1537e604f2e50506eacb0c1dc1aa3bcb" alt="" data-og-width="964" width="964" data-og-height="618" height="618" data-path="images/agent-builder/vault-add-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=19a12076120d71ef6d1e4489e41ae561 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c79a2e7e9623c0fe355e5d2fd01d26ff 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=4fd9f60e1bbb5eea13f3435f483ba9c2 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b66edd2bdd42ff870f7e1e1f0f811493 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d174a98844576a825259f4f34b889421 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-add-secret.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d362bb87f81d1666f9a71b4537510ce5 2500w" />

You can also delete and update secrets from the **Vault** tab.

## Use a secret

To use a secret, reference it in a block in your blueprint with the prefix `@{vault}`. For example, to use the `WRITER_API_KEY` secret, you would use it as `@{vault.WRITER_API_KEY}`.

The example below shows adding an authorization header to an HTTP request block using the `WRITER_API_KEY` secret.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=51c8036c149045216e9117c6de71a143" alt="" data-og-width="2738" width="2738" data-og-height="1290" height="1290" data-path="images/agent-builder/vault-use-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b1cd4693e9b8f05bcae0a31bd0bd8cc2 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=d0d0fc35cc0a322af3ab22279cf29222 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=842e9dc28714dde138536d3dc838e1a3 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c910ac6b2d488cf079e8721e1308bad2 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=c96153f760623cc2ed48506382212b67 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/vault-use-secret.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=4393323313d99240bc2dd64c43058961 2500w" />

When you reference a secret, it's automatically masked in the UI.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=69db2753aaee6aad3cab3964cb020cb6" alt="" data-og-width="1562" width="1562" data-og-height="850" height="850" data-path="images/agent-builder/http-request-with-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9b9ac41845fc423fe90f195f84222fb8 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7a58ad390df37422a8872e445b47be0e 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5bd49dfc4829387c4f0346e121c223d5 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=de25acdb7f7a1621cdf39653d2731a69 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=97f01ffe67f46e76e91ed4a1e6963eae 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/http-request-with-secret.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=daf65ca4407e17fcdf5c8fc5ed05f367 2500w" />

## Use a secret in Python code

You can access secrets in Python code blocks within blueprints using the `vault` object. `vault` is a dictionary that contains all the secrets in your blueprint.

<Warning>
  Vault secrets are only available in **blueprint code blocks** and **event handlers**. They are not available in `main.py` or other Python modules at the global scope. This is by design for security reasons. If you need to access secrets in `main.py`, use environment variables like `os.getenv('WRITER_API_KEY')` instead.
</Warning>

For example, to access a secret called `API_KEY` and use it in an HTTP request, you would use the following code:

```python  theme={null}
headers = {
    "Authorization": f"Bearer {vault['API_KEY']}"
}
```

Learn more about [accessing secrets in Python code](/agent-builder/python-secrets).

## Next steps

Now that you've learned how to store and use secrets in Vault, learn how to [make authenticated API calls using HTTP request blocks](/blueprints/httprequest) with your stored credentials.

**More resources**

* [Access secrets in Python code](/agent-builder/python-secrets) - Learn how to use vault secrets in event handlers and Python code blocks
* [Python code blocks](/blueprints/pythoncode) - Add custom Python logic to your blueprints
* [Local development](/agent-builder/local-development) - Set up local development with environment variables

<feedback />
