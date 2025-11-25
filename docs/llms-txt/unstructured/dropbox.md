# Source: https://docs.unstructured.io/ui/sources/dropbox.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/dropbox.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/dropbox.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/dropbox.md

# Dropbox

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

Ingest your files into Unstructured from Dropbox.

The requirements are as follows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vku5uYa-2N4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

1. A [Dropbox account](https://www.dropbox.com/try/teams).

2. A Dropbox app for your Dropbox account. To create a Dropbox app, do the following:

   a) Sign in to the [Dropbox Developers](https://www.dropbox.com/developers) portal with the same credentials as your Dropbox account.<br />
   b) Open your [App Console](https://www.dropbox.com/developers/apps).<br />
   c) Click **Create app**.<br />
   d) For **Choose an API**, select **Scoped access**.<br />
   e) For **Choose the type of access you need**, select **App folder**.<br />
   f) Enter a name for your app, and then click **Create app**.<br />
   g) On the app's **Permissions** tab, under **Files and folders**, check the boxes labelled **files.content.read** or **files.content.write** or both,
   depending on whether you want to read files, write files, or both. Then click **Submit**.<br />
   h) On the app's **Settings** tab, note the value of the **App folder name** field. This is the name of the app folder that Dropbox will create under the `Apps` top-level folder in your Dropbox
   account that the Dropbox app will use for access. If you change the value of **App folder name** field here, Dropbox will create an app folder with that name under the `Apps` top-level folder instead.<br />
   i) Under **OAuth 2**, next to **Generated access token**, click **Generate**. Copy the value of this access token. You should only click **Generate** after you have completed all of the preceding steps first.
   This is because the access token is scoped to the specific app folder and settings at the time the access token is generated. If you change the app folder name or any of the permissions later,
   you should regenerate the access token.<br />

   <Warning>
     Access tokens are valid for **only four hours** after they are created. After this four-hour period, you can no longer use the expired access token.
     Dropbox does not allow the creation of access tokens that are valid for more than four hours.

     To replace an expired access token, you must first generate a *refresh token* for the corresponding access token. To learn how to generate an access token and its corresponding refresh token,
     see [Replace an expired access token](#replace-an-expired-access-token), later in this article.

     If you do not already have the corresponding refresh token for an existing access token, or if you lose a refresh token after you generate it,
     you must generate a new access token and its corresponding refresh token.

     Instead of continualy replacing expired access tokens yourself, you can have Unstructured do it for you as needed; just supply Unstructured
     with the refresh token along with the Dropbox app's **App key** and **App secret** values.
     To learn how to supply these to Unstructured, look for mentions of "refresh token," "app key," and "app secret" in the connector settings later in this article.
   </Warning>

3. The app folder that your Dropbox app will use for access can be found in your Dropbox account under the `Apps` top-level folder. For example, if the value of the **App folder name**
   field above is `my-folder`, then the app folder that your Dropbox app will use for access can be found under `https://dropbox.com/home/Apps/my-folder`

   <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b5f9679d941b592ae0c62b0c661d6dac" alt="The my-folder app folder under the Apps top-level folder" data-og-width="254" width="254" data-og-height="279" height="279" data-path="img/connectors/dropbox-app-folder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=96784d3e87b315412327a8a051173244 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=b3dc98eb9b0d97d17a91cc7c328c1ac1 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=c3614d4e743e978e288681bc7876e91b 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=3f63e54518ac1abc767a8506ee7c4b59 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=27f3406da66a7be0ea1616c7ea7af434 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-folder.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=2f3a1cb5d47837746c005256c9cbd204 2500w" />

   <Warning>
     Your Dropbox app will *not* have access to upload or download files from the root of the app folder. Instead, you *must* create a subfolder inside of the app folder for your Dropbox
     app to upload or download files from. You will use the name of that subfolder when specifying your remote URL in the next step. For example, if your Dropbox app uses an app folder named `my-folder`
     for access within the `Apps` top-level folder, and you create a subfolder named `data` within the `my-folder` app folder, then the subfolder that your Dropbox app will upload and download files from
     can be found under `https://dropbox.com/home/Apps/my-folder/data`

       <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=63e6a2c4483435a32ff6ece5f9a3c297" alt="The data subfolder under the my-folder subfolder" data-og-width="253" width="253" data-og-height="316" height="316" data-path="img/connectors/dropbox-app-subfolder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9370c2c5af305d9c8d5608de9e64a18e 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5feb79063a38cbc91aa4abe8cf4d06da 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=78afbfbd91904675d2c1e9c4b671da7f 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e54cebed177b25e770559a8ba1855a4b 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=44e94fe9e106893a5013838610203a87 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5222a5db731a8ecf05b2fa7e4eee0540 2500w" />
   </Warning>

4. Note the remote URL to your subfolder inside of the app folder, which takes the format `dropbox://<subfolder-name>`. For example,
   if your Dropbox app uses an app folder named `my-folder` for access within the `Apps` top-level folder, and you create a subfolder named `data` within the `my-folder` app folder, then
   the remote URL is `dropbox://data`

   <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=63e6a2c4483435a32ff6ece5f9a3c297" alt="The data subfolder under the my-folder subfolder" data-og-width="253" width="253" data-og-height="316" height="316" data-path="img/connectors/dropbox-app-subfolder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9370c2c5af305d9c8d5608de9e64a18e 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5feb79063a38cbc91aa4abe8cf4d06da 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=78afbfbd91904675d2c1e9c4b671da7f 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=e54cebed177b25e770559a8ba1855a4b 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=44e94fe9e106893a5013838610203a87 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/connectors/dropbox-app-subfolder.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=5222a5db731a8ecf05b2fa7e4eee0540 2500w" />

## Replace an expired access token

Dropbox app access tokens are valid for **only four hours**. After this time, you can no longer use the expired access token.

To have Unstructured automatically replace expired access tokens on your behalf, do the following:

<iframe width="560" height="315" src="https://www.youtube.com/embed/PZyRgpPNEUs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

1. Get the app key and app secret values for your Dropbox app. To do this:

   a) Sign in to the [Dropbox Developers](https://www.dropbox.com/developers) portal with the same credentials as your Dropbox account.<br />
   b) Open your [App Console](https://www.dropbox.com/developers/apps).<br />
   c) Click your Dropbox app's icon.<br />
   d) On the **Settings** tab, next to **App key**, copy the value of the app key.<br />
   e) Next to **App secret**, click **Show**, and then copy the value of the app secret.

2. Use your web browser to browse to the following URL, replacing `<app-key>` with the app key for your Dropbox app:

   ```text  theme={null}
   https://www.dropbox.com/oauth2/authorize?client_id=<app-key>&response_type=code&token_access_type=offline
   ```

3. Click **Continue**.

4. Click **Allow**.

5. In the **Access code generated** tile, copy the access code that is shown.

6. Use the [curl](https://curl.se/) utility in your Terminal or Command Prompt, or use a REST API client such as
   [Postman](https://www.postman.com/product/api-client/), to make the following REST API call, replacing the following placeholders:

   * Replace `<app-key>` with the app key for your Dropbox app.
   * Replace `<app-secret>` with the app secret for your Dropbox app.
   * Replace `<access-code>` with the access code that you just copied.

   ```text  theme={null}
   curl --location --request POST 'https://api.dropbox.com/oauth2/token' \
   --user '<app-key>:<app-secret>' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'code=<access-code>' \
   --data-urlencode 'grant_type=authorization_code'
   ```

7. In the response, copy the following two values:

   * The value of `access_token` (starting with the characters `sl`) is the new, valid access token.
   * The value of `refresh_token` is the refresh token that can be used to replace this access token much faster and easier next time.
     If you lose this refresh token, you must go back to Step 2.

   For the [Unstructured UI](/ui/overview), if you want Unstructured to use this refresh token to automatically replace the expired access token instead of replacing it yourself, then
   add the following values to your connector settings, and then stop here:

   * Add the `refresh_token` value to the connector settings **Refresh token** field.
   * Add the `<app-key>` value to the connector settings **App key** field.
   * Add the `<app-secret>` value to the connector settings **App secret** field.

   For the [Unstructured API](/api-reference/overview) and [Unstructured Ingest](/open-source/ingestion/overview), if you want Unstructured to use this refresh token to automatically replace the expired access token instead of replacing it yourself, then
   add the following values to your connector settings, and then stop here:

   * Add the `refresh_token` value to the `refresh_token` parameter.
   * Add the `<app-key>` value to the `app_key` parameter.
   * Add the `<app-secret>` value to the connector settings `app_secret` parameter.

8. If for some reason you need to manually replace the expired access token yourself instead of having Unstructured do it for you, you can use the refresh token that you just copied to get a new access token:

   * Replace `<refresh-token>` with the refresh token.
   * Replace `<app-key>` with the app key for your Dropbox app.
   * Replace `<app-secret>` with the app secret for your Dropbox app.

   ```text  theme={null}
   curl https://api.dropbox.com/oauth2/token \
   --data refresh_token=<refresh-token> \
   --data grant_type=refresh_token \
   --data client_id=<app-key> \
   --data client_secret=<app-secret>
   ```

9. In the response, copy the following two values:

   * The value of `access_token` (starting with the characters `sl`) is the new, valid access token. In the connector, replace the old,
     expired access token value with this new, valid access token value.

   * The value of `refresh_token` is the new, valid refresh token. To replace the expired access token yourself, go back to Step 8.

To create a Dropbox source connector, see the following examples.

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
                  type="dropbox",
                  config={
                      "remote_url": "<remote-url>",
                      "recursive": <True|False>,
                      "refresh_token": "<refresh-token>",
                      "app_key": "<app-key>",
                      "app_secret": "<app-secret>"
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
      "type": "dropbox",
      "config": {
          "remote_url": "<remote-url>",
          "recursive": <true|false>,
          "refresh_token": "<refresh-token>",
          "app_key": "<app-key>",
          "app_secret": "<app-secret>"
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<remote-url>` (*required*) - The remote URL to the target subfolder inside of the app folder for the Dropbox app.
* Set `recursive` to `true` to recursively process data from subfolders within the target subfolder. The default is `false` if not otherwise specified.
* `<app-key>` (*required*) - The app key for your Dropbox app. This allows Unstructured to automatically replace expired access tokens.
* `<app-secret>` (*required*) - The app secret for your Dropbox app. This allows Unstructured automatically to replace expired access tokens.
* `<refresh-token>` (*required*) - The refresh token for the Dropbox app. This allows Unstructured to automatically replace expired access tokens.
