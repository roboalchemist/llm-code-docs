# Source: https://docs.wiremock.io/openAPI/openapi-git-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAPI Git Integration

> Integrating your Git repository with your mock API

WireMock Cloud offers the ability to synchronize your mock API's OpenAPI spec with a Git repository.
This synchronization is bidirectional, allowing you to pull your spec from Git to WireMock Cloud, as well as push
updates from WireMock Cloud to Git.

This enables WireMock Cloud to be integrated into your workflows seamlessly.
Your stubs can be kept up to date without having to manually copy your specification into WireMock Cloud each time it is
updated, and you can prototype your OpenAPI specification in WireMock Cloud before pushing it to your code base.

## Configuring your Git integration

To configure your mock API to synchronize its OpenAPI document with a Git repository, navigate to the Settings tab of
the OpenAPI page.

Toggle "Enable synchronization" in the Git repository settings section.

Fill in the fields with the appropriate Git configuration data, including the SSH address of your Git repository and
the path to the OpenAPI file within the repository.

The key that WireMock Cloud will use to authenticate calls to your Git repository must also be configured here.
You can either select an existing key or create a new one.

You can learn more about keys in WireMock Cloud [here](/security/key-management).

Once you have entered the relevant Git repository configuration, save your changes.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3666994d6fdbf1337fabe46dceb6977f" alt="OpenAPI Git integration settings" data-og-width="1044" width="1044" data-og-height="568" height="568" data-path="images/openapi/git-integration-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=b97a78241a321deddfd0f2e123fc62d9 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=5c7739b191c9be9bb08bec9daa9f2a3e 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=a7c10d2c53f15f40573b698c347afe82 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=50528666ebf6670126f76222e88f3526 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=acf0d8a0690496a697052c16ec69eff4 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-settings.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8cfe4d26d6ab521488959e1e637a70f6 2500w" />

The SSH public key for the key you selected will be displayed at the bottom of the configuration.
[Add this key to your Git repository.](#adding-ssh-keys-to-your-git-repository)

When you navigate to the Document tab of the OpenAPI page, there will be buttons for performing Git operations on your
OpenAPI document.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=1319bbc6133dc0515350d8dac62740be" alt="OpenAPI Git integration buttons" width="50%" data-og-width="492" data-og-height="490" data-path="images/openapi/git-integration-buttons.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=4fe680a0c0c5f834dd7d07aa86742aa0 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9a0f3b5e82401addc3d52aeaf74a09a4 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=43543e0d51ac99271fb22808c14295d0 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ba04e8ad6628edc8ee81a3305732906d 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=852f6e5e63310f30ad115def578d153d 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/git-integration-buttons.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=28a1db046e923d8b7d57f12445307a43 2500w" />

Clicking the Pull button will retrieve the contents of the file at the configured path in your Git repository and save
it in WireMock Cloud.
The document will be validated and stubs generated like normal.
The pulled document will appear in the document text area.
Note, this will not immediately overwrite any local changes you have made to the specification (see
[Git conflicts](#handling-git-conflicts) for details).

Clicking the Push button in the Document tab of the OpenAPI page will push your currently saved OpenAPI document on
WireMock Cloud to the configured Git repository.
If the file does not exist on the configured branch of the Git repository, then it will be created by this action.

If you wish to push to your Git repository, ensure that write access is granted to the SSH key when you add it to your
repository, if required by the platform (e.g. GitHub).

With the Git integration enabled, changes can still be saved to WireMock Cloud's copy of the OpenAPI document
independently of the configured Git repository.
WireMock Cloud and your Git repository are only synchronized when the document is pulled or pushed.

## Handling Git Conflicts

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

There are circumstances where performing a pull or push will cause conflicts with your mock API's copy of your OpenAPI
specification.
This can occur when a pull is attempted after changes have been applied to your mock API's copy of the specification
that have yet to be pushed to your repository, or when pushing after changes have been made to the file in the
repository since the last time it was pulled into WireMock.

In these cases, attempting a pull or push will display a dialog explaining that your mock API is out of sync with the
repository and ask if you wish to overwrite the document on WireMock (when pulling) or the document in the repository
(when pushing).
If this dialog is cancelled, no changes will occur in WireMock or your repository.

If you are receiving these conflict messages and are unsure of what action to perform, WireMock recommends performing
an overwriting push to the repository, rather than an overwriting pull to your mock API, and resolving any issues using
external Git tooling.
This ensures that no data is lost, since all changes will be logged in version control.

## Testing Connections to Your Git Repository

If you want to test that your Git configuration is correct before attempting a pull or push (or even saving the
configuration), you can use the "Test Connection" button on the settings page.
Simply fill in the configuration fields and press the button.
If WireMock Cloud is able to connect to your Git repository, then a success will be displayed.
Otherwise, a message will be displayed explaining what went wrong.

## Adding SSH Keys to Your Git Repository

[//]: # "WARNING: This heading is referenced by the UI. Do not change it without changing the link in the UI."

In order for WireMock Cloud to be able to communicate with your Git repository, you must add the SSH public key displayed in your mock API's OpenAPI settings to the repository.
The process for adding the public key to your Git repository depends on the method you are using to host your Git
repository.

Below are instructions for adding keys to your repository on popular hosting platforms.
These instructions are up-to-date as of writing, but are subject to changes outside WireMock's control.

### GitHub

If you are hosting a repository on [GitHub](https://github.com), you can add the key to your repository via the "Deploy
keys" page of the repository settings tab.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=2d5e42a364938fe9b2154d8dc4e93fc2" alt="GitHub Deploy Keys Page" data-og-width="1485" width="1485" data-og-height="813" height="813" data-path="images/openapi/github-deploy-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e5af3bfae7fec5a8621ba2f2299401a9 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=fd63ed85dc063f55bd7fb66dcc869d67 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=7a190db581f79d094abf139247d80538 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=c166e8153e96f4d1890909c07e9e67f3 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=8fe23da9d2c2e2b1ae87a799ce7724ec 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-deploy-keys.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=d3f3870da0295aa73d1ce75c16b8d0be 2500w" />

Make sure to allow the key write access if you want to push to the repository from WireMock Cloud.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=857bf0e9281e8d133fdbec43d1473489" alt="GitHub Add Deploy Key Page" data-og-width="818" width="818" data-og-height="508" height="508" data-path="images/openapi/github-add-deploy-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3e43ef27759946fd609f06efd1d03258 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=835c915dee6f172f88637e2f5ce5c132 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ce52a338d694042efa8bf4a5b97b527a 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ad56c72aed5aea1195612417545147c3 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=9c860451ce7e50dcb0504c5b4a4a84f5 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/github-add-deploy-key.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=5c9d2575ad3ecb25725ff1bd7dfb2d7f 2500w" />

### Bitbucket

If you are hosting a repository on [Bitbucket](https://bitbucket.org), you can add the key to your repository via the
repository's "Access keys" page.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=67ca5972fce0b0adce6426268d9dbf47" alt="Bitbucket Access Keys Page" data-og-width="1266" width="1266" data-og-height="507" height="507" data-path="images/openapi/bitbucket-access-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ddb9d9fe381b6459b1c717317e1a2508 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=355a807a355afd902c9c35412f6564d3 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6caddacf746a315d5cd982381ac6c863 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=1a8e74d5bca22e481d4b99f4f50c86ae 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=887ce5ece7b3f31b10678284053772d9 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-access-keys.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=fe347e82572180ccf36d06b54971fb2d 2500w" />

Bitbucket's access keys are limited to read-only access to a repository.
This means pushing from WireMock Cloud is not possible when using access keys.
If write access is required, the key can be added to a user's personal SSH keys.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=59462c1255beffd94f36f88af307fe56" alt="Bitbucket Personal SSH Keys Page" data-og-width="1086" width="1086" data-og-height="589" height="589" data-path="images/openapi/bitbucket-personal-ssh-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=3f144b8d6e27f7973f7bd8d0da010b4a 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=abb058ce945eb9ec80f89d76923b9305 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=6bc018fc0b6bf4c80d148bc077255072 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=01f967c19886456dd4235045fcdd80a0 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=269c4480982c3a26feb5a04a44d93af7 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/bitbucket-personal-ssh-keys.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=498ae06423efc65036a15b253152b883 2500w" />

This will allow the key write access to all repositories that the user has access to.
Therefore, it may be advisable to create a specific user for WireMock Cloud in your Bitbucket organisation that only has
access to the desired repository.

### Gitlab

If you are hosting a repository on [Gitlab](https://gitlab.com), you can add the key to your repository via the
repository's "Deploy keys" section of the repository settings page.
Make sure to grant the key write permissions if you want to push to the repository from WireMock Cloud.

<img src="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ebc310d56ac5dc05538e8d2aca1ee820" alt="Gitlab Add SSH Key Settings" data-og-width="1707" width="1707" data-og-height="850" height="850" data-path="images/openapi/gitlab-add-ssh-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=280&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=ee9fcd4301675784522c644cb27be7e2 280w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=560&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=19d0a5a7b7b3594c9b18f23b5250b16b 560w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=840&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=c064a8b574d34b4712783d74c1111ff0 840w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=1100&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=2775756ae439b7e7a0d38f36b1622b7a 1100w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=1650&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=e096bc40bd29455e1160e8c916a7f949 1650w, https://mintcdn.com/wiremockinc/9niDaTpLrBsVTNkq/images/openapi/gitlab-add-ssh-key.png?w=2500&fit=max&auto=format&n=9niDaTpLrBsVTNkq&q=85&s=bd26da69e0f8d414aafa74ecbfec9aa6 2500w" />

### Self-Hosted Server

If you are hosting a repository on a server that you maintain, adding the key to your repository will generally involve
adding it to the Git user's `.ssh/authorized_keys` file.
For example, if your Git repository address is `git-user@my-git-server.com:path/to/repository.git`, you will likely have
to append the key to the contents of `/home/git-user/.ssh/authorized_keys` on the server that `my-git-server.com`
addresses.
Approaches may vary, so it is best to consult your system administrator.

For security purposes, WireMock recommends creating a specific user for WireMock Cloud on your server with read
permission on the Git repository directory only (and write permission if pushing from WireMock Cloud is desired).
