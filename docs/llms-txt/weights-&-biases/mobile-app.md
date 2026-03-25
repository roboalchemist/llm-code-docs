# Source: https://docs.wandb.ai/platform/hosting/monitoring-usage/mobile-app.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# W&B Mobile App (iOS)

> Track training runs, view line plots, and explore your W&B Models projects from your iPhone or iPad.

<Columns cols={4}>
  <Frame>
        <img src="https://mintcdn.com/wb-21fd5541/XPXC1BFyZbgpU38S/images/mobile-app/project-panels.png?fit=max&auto=format&n=XPXC1BFyZbgpU38S&q=85&s=22c38cd9e56f061496b4385e47915d2f" alt="W&B mobile app runs list view" width="1179" height="2556" data-path="images/mobile-app/project-panels.png" />
  </Frame>

  <Frame>
        <img src="https://mintcdn.com/wb-21fd5541/XPXC1BFyZbgpU38S/images/mobile-app/manage-alerts.png?fit=max&auto=format&n=XPXC1BFyZbgpU38S&q=85&s=9996d5c045642e88c266095a3524ee24" alt="W&B mobile app run detail view" width="1179" height="2556" data-path="images/mobile-app/manage-alerts.png" />
  </Frame>

  <Frame>
        <img src="https://mintcdn.com/wb-21fd5541/XPXC1BFyZbgpU38S/images/mobile-app/projects.png?fit=max&auto=format&n=XPXC1BFyZbgpU38S&q=85&s=86ae0742e00826c09c060d9632878c3d" alt="W&B mobile app projects view" width="1179" height="2556" data-path="images/mobile-app/projects.png" />
  </Frame>

  <Frame>
        <img src="https://mintcdn.com/wb-21fd5541/XPXC1BFyZbgpU38S/images/mobile-app/project-runs.png?fit=max&auto=format&n=XPXC1BFyZbgpU38S&q=85&s=edf585637011747c4cc70f1403b371e1" alt="W&B mobile app workspace view" width="1179" height="2556" data-path="images/mobile-app/project-runs.png" />
  </Frame>
</Columns>

The W\&B Mobile App for iOS keeps you connected to your W\&B Models projects wherever you go. Track training runs in real time, view line plots, explore your projects' histories, and follow your team's progress—all from your iPhone or iPad.

<Info>
  The mobile app is only available for [Multi-tenant Cloud](/platform/hosting/hosting-options/multi_tenant_cloud) accounts. It is not available for [Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) or [Self-Managed](/platform/hosting/hosting-options/self-managed) deployments.
</Info>

## Download the app

<Card title="Download on the App Store" href="https://apps.apple.com/us/app/6755162576" icon="apple" />

## Features

* **Track training runs**: View run status, metrics, and line plots in real time
* **Explore project history**: Browse and search across your W\&B projects.
* **Stay informed**: Get updates on your experiments without opening your laptop using notifications.

## Set up notifications

You can configure notifications in two ways:

**Metric threshold alerts**

1. Navigate to a run.
2. Tap the graph to enter fullscreen view.
3. Tap the bell icon on the top-right.
4. Set notifications that trigger when future runs cross the specified metric threshold.

**Run failure alerts**

1. Navigate to a project.
2. Tap the three-dot menu on the top-right.
3. Select **Run failed alert** to receive notifications for future run failures in that project.
