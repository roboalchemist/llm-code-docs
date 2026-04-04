# Source: https://planetscale.com/docs/vitess/schema-changes/safe-migrations.md

# Safe migrations

> Safe migrations is an optional but highly recommended feature for branches in PlanetScale. With safe migrations enabled on a branch, you’ll gain zero-downtime schema migrations, schema reverts, and protection against accidental schema changes. The safe migrations setting is recommended for all production database branches to prevent downtime and unintentional data loss during schema migrations.

## Zero-downtime schema migrations

Safe migrations enable the [PlanetScale workflow](/docs/vitess/best-practices) on a given branch and allow your team to create deploy requests to merge schema changes into that branch. When changes are merged using deploy requests, a ghost table will be created with the desired schema changes. Your data will be continuously synchronized with that table until you decide to apply the changes.

## Schema revert

Safe migrations and deploy requests provide the option to quickly [revert schema changes](/docs/vitess/schema-changes/deploy-requests#revert-a-schema-change) if you discover that they are not compatible with your application. With schema revert enabled for a database, the old table is retained. You’re provided a 30-minute window where data will still be synchronized as writes occur on the new table. If you decide to revert your changes, the status of the two tables is flipped, bringing the former table back.

## Protection against accidental schema changes

To prevent accidental changes to the database schema, which may cause downtime, safe migrations enforce the use of [branching](/docs/vitess/schema-changes/branching) and [deploy requests](/docs/vitess/schema-changes/deploy-requests). This requires that changes be made safely and allows all team members to check and comment on schema changes before they are applied.

With safe migrations enabled, Data Definition Language (DDL) statements issued to branches with safe migrations enabled will automatically be rejected by PlanetScale. Any `CREATE`, `ALTER`, or `DELETE` commands, whether sent using the PlanetScale built-in console, terminal, or MySQL GUI, will fail when we receive them.

## Staging branches

You can use a development branch with safe migrations enabled to set up a workflow with a “staging” branch. First, make sure you have safe migration enabled for your main production branch. Then, create a “staging” branch with your main production branch as the base and turn on safe migrations. All new branches created for development can use this “staging” branch as the base branch.

You can then open a deploy request against either the main production or “staging” branch. Once it is deployed to “staging,” you can open a deploy request against the main production branch. The main production branch must be set as the default branch (found in your database's “Settings” page) to open a deploy request against it.

<Note>
  In this setup, the “staging” branch is still a development branch. Compared to your production branch, it will have reduced resources, similar to other development branches.
</Note>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=20e51f36f0f5bba30a6144fcb88da38b" alt="View of the Branches tab with main <- staging <- dev branches" data-og-width="2666" width="2666" data-og-height="1068" height="1068" data-path="docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=fec815a5dc354f6a1f5e92d6cafffc50 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f8bfda07b953fea00bf770d037f5bb63 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0ddf30c62b8c83e80d42fb442977be85 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e366cff1aea7aefe20dc3411be5d5cd2 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2970428b8a650341f2a9a93cf8c8e0eb 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/branches-with-staging-branch.jpg?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=002f8be68218bc4cbbb4bfad6dcc6b98 2500w" />
</Frame>

## How to enable safe migrations

Safe migrations can be enabled using the PlanetScale dashboard or the pscale CLI.

### Using the PlanetScale dashboard

To enable safe migrations on a branch, select the branch you want to modify from the branch dropdown and click the **”cog”** in the upper right of the infrastructure card on the ”**Dashboard**” tab of the database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d77aff926810f9aced640b9042f2825a" alt="The production branch UI card." data-og-width="1096" width="1096" data-og-height="801" height="801" data-path="docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a70e2e792c9be9d9910b72f60dba486e 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=dc711c27836592b1c1383b81991237e9 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a378c5c5f3d96cab07b9f6d8d3574ac6 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=69937667ea353b7fd6592ef34cca3f0b 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=831545989868b18c8a9f7677d79d6fd9 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-disabled-2.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=badcd818b18072b14bc1585c56a79054 2500w" />
</Frame>

In the modal, toggle the option labeled **”Enable safe migrations”**, then click the **”Enable safe migrations”** button to save and close the modal.

The UI card will reflect the status of the safe migrations for that branch.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e0972c621c9b01378df27a9dde76bc10" alt="Branch UI card with safe migrations enabled." data-og-width="1074" width="1074" data-og-height="792" height="792" data-path="docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7458fc89a527d68a5f46b11de6734cb5 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=08e502c38d2fdd07f8836d526c1810cb 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d45279dc3f7f2534ee71e24db6806eb9 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7e315c47cc1df73f3a291230b8e419a8 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f911c9e3abc2eeae5a115bb691759799 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/production-branch-card-with-sm-enabled-2.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5251d91ac8bcea5dede883f99806974e 2500w" />
</Frame>

You can also access the same settings from the **”cog”** on a branch overview page (from the **”Branches”** tab, then select the branch you want to view or modify).

### Using the pscale CLI

To enable safe migrations on a branch using the pscale CLI, use the following command in your terminal:

```
pscale branch safe-migrations enable <DATABASE\_NAME> <BRANCH\_NAME>
```

## How to disable safe migrations

There are two ways to disable safe migrations: the PlanetScale dashboard and the CLI.

### Using the PlanetScale dashboard

To disable safe migrations, click the **”cog”** in the upper right of the infrastructure card on the ”**Dashboard**” tab of the database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=472cb2e74a1c1a77bcf63927ee18270c" alt="Branch UI with enabled with cog highlighted." data-og-width="1074" width="1074" data-og-height="792" height="792" data-path="docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bdda7a5ef3db38524a81aabb83b8dbf5 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=4c24a90a6fa11d4a3d887eb89adf1610 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=3edcf9a13deb889fc8b3627cff152989 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=34c964ac1e63f836a2e01dfe1b48d10e 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=68d659f197d3b3ca5d909babbaa3df5a 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/safe-migrations/prod-card-cog-2.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=70c0a8af2f4dc13f6a3183dc52229936 2500w" />
</Frame>

In the modal, toggle the option labeled **”Enable safe migrations,”** then click the **”Disable safe migrations”** button to save and close the modal.

You can also access the same settings from the **”cog”** on a branch overview page (from the **”Branches”** tab, then select the branch you want to view or modify).

### Using the pscale CLI

To disable safe migrations on a branch using the pscale CLI, use the following command in your terminal:

```
pscale branch safe-migrations disable <DATABASE\_NAME> <BRANCH\_NAME>
```

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt