# Source: https://firebase.google.com/docs/app-hosting/vpc-network.md.txt

<br />

YourFirebase App Hostingbackend can connect to a[Virtual Private Cloud (VPC)](https://cloud.google.com/vpc/docs)network. This allows yourFirebase App Hostingbackend to access backend services not accessible using public IP addresses, such as Cloud SQL, Spanner, Cloud Memorystore,Compute Engine, or Kubernetes internal microservices.

VPC access is only available at runtime (from yourCloud Runcontainer), not at build time (Cloud Build).

## Choose how to connect to a VPC network

- [Direct VPC Egress](https://cloud.google.com/run/docs/configuring/vpc-direct-vpc): Simpler, faster, and less expensive. Uses one IP address per container. Recommended for most use cases.
- [Serverless Connectors](https://cloud.google.com/vpc/docs/serverless-vpc-access): Pools IP addresses for larger applications. Requires payment for the underlying VM. See "Serverless VPC Access" in the[VPC pricing page](https://cloud.google.com/vpc/network-pricing)for pricing details.

## Configure in`apphosting.yaml`

Use the`vpcAccess`mapping in your`apphosting.yaml`file to configure access. Use either a fully qualified network/connector name or an ID. Using IDs allows for portability between staging and production environments with different connectors/networks.

### Direct VPC Egress Configuration (`apphosting.yaml`):

    runConfig:
      vpcAccess:
        egress: PRIVATE_RANGES_ONLY # Default value
        networkInterfaces:
          # Specify at least one of network and/or subnetwork
          - network: my-network-id
            subnetwork: my-subnetwork-id

### Serverless Connector Configuration (`apphosting.yaml`):

    runConfig:
      vpcAccess:
        egress: ALL_TRAFFIC
        connector: connector-id

## Example: connect to Memorystore for Redis from a Next.js app

Caching systems like Redis or Memcached are commonly used to build a fast data caching layer for an app. This example shows you how to set up[Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)in the sameGoogle Cloudproject as yourFirebase App Hostingbackend and connect to it using[Direct VPC egress](https://cloud.google.com/run/docs/configuring/vpc-direct-vpc).

### Step 0: Create a Memorystore for Redis instance

| **Note:** you may also be prompted to create a[service connection policy](https://cloud.google.com/vpc/docs/about-service-connection-policies)as part of this setup.

1. Go to the[*Memorystore for Redis*page](https://console.cloud.google.com/memorystore/redis/instances)in theGoogle Cloudconsole.
   - Make sure the same project you're using forFirebase App Hostingis selected.
   - If you can't access this page, make sure billing is enabled for your project and that you've enabled the[Memorystore API](https://console.cloud.google.com/apis/dashboard).
2. Select**Create Instance**.
3. Configure the new instance with your preferred settings. Here are some example values you can use:
   - Enter`my-redis-cache`under**Instance ID**.
   - Enter`Redis cache`under**Display name**.
   - Choose**Basic**under the tier selector. Basic tier designates a standalone Redis node, as opposed to standard tier, which uses a replica node to backup your data.
   - Choose yourApp Hostingbackend's region from the**Region** selector.**Be sure to set this value to match the region of your backend.**
   - Choose**any**from the zone selector.
   - Enter`5`under**Capacity**. This sets your instance capacity to 5 GB.
   - Select`5.0`under**Version**(recommended).
   - Choose**default** from the**Authorized network**selector.

### Step 1: Update`apphosting.yaml`with your VPC network ID

1. Visit the[VPC networks page](https://firebase.google.com/docs/app-hosting/console.cloud.google.com/networking/networks/list)in theGoogle Cloudconsole.
2. Find the VPC network ID for your Memorystore for Redis instance (it will often be`default`).
3. Set direct VPC egress configuration in`apphosting.yaml`using the VPC network ID:

       runConfig:
         vpcAccess:
           egress: PRIVATE_RANGES_ONLY # Default value
         networkInterfaces:
           - network: my-network-id

### Step 2: Add environment variables that direct your app to Redis

1. Find connection information (host and port) in the "Connections" tab of your Memorystore for Redis instance in theGoogle Cloudconsole.
2. Connect to Redis with`REDISPORT`and`REDISHOST`environment variables. Set these in`apphosting.yaml`using the host and port values from theGoogle Cloudconsole:

       env:
         # Sample only. Use actual values provided by Memorystore
         - variable: REDISPORT
           value: 6379
         - variable: REDISHOST
           value: 10.127.16.3

### Step 3: Use redis from your app

1. Install the[redis](https://www.npmjs.com/package/redis)npm package:

   `npm install redis@latest`
2. Access your redis cache from your code. Use the environment variables configured in the previous step. For example, here's how you might read from a cache in a Next.js route handler:

   - `src/lib/redis.js`

         import { createClient } from "redis";

         // Set these environment variables in apphosting.yaml
         const REDISHOST = process.env.REDISHOST;
         const REDISPORT = process.env.REDISPORT;

         let redisClient;

         export async function getClient(req, res) {
           // Only connect if a connection isn't already available
           if (!redisClient) {
             redisClient = await createClient(REDISPORT, REDISHOST)
               .on("error", (err) => console.error("Redis Client Error", err))
               .connect();
           }

           return redisClient;
         }

   - `src/app/counter/route.js`

         import { getClient } from "@/lib/redis.js";

         export async function GET(request) {
           const redisClient = await getClient();
           const count = await redisClient.get("counter");

           return Response.json({ count });
         }

         export async function POST(request) {
           const redisClient = await getClient();
           const count = await redisClient.incr("counter");

           return Response.json({ count });
         }

### Step 4 (optional): Configure your app for local development

TheFirebase App Hostingemulator can override values using`apphosting.emulator.yaml`. Here, you can change the value of`REDISHOST`to point to the localhost so that you can develop locally using a local installation of Redis.

1. [Install Redis on your local machine](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/)
2. Create or edit`apphosting.emulators.yaml`to reference your local instance:

       env:
         - variable: REDISHOST
           value: 127.0.0.1