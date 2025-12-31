# Source: https://planetscale.com/docs/metal/create-a-metal-database.md

# Create a Metal database

export const YouTubeEmbed = ({id, title}) => {
  return <Frame>
      <iframe src={`https://www.youtube-nocookie.com/embed/${id}?rel=0`} title={title} className="aspect-video w-full" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" />
    </Frame>;
};

[PlanetScale Metal](/docs/metal) databases can be created in a similar way to other PlanetScale databases.
However, there are a few important things to keep in mind when creating a new Metal database or upgrading an existing database to Metal, which will be covered here.

<YouTubeEmbed id="6BBrgJcpTBY" title="Create a database on PlanetScale" />

## Create a new Metal database

After logging in to `app.planetscale.com`, click "New database" -> "Create new database."
Next, enter the name of your new database and select the "PlanetScale Metal" option.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fa12b24902ed3f1498d6412e9842537a" className="block dark:hidden" alt="New Metal database" data-og-width="2674" width="2674" data-og-height="1428" height="1428" data-path="docs/images/metal/metal-new-db.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f085e0f1822de711fa18dfd0b5e63b37 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7bce192a92f4edf19cda8fdf379ef3ea 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=85a28006f795f87371933ac8f695d083 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=90c9d75920f33977f5a18663c74e70ad 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4bfc69ac97dd2ba8627b7a2b127e4a51 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b9e3290bc48e215fa887029c474a78ec 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2401b83cd85c1db8ea2d260381d8faef" className="hidden dark:block" alt="New Metal database" data-og-width="2674" width="2674" data-og-height="1428" height="1428" data-path="docs/images/metal/metal-new-db-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=bf433acb069636505a4d17e49e3fef6f 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=759ea6c6a2292fc02a510c85c23984f0 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7a79d02fdd5595f322993250b5437215 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c4692b881fefe1eff6e0818f6d0f8e03 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2931d9dc36a8540b1c35eb14106c3296 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3af4f71bebdc0915faacec6881fc29e8 2500w" />
</Frame>

This brings up a set of options to choose from for the size of your Metal database.
Start by choosing the vCPU and RAM combination that best suits your needs, then use the dropdown to select the drive size for the instance.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=52cb4305bc9732cbc8ebfd7cb1393c88" className="block dark:hidden" alt="Select Metal database size" data-og-width="2698" width="2698" data-og-height="1904" height="1904" data-path="docs/images/metal/metal-new-db-choose-size.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e7b8152ca7c2e927b29ac76641dd9f1f 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=07d933a45dce08e78975d53ff44d604a 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b412e7038fbfa9963c998622b1383e54 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=6ddbe7c768f0b97f2f2274b5678c33f6 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c7ad008fea809f4dddb46c9172d76c13 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=67d9a25d7eaf881ec244341ab332f536 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4fa454a4c8f8c5a39ebf55b5b95e2016" className="hidden dark:block" alt="Select Metal database size" data-og-width="2698" width="2698" data-og-height="1904" height="1904" data-path="docs/images/metal/metal-new-db-choose-size-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c5a64de7a623df5058240fa90538b53e 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ac7b9710bb06937b1e20c8d1e6ae8728 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=394095b6a5d31e13bda11de833892641 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ed1790f5077a0893df725729bbb5018f 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7f812f1d5e9426af90a0f5c704e0592c 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-new-db-choose-size-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=db02d95e84d7f5c59c39a55bf3896654 2500w" />
</Frame>

As opposed to [network-attached storage](/docs/plans/planetscale-skus#network-attached-storage) databases, [Metal](/docs/plans/planetscale-skus#metal) databases do not autoscale their storage size.
Therefore, it's important to make a good size choice from the start.
If you are starting a new project from scratch on a Metal database and you do not expect massive initial growth, it is likely best to choose the smallest drive possible.
If you intend to migrate an existing database into this in the near future, ensure that your drive will fit all of the data while also allowing room for further growth.

When ready, click "Create database."
After database initialization completes, you can begin using the database.

## Upgrading an existing database to Metal

You can also upgrade an existing keyspace in your database to Metal.
This is a no-downtime operation.
To do this, select your database, and then click on the "**Clusters**" in the navigation pane on the left side of the dashboard.
From here, you should choose the keyspace that you want to upgrade.
Click on the cluster size drop-down and scroll down to the Metal instance types.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=d5bf61d8eb3a669c432283c6f7ce3653" className="block dark:hidden" alt="Upgrade keyspace to Metal" data-og-width="3047" width="3047" data-og-height="1800" height="1800" data-path="docs/images/metal/metal-upgrade.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7752d8a2a126b1a230b14e747205b6dc 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9ac482be65d151f9d2b66e1e79908293 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b89c2e29e71f682f7eb2fae7151d0cc5 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b0e44dbb585dd983a2594486bed2ddd6 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=bd7781955482fd94191d04e85940948d 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=79ed77f76a75d9786d563d70825e095b 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e091491269ec7517706fe2ed1484f868" className="hidden dark:block" alt="Upgrade keyspace to Metal" data-og-width="3046" width="3046" data-og-height="1797" height="1797" data-path="docs/images/metal/metal-upgrade-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3f62bb74ba6224f1393a5304070f98e4 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=1410001bc184f148da2f7ae68bae1562 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=1237168c24e33b94aca231f2f8ee866b 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=06cf6482f24298c6945fb0440450e915 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=809787c6b37d5bef4dd86715c9919aa2 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/metal-upgrade-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fa6d76d31d89c3486251199be8124aaf 2500w" />
</Frame>

Select the desired compute and storage combination, and then click "Save changes."

Keep in mind that this is not an immediate operation.
If you have a large database, it may take a while for the upgrade to complete since behind the scenes, your entire database needs to be migrated to the new NVMe drives.
Ensure that you upgrade well before reaching max drive capacity.
We recommend upgrading at no later than 75% in most cases, and even earlier than that if you are growing quickly.

## Monitoring Metal storage

<Warning>
  The storage for Metal databases does not autoscale.
  It is important to keep a close eye on the storage capacity of Metal databases, and upgrade well before running out of space.
</Warning>

There are several ways to monitor this.

You can view storage information on the right side of the main PlanetScale dashboard for Metal databases.

After the upgrade is complete, we recommend going to the Insights page and view your query latency diagrams.
If you transitioned from a network-attached storage keyspace to a Metal one of the same size, you should see a reduction in query latency.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=d55514fd14f9dd42caab4c578d621d6f" className="block dark:hidden" alt="Metal storage info" data-og-width="1450" width="1450" data-og-height="1290" height="1290" data-path="docs/images/metal/storage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fc3f3336869931538dc74b9340bfb276 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=1948b04f8ff7b7a15d344e3fa70a8232 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f5fbda3db9f639922246ca6c0be8c11f 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=74999b7db20436b4b27ad64c4813453a 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=1670ae210f2974966a209dbcc3a61da6 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fd13087ee5563e31f00d9b5b9e1f953f 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=225f437db1b103b0af5d725fad955a9b" className="hidden dark:block" alt="Metal storage info" data-og-width="1450" width="1450" data-og-height="1290" height="1290" data-path="docs/images/metal/storage-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2b82638773136e2b233f58f580b9063b 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=22150b9eedb91d1fd179a723d4fb5368 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=32f0668a07490725ca2ed6b64b280bba 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=89f536d173fabe20c36240ceda36b22f 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=51e50ef2c3e6834ebcb9a12a8d96f0bb 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/storage-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=d98bdd763cce8678d1c5b0a6d2dacfe6 2500w" />
</Frame>

You should make a habit of regularly logging in and checking the health of your database, keep an eye on this number.
If PlanetScale detects that you have only 6GiB or less of available storage, it will cause your database to reject writes, preferring to keep the database available rather than cause a total system failure due to running out of storage.
This is a safety measure put in place to protect your data.
You should upgrade to a larger instance long before reaching this point.
You can upgrade to a larger Metal instance / drive using the same set of steps described above.

Additionally, operations such as deploy requests may not run if you do not have enough storage.
The exception to this is if you are performing an [instant deployment](/docs/vitess/schema-changes/deploy-requests#instant-deployments).

Deploying online schema changes with VReplication requires that we [make a copy of the affected tables](/docs/vitess/schema-changes/how-online-schema-change-tools-work#initializing-the-ghost-table-schema).
If you are nearing max capacity or making a change on a very large table, you risk not having enough storage to begin the online schema change.
We will let you know that there is not enough space to create a deploy request in these cases.

It is critical to upgrade your instance storage size well before you are nearing max capacity.
We will sent you email notices when your database storage reaches the following thresholds: 60%, 75%, 85%, 90%, 95%.
We will also email you when we estimate that your storage will run out in 1 week and 24 hours, based on recent usage trends.

The exact point at which you should upgrade depends on your data growth rate, drive size, and other factors.
We recommend upgrading no later than at 75% capacity, and even before that in some cases of fast growth.
Upgrading to a larger drive takes time, as it requires copying your database to new drives, so it's important to upgrade well before hitting max capacity.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt