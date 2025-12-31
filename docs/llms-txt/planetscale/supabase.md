# Source: https://planetscale.com/docs/postgres/imports/supabase.md

# Migrate from Supabase to PlanetScale

Use this guide to migrate an existing Supabase database to PlanetScale Postgres.

This guide will cover a no-downtime approach to migrating using Postgres logical replication. If you are willing to tolerate downtime during a maintenance window, you may also use [`pg_dump` and restore](/docs/postgres/imports/postgres-migrate-dumprestore). The `pg_dump`/restore approach is simpler, but is only for applications where downtime is acceptable.

These instructions work for all versions of Postgres that support logical replication (version 10+). If you have an older version you want to bring to PlanetScale, [contact us](https://planetscale.com/contact?initial=support) for guidance.

Before beginning a migration, you should check our [extensions documentation](/docs/postgres/extensions) to ensure that all of the extensions you rely on will work on PlanetScale.

As an alternative to this guide, you can also try our [Postgres migration scripts](https://github.com/planetscale/migration-scripts/tree/main/postgres-direct). These allow you to automate some of the manual steps that we describe in this guide.

## 1. Prepare your PlanetScale database

Go to `app.planetscale.com` and create a new database. A few things to check when configuring your database:

* Ensure you select the correct cloud region. You typically want to use the same region that you deploy your other application infrastructure to.
* Since Supabase uses Postgres, you'll also want to create a Postgres database in PlanetScale.
* Choose the best storage option for your needs. For applications needing high-performance and low-latency I/O, use [PlanetScale Metal](/docs/metal). For applications that need more flexible storage options or smaller compute instances, choose "Elastic Block Storage" or "Persistent Disk."
* Choose between aarch64 and x86-64 architecture. If you don't know which to choose, `aarch64` is a good default choice.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=aaca50d3753073aaac499b3abe680c83" alt="Create a new PlanetScale Postgres database" data-og-width="2726" width="2726" data-og-height="2148" height="2148" data-path="docs/images/assets/docs/postgres/imports/image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f7b060cbe656ddd34f337d2870306616 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2f2759f8703396f8d82d0006cca222dc 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ea54c4d42a7e6b5626b949b028a0397e 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f6cada130f06c28a51eae34168733a6c 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=d55b83a571d773396a91cf76dbaa4193 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=172c7f01989b23bb3a4b34b7e3efb7bc 2500w" />
</Frame>

Once the database is created and ready, navigate to your dashboard and click the "Connect" button.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=270f751b79b7c6411747336f1808f84f" alt="Connect to a PlanetScale Postgres database" data-og-width="3688" width="3688" data-og-height="1522" height="1522" data-path="docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=847e17b3d16516f98c95e4dedcd608c5 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=88ff3e44f389ceea4444e1684d24fa48 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=660052ad98066d43bc1734d983e543cf 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=c091929944f238b2d6e09bc903532470 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2337b79a44ae1e3cf24a89f7d43fa6df 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/migration-dashboard-connect.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=cca93110dfeec30a5911ff789961468d 2500w" />
</Frame>

From here, follow the instructions to create a new default role. This role will act as your admin role, with the highest level of privileges.

Though you may use this one for your migration, we recommend you use a separate role with lesser privileges for your migration and general database connections.

To create a new role, navigate to the [Role management page](/docs/postgres/connecting/roles). Click "New role" and give the role a memorable name. By default, `pg_read_all_data` and `pg_write_all_data` are enabled. In addition to these, enable `pg_create_subscription` and `postgres`, and then create the role.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7b0a8b6b27a1f28e4e5f16dece3f6087" alt="New Postgres role privileges" data-og-width="1882" width="1882" data-og-height="2296" height="2296" data-path="docs/images/assets/docs/postgres/imports/image3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a50f24908e67709672005dd83e01c9bb 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=96c638d12b0b809e48db540b4ce9d5e4 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=31670bdb00129efad3e127ded0d29288 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=f486f0dbc600324559edde676eb51b57 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=5f2b82317aa9c7261125928f8f4c13cc 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image3.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=99b0e011ed462a95561b4f6270b6973d 2500w" />
</Frame>

Copy the password and all other connection credentials into environment variables for later use:

```
PLANETSCALE_USERNAME=pscale_api_XXXXXXXXXX.XXXXXXXXXX
PLANETSCALE_PASSWORD=pscale_pw_XXXXXXXXXXXXXXXXXXXXXXX
PLANETSCALE_HOST=XXXX.pg.psdb.cloud
PLANETSCALE_DBNAME=postgres
```

We also recommend that you increase `max_worker_processes` for the duration of the migration in order to speed up data copying. Go to the "Parameters" tab of the "Clusters" page:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=fd168c176e0298871ee45a7123567280" alt="Configure parameters" data-og-width="3318" width="3318" data-og-height="1964" height="1964" data-path="docs/images/assets/docs/postgres/imports/image4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=075701b9e7dbbd64b8550a10b3de1d04 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3e166ad64beed2f3441696695d9cba1c 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=9138a06417f7398ff6e9f14f38604bf6 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0d33d7bfda846e537e9c8cc995f1a470 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=51c49ebc128442dfa410edc0cf143171 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image4.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=25c6b8e572da8583f6aa5b5f02dc1cd6 2500w" />
</Frame>

On this page, increase this value from the default of `4` to `10` or more:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7a72f9fbfe69dce955277d64ff350468" alt="Configure max worker processes" data-og-width="1784" width="1784" data-og-height="1152" height="1152" data-path="docs/images/assets/docs/postgres/imports/image5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=43cdf8d56e56612385e1cd709a95a02d 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=afe0c4b5a912dd8d370c5da270d2cfca 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=a12e2dde97abdc8d2501bb815ebd610c 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ad7a0405ed2501abf90c8ac700462dd4 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=c8005e4724a61c1aed8c1aeea1375d80 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image5.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=8535815774dcde2ae30f346d9d7a507e 2500w" />
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
Resizing is a no-downtime operation that can be performed on the [clusters](httsp://planetscale.com/docs/postgres/cluster-configuration) page.

## 3. Enable IPv4 direct connections in Supabase

In Supabase, logical replication to external sources requires direct connections. Direct IPv4 connections are not enabled by default. If you have not enabled them yet, go to your project dashboard in Supabase and click the "Connect" button:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=75da23b6022df1231329326638764c4b" alt="Supabase dashboard" data-og-width="2760" width="2760" data-og-height="1300" height="1300" data-path="docs/images/assets/docs/postgres/imports/image6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=47f3fa9d26f9fe875a3bdeb41b2809b3 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=ed89369c4af6f9c4066984096aa7a22c 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=d157d1451fd2f7f34ab4d673df77762a 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=3b8cac8ea4899d5730a82dcdc397ade4 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=0ad348e56464b1152315c2ae870eb6ae 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image6.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=906fe153d134a0855d99480b0a426bd1 2500w" />
</Frame>

In the connection modal, click "IPv4 add-on."

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=39d39e9766f6e3eb80d29ae9c56c8d80" alt="Supabase direct" data-og-width="3448" width="3448" data-og-height="1660" height="1660" data-path="docs/images/assets/docs/postgres/imports/image7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=429cd3e706588007e1e8f3467c32141b 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=8df45561e83d5c076635ab6d00562739 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=2444e506709af5a1442bb901771fc28a 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=c049f5487f768090a962865422d83d26 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7a9e83b6d8217110ae6f88fe8f30f44c 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image7.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=470003eb32f225c5e407c566a478e3d2 2500w" />
</Frame>

In the menu that appears, enable the IPv4 add-on:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=357454d8ee4ab345b55f87769d3d392c" alt="Supabase IPV4" data-og-width="2006" width="2006" data-og-height="1660" height="1660" data-path="docs/images/assets/docs/postgres/imports/image8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=280&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=40daa530dd61e5a85105ed307941bfe3 280w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=560&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=e5cde381f4f5de743488eea33b3658da 560w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=840&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=de56fface9fce8c87b0a2c3c63bbcd1f 840w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=1100&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=37d78f2b735b21c3f77c46558d4c65df 1100w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=1650&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=7f9a78b1246f277707f44add25e2ab02 1650w, https://mintcdn.com/planetscale-cad1a68a/KejcMcI0BguxMNLm/docs/images/assets/docs/postgres/imports/image8.png?w=2500&fit=max&auto=format&n=KejcMcI0BguxMNLm&q=85&s=df151b213161b42295b6e557d0b607b6 2500w" />
</Frame>

Supabase notes that enabling this might incur downtime. Take that into account when planning your migration.

## 4. Copy schema from Supabase to PlanetScale

Before we begin migrating data, we first must copy the schema from Supabase to PlanetScale. We do this as a distinct set of steps using `pg_dump`.

<Warning>
  You should not make any schema changes during the migration process. You may continue to select, insert, update, and delete data, keeping your application fully online during this process.
</Warning>

For these instructions, you'll need to connect to your Supabase role that has permissions to create replication publications and read all data. You also must use a direct IPv4 connection. Your default role that was generated by Supabase when you first created your database should suffice here. We will assume that the credentials for this user and other connection info are stored in the following environment variables.

```
SUPABASE_USERNAME=XXXX
SUPABASE_PASSWORD=XXXX
SUPABASE_HOST=XXX
SUPABASE_DBNAME=XXX
```

Run the below command to take a snapshot of the full schema of the `$SUPABASE_DBNAME` that you want to migrate:

```
PGPASSWORD=$SUPABASE_PASSWORD \
pg_dump -h $SUPABASE_HOST \
        -p 5432 \
        -U $SUPABASE_USERNAME \
        -d $SUPABASE_DBNAME \
        --schema-only \
        --no-owner \
        --no-privileges \
        --schema=public \
        -f schema.sql
```

This saves the schema into a file named `schema.sql`.

<Note>
  The above command will dump the tables only for the `public` schema. If you want to include other schemas in the migration, you can repeat these steps for each, or customize the commands to dump multiple schemas at once.
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

```bash  theme={null}
psql:schema.sql:LINE: ERROR: DESCRIPTION
```

You should inspect these to see if they are of any concern. You can [reach out to our support](https://planetscale.com/contact?initial=support) if you need assistance at this step.

## 5. Set up logical replication

We now must create a `PUBLICATION` on Supabase that the PlanetScale database can subscribe to for data copying and replication. This example shows how to create a publication that only publishes changes to tables in the `public` schema of your Postgres database. You can adjust the commands if you want to do so for a different schema, or have multiple schemas to migrate.

First, run this command on your Supabase database to get all of the tables in the `public` schema:

```sql  theme={null}
SELECT 'CREATE PUBLICATION replicate_to_planetscale FOR TABLE ' ||
       string_agg(format('%I.%I', schemaname, tablename), ', ') || ';'
FROM pg_tables
WHERE schemaname = 'public';
```

This will generate a query that looks like this:

```sql  theme={null}
CREATE PUBLICATION replicate_to_planetscale FOR TABLE
  public.table_1,
  public.table_2,
  ...
  public.table_n;
```

Take this command and execute it on your Supabase database. You should see this if it created correctly:

```sql  theme={null}
CREATE PUBLICATION
```

We then need to tell PlanetScale to `SUBSCRIBE` to this publication.

```sql  theme={null}
PGPASSWORD=$PLANETSCALE_PASSWORD psql \
  -h $PLANETSCALE_HOST \
  -U $PLANETSCALE_USERNAME \
  -p 5432 $PLANETSCALE_DBNAME \
  -c "
CREATE SUBSCRIPTION replicate_from_supabase
CONNECTION 'host=$SUPABASE_HOST dbname=$SUPABASE_DBNAME user=$SUPABASE_USERNAME password=$SUPABASE_PASSWORD'
PUBLICATION replicate_to_planetscale WITH (copy_data = true);"
```

Data copying and replication will begin at this point. To check in on the row counts on the tables, you can run a query like this on your source and target databases:

```sql  theme={null}
SELECT table_name, row_count FROM (
  SELECT 'table_name_1' as table_name, COUNT(*) as row_count FROM table_name_1 UNION ALL
  SELECT 'table_name_2', COUNT(*) FROM table_name_2 UNION ALL
  ...
  SELECT 'table_name_N', COUNT(*) FROM table_name_N
) t ORDER BY table_name;
```

When the row counts match (or nearly match) you can begin testing and preparing for your application to cutover to use PlanetScale.

## 6. Handling sequences

Logical replication is great at migrating all of your data over to PlanetScale. However, logical replication does *not* synchronize the `nextval` values for [sequences](https://www.postgresql.org/docs/current/sql-createsequence.html) in your database. Sequences are often used for things like auto incrementing IDs, so it's important to ensure we update this before you switch your traffic to PlanetScale.

You can see all of the sequences and their corresponding `nextval`s on your source Supabase database using this command:

```sql  theme={null}
SELECT schemaname, sequencename, last_value + increment_by
  AS next_value
  FROM pg_sequences;
```

An example output from this command:

```
 schemaname |   sequencename   | next_value
------------+------------------+------------
 public     | users_id_seq     |        105
 public     | posts_id_seq     |       1417
 public     | followers_id_seq |       3014
```

What this means is that we have three sequences in our database. In this case, they are all being used for auto-incrementing primary keys. The `nextval` for the `users_id_seq` is 105, the `nextval` for the `posts_id_seq` is 1417, and the `nextval` for the `followers_id_seq` is 3014. If you run the same query on your new PlanetScale database, you'll see something like:

```
 schemaname |   sequencename   | next_value
------------+------------------+------------
 public     | users_id_seq     |          0
 public     | posts_id_seq     |          0
 public     | followers_id_seq |          0
```

If you switch traffic over to PlanetScale in this state, you'll likely encounter errors when inserting new rows:

```bash  theme={null}
ERROR:  duplicate key value violates unique constraint "XXXX"
DETAIL:  Key (id)=(ZZZZ) already exists.
```

Before switching over, you need to progress all of these sequences forward so that the `nextval`s produced will be greater than any of the values previously produced on the source Supabase database, avoiding constraint violations. There are several approaches you can take for this. A simple way to solve the problem is to first run this query on your source Supabase database:

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

You would then execute these on your target PlanetScale database. You need to ensure you advance each sequence far enough forward so that the sequences in the Supabase database will not reach these `nextval`s before you switch your primary to PlanetScale. For tables that have a high insertion rate, you might need to increase this by a larger value (say, 100,000 or 1,000,000).

## 7. Cutting over to PlanetScale

Before you cutover, it's good to have confidence that the replication is fully caught up between Supabase and PlanetScale. You can do this using Log Sequence Numbers (LSNs). The goal is to see these match up between the source Supabase database and the target PlanetScale database exactly. If they don't, it indicates that the PlanetScale database is not fully caught-up with the changes happening on Supabase.

You can run this on Supabase to see the current LSN:

```bash  theme={null}
postgres=> SELECT pg_current_wal_lsn();
 pg_current_wal_lsn
--------------------
 0/703FE460
```

Then on PlanetScale, you would run the following query to confirm the match:

```bash  theme={null}
postgres=> SELECT received_lsn, latest_end_lsn
             FROM pg_stat_subscription
             WHERE subname = 'replicate_from_supabase';
 received_lsn | latest_end_lsn
--------------+----------------
 0/703FE460   | 0/703FE460
```

Once you are comfortable that all your data has successfully copied over and replication is sufficiently caught up, it's time to switch to PlanetScale. In your application code, prepare the cutover by changing the database connection credentials to go to PlanetScale rather than Supabase. Then, you can deploy this new version of your application, which will begin using PlanetScale as your primary database.

After doing this, new rows written to PlanetScale will not be reverse-replicated to Supabase. Thus, it's important to ensure you are fully ready for the cutover at this point.

Once this is complete, PlanetScale is now your primary database!

We recommend you keep the old Supabase database around for a few days, in case you discover any data or schemas you forgot to copy over to PlanetScale. If necessary, you can switch traffic back to the old database. However, keep in mind that any database writes that happened with PlanetScale as the primary will not appear on Supabase. This is why it's good to test the database thoroughly before performing the cutover.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt