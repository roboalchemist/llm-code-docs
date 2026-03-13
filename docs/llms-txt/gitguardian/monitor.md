# Source: https://docs.gitguardian.com/honeytoken/deploy-honeytokens/monitor.md

# Monitor the deployment of your honeytokens

> Track and monitor the deployment status of your honeytokens across git repositories integrated with GitGuardian.

:::info Reminder
You can deploy honeytokens [anywhere in your SDLC](../core-concepts#where-should-you-place-your-honeytokens), but for source code repositories in particular, GitGuardian has the capability to detect the deployment of your honeytokens and monitor it in its dashboard.
:::

## Source information

In the case of honeytokens deployed in git repositories that are integrated with GitGuardian, the source (and file) where the honeytoken has been placed is automatically detected and displayed.

![Honeytoken source detected](/img/honeytoken/source-detected.png)

Again, watch out for honeytokens that get duplicated in several repositories: you would not know which source is compromised if it gets triggered. You can identify from there if a honeytoken gets propagated to several different repositories (eg. by forking a repository or copying code).

:::tip
If the repository where your honeytoken has been planted contains secret incidents that we have already detected, we will provide you with a link to quickly navigate to those secret incidents. 
Indeed, If a honeytoken alerts you that a repository has been compromised, it means that **all the secrets contained within it are at maximum risk**.
:::

## Monitor honeytoken coverage across your entire perimeter

The Perimeter page now presents information related to honeytokens.

![Perimeter](/img/honeytoken/perimeter.png)

For each source, monitor how many honeytokens are deployed, if any of them are triggered, and also if any have been found âPublicly exposedâ.

The right panel also displays how much of your perimeter is covered by honeytokens.
