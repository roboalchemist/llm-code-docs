# Source: https://pipedream.com/docs/projects/access-controls.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Access Controls

The [projects list view](https://pipedream.com/projects) contains **Owner** and **Access** columns.

**Owner** indicates who within the workspace owns each project. This is typically the person who created the project.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/11ae1995-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=24f634f9bde40f669c19bb30f4da5180" width="3840" height="1968" data-path="images/11ae1995-image.png" />
</Frame>

<Warning>
  Projects created before February 2024 don’t automatically have owners, which has no functional impact.
</Warning>

**Access** indicates which workspace members have access to each project, and this can be displayed as “me”, “Workspace”, or “N members”.

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d2aecba9-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=5ae2e3bc05bb08dc4aa35e22695a20c5" width="3840" height="1968" data-path="images/d2aecba9-image.png" />
</Frame>

## Permissions

Workspace owners and admins are able to perform all actions in projects, whereas workspace members are restricted from performing certain actions in projects.

| Operation                                                    | Project creator | Workspace members |
| ------------------------------------------------------------ | --------------- | ----------------- |
| View in [projects listing](https://pipedream.com/projects)   | ✅               | ✅                 |
| View in [Event History](https://pipedream.com/event-history) | ✅               | ✅                 |
| View in global search                                        | ✅               | ✅                 |
| Manage project workflows                                     | ✅               | ✅                 |
| Manage project files                                         | ✅               | ✅                 |
| Manage project variables                                     | ✅               | ✅                 |
| Manage member access                                         | ✅               | ❌                 |
| Manage GitHub Sync settings                                  | ✅               | ❌                 |
| Delete project                                               | ✅               | ❌                 |

<Note>
  **Workspace admins and owners have the same permissions as project creators for all projects in the workspace.**
</Note>

## Managing access

<Note>
  By default, all projects are accessible to all workspace members. Workspaces on the [Business plan](https://pipedream.com/pricing) can restrict access for individual projects to specific workspace members.
</Note>

You can easily modify the access rules for a project directly from the [project list view](https://pipedream.com/projects), either by clicking the access badge in the project row (fig 1) or clicking the 3 dots to open the action menu, then selecting **Manage Access** (fig 2).

Via the access badge (fig 1):

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/01b7c218-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=a047fb81cafe2cc543d8597d0db847db" width="3840" height="1968" data-path="images/01b7c218-image.png" />
</Frame>

Via the action menu (fig 2):

<Frame>
  <img src="https://mintcdn.com/pipedream/nKh6d_6A4aXFb6xD/images/fe9589a7-image.png?fit=max&auto=format&n=nKh6d_6A4aXFb6xD&q=85&s=0f892714f0934f23853b5e67d93f0350" width="3840" height="1968" data-path="images/fe9589a7-image.png" />
</Frame>

From here, a slideout drawer reveals the access management configuration:

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/bcd7bbaf-image.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=d27622a47f953efaf83bbc6a981f2dfb" width="3840" height="2289" data-path="images/bcd7bbaf-image.png" />
</Frame>

Toggle the **Restrict access to this project** switch to manage access:

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/5933f304-image.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=adebccb7e4587d7399d3bdbaff78c394" width="3840" height="2289" data-path="images/5933f304-image.png" />
</Frame>

Select specific members of the workspace to grant access:

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/c251d0ca-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=1f26579efd039e60e07eae86ad1a860a" width="3840" height="2289" data-path="images/c251d0ca-image.png" />
</Frame>

You can always see who has access and remove access if necessary:

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/13812ecb-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=3145898c2a4e95487d9976b3bc32d058" width="3840" height="2289" data-path="images/13812ecb-image.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
