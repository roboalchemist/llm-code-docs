# Source: https://docs.envzero.com/guides/admin-guide/environments/ad-hoc-tasks.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running Ad Hoc Tasks

> Run arbitrary commands on your env zero deployment container without committing to git using ad hoc tasks

Sometimes you may want to execute arbitrary commands on your deployment container - for example, manually altering the state or manipulating a local file. These commands can be run using [Custom Flows](/guides/admin-guide/custom-flows), but that requires committing the commands to your git repository, which doesn't always fit the use case. In these cases, it is possible to execute **Run a Task** on the deployment container.

<Info>
  **Permissions to run a one time tasks**

  Ad hoc tasks allow you to run **any** command on the deployment container, so by default only [organization administrators](/guides/admin-guide/user-role-and-team-management/user-management) may run these tasks. You can use [custom roles](/guides/admin-guide/user-role-and-team-management/custom-roles) to grant this permission to other users.
</Info>

## Executing a Run Task

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/5299661-ss.jpg?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=7e0930b706c6136cf51ecdaebd572eac" alt="" width="2890" height="488" data-path="images/guides/admin-guide/environments/5299661-ss.jpg" />

From the environment's advanced context menu, click on `Run a Task`.\
It will prompt you to enter the commands you desire to execute.\
Enter the commands, as you would in a bash script. Separate commands with new lines.\
When you are ready to run your task - click the `RUN A TASK` button below.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environments/1ee51e5-screenshot_2023-01-23_at_10.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=79a7cc10f5abbfb0e9e7434b18792518" alt="" width="709" height="608" data-path="images/guides/admin-guide/environments/1ee51e5-screenshot_2023-01-23_at_10.png" />

<Warning>
  Task Timeouts

  Tasks have a 30 minute timeout
</Warning>

Your task will be queued and executed on the deployment container, including the local cache env zero saves between deployments. You'll be able to see your commands execute in the Deployment Logs, like any other deployment.\
During the task execution, all the variables that are defined in the environment will be available for you to use.

Tasks also support [custom flows](/guides/admin-guide/custom-flows). You can read more about the available hooks [here](/guides/admin-guide/custom-flows/#hook-stages).

## Common Tasks

* [Migrate state](https://www.terraform.io/cli/commands/init#backend-initialization): `terraform init -migrate-state -force-copy` or `echo "yes" | terraform init -migrate-state`
* [Unlock state](https://www.terraform.io/cli/commands/force-unlock): `terraform force-unlock -force LOCK_ID [DIR]`
* [Retrieve output](https://www.terraform.io/cli/commands/output): `terraform output [options] [NAME]`
* [Taint a resource](https://www.terraform.io/cli/commands/taint) `terraform taint [options] <address>`
* [Move state](https://www.terraform.io/cli/commands/state/mv): `terraform state mv [options] SOURCE DESTINATION`

<Info>
  The tools available for executing commands are the same ones that were available during your last deployment.
  If you require additional tools, make sure to update the ENV0\_INSTALLED\_TOOLS variable and run the deployment again.
</Info>

## Task Comments

You can add a comment, to let your teammates know why the task was run.\
Add a comment, by filling in the *"Comment"* input down below the `bash` input.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/db668ae-screenshot_2023-01-23_at_10.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=975fb83c3e75d6f935c5b74765e99585" alt="" width="707" height="608" data-path="images/guides/admin-guide/environments/db668ae-screenshot_2023-01-23_at_10.png" />

The comment will be displayed in the Task page.\
Markdown syntax is supported.

<img src="https://mintcdn.com/envzero-b61043c8/RwbdEslsc74czQBG/images/guides/admin-guide/environments/a35dcfd-screenshot_2023-01-22_at_14.png?fit=max&auto=format&n=RwbdEslsc74czQBG&q=85&s=70b2177d1f85b379c3e5db3871a22729" alt="" width="398" height="288" data-path="images/guides/admin-guide/environments/a35dcfd-screenshot_2023-01-22_at_14.png" />

<Info>
  **Markdown Support**

  The comment supports Markdown, so you would be able to generate even more context.
</Info>

Built with [Mintlify](https://mintlify.com).
