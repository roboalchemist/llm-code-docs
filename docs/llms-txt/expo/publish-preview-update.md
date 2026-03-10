# Source: https://docs.expo.dev/eas/workflows/examples/publish-preview-update

---
modificationDate: March 09, 2026
title: Publish preview updates with EAS Workflows
description: Learn how to publish preview updates with EAS Workflows.
---

# Publish preview updates with EAS Workflows

Learn how to publish preview updates with EAS Workflows.

Once you've made changes to your project, you can share a preview of your changes with your team by publishing a [preview update](/review/share-previews-with-your-team). This is useful when you want to review changes with your team without pulling the latest changes and running them locally.

You can access preview updates in the development build UI and through scannable QR codes on the EAS dashboard. When publishing a preview on every commit, your team can review changes without pulling the latest changes and running them locally.

[Expo Golden Workflow: Share preview updates with your team](https://www.youtube.com/watch?v=v_rzRcVSQYQ) — Publish preview updates on every commit with EAS Workflows so your team can review changes without pulling code locally.

## Get started

Prerequisites

2 requirements

1.

Set up EAS Update

Your project needs to have [EAS Update](/eas-update/introduction) setup to publish preview updates. You can set up your project with:

```sh
eas update:configure
```

2.

Create new development builds

After you've configured your project, create new [development builds](/develop/development-builds/create-a-build) for each platform.

The following workflow publishes a preview update for every commit on every branch.

```yaml
name: Publish preview update

on:
  push:
    branches: ['*']

jobs:
  publish_preview_update:
    name: Publish preview update
    type: update
    params:
      branch: ${{ github.ref_name || 'test' }}
```
