# Source: https://planetscale.com/docs/postgres/imports/aurora.md

# Migrate from Aurora to PlanetScale

> Use this guide to migrate an existing Aurora (Postgres) database to PlanetScale Postgres.

This guide will cover a no-downtime approach to migrating using Postgres logical replication. If you are willing to tolerate downtime during a maintenance window, you may also use [`pg_dump` and restore](/docs/postgres/imports/postgres-migrate-dumprestore). The `pg_dump`/restore approach is simpler, but is only for applications where downtime is acceptable.

This guide assumes that public internet access is enabled on your Aurora database, as it will be needed to connect and replicate to the new PlanetScale host. If you cannot enable this due to security policies, consider using [AWS DMS](/docs/postgres/imports/aurora-dms) for your migration, or [contact support](https://planetscale.com/contact?initial=support) for more specific guidance.

These instructions work for all versions of Postgres that support logical replication (version 10+). If you have an older version you want to bring to PlanetScale, [contact us](https://planetscale.com/contact?initial=support) for guidance.

Before beginning a migration, you should check our [extensions documentation](/docs/postgres/extensions) to ensure that all of the extensions you rely on will work on PlanetScale.

As an alternative to this guide, you can also try our [Postgres migration scripts](https://github.com/planetscale/migration-scripts/tree/main/postgres-direct). These allow you to automate some of the manual steps that we describe in this guide.

## 1. Prepare your PlanetScale database

Go to `app.planetscale.com` and create a new database. A few things to check when configuring your database:

* Ensure you select the correct cloud region. You typically want to use the same region that you deploy your other application infrastructure to.
* This guide assumes you are migrating from a Postgres Aurora database, so also choose the Postgres option in PlanetScale.
* Choose the best storage option for your needs. For applications needing high-performance and low-latency I/O, use [PlanetScale Metal](/docs/metal). For applications that need more flexible storage options or smaller compute instances, choose "Elastic Block Storage" or "Persistent Disk."

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0e7ca13a6351b7e5364d24416b83a816" alt="Create a new PlanetScale Postgres database" data-og-width="2726" width="2726" data-og-height="2148" height="2148" data-path="docs/images/assets/docs/postgres/neon/image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=91f0fbefca3fdb5c798b8ba29f397550 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=93c1f48350fe2f5f6066b33f9157a84e 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=68b2c55f471d0b2d64f3d3e50843d6b0 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f2d33fa644794d0806af901658c63430 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4fe66bc0957449acd0a0bb6775a34082 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=6959ae35b1808fc9b994a7d7766f270a 2500w" />
</Frame>

Once the database is created and ready, navigate to your dashboard and click the "Connect" button.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=e4784f2b40a6f88e2a601f6659be6712" alt="Connect to a PlanetScale Postgres database" data-og-width="3950" width="3950" data-og-height="1522" height="1522" data-path="docs/images/assets/docs/postgres/neon/image2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=35904d388380db65a9cf22ead105fba4 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3593d6da1c20252552cb54c1526ed027 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7b115652225005446dbd9f8641607f91 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=e647fc714478c4d2f67e6e4054ad4c07 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=b7cf52021b91f7922bd209ef5da0d3ad 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image2.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=74588936353bdc994269d4f2fa5085c9 2500w" />
</Frame>

From here, follow the instructions to create a new default role. This role will act as your admin role, with the highest level of privileges.

Though you may use this one for your migration, we recommend you use a separate role with lesser privileges for your migration and general database connections.

To create a new role, navigate to the [Role management page](/docs/postgres/connecting/roles) in your database settings. Click "New role" and give the role a memorable name. By default, `pg_read_all_data` and `pg_write_all_data` are enabled. In addition to these, enable `pg_create_subscription` and `postgres`, and then create the role.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=9345f5bdc50a2f4ff4377b29113593f9" alt="New Postgres role privileges" data-og-width="1882" width="1882" data-og-height="2296" height="2296" data-path="docs/images/assets/docs/postgres/neon/image3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=381e4a65ddfaad1e630f3c5c60ec9883 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a35fe462b430de0a0f9ebaa37f7a58cd 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=236cc405e176abd706451721f2725862 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=de2ce65079050ea0df953c50d589a526 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=cdeca3bf12d0bd60e21773df8f3b4123 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image3.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2fc3ccd3aff59df61ef18ffa048296fc 2500w" />
</Frame>

Copy the password and all other connection credentials into environment variables for later use:

```bash  theme={null}
PLANETSCALE_USERNAME=pscale_api_XXXXXXXXXX.XXXXXXXXXX
PLANETSCALE_PASSWORD=pscale_pw_XXXXXXXXXXXXXXXXXXXXXXX
PLANETSCALE_HOST=XXXX.pg.psdb.cloud
PLANETSCALE_DBNAME=postgres
```

We also recommend that you increase `max_worker_processes` for the duration of the migration, in order to speed up data copying. Go to the "Parameters" tab of the "Clusters" page:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=b5d48fae3e6cad4c1ae316014c403374" alt="Configure parameters" data-og-width="3318" width="3318" data-og-height="1964" height="1964" data-path="docs/images/assets/docs/postgres/neon/image4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4b5874a8e96fb196931e2f4158be0e03 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=c276e4374fd4ed9bbf670b0c9d64b454 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=faee7333278a4ecebd20c0114791c8a0 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2b65c663586797fafee2a1019d4bf45c 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=1c762d7dbbd20410b4182ad10ab09f51 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image4.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0a58144ac8b35386a8ac3609b2ec2554 2500w" />
</Frame>

On this page, increase this value from the default of `4` to `10` or more:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=14b57255afb2d6ffdc04306e40df04c5" alt="Configure max worker processes" data-og-width="1784" width="1784" data-og-height="1152" height="1152" data-path="docs/images/assets/docs/postgres/neon/image5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=df8d165ce6a0c1ba9dd16af3946a181a 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7a7571b3e235c962e88c8e1c45a2dae2 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4f6fe35d2a93b930533eeff594421ea1 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=913e8986a50aa44776c427f4ba7dc60f 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=bf346d34e516c3ceca3b51758a6bed47 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image5.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=87090013cab70e6a63ac4721274c8ad0 2500w" />
</Frame>

You can decrease these values after the migration is complete.

## 2. Configure disk size on PlanetScale

If you are importing into a database backed by network-attached storage, you must configure your disk in advance to ensure your database will fit.
Though we support disk autoscaling for these, AWS and GCP limit how frequently disks can be resized.

If you don't ensure your disk is large enough for the import in advance, it will not be able to resize fast enough for a large data import.

To configure this, navigate to "Clusters" and then the "Storage" tab:

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=a5c9b5d45b3e70904dcd63ebae86ed51" alt="Storage configuration min size" data-og-width="3076" width="3076" data-og-height="2336" height="2336" data-path="docs/postgres/imports/storage-configuration-min-size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e7ce34378d7f13060b6f55798d84ca81 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=752e51dbf17cd95a054e8bfcffc88310 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=afcc0a16e5cc562f507a58f397e48648 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=430433f27649b68a6a612010926fd5ed 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f7a31fb98516dea9d3808e0e1649a1d8 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/storage-configuration-min-size.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e0447135018372dbfde71a8647a6a9a2 2500w" />

On this page, adjust the "Minimum disk size."
You should set this value to at least 150% of the size of the database you are migrating.
For example, if the database you are importing is 330 GB, you should set your minimum disk size to at least 500 GB.

The 50% overhead is to account for:

1. Data growth during the import process and
2. Table and index bloat that can occur during the import process.
   This can be later mitigated with careful [VACUUMing](https://www.postgresql.org/docs/current/sql-vacuum.html) or using an extension like [pg\_squeeze](https://planetscale.com/docs/postgres/extensions/pg_squeeze), but is difficult to avoid during the migration itself.

When ready, queue and apply the changes.
You can check the "Changes" tab to see the status of the resize:

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ade2793422ccfcf0bd7e6c5ee2511a98" alt="Confirm disk size change" data-og-width="2626" width="2626" data-og-height="1264" height="1264" data-path="docs/postgres/imports/confirm-disk-size-change.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b193023eae6603ca54d2d21d4b8cf3ce 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=36f59f9028dc0674d68594d7efbfd912 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=92d471e9e4afa9de0dc7ff1e9adcf2e3 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=f237cdd75c3a3c243b7b6b4c77fdba61 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=99e53e615c6ca48b396d0b0ada146cf7 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/confirm-disk-size-change.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=226ed370d1291db934cd6fbda032d633 2500w" />

Wait for it to indicate completion.

If you are importing to a Metal database, you must choose a disk size when first creating your database.
You should launch your cluster with a disk size at least 50% larger than the storage used by your current source database (150% of the existing total).

As an example, if you need to import a 330 GB database onto a PlanetScale `M-160` there are three storage sizes available:

<img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=3c7924b6c3c1c712eb2772b9c16adb41" alt="Metal disk size" data-og-width="2074" width="2074" data-og-height="1812" height="1812" data-path="docs/postgres/imports/metal-disk-size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d2db5c8f73a3d3e450aa7410d517966a 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b0c63716f22d784102107f89435f90c5 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=83ccb63b153d07c065f434a026156c32 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b70ee20b312291760b4851520c333006 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=23f72e5606dd17d426b63d1404436a59 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/imports/metal-disk-size.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=9bb971a81d534a7ac24bde77932d9717 2500w" />

You should use the largest, 1.25TB option during the import.
After importing and cleaning up table bloat, you may be able to downsize to the 468 GB option.
Resizing is a no-downtime operation that can be performed on the [Clusters](https://planetscale.com/docs/postgres/cluster-configuration) page.

## 3. Prepare the Aurora database

For PlanetScale to import your database, it needs to be publicly accessible. You can check this in your AWS dashboard.

In the writer instance of your database cluster, go to the “Connectivity & security” tab, and under “Security” you will see if your database is publicly accessible. If it says “No,” you will need to change it to be publicly accessible through the “Modify” button. If this is an issue, you cannot do this, or you have questions, please [contact support](https://planetscale.com/contact?initial=support) to explore your migration options.

You will also need to change some parameters and ensure that logical replication is enabled. If you don't already have a parameter group for your Aurora cluster, create one from the "Parameter groups" page in the AWS console:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=437cc52c48f561e2967fc71f1dc0ecd6" alt="AWS parameter groups" data-og-width="4122" width="4122" data-og-height="1606" height="1606" data-path="docs/images/assets/docs/postgres/neon/image6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=1eb0773552ec8befea1a5743b371f9e3 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f78f4dbba4f2ecd7258a2d5971ddfcbc 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=b8c500ecd7e0bfc1e636040989b9d271 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=9b9a166776e5e51088f3cf0bea8d40d0 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=6533437ced6eb4a9dc97fe69e0236f88 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image6.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3e2c52b2e21ec9ec3d23ba8241d7a917 2500w" />
</Frame>

From here, click the button to create a new group. Choose whichever name and description you want. Set the `Engine type` to `Aurora Postgres` and the `Parameter family group` to the version that matches your Aurora Postgres database. Set the `Type` to `DB Cluster Parameter Group`.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f7faa02e15f9cf0c3463d108f027f8b5" alt="Create an AWS parameter group" data-og-width="4014" width="4014" data-og-height="1734" height="1734" data-path="docs/images/assets/docs/postgres/neon/image7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=70e3ddc8922fce6267e8e95176579b5a 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fea1791d1837981e940b3fab24df8b89 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=55f89b14b50fd66eb9936b49a557842b 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ec31976f08b4942bc302ac0b4a30615e 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f1a8ecfa03f13c4157260de1e8018d90 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image7.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=545b2d54257e923653347bfd6ad99f49 2500w" />
</Frame>

If you already have a custom parameter group for your cluster, you can use the existing one instead. The two key parameters you need to update are adding `pglogical` to `shared_preload_libraries` and setting `rds.logical_replication` to `1`:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=d527ce318372760d89e0f66b396d9eb2" alt="Preload libraries parameter" data-og-width="3172" width="3172" data-og-height="878" height="878" data-path="docs/images/assets/docs/postgres/neon/image8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=baaea23e9ec6477681aa6ac342bd8c5c 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fc08b9e8f05a0cdebc4d8be7b0725791 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3da38b14614ad15ffb52271c1a2fcf35 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3ac296460769938b116b688929409ed2 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=614612a3c54145c8a8374978838a201a 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image8.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=cbda0d97a3d2374881a486fe2f26e56b 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=10375ea413b0ea3bf8acd6fdc5036d83" alt="Logical replication parameter" data-og-width="3172" width="3172" data-og-height="678" height="678" data-path="docs/images/assets/docs/postgres/neon/image9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=50698550a0d50eecc777488f0afdf221 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fe69ea763e66da6604ab64ed3f984c6a 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=af3248b84015b00e8176d94416d463b8 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ab56c9840db2a3a18a5dbe78a5b3d9b9 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=72f573009fcbc5e2f35195a837b22ff8 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image9.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2843095ae0b7d11ec42345220d056bae 2500w" />
</Frame>

Once these are set, you need to make sure your Aurora database is configured to use them. Navigate to your Aurora database in the AWS console, click the "Modify" button, and then ensure your database is using the parameter group:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f5e74b4e1c11a7357f6ef4dad70f35fb" alt="Set parameter group for Aurora" data-og-width="2506" width="2506" data-og-height="846" height="846" data-path="docs/images/assets/docs/postgres/neon/image10.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=43efe5b6ad03aae3ee97918cfa13b387 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0c563c5ec564953f918c072b11ce6b33 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=4acb213406faaac4699aaa4bfc461b1c 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=20f0499c0917a18e98853ae750e1b1b4 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=355f7e4ccfb5fd7df250b42ae294ff3b 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/neon/image10.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=d39a87c7e1f50fcf7450b954d0ddb0a2 2500w" />
</Frame>

When you go to save the changes, select the option to either apply immediately or during your next maintenance window. The changes may take time to propagate. You can confirm that the `wal_level` is set to `logical` by running `SHOW wal_level;` on your Aurora database:

```sql  theme={null}
postgres=> SHOW wal_level;
 wal_level
-----------
 logical
```

If you see a result other than `logical`, then it is not configured correctly. If you are having trouble getting the settings to propagate, you can try restarting the Aurora instance, though that will cause a period of downtime.

## 4. Copy schema from Aurora to PlanetScale

Before we begin migrating data, we first must copy the schema from Aurora to PlanetScale. We do this as a distinct set of steps using `pg_dump`.

<Warning>
  You should not make any schema changes during the migration process. You may continue to select, insert, update, and delete data, keeping your application fully online during this process.
</Warning>

For these instructions, you'll need to connect to Aurora with a role that has permissions to create replication publications and read all data. Your default role that was generated by Aurora when you first created your database should suffice here, but you may also use other roles. We will assume that the credentials for this user and other connection info are stored in the following environment variables.

```bash  theme={null}
AURORA_USERNAME=XXXX
AURORA_PASSWORD=XXXX
AURORA_HOST=XXX
AURORA_DBNAME=XXX
```

Run the below command to take a snapshot of the full schema of the `$AURORA_DBNAME` that you want to migrate:

```bash  theme={null}
PGPASSWORD=$AURORA_PASSWORD \
pg_dump -h $AURORA_HOST \
        -p 5432 \
        -U $AURORA_USERNAME \
        -d $AURORA_DBNAME \
        --schema-only \
        --no-owner \
        --no-privileges \
        -f schema.sql
```

This saves the schema into a file named `schema.sql`.

<Note>
  The above command will dump the tables for all schemas in the current database. If you want to migrate only one specific schema, you can add the `--schema=SCHEMA_NAME` option.
</Note>

The schema then needs to be loaded into your new PlanetScale database:

```bash  theme={null}
PGPASSWORD=$PLANETSCALE_PASSWORD \
psql -h $PLANETSCALE_HOST \
     -p 5432 \
     -U $PLANETSCALE_USERNAME \
     -d $PLANETSCALE_DBNAME \
     -f schema.sql
```

In the output of this command, you might see some error messages of the form:

```
psql:schema.sql:LINE: ERROR: DESCRIPTION
```

You should inspect these to see if they are of any concern. You can [reach out to our support](https://planetscale.com/contact) if you need assistance at this step.

## 5. Set up logical replication

We now must create a `PUBLICATION` on Aurora that the PlanetScale database can subscribe to for data copying and replication.

To create a publication for all tables in all schemas of the current database, run the following command on your Aurora database:

```sql  theme={null}
CREATE PUBLICATION replicate_to_planetscale FOR ALL TABLES;
```

You should see this if it created correctly:

```sql  theme={null}
CREATE PUBLICATION
```

<Note>
  To publish changes for only one specific schema, run the following query:

  ```sql  theme={null}
  SELECT 'CREATE PUBLICATION replicate_to_planetscale FOR TABLE ' ||
         string_agg(format('%I.%I', schemaname, tablename), ', ') || ';'
  FROM pg_tables
  WHERE schemaname = 'YOUR_SCHEMA_NAME';
  ```

  This will generate a query that looks like this:

  ```sql  theme={null}
  CREATE PUBLICATION replicate_to_planetscale FOR TABLE
    public.table_1,
    public.table_2,
    ...
    public.table_n;
  ```

  You can then copy/paste this and execute on Aurora. This will create a publication that only publishes changes for the tables in `YOUR_SCHEMA_NAME`
</Note>

After creating the publication on Aurora, we then need to tell PlanetScale to `SUBSCRIBE` to this publication.

```sql  theme={null}
PGPASSWORD=$PLANETSCALE_PASSWORD psql \
  -h $PLANETSCALE_HOST \
  -U $PLANETSCALE_USERNAME \
  -p 5432 $PLANETSCALE_DBNAME \
  -c "
CREATE SUBSCRIPTION replicate_from_aurora
CONNECTION 'host=$AURORA_HOST dbname=$AURORA_DBNAME user=$AURORA_USERNAME password=$AURORA_PASSWORD'
PUBLICATION replicate_to_planetscale WITH (copy_data = true);"
```

Data copying and replication will begin at this point. To check in on the row counts for the tables, you can run a query like this on your source and target databases:

```sql  theme={null}
SELECT table_name, row_count FROM (
  SELECT 'table_name_1' as table_name, COUNT(*) as row_count FROM table_name_1 UNION ALL
  SELECT 'table_name_2', COUNT(*) FROM table_name_2 UNION ALL
  ...
  SELECT 'table_name_N', COUNT(*) FROM table_name_N
) t ORDER BY table_name;
```

When the row counts match (or nearly match) you can begin testing and prepare for your application to cutover to use PlanetScale.

## 6. Handling sequences

Logical replication is great at migrating all of your data over to PlanetScale. However, logical replication does *not* synchronize the `nextval` values for [sequences](https://www.postgresql.org/docs/current/sql-createsequence.html) in your database. Sequences are often used for things like auto incrementing IDs, so it's important to ensure we update this before you switch your traffic to PlanetScale.

You can see all of the sequences and their corresponding `nextval`s on your source Aurora database using this command:

```sql  theme={null}
SELECT schemaname, sequencename, last_value + increment_by AS next_value
FROM pg_sequences;
```

An example output from this command:

```sql  theme={null}
 schemaname |   sequencename   | next_value
------------+------------------+------------
 public     | users_id_seq     |        105
 public     | posts_id_seq     |       1417
 public     | followers_id_seq |       3014
```

What this means is that we have three sequences in our database. In this case, they are all being used for auto-incrementing primary keys. The `nextval` for the `users_id_seq` is 105, the `nextval` for the `posts_id_seq` is 1417, and the `nextval` for the `followers_id_seq` is 3014. If you run the same query on your new PlanetScale database, you'll see something like:

```sql  theme={null}
 schemaname |   sequencename   | next_value
------------+------------------+------------
 public     | users_id_seq     |          0
 public     | posts_id_seq     |          0
 public     | followers_id_seq |          0
```

If you switch traffic over to PlanetScale in this state, you'll likely encounter errors when inserting new rows:

```sql  theme={null}
ERROR:  duplicate key value violates unique constraint "XXXX"
DETAIL:  Key (id)=(ZZZZ) already exists.
```

Before switching over, you need to progress all of these sequences forward so that the `nextval`s produced will be greater than any of the values previously produced on the source Aurora database, avoiding constraint violations. There are several approaches you can take for this. A simple way to solve the problem is to first run this query on your source Aurora database:

```sql  theme={null}
SELECT 'SELECT setval(''' || schemaname || '.' || sequencename || ''', '
       || (last_value + 10000) || ');' AS query
FROM pg_sequences;
```

This will generate a sequence of queries that will advance the `nextval` by 10,000 for each sequence:

```sql  theme={null}
                      query
--------------------------------------------------
 SELECT setval('public.users_id_seq', 10104);
 SELECT setval('public.posts_id_seq', 11416);
 SELECT setval('public.followers_id_seq', 13013);
```

You would then execute these on your target PlanetScale database. You need to ensure you advance each sequence far enough forward so that the sequences in the Aurora database will not reach these `nextval`s before you switch your primary to PlanetScale. For tables that have a high insertion rate, you might need to increase this by a larger value (say, 100,000 or 1,000,000).

## 7. Cutting over to PlanetScale

Before you cutover, it's good to have confidence that the replication is fully caught up between Aurora and PlanetScale. You can do this using Log Sequence Numbers (LSNs). The goal is to see these match up between the source Aurora database and the target PlanetScale database exactly. If they don't, it indicates that the PlanetScale database is not fully caught-up with the changes happening on Aurora.

You can run this on Aurora to see the current LSN:

```sql  theme={null}
postgres=> SELECT pg_current_wal_lsn();
 pg_current_wal_lsn
--------------------
 0/703FE460
```

Then on PlanetScale, you would run the following query to check for a match:

```sql  theme={null}
postgres=> SELECT received_lsn, latest_end_lsn
             FROM pg_stat_subscription
             WHERE subname = 'replicate_from_aurora';
 received_lsn | latest_end_lsn
--------------+----------------
 0/703FE460   | 0/703FE460
```

Once you are comfortable that all your data has successfully copied over and replication is sufficiently caught up, it's time to switch to PlanetScale. In your application code, prepare the cutover by changing the database connection credentials to go to PlanetScale rather than Aurora. Then, you can deploy this new version of your application, which will begin using PlanetScale as your primary database.

After doing this, new rows written to PlanetScale will not be reverse-replicated to Aurora. Thus, it's important to ensure you are fully ready for the cutover at this point.

Once this is complete, PlanetScale is now your primary database! We recommend you keep your old database around for at least a few days, just in case you discover any data or schemas you forgot to copy over to PlanetScale.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt