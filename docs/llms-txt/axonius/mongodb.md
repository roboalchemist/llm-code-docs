# Source: https://docs.axonius.com/docs/mongodb.md

# MongoDB

MongoDB is a document-oriented NoSQL database.

### Asset Types Fetched

* Devices, Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **MongoDB Server** - The hostname or IP address of the MongoDB server.

<Callout icon="📘" theme="info">
  Note

  If configuring the adapter to communicate to a MongoDB Atlas cluster, you must configure `mongo+srv://` as a prefix in the MongoDB Server name and TLS must be enabled.
</Callout>

2. **Port** - The port to be used in the connection.
3. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.
4. **Database** - The name of the MongoDB database.

<Image alt="MongoDB(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MongoDB(1).png" />

### Optional Parameters

1. **Use TLS** - Toggle this option to enable Transport Layer Security (TLS).
   * **CA Certificate** *(optional)* - The CA certificate MongoDB deployment presents for the application to establish its identity. Click **Upload File** to upload a CA certificate. For more information, see [Specify a CA File](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/tls/#specify-a-ca-file).
   * **Certificate Key** *(optional)* - The client’s certificate and private key. Your client certificate and private key must be in the same `.pem` file. If they are stored in different files, you must concatenate them. Click **Upload File** to upload a certificate key. For more information, see [Present a Client Certificate](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/tls/#present-a-client-certificate).
   * **Certificate Key Password** *(optional)* - The password to the client’s certificate and private key file.
2. **Use LDAP Authorization** - Enable this option to use LDAP authorization.
3. **Devices Collection**  - The name of the devices collection in the MongoDB database.
4. **Users Collection**  - The name of the users collection in the MongoDB database.

<Callout icon="📘" theme="info">
  Note

  You have to enter a name for either **Devices Collection** or  **Users Collection**.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Sensitive Fields to exclude** *(default: credentials)* - Enter a list of sensitive fields to exclude from the raw data.
2. **Custom Parsing** - See [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>