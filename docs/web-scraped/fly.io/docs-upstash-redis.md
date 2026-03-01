# Source: https://fly.io/docs/upstash/redis/

Title: Upstash for Redis®*

URL Source: https://fly.io/docs/upstash/redis/

Markdown Content:
[Docs](https://fly.io/docs/)[Upstash](https://fly.io/docs/upstash)Upstash for Redis®*![Image 1: Illustration by Annie Ruygt of a puzzle box figure holding two slices of cake](https://fly.io/static/images/redis-upstash.png)
*Redis is a registered trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Fly.io is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Fly.io.

[Upstash for Redis](https://docs.upstash.com/redis) is a fully-managed, Redis-compatible database service offering global read replicas for reduced latency in distant regions. Upstash databases are provisioned inside your Fly organization, ensuring private, low-latency connections to your Fly applications.

See the [What you Should Know](https://fly.io/docs/upstash/redis/#what-you-should-know) section for more details about how Upstash Redis operates on Fly.io.

[](https://fly.io/docs/upstash/redis/#create-and-manage-a-redis-database)Create and manage a Redis database
-----------------------------------------------------------------------------------------------------------

Creating and managing databases happens exclusively via the [Fly CLI](https://fly.io/docs/flyctl/install/). Install it, then [signup for a Fly account](https://fly.io/docs/getting-started/sign-up-sign-in/).

### [](https://fly.io/docs/upstash/redis/#create-and-get-status-of-a-redis-database)Create and get status of a Redis database

If you’re using Sidekiq, BullMQ or similar software, consider switching your database to a [fixed price plan](https://fly.io/docs/upstash/redis/#fixed-price-plans) to avoid running up your pay-as-you-go bill.

```
flyctl redis create
```

```
? Select Organization: fly-apps (fly-apps)
? Choose a primary region (can't be changed later) Madrid, Spain (mad)
? Optionally, choose one or more replica regions (can be changed later): Amsterdam, Netherlands (ams)
```

### [](https://fly.io/docs/upstash/redis/#the-upstash-web-console)The Upstash web console

To view more details about database usage, connection strings, and more, use:

```
flyctl redis dashboard <org_name>
```

### [](https://fly.io/docs/upstash/redis/#list-your-databases-and-view-status)List your databases and view status

Get a list of all of your Redis databases.

```
flyctl redis list
```

```
ID              NAME                ORG             PLAN    PRIMARY REGION  READ REGIONS
aaV829vaMVQGbi5 late-waterfall-1133 fly-apps        payg    mad             ams
```

Note the database name, then fetch its status.

```
fly redis status late-waterfall-1133
```

```
Redis
  ID             = aaV829vaMVDGbi5
  Name           = late-waterfall-1133
  Plan           = Pay-as-you-go
  Primary Region = mad
  Read Regions   = ams
  Private URL     = redis://password@fly-late-waterfall-1133.upstash.io
```

### [](https://fly.io/docs/upstash/redis/#connect-to-a-redis-database)Connect to a Redis database

If you have `redis-cli` installed, you can connect directly to your Redis database and run commands.

```
fly redis connect
? Select a database to connect to empty-water-3291 (sjc) 200M
Proxying local port 16379 to remote [fdaa:0:6d6b:0:1::3]:6379
127.0.0.1:16379> set foo bar
OK
127.0.0.1:16379> get foo
"bar"
127.0.0.1:16379>
```

### [](https://fly.io/docs/upstash/redis/#update-a-redis-database)Update a Redis database

Upstash Redis instances can’t change their primary region or name, but the following may change:

*   Read regions 
*   Pricing plan 
*   Eviction settings 

Use `flyctl redis update` and follow the prompts. Changing region settings doesn’t cause downtime.

### [](https://fly.io/docs/upstash/redis/#delete-a-redis-database)Delete a Redis database

Deleting a Redis database can’t be undone. Be careful!

```
fly redis destroy my-redis-db
```

```
Your Redis database my-redis-db was deleted
```

[](https://fly.io/docs/upstash/redis/#what-you-should-know)What you should know
-------------------------------------------------------------------------------

Your databases run within Fly.io infrastructure, but not inside your organization’s network. So you’re only paying Upstash pricing - not additional VM costs.

All Upstash Redis databases are replicated within the same region in a highly-available configuration. This means that hardware failures generally don’t affect Upstash software, and therefore, your databases. Upstash also keeps regular backups of data in storage outside of Fly.io.

Once provisioned, the database primary region cannot be changed. However, replica regions can be added and removed at any time.

### [](https://fly.io/docs/upstash/redis/#traffic-routing)Traffic routing

Upstash Redis is available in all Fly regions via a [private IPv6 address](https://fly.io/docs/networking/flycast/) restricted to your Fly organization. Traffic is automatically routed to the nearest replica, or in the absence of nearby replicas, to the primary instance.

**If you plan to deploy in a single region, ensure that your database is deployed in the same region as your application.**

### [](https://fly.io/docs/upstash/redis/#writing-to-replica-regions)Writing to replica regions

**Replicas forward writes to the primary**. Replicas can’t be written to. Writes are synchronous, and synchronous writes over geographic distance experience latency. Plan for this latency in your application design.

If you’re using Redis as region-local cache and don’t require a shared cache, setup separate databases per-region and enable object eviction.

### [](https://fly.io/docs/upstash/redis/#memory-limits-and-object-eviction-policies)Memory limits and object eviction policies

By default, Upstash Redis will disallow writes when the max data size limit has been reached. If you enable **eviction**, keys will be evicted to free up space.

First, keys marked with a TTL will be evicted at random. In the absence of volatile keys, keys will be chosen randomly for eviction. This is roughly the combination of the `volatile-random` and `allkeys-random`[eviction policies available in standard Redis](https://redis.io/docs/manual/eviction/).

Note that items marked with an explicit TTL will expire accurately, regardless of whether eviction is enabled.

[](https://fly.io/docs/upstash/redis/#pricing)Pricing
-----------------------------------------------------

Upstash offers a range of payment plans for different use cases.

#### [](https://fly.io/docs/upstash/redis/#pay-as-you-go-plan)Pay-as-you-go plan

Upstash Redis databases start on the pay-as-you-go plan at **$0.20 per 100k requests**. This means you only pay for what you use. For most use cases, this is a good starting point. Pay-as-you-go plan has following limits:

*   Maximum Commands per Second: 10,000 
*   Maximum Request Size: 10 MB (Customizable) 
*   Maximum Entry Size: 100 MB (Customizable) 
*   Storage Limit: 10 GB 

Your usage is updated hourly on your monthly Fly.io bill. You can track database usage details in the [Upstash web console](https://fly.io/docs/upstash/redis/#the-upstash-web-console) as well.

#### [](https://fly.io/docs/upstash/redis/#fixed-price-plans)Fixed price plans

Upstash also offers fixed price plans for when:

*   You’re using Sidekiq, BullMQ or similar pre-packaged software that uses Redis as a queue, that aggressively poll Redis 
*   You understand your Redis usage patterns and want a predictable monthly pricing 

These fixed price plans are available via `flyctl redis update <dbname>`:

| Plan | Max Data Size | Monthly Bandwidth | Monthly Price |
| --- | --- | --- | --- |
| Fixed 250MB | 250 MB | 50 GB | $10/mo + $5/read region |
| Fixed 1GB | 1 GB | 100 GB | $20 + $10/read region |
| Fixed 5GB | 5 GB | 500 GB | $100 + $50/read region |
| Fixed 10GB | 10 GB | 1 TB | $200 + $100/read region |
| Fixed 50GB | 50 GB | 5 TB | $400 + $200/read region |

Check the official [Upstash Pricing](https://upstash.com/pricing) page for more information.

[](https://fly.io/docs/upstash/redis/#add-ons)Add Ons
-----------------------------------------------------

Upstash offers two add-on features that can be enabled when provisioning a new DB, or on existing DBs using `fly redis update <dbname>`

#### [](https://fly.io/docs/upstash/redis/#auto-upgrade)Auto Upgrade

On Fixed plans, Upstash will apply usage limits based on your current plan. When you reach these limits, behavior depends on the specific limit type - bandwidth limits will throttle your traffic, while storage limits will reject new write operations.

The Auto Upgrade feature automatically upgrades your database to the next higher plan when you reach your usage limits, ensuring uninterrupted service. For more details see [Upstash’s docs](https://upstash.com/docs/redis/features/auto-upgrade)

AutoUpgrade can be enabled on fixed plan DBs using `fly redis update <dbname>` or as an option when creating a DB on a fixed plan.

#### [](https://fly.io/docs/upstash/redis/#prod-pack-200-mo)Prod Pack - $200/mo

Upstash offers a ProdPack add-on for enabled Enterprise level features on a per-database level. This add on unlocks additional monitoring, compliance, and availability features for your database. Prod Pack is available on both pay-as-you-go and fixed plans. For a full list of benefits, please see Upstash’s official [ProdPack Documentation](https://upstash.com/docs/redis/overall/enterprise#prod-pack-and-enterprise)

Prod Pack can be enabled when provisioning a new DB, and on existing DBs using `fly redis update <dbname>`, or from your Upstash dashboard.
