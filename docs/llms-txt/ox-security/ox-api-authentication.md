# Source: https://docs.ox.security/api-documentation/api-reference/ox-api-authentication.md

# OX API Authentication

**To create a new API key:**

1. From the left pane of **OX dashboard**, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.
3. In the **Create API Key** box set the following and select **CREATE**:

* **API Key Name:** Add a meaningful name that is easy to identify. It is good practice to include the key's intended purpose in the name.
* **API Key Type:** Select **API Integration**.
* **Expiration Date:** Until when you can use this key.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0817553963425ab3dd5e5b9216bb1e9f098b3761%2F3.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

1. Copy the **API Key Secret** to be used when connecting to APIs. Save the key in a safe location. This is the only time when you can see and copy the actual key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-32d85ffe2adf9834290baab3cb51f677829972d6%2F4.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the **Postman**, add the collection and then:

* Select request method **Post**.
* Use the following URL: <https://api.cloud.ox.security/api/apollo-gateway>
* In the **Headers > Authorization**, add the OX API Key.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b7c3ca22e3ddca2bf11d051a6297f592f86ca731%2F5b.png?alt=media" alt=""><figcaption></figcaption></figure>

1. In the **Body** section, add query and click **Send**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-745e32827e5186b18f8bb4c01b51420a3d59d97d%2F6a%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
