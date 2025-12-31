# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/post-requests.md

# Source: https://docs.unstructured.io/api-reference/partition/post-requests.md

# Process an individual file by making a direct POST request

Watch the following 4-minute video to learn how to make POST requests to the Unstructured Partition Endpoint to process individual files:

<iframe width="560" height="315" src="https://www.youtube.com/embed/fU080EahKwc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

Open the related [notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_API_Partition_endpoint.ipynb) that is shown in the preceding video.

To make POST requests to the Unstructured Partition Endpoint, you will need:

These environment variables:

* `UNSTRUCTURED_API_KEY` - Your Unstructured API key value.
* `UNSTRUCTURED_API_URL` - Your Unstructured API URL.

To get your API key, do the following:

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

3. Get your Unstructured API key:<br />

   a. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

   <Note>
     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).
   </Note>

   b. Click **Generate API Key**.<br />
   c. Follow the on-screen instructions to finish generating the key.<br />
   d. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

The API URL was provided to you when your Unstructured account was created.
If you do not have this URL, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

<Note>
  The default URL for the Unstructured Partition Endpoint is `https://api.unstructuredapp.io/general/v0/general`.
  However, you should always use the API URL that was provided to you when your Unstructured account was created.
</Note>

Let's start with a simple example in which you use [curl](https://curl.se/) to send a local PDF file (`*.pdf`) to partition via the Unstructured Partition Endpoint.

In this command, be sure to replace `<path/to/file>` with the path to your local PDF file.

```bash  theme={null}
curl --request 'POST' \
"$UNSTRUCTURED_API_URL" \
--header 'accept: application/json' \
--header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
--header 'content-Type: multipart/form-data' \
--form 'content_type=string' \
--form 'strategy=vlm' \
--form 'vlm_model_provider=openai' \
--form 'vlm_model=gpt-4o' \
--form 'output_format=application/json' \
--form 'files=@<path/to/file>;type=application/pdf'
```

In the example above we're representing the API endpoint with the environment variable `UNSTRUCTURED_API_URL`. Note, however, that you also need to authenticate yourself with
your individual API Key, represented by the environment variable `UNSTRUCTURED_API_KEY`. Learn how to obtain an API URL and API key in the [Unstructured Partition Endpoint guide](/api-reference/partition/overview).

## Parameters & examples

The API parameters are the same across all methods of accessing the Unstructured Partition Endpoint.

* Refer to the [API parameters](/api-reference/partition/api-parameters) page for the full list of available parameters.
* Refer to the [Examples](/api-reference/partition/examples) page for some inspiration on using the parameters.

[//]: # "TODO: when we have the concepts page shared across products, link it from here for the users to learn about partition strategies, chunking strategies and other important shared concepts"

## Postman collection

Unstructured offers a [Postman collection](https://learning.postman.com/docs/collections/collections-overview/) that you can import into Postman to make POST requests through a graphical user interface.

1. [Install Postman](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/).

2. [Sign in to Postman](https://learning.postman.com/docs/getting-started/installation/postman-account/#signing-in-to-postman).

3. In your workspace, click **Import**.

   <img src="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=75b5e5c9bedfc173f80852e45bc2086a" alt="Import a Postman collection" data-og-width="374" width="374" data-og-height="95" height="95" data-path="img/api/post/import.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=280&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=04bb0bcbdfe8e173423a8694cb2fd9de 280w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=560&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=712a18b8d6843fc0a57961facd927478 560w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=840&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=03191eebb7f94b687e91053793a3a789 840w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=1100&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=9dee61ef12f6045a745eb1b9c85104b5 1100w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=1650&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=dd0124c64017d4e2363fb730e6788d4e 1650w, https://mintcdn.com/unstructured-53/vKFDfUfAWhz_siB3/img/api/post/import.png?w=2500&fit=max&auto=format&n=vKFDfUfAWhz_siB3&q=85&s=fe3c5fd1741ff86d7248dc66c96145a7 2500w" />

4. In the **Paste cURL, Raw text or URL** box, enter the following URL, and then press `Enter`:

   ```
   https://raw.githubusercontent.com/Unstructured-IO/docs/main/examplecode/codesamples/api/Unstructured-POST.postman_collection.json
   ```

5. On the sidebar, click **Collections**.

6. Expand **Unstructured POST**.

7. Click **(Partition Endpoint) Basic Request**.

8. On the **Headers** tab, next to `unstructured-api-key`, enter your Unstructured API key in the **Value** column.

9. On the **Body** tab, next to `files`, click the **Select files** box in the **Value** column.

10. Click **New file from local machine**.

11. Browse to and select the file that you want Unstructured to process.

12. Click **Send**. Processing could take several minutes.

To download the processed data to your local machine, in the response area, click the ellipses, and then click **Save response to file**.
