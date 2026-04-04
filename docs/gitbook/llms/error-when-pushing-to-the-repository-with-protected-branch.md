# Source: https://gitbook.com/docs/help-center/integrations/integrations-troubleshooting/git-sync/error-when-pushing-to-the-repository-with-protected-branch.md

# Error when pushing to the repository with protected branch

This error occurs when your Git branch is protected.&#x20;

{% code overflow="wrap" fullWidth="true" %}

```
Error: Missing permissions to push to the refs/heads/main protected branch. Check your branch configuration on your git provider.
```

{% endcode %}

Git Sync requires our bot to make and push changes to your repo without restrictions. This means that even during setup, our app must have full permission to make those changes.

You need to allow the GitBook app to bypass any branch protections for the Git Sync sync to work.&#x20;

### Supported branch protections

﻿Currently, we support the following branch protections:

* Require a pull request before merging
* Restrict who can push to matching branches

In both cases, you can allow the app to bypass specific teams or apps.

To do so, navigate to your settings in GitHub and allow `gitbook-com` to bypass those restrictions. The branch protections should look like this:

<figure><img src="https://downloads.intercomcdn.com/i/o/849781431/cb2b6a1dd403d5425709aa14/image.png" alt=""><figcaption><p>How to allow GitBook to bypass specifc branch protection rules</p></figcaption></figure>
