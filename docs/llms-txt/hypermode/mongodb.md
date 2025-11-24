# Source: https://docs.hypermode.com/agents/connections/mongodb.md

# Using MongoDB with Hypermode

> Connect your Hypermode agent to MongoDB for scalable document database operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=28f495121d5abb53f4b1371b80e09db4" alt="MongoDB" width={48} height={48} width="895" height="2000" data-path="images/agents/connections/icons/mongodb.svg" srcset="https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=280&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=1c7f34db752dd3b347ea0a2ed9a51c01 280w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=560&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=cd9bdfb34bfef3a3a25d2a30464f6953 560w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=840&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=529aa893d7e2903b06bb52ccad86435f 840w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=1100&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=f111df13e2b8c763adb56861d4077204 1100w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=1650&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=42080aad23e872e87994d3b23c4eaa96 1650w, https://mintcdn.com/hypermode/hdAle6Bocil2pzje/images/agents/connections/icons/mongodb.svg?w=2500&fit=max&auto=format&n=hdAle6Bocil2pzje&q=85&s=7982c4ce0656533bf18a3ebb526de145 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">MongoDB</h2>

    <p className="text-gray-600 m-0">
      Document-oriented NoSQL database platform
    </p>
  </div>
</div>

## Overview

MongoDB is a popular NoSQL document database that provides flexible schema
design and powerful querying capabilities. This guide will walk you through
connecting your Hypermode agent to MongoDB, enabling seamless document
operations and data management for your applications.

## Prerequisites

Before connecting MongoDB to Hypermode, you'll need:

1. A [MongoDB Atlas account](https://www.mongodb.com/cloud/atlas) or local
   MongoDB installation
2. A MongoDB database with connection credentials
3. A [Hypermode workspace](https://hypermode.com/)

## Setting up MongoDB

### Step 1: Create your MongoDB Atlas account

If you haven't already, sign up for a
[free MongoDB Atlas account](https://www.mongodb.com/cloud/atlas) to get started
with cloud-hosted MongoDB.

### Step 2: Create a cluster and database

1. Create a new cluster in MongoDB Atlas
2. Set up database access credentials
3. Configure network access (whitelist IP addresses)
4. Create your first database and collection

Check the box to load sample data. This will create a movies database with
sample data in several collections.

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2edc54dda31307305754466310e760c9" alt="Create MongoDB cluster" width="2114" height="2296" data-path="images/connections/mongodb/create-cluster.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=02ce4552dfe039e4164f736108e652db 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=090f1b64ae7b19f6eb478581eae015e5 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=84da7ad0591d9be857e6b18b7a5a1dd8 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3e2166344e762d96b26e538d37e3c472 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ce50c5df1c7c5714fb180343b13c95a0 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-cluster.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a657440c93cd135a20c001c73dc2a2e3 2500w" data-optimize="true" data-opv="2" />

You'll also need to create a user and password for your database.

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b03a786b90391a3b9c73f2a56ec49620" alt="Create MongoDB user" width="1636" height="1388" data-path="images/connections/mongodb/create-user.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=727551dc3f973ec887e8c9cdfe46cb73 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=bee6a72eaf1f590af725642a4ed48444 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2085a1f67d0b3f570895f993c2986a10 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=41a4b609542c227cb2d1ebf71c8e2160 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=54df419dba6a449936a18fd3e98aadd5 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-user.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4aacac9145d3659bf3b35a83b645176c 2500w" data-optimize="true" data-opv="2" />

### Step 3: Generate connection string

Navigate to your cluster and get the connection string:

1. Click "Connect" on your cluster
2. Choose "Connect"
3. Copy the connection string and replace `<password>` with your database user
   password. You'll use this connection string to connect your Hypermode agent
   to MongoDB.

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7e9aa78e5f465d68b37317c1b29cc09c" alt="MongoDB connection string" width="1642" height="1956" data-path="images/connections/mongodb/connection-string.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e253eea13dc56d4d7da819bd5ec7edbe 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2a8f6844d9f496737f17bc4bc6f22f1f 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=23dadc31d529a002014fef08da26d466 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6d1625bee6ca46e2ed0bc452d4cf9623 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a0ba2ea8c3add8753630ce59423ecd5c 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/connection-string.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d83a378f256b59127626fb7e3de8122f 2500w" data-optimize="true" data-opv="2" />

<Note>
  Your connection string will look like:
  `mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority`
</Note>

### Step 4: Whitelist IP addresses

Navigate to your cluster and whitelist IP addresses to allow connections from
your Hypermode agent:

1. Click "Network Access" on your cluster
2. Add the IP address range `0.0.0.0/0` to allow connections from any IP address

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=8f36ec3130b93d281c54132680ff7342" alt="Whitelist IP addresses" width="1660" height="838" data-path="images/connections/mongodb/mongodb-connection-ip-address.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=dc6e81ddb4bd1435576e593f94393e53 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=49339332a7daae98367a8ec3a6c1ea92 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=d0fe2287e119270941655cf775d3ad9a 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=a685b0d2c56f2fd0aac297b2e6b20bb3 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=520eb90d2ec9b9033487bc93bed5cfa7 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-ip-address.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=790347356a22523fbd2aaa7271d8a4b1 2500w" data-optimize="true" data-opv="2" />

## Creating your MongoDB agent

### Step 1: Create a new agent

From the Hypermode interface, create a new agent manually:

1. Click the agent dropdown menu
2. Select "Create new Agent"

### Step 2: Configure agent settings

Use these recommended settings for your MongoDB agent:

* **Agent Name**: MongoAgent
* **Agent Title**: Connects to MongoDB
* **Description**: MongoAgent manages document operations
* **Instructions**: You have a connection to MongoDB and various other developer
  tools to streamline document data access and management. You can perform CRUD
  operations, aggregations, and complex queries on MongoDB collections.
* **Model**: GPT-4.1

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=0fd2f752e9ff410538b817bccbf94433" alt="Create agent modal" width="982" height="1104" data-path="images/connections/mongodb/create-agent-modal.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=290f3d5565c702b67bca9198059dcc5d 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=aeba0c79cf3b4f0b3421b721c920ec6c 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=75a7409e9ed369eeec8eb3642593a381 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e989f67f687bcf3865bf698dcbc9b529 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=14602a1604c79617019defd534c2e261 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/create-agent-modal.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=6565e223e8be0a65cb9264827caebaa9 2500w" data-optimize="true" data-opv="2" />

## Connecting to MongoDB

### Step 1: Add the MongoDB connection

Navigate to the **Connections** tab and add MongoDB:

1. Click "Add connection"
2. Select "MongoDB" from the dropdown

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=93904eb248aa42721e5774c9a65e115c" alt="Add MongoDB connection" width="1038" height="512" data-path="images/connections/mongodb/add-mongodb-connection.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=11deb06b902163280876ed7d9cbde580 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e5957e11c1bad7ef624c1a15016b041e 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3d8c6cc19e917564660bbea5c4e0daa6 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=fe6c59fbaa8f3915e60d11041169f063 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=723bf3f3c9af71c95d8b36623911faad 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-mongodb-connection.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=0d1aea30901531018b6a92b9068b2bd1 2500w" data-optimize="true" data-opv="2" />

### Step 2: Configure credentials

Enter your MongoDB credentials:

* **Username**: The username of your MongoDB user
* **Password**: The password of your MongoDB user
* **Database Name**: The default database to connect to
* **Hostname**: The hostname of your MongoDB cluster. This is the part of your
  MongoDB connection string that comes after `mongodb+srv://` and is a domain
  name. For example given the connection string
  `mongodb+srv://will:<db_password>@hypermodeturorials.o7ygcmn.mongodb.net/?retryWrites=true&w=majority&appName=HypermodeTurorials`,
  the hostname is `hypermodeturorials.o7ygcmn.mongodb.net`

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=0b14ae856e679ed9c2f88f97e72a1561" alt="MongoDB connection modal" width="776" height="1316" data-path="images/connections/mongodb/mongodb-connection-modal.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=29a643c8bcc8052b04351ce047c860ec 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=2890c7219be52e8c1c3a0097a7efef74 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=96abef512bfba82c06557bf7e2546100 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7fce62bc033d255f7844dcd98e3e4fee 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=bec0bc3bad52b7e063783ba97c306d42 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/mongodb-connection-modal.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=486de969f2e1798efe454ee7c5f3ff18 2500w" data-optimize="true" data-opv="2" />

<Warning>
  Keep your connection string secure! This contains your database credentials
  and should never be exposed in client-side code.
</Warning>

## Testing the connection

Your agent can create collections, add documents, and perform queries on your
MongoDB database. Since we created a sample movies database, let's test it out
using the sample data in MongoDB.

### Test 1: Query empty collections

Start a new thread and test with a simple query:

```text
Can you show me all movies in the database?
```

You should see a MongoDB tool call in the chat history, confirming the
connection works:

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=e8104410a01ebbdb3d3f9da58fcbc136" alt="Empty movies query" width="2348" height="2034" data-path="images/connections/mongodb/empty-movies.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=234bbb040b84098d0381dc6dac9f6c0e 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b16e6793c2fa56df2ab2a8187763f2a3 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=3081db8378e55a63105a2e8e6e46b1f1 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=63b4e6bcb8061d3cfc70e7af67bef198 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=4a4d46e60362df4b911ff2b7d42b29a3 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/empty-movies.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7f192ed20702ec26d82853d1957dd02a 2500w" data-optimize="true" data-opv="2" />

### Test 2: Insert documents

Now try adding data to your database:

```text
Can you add The Matrix from 1999 directed by the Wachowskis to my MongoDB database?
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f61278d8112dbc60dd10cb95b88f0426" alt="Add Matrix movie" width="2338" height="1920" data-path="images/connections/mongodb/add-matrix.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=b7d86ef478870e554cdba2eea6259427 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f5e439962ea1f6ea18da72595438475f 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=0a1450521c4c13eb0938e522408af374 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=94843b73325ecce72980aed5ad10f14c 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=49d9343c865fda27d6d2cc1f7c1e82d7 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/add-matrix.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=392c9d9d4a64e5152a65adb4ff30a6af 2500w" data-optimize="true" data-opv="2" />

### Test 3: Complex queries

Test more advanced operations:

```text
Can you find all movies from the 1910s and show their average rating?
```

<img src="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=144e1a39bcd6d9bd6176120c7f05a9d7" alt="Complex query" width="2338" height="1992" data-path="images/connections/mongodb/complex-query.png" srcset="https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=280&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=75676308554d587c2c20f7f280202293 280w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=560&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7514f5a08051109b13b36b6b1f7d95d1 560w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=840&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=f933d22950123b3f0fc62c85d3675a91 840w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=1100&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=ce245efeeca32dbfc837028845f3e4f7 1100w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=1650&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7ef346e3b12deb12c19e3355e955739c 1650w, https://mintcdn.com/hypermode/9QWuPyr_PIBFkocg/images/connections/mongodb/complex-query.png?w=2500&fit=max&auto=format&n=9QWuPyr_PIBFkocg&q=85&s=7712b63d3afb375b8f9a28972e974a8a 2500w" data-optimize="true" data-opv="2" />

## What you can do

With your MongoDB connection established, your agent can:

* **Query documents** with complex filters and projections
* **Insert, update, and delete** documents
* **Perform aggregations** for data analysis and reporting
* **Work with embedded documents** and arrays
* **Execute transactions** for multi-document operations
* **Create indexes** for improved query performance
* **Integrate with other tools** like GitHub, Slack, and Stripe

## Best practices

1. **Schema design**: Design your document structure to match your query
   patterns
2. **Indexing**: Create indexes on frequently queried fields
3. **Connection management**: Use connection pooling for better performance
4. **Error handling**: Your agent will handle common database errors gracefully
5. **Data validation**: Consider using MongoDB schema validation for data
   consistency

## Advanced operations

### Aggregation pipelines

Your agent can perform complex aggregation operations:

```text
Can you group movies by decade and show the count and average rating for each decade?
```

### Text search

Enable text search on your collections:

```text
Can you find all movies that mention "robot" in their title or description?
```

### Geospatial queries

For location-based data:

```text
Find all movie theaters within 10 miles of coordinates [40.7128, -74.0060]
```

## Troubleshooting

### Common connection issues

1. **Network access**: Ensure your IP is whitelisted in MongoDB Atlas
2. **Authentication**: Verify your username and password are correct
3. **Connection string**: Check that your connection string format is valid
4. **Database permissions**: Ensure your user has appropriate read/write
   permissions

### Performance optimization

1. **Query optimization**: Use explain() to analyze query performance
2. **Index usage**: Monitor index usage and create appropriate indexes
3. **Document size**: Keep documents reasonably sized for better performance
4. **Connection pooling**: Configure appropriate connection pool settings

## Learn more

* [MongoDB Documentation](https://docs.mongodb.com/)
* [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/)
* [MongoDB Query Language](https://docs.mongodb.com/manual/tutorial/query-documents/)
* [Aggregation Framework](https://docs.mongodb.com/manual/aggregation/)

<Tip>
  Combine MongoDB with other Hypermode connections to build powerful workflows.
  For example, use GitHub to track code changes that affect your data models, or
  Slack to notify your team of important database updates and analytics
  insights.
</Tip>

## Example workflows

### E-commerce integration

```text
Track inventory levels and automatically update product availability when stock changes
```

### Content management

```text
Manage blog posts, user comments, and media assets with flexible document structures
```

### Analytics and reporting

```text
Generate real-time reports on user behavior, sales metrics, and application performance
```
