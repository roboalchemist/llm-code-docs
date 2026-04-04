# Source: https://planetscale.com/docs/vitess/integrations/airbyte.md

# Airbyte integration

> With PlanetScale Connect, you can extract data from your PlanetScale database and safely load it into other destinations for analysis, transformation, and more.

We implemented an [Airbyte](https://airbyte.com/) connector as the pipeline between your PlanetScale source and selected destination. This document will walk you through how to connect your PlanetScale database to Airbyte.

## Connect to Airbyte

Only [Airbyte Open Source](https://docs.airbyte.com/quickstart/deploy-airbyte) supports the PlanetScale data source. In this section, you'll learn how to set up Airbyte and connect your PlanetScale source.

### Requirements

* A PlanetScale database
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Docker terms apply)

### Set up Airbyte locally

<Steps>
  <Step>
    Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
  </Step>

  <Step>
    Follow the related installation instructions included within the [Airbyte Quickstart Documentation](https://docs.airbyte.com/using-airbyte/getting-started/oss-quickstart).
  </Step>

  <Step>
    Open Airbyte in the browser at [http://localhost:8000](http://localhost:8000).
  </Step>
</Steps>

### Set up PlanetScale source

Now that Airbyte is running locally, let's set up the custom PlanetScale source.

<Steps>
  <Step>
    In the Airbyte dashboard, click "**Settings**" on the bottom left.
  </Step>

  <Step>
    Click "**Sources**" on the left sidebar.
  </Step>

  <Step>
    Click the "**New connector**" button.
  </Step>

  <Step>
    Click the "**Add a new Docker connector**" option.
    Fill in the connector values as follows:

    * **Connector display name**: PlanetScale
    * **Docker repository name**: planetscale/airbyte-source
    * **Docker image tag**: `latest`
    * **Connector Documentation URL**:(/docs/vitess/integrations/airbyte
  </Step>
</Steps>

You can find the [PlanetScale Airbyte Source Dockerhub release page here](https://hub.docker.com/r/planetscale/airbyte-source).

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ef6bfa8dca1b88bd8a26a6358756c201" alt="Airbyte new PlanetScale connector" data-og-width="2594" width="2594" data-og-height="2378" height="2378" data-path="docs/images/assets/docs/integrations/airbyte/modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=110ee71f12cb600875234630992f542f 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1dfee5945b8f2a5cae3b0c67faaf5511 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ba3ed772204ff90901eac87c33f16be9 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=4608782f2938240339295f8a07b19ab1 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=a7b4e9e5cf23c24b10c8feb6ff52d70b 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/modal.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d3b824c8bd15d8e9dde4585d76486ab1 2500w" />
</Frame>

### Fill in PlanetScale connection information

You're now ready to connect your PlanetScale database to Airbyte.

<Steps>
  <Step>
    Click on the database and branch you want to connect to.
  </Step>

  <Step>
    Click "**Connect**", select "**General**" from the "**Connect with**" dropdown.
  </Step>

  <Step>
    Leave this tab open, as you'll need to copy these credentials shortly.
  </Step>

  <Step>
    Back in Airbyte, click "**Sources**" in the main left sidebar > "**New source**".
  </Step>

  <Step>
    Select the new PlanetScale source you created from the dropdown.
  </Step>

  <Step>
    Fill in the "**Set up the source**" values as follows:

    * **Name**: Any name of your choice
    * **Source type**: Select "PlanetScale"
    * **Host**: Paste in the copied value for `host`
    * **Database**: Paste in the copied value for `database`
    * **Username**: Paste in the copied value for `username`
    * **Password**: Paste in the copied value for `password`

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9156ee6a9a926f94dc2371974e3005a2" alt="Airbyte - PlanetScale source setup" data-og-width="4324" width="4324" data-og-height="2644" height="2644" data-path="docs/images/assets/docs/integrations/airbyte/db-info.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b75e136d3d83196bf22f4a1ebd3b952d 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ea3e7fd4b8fce00802d3ebd9b2dc8157 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=377c6f0ce5c6cea656dcd9abc69339e1 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f0588dc2df2cfee1abb7485f6c1cf88d 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f39ecce6d26eb435368ac0b9c629a835 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/db-info.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=03c48e7b2c429dd31df5be8a60d9eaa6 2500w" />
    </Frame>
  </Step>

  <Step>
    You can also provide some optional values:

    * **Replicas**: Select whether or not you want to collect data from replica nodes.
    * **Shards**: Map your shards.
    * **Starting GTIDs**: Start replication from a specific GTID per keyspace shard.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2f794ce4c4d22e5d758ad3a7a023fa09" alt="Airbyte - PlanetScale optional setup" data-og-width="3606" width="3606" data-og-height="892" height="892" data-path="docs/images/assets/docs/integrations/airbyte/optional.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2101603af5c5d9ea7ed0043d15fefa16 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=5aa5a36c49d5e279fbc04910a8e55305 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c3044a4ff72063ccee4a85170d19bb1d 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=8a0a6a4bf487f046e58afec5d5d64d69 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=bd2b40c5361158ede3454f442850fdc9 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/optional.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=90d0140fe65976240cbb99382c2505f5 2500w" />
    </Frame>

    You can see the [PlanetScale airbyte-source README](https://github.com/planetscale/airbyte-source/blob/main/README.md) for more details on these options.
  </Step>

  <Step>
    Click "**Set up source**" to connect.
  </Step>
</Steps>

You should get a success message that the connection test passed.

### Choose your destination

With the connection complete, you can now choose your destination.

<Steps>
  <Step>
    Click "**Destinations**" in the sidebar or the "**New destination**" button on the source connection page.
  </Step>

  <Step>
    Set up the destination you want to sync your data to.
  </Step>
</Steps>

Each destination should have a Setup Guide linked on its destination setup page.

### Configure a connection

Now to get the connection fully set up.
Click on "Connections" on the left side bar.
If you have not yet set up any connectors, you should see this:

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=57549ae292673f7ca90957f6dd42e190" alt="Airbyte - New connection" data-og-width="2552" width="2552" data-og-height="1326" height="1326" data-path="docs/images/assets/docs/integrations/airbyte/create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=3d64b2ee1c49472102ff37b60b45d1c8 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=4cedbe097f5f50777d915a038b62c812 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=329e8d1d5ecba847d241b4f36a19a1c1 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=206ec13c826bcd8d225b482748e7d9f1 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=88b11bdea316e0e93e417a9133c4e87f 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/create.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1bd27e0595fc879ec5e1620627868a17 2500w" />
</Frame>

Click the button to set up a connection.
Otherwise, click "**New Connection**" in the top right corner.
From here, follow these steps:

<Steps>
  <Step>
    On the "**Define source**" page, choose your PlanetScale source as the **source**.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=122d64604916ed970c722c9c8a8224bb" alt="Airbyte - Source" data-og-width="2252" width="2252" data-og-height="575" height="575" data-path="docs/images/assets/docs/integrations/airbyte/source.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=732bb48274fc60a831deef96f7f3a76c 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=ef8a06c77ac9231efef47bb68c9847cc 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=bb1b69abe4de4eb885a88ec6bc7e8b15 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=f1f31552437842b083d61a6bfae0b3da 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=22fcc667d657276bf8d182438365090a 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/source.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=caf26f2ac9dd1e99f601cc72bf33bf6d 2500w" />
    </Frame>
  </Step>

  <Step>
    On the "**Define destination**" page, select the **destination** you want to sync your PlanetScale data to.
    For this demo, we are using a CSV destination.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9e666c58a217148bc5eeb50ee7af5781" alt="Airbyte - Source" data-og-width="2253" width="2253" data-og-height="638" height="638" data-path="docs/images/assets/docs/integrations/airbyte/destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=817c7746574cb2d96b7cb2716bb9be68 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2100502590cd938fe514a33dc534b369 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d528b4e08a0062fe61859e9cb375d86a 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=5c44c77506555de4fc103e91899aa318 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=d764edee220bf7efb47d4383cdc5685d 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/destination.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1113b0e555ba96677279e48cc997e5a1 2500w" />
    </Frame>
  </Step>

  <Step>
    On the "**Select streams**" page, select a sync mode.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=1b421fd50ce7af795468970b1a5b65e3" alt="Airbyte - Source" data-og-width="2252" width="2252" data-og-height="1019" height="1019" data-path="docs/images/assets/docs/integrations/airbyte/streams.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e17c18e63dfc972e4174a31ae885734f 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=46815452786a2293cf68af06509b4491 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=da45da2c551116b61b685bd70384c3de 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7173fc0c3ab932af03024b5cb5c2ec8e 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=307500b930fa91fd16f614142be48d52 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/streams.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=cf4c9fe7aaa25401603c1e0ca3a09ca1 2500w" />
    </Frame>
  </Step>

  <Step>
    Also on this page, you will need to select the specific tables and columns you want to sync. For each, choose what type of sync mode you'd like to use for each source table.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=42dc150525ebf7d9153f427e4dda03c8" alt="Airbyte - Sync" data-og-width="1259" width="1259" data-og-height="718" height="718" data-path="docs/images/assets/docs/integrations/airbyte/sync.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7cbea68ebcca591800938d4e3727f300 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9974d2bb3cda98079ee69cbe41975f09 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=0111c403cb4baaa491ae40d104fd0b81 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9261a8fcf4c4f25553a4efbb7537dd70 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=b079bb2ef5e55820ca31414968e7d77e 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/sync.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=dfed6a2e1823f2fdddddb1bfa91a4845 2500w" />
    </Frame>

    * **Incremental** — Incremental sync pulls *only* the data that has been modified/added since the last sync. We use [Vitess VStream](https://vitess.io/docs/concepts/vstream/) to track the stopping point of the previous sync and only pull any changes since then.
    * **Full refresh** — Full refresh pulls *all* data at every scheduled sync frequency.
  </Step>

  <Step>
    On the "**Configure connection**" page, choose a sync frequency, which is how often we will connect to your PlanetScale database to download data.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=7f8c857355fc78335edf1f5530e113aa" alt="Airbyte - Connection" data-og-width="4498" width="4498" data-og-height="2580" height="2580" data-path="docs/images/assets/docs/integrations/airbyte/connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=6ecea76451147ff86116041d09fb54fd 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=00a123c6e1acf6eed73f694c01324520 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2a85a04a3f67500aa4ee4827e7c33162 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=6c6519255a181eb101f5d671ba986e18 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=8f716411648dc8d6e344356a9f1dacad 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/connection.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=9b0db125a4d92fbb9a216b61e0172403 2500w" />
    </Frame>
  </Step>

  <Step>
    Click "**Finish and sync**".
  </Step>
</Steps>

Everything is now configured to pull your PlanetScale data into Airbyte and sync it to the selected destination on the schedule you chose. To run the connection, click "**Connections**" > "**Launch**".

## Handling schema changes

Airbyte will not automatically detect when you make schema changes to your PlanetScale database. If you drop a column, your sync should throw an error as it looks for a column that doesn't exist. However, if you add a column, the sync will continue without any errors. Airbyte will be unaware of the new column altogether. This is known as schema drift.

Whenever you perform a schema change, you need to notify Airbyte of it:

<Steps>
  <Step>
    In the Airbyte dashboard, click "**Connections**", select the connection, then navigate to the "**Schema**" tab.
  </Step>

  <Step>
    Click "**Refresh source schema**".
  </Step>

  <Step>
    Click "**Save changes**". Keep in mind, this might delete all data for the connection and start a new sync from scratch.
  </Step>
</Steps>

## Stopping Airbyte

At any point, you can disable any incremental or full syncs by going to the 'Connection' settings page and clicking 'Delete this connection'. This will not touch any of the source or destination data, but will prevent Airbyte from doing any further operations.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=709a4f7998328d6720fb7fe8f84254be" alt="Airbyte - PlanetScale disconnection" data-og-width="2428" width="2428" data-og-height="1288" height="1288" data-path="docs/images/assets/docs/integrations/airbyte/delete.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=27e4d0c7a87604c466f70977b71f0b64 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=2e1847c2ba136082c014e78c5f5060b5 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=da39b6b2f9d3c2bb576ece90d0d3c4cc 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=558138c0c9d44171f93e777d6ea23ab2 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=35de7064cf934e4b7d0aa95118d3382e 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/airbyte/delete.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=54be9992cd4a4112b9688eeb5a778f89 2500w" />
</Frame>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt