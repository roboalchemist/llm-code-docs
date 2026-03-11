# Source: https://docs.xano.com/team-collaboration/branching-and-merging.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Branching & Merging

<Info>
  **Prefer Git?** If you're using the [Xano CLI](/xano-cli/get-started) for local development, you can use standard Git branching, diffs, and PRs alongside Xano's [push & pull](/xano-cli/push-pull) workflow instead of Xano's built-in branching. Use whichever fits your team — or both together.
</Info>

A Branch is a copy of a workspace's business logic (APIs, Functions, Addons, and Tasks). They are most useful for testing and developing new versions of your app without affecting your customers' primary experience.

You can create new Branches and select which Branch to make a copy of, choose which Branch to make edits to, and select which Branch you want to be live for your API.

**Branches can also [merge](/team-collaboration/branching-and-merging#merging) from a source Branch to a destination Branch to make managing development, test, and live environments as seamless as ever**.

Your initial Branch will be considered v1 of your business logic. Below your workspace name, you will be able to identify which Branch you are currently editing.

## Create a New Branch

<Tip>
  Branches do not apply to the database. To enable test data sources, see [Data
  Sources](/the-database/database-basics/data-sources).
</Tip>

Select the Branch identifier located underneath the workspace name.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211259.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=28e80d95a76fe294d70c7460b731c64b" alt="branching-and-merging-20250925-211259" width="564" height="426" data-path="images/branching-and-merging-20250925-211259.png" />

This will allow you to see and change which Branch you are currently editing and which is live for your users, and allow you to add a new Branch.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211404.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=a4da2664e76826c18316d85a68bf9b2e" alt="branching-and-merging-20250925-211404" width="552" height="838" data-path="images/branching-and-merging-20250925-211404.png" />

When you select Add new Branch you will be able to choose a source Branch to make a copy from, the name of your new Branch, set a color, and add a description.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211443.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=f33bab776629301bcf9076d659e9f9c7" alt="branching-and-merging-20250925-211443" width="553" height="742" data-path="images/branching-and-merging-20250925-211443.png" />

The color you select will be reflected in different elements of the Xano UI to represent and easily inform which branch you are currently working on.

Adding a new Branch makes a copy of the source Branch at that given time. So for example, if you create v2 from source Branch v1, you will have all the same business logic (APIs, Functions, Addons, and Tasks).

## Change which Branch to Edit and Set Live

The Branch you are currently editing will be identified underneath the workspace name on the left menu column and in the top banner.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211520.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=d62f6e61b4664bee5359ac85b81a94cf" alt="branching-and-merging-20250925-211520" width="804" height="367" data-path="images/branching-and-merging-20250925-211520.png" />

To change which branch you are editing, head back to the branches, select the branch you'd like to edit, and click Edit.

When editing a Branch that is not live, the Swagger documentation and API Endpoint URL buttons will provide the version of that branch and not the live Branch.

To get the URL of the live branch, either remove the :branch name after the canonical or switch back to editing the live branch.

When you're ready to set a branch live, you can do so from the same menu.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211610.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=7f5f79b12b549c628e048b7aad067d50" alt="branching-and-merging-20250925-211610" width="553" height="523" data-path="images/branching-and-merging-20250925-211610.png" />

When a Branch is set live, the changes are immediately available to your users.

If you wish to call an API endpoint from a Branch that is not live, you can do so by adding the branch name after the canonical ID in the URL, for example:

If the live branch is:

```txt  theme={null}
https://xb17-511e-40b9.xano.io/api:b4afb8/tutorial
```

You can access a different branch by adding :branch name after the canonical:

```txt  theme={null}
https://xb17-511e-40b9.xano.io/api:b4afb8:v2/tutorial
```

You can also send a special header in your API requests, X-Branch header, followed by the Branch name. For example:

```
X-Branch: v2
```

## Compare Differences (Compare Branches)

Comparing differences allows you to see the differences between a source branch and a destination branch. Comparing differences gives you full context into what's going to change before you decide to [merge branches](/team-collaboration/branching-and-merging#merging).

### How to compare branches

To compare branches, select **Compare Branches** from the branches menu.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211829.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=b10fb0efe589fe03ae9dd03b1f9dcedd" alt="branching-and-merging-20250925-211829" width="650" height="381" data-path="images/branching-and-merging-20250925-211829.png" />

#### Step 1 - Select the branch to compare from

First, select the branch to compare from. This is considered the source branch.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-211853.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=afd4fb9a18c936a0c0b29a88b59a42c8" alt="branching-and-merging-20250925-211853" width="554" height="583" data-path="images/branching-and-merging-20250925-211853.png" />

#### Step 2 - Select the destination branch to compare to.

Next, select the destination branch to compare to. If you were to merge, this is the branch to merge into.

<Info>
  Comparing mode will not commit to a merge; it is simply an opportunity to see and compare differences between the branches. You will only merge by selecting the merge option on the branches menu.
</Info>

The **Compare Branches** modal will open, showing you all the differences between the source branch and the destination branch, separated by workflow. On the left-hand side, you'll see a list of everything that's been updated. Selecting an item will present you with a diff view, written in (XanoScript)\[/xanoscript/introduction] to show you exactly what has changed.

Additions are highlighted in green, and deletions are highlighted in red.

<img src="https://mintcdn.com/xano-997cb9ee/s2E-yK-xHnbLvltY/images/branching-and-merging-20251019-105243.png?fit=max&auto=format&n=s2E-yK-xHnbLvltY&q=85&s=e9fb3ac482319a6921dce209b334b2ba" alt="branching-and-merging-20251019-105243" width="1053" height="718" data-path="images/branching-and-merging-20251019-105243.png" />

Use the <span class="ui-bubble"> > </span> and <span class="ui-bubble"> \< </span> buttons in the top-right to navigate between changes.

<img src="https://mintcdn.com/xano-997cb9ee/s2E-yK-xHnbLvltY/images/branching-and-merging-20251019-105342.png?fit=max&auto=format&n=s2E-yK-xHnbLvltY&q=85&s=8990835d0194706da89cca941d23eb7c" alt="branching-and-merging-20251019-105342" width="732" height="376" data-path="images/branching-and-merging-20251019-105342.png" />

## Merging

Merging Branches allows for seamless development management of different environments. It allows you to update a destination Branch with changes and updates created from a source Branch. Merging will include changes to published objects such as APIs, Functions, Addons, and Tasks, and newly created ones.

For example, your live Branch is v1. You are editing v2, which has some new API endpoints for a new feature you are rolling out. During the development phase of v2, you had to modify an API endpoint in v1. When you're ready to merge v2 into v1, Xano will add the new API endpoints from v2 and maintain the update to the API endpoint on the destination v1 Branch.

### How to Merge

To merge Branches open the Branches menu by selecting the Branch name under the Workspace name in the left-hand navigation bar.

Next, select **Merge Branches**.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-213835.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=399589a000955f491aa072735414801f" alt="branching-and-merging-20250925-213835" width="496" height="309" data-path="images/branching-and-merging-20250925-213835.png" />

After selecting Merge Branches, Xano will ask you to select the source Branch.

<Info>
  **The Source Branch is the Branch containing the updates and modifications** that you want to merge into the Destination Branch.
</Info>

Next, select the Destination Branch to merge the changes from the Source Branch.

You'll then be taken to the Merge Branches modal, which is very similar to the Compare Branches modal detailed above, but with a few additional options for performing the merge.

In the top-right, you'll see a <span class="ui-bubble"> BACKUP DESTINATION </span> option. This allows you to toggle on/off automatic backup of the destination branch before merging. It's recommended to leave this on to ensure you have a restore point if needed.

On the left, using the checkboxes, you can select what to include in the merge. By default, all changes will be selected.

Once satisfied with all the updates included in the merge, click <span class="ui-bubble">Merge</span> in the bottom-right to merge the Branches.

## Dealing with Merge Conflicts

<Steps>
  <Step title="Compare the differences between the branches to see where the conflict lies">
    Learn more about comparing branches [here](/team-collaboration/branching-and-merging#compare-differences-compare-branches).
  </Step>

  <Step title="If you receive a merge conflict notice but there is no apparent conflict, you might have a function stack with the same name, but a different GUID.">
    <Warning>
      **If you aren't sure updating the GUID is necessary in your situation, please reach out to support before proceeding.**
    </Warning>

    Head to the settings of the function stack and choose **Security**.

        <img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-214133.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=ad2af4e75deb4f26dddefa9171ce6ff6" alt="branching-and-merging-20250925-214133" width="399" height="273" data-path="images/branching-and-merging-20250925-214133.png" />

    You can update the GUID in the \*\*destination branch \*\*to match the function stack of the same name from the **source branch**

        <img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-214151.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=aeda7786a5a21bf616c51caf4b12ba33" alt="branching-and-merging-20250925-214151" width="400" height="315" data-path="images/branching-and-merging-20250925-214151.png" />
  </Step>
</Steps>

## Workspace Triggers for Branch Merges

From your workspace settings, you have the option to enable triggers based on certain events.

* Branch Live - Any time a branch status is set to live

* Branch Merge - When a branch is merged

* Branch New - When a new branch is created

From your Dashboard, access the menu from the top-right corner, and choose Triggers.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-214245.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=000fad3baaa33431bf77c6a35a173a1c" alt="branching-and-merging-20250925-214245" width="400" height="461" data-path="images/branching-and-merging-20250925-214245.png" />

Choose 'Add Workspace Trigger' and provide the requested information. In the example below, we are creating a trigger called My Workspace Trigger that will run anytime a branch merge takes place, or a new branch is created.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-214302.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=bc422d76c12c02e307a16a543db97cb8" alt="branching-and-merging-20250925-214302" width="399" height="786" data-path="images/branching-and-merging-20250925-214302.png" />

Your Workspace Trigger will have three inputs defined. Inputs for triggers can not be modified.

* to\_branch - Information regarding the destination branch

* from\_branch - Information regarding the source branch

* action - The action taking place

Now that your trigger is set up, you can build a function stack that will run every time one of the actions selected takes place.

## Restoring a Branch Backup

If after you have merged branches, you would like to restore from a backed up branch, click on the branches option, and check the "Include Backups" checkbox. This will show you all available backups, which you can then click and edit or set live just like any other branches. Setting live the backed up branch will allow you to quickly roll back to before the merge was made.

<img src="https://mintcdn.com/xano-997cb9ee/2JwmgFtXYDlaNpNH/images/branching-and-merging-20250925-214329.png?fit=max&auto=format&n=2JwmgFtXYDlaNpNH&q=85&s=0da78925e9c399b6fd06403ec70bf81b" alt="branching-and-merging-20250925-214329" width="517" height="326" data-path="images/branching-and-merging-20250925-214329.png" />


Built with [Mintlify](https://mintlify.com).