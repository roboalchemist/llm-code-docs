# Source: https://developers.webflow.com/browser/data-exports/destinations/aurora-postgres.mdx

***

title: Aurora PostgreSQL
slug: data-exports/destinations/aurora-postgres
description: Configure Aurora PostgreSQL as a destination for Data Exports
--------------------------------------------------------------------------

This guide walks you through configuring Aurora PostgreSQL / Amazon RDS as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your Postgres database is protected by security groups or other firewall settings, you will need to use the Webflow static IP address: `34.69.83.207/32` to complete Step 1.

## Configuration steps

<Steps>
  ### Allow access

  Allow write access to a portion of your RDS or Aurora PostgreSQL database.

  **Configure the security group**

  1. In your **Amazon RDS** > **Databases** list, click the PostgreSQL instance you want to send data to.

  2. In the database page, in the **Connectivity & security** tab, make note of the **Endpoint** and the **Port** number.

     ![Endpoint and port](https://storage.googleapis.com/prequel_docs/images/postgres-endpoint.png)

  3. In the **Security** section, ensure that the **Publicly accessible** setting is set to **Yes** to ensure that the destination is accessible from outside your VPC. Note that it is still only accessible through allowlisted IPs at this point.

     ![Publicly accessible](https://storage.googleapis.com/prequel_docs/images/postgres-publicly-accessible.png)

  4. Click one of the VPC security groups (usually `default`). Note: VPC groups are permissive (vs. restrictive) and for instances with multiple VPC security groups, only one needs to be configured with the new inbound rule.

     ![VPC security groups](https://storage.googleapis.com/prequel_docs/images/postgres-vpc-security-groups.png)

  5. In the **Security Groups** section, select the **Inbound rules** tab.

  6. Click **Edit inbound rules** and then click **Add rule**.

  7. Edit the newly created rule of type **Custom TCP** with the **Port range** noted in the first step (usually `5432`) and a `Custom` **Source** value that includes all of the service IPs. Note: you will need to add `/32` to the end of each IP (CIDR notation).

     <Note>
       **Network allowlisting**

       Webflow Static IP: `34.69.83.207/32`
     </Note>

  8. Click **Save rules**.

     ![Add rule](https://storage.googleapis.com/prequel_docs/images/postgres-add-rule.png)

  **Configure network ACLs (access control list)**

  For database instances in a VPC:

  1. In your RDS dashboard, select the PostgreSQL instance.

  2. Click the link to the instance's VPC.

  3. Click the **VPC ID**.

     ![VPC ID](https://storage.googleapis.com/prequel_docs/images/postgres-vpc-id.png)

  4. In the **Details** section, click on the link under **Main network ACL**.

     ![Network ACL ID](https://storage.googleapis.com/prequel_docs/images/postgres-main-network-acl-id.png)

  5. Click on the network ACL ID.

     ![Network ACL](https://storage.googleapis.com/prequel_docs/images/postgres-network-acl-id.png)

  **Edit the inbound rules**

  6. Click on the **Inbound rules** tab, and check if there is an existing rule with a Source of `0.0.0.0/0` set to `Allow`. (This is a default rule created by AWS. If this rule already exists, skip to **Edit outbound rules**.)

     ![Inbound rules](https://storage.googleapis.com/prequel_docs/images/postgres-inbound-rules.png)

  7. Create the inbound rule (if it doesn't exist). Click **Edit inbound rules** and either **Add new rule** or edit an existing rule to allow access to the **port number** of your database instance (usually `5432`) from the static IP. Click **Save changes**.

  **Edit the outbound rules**

  8. In the ACL menu, select the **Outbound rules** tab, and check if there is an existing rule with a Destination of `0.0.0.0/0` set to `Allow`. (This is a default rule created by AWS. If this rule already exists, skip to the next step.)

     ![Outbound rules](https://storage.googleapis.com/prequel_docs/images/postgres-outbound-rules.png)

  9. Create the outbound rule (if it doesn't exist). Click **Edit outbound rules** and edit the rules to allow outbound traffic to ports 1024-65535 for **Destination** `0.0.0.0/0`.

  ### Create writer user

  Create a database user to perform the writing of the source data.

  1. Open a connection to your Amazon RDS PostgreSQL database.

  2. Create a user for the data transfer by executing the following SQL command.

     ```sql
     CREATE USER <username> PASSWORD '<some-password>';
     ```

  3. Grant user `create` and `temporary` privileges on the database. `create` allows the service to create new schemas and `temporary` allows the service to create temporary tables.

     ```sql
     GRANT CREATE, TEMPORARY ON DATABASE <database> TO <username>;
     ```

     <Warning>
       **If the schema already exists**

       By default, the service creates a new schema based on the destination configuration (in the next step). If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema, using `GRANT ALL ON schema <schema> TO <username>;`
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, **port**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268548955411)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271245661971)
</Steps>
