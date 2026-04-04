# Source: https://docs.xano.com/xano-features/advanced-back-end-features/xano-link.md

# Source: https://docs.xano.com/enterprise/enterprise-features/xano-link.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano Link

<Tip>
  The Xano Link feature is an additional add-on. Please contact your Xano representative or support for details.
</Tip>

### What is Single-Tenancy vs Multi-Tenancy

Single-tenancy means that a user is on their own dedicated server environment. Their data is completely separated and isolated from any other user. A multi-tenancy environment means users share the same server resources across a shared environment.

### How Xano Link Works

Xano Link is a feature that allows you to use a separate workspace for each client (aka tenant). Each workspace is a separate environment with its own copy of all schema, which includes the database, API, Addons, Functions, and Background Tasks. This allows for a single-tenant solution to be built on Xano.

<Info>
  Xano Link still shares the same Instance server resources across all tenants, so Link is not a true form of single-tenancy. However, it is a similar solution through data separation and workspace isolation.
</Info>

Xano Link provides the Instance owner an interface where they can publish one source workspace to many client workspaces. Changes or updates can be made to the source workspace and published to many client workspaces. This is a manual process so it requires keeping track of which client workspaces need to be updated. It is recommended to use naming conventions for the workspaces to help keep track (e.g. product\_name:source, product\_name:user\_id).

Xano Link can be accessed from the settings of the source workspace.

<Frame caption="Accessing Xano Link">
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/55e44941-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=5dbab3497a0fbf2dfebc651d817efcb1" width="2304" height="905" data-path="images/55e44941-image.jpeg" />
</Frame>

Once inside, you can choose to Link APIs, functions, addons, and database tables. Take note of the **Select All/None** and **Auto include dependencies** options to assist in ensuring that the Link only merges the data you want. You also have the option to include records from the selected database tables, or only merge the schema.

<Info>
  **Select All/None** allows you to quickly bulk select or de-select items.

  **Auto include dependencies** will scan and auto-include in the Link any items that are dependent on what you have already selected. For example, if you are choosing API endpoints that include custom functions, the functions will also be merged without you having to select them manually.
</Info>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e572f303-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=96b157ad354889d849e2f600415ee2fe" width="608" height="1232" data-path="images/e572f303-image.jpeg" />
</Frame>

### Merging Database Tables

<Frame caption="Choosing Database Tables and Records">
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/38c1ce84-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=6c256f1ba649c6c989f1b33753ba4b4f" width="866" height="719" data-path="images/38c1ce84-image.jpeg" />
</Frame>

You have the option to choose specific tables and records to merge when using Xano Link. Click on the record count to select specifically which records you want to merge, or select all.

<Frame caption="Choosing records to merge">
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a60cdf9b-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=58e62ad6183d5d850b11456f5df6a4f8" width="776" height="782" data-path="images/a60cdf9b-image.jpeg" />
</Frame>

<Warning>
  When you use Xano Link to merge database tables, and the destination workspace already has that table created, you will need to change the GUID of the destination table to match, otherwise you will have duplicate tables. The steps below will outline how to change the GUID. Please proceed with caution as you change these advanced settings.
</Warning>

1. Head to the **source table**, click the three dots in the top-right, and choose Security.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/53bc15c0-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=67f7d51cf29a8866683e8a324476ec66" width="2304" height="902" data-path="images/53bc15c0-image.jpeg" />
</Frame>

2. Click "Show Advanced Settings" and copy the GUID that is shown in the box.

<Frame caption="Copying the GUID from the source table">
  <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/9e700b42-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=92b1ed2e93d1c03a416305ed220c725f" width="864" height="1245" data-path="images/9e700b42-image.jpeg" />
</Frame>

3. After you've copied the GUID, head to the **destination table** in the new workspace, and replace the GUID with the copied value from the source table and save your changes.

Once you're ready to publish an update select which client workspaces the update should be pushed to. You also have the option to merge the newly created branch with whatever branch in the target workspace is set to live, and / or set the newly created branch as the live branch.

<Info>
  **Merge New Branch with existing Live Branch** will merge the newly created branch with the branch in the destination workspace that is currently set to live.

  **Set New Branch Live** will set the newly created branch as the live branch immediately.
</Info>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/8ec26d10-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=e0fe343b11192edf8494b4583796d66a" width="620" height="1234" data-path="images/8ec26d10-image.jpeg" />
</Frame>

#### Customization

Customization on a per-client basis is possible by using **additional** tables or APIs that are independent of the source workspace. Customization to the schema from the source workspace would get overwritten with any new updates.

### Compare Differences

Xano Link allows you to view and compare differences before merging a branch from the source workspace into a branch from the destination workspace.

Be sure to select the Merge New Branch option and the destination workspace before selecting "view.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b468fa02-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=e86800f1e2f094dbd53f8e24dc617a5d" width="445" height="774" data-path="images/b468fa02-image.jpeg" />
</Frame>

By selecting view, you can see which items contain differences.

<Frame caption="Changed items.">
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c1a7b494-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=f20894b0af7381a803f5ce14ec9a9ad6" width="435" height="820" data-path="images/c1a7b494-image.jpeg" />
</Frame>

By selecting "changes" next to an item, you can see a snapshot of the differences.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5e854ae0-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=6eff364d7e4dc2992f848d2c11399546" width="1543" height="756" data-path="images/5e854ae0-image.jpeg" />
</Frame>

In the above example there are six changes:

1. Created\_at input deleted

2. Name input edited

3. Category input edited

4. Value input edited

5. API Request function added

6. Create Variable function added


Built with [Mintlify](https://mintlify.com).