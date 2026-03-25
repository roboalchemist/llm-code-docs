# Source: https://docs.envzero.com/guides/admin-guide/environments/move-environment.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Moving Environments

> Move env zero environments between projects to reorganize structures and reallocate resources

Moving environments between projects can be useful when reorganizing project structures, reallocating resources, or consolidating environments for more efficient management.

By moving environments, you can ensure that your infrastructure aligns with your team’s evolving needs and project goals.

1. Navigate to the Environment page of the environment you would like to move
2. Open the menu at the top of the card
3. Click `Move Environment`

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/07/c963361-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=e55a7c55af814b34b709772fec99f3d7" alt="" width="785" height="418" data-path="images/changelogs/2024/07/c963361-image.png" />

1. Select your target project from the list and click `Move`

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/07/b870ffa-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=58a8d52ba27f5107964f205a287579e2" alt="" width="518" height="584" data-path="images/changelogs/2024/07/b870ffa-image.png" />

1. That's it! You'll be redirected to the redeploy page so you can deploy the environment on the target project.

<Warning>
  **Limitations**

  When moving an environment, most of your environment settings will stay intact, however, project related settings may change. Here is a list of the settings that might change:

* Variables
* Project policies
* State access control
* Costs

  From now on those settings will be part of the new project, however, this will only take affect after a successful deployment on the new project.

  **We strongly encourage you to re-deploy your environment immediately after moving it**
</Warning>

Built with [Mintlify](https://mintlify.com).
