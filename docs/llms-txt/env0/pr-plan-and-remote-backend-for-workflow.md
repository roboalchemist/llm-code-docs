# Source: https://docs.envzero.com/changelogs/2023/06/pr-plan-and-remote-backend-for-workflow.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ➕2️⃣ PR Plan and Remote Backend for Workflow

> Creating a workflow is a great way to have a deployment of your infrastructure and create dependencies between different parts of your infrastructure, allowing you to easily manage your infrastructure as you scale. However, you may want to have different variables and settings for each part, so today you can do it when creating or deploying a new Workflow. Now we have two new enhancements when working with Workflow environments.

Creating a workflow is a great way to have a deployment of your infrastructure and create dependencies between different parts of your infrastructure, allowing you to easily manage your infrastructure as you scale. However, you may want to have different variables and settings for each part, so today you can do it when creating or deploying a new Workflow. Now we have two new enhancements when working with Workflow environments.

## ✨ Remote Backend In Your Sub Environments ✨

When creating a workflow you are now able to set it to use env0's remote backend. That will make all its terraform sub environment use env0's remote backend as well. Note that all the rules regarding workspace names for templates and remote backend within env0 organizations still apply.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/06/88b9dfd-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=5207415d95c579133d9b0ead7e4eff90" alt="Workflow configuration interface showing remote backend settings for sub environments" width="696" height="223" data-path="images/changelogs/2023/06/88b9dfd-image.png" />
</Frame>

## ✨ PR Plans for Workflow Environments ✨

By creating a Pull Request that targets your workflow environment, you can execute Plan on changes to your branch!

It will trigger the Plan for all deployed environments that contain your workflow environment. Any change to the workflow file won't take effect

env0 will comment and set a commit check for each environment separately so you can keep track of the changes you made!

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/06/095670d-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=46d0f13194b4bdd5fb61a92ec0d8e3ce" alt="Pull Request plan execution interface showing workflow environment plan triggers" width="963" height="778" data-path="images/changelogs/2023/06/095670d-image.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/06/7897550-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=500d189bc1ef9c56137c5f986f13998a" alt="Pull Request comments and commit checks interface showing separate environment tracking" width="461" height="232" data-path="images/changelogs/2023/06/7897550-image.png" />
</Frame>

## Related Content

[Workflow Creation](/guides/admin-guide/workflows/create-a-new-workflow)

[Remote Backend](/guides/admin-guide/remote-backend)

[Plan On Pull Request](/guides/admin-guide/environments/plan-on-pull-request)

Built with [Mintlify](https://mintlify.com).
