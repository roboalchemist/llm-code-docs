# Source: https://docs.airbyte.com/platform/connector-development/connector-builder-ui/tutorial.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/connector-builder-ui/tutorial.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/connector-builder-ui/tutorial.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/connector-builder-ui/tutorial.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/connector-builder-ui/tutorial.md

# Tutorial

Copy Page

This tutorial will walk you through the creation of an Airbyte connector using the connector builder UI to read and extract data from an HTTP API.

You will build a connector reading data from the Exchange Rates API, but the steps apply to other HTTP APIs you might be interested in integrating with.

The API documentation can be found [here](https://apilayer.com/marketplace/exchangerates_data-api). In this tutorial, we will read data from the following endpoints:

* `Latest Rates Endpoint`
* `Historical Rates Endpoint`

With the end goal of implementing a source connector with a single `Stream` containing exchange rates going from a base currency to many other currencies. The output schema of our stream will look like the following:

```
{
  "base": "USD",
  "date": "2022-07-15",
  "rates": {
    "CAD": 1.28,
    "EUR": 0.98
  }
}
```

## Step 1 - Setup[​](#step-1---setup "Direct link to Step 1 - Setup")

### Setting up Exchange Rates API key[​](#setting-up-exchange-rates-api-key "Direct link to Setting up Exchange Rates API key")

Before we get started, you'll need to generate an API access key for the Exchange Rates API. This can be done by signing up for the Free tier plan on [Exchange Rates API](https://apilayer.com/marketplace/exchangerates_data-api):

1. Visit <https://apilayer.com> and click Sign In on the top right - either sign into an existing account or sign up for a new account on the free tier.
2. Once you're signed in, visit <https://apilayer.com/marketplace/exchangerates_data-api>
3. You should see an API Key displayed with a `Copy API Key` button next to it. This is your API key.

### Setting up the environment[​](#setting-up-the-environment "Direct link to Setting up the environment")

Besides an Exchange Rates API key, only a browser and an up-to-date running Airbyte instance is required. There are two ways to accomplish this:

* Sign up on [cloud.airbyte.com](https://cloud.airbyte.com/)
* Download and run Airbyte [on your own infrastructure](https://github.com/airbytehq/airbyte#quick-start). Make sure you are running version 0.43.0 or later

## Step 2 - Basic configuration[​](#step-2---basic-configuration "Direct link to Step 2 - Basic configuration")

### Creating a connector builder project[​](#creating-a-connector-builder-project "Direct link to Creating a connector builder project")

When developing a connector using the connector builder UI, the current state is saved in a connector builder project. These projects are saved as part of the Airbyte workspace and are separate from your source configurations and connections. In the last step of this tutorial you will publish the connector builder project to make it ready to use in connections to run syncs.

To get started, follow the following steps:

* Visit the Airbyte UI in your browser
* Go to the connector builder page by clicking the "Builder" item in the left hand navigation bar
* Select "Start from scratch" to start a new connector builder project (in case you have already created builder connectors before, click the "New custom connector" button in the top right corner)
* Set the connector name to `Exchange Rates (Tutorial)`

Your connector builder project is now set up. The next steps describe how to configure your connector to extract records from the Exchange Rates API.

### Setting up global configuration[​](#setting-up-global-configuration "Direct link to Setting up global configuration")

On the "global configuration" page, general settings applying to all streams are configured - the base URL that requests are sent to, as well as configuration for how to authenticate with the API server.

* Set the base URL to `https://api.apilayer.com`
* Select the "API Key" authentication method
* Set the "Header" to `apikey`

The actual API Key you copied from apilayer.com will not be part of the connector itself - instead it will be set as part of the source configuration when configuring a connection based on your connector in a later step.

You can find more information about authentication method on the [authentication concept page](/platform/1.6/connector-development/connector-builder-ui/authentication.md).

### Setting up and testing a stream[​](#setting-up-and-testing-a-stream "Direct link to Setting up and testing a stream")

Now that you configured how to talk the API, let's set up the stream of records that will be sent to a destination later on. To do so, click the button with the plus icon next to the "Streams" section in the side menu and fill out the form:

* Set the name to "Rates"
* Set the "URL path" to `/exchangerates_data/latest`
* Submit

Now the basic stream is configured and can be tested. To send test requests, supply testing values by clicking the "Testing values" button in top right and pasting your API key in the input.

This form corresponds to what a user of this connector will need to provide when setting up a connection later on. The testing values are not saved along with the connector project.

Now, click the "Test" button to trigger a test read to simulate what will happen during a sync. After a little while, you should see a single record that looks like this:

```
{
  "base": "EUR",
  "date": "2023-04-13",
  "rates": {
    "AED": 4.053261,
    "AFN": 95.237669,
    "ALL": 112.964844,
    "AMD": 432.048005,
    // ...
  }
}
```

In a real sync, this record will be passed on to a destination like a warehouse.

The request/response tabs are helpful during development to see which requests and responses your connector will send and receive from the API.

The detected schema tab indicates the schema that was detected by analyzing the returned records; this detected schema is automatically set as the declared schema for this stream, which you can see by visiting the Declared schema tab in the center stream configuration view.

## Step 3 - Advanced configuration[​](#step-3---advanced-configuration "Direct link to Step 3 - Advanced configuration")

### Making the stream configurable[​](#making-the-stream-configurable "Direct link to Making the stream configurable")

The exchange rate API supports configuring a different base currency via query parameter - let's make this part of the user inputs that can be controlled by the user of the connector when configuring a source, similar to the API key.

To do so, follow these steps:

* Scroll down to the "Query Parameters" section and add a new query parameter
* Set the key to `base`
* For the value, click the user icon in the input and select "New user input"
* Set the name to "Base"
* Click "Create"

The value input is now set to `{{ config['base'] }}`. When making requests, the connector will replace this placeholder by the user supplied value. This syntax can be used in all fields that have a user icon on the right side, see the full reference [here](/platform/connector-development/config-based/understanding-the-yaml-file/reference.md#variables).

Now your connector has a second configuration input. To test it, click the "Testing values" button again, set the "Base" to `USD`. Then, click the "Test" button again to issue a new test read.

The record should update to use USD as the base currency:

```
{
    "base": "USD",
    "date": "2023-04-13",
    "rates": {
      "AED": 3.6723,
      "AFN": 86.286329,
      "ALL": 102.489617,
      "AMD": 391.984204,
      // ...
    }
}
```

### Adding incremental reads[​](#adding-incremental-reads "Direct link to Adding incremental reads")

We now have a working implementation of a connector reading the latest exchange rates for a given currency. In this section, we'll update the source to read historical data instead of only reading the latest exchange rates.

According to the API documentation, we can read the exchange rate for a specific date range by querying the `"/exchangerates_data/{date}"` endpoint instead of `"/exchangerates_data/latest"`.

To configure your connector to request every day individually, follow these steps:

* On top of the form, change the "URL Path" input to `/exchangerates_data/{{ stream_interval.start_time }}` to [inject](/platform/connector-development/config-based/understanding-the-yaml-file/reference.md#variables) the date to fetch data for into the path of the request
* Enable "Incremental sync" for the Rates stream
* Set the "Cursor Field" to `date` - this is the property in our records to check what date got synced last
* Set the "Cursor Field Datetime Format" to `%Y-%m-%d` to match the format of the date in the record returned from the API
* Leave start time to "User input" so the end user can set the desired start time for syncing data
* Leave end time to "Now" to always sync exchange rates up to the current date
* In a lot of cases the start and end date are injected into the request body or query parameters. However in the case of the exchange rate API it needs to be added to the path of the request, so disable the "Inject start/end time into outgoing HTTP request" options
* Open the "Advanced" section and enable "Split up interval" so that the connector will partition the dataset into chunks
* Set "Step" to `P1D` to configure the connector to do one separate request per day
* Set the "Cursor granularity" to `P1D` to tell the connector the API only supports daily increments
* Set a start date (like `2023-06-11`) in the "Testing values" menu
* Hit the "Test" button to trigger a new test read

Now, you should see a dropdown above the records view that lets you step through the daily exchange rates along with the requests performed to fetch this data. Note that in the connector builder at most 5 partitions are requested to speed up testing. During a proper sync the full time range between your configured start date and the current day will be executed.

When used in a connection, the connector will make sure exchange rates for the same day are not requested multiple times - the date of the last fetched record will be stored and the next scheduled sync will pick up from where the previous one stopped.

You can find more information about incremental syncs on the [incremental sync concept page](/platform/1.6/connector-development/connector-builder-ui/incremental-sync.md).

## Step 4 - Publishing and syncing[​](#step-4---publishing-and-syncing "Direct link to Step 4 - Publishing and syncing")

So far, the connector is only configured as part of the connector builder project. To make it possible to use it in actual connections, you need to publish the connector. This captures the current state of the configuration and makes the connector available as a custom connector within the current Airbyte workspace.

To use the connector for a proper sync, follow these steps:

* Click the "Publish" button and publish the first version of the "Exchange Rates (Tutorial)" connector
* Go to the "Connections" page and create a new connection
* As Source type, pick the "Exchange Rates (Tutorial)" connector you just created
* Set API Key, base currency and start date for the sync - to avoid a large number of requests, set the start date to one week in the past
* Click "Set up source" and wait for the connection check to validate the provided configuration is valid
* Set up a destination - to keep things simple let's choose the "E2E Testing" destination type
* Click "Set up destination", keeping the default configurations
* Wait for Airbyte to check the record schema, then click "Set up connection" - this will create the connection and kick off the first sync
* After a short while, the sync should complete successfully

Congratulations! You just completed the following steps:

* Configured a production-ready connector to extract currency exchange data from an HTTP-based API:

  <!-- -->

  * Configurable API key, start date and base currency
  * Incremental sync to keep the number of requests small

* Tested whether the connector works correctly in the builder

* Made the working connector available to configure sources in the workspace

* Set up a connection using the published connector and synced data from the Exchange Rates API

## Next steps[​](#next-steps "Direct link to Next steps")

This tutorial didn't go into depth about all features that can be used in the connector builder. Check out the concept pages for more information about certain topics:

* [Authentication](/platform/connector-development/connector-builder-ui/authentication.md)
* [Record processing](/platform/connector-development/connector-builder-ui/record-processing.md)
* [Pagination](/platform/connector-development/connector-builder-ui/pagination.md)
* [Incremental sync](/platform/connector-development/connector-builder-ui/incremental-sync.md)
* [Partitioning](/platform/connector-development/connector-builder-ui/partitioning.md)
* [Error handling](/platform/connector-development/connector-builder-ui/error-handling.md)

Not every possible API can be consumed by connectors configured in the connector builder. If you need more flexibility, consider using the [Low Code CDK](/platform/connector-development/config-based/low-code-cdk-overview.md) or the [Python CDK](/platform/connector-development/cdk-python/.md) to build a connector with more advanced features.
