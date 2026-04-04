# Source: https://render.com/docs/connect-to-mongodb-atlas.md

# Connecting to MongoDB Atlas

This guide walks through connecting your Render-hosted application to a database hosted on [MongoDB Atlas](https://www.mongodb.com/atlas/database). This is an alternative to hosting a containerized instance of MongoDB on Render. If you prefer to host your own MongoDB instance on Render, see [Deploy MongoDB](/deploy-mongodb).

For advanced usage and troubleshooting, see the [MongoDB documentation](https://www.mongodb.com/docs/)

## Create and configure a database

You complete these steps in the MongoDB Atlas web interface.

1. Select one of the following deployment options for your database:

   - Serverless
   - Dedicated
   - Shared

2. Select AWS as the cloud provider and pick the AWS region closest to the region where your Render app is deployed. You can also set the cluster tier, cluster name, and any additional settings at this point. Click *Create Cluster*.

   | *Render Region*    | *Database Region*                                                            |
   | -------------------- | ------------------------------------------------------------------------------ |
   | `Oregon, USA`        | `Oregon (us-west-2)`                                                           |
   | `Ohio, USA`          | Dedicated tier: `Ohio (us-east-2)`   Shared tier: `N. Virginia (us-east-1)` |
   | `Virginia, USA`      | `Virginia (us-east-1)`                                                         |
   | `Frankfurt, Germany` | `Frankfurt (eu-central-1)`                                                     |
   | `Singapore`          | `Singapore (ap-southeast-1)`                                                   |

3. Choose an authentication method. This guide assumes you are using a username and password for authentication. You could also use a [Certificate](https://www.mongodb.com/docs/manual/core/security-x.509/).

4. Create a user profile for the new database and make a note of your database username and password. You will create environment variables for these values in your Render service connecting to Atlas.

5. Update cluster connections under "Network Access". Add your Render service's [outbound IP addresses](outbound-ip-addresses).

   [image: MongoDB Atlas IP]

6. Under "Connection Method", select "Connect your Application". Pick the Mongo driver and version used in your Render service to create a [connection string URI](https://www.mongodb.com/docs/manual/reference/connection-string/).

## Connect to your application on Render

1. Return to the Render Dashboard and create [environment variables](configure-environment-variables) for `username` and `password` in your Render service using the database username and password your created above.

   - There are some characters that require special treatment. See the [MongoDB documentation on connection string formats](https://www.mongodb.com/docs/manual/reference/connection-string/#std-label-connections-standard-connection-string-format)

2. Add connection details to your code by following the steps for your app's language or framework.

That's it! Your Render service should now be able to connect to your MongoDB Atlas instance.

## Further reading

MongoDB supports a variety of [drivers](https://www.mongodb.com/docs/drivers/). This guide highlights some of the most useful resources for Python and Node applications.

### [Python](https://www.mongodb.com/docs/drivers/python/)

The method for adding a database connection to your Python application code depends on whether your application is synchronous or asynchronous.

Use [Pymongo](https://www.mongodb.com/docs/drivers/pymongo/) in your application to connect to MongoDB (for synchronous applications)

- [Tutorial for completing common database operations with Pymongo](https://pymongo.readthedocs.io/en/stable/tutorial.html)

Use [Motor](https://www.mongodb.com/docs/drivers/motor/) in your Python app to connect to MongoDB Atlas (for asynchronous applications using either Tornado or asyncio.

- [Tutorial for completing common database operations using Motor with Tornado](https://motor.readthedocs.io/en/stable/tutorial-tornado.html)
- [Tutorial for completing common database operations using Motor with asyncio](https://motor.readthedocs.io/en/stable/tutorial-asyncio.html)

### [Node](https://www.mongodb.com/docs/drivers/node/current/quick-start/)

- [Guide to CRUD operations for Interacting with the Database in Node Applications](https://www.mongodb.com/docs/drivers/node/current/fundamentals/crud/#std-label-node-crud-landing)