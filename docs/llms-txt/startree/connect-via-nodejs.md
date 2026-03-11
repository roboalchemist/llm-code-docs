# Source: https://docs.startree.ai/corecapabilities/query_data/query_interfaces/connect-via-nodejs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting to StarTree Cloud via Node.js

Applications can use this sample client Node.js driver to query Pinot.

<Warning>This solution may not scale to meet performance and throughput requirements for your use case.</Warning>

### Integrate Pinot in Node.js applications

1. Install axios.

```
 npm install axios
```

1. Contact StarTree Support to obtain the following information:

* **Controller URL:** The general format is `https://pinot.<random-string>.cp.s7e.startree.cloud`
* **Broker URL:** The general format is `https://pinot.<random-string>.cp.s7e.startree.cloud`
* **AUTH\_TOKEN**

1. Run the Node.js driver script:

```
node queryPinot.js
```

## queryPinot.js: Node.js driver script

```
const axios = require('axios');
    // Pinot broker and controller URLs
    const pinotBrokerUrl = '<Broker URL mentioned above>';
    const pinotControllerUrl = '<Controller URL mentioned above>';
    // Function to query Pinot broker
    async function queryPinotBroker() {
     try {
    const response = await axios.post(`${pinotBrokerUrl}/query/sql`, {
      // Add your SQL query here
      sql: 'SELECT count(*) FROM <TABLE_NAME>,
    }, {
      headers: {
        Authorization: 'Basic <AUTH_TOKEN>',
      }
    });
    console.log('Query Result:', response.data);
  } catch (error) {
    console.error('Error querying Pinot broker:', error.message);
  }
}
// Function to fetch Pinot table schema from controller
async function getPinotTableSchema(tableName) {
  try {
    const response = await axios.get(`${pinotControllerUrl}/tables/${tableName}/schema`, {
      headers: {
        Authorization: 'Basic <AUTH_TOKEN>',
      }
    });
    console.log('Table Schema:', response.data);
  } catch (error) {
    console.error('Error fetching table schema:', error.message);
  }
}

// Example usage
queryPinotBroker();
getPinotTableSchema('companies_v1');
```

## Obtaining Username and Password

You can cenerate an API token in the [Data Portal](/corecapabilities/security/manage-api-tokens#generating-an-api-token) or using the [REST API](/api-reference/introduction#authentication-%26-prerequisites). Then, [obtain the username and password from the service token](/corecapabilities/security/manage-api-tokens#extracting-username-and-password-from-a-startree-bearer-token)

Th username and password are used to authorize your API requests.

## Finding Your Broker URL

To find the correct Broker URL for your table in StarTree Cloud:

1. Access the Data Portal.
2. Click on **Tables**.
3. Select the specific table you want to query.
4. From the browser address bar, copy the URL to your Pinot cluster. For example, if the URL shown is `https://dp.1abcde6.cp.s7e.startree.cloud/tables`, then the Broker URL for the table will be `broker.pinot.1abcde6.cp.s7e.startree.cloud`.

Built with [Mintlify](https://mintlify.com).
