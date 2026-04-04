# Source: https://northflank.com/docs/v1/application/databases-and-persistence/integrate-with-a-database-provider/integrate-mongodb-atlas-with-northflank.md

# Integrate MongoDB Atlas with Northflank

This guide explains how to connect your [MongoDB® Atlas](https://www.mongodb.com/atlas) cluster to your applications on Northflank. We will first take you through setting up an Atlas cluster, deploying an application on Northflank, and connecting a database in your cluster with your application.

We will then look at egress gateways and configuring your Atlas cluster and Northflank project to reduce latency and bandwidth costs.

To get started you will need a Northflank account and a MongoDB Atlas account. [Create your Northflank account here](https://app.northflank.com/signup) and follow the onboarding steps, and create your [MongoDB Atlas account here](https://www.mongodb.com/cloud/atlas/register).

## Create a MongoDB Atlas cluster

For this example we will deploy a free cluster on Google Cloud, in the central US region, the same as the Northflank project we will create in this guide.

1. Log in to your Atlas account, and select the organisation and project to deploy your cluster in

2. Navigate to the Database page under the Deployment section and click Build a database

3. Configure your Atlas cluster:
  
  
  1. select the `M0 (free)` plan
  
  2. Choose `Google Cloud` as the provider
  
  3. Select `Iowa (us-central1)` for the region
  
  4. Name your cluster `Northflank-Atlas`

4. Click Create

You should be taken automatically to the security quickstart page for your new Atlas cluster. You can read more about configuring your Atlas cluster for low latency, and reduced bandwidth costs later in this guide.

## Configure MongoDB Atlas authentication

You can authenticate to your cluster using a username and password combination, or via certificate. To configure authentication using the quickstart page for security:

1. Select username and password, enter a username (`northflank`, for example), and generate a password

2. Save the password in a secure place and click Create user

3. Add `0.0.0.0/0` to your IP Access List

4. Click finish and close, and return to the cluster overview

This will allow Northflank workloads to connect to your Atlas cluster. You can read more about configuring a secure egress gateway on Northflank later in this guide.

## Find your MongoDB Atlas connection string

We will now find and save your connection string, which you will use to connect your application to your Atlas database.

1. From the overview click the Connect button for the database we just deployed

2. Select Drivers from the 'connect to your application' section

3. Skip the configuration steps and find and copy your connection string. It should look like this:
  `mongodb+srv://<username>:<password>@<host>/?retryWrites=true&w=majority`

4. Replace `<password>` with your password for the user that you created earlier, and save the connection string in a secure place

We are now ready to connect our Atlas database with an application running on Northflank.

## Deploy an application on Northflank

Follow the steps below to create a project and deploy your application:

1. Open the Create new menu and select Project

2. Give your project a name (for example, ‘Atlas integration’) and select `US - Central` as the region

3. Click Create project, then select Create secret and give it a name

4. Add the following variables to your secret group:

```ENV
PAYLOAD_SECRET=${fn.randomSecret(32)}
MONGODB_URI=<your-Atlas-connection-string>
```

1. Open the Create new menu and select Combined service

2. Give it a name, enter `https://github.com/northflank-guides/deploy-payload-on-northflank-with-atlas` for the repository and select Dockerfile for the build type

3. Create your service, and it will start a new build and deploy it when ready. It may take a moment for the Payload application to become ready after the container has deployed and is running.

4. Open the domain displayed in the header of your service to view the Payload application and add your first user

You can now return to your database on Atlas to Browse collections, where you will see your new user in the `users` collection.

## Use an egress gateway to secure your network traffic

In our example we allowed any IP address to connect to our Atlas cluster, by adding `0.0.0.0/0` to the IP Access List. This makes your databases less secure, and should only be used for demonstration and testing purposes.

To use MongoDB Atlas with Northflank in production you should restrict your Atlas cluster to specific IP addresses. To allow your Northflank projects to communicate with your Atlas cluster, you can request to route traffic via an egress gateway, and provide a static IP address for your Atlas cluster’s IP Access List.

[Contact Northflank for more information](mailto:support@northflank.com).

## Provision clusters to reduce latency and bandwidth costs

You can provision your Atlas clusters and Northflank projects on the same cloud provider and region to reduce latency between your applications and databases, and reduce your bandwidth costs.

If you’re deploying on Northflank’s managed cloud, you can choose Google Cloud when configuring your Atlas cluster, and choose the corresponding region:

| Northflank managed cloud region | Atlas Google Cloud region |
| --- | --- |
| Europe West | London (europe-west2) |
| Europe West Netherlands | Netherlands (europe-west4) |
| US East | South Carolina (us-east1) |
| US Central | Iowa (us-central1) |
| US West | Oregon (us-west1) |
| Asia Southeast | Singapore (asia-southeast1) |

You can also deploy Northflank clusters in your own cloud provider account, and use any provider and region available to you on MongoDB Atlas.

## Next steps

- [How-to guides: Find out how to do anything on Northflank, from building from Git to deploying on your custom domain.](/v1/application/overview)
- [Run production workloads: Learn how to set up your DevOps workflow and confidently manage your production workloads on Northflank.](/v1/application/production-workloads/get-production-ready-on-northflank)
