# Source: https://planetscale.com/docs/vitess/schema-changes/deploy-requests.md

# Deploy requests

> Deploy requests are an integral part of the [PlanetScale workflow](/docs/vitess/best-practices).

export const VimeoEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://player.vimeo.com/video/${id}?dnt=true`} title={title} className="aspect-video w-full" allow="autoplay; fullscreen; picture-in-picture" />
    </Frame>;
};

## Overview

Database branching, coupled with deploy requests, allows you to **deploy non-blocking schema changes to your production database with zero downtime**. You can also [undo deployments](#revert-a-schema-change) without losing any data that was written during that time.

<VimeoEmbed id="830571933" title="Deploy requests overview" />

## Create a deploy request

<Note>
  Before you can create a deploy request, the branch you are merging into must have [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled.
</Note>

<Steps>
  <Step>
    Click on "**Branches**".
  </Step>

  <Step>
    Select the development branch you want to deploy into the base branch.
  </Step>

  <Step>
    This page shows you a diff of the schema against its base branch.
  </Step>

  <Step>
    To the right of the page, you'll see a dropdown that says "**Deploy to**". If you don't see this option, you likely don't have [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled on the branch you're deploying into. Go to the branch page for the branch you'd like to merge into, and enable safe migrations.
  </Step>

  <Step>
    Select the branch you want to deploy to. Again, if the branch doesn't show in the dropdown, you need to enable [safe migrations](/docs/vitess/schema-changes/safe-migrations).
  </Step>

  <Step>
    Optionally, add a comment about the deploy request.
  </Step>

  <Step>
    Click "**Create deploy request**".
  </Step>
</Steps>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=a07195e9f08d13e1e7caff6de117dce4" alt="Example of deploy request on branch page" data-og-width="2970" width="2970" data-og-height="1832" height="1832" data-path="docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=280&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=a792ed08dbafe1c25bcf87741479ca14 280w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=560&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=36696bf252d3435013663eb3b2958f5e 560w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=840&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=5b6321ea739b3ecba6cd3bacd77ea216 840w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=1100&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=5ae481a3ef39f483b93307e35311f458 1100w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=1650&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=8a693bf30c15dd27e2a73f3c57864ab9 1650w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-request-page-2.png?w=2500&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=34bfffaebd1a94b8c0900a6de42952eb 2500w" />
</Frame>

## Review a deploy request

Once you create a deploy request, you or your team can review it and, optionally, approve it before deploying it.

PlanetScale will check if the request is deployable. This process includes checking for issues like:

* [Incompatible unique keys](/docs/vitess/schema-changes/onlineddl-change-unique-keys)
* Invalid charsets (PlanetScale supports `utf8`, `utf8mb4`, `utf8mb3`, `latin1`, and `ascii`)
* Invalid foreign key constraint names or lengths
* And other various checks to ensure successful schema changes

We will also warn you about potential data loss or inconsistencies and check if there are any known conflicts with the production schema that could prevent a clean merge. While we attempt to find all possible conflicts, it is ultimately up to you to confirm merge details.

<Steps>
  <Step>
    Click the "**Deploy requests**" tab on the database dashboard page.
  </Step>

  <Step>
    Select the open deploy request you want to review.
  </Step>

  <Step>
    Under "**Summary**", you'll see if the request is deployable.
  </Step>

  <Step>
    To review the schema changes, click the "**Schema changes**" tab.
  </Step>

  <Step>
    You'll see the proposed changes here. New additions are highlighted in green, and deletions are highlighted in red.
  </Step>

  <Step>
    If you have required deploy requests to be approved before deployment, other users in your Organization will see the option to "**Approve changes**" or "**Leave a comment**" on the "**Schema changes**" tab.
  </Step>
</Steps>

<Note>
  If you are the only administrator in your Organization and you enable the "Require administrator approval for deploy requests" setting, you can self-approve your own deploy requests. If there is more than one administrator, self-approval is not allowed.
</Note>

### Reviewing changes across shards

If your deploy request contains changes to a sharded keyspace, you can see the affected shards by clicking the arrow next to each changed table. This will show the SQL that will run, and in the next tab, each shard that will be affected.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ec1241dade76dbf362911a030687646a" alt="PlanetScale deploy request - changes on sharded keyspace" data-og-width="2960" width="2960" data-og-height="1820" height="1820" data-path="docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=cda95a228ca93dffa0aa2b912f2a737c 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c60cdf1adb51c08e339cb742fd889421 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a9bb7a05d2afab11a50116a64b903d53 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=cc289d3309d063b13a1d626bd346393e 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a22ec6182117af12cbd74c3a91a782aa 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/sharded-deploy-request.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=270a275cc4c4316846be6c467f3d1573 2500w" />
</Frame>

## Deploy a deploy request

<Steps>
  <Step>
    Once the request is approved, if required, it's ready to be added to the deploy queue. Click on the "Summary" tab, and you'll see the option to deploy.
  </Step>

  <Step>
    Here you'll have the option to choose to "Deploy changes" or to "Deploy changes instantly":

    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=229df8fbf024c34758499843b2b89ae6" alt="PlanetScale deploy request - deploy options" data-og-width="2520" width="2520" data-og-height="1688" height="1688" data-path="docs/images/assets/docs/concepts/deploy-requests/deploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1a730eabeaedb36dcf7c3d041a5b93a5 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9be554f0e46d7def3d4486a48b290e38 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=edcb0aa31be203f347d761575afb7468 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3653a52aba3a7c25162fdd26d63803ff 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=102e5e9e22ea4ac2b92de0c764bf1485 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/deploy.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=450baefda533eb99b0b15d66be4cd4bc 2500w" />
    </Frame>
  </Step>
</Steps>

### Deploy changes

<Steps>
  <Step>
    (Optional) You have the option to enable [**gated deployments**](#gated-deployments), which gives you the power to control exactly when the migration cuts over. You'll see an "**Auto-apply changes**" checkbox, which is checked by default. If you uncheck this, you will get the option to apply the changes once the schema changes are complete. If you leave it checked, it will auto-deploy as soon as it's ready.
  </Step>

  <Step>
    (Optional) You also have the option to run the migration using MySQL's **ALGORITHM=INSTANT**. If you would like to deploy instantly, click the arrow next to "Deploy changes" and select "Deploy changes instantly". Gated deployments are not available for this option. See the [Deploy changes instantly](#deploy-changes-instantly) section below for more information.
  </Step>

  <Step>
    When you're ready to deploy, click "**Deploy changes**". The deployment will begin or be queued if there are other pending deployments. You will still have a short window after deploying to enable [gated deployments](#gated-deployments) in this step.
  </Step>

  <Step>
    If you enabled gated deployments (step 2), you can click "**Apply changes**" to merge the deployment to production once it completes.
  </Step>

  <Step>
    After you deploy, you have **30 minutes to "undo"** it using our [schema revert feature](#revert-a-schema-change).
  </Step>

  <Step>
    If you are deploying changes to a sharded keyspace, you'll see the progress for each shard here as well.
  </Step>
</Steps>

### Deploy changes instantly

You also have the option to use MySQL's  **ALGORITHM=INSTANT** to instantly deploy the schema change. Learn more in the [**Instant Deployments** section](#instant-deployments).

1. When you're ready to deploy, click "**Deploy changes instantly**". The deployment will begin or be queued if there are other pending deployments.
   * Though the deployment many be queued, once it's at the front of the queue, it will be deployed instantly.
   * Instant deployments **cannot be reverted**.

If you would like to require an administrator's approval before a request can be deployed, go to the "**Settings**" page for your database and check the "**Require administrator approval for deploy requests**" box. You must be an Organization Administrator to enable this restriction. Please note you will not be able to approve your own deploy requests.

## Close a deploy request

If you decide you don't want to proceed with a deploy request, you can easily close it.

<Steps>
  <Step>
    Click the "**Deploy requests**" tab on the database dashboard page.
  </Step>

  <Step>
    Select the request you want to close.
  </Step>

  <Step>
    Click on the "**Close deploy request**" button on the right-hand side.
  </Step>
</Steps>

## Deploy requests and foreign key constraints

In most cases, deploy requests should work as expected when your schema changes have [foreign key constraints](/docs/vitess/foreign-key-constraints).

There are some cases where a deploy request will not be deployable.
This includes cases where there is a mismatched column type or when a foreign key constraint references a deleted column.

For example, if we open a deploy request to add a foreign key constraint `t1_id` with type `BIGINT` on a table `t2` that references a column `id` on table `t1`, where `t1.id`'s type is `BIGINT`, the following cases would produce a linting error in the deploy request because it is not deployable:

* if, while the previously mentioned deploy request is open, someone else updates `t1.id` to a different column type, i.e., `int`.
* if, while the previously mentioned deploy request is open, someone else deletes `t1.id`.
* if, while the previously mentioned deploy request is open, someone else deletes all indexes that cover `t1.id` as their prefix. (Because in a foreign key relationship, the referenced columns on the parent table must be indexed, usually by a dedicated index, but they can be the first columns in an otherwise wider index.)

These are all cases where another user changes schema, causing the initial user's definition to be invalid MySQL.

There are also two cases where a revert would cause orphaned rows that you can read about in this document's [revert section](#when-a-revert-can-result-in-orphaned-rows).

### Validating referential integrity of existing columns

Deploy requests do not validate the referential integrity of *existing* columns. `ALTER TABLE… ADD FOREIGN KEY…` does not validate existing row relations within the context of a deploy request. Unlike standard MySQL, it is possible to add the foreign key constraint to a table with orphaned rows, and they will remain orphaned. In standard MySQL, adding a foreign key is a blocking operation, and it fails if any orphaned rows are found.

## Instant deployments

Instant deployments give you the option to run schema changes using MySQL's **ALGORITHM=INSTANT**. This is different than how our [**online schema migrations**](/docs/vitess/schema-changes/how-online-schema-change-tools-work) work.

Instant deployments will apply schema changes faster, however, these schema changes must be **auto-applied** and **cannot be reverted**.

### Who should use instant deployments?

We recommend instant deployments to experienced users that are making schema changes to large tables, or users that would like their schema changes to be deployed instantly.

### Supported operations

In order for a deploy request to be instantly deployed, *all* schema changes in the deploy request must be instantly deployable. Some of those changes include:

* Adding or dropping a column (with some exceptions)
* Changing or dropping a column's default value
* Changing an `ENUM` or `SET` definition

The following changes are examples of changes that are **not** instantly deployable:

* Changing a column's data type
* Adding a column with a non-literal default value
* Adding or dropping an index
* Adding or dropping a foreign key constraint
* Extending a `VARCHAR` column size
* Updating a column to `NULL` or `NOT NULL`

To know whether or not a deploy request is instantly deployable, look for the "Instantly deployable" badge on your deploy request. This badge will only be visible on deploy requests that can be deployed instantly.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=6eec398153b8a9a670e036e509469b0b" alt="PlanetScale deploy request - deploy instantly badge" data-og-width="2522" width="2522" data-og-height="1414" height="1414" data-path="docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=280&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=7f585d13b2398c3db2a411a52dfa2522 280w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=560&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=81d8691687a624cb065fda9965b31c09 560w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=840&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=24ade6f88b569973fef052e35d28905c 840w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=1100&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=f93651481b561e3b011d57f578dd2534 1100w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=1650&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=409df0d02944756668fdc5a655cf509e 1650w, https://mintcdn.com/planetscale-cad1a68a/1n39MWo25_njbahn/docs/images/assets/docs/concepts/deploy-requests/deploy-instantly.png?w=2500&fit=max&auto=format&n=1n39MWo25_njbahn&q=85&s=1009e44e0bab07501169bcf292239183 2500w" />
</Frame>

We recommend reading [MySQL's Online DDL documentation](https://dev.mysql.com/doc/refman/8.0/en/innodb-online-ddl-operations.html) for the full list of operations that can be deployed instantly.

## Gated deployments

Gated deployments give you more control over when a migration goes live after the deployment process completes.

As part of our non-blocking schema change process, instead of directly modifying table(s) when you deploy a deploy request, we make a copy of the affected table(s) and apply changes to the copy. We get the data from the original table and the copy table in sync, and once complete, initiate a quick cutover where we swap the tables.

<Note>
  If a deploy request includes changes to multiple tables, all tables cut over at the same time — unless there is a sequential dependency.
</Note>

With gated deployments, you can initiate the deployment, but once the table syncing is complete, we'll hold off on the cutover and let you click a button to swap the tables and complete the deployment. Gated deployments can be enabled on each deploy request by unchecking the "Auto-apply changes" box before you deploy.

This feature is helpful if you have long-running migrations. For very large or complex databases, deploying a schema change can take several hours to complete. In those scenarios, you don't want the cutover to happen while you're offline. With gated deployments, you can start the deployment process by adding your deploy request to the queue, and once it's done, you'll be able to click a button to merge it in and complete the deployment while you're there to monitor it.

### Enable gated deployments in the dashboard

<Steps>
  <Step>
    When you open a deploy request, uncheck the "**Auto-apply changes**" box.
  </Step>

  <Step>
    <Frame>
      <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=cb1e535b9f7499c8c0158e514fc3b0a8" alt="PlanetScale deploy request - Auto-apply changes checkbox unchecked" data-og-width="2450" width="2450" data-og-height="1652" height="1652" data-path="docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f7b4c397aaffcd5fcaedc1d28fe8186c 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=99a3013ae65886abf12ffb949301886e 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=076c2324e995a6d850293d70675e1360 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=da22f4d9230f162fae47a5f82304c64c 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d1691c3f0c961800931533098143e230 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/deploy-requests/gated-deployments-2.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ed4e84c9aa6f7385210ab6985971f349 2500w" />
    </Frame>

    Once your deploy requests begins running, you'll also have the option to uncheck the box here.
  </Step>

  <Step>
    When your deploy request has completed and is ready for cutover, the "**Apply changes**" button will appear. You can now complete the deployment at any time by clicking this button.
  </Step>
</Steps>

### Enable gated deployments via CLI

You can also manage auto-apply settings using the [PlanetScale CLI](/docs/cli/deploy-request).

To create a deploy request with auto-apply disabled:

```bash  theme={null}
pscale deploy-request create <DATABASE_NAME> <BRANCH_NAME> --disable-auto-apply
```

To disable auto-apply on an existing deploy request:

```bash  theme={null}
pscale deploy-request edit <DATABASE_NAME> <DR_NUMBER> --disable-auto-apply
```

Once your deploy request has completed and is ready for cutover, trigger the swap:

```bash  theme={null}
pscale deploy-request apply <DATABASE_NAME> <DR_NUMBER>
```

<Note>
  If neither `--enable-auto-apply` nor `--disable-auto-apply` is provided when creating a deploy request, the setting is inherited from the previous deploy request.
</Note>

### Limitations

* If you have an open gated deployment, you cannot deploy another deploy request until the current one has been merged in.
* Deploy requests that are [instantly deployed](#instant-deployments) cannot be gated.

For more information about this process and why we built it, check out the [Gated Deployments: Addressing the complexity of schema deployments at scale](https://planetscale.com/blog/gated-deployments-addressing-the-complexity-of-schema-deployments-at-scale) blog post.

## Artifact tables

During schema changes, Vitess creates artifact tables to facilitate non-blocking migrations. For detailed information about artifact table behavior, storage implications, and cleanup processes, see the [Artifact tables in schema changes](/docs/vitess/schema-changes/artifact-tables) documentation.

## Revert a schema change

If you ever merge a deploy request, only to realize you need to undo it, PlanetScale can handle that! You have the option to revert a recently deployed schema change while maintaining data that was written to the original schema during that time.

<Note>
  Deploy requests that are instantly deployed *cannot* be reverted.
</Note>

### How to revert a schema change

You can revert a deployment for **up to 30 minutes** after the deploying. After the 30 minute period is up, the deployment becomes permanent, and you will no longer have the option to revert.

<VimeoEmbed id="830571822" title="Revert a schema change" />

<Steps>
  <Step>
    Select the deploy request you want to revert.
  </Step>

  <Step>
    To revert the schema changes made with the deploy request, click "**Revert changes**" and confirm.
  </Step>

  <Step>
    We will immediately revert the base branch back to its previous schema.
  </Step>

  <Step>
    Any data that was written to the original schema in the time between deploying and reverting will remain in your database after the revert.
  </Step>

  <Step>
    The deploy request will be closed, but the branch will remain for you to continue development on if you choose.
  </Step>
</Steps>

### When is data not retained

There are some scenarios where some data is not retained when you revert your changes.

1. You add a table or column to your schema and then revert it. If any data was written to those newly introduced fields between deployment and reverting, that data will not be retained upon revert, as the fields will no longer exist.

### When a revert can result in orphaned rows

In some cases, when you are using foreign key constraints, a revert of a deploy request can result in orphaned rows. These can happen when your schema change is:

* Dropping a foreign key constraint: Once a foreign key constraint is dropped, new data written to the table is less constrained. Reverting this change may result in data that is inconsistent with the dropped foreign key constraint.
* Dropping a table with foreign key constraints: When a table with foreign key constraints is dropped, the parent table(s) will continue to be written to. If this change is reverted, data in the table that was dropped may no longer be consistent with its foreign key constraints.

<Note>
  You must enable [foreign key constraint](/docs/vitess/foreign-key-constraints) support in the database settings page before using them.
</Note>

### When are you unable to revert a schema change

There are also some edge cases where reverting a schema change is not possible. We will always attempt to revert, but if there are scenarios where your data integrity is at risk, we will not proceed with the revert. The following are some cases where a revert will fail:

1. If you deploy a schema change that expands the length of some column, such as changing from `VARCHAR(10)` to `VARCHAR(50)`, and add new data larger than 10 characters to it, a revert attempt may fail. This is to protect your data. You may have written data to the `VARCHAR(50)` field in that time that will not fit in the smaller 10 character space. If no data is added between deployment and revert, the revert process can proceed.
2. Some examples of other similar scenarios where revert won't be possible (again, only if larger sized data is added between deployment and revert) are:
   * `INT` to `BIGINT`
   * `NOT NULL` to `NULL`
   * `TIMESTAMP` to `TIMESTAMP(6)`
   * `utf8` to `utf8mb4`
   * Any other operation that expands the size of a field
3. If you deploy a schema change that removes a unique key or relaxes a unique constraint, and in the time between deployment and attempting to revert, you insert rows that would otherwise conflict with that constraint, the revert may fail.
4. Another uncommon but possible scenario: you deploy a schema change that has a `NOT NULL` column without a `DEFAULT` value, combined with an `ALTER TABLE DROP COLUMN` statement for that column. If you insert some rows between the deployment and the revert attempt, the revert will fail. We will not be able to re-add that column for the newly inserted rows and will not know how to populate it.

For an in-depth look at how this process works, check out our [Behind the scenes: how schema reverts work](https://planetscale.com/blog/behind-the-scenes-how-schema-reverts-work) blog post.

### Schema revert and migration data

If you've selected a migration framework or specified a table with migration data in the settings tab of your database, the data within the table that tracks migrations will be moved to the production branch only after the revert window has been closed. This is to ensure that if the deploy request is reverted, the production branch has the correct log of applied migrations.

### Billing considerations

You may see some temporary `_vt` tables in your database. These are called [artifact tables](/docs/vitess/schema-changes/artifact-tables) and are used to facilitate the deployment and revert process. They do not count toward your storage costs if you're using [network-attached storage](/docs/plans/planetscale-skus#network-attached-storage).

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt