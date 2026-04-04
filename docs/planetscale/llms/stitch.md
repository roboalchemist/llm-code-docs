# Source: https://planetscale.com/docs/vitess/integrations/stitch.md

# Stitch integration

> With PlanetScale Connect, you can extract data from your PlanetScale database and safely load it into other destinations for analysis, transformation, and more.

We implemented an [Stitch Singer Tap](https://stitchdata.com/) as the pipeline between your PlanetScale source and selected destination. This document will walk you through how to connect your PlanetScale database to Stitch.

## How to connect

### Step 1 : Setup an Import API integration in Stitch.

PlanetScale's Stitch tap outputs records and metadata to stdout so that the `http tap` can import them into Stitch via [Stitch Import API](https://www.stitchdata.com/docs/developers/import-api/).
into Stitch via [Stitch Import API](https://www.stitchdata.com/docs/developers/import-api/)

<Steps>
  <Step>
    Sign up for a [StitchData](https://app.stitchdata.com/signup) account
  </Step>

  <Step>
    Once you've signed up, create an Integration by clicking on **Add Integration**.
  </Step>

  <Step>
    On the marketplace screen, type in **import** to narrow the list down to the **Import API**

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=cf44062fff5c6e1c1b33ad3cf25028c6" alt="Add Stitch Integration" data-og-width="2416" width="2416" data-og-height="950" height="950" data-path="docs/images/assets/docs/integrations/stitch/integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=29df37f8a0e7948265e54e3742c28f35 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=eb06af4050721748e3ce4f01a7921f1e 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ba03ec7e67f2b7e388355325cb76ff11 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=551bdfefbdaf9e0b9d3b1baa9650caa0 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=66dbc96ff1e33e6c03e380e1f3e555c3 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/integration.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b6a7b53e0e42e99c4f2e2fb1f03f1641 2500w" />
    </Frame>
  </Step>

  <Step>
    On the next screen, configure your integration name and destination.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ab151ca2cdce023f173779a9d66bc9e4" alt="Configure Stitch Integration" data-og-width="1618" width="1618" data-og-height="1834" height="1834" data-path="docs/images/assets/docs/integrations/stitch/configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=88e95c19553eda7e21bd1b660c41ea89 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=5b2f47231ab669bfbaf34b742c0d8e04 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b4f4a3a6afb6099051261563e2761467 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=c946304e33d6259894d386ea9e6c82b3 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ac6aaccdf5eab4cd9759b50743c7a8e4 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/configure.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=92410f36f2050aea65a64b304936fe2f 2500w" />
    </Frame>
  </Step>

  <Step>
    Once the integration is created, save the access token for use with the PlanetScale tap.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=3a942c46b78b5236ba0a4f56cc2df8a8" alt="Save Stitch API Token" data-og-width="1478" width="1478" data-og-height="760" height="760" data-path="docs/images/assets/docs/integrations/stitch/api-token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ad8bb6c3ced02f65643be5cb8238f1bf 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=ba25a7c639b3d13ae594638bd0fecef9 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=2c4d600369495ca2d419eabeabbcec1d 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=44a64a867975a5b2df1cbd970c235d39 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=4168322e436e009dbab7d7eef8689a86 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/api-token.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=b25b4403108ba3520df8d627acafb06a 2500w" />
    </Frame>
  </Step>
</Steps>

### Step 2 : Configure the PlanetScale Stitch Tap

In this step, we will connect your PlanetScale database to the PlanetScale Singer Tap.

<Steps>
  <Step>
    Click on the database and branch you want to connect to.
  </Step>

  <Step>
    Click "Connect", and select "Stitch source" from the "Connect with" dropdown.
  </Step>

  <Step>
    Leave this tab open, as you'll need to copy these credentials shortly.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=1a3e1e44268d2fc19ef5379f286dd988" alt="Stitch Source config" data-og-width="1148" width="1148" data-og-height="634" height="634" data-path="docs/images/assets/docs/integrations/stitch/connect.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=1f4bab3b21c7b331f1c85c33977e600b 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=7e8f28ac253ae633560bb1524a1b96eb 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=a2ba284821850894faf9360b256c8059 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=37d23a9496b20554d28f80995fb89a69 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=cc4b2c5e079acfc6b294d6c324417a04 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/connect.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=02a43d173615fed1833069459763aa4e 2500w" />
    </Frame>
  </Step>

  <Step>
    Copy the contents of `source.json` as a file on your local file system, and save it as `source.json`. This will now act
    as the `PlanetScale source config` when connecting the `PlanetScale Stitch Tap` to your database.
  </Step>
</Steps>

### Step 3: Run the PlanetScale Stitch Tap

<Steps>
  <Step>
    Install the PlanetScale Singer tap by running:

    ```bash  theme={null}
    brew install planetscale/tap/ps-singer-tap
    ```
  </Step>

  <Step>
    Install the PlanetScale Http tap by running

    ```bash  theme={null}
    brew install planetscale/tap/ps-http-tap
    ```
  </Step>

  <Step>
    Save the schema for your PlanetScale database.

    ```bash  theme={null}
    ps-singer-tap --config source.json  --discover > schema.json
    ```
  </Step>

  <Step>
    The `schema.json` file you saved in the previous step is a JSON document
    that describes all tables & columns available in your PlanetScale database. By default, no tables/columns are selected.
    You can select a column or table by setting its `selected` property in the table's `metadata` element in the JSON document to be true.
    Here's an example of selecting the `dept_no` property in a table.

    ```json  theme={null}
    {
      "metadata": {
        "selected": true,
        "inclusion": "available",
        "breadcrumb": ["properties", "dept_no"]
      }
    }
    ```
  </Step>

  <Step>
    Sync your PlanetScale database to Stitch by running the following command:

    ```bash  theme={null}
    ps-singer-tap --config source.json  --catalog schema.json | ps-http-tap  --api-token $(cat access_token)
    ```
  </Step>

  <Step>
    You should see an output similar to this:

    ```bash expandable theme={null}
    PlanetScale Tap : INFO : Syncing records for PlanetScale database : import-on-scaler
    PlanetScale Tap : INFO : syncing rows from stream "departments" from shard "-"
    PlanetScale Tap : INFO : [departments shard : -] peeking to see if there's any new rows
    PlanetScale Tap : INFO : new rows found, syncing rows for 1m0s
    PlanetScale Tap : INFO : [departments shard : -] syncing rows with cursor [shard:"-" keyspace:"import-on-scaler"]
    PlanetScale Tap : INFO : Syncing with cursor position : [], using last known PK : false, stop cursor is : [MySQL56/e42292e8-e28f-11ec-9c5b-d680f5d655b3:1-705,e4e20f06-e28f-11ec-8d20-8e7ac09cb64c:1-26,eba743a8-e28f-11ec-9227-62aa711d33c6:1-20]
    PlanetScale Tap : INFO : [departments shard : -] Continuing with cursor after server timeout
    PlanetScale Tap : INFO : [departments shard : -] peeking to see if there's any new rows
    HTTP Tap : INFO : flushing [20] messages for stream "departments"
    PlanetScale Tap : INFO : [departments shard : -] no new rows found, exiting
    HTTP Tap : INFO : Server response status : "OK", message : "Batch accepted"
    HTTP Tap : INFO : flushing [1] messages for stream "departments"
    HTTP Tap : INFO : Server response status : "OK", message : "Batch accepted"
    HTTP Tap : INFO : saving state to path : state/state-1656850746251.json
    ```
  </Step>

  <Step>
    Any state outputted by the PlanetScale Tap will be saved and you can look at the logs for the location.
    Here is an example of outputted state:

    ```bash  theme={null}
    HTTP Tap : INFO : saving state to path : state/state-1656850746251.json
    ```
  </Step>

  <Step>
    In this example, you should see that Stitch loaded `21` records to be replicated.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=af1bafbe3119ba224a421720b537085e" alt="Completed Stitch import" data-og-width="1630" width="1630" data-og-height="988" height="988" data-path="docs/images/assets/docs/integrations/stitch/success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=280&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fd59096872b00ed3ff6c36d5c24ae998 280w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=560&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=390fef253157c1dd13b51151bdbd8b30 560w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=840&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=fee7607b2a2843bffac67183c4d26acc 840w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=1100&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=bf5ec5bce2f9276389c80e2c051113ba 1100w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=1650&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=d80688c49f8083411b1fda51c6c191a1 1650w, https://mintcdn.com/planetscale-cad1a68a/vjR5C2sTgdIGKQJc/docs/images/assets/docs/integrations/stitch/success.png?w=2500&fit=max&auto=format&n=vjR5C2sTgdIGKQJc&q=85&s=11093e3b77900646d13b06a454dba8f5 2500w" />
    </Frame>
  </Step>

  <Step>
    To incrementally sync from this last sync position, pass the path to last saved state in step 7 as the `--state` argument when you run sync.
  </Step>
</Steps>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt