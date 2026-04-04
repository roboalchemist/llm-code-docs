# Source: https://planetscale.com/docs/postgres/imports/neon.md

# Migrate from Neon to PlanetScale

> Use this guide to migrate an existing Neon database to PlanetScale Postgres.

This guide will cover a no-downtime approach to migrating using Postgres logical replication. If you are willing to tolerate downtime during a maintenance window, you may also use [`pg_dump` and restore](/docs/postgres/imports/postgres-migrate-dumprestore). The `pg_dump`/restore approach is simpler, but is only for applications where downtime is acceptable.

These instructions work for all versions of Postgres that support logical replication (version 10+). If you have an older version you want to bring to PlanetScale, [contact us](https://planetscale.com/contact?initial=support) for guidance.

Before beginning a migration, you should check our [extensions documentation](/docs/postgres/extensions) to ensure that all of the extensions you rely on will work on PlanetScale.

As an alternative to this guide, you can also try our [Postgres migration scripts](https://github.com/planetscale/migration-scripts/tree/main/postgres-direct). These allow you to automate some of the manual steps that we describe in this guide.

## 1. Prepare your PlanetScale database

Go to `app.planetscale.com` and create a new database. A few things to check when configuring your database:

* Ensure you select the correct cloud region. You typically want to use the same region that you deploy your other application infrastructure to.
* This guide assumes you are migrating from a Neon database, so also choose the Postgres option in PlanetScale.
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
Resizing is a no-downtime operation that can be performed on the [clusters](https://planetscale.com/docs/postgres/cluster-configuration) page.

## 3. Prepare the Neon database

You will need to enable logical replication to use this import guide. To do so, go to the settings page in your Neon project:

<img src="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=3cf5c4d00d83164323817fa5d1d019f9" alt="Neon dashboard" data-og-width="3662" width="3662" data-og-height="1662" height="1662" data-path="docs/postgres/imports/neon-dashboard-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=280&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=1182fb7f711c404debc1e4528a71ea90 280w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=560&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=d31474ea66c03ac9bd6853faf6c94261 560w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=840&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=52f37bee5706113a97b16c2314a0e3a5 840w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=1100&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=fabe4a644db5f9afb22daf1453765374 1100w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=1650&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=ff433d48241c6af5960344789d8c132b 1650w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-darkmode.png?w=2500&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=fe80946ff355350b096a3d1a19a95a27 2500w" />

Navigate to the "Logical Replication" section and ensure it is enabled.

<Warning>
  Note the warnings in the Neon dashboard. Changing this setting will sever all existing connections and restart all computes.
</Warning>

<img src="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=ed0577857d38927b37cc7bcbd2b4ac82" alt="Neon logical replication" data-og-width="3662" width="3662" data-og-height="1994" height="1994" data-path="docs/postgres/imports/neon-logical-replication-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=280&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=59779671c1532b2c8915d3a75e1592f9 280w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=560&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=915ad1cefbd205b3b19538fcd751985a 560w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=840&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=4584687f11a0fc07f04080dd79a72176 840w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=1100&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=1869c547ff123a55219755c3f09e1542 1100w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=1650&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=2715bf1fb80870054c9ed755d15fd7c9 1650w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-logical-replication-darkmode.png?w=2500&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=e944fff9e6de75cc158a5cfd040f6248 2500w" />

You can confirm that the `wal_level` is set to `logical` by running `SHOW wal_level;` on your Neon database:

```sql  theme={null}
neondb=> SHOW wal_level;
 wal_level
-----------
 logical
```

If you see a result other than `logical`, then it is not configured correctly. Once this is enabled, return to the dashboard.

For these instructions, you'll need to connect to Neon with a role that has permissions to create replication publications and read all data. Your default role that was generated by Neon when you first created your database should suffice here. To get these connection credentials to use for the migration, click on the "Connect" button from your project dashboard:

<img src="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=040cd92464f41783d3e64592752a1e4d" alt="Neon dashboard connect" data-og-width="3662" width="3662" data-og-height="1662" height="1662" data-path="docs/postgres/imports/neon-dashboard-connect-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=280&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=fccd40652619be1eef63f14f6b0dd91a 280w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=560&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=d86bbdcfa89b3ecc2bc256916de7f732 560w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=840&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=8101ed93471b75051d4a5e93f2225f5b 840w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=1100&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=16acf0517791f56a7bc8595970dccca5 1100w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=1650&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=5c611ea3107916c276a7b755c69f1b9a 1650w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-dashboard-connect-darkmode.png?w=2500&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=012c2c9b07b2bc6a9f6ab2da202a6771 2500w" />

In the connection modal that appears, ensure you have "connection pooling" disabled.

<img src="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=f8b4f9e54af797cf6594b1d65adb8501" alt="Neon connect" data-og-width="2254" width="2254" data-og-height="1740" height="1740" data-path="docs/postgres/imports/neon-connect-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=280&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=ed66ea629ddc1d25166e362ed870314c 280w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=560&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=a4eed4b90d402864512f7c2551733676 560w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=840&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=fef28b3f26b97a0359a729de1a0e1598 840w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=1100&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=19afc09ce3417ad5e65f2908aa8ae2b8 1100w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=1650&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=79b0e3a2e4fa0073d5d1ecf65e41a77b 1650w, https://mintcdn.com/planetscale-cad1a68a/-T12oTnFGgHO6jM1/docs/postgres/imports/neon-connect-darkmode.png?w=2500&fit=max&auto=format&n=-T12oTnFGgHO6jM1&q=85&s=315ce4e34777a258c95de9c8320af21c 2500w" />

The credentials displayed here are the ones you can use for the migration. For the rest of this guide, we'll assume these are saved into the following environment variables:

```bash  theme={null}
NEON_USERNAME=XXXX
NEON_PASSWORD=XXXX
NEON_HOST=XXX
NEON_DBNAME=XXX
```

## 4. Copy schema from Neon to PlanetScale

Before we begin migrating data, we first must copy the schema from Neon to PlanetScale. We do this as a distinct set of steps using `pg_dump`.

<Warning>
  You should not make any schema changes during the migration process. You may continue to select, insert, update, and delete data, keeping your application fully online during this process.
</Warning>

Run the below command to take a snapshot of the schema for the `$NEON_DBNAME` database that you want to migrate:

```bash  theme={null}
PGPASSWORD=$NEON_PASSWORD \
pg_dump -h $NEON_HOST \
        -p 5432 \
        -U $NEON_USERNAME \
        -d $NEON_DBNAME \
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

We now must create a `PUBLICATION` on Neon that the PlanetScale database can subscribe to for data copying and replication.

To create a publication for all tables in all schemas of the current database, connect to the Neon database:

```
PGPASSWORD=$NEON_PASSWORD \
PGSSLMODE=require \
PGCHANNELBINDING=require \
psql \
  -h $NEON_HOST \
  -U $NEON_USERNAME \
  -p 5432 \
  $NEON_DBNAME
```

Then run the following command:

```sql  theme={null}
CREATE PUBLICATION replicate_to_planetscale FOR ALL TABLES;
```

You should see this output if it created correctly:

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

  You can then copy/paste this and execute on Neon. This will create a publication that only publishes changes for the tables in `YOUR_SCHEMA_NAME`
</Note>

After creating the publication on Neon, we need to tell PlanetScale to `SUBSCRIBE` to this publication.

```sql  theme={null}
PGPASSWORD=$PLANETSCALE_PASSWORD psql \
  -h $PLANETSCALE_HOST \
  -U $PLANETSCALE_USERNAME \
  -p 5432 $PLANETSCALE_DBNAME \
  -c "
CREATE SUBSCRIPTION replicate_from_neon
CONNECTION 'host=$NEON_HOST dbname=$NEON_DBNAME user=$NEON_USERNAME password=$NEON_PASSWORD sslmode=require channel_binding=require'
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

You can see all of the sequences and their corresponding `nextval`s on your source Neon database using this command:

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

Before switching over, you need to progress all of these sequences forward so that the `nextval`s produced will be greater than any of the values previously produced on the source Neon database, avoiding constraint violations. There are several approaches you can take for this. A simple way to solve the problem is to first run this query on your source Neon database:

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

You would then execute these on your target PlanetScale database. You need to ensure you advance each sequence far enough forward so that the sequences in the Neon database will not reach these `nextval`s before you switch your primary to PlanetScale. For tables that have a high insertion rate, you might need to increase this by a larger value (say, 100,000 or 1,000,000).

## 7. Cutting over to PlanetScale

Before you cutover, it's good to have confidence that the replication between Neon and PlanetScale is fully caught up. You can do this using Log Sequence Numbers (LSNs). The goal is to see these match up between the source Neon database and the target PlanetScale database exactly. If they don't, it indicates that the PlanetScale database is not fully caught-up with the changes happening on Neon.

You can run this on Neon to see the current LSN:

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
             WHERE subname = 'replicate_from_neon';
 received_lsn | latest_end_lsn
--------------+----------------
 0/703FE460   | 0/703FE460
```

Once you are comfortable that all your data has successfully copied over and replication is sufficiently caught up, it's time to switch to PlanetScale. In your application code, prepare the cutover by changing the database connection credentials to go to PlanetScale rather than Neon. Then, you can deploy this new version of your application, which will begin using PlanetScale as your primary database.

After doing this, new rows written to PlanetScale will not be reverse-replicated to Neon. Thus, it's important to ensure you are fully ready for the cutover at this point.

Once this is complete, PlanetScale is now your primary database! We recommend you keep your old database around for at least a few days, just in case you discover any data or schemas you forgot to copy over to PlanetScale.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt