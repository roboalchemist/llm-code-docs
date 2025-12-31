# Source: https://planetscale.com/docs/vitess/scaling/cluster-sizing.md

# Source: https://planetscale.com/docs/plans/cluster-sizing.md

# Cluster sizing

export const YouTubeEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://www.youtube-nocookie.com/embed/${id}?rel=0`} title={title} className="aspect-video w-full" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" />
    </Frame>;
};

You can easily upsize and downsize your database cluster from within the PlanetScale dashboard. This documentation covers some information about selecting a cluster size upon database creation as well as how to upsize and downsize.

<Note>
  If you are on a consumption commitment plan, please be aware that any changes in cluster size will be reflected against your monthly or annual consumption commitment amount. Changes to the originally selected cluster size may cause you to utilize this amount either more quickly or slowly. If you have further questions, please reach out to your account manager or our [Support](https://planetscale.com/contact) team.
</Note>

<YouTubeEmbed id="y94VExata3A" title="Resize your database" />

## Selecting a cluster size

Selecting the correct cluster size for your database can have a dramatic impact on how it performs and how much it costs.

A good rule of thumb is when you notice CPU usage is consistently at or close to 100% for an extended period of time, you may benefit from [upsizing your cluster](/docs/plans/planetscale-skus#upsizing-and-downsizing-clusters). Conversely, if your CPU usage is consistently below 50%, you may be able to downsize. You can monitor your CPU usage by clicking on your database, clicking "Primary" in your architecture diagram, and referencing the chart under "Metrics and performance".

<Warning>
  For Metal instances, you have to consider both the compute and the storage, as storage does not autoscale. For more information about adjusting a Metal instance, see [Upgrading an existing database to Metal](/docs/metal/create-a-metal-database#upgrading-an-existing-database-to-metal).
</Warning>

There are also special cases where you may want to temporarily upsize out of caution if you're anticipating a large spike in traffic, such as during a launch or event. In these cases, you can easily [upsize](/docs/plans/#upsizing-and-downsizing-clusters) ahead of your event, and then downsize after.

If you are switching between [network-attached storage](/docs/plans/planetscale-skus#network-attached-storage) (Amazon Elastic Block Storage or Google Persistent Disk) and [Metal](/docs/plans/planetscale-skus#metal), or changing the size of your Metal instance, be aware this switch takes additional time.

### Comparing PlanetScale to other database providers

If you are migrating from an existing cloud provider with resource-based pricing, be sure to compare your currently selected instance with our available cluster sizes.

Keep in mind, each database comes with a production branch with two replicas. Vitess databases include 1,440 hours worth of development branches. The development branches essentially equate to two extra "always on" databases. In many cases, you can deprecate your dev/staging databases that you pay extra for with other providers in favor of the development branches. In the end, this usually results in significant cost savings.

Databases in PlanetScale also come with additional beneficial infrastructure that is not easily configured or available in other hosted database solutions. For more information on what is provisioned with each database, read our [Vitess Architecture](/docs/vitess/architecture) and [Postgres Architecture](/docs/vitess/architecture) docs.

If you are unsure which plan or cluster size is right for your application, [contact us](https://planetscale.com/contact) to get further assistance.

Our self-serve plans are flexible enough to handle the majority of customers. However, there are several use cases where you may need a more custom plan. This is where our Enterprise offerings shine.

## Sharding with Vitess

You can create sharded Vitess keyspaces on any plan by adding a new sharded keyspace using the [cluster configuration page](/docs/vitess/cluster-configuration) and running an [unsharded to sharded workflow](/docs/vitess/sharding/sharding-quickstart) in your dashboard.

If you would like additional support from our expert team, our [Enterprise plan](/docs/planetscale-plans#planetscale-enterprise-plan) may be a good fit. [Get in touch](https://planetscale.com/contact) for a quick assessment.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt