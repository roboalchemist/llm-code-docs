# Source: https://developers.webflow.com/browser/data-exports/destinations/aurora-mysql.mdx

***

title: Aurora MySQL
slug: data-exports/destinations/aurora-mysql
description: Configure Aurora MySQL as a destination for Data Exports
---------------------------------------------------------------------

This guide walks you through configuring Aurora MySQL as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your MySQL database is protected by security groups or other firewall settings, you will need to use the Webflow static IP address: `34.69.83.207/32` to complete Step 1.

## Configuration steps

<Steps>
  ### Allow access

  Allow write access to a portion of your Aurora MySQL database.

  **Configure the security group**

  1. In your **Amazon RDS** > **Databases** list, click the MySQL instance you want to send data to.

  2. In the database page, in the **Connectivity & security** tab, make note of the **Endpoint** and the **Port** number. Note that you may need to select the "**Writer instance**" in the DB identifier list to reveal the endpoint.

     ![MySQL endpoint port](https://storage.googleapis.com/prequel_docs/images/aws-mysql-endpoint-port.png)

  3. To ensure that the destination is accessible from outside your VPC, click "**Modify**" in the top right, and in the "**Connectivity**" section, within the **Additional configuration** dropdown, confirm the **Publicly accessible** setting is set to **Yes**. Note that it is still only accessible through allowlisted IPs at this point.

     ![MySQL publicly accessible](https://storage.googleapis.com/prequel_docs/images/aws-mysql-publicly-accessible.png)

  4. Returning to the database page, within the "**Writer instance**" details, click one of the VPC security groups (usually `default`). Note: VPC groups are permissive (vs. restrictive) and for instances with multiple VPC security groups, only one needs to be configured with the new inbound rule.

     ![VPC security group](https://storage.googleapis.com/prequel_docs/images/aws-mysql-default-security-group.png)

  5. In the **Security Groups** section, select the **Inbound rules** tab.

  6. Click **Edit inbound rules** and then click **Add rule**.

  7. Edit the newly created rule of type **Custom TCP** with the **Port range** noted in the first step (usually `3306`) and a `Custom` **Source** value that includes all of the service IPs. Note: you will need to add `/32` to the end of each IP (CIDR notation).

     <Note>
       **Network allowlisting**

       Webflow Static IP: `34.69.83.207/32`
     </Note>

  8. Click **Save rules**.

     ![Add rule](https://storage.googleapis.com/prequel_docs/images/postgres-add-rule.png)

  **Configure network ACLs (access control list)**

  For database instances in a VPC:

  1. In your RDS dashboard, select the MySQL instance.

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

  7. Create the inbound rule (if it doesn't exist). Click **Edit inbound rules** and either **Add new rule** or edit an existing rule to allow access to the **port number** of your database instance (usually `3306`) from the static IP. Click **Save changes**.

  **Edit the outbound rules**

  8. In the ACL menu, select the **Outbound rules** tab, and check if there is an existing rule with a Destination of `0.0.0.0/0` set to `Allow`. (This is a default rule created by AWS. If this rule already exists, skip to the next step.)

     ![Outbound rules](https://storage.googleapis.com/prequel_docs/images/postgres-outbound-rules.png)

  9. Create the outbound rule (if it doesn't exist). Click **Edit outbound rules** and edit the rules to allow outbound traffic to ports 1024-65535 for **Destination** `0.0.0.0/0`.

  ### Create writer user

  Create a database user to perform the writing of the source data.

  1. Open a connection to your Aurora MySQL database.

  2. Create a user for the data transfer by executing the following SQL command.

     ```sql
     CREATE USER <username>@'%' IDENTIFIED BY '<some-password>';
     ```

  3. Grant user required privileges on the database.

     ```sql
     GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, ALTER, CREATE TEMPORARY TABLES, CREATE VIEW ON *.* TO <username>@'%';
     ```

     <Warning>
       **If the schema/database already exists**

       By default, the service creates a new schema (*in MySQL, `schema` is synonymous with `database`*). If you prefer to create the schema yourself before connecting the destination, you must ensure that the writer user has the proper permissions on the schema, using `GRANT ALL PRIVILEGES ON <database_name>.* TO <username>@'%';`
     </Warning>

  ### Add your destination

  Use the following details to complete the connection setup: **host name**, **database name**, **port**, your chosen **schema name**, **username**, and **password**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268576434963)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271322817299)
</Steps>
