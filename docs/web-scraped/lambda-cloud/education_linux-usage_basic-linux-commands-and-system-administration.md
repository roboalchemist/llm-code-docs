# Basic Linux commands and system administration -

Source: https://docs.lambda.ai/education/linux-usage/basic-linux-commands-and-system-administration/

---

# Basic Linux commands and system administration [#](#basic-linux-commands-and-system-administration)

## Importing SSH keys from GitHub accounts [#](#importing-ssh-keys-from-github-accounts)

To import an SSH key from a GitHub account and add it to your server (or Lambda GPU Cloud on-demand instance):

-
Using your existing SSH key, SSH into your server.

Alternatively, if you're using an on-demand instance, open a terminal in [JupyterLab](../../../public-cloud/on-demand/getting-started/#how-do-i-open-jupyterlab-on-my-instance).

-
Import the SSH key from the GitHub account by running:

```bash
`[](#__codelineno-0-1)ssh-import-id gh:USERNAME
`

```
