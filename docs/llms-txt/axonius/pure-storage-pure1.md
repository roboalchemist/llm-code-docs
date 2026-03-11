# Source: https://docs.axonius.com/docs/pure-storage-pure1.md

# Pure Storage Pure1

Pure Storage Pure1 is a cloud-based storage management solution that provides self-driving storage, data-storage management, and monitoring.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Pure Storage Pure1 Domain** *(required)* - The hostname or IP address of the Pure Storage Pure1 server.

2. **Application ID** and **Private Key** *(required)* - Specify the details required to fetch asset details using Pure1 Public REST API. For more details, see [How to Create Key Pair and Register It with Pure1](#how-to-create-key-pair-and-register-it-with-pure1).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(858\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch volumes and volume snapshots** - Select this option to enrich each device with its volumes and volume snapshots.
2. **Fetch tags** - Select this option to fetch tags (arrays).
3. **Fetch targets** - Select this option to fetch targets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Pure1 Public REST API](https://static.pure1.purestorage.com/api-swagger/index.html).

## How to Create Key Pair and Register It with Pure1

To allow Axonius use the [Pure1 Public REST API](https://static.pure1.purestorage.com/api-swagger/index.html), you must create a key pair and then registering it with Pure1.

### 1. Create a Key Pair

Creating a key pair is a one-time operation, or a per-user operation.

<Callout icon="📘" theme="info">
  NOTE

  There are a variety ways of doing this, but the simplest option is to just use the OpenSSL tool native in Linux distributions.
</Callout>

1. Create a private key without password.
2. Take the created private key and copy it to a text editor.
3. Edit the copied private key to a single string, by replacing any line break with "/n".
4. When configuring the adapter connection, copy the edited private key to the [**Private Key**](#parameters) field.
5. Use the created private key to create a public key without password.

### 2. Registering the Key Pair with Pure1

You need to actually tell Pure1 that this key is valid for REST access. You must be an administrator in your Pure1 organization to be able to do this step.

1. Login to Pure1.
2. Under the **Administration** section, click **API registration**. Then **Register Application**.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(827\).png)

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(828\).png)
3. Enter in a friendly name for the application or user (for example, Axonius). Then, copy and paste the whole public key. Including the dashes and the BEGIN/END text (similar to what is highlighted above). Paste it into the text box in Pure1:
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(830\).png)
4. Click **Upload** when done.
   When configuring the adapter connection, you will need to specify the generated application ID in the [**Application ID**](#parameters) field.