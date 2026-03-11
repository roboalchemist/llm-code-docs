# Source: https://docs.envzero.com/changelogs/2024/03/vcs-environments-in-workflows.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤹🎬 VCS environments in workflows

> We’re excited to introduce our latest feature: support for a new workflow environment format! This update eliminates the need to create templates as prerequisites. Now, all fields can be defined directly within the workflow itself, similar to env0 VCS environments. Experience a more efficient workflow process with env0's latest enhancement. #env0 #workflow

We’re excited to introduce our latest feature: support for a new workflow environment format! This update eliminates the need to create templates as prerequisites. Now, all fields can be defined directly within the workflow itself, similar to env0 VCS environments. Experience a more efficient workflow process with env0's latest enhancement. #env0 #workflow

# New vcs format

The new format adds`vcs` (which conflict with the existing `templateName`) which allows the  customer fewer prerequisites work by inserting all the required information directly in the workflow file itself

```yaml Example theme={null}
environments:
  vpc:
    name: 'VPC and Network'
    templateName: 'VPC'
  db:
    name: DB
    templateName: 'DB'
    needs:
      - vpc
  eks:
    name: EKS
    vcs:
      type: 'terraform'
      terraformVersion: 'latest'
      repository: 'https://github.com/env0/templates'
      path: 'aws/hello-world'
      githubInstallationId: 123456789.00
    needs:
      - vpc
```

read in depth in our [docs](/guides/admin-guide/workflows/create-a-new-workflow)

Built with [Mintlify](https://mintlify.com).
