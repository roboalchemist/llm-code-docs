# Source: https://docs.port.io/build-your-software-catalog/custom-integration/ocean-custom-integration/installation-types/self-hosted/build-your-integration.md

# Build your integration

This interactive guide will help you generate everything you need to connect your API to Port.

**How it works:**

1. Configure your API connection settings
2. Choose an endpoint and select which fields to sync
3. Get your installation commands, blueprint, and mapping configuration

***

## Step 1: Configure your API[â](#step-1-configure-your-api "Direct link to Step 1: Configure your API")

Set up the connection details for your API. These settings apply globally to all endpoints you'll sync from this API.

**What you're configuring:**

* **Base URL**: The root URL that all endpoint paths will be appended to
* **Authentication**: How your API verifies requests (bearer token, API key, basic auth, or none)
* **Pagination** (optional): How to fetch data across multiple pages if your API uses pagination
* **Performance settings** (optional): Timeouts, concurrent requests, SSL verification

Think of this as setting up the "connection" - these settings will be used for every API call the integration makes.

**Base URL**https\://api.example.com**Authentication**

\[x]Bearer Token\[ ]API Key\[ ]Basic Auth\[ ]None

â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢

**Advanced Configuration**

**Pagination (optional)**

\[x]None\[ ]Offset/Limit\[ ]Page/Size\[ ]Cursor

**Request Timeout (seconds)**&#x33;0Maximum time to wait for API response (default: 30)**Max Concurrent Requests**10Maximum number of parallel API requests (default: 10)\[x]Verify SSL certificates

***

## Step 2: Choose what data to sync[â](#step-2-choose-what-data-to-sync "Direct link to Step 2: Choose what data to sync")

Now that your API connection is configured, let's define what data to sync. This step helps you map a specific API endpoint to a Port blueprint.

**What you'll do:**

1. **Specify the endpoint path** (e.g., `/api/v1/users`) that you want to sync
2. **Paste a sample API response** so we can detect the data structure
3. **Select the data path** - tell us where the array of items is in the response (e.g., `.data`, `.users`, or root array)
4. **Configure the blueprint** - give it an identifier and title
5. **Choose which fields to sync** - select the fields you want to ingest and mark which field is the unique identifier

The builder will automatically detect field types (string, number, boolean, email, date, URL) from your sample response.

### 1ï¸â£ Enter Your Endpoint

/api/v1/users

### 2ï¸â£ Paste API Response

Test your endpoint (e.g., with `curl`) and paste a sample response here:

{
"data": \[
&#x20;   {
&#x20;     "id": 1,
&#x20;     "name": "John Doe",
&#x20;     "email": "john\@example.com",
&#x20;     "role": "admin"
&#x20;   },
&#x20;   {
&#x20;     "id": 2,
&#x20;     "name": "Jane Smith",
&#x20;     "email": "jane\@example.com",
&#x20;     "role": "user"
&#x20;   }
&#x20; ],
&#x20; "meta": {
&#x20;   "total": 2,
&#x20;   "page": 1
&#x20; }
}

### 3ï¸â£ Select Data Path

**Select the array** that contains the items you want to sync to Port:

\[ ]data2

<!-- -->

items

***

## Step 3: Install and create in Port[â](#step-3-install-and-create-in-port "Direct link to Step 3: Install and create in Port")

You're all set! Based on your configuration, we've generated everything you need:

**What you'll get:**

* **Installation commands** (Helm or Docker) with all your settings pre-configured
* **Blueprint JSON** to create the data model in Port
* **Mapping YAML** to configure which fields to sync

Simply copy and run these in order to complete your integration setup.

#### ð Complete Step 2 to generate your configuration

You need to:

* **Enter a Blueprint Identifier** (e.g., "user", "project")
* **Select an Identifier field** (click "ID" button next to a field)

Once complete, this section will show your installation commands, blueprint JSON, and mapping configuration.

Port credentials needed

Get your `PORT_CLIENT_ID` and `PORT_CLIENT_SECRET` from [Port Settings â Credentials](https://app.getport.io/settings).
