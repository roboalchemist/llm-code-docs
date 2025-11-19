# Source: https://www.aptible.com/docs/core-concepts/managed-databases/connecting-databases/database-endpoints.md

# Database Endpoints

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8165135c3b4463b1f6202053c9cae23e" alt="Image" data-og-width="1280" width="1280" data-og-height="720" height="720" data-path="images/5eac51b-database-endpoints-basic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=d81fb821c318e4d2da7bea968d49ed03 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a2f181ad5bb3fbc97f49513061161633 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=41abc094e86815ce19431a360fd3f51e 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=9f4a8d14e9cb65f3a478a0efefca8eff 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=5d026146ef483bb1f68b721c5721e9e8 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/5eac51b-database-endpoints-basic.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a02836b1d8047e1d043ff24c9c25560e 2500w" />

Database Endpoints let you expose a [Database](/core-concepts/managed-databases/overview) to the public internet. <Info> The underlying AWS hardware that backs Database Endpoints has an idle connection timeout of 60 minutes. If clients need the connection to remain open longer they can work around this by periodically sending data over the connection (i.e., a "heartbeat") in order to keep it active.</Info>

<Accordion title="Creating a Database Endpoint">
  A Database Endpoint can be created in the following ways:

  1. Within the Aptible Dashboard by navigating to the respective Environment >selecting the respective Database > selecting the "Endpoints" tab > selecting "Create Endpoint"
  2. Using the [`aptible endpoints:database:create`](/reference/aptible-cli/cli-commands/cli-endpoints-database-create) command
  3. Using the [Aptible Terraform Provider](/reference/terraform)
</Accordion>

# IP Filtering

<img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=a6aee938febfb06390a74de23bef066e" alt="Image" data-og-width="1280" width="1280" data-og-height="720" height="720" data-path="images/964e12a-database-endpoints-ip-filtering.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=beaaac8fe7b726387b0c79cb488b405d 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=732c8319492fc0389ed5bf106e96d02d 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=386e67be7cf8cec810248e35986ac6f1 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=84a19462e1d599d928f59ce971d574b3 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=e7d3ba3ec3fe1119d1dcf7a0687ab4ff 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/964e12a-database-endpoints-ip-filtering.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=37577b0469fc129dcc06afe217e0ab62 2500w" />

<Warning> To keep your data safe, it's highly recommended to enable IP filtering on Database Endpoints. If you do not enable filtering, your Database will be left open to the entire public internet, and it may be subject to potentially malicious traffic. </Warning>

Like [App Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), Database Endpoints support [IP Filtering](/core-concepts/apps/connecting-to-apps/app-endpoints/ip-filtering) to restrict connections to your Database to a set of pre-approved IP addresses.

<Accordion title="Configuring IP Filtering">
  IP Filtering can be configured in the following ways:

  * Via the Aptible Dashboard when creating an Endpoint
  * By navigating to the Aptible Dashboard > selecting the respective Database > selecting the "Endpoints" tab > selecting "Edit"
</Accordion>

# Certificate Validation

<Warning> Not all Database clients will validate a Database server certificate by default. </Warning>

To ensure that you connect to the Database you intend to, you should ensure that your client performs full verification of the server certificate. Doing so will prevent Man-in-the-middle attacks of various types, such as address hijacking or DNS poisoning. You should consult the documentation for your client library to understand how to ensure it is properly configured to validate the certificate chain and the hostname.

For MySQL and PostgreSQL, you will need to retrieve a CA certificate using the [`aptible environment:ca_cert`](/reference/aptible-cli/cli-commands/cli-environment-ca-cert) command in order to perform validation. After the Endpoint has been provisioned, the Database will also need to be restarted in order to update the Database's certificate to include the Endpoint's hostname. See the [Database Encryption in Transit](/core-concepts/managed-databases/managing-databases/database-encryption/database-encryption-in-transit) page for more details.

If the remote service is not able to validate your database certificate, please [contact support](https://aptible.zendesk.com/hc/en-us/requests/new) for assistance.

# Least Privileged Access

<Warning> The provided [Database Credential](/core-concepts/managed-databases/connecting-databases/database-credentials) has the full set of privileges needed to administer your Database, and we recommend that you *do not* provide this user/password to any external services. </Warning>

Create Database Users with the least privileges needed to use for integrations. For example, granting only "read" privileges to specific tables, such as those that do not contain your user's hashed passwords, is recommended when integrating a business intelligence reporting tool.

Please refer to database-specific documentation for guidance on user and permission management.
<Tip> Create a unique user for each external integration. Not only will this making auditing access easier, it will also allow you to rotate just the affected user's password in the unfortunate event of credentials being leaked by a third party</Tip>
