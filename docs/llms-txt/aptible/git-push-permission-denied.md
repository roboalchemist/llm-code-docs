# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/git-push-permission-denied.md

# git Push Permission Denied

When pushing to your [App](/core-concepts/apps/overview)'s [Git Remote](/how-to-guides/app-guides/deploy-from-git#git-remote), you may encounter a Permission denied error. Below are a few common reasons this may occur and steps to resolve them.

```sql  theme={null}
Pushing to git@beta.aptible.com:[environment]/[app].git
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```

## Wrong SSH Key

If you attempt to authenticate with a [public SSH key](/core-concepts/security-compliance/authentication/ssh-keys) not registered with Aptible, Git Authentication will fail and raise this error.

To confirm whether Aptible’s Git server correctly authenticates you, use the ssh command below.

```
ssh -T git@beta.aptible.com test
```

On successful authentication, you'll see this message:

```
Hi [email]! Welcome to Aptible. Please use `git push` to connect.
```

On failure, you'll see this message instead:

```
git @beta.aptible.com: Permission denied(publickey).
```

## Resolution

The two most common causes for this error are that you haven't registered your [SSH Public Key](/core-concepts/security-compliance/authentication/ssh-keys) with Aptible or are using the wrong key to authenticate. 

From the SSH Keys page in your account settings (locate and click the Settings option on the bottom left of your Aptible Dashboard , then click the SSH Keys option), double-check you’ve registered an SSH key that matches the one you’re trying to use. If you’re still running into issues and have multiple public keys on your device, you may need to specify which key you want to use when connecting to Aptible. To do so, add the following to your local \~/.ssh/config file (you might need to create it):

```
Host beta.aptible.com
    IdentityFile /path/to/private/key
```

## Environment Permissions

If you don’t have the proper permissions for the Environment or because the Environment/App you’re pushing to doesn’t exist, you’ll also see the Permission denied (publickey) error above.

## Resolution

In the [Dashboard](https://app.aptible.com), check that you have the proper [permissions](/core-concepts/security-compliance/access-permissions) for the Environment you’re pushing to and that the Git Remote you’re using matches the App’s Git Remote.
