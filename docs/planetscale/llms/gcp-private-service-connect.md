# Source: https://planetscale.com/docs/postgres/connecting/private-connections/gcp-private-service-connect.md

# Connect privately with GCP Private Service Connect

> When you use GCP Private Service Connect, your network traffic between your VPC and PlanetScale stays within the Google Cloud network, without traversing the public internet.

[GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) is a highly available, scalable technology that enables you to privately connect your VPC to supported GCP services, endpoint services, and partner services.

### When to use GCP Private Service Connect

By default, PlanetScale Postgres databases use secure connections over the public internet with industry-standard TLS encryption. This approach is secure and meets the needs of most customers. However, you may want to consider GCP Private Service Connect if:

* **Compliance requirements**: Your organization has regulatory or compliance mandates that require database connections to avoid the public internet entirely
* **Enhanced security posture**: You want an additional layer of network isolation for sensitive data workloads
* **Network architecture**: Your existing GCP infrastructure is designed around private connectivity patterns
* **Reduced network latency**: GCP Private Service Connect can help reduce latency by keeping traffic within Google's network backbone

GCP Private Service Connect provides these security and compliance benefits by ensuring your database traffic never leaves the Google Cloud network.

<Note>
  Normal PlanetScale Postgres connectivity (as described in our [standard connection documentation](/docs/postgres/connecting)) uses secure TLS encryption over the public internet and is appropriate for most use cases. GCP Private Service Connect is primarily beneficial for compliance and enhanced security requirements.
</Note>

### Private Service Connect pricing

PlanetScale does not charge any additional fees for GCP Private Service Connect connectivity. However, Google Cloud charges standard Private Service Connect pricing for endpoints, which includes:

* **Private Service Connect endpoint charges**: Based on your endpoint configuration and usage
* **Network egress charges**: Standard GCP egress pricing may apply for data transfer

For current pricing in your region, see the [GCP Private Service Connect pricing page](https://cloud.google.com/vpc/pricing#private-service-connect).

## Prerequisites

* A PlanetScale Postgres database in a GCP region
* A GCP VPC in the same region where you want to establish the private connection
* Appropriate GCP IAM permissions to create Private Service Connect endpoints
* **Required APIs enabled**: Cloud DNS API and Service Directory API must be enabled in your project for automatic DNS zone creation (see [GCP documentation](https://cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer))

## Establishing a Private Service Connect endpoint

1. **Retrieve the Private Service Name**:

   1. From the PlanetScale organization dashboard, select the desired database
   2. Navigate to **Settings** from the menu on the left
   3. Select **Roles**
   4. Click on a role with permissions to the relevant `Branch`
   5. Copy the `Private Host` and `Private Service Name` from the role details

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e9f6dc8d5c8e1200605ecbc591654ada" alt="Private connection strings" data-og-width="1814" width="1814" data-og-height="356" height="356" data-path="docs/postgres/connecting/private-connections/psc-private-host-names.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=2e2c447eb05997378a3db533db3f619d 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c1f03cd844054a61b07bde1a1ecc2ad4 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=605af81afa51b1b288d2d719893ef59d 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dcb6414f97afbcf4e57a6f1dd86d5b6c 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=c0409e80527977ce87ca6ddb08dd0e2c 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-private-host-names.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=881652af414bec7ed4d9fbd82e1ad014 2500w" />

   Save these two attributes for your records and the rest of the configuration.

   <Note>
     Both the `Private Host` and `Private Service Name` values are the same for all roles for a given PlanetScale database `Branch`. Once enabled, any role can use the Private Service Connect endpoint. You do not need to configure this per PlanetScale `Role`.
   </Note>

2. **Enable required APIs**: Ensure Cloud DNS and Service Directory APIs are enabled for automatic DNS zone creation:

   Via GCP Console:

   1. Confirm you are in the proper `<gcp-region>` from the project selector
   2. From the top search bar, search for `CloudDNS` and select it from the results
   3. Click to enable the API
   4. From the top search bar, search for `Service Directory` and select it from the results
   5. Click to enable the API

3. **Navigate to Private Service Connect**: In the GCP Console:

   1. Confirm you are in the proper `<gcp-region>` from the project selector
   2. From the top search bar, search for `Private Service Connect` and select it from the results

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=04c0d189aa91668dbd413f4a9e7154fb" alt="Private Service Connect console" data-og-width="1416" width="1416" data-og-height="648" height="648" data-path="docs/postgres/connecting/private-connections/psc-search.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=85b6de8ace83743eabbdaa3c6c1c5a13 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=48827fe097d04a2276067ca0c1bd05c9 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=9228523aeafb7184172b6611e7f9209e 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=95389e0daca62f787e5a955725154402 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=75c0011d3c2650462ffd88032162fafe 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-search.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=dbc51f7a82468445e695796bf84e3c43 2500w" />

4. **Create a new endpoint**: Click "**+ Connect endpoint**".

5. **Configure endpoint details**:

   * **Target**: Select "Published Service"
   * **Target Service**: Enter the `Private Service Name` recorded from the PlanetScale Dashboard
   * **Endpoint name**: Choose a descriptive name (e.g., "planetscale-main" uses the `Branch` name in it. This name will be part of the connection host string you use going forward)
   * **Network**: Select your VPC network
   * **Subnet**: Choose a subnet that your application servers can access
   * **Create an IP Address**: Reserve a static IP address for the endpoint
   * **Enable Global Access**: Recommended - allows applications in other regions to reach the endpoint
   * **Create a namespace**: Recommended - Set a namespace in `Service Directory` to enable creation of an entry for this endpoint

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8a0e0a7a61ae82a5a409cf5846919bed" alt="Endpoint configuration details" data-og-width="1180" width="1180" data-og-height="1914" height="1914" data-path="docs/postgres/connecting/private-connections/psc-endpoint-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=60a26f6bb0e3edcf94a0342c370a7de7 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=1c3ae72db3a3ad08e6e101497c271686 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e4447d283c8007df9565460c8af1936d 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=b986474bcb1d3b9cedf552005ee3a9c5 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d0b12b08d7e2ef87daf0944d3bcdebd7 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-endpoint-configuration.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=d860a6fc91fc35697d53bd3c2b597e8f 2500w" />

6. **Create the endpoint**: Click "**Add Endpoint**" and wait for the endpoint status to show "Accepted" (this may take several minutes).

## Verifying your Private Service Connect endpoint connectivity

1. **Confirm endpoint status**: In the GCP Console, verify that your endpoint's status shows "Accepted".

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=599f0bde1b2d4e4b4ca0b215f361f801" alt="Active Endpoint" data-og-width="2164" width="2164" data-og-height="1454" height="1454" data-path="docs/postgres/connecting/private-connections/psc-active-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=70ab88598763c06a473739d249af2248 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=57919ed18bd637b22c1252e0833aaa96 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=bb3813bb4de27b0e9ab9e0e6d2d7ef02 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=8d8ae727d98c8ce7bd4e7485a2ecd0f7 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=7372e67d613b79d8bbd3e68fd7210311 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-active-endpoint.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=31bf63e6ac9a3f47d6f6c82a65fcae13 2500w" />

2. **Test DNS resolution**: If Cloud DNS is enabled, GCP automatically creates a private Cloud DNS zone for your endpoint. The DNS zone will match the `Private Host` (recorded earlier from the PlanetScale Dashboard).

   You can verify by navigating to the `Cloud DNS` page from the left Nav:

   <img src="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=82e2f0554056e66348c166ca1933d83c" alt="Cloud DNS resource" data-og-width="2326" width="2326" data-og-height="874" height="874" data-path="docs/postgres/connecting/private-connections/psc-clouddns-record.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=280&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=0914ba0c1f43ecb33d334742f256b3d8 280w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=560&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=ab1937c061a9c6451550db4eef5ffecc 560w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=840&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=e23e24f44d3bfbb3b896635e58892691 840w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=1100&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=39c3277a0f79f40efd0caca4a1ae4a22 1100w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=1650&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=4f5e4e1c3e73b51c900435f2fead02a5 1650w, https://mintcdn.com/planetscale-cad1a68a/wcvpdoJo_ezgDX4B/docs/postgres/connecting/private-connections/psc-clouddns-record.png?w=2500&fit=max&auto=format&n=wcvpdoJo_ezgDX4B&q=85&s=39262d84f6eb2ba1ad53181f4d065978 2500w" />

   To address the actual host endpoint you will use, you need to combine the `Endpoint name` you defined with the DNS zone name here (same as the `Private Host` recorded earlier).

   From this example:

   * `Endpoint name` = planetscale-main
   * `Private Host` = gcp-us-central1-1.private-pg.psdb.cloud

   Which results in:

   ```
   planetscale-main.gcp-us-central1-1.private-pg.psdb.cloud
   ```

   To confirm DNS is working properly in your VPC, run a DNS lookup from a VM instance in your configured VPC:

   ```bash  theme={null}
   dig +short planetscale-main.gcp-us-central1-1.private-pg.psdb.cloud
   10.128.0.17
   ```

3. **Test your PostgreSQL connection**:

   Once you have confirmed DNS resolution, test the private endpoint:

   ```bash  theme={null}
   psql 'host=planetscale-main.gcp-us-central1-1.private-pg.psdb.cloud port=5432 user=postgres.XYZ234 password=pscale_pw_REDACTED dbname=postgres sslmode=require'
   ```

## Update your connection strings

Once your Private Service Connect endpoint is established and verified, update your application's connection strings to use the private endpoint address. Note that you need both the `Endpoint name` you configured and the `Private Host` from the PlanetScale dashboard to form the full hostname for your application to use.

* **Original**: `gcp-us-central1-1.pg.psdb.cloud`
* **Private**: `planetscale-main.gcp-us-central1-1.private-pg.psdb.cloud`

Replace the hostname in your connection strings while keeping all other parameters (user, password, database name, etc.) the same.

## VPC considerations

Your VPC configuration should allow:

* **Private Google Access**: Enable this if your compute instances don't have external IP addresses
* **Subnet routing**: Ensure proper routing between your application subnets and the PSC endpoint subnet
* **Network tags**: Use network tags to organize and control access to your PSC endpoint

## Troubleshooting

If you're experiencing connectivity issues:

1. **Verify endpoint status**: Ensure your Private Service Connect endpoint shows "Accepted" status
2. **Test DNS resolution**: Verify DNS is resolving to the private IP address in your VPC
3. **Check VPC routing**: Ensure there are no route conflicts or missing routes
4. **Verify network connectivity**: Use tools like `telnet` or `nc` to test port connectivity
5. **Contact support**: If issues persist, contact PlanetScale support with your endpoint configuration details

## Next steps

* [Learn about PostgreSQL roles and permissions](/docs/postgres/connecting/roles)
* [Configure connection pooling with PgBouncer](/docs/postgres/connecting/pgbouncer)
* [Monitor your connections and performance](/docs/postgres/monitoring/query-insights)

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt