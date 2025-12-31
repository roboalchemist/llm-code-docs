# Source: https://planetscale.com/docs/vitess/scaling/workflows.md

# What are workflows?

> PlanetScale workflows provide pre-defined recipes that make it simple to run operations on your databases.

You can currently perform the following workflows:

* [Moving tables from an unsharded to a sharded keyspace](/docs/vitess/sharding/sharding-quickstart)
* Moving tables from an existing unsharded keyspace to another unsharded keyspace

If you are familiar with [Vitess Workflows](https://vitess.io/docs/reference/vreplication/workflow/), you will see some similarities. For example, the PlanetScale workflow that allows you to move tables from an unsharded to a sharded keyspace is similar to the [Vitess `MoveTables` workflow](https://vitess.io/docs/user-guides/migration/move-tables/).

## Create a workflow

To create a new workflow, select your database, and click "Workflows" in the left nav. Next, click "New workflow". Because we currently only have one available workflow, this will drop you straight into the page to create a new workflow to move tables between keyspaces.

## View workflow history

To view the history of all completed or pending workflows, click on "Workflows" in the left nav. From here, you can see all previous workflows along with information such as status, duration, and the time it took to complete.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt