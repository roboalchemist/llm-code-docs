# Source: https://docs.axonius.com/docs/backblaze.md

# Backblaze

Backblaze provides cloud backup and storage services.

### Asset Types Fetched

This adapter fetches the following types of assets:

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Object_Storage.svg) Object Storage

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

Standard Application Keys

### APIs

Axonius uses the [Blackblaze API Version 4](https://www.backblaze.com/apidocs/introduction-to-the-s3-compatible-api)

### Permissions

The following permissions are required:

* `listBuckets` and `listKeys` capabilities
* read-level access to the account or specific buckets

<br />

#### Supported From Version

Supported from Axonius version 6.0

## Setting up Backblaze to Work With Axonius

Standard Application Keys (Recommended)

1. Go to the **App Keys** page in the web console.
2. Click the **Add a New Application Key** button.
3. Configure the key:
   1. Key Name: Give it a name to remember what it's for.
   2. Allow Access to Bucket(s): Choose "All" or a specific bucket.
   3. Access Type: Choose Read Only.
4. Click **Create New Key**.

A blue box will appear displaying your keyID (Access Key) and applicationKey (Secret Key).The Secret Key (applicationKey) is only displayed at the moment of creation. If you close the window or refresh the page without saving it, you cannot retrieve it; you will have to delete that key and create a new one.

## Connecting the Adapter in Axonius

* Navigate to the Adapters page, search for Backblaze, and click on the adapter tile.
* Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address**  - The hostname or IP address of the Backblaze server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Access Key** *(required to fetch buckets)* -  This is a public identifier for your key. In S3-compatible integrations, the keyID serves as your Access Key.

3. **Secret Key** *(required to fetch buckets)* - This is the private key used for authentication. In S3-compatible integrations, the applicationKey serves as your Secret Key.

4. **User Name** and **Password**  *(required to fetch users)*- Backblaze credentials that have permissions to fetch assets.

5. **Region** - The AWS region where the S3 bucket is stored.

6. **Account ID** *(required)* - The account ID of the AWS account that hosts the S3 bucket.

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BackBlaze" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BackBlaze.png" />

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.