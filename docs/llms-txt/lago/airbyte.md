# Source: https://getlago.com/docs/integrations/data/airbyte.md

# Airbyte (ETL)

Airbyte is an open-source **data integration platform** used as an ETL. With this integration, you can connect Lago billing data to any warehouses.

## Destinations

You can push Lago billing data to destinations such as Snowflake, BigQuery, Redshift, S3 buckets or Azure, for instance.
The entire list of data destinations enabled by Airbyte is listed on their [destinations documentation](https://docs.airbyte.com/integrations/destinations/).

## Data available for extraction

With Airbyte's native integration of Lago, you can push the following billing data to warehouses:

* billable\_metrics
* plans
* coupons
* add\_ons
* invoices
* customers
* subscriptions

<Warning>
  At present this connector **only supports full refresh syncs** meaning that each time you use the connector it will sync all available records from scratch. Please use cautiously if you expect your API to have a lot of records.
</Warning>

Find the full documentation of [Airbyte's native Lago integration](https://docs.airbyte.com/integrations/sources/getlago/).

## 1. Connect Lago to Airbyte

First of all, you simply need to bring your Lago private API key.
In airbyte:

* Go to **Sources**;
* Select getLago as a source of data; and
* Paste your Lago private API key.

<Frame caption="Lago data source in Airbyte">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8de8a86a55eba4f57719b41b7bea22a1" data-og-width="2858" width="2858" data-og-height="1466" height="1466" data-path="integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8f4b5b5d4e7e25e8311b3b62b4d91509 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b42003dce0c49e99fdb6b6126746fa85 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=c78702fe88eae7c8583ed35ff656eeee 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=439146ea421972328a260899c0e8ace1 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=175b4e64ccd16a99c5c29a58869090a3 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-airbyte-source-e56dc399ab95d5f523683b5c62f3b3e5.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0114376a4288157769989ac63efa37ff 2500w" />
</Frame>

## 2. Select a destination

You can select any of the data destinations available in Airbyte. It could be a warehouse (BigQuery, Redshift, Snowflake...) or a file storage tool (S3, for instance). Please find here the entire list of [data destinations available in Airbyte](https://docs.airbyte.com/integrations/destinations/).

<Frame caption="Destination in Airbyte">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=d22ef1721d451312a2014a4c423d4ea8" data-og-width="2674" width="2674" data-og-height="866" height="866" data-path="integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=bc539f62d8a15fe76169133532f69d39 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=e63ab54c134997b4f1da58145d0aedba 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=76a0abb74a69b90469fd429e47c41cd6 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=677e1082965f00d06b441817284ea979 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=61aa94f4f2c1b99ade8fd60051422815 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/destination-airbyte-52676d7f8ffd515d98027fbe02eb2b05.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=8c0fcf4ce9963e8dfad652f50df8f4e2 2500w" />
</Frame>

## 3. Sync billing data

In the following example, we connected Lago billing data to Snowflake data warehouse. Obviously, you can select another destination if needed.

1. Create a **data sync** between Lago source and your destination;
2. Define a **sync frequency**; and
3. Activate the sync in Airbyte between Lago source and your destination.

This action will populate Lago billing data into a warehouse (Snowflake in our example).

<Frame caption="Lago data in Snowflake">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b77d199c49ce04e783e80c5c636cc9fd" data-og-width="2332" width="2332" data-og-height="786" height="786" data-path="integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=52a278072922422bd016521ab554c46e 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=1b834ed829f48dae9482a758e0f5c64e 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=da9eba3372493a417dd848f4c0965a3b 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=fea183ed57767f471290e5ef0df205e4 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=a247f0fc23037eadc5936dd6d70675d3 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/lago-data-snowflake-ec9a012ccb50edc332d6750de7246076.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=20b1ac77dd35169c1e9a0208c938118e 2500w" />
</Frame>

## 4. Query Lago billing data

Once the data has been populated in your destination, a warehouse in our example, you can easily query your billing data. Here is a query calculating your monthly revenue with Lago:

<Frame caption="Query in snowflake">
  <img src="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=7b5a86ea97e04088f6087bc006e51d90" data-og-width="1646" width="1646" data-og-height="1362" height="1362" data-path="integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=280&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=9405aa9ebba7efaa5780f1989b9655c1 280w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=560&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=52903fc775daa5fb892f048e85d3b9d0 560w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=840&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b3273c026018de603cdd5dc2dadae315 840w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=1100&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=b913d6c74ddaf2382a0b3f9cff6153c4 1100w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=1650&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=efb22c52978c37b2478d285ffad9cb54 1650w, https://mintcdn.com/lago-docs/xDoze7ebvXBe1su1/integrations/data/images/example-billing-query-snowflake-a4cf76e6bca92363215567a0e4e51f06.png?w=2500&fit=max&auto=format&n=xDoze7ebvXBe1su1&q=85&s=0e2b544b1c94f5766f2c18f23365b793 2500w" />
</Frame>
