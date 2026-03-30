# Source: https://developers.webflow.com/browser/data-exports/destinations/mongodb.mdx

***

title: MongoDB
slug: data-exports/destinations/mongodb
description: Configure MongoDB as a destination for Data Exports
----------------------------------------------------------------

This guide walks you through configuring MongoDB as a destination for your Webflow Analyze and Optimize data export.

## Prerequisites

* If your MongoDB security posture requires IP allowlisting, you will need to use the Webflow static IP address: `34.69.83.207/32` during the following steps. It will be required in Step 3.

## Configuration steps

<Steps>
  ### Locate connection information

  **MongoDB CLI**

  1. Connect to your **MongoDB node** using the **MongoDB CLI** as an **admin**.

  2. Execute the following query:

     ```javascript
     db.adminCommand( { replSetGetStatus : 1 } ).members
     ```

  3. Make a note of the **host identifiers**.

  **MongoDB Atlas**

  1. Log in to your Atlas **dashboard**, click into the **Database** tab and click **Connect**.
  2. Under **Connect your application**, click into the **Drivers** option.
  3. In the following screen, make a note of the **host identifier** within your connection string. It can be found within the string that starts with `mongodb+srv` and the identifier is the URI after the `@`. E.g., `some-cluster.some-characters.mongodb.net`.

  ### Allow database access

  See CLI or Atlas instructions below depending on your MongoDB deployment type.

  **MongoDB CLI**

  1. Connect to your MongoDB node using the MongoDB CLI as an admin.
  2. Execute the following script (with a `username` and `password`) to create a new user. Replace `database` with the name of the database you'd like to load data into.

     ```javascript
     use admin

     db.createUser({
       user: "<username>",
       pwd: "<password>",
       roles: [ {role: "readWrite", db: "<database>"} ]
     })
     ```

  **MongoDB Atlas**

  1. Log in to your Atlas **dashboard**, click into the **Database Access** section of the **Security** options.
  2. Select **Add New Database User**. Choose the **Password** authentication method, and enter a `username` and `password` for the new user.
  3. In the **Database User Privileges** menu, select **Grant Specific User Privileges**. Within **Specific Privileges**, add the following: `readWrite@<database>` (with the name of the database you'd like to load data into). You can leave the **Collection** field blank (`*`).
  4. Click **Add User** to create the new user.

  ### Set up network access

  If your MongoDB instance enforces IP Access restrictions, you'll need to allow access to a static IP.

  <Note>
    **For self-hosted MongoDB deployments**

    IP allowlisting should be configured at the network or firewall level (e.g., using cloud provider security groups, `iptables`, or other firewall tools). Please consult your network administrator or your hosting provider's documentation.
  </Note>

  <Note>
    **Network allowlisting**

    Webflow Static IP: `34.69.83.207/32`
  </Note>

  **MongoDB Atlas CLI**

  If you manage your Atlas project with the Atlas CLI, execute the following command to add the static IP to your project's IP access list. You may need to append `/32` to the IP address to specify it in CIDR notation.

  ```bash
  atlas accessLists create "<static_ip_address>/32" --comment "data sharing service static IP"
  ```

  **MongoDB Atlas**

  1. Log in to your Atlas **dashboard**, click into the **Network Access** section of the **Security** options.
  2. Select **Add IP Address**. In **Access List Entry** enter the static IP of the service.
  3. Add an optional comment (e.g., "data sharing service") and click **Confirm**.

  ### Add your destination

  Use the **host name**, **port** (unless using Atlas, in which case is not needed), and **database name** (as noted in **Step 1**) and the **username** and **password** (as configured in **Step 2**) to complete the connection.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49269168200467)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271375895059)
</Steps>

## Permissions checklist

* Network:
  * Inbound rule allows TCP connections from the static egress IP
* MongoDB:
  * `readWrite` on the target database
  * `atlas accessLists create` (if using Atlas CLI for IP allowlisting)

## FAQ

<Accordion title="How is the MongoDB connection secured?">
  The connection uses a dedicated MongoDB user with `readWrite` role scoped to the target database. Network access can be restricted to the static egress IP.
</Accordion>
