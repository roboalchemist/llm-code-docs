# Source: https://docs.sandboxes.cloud/docs/secrets.md

# Secrets for storing dev credentials

`Secrets` in the Crafting system are used to store sensitive information which will be encrypted at rest, and with limited access in a sandbox in the cloud. So the services running in the sandbox will have the expected configuration without saving the sensitive information in inappropriate places, like source code.

A cloud-native service may need credentials (like tokens, API keys) to talk to external services. A developer may need certain login information for accessing VPN, cloud storage, etc., in their organization. It's best practice to make sure this information is encrypted at rest and has limited access to only authorized users.

### Create secrets

A secret can be created by a user in one of the scopes:

* Shared in org: the secret is accessible from all the sandboxes in the current organization
* Private: the secret is only accessible by the sandboxes owned by the user in the current organization

To create a secret, one way is to go to the `Resources -> Secrets` page on Crafting Web Console and click `New Secret` as shown below.

<Image align="center" className="border" border={true} src="https://files.readme.io/3f1f561-image.png" />

In the dialog, we can input the name of secret and the content, as shown below.

<Image align="center" width="80% " src="https://files.readme.io/96b3280-image.png" />

Note that after creating the secret, you will not be able to view the content from web console for security. To access the secret, please see [below](#access-secrets)

Secrets can also be created via CLI, `cs`, using following commands, please see [CLI Command](https://docs.sandboxes.cloud/docs/command-line-tool#secret) for the full reference.

```shell
cs secret create NAME          # this creates a secret private in org
cs secret create --shared NAME # this creates a secret shared in org
```

Secrets are allowed to have the same name if they belong to different scopes.

*Note*: secrets are designed for sensitive information. It should be small in size (KB level) and accessed infrequently.

### Access secrets

The content of a secret can only be accessed inside a workspace:

* Shared in org: `/var/run/sandbox/fs/secrets/shared/NAME`
* Private: `/var/run/sandbox/fs/secrets/owner/NAME`

For protecting the private secrets, they are only mounted to the file system if the sandbox is in private mode. When the sandbox is changed to shared mode, it will be unmounted and only remounted after it changes back to private mode. For sandbox access control, please see [Access control in sandbox](https://docs.sandboxes.cloud/docs/access-control) for more information.

Note: folder `/var/run/sandbox/fs/secrets/owner` also contains shared secrets as it represents all secrets accessible by the sandbox owner. However, only private secrets is revealed if the same name is assigned to both a private secret and a shared secret.

The content of a *shared* secret can be placed in the value of an environment variable, for example:

```yaml
env:
- SOME_API_KEY=prefix${secret:NAME}
```

Where `NAME` is the secret name. Note: only *shared* secrets can be referenced.