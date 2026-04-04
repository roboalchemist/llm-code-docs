# Source: https://clickhouse.ferndocs.com/click-pipes/integrations/clickpipes/postgres/source/google-cloudsql.md

---
sidebar_label: Google Cloud SQL
description: Set up Google Cloud SQL Postgres instance as a source for ClickPipes
slug: /integrations/clickpipes/postgres/source/google-cloudsql
title: Google Cloud SQL Postgres source setup guide
doc_type: guide
keywords:
  - google cloud sql
  - postgres
  - clickpipes
  - logical decoding
  - firewall
---

<Note>

If you use one of the supported providers (in the sidebar), please refer to the specific guide for that provider.

</Note>

## Supported Postgres versions [#supported-postgres-versions]

Anything on or after Postgres 12

## Enable logical replication [#enable-logical-replication]

**You don't need** to follow the below steps if the settings `cloudsql. logical_decoding` is on and `wal_sender_timeout` is 0. These settings should mostly be pre-configured if you are migrating from another data replication tool.

1. Click on **Edit** button on the Overview page.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/9447643f98fae1feea1f9b47d6c5b40404962664ddbd84dcbd5a0c41f6080221/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/edit.png" alt="Edit Button in Cloud SQL Postgres"/>

2. Go to Flags and change `cloudsql.logical_decoding` to on and `wal_sender_timeout` to 0. These changes will need restarting your Postgres server.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/172bdbfd247682e94c580e89698f265cbec18565a7995fe19236d0554987e95b/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/cloudsql_logical_decoding1.png" alt="Change cloudsql.logical_decoding to on"/>
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d7ae0144aa6798ab69d5d4f7b620e939e11141ac0952fc9d1ff9a285b7fc2f34/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/cloudsql_logical_decoding2.png" alt="Changed cloudsql.logical_decoding and wal_sender_timeout"/>
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/29df929e57bee1ca7eca319f05da55d18e1ba46fc140e975a772ccf44f11215d/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/cloudsql_logical_decoding3.png" alt="Restart Server"/>

## Creating ClickPipes user and granting permissions [#creating-clickpipes-user-and-granting-permissions]

Connect to your Cloud SQL Postgres through the admin user and run the below commands:

1. Create a Postgres user for exclusively ClickPipes.

   ```sql
   CREATE USER clickpipes_user PASSWORD 'some-password';
   ```

2. Provide read-only access to the schema from which you are replicating tables to the `clickpipes_user`. Below example shows setting up permissions for the `public` schema. If you want to grant access to multiple schemas, you can run these three commands for each schema.

   ```sql
   GRANT USAGE ON SCHEMA "public" TO clickpipes_user;
   GRANT SELECT ON ALL TABLES IN SCHEMA "public" TO clickpipes_user;
   ALTER DEFAULT PRIVILEGES IN SCHEMA "public" GRANT SELECT ON TABLES TO clickpipes_user;
   ```

3. Grant replication access to this user:

   ```sql
   ALTER ROLE clickpipes_user REPLICATION;
   ```

4. Create publication that you'll be using for creating the MIRROR (replication) in future.

   ```sql
   CREATE PUBLICATION clickpipes_publication FOR ALL TABLES;
   ```

[//]: # (TODO Add SSH Tunneling)

## Add ClickPipes IPs to Firewall [#add-clickpipes-ips-to-firewall]

Please follow the below steps to add ClickPipes IPs to your network.

<Note>

If your are using SSH Tunneling, then you need to add the [ClickPipes IPs](../../index.md#list-of-static-ips) to the firewall rules of the Jump Server/Bastion.

</Note>

1. Go to **Connections** section

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/93c532e740d092cb6220ce0b06ad82b7c730aaa1a2ba6e946d0084d2348449a8/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/connections.png" alt="Connections Section in Cloud SQL"/>

2. Go to the Networking subsection

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2420e0f9397464f70d0c3e3a1dbaf9976ab5c1acd151db6039a719f90230005c/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/connections_networking.png" alt="Networking Subsection in Cloud SQL"/>

3. Add the [public IPs of ClickPipes](../../index.md#list-of-static-ips)

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7e37a30f7f3f08d85f71ef37d09e6778bf4c933b2fa56bbb00da9f039932fe92/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/firewall1.png" alt="Add ClickPipes Networks to Firewall"/>
<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0b5a076e51b9e2e9b01fd9d8369c976808d680bcdf5ea3f4005d639bfbed6d04/images/integrations/data-ingestion/clickpipes/postgres/source/google-cloudsql/firewall2.png" alt="ClickPipes Networks Added to Firewall"/>

## What's next? [#whats-next]

You can now [create your ClickPipe](/click-pipes/integrations/clickpipes/postgres) and start ingesting data from your Postgres instance into ClickHouse Cloud.
Make sure to note down the connection details you used while setting up your Postgres instance as you will need them during the ClickPipe creation process.
