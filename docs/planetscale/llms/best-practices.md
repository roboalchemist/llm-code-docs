# Source: https://planetscale.com/docs/vitess/best-practices.md

# PlanetScale workflow for Vitess

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3248003ec557ff31fd529bf8e2eb717c" alt="Diagram showing PlanetScale workflow" data-og-width="1511" width="1511" data-og-height="407" height="407" data-path="docs/images/planetscale-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a0a07a5c2c44f8b140e904ba8e968b0f 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=550934b3f690b2c665e1278effac6b68 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f0c0f8e6e8e4aaa56138460392d44e67 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=dfd39c2550b147efff8542d7ba1d8af6 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c9d5fa068ed136fd1d0a570a8d382ce3 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/planetscale-workflow.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=8294de9fea0486702918a8cd142f1a0c 2500w" />
</Frame>

PlanetScale databases are designed for developers and developer workflows. Deploy a fully managed database cluster with the reliability of MySQL (our databases run on MySQL 8) and the scale of open source Vitess in just minutes.

Deploy, branch, and query your database directly from the UI, download our [CLI](https://github.com/planetscale/cli#installation) and run commands there, or automate your deployments using our [GitHub Actions](/docs/vitess/integrations/github-actions) and [API](/docs/api/reference/getting-started-with-planetscale-api).

Built-in connection pooling means you’ll never run into connection limits for your database.

## PlanetScale branching

The PlanetScale branching feature allows you to treat your databases like code by creating a branch of your production database schema to serve as an isolated development environment.

PlanetScale provides two types of database branches: **development** and **production**.

Development branches provide isolated copies of your database schema where you can make changes, experiment, or run CI against. Instantly branch your production database to create a staging environment for testing out your schema changes.

Production branches are highly available databases intended for production traffic. They include an additional replica for high availability and are automatically backed up daily.

Branches can also have [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled for zero-downtime schema migrations, protection against accidental schema changes, and enhanced team collaboration through [deploy requests](/docs/vitess/schema-changes/deploy-requests).

We also offer a [Data Branching®](/docs/vitess/schema-changes/data-branching) feature, which allows you to create an isolated replica of your database for development that includes both the schema **and** data.

Learn more about [database branching](/docs/vitess/schema-changes/branching).

## Non-blocking schema changes

PlanetScale makes it safe to deploy schema changes to production and easy to automate schema management as a part of your CI/CD process. Schema changes to production branches with safe migrations enabled are applied online and protect against changes that block databases, lock individual tables, or slow down production during the migration.

Use a development branch to apply schema changes and view the schema diff in the UI or the CLI. Once you’re satisfied with your schema changes, you can open a deploy request.

Learn more about [non-blocking schema changes](/docs/vitess/schema-changes).

## Deploy requests

<Note>
  Your database must have a branch with [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled before you can create a deploy request.
</Note>

[Deploy requests](/docs/vitess/schema-changes/deploy-requests) allow you to propose schema changes and get feedback from your team. The deploy requests display DDL statements (`CREATE`, `ALTER`, and `DROP`) for each table changed, with a line-by-line schema diff, making it easy to review the changes.

For example, you can pair deploy requests with GitHub pull requests so that your teammates can review the code and the schema changes in parallel.

PlanetScale also analyzes your schema changes for conflicts when you open a deploy request. It checks against the production schema at the time the branch was created and against the current production schema which may have changed in the interim. This ensures your changes can be deployed safely without impacting production.

## Deploy a schema change

Once a deploy request has been approved, it gets added to the deploy queue. Schema changes are applied to your production database branch in the order in which they are added to the deploy queue.

As a part of the process of adding the schema changes to the deploy queue, PlanetScale analyzes the schema changes in the deploy requests ahead of your deploy request for any potential conflicts. If a conflict exists, your deploy request is rejected from the queue, and you are immediately notified of the conflict. This means you’ll never wait for your schema change to deploy only to learn that there’s an unanticipated conflict. This is especially useful if long running schema changes are being applied.

## Revert a schema change

If you ever deploy a schema change, only to realize you need to undo it, PlanetScale can handle that. With our [schema revert feature](/docs/vitess/schema-changes/deploy-requests#revert-a-schema-change), you have 30 minutes to "undo" a schema change deployment. Simply click the "Revert changes" button on the affected deploy request page and your production database will instantly revert back to the previous schema. Additionally, any data that was added to your production database in the time between deployment and reverting will be retained. Learn more about this process in our [Revert a schema change section](/docs/vitess/schema-changes/deploy-requests#revert-a-schema-change) of our deploy requests documentation.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt