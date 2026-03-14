# Source: https://docs.statsig.com/statsig-warehouse-native/connecting-your-warehouse/redshift.md

# Source: https://docs.statsig.com/integrations/data-imports/redshift.md

# Source: https://docs.statsig.com/data-warehouse-ingestion/redshift.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Redshift

## Overview

To set up connection with Redshift, Statsig needs the following

* Cluster Endpoint
* Admin User Name
* Admin User Password

<Note>
  SHA256 passwords are not currently supported, please utilize MD5 to avoid issues.
</Note>

You can find this information in your aws console within your specific cluster, as shown in the image below. (Open image in new tab for a bigger image)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/connecting-your-warehouse/redshift/187515405-17fa7d90-44e1-422f-87a7-cfde090637ed.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=8d69765b91c1dc9f0aeb6e5bb0306770" alt="AWS Redshift cluster details highlighting endpoint and admin user" width="1882" height="863" data-path="images/statsig-warehouse-native/connecting-your-warehouse/redshift/187515405-17fa7d90-44e1-422f-87a7-cfde090637ed.png" />
</Frame>

<b>Admin user name and password will be used by Statsig to create a user with restricted access to query from your data warehouse.</b>

## SSH Tunneling

For Redshift connections, we also allow users to create an SSH tunnel into their Redshift cluster for a more secure and private access to the database.
To enable access, Statsig requires:

* SSH Host
* SSH Port
* SSH User

Statsig will use this information to generate an SSH key. Please add this generated key to your `~/.ssh/authorized_keys` file on your SSH proxy machine to enable SSH tunneling.

### Custom User Privileges

To create a custom user with specific privileges instead of using an admin user, run the following code in your Redshift cluster with your admin user.
Replace `<USER>` and `<PASSWORD>` with your value, which you will copy over into our console.

```sql  theme={null}
# Create Statsig User
CREATE USER <USER> WITH PASSWORD <PASSWORD> SYSLOG ACCESS UNRESTRICTED;

# Give access to any Schemas that the Statsig User needs to read from
GRANT USAGE ON SCHEMA <SCHEMA> to <USER>;
GRANT SELECT ON ALL TABLES IN SCHEMA <SCHEMA> to <USER>;

# Create a Schema for Statsig User to write temporary data to
CREATE SCHEMA IF NOT EXISTS statsig_ingestion_staging;
GRANT ALL ON SCHEMA <SCHEMA> TO <USER>;
```

After running the script, input the `<USER>` and `<PASSWORD>` you created in our console, during Connection Set Up stage under the Advanced settings options.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/KzTmSDyskL8DnHsb/images/data-warehouse-ingestion/redshift/188943178-6b541962-62da-4529-b5af-ff59b20b7a8d.png?fit=max&auto=format&n=KzTmSDyskL8DnHsb&q=85&s=4e023d87d3192c51f836e6f5f8501e24" alt="Statsig Redshift connection setup form showing cluster endpoint and credentials fields" width="1713" height="691" data-path="images/data-warehouse-ingestion/redshift/188943178-6b541962-62da-4529-b5af-ff59b20b7a8d.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).