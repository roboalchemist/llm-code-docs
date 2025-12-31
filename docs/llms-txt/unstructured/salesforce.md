# Source: https://docs.unstructured.io/ui/sources/salesforce.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/salesforce.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/salesforce.md

# Source: https://docs.unstructured.io/ui/sources/salesforce.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/salesforce.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/salesforce.md

# Source: https://docs.unstructured.io/ui/sources/salesforce.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/salesforce.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/salesforce.md

# Salesforce

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a source connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key, as follows:

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the source connector, add it along with a
  [destination connector](/api-reference/workflow/destinations/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create source connectors with the Unstructured user interface (UI).
  [Learn how](/ui/sources/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a source connector! Keep reading to learn how.
</Note>

Ingest your files into Unstructured from Salesforce.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5a-nh4t78V8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* A [Salesforce account](https://developer.salesforce.com/signup).

* Your Salesforce username. To get this username, do the following:

  1. Log in to your Salesforce account.
  2. In the top navigation bar, click the **Quick Settings** (gear) icon, and then click **Open Advanced Setup**.
  3. In the **Home** tab, under **Administration**, expand **Users**, and then click **Users**.
  4. Note the **User Name** value (*not* the **Name** value) for your user.

* The names of the Salesforce categories (objects) that you want to access, specified as a comma-separated list.
  Available categories include `Account`, `Campaign`, `Case`, `EmailMessage`, and `Lead`.

* A Salesforce connected app in your Salesforce account.

  If you do not already have a Salesforce connected app, to create one, start by creating or getting the certificate (`.crt`) and private key (`.pem`) files
  that you will associate with the connected app.

  If you do not have the certificate and private key files, you can use the `openssl` utility on your local machine to create your own
  private key and self-signed certificate, if your organization allows, by running the following commands, one command at a time:

  ```bash  theme={null}
  openssl genrsa -out MyPrivateKey.pem -traditional
  openssl req -new -key MyPrivateKey.pem -out MyCertificateSigningRequest.csr
  openssl x509 -req -in MyCertificateSigningRequest.csr -signkey MyPrivateKey.pem -out MyCertificate.crt -days 365
  ```

  Of course, you can change these preceding example filenames as needed. Be sure to store these generated files in a secure location.

  To create a Salesforce connected app, do the following:

  1. Log in to your Salesforce account.

  2. In the top navigation bar, click the **Quick Settings** (gear) icon, and then click **Open Advanced Setup**.

  3. In the **Home** tab, under **Platform Tools**, expand **Apps**, and then click **App Manager**.

  4. Click **New Connected App**.

  5. With **Create a Connected App** selected, click **Continue**.

  6. At a minimum, fill in the following, and then click **Save**:

     * **Connected App Name**
     * **API Name** (can be the same as **Connected App Name**, but do not use spaces or punctuation)
     * **Contact Email**
     * Under **API (Enable OAuth Settings)**, check **Enable OAuth Settings**.
     * For **Callback URL**, entering `https://localhost` is okay if you won't be using this connected app for other special authentication scenarios.
     * Check **Use digital signatures**, click **Choose File**, and browse to and select your certificate (`.crt`) file.
     * For **Selected OAuth Scopes**, move the following entries from the **Available OAuth Scopes** list to the **Selected OAuth Scopes** list:

       * **Manage user data via APIs (api)**
       * **Perform requests on your behalf at any time (refresh\_token, offline\_access)**
     * Uncheck **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**.
     * Leave **Require Secret for Web Server Flow** checked.
     * Leave **Require Secret for Refresh Token Flow** checked.
     * Check **Enable Authorization Code and Credentials Flow**.

  7. On the connected app's details page, click **Manage**, click **Edit Policies**, set the following under **OAuth Policies**, and then click **Save**:

     * Set **Permitted Users** to **All users may self-authorize**.
     * Set **IP Relaxation** to **Relax IP restrictions**.
     * Set **Refresh Token Policy** to **Refresh token is valid until revoked**.

* The OAuth consumer key (client ID) for the Salesforce connected app.

  To get the Salesforce connected app's consumer key, do the following:

  1. Log in to your Salesforce account.
  2. In the top navigation bar, click the **Quick Settings** (gear) icon, and then click **Open Advanced Setup**.
  3. In the **Home** tab, under **Platform Tools**, expand **Apps**, and then click **App Manager**.
  4. In the list of apps, click the arrow next to the target connected app, and click **View**.
  5. Click **Manage Consumer Details**.
  6. Complete the on-screen security verification.
  7. Note the **Consumer Key** value.

* You must use your Salesforce account to do a one-time approval of the Salesforce connected app by using its consumer key and callback URL. To do this, while you are logged in to your
  Salesforce account, browse to the following URL, replacing `<client-id>` with the consumer key value. This URL assumes that the callback URL
  is `https://localhost`:

  ```
  https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id=<client-id>&redirect_uri=https%3A%2F%2Flocalhost
  ```

* To ensure maximum compatibility across Unstructured service offerings, you should give the contents of the private key (`.pem`) file to Unstructured as
  a string that contains the contents of the file (*not* the private key file itself).\
  To print this string suitable for copying, you can run one of the following commands from your Terminal or Command Prompt.
  In this command, replace `<path-to-private-key-file>` with the path to the private key file.

  * For macOS or Linux:

    ```bash  theme={null}
    cat <path-to-private-key-file>
    ```

  * For Windows:

    ```text  theme={null}
    Get-Content <path-to-private-key-file>
    ```

To create a Salesforce source connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateSourceRequest
  from unstructured_client.models.shared import CreateSourceConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.sources.create_source(
          request=CreateSourceRequest(
              create_source_connector=CreateSourceConnector(
                  name="<name>",
                  type="salesforce",
                  config={
                      "username": "<user-name>",
                      "consumer_key": "<consumer-key>",
                      "private_key": "<private-key>",
                      "categories": [
                          "<category>",
                          "<category>"
                      ]
                  }
              )
          )
      )

      print(response.source_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/sources" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "salesforce",
      "config": {
          "username": "<user-name>",
          "consumer_key": "<consumer-key>",
          "private_key": "<private-key>",
          "categories": [
              "<category>",
              "<category>"
          ]
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<user-name>` - The Salesforce username that has access to the required Salesforce categories.
* `<consumer-key>` - The consumer key (client ID) for the Salesforce connected app.
* `<private-key>` - The contents of the private key (PEM) associated with the consumer key for the Salesforce connected app, expressed as a single-line string.
* For `categories`, set one or more `<category>` values (such as `Account`, `Campaign`, `Case`, `EmailMessage`, and `Lead`) to process only those categories.
  The default is to include these catagories if not otherwise specified: `Account`, `Campaign`, `Case`, `EmailMessage`, and `Lead`.
