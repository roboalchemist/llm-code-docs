# Source: https://getlago.com/docs/integrations/usage/hightouch.md

# Hightouch

> Hightouch is a Data Activation platform that syncs data from sources (database, warehouses, spreadsheet and much more) to business  applications and developer tools. This data can be sent to Lago, our usage-based billing platform, to automate your billing process  and ensure accurate invoicing for your customers.

Here's a step-by-step guide to help you get started:

## Prerequisites

**In Lago:**

1. Create a Lago organization to manage your billing and invoicing;
2. Create a Billable metric to track the usage of your customers;
3. Create a Plan and price the above billable metric to determine the billing rates for your customers; and
4. Create a Customer and assign the Plan.

**In Hightouch:**

1. Create a Hightouch account;
2. Create a data source (ideally, product usage of your customer);
3. Create a **HTTP Request** destination.

## Send usage from Hightouch to Lago

### Create a data source

To accomplish this, you'll need first to create a source in Hightouch. This can be done by following these simple steps:

1. Navigate to the **Sources** tab;
2. Add a **new source**; and
3. Choose and set up a data source that is available in Hightouch (it could be a database, a warehouse or a spreadsheet, for instance).

<Frame caption="Hightouch Sources">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=23c08f86883b1867132ea4c41179e758" data-og-width="3002" width="3002" data-og-height="1492" height="1492" data-path="integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1ad2443857dbf5bca703d68967308712 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=4d4e4f357ab4c43532ccbd333513caf5 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e98afe6670ec8fed5c23341fb18a0309 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c8f2206a211fd286a8b2fdac88a08270 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5914f18e7473dd9543ff863b5ece08b7 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-sources-3aa4046d89ec2208963b3e541408a249.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=cc3048597c1e6787983caf00d21472b8 2500w" />
</Frame>

### Use the HTTP Request destination

Lago uses Hightouch's HTTP Request to ingest usage. Here is how to set it up:

1. Go to the **Destinations** tab;
2. Select the **HTTP Request** destination;
3. Define your **Headers**. Lago requires `Authorization` (secret, used for the API Key) and `Content-Type: application/json` headers; and
4. Save this newly created destination.

<Frame caption="Hightouch HTTP Request Destination">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=3db4f863f80ce784b0a2bace0fc668be" data-og-width="3016" width="3016" data-og-height="1124" height="1124" data-path="integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=058a87165699c31febef340cdfe58cbb 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=0e5b7b4aa93202843852d938d05a1a09 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=d3aade7a6c70a42f48f8489cbffa3c5d 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=2bf6615d8e3304102943c90779ed5649 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=1ca0d3605322bbf1622e0c337e3ffb4a 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/hightouch-http-destination-d613e2e5663423ea83712c055d893333.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=eef366e682ccd5bedba0f174c6680126 2500w" />
</Frame>

### Create a Sync

In order to send usage from Hightouch to Lago, you will have to create a new **Sync**. To do so, go in the **Syncs** tab and create a new sync from a source to this HTTP Request destination.

1. Configure when you want to trigger the event (row added, row deleted, row updated);
2. Define `POST` as the targeted HTTP Method;
3. Define the targeted url (for usage events, use `https://api.getlago.com/api/v1/events`);
4. Send data as `JSON` and use the JSON editor;
5. Define rate limits, if applicable

### Example of JSON payload

You can define manually the JSON payload that will be sent to Lago. Note that Hightouch supports Liquid template language to insert variables from your source to your JSON payload. These variables are created following this syntax: `"{{ row.variable }}"`, *"variable"* being the column name of your source.

Here is a JSON payload example to send usage events to Lago:

```json  theme={"dark"}
{
  "event": {
    "transaction_id": "{{ row.transactionId }}",
    "external_customer_id": "{{ row.customerId }}",
    "code": "invoice_created",
    "properties": {
      "invoice_id": "{{ row.invoiceId }}"
  }
}
}
```

<Info>
  The `body` structure of the event depends on your use case. Please adapt it if needed (*ie: remove or add properties*).
</Info>

### Test and activate your sync

Note that you can test your sync with a data sample. As a result of this test, you should see data flowing into Lago, in the events list. Once you are ready to go, you can activate this sync, and define the periodic trigger.

<Frame caption="Hightouch Test Sync with Lago">
  <img src="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e4f2232fcdfac5c82d7b335bc80835a7" data-og-width="2514" width="2514" data-og-height="1456" height="1456" data-path="integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=280&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=e4b1fdeff3b2e838fb5eb889f05a42b2 280w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=560&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=64563ed74bf106539c7ec113349362bf 560w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=840&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=5f0284f3109b97c6ad45f1070cb902c4 840w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=1100&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=528bb6c00603940d451f0401dbd48cdd 1100w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=1650&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=c277b00b39d65f7bcc9cc3e23af7981f 1650w, https://mintcdn.com/lago-docs/aaVDsanqVM_V30mw/integrations/usage/images/sync-test-hightouch-34f6e41a10dd05b637841b6f4d1581fa.png?w=2500&fit=max&auto=format&n=aaVDsanqVM_V30mw&q=85&s=14291930b149b4d9067762564c1b836d 2500w" />
</Frame>

## Hightouch to Lago - demo video

If easier, please find a demo video explaining the full setup to send events from Hightouch to Lago.

<iframe width="700" height="500" src="https://www.youtube.com/embed/2NBmQYjrz40" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen />
