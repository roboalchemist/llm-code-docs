# Source: https://developers.webflow.com/data/docs/working-with-webhooks.mdx

***

title: Working with webhooks
slug: data/docs/working-with-webhooks
hidden: false
-------------

Webhooks are a powerful way to integrate your applications and services with Webflow, allowing you to receive real-time updates whenever [specific events](#event-types)  occur on your site. By setting up webhooks, you can automate workflows, trigger external processes, and synchronize data across different platforms without any manual intervention.

<br />

<Card
  title="Get started with webhooks"
  iconPosition="left"
  iconSize="12"
  icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/CustomWebhooks.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/CustomWebhooks.svg" alt="" className="block dark:hidden" />
        </>
    }
>
  Ready to streamline your workflow? Follow the steps below to create your first webhook using the Webflow API. <br /><br />

  <a href="#creating-a-webhook">
    <button>
      Start Tutorial
    </button>
  </a>
</Card>

<br />

# Webhook requests

When an event occurs, Webflow will send a `POST` request to a specified URL.

The webhook body will be a JSON resource object that relates to the event. The request headers will include:

* A `Content-Type` header set to `application/json`
* A `x-webflow-timestamp` with the time the webhook was sent
* A `x-webflow-signature` header containing the request signature. Read on for information about [validating request signatures.](#validating-request-signatures)

<br />

Below is an example of webhook event data.

<Tabs>
  <Tab title="JSON Example">
    ```json Payload
      {
        "triggerType": "form_submission",
        "payload": {
          "name": "Contact Us",
          "siteId": "65427cf400e02b306eaa049c",
          "data": {
            "First Name": "Zaphod",
            "Last Name": "Beeblebrox",
            "email": "zaphod@heartofgold.ai",
            "Phone Number": 15550000000
          },
          "schema": [
            {
              "fieldName": "First Name",
              "fieldType": "FormTextInput",
              "fieldElementId": "285042f7-d554-dc7f-102c-aa10d6a2d2c4"
            },
            {
              "fieldName": "Last Name",
              "fieldType": "FormTextInput",
              "fieldElementId": "285042f7-d554-dc7f-102c-aa10d6a2d2c5"
            },
            {
              "fieldName": "email",
              "fieldType": "FormTextInput",
              "fieldElementId": "285042f7-d554-dc7f-102c-aa10d6a2d2c6"
            },
            {
              "fieldName": "Phone Number",
              "fieldType": "FormTextInput",
              "fieldElementId": "285042f7-d554-dc7f-102c-aa10d6a2d2c7"
            }
          ],
          "submittedAt": "2022-09-14T12:35:16.117Z",
          "id": "6321ca84df3949bfc6752327",
          "formId": "65429eadebe8a9f3a30f62d0",
          "formElementId": "4e038d2c-6a1e-4953-7be9-a59a2b453177"
        }
      }
    ```
  </Tab>

  <Tab title="Properties">
    <ParamField path="triggerType" type="string">
      The type of event that triggered the request
    </ParamField>

    <ParamField path="payload" type="object">
      The payload of data sent from Webflow

      <div class="expandable">
        <Accordion title=" ">
          <ParamField path="name" type="string">
            The name of the form
          </ParamField>

          <ParamField path="siteId" type="string">
            The id of the site that the form was submitted from
          </ParamField>

          <ParamField path="data" type="object">
            The data submitted in the form

            <Accordion title=" ">
              <ParamField path="firstName" type="string" />

              <ParamField path="lastName" type="string" />

              <ParamField path="email" type="string" />

              <ParamField path="phoneNumber" type="string" />
            </Accordion>
          </ParamField>

          <ParamField path="submittedAt" type="string">
            The timestamp the form was submitted
          </ParamField>

          <ParamField path="id" type="string">
            the ID of the event
          </ParamField>

          <ParamField path="formId" type="string">
            The ID of the form submission
          </ParamField>
        </Accordion>
      </div>
    </ParamField>
  </Tab>
</Tabs>

<br />

# Creating a webhook

In this tutorial, we'll walk through creating a webhook to listen for new submissions to a contact form on a site. Whenever someone submits this form, Webflow will send a notification to the specified destination. Additionally, we'll cover how to verify that the webhook requests you're receiving are genuinely from Webflow, ensuring secure and reliable communication with your application.

<Note title="Looking for a simpler setup?">
  If you'd prefer a way to set up webhooks without using the API, you can easily [configure them through the Webflow dashboard](https://university.webflow.com/lesson/intro-to-webflow-apis?topics=cms-dynamic-content#how-to-create-a-webhook). Please note, that webhooks created through the dashboard will not include the request headers needed to [validate request signatures.](#validating-request-signatures)
</Note>

#### Prerequisites

* A [site token](/data/reference/site-token) or bearer token from a Webflow [Data Client App](/data/docs/getting-started-apps) with the `forms:read` scope.
* A Webflow test site. You can use the [Biznus template](https://webflow.com/templates/html/biznus-retail-website-template) to quickly set up a site equipped with a contact form.
* A service to accept an HTTPS request. While we'll be using [https://webhook.site](https://webhook.site) in this tutorial, you're free to choose any platform.

<br />

<Accordion title="Step 1. Create a form">
  Before we get started working with the API, we'll first need to create a form and publish our site. If you already have a working form on your site, you can skip this step. To create a site with a form, we'll use the <a href="https://webflow.com/dashboard/sites/new?t=5e864888a8dec40670d77ac4">Biznus template</a>, which already has a <a href="https://biznus-template.webflow.io/contact">form</a> on its contact page.

  1. **Clone the [Biznus template](https://webflow.com/dashboard/sites/new?t=5e864888a8dec40670d77ac4)** to your development Workspace.

  2. **Go to the Contact Page** to view your form. Here, you can review your form's fields. Ensure each field has a unique name. These field names will be used as keys in the webhook's payload.
     ![Form Fields](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3f45f69aca87ea3c60972974e53a7c72a80b4b8388b2542172397cc692223eb8/assets/images/6f39396-Screen_Shot_2022-11-08_at_1.42.30_PM.png)

  3. **Publish the site** by clicking the publish button in the top right corner.
</Accordion>

<Accordion title="Step 2. Create a webhook">
  Webhooks require the following elements to function:

  * **Site ID:** The unique identifier of your Webflow site.
  * **Trigger Type:** Specific event the webhook will monitor.
  * **Destination URL:** Unique URL prepped to accept HTTP requests.

  Once we have these elements, we can create the webhook by sending a `POST` request to the [Create Webhook](https://developers.webflow.com/data/reference/webhooks/create) endpoint.

  1. **Get the Site ID.** There are two ways to get your Site ID, you can access the ID via site settings, or send a request to the [List Sites](https://developers.webflow.com/data/reference/sites/list) endpoint.

     <Tabs>
       <Tab title="Site Settings">
         1. In the designer, click the Webflow Icon in the top left corner, and select "Site Settings" from the menu.

         2. In your site settings, scroll down to the "Overview" section to find your Site ID
            ![Site ID location in settings](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/e3071f6add47d66472945082d7cd25929679b0781c24f75b145232439b4c9358/assets/images/7bbb258-Screenshot_2024-07-29_at_2.49.21_PM.png)
       </Tab>

       <Tab title="API Request">
         1. Send a request to the [List Sites](https://developers.webflow.com/data/reference/sites/list) endpoint.

            <CodeBlocks>
              ```curl cURL
              curl --request GET \
                        --url https://api.webflow.com/v2/sites \
                        --header 'accept: application/json' \
                        --header 'authorization: Bearer YOUR_ACCESS_TOKEN'
              ```

              ```javascript node.js
              const webflow = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
              async function fetchSites() {
                try {
                  const sites = await webflow.sites.get();
                  console.log(sites);
                } catch (error) {
                  console.error("Error fetching sites:", error);
                }
              }
              fetchSites();
              ```
            </CodeBlocks>

         2. Review the response to find the `displayName` of your test site and its corresponding `id`.

            ```json Response
            {
              "sites": [
                {
                  "id": "42e63e98c9a982ac9b8b741",
                  "workspaceId": "42e63fc8c9a982ac9b8b744",
                  "createdOn": "1979-10-12T12:00:00.000Z",
                  "displayName": "Heart of Gold Spaceship",
                  "shortName": "heart-of-gold",
                  "lastPublished": "2023-04-02T12:42:00.000Z",
                  "previewUrl": "https://dev-assets.website-files.com/42e63e98c9a982ac9b8b741/197910121200.png",
                  "timeZone": "DeepSpace/InfiniteImprobability",
                  "parentFolderId": "1as2d3f4g5h6j7k8l9z0x1c2v3b4n5m6",
                  "customDomains": [
                    {
                      "id": "589a331aa51e760df7ccb89e",
                      "url": "heartofgold.galaxy"
                    }
                  ],
                  "locales": {
                    "primary": {
                      "id": "653fd9af6a07fc9cfd7a5e57",
                      "cmsLocaleId": "653ad57de882f528b32e810e",
                      "enabled": true,
                      "displayName": "English - Heart of Gold Standard",
                      "redirect": false,
                      "subdirectory": "/en",
                      "tag": "The Ultimate Answer"
                    },
                    "secondary": [
                      {
                        "id": "653fd9af6a07fc9cfd7a5e58",
                        "cmsLocaleId": "653ad57de882f528b32e810g",
                        "enabled": true,
                        "displayName": "Betelgeusian - Vogon Liaison",
                        "redirect": true,
                        "subdirectory": "/bet",
                        "tag": "Vogon"
                      },
                      {
                        "id": "653fd9af6a07fc9cfd7a5e59",
                        "cmsLocaleId": "653ad57de882f528b32e810h",
                        "enabled": false,
                        "displayName": "Magrathean - Custom Planet Designs",
                        "redirect": true,
                        "subdirectory": "/mg",
                        "tag": "Magrathean"
                      }
                    ]
                  }
                },  ]
            }
            ```
       </Tab>
     </Tabs>

  2. **Get your destination URL.** Navigate to [webhook.site](https://webhook.site) and copy your unique URL. This URL will be used as the destination where Webflow will send webhook events.
     ![Screenshot showing webhook.site interface with unique URL](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/016bf242fb68ded0df190fc26dc9210e727b87844ce8ce16e31b665bdcc1bd50/assets/images/1428146-Screenshot_2024-07-30_at_12.54.18_PM.png)

  3. **Send a `POST` request to the [Create Webhook](https://developers.webflow.com/data/reference/webhooks/create) endpoint.** In the request, you'll include the `site_id`, `url`, and `triggerType` of `form_submission`.

     <CodeBlocks>
       ```curl cURL
       curl -X POST "https://api.webflow.com/sites/YOUR_SITE_ID/webhooks" \
               -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
               -H "Content-Type: application/json" \
               -d '{
                     "triggerType": "form_submission",
                     "url": "https://your-webhook-url.com"
                   }'
       ```

       ```javascript JavaScript
       const WebflowClient = require('webflow-api'); // Import Webflow API client

       async function createWebhook(req) {
         const accessToken = req.accessToken; // Get access token from the request
         const siteId = "YOUR_SITE_ID"; // Replace with your actual Site ID

         const webflow = new WebflowClient({ accessToken }); // Initialize Webflow client

         try {
           const webhook = await webflow.webhooks.create(siteId, {
             triggerType: 'form_submission', // Trigger type for the webhook
             url: "https://your-webhook-url.com" // Replace with your webhook URL
           });
           console.log('Webhook created successfully:', webhook);
           return webhook;
         } catch (error) {
           console.error('Error creating webhook:', error.message);
         }
       }

       createWebhook(req); // Moved function call outside the function definition
       ```
     </CodeBlocks>

     Additionally, the `form_submission` trigger supports a `filter` parameter, allowing you to specify the name of the form you'd like to receive notifications for. This is particularly helpful if you have multiple forms on a site.

     <Info title="Use our interactive API Docs to send requests">
       You can also use the interactive API Reference to quickly send a POST request to the [Create Webhook](/data/reference/webhooks/create) endpoint without writing any code.
     </Info>

  4. **Review the response.** After successfully establishing your webhook, you should receive a confirmation similar to the one shown below:
     <CodeBlocks>
       ```json Successful response
       {
         "id": "582266e0cd48de0f0e3c6d8b",
         "triggerType": "form_submission",
         "siteId": "562ac0395358780a1f5e6fbd",
         "workspaceId": "4f4e46fd476ea8c507000001",
         "createdOn": "2022-11-08T23:59:28.572Z",
         "lastTriggered": "2023-02-08T23:59:28.572Z",
         "filter": null,
         "url": "https://webhook.site/7f7f7f7f-7f7f-7f7f-7f7f-7f7f7f7f7f7f",
         "secretKey": "2b4acfd1c5518bf03c73a4889d197d77251353857c22694bf150b9e3402ba15f"
         // 👆 The secret key is only present if using a Site API key created from the Site Dashboard
       }
       ```
     </CodeBlocks>
</Accordion>

<Accordion title="Step 3. Send a test submission">
  Once you've successfully created the Webhook to listen for new form submissions, you can test it by navigating to the form on your site and submitting a response.

  Once you've submitted a response, head over to [webhook.site](https://webhook.site) to view the `POST` request from Webflow. If the request is successful, you'll see the Request Details, Headers, and Payload sections. These details should match the JSON object shown below.

  <CodeBlocks>
    ```json JSON
    Content-Type: application/json
    x-webflow-timestamp: 1722370035277
    x-webflow-signature: cb6162d8daf6573c658805a5f431adab25f56faf6c601935067d3957a161dfeb
    {
      "triggerType": "form_submission",
      "payload": {
        "name": "Email Form",
        "siteId": "65427cf400e02b306eaa049c",
        "data": {
          "Email 2": "hello@gmail.com"
        },
        "submittedAt": "2024-07-30T20:07:15.220Z",
        "id": "66a947f35b9d7ba400e22733",
        "formId": "65429eadebe8a9f3a30f62d7"
      }
    }
    ```
  </CodeBlocks>

  <Info>
    Notice the headers included in the response: `x-webflow-timestamp` and `x-webflow-signature`. These headers are crucial for verifying the authenticity of the webhook.
  </Info>
</Accordion>

# Webhook retries

Your service should return a `200` response  to show that the webhook was successfully captured. If the response status is anything else, the webhook will be retried up to three more times at which point the request will be considered failed and will no longer be retried.

<br />

### Failure conditions

Webflow considers the following scenarios as failure conditions:

* **Non-200 HTTP status code response**: If we receive any response other than a valid HTTP 200 response, it is regarded as a failure.
* **Redirects**: If the webhook encounters redirects while attempting to deliver the payload, it will be treated as a failure.
* **SSL Certificate Issues**: If we cannot successfully negotiate or validate your server's SSL certificate, it will be marked as a failure.
* **Timeouts**: Webflow expects a swift response during webhook delivery. If there are prolonged delays in receiving a response from your server, it will be considered a failure.

<br />

### Deactivation of webhooks

If Webflow repeatedly encounters failure conditions while attempting to deliver a webhook payload, we will take the following action:

* **Deactivation**: We will deactivate your webhook to prevent further delivery attempts.
* **Notification**: You will be notified of the webhook deactivation via email.

To reactivate your webhook or if you have any questions regarding a deactivated webhook, please don't hesitate to reach out to our [support team](https://support.webflow.com/).

<br />

### Limits

Understanding the limits imposed by Webflow can help you design and manage your webhooks more efficiently:

| **Criteria**                                                        | **Limitation** |
| :------------------------------------------------------------------ | :------------: |
| Maximum webhooks for a specific `trigger_type`                      |     **75**     |
| Maximum number of retry attempts after an unsuccessful webhook call |      **3**     |
| Interval (in minutes) between each retry                            |     **10**     |

<br />

# Event types

This is the full list of webhook events available in Webflow. For complete documentation of webhook events with payloads, please see the [webhook events documentation.](https://developers.webflow.com/data/reference/all-events)

| Event                         | Description                                                                                                                                 |   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | - |
| `form_submission`             | Details about a form submission, including form name, site ID, data submitted, submission timestamp, and form ID.                           |   |
| `site_publish`                | Details about a site publish event, including site ID, published timestamp, domains, and user who published the site.                       |   |
| `page_created`                | Information about a new page event, including site ID, page ID, page title, and creation timestamp.                                         |   |
| `page_metadata_updated`       | Metadata of a page is updated and published, including site ID, page ID, page title, and last updated timestamp.                            |   |
| `page_deleted`                | Information about a deleted page, including site ID, page ID, page title, and deletion timestamp.                                           |   |
| `ecomm_new_order`             | Information about a new order, including order ID, status, customer information, shipping details, and purchased items.                     |   |
| `ecomm_order_changed`         | Details about an order that changed, including order ID, status, comments, customer information, and updated order details.                 |   |
| `ecomm_inventory_changed`     | Information about the inventory item that changed, including item ID, quantity, and inventory type.                                         |   |
| `collection_item_created`     | Details about a newly created collection item, including item ID, site ID, Workspace ID, collection ID, creation date, and draft status.    |   |
| `collection_item_changed`     | Information about an updated collection item, including item ID, site ID, Workspace ID, collection ID, last updated date, and item details. |   |
| `collection_item_deleted`     | Details about a deleted collection item, including item ID, site ID, Workspace ID, and collection ID.                                       |   |
| `collection_item_unpublished` | Information about an unpublished collection item, including item ID, site ID, Workspace ID, and collection ID.                              |   |

# Validating request signatures

Webflow provides methods to verify that requests are genuinely coming from the Webflow API by using signatures included in the request headers. **These signatures vary based on the creation method of the webhook.**

### Request headers

* `x-webflow-timestamp` : The time the webhook was sent, represented in Unix epoch time format.
* `x-webflow-signature` : The request signature, formatted as a SHA-256 HMAC hash. It uses either the site token secret or the OAuth app's client secret as the signing key.

To ensure the authenticity of a webhook request from Webflow, validate the request signature using the provided headers and your webhook's associated signing key.

### Signing keys

Depending on the creation method of the webhook, you'll receive a different signing key.

* **Site token secret** : For webhooks created through site settings via a site token after **April 14, 2025**, each webhook will have its own secret key. You'll need to store this key securely and use it as your signing key.
* **OAuth app client secret** : For webhooks created through an OAuth application, you won't receive a separate secret key. Instead, you'll use your OAuth app's client secret as the signing key.

### Recommended: Use the provided signature validation method

Webflow recommends use of the provided SDK method to verify the incoming webhook requests' signatures.

As signature implementations are subject to change, Webflow will support updates to the method to ensure smooth transitions for developers.
All you will need to do is update the package version to benefit from these changes.

1. **Extract data from the HTTP Request**
   * `headers` : Keep the headers as a record-like object
   * `body` : Stringify the entire request body

2. **Await the results**
   <CodeBlocks>
     ```javascript Javascript
     import express from 'express';
     import { WebflowClient } from "webflow-api";

     const webflowClient = new WebflowClient({ accessToken: AUTHTOKEN });
     const app = express();
     app.use(express.json());
     // ...

     app.post('/FormSubmission', async (req, res) => {
       const isValidRequest = await webflowClient.webhooks.verifySignature({
         headers: req.headers,
         body: JSON.stringify(req.body),
         secret: WEBHOOK_SECRET,
       });

       if (isValidRequest) {
         // ...handle the request
       } else {
         // ...handle malicious request
       }

       res.sendStatus(200);
     });
     ```
   </CodeBlocks>

### Steps to manually validate the request signature

If you need to validate the request signature without use of the SDK, follow the steps below to achieve the same effect as the SDK method.

1. **Generate the HMAC hash**
   * Retrieve the timestamp from the `x-webflow-timestamp` header.
   * Concatenate the timestamp and the request body with a colon (`:`) separator. The format should be:
     <CodeBlocks>
       ```javascript JavaScript
       timestamp + ":" + JSON.stringify(request_body)
       ```

       ```python Python
       data = f"{request_timestamp}:{request_body_json}"
       ```
     </CodeBlocks>
   * Use your OAuth application's client secret (or your secret key if the webhook is not associated with an OAuth Application) and the SHA-256 hashing algorithm to generate the HMAC hash.

2. **Compare the generated hash with the provided signature**
   Compare the generated HMAC hash with the `x-webflow-signature` header from the request. A match confirms the request's legitimacy; otherwise, it should be considered potentially tampered with or fraudulent.

3. **Verify the timestamp**
   Check the `x-webflow-timestamp` header to ensure the request is recent. A request older than 5 minutes may indicate a replay attack. Calculate the request's age as follows:

   <CodeBlocks>
     ```javascript JavaScript
     currentTime - Number(request_timestamp)
     ```

     ```python Python
     current_time - int(request_timestamp)
     ```
   </CodeBlocks>

   If the difference exceeds 5 minutes (300,000 milliseconds), consider the request potentially compromised.

   See below for examples that accept an incoming HTTPS request and validate the signature:

   <CodeBlocks>
     ```javascript Node
     const express = require('express');
     const crypto = require('crypto');
     const bodyParser = require('body-parser');

     const app = express();
     const PORT = 3000;
     const CLIENT_SECRET = 'your_client_secret'; // Replace with your Webflow OAuth application's client secret

     app.use(bodyParser.json()); // Parse JSON request bodies

     app.post('/webhook', (req, res) => {
       // Step 1: Extract headers and body from the request
       const requestBody = JSON.stringify(req.body);
       const timestamp = req.headers['x-webflow-timestamp'];
       const providedSignature = req.headers['x-webflow-signature'];

       // Step 2: Verify the signature
       if (!verifyWebflowSignature(CLIENT_SECRET, timestamp, requestBody, providedSignature)) {
         return res.status(400).send('Invalid signature'); // Respond with a 400 Bad Request if verification fails
       }

       // Process the webhook request as necessary
       console.log('Webhook verified and received:', req.body);
       res.status(200).send('Webhook received');
     });

     function verifyWebflowSignature(clientSecret, timestamp, requestBody, providedSignature) {
       try {
         // Step 3: Convert the timestamp to an integer
         const requestTimestamp = parseInt(timestamp, 10);

         // Step 4: Generate the HMAC hash
         const data = `${requestTimestamp}:${requestBody}`;
         const hash = crypto.createHmac('sha256', clientSecret)
                           .update(data)
                           .digest('hex');

         // Step 5: Compare the generated hash with the provided signature
         if (!crypto.timingSafeEqual(Buffer.from(hash, 'hex'), Buffer.from(providedSignature, 'hex'))) {
           throw new Error('Invalid signature');
         }

         // Step 6: Validate the timestamp (within 5 minutes)
         const currentTime = Date.now();
         if (currentTime - requestTimestamp > 300000) { // 5 minutes in milliseconds
           throw new Error('Request is older than 5 minutes');
         }

         return true; // The request is valid

       } catch (err) {
         console.error(`Error verifying signature: ${err.message}`);
         return false;
       }
     }

     app.listen(PORT, () => {
       console.log(`Server is running on port ${PORT}`);
     });

     ```

     ```python Python
     import hashlib
     import hmac
     import json
     import time
     from flask import Flask, request, abort

     app = Flask(__name__)

     @app.route('/webhook', methods=['POST'])
     def webhook():
         # Step 1: Extract headers and body from the request
         client_secret = 'your_client_secret'  # Your Webflow OAuth application's client secret
         request_body = request.get_data(as_text=True)
         request_json = json.loads(request_body)
         timestamp = request.headers.get('x-webflow-timestamp')
         provided_signature = request.headers.get('x-webflow-signature')

         # Step 2: Verify the signature
         if not verify_webflow_signature(client_secret, timestamp, request_body, provided_signature):
             abort(400, 'Invalid signature')  # Respond with a 400 Bad Request if verification fails

         # Process the webhook request as necessary
         return 'Webhook received', 200

     def verify_webflow_signature(client_secret, timestamp, request_body, provided_signature):
         try:
             # Convert the timestamp to an integer
             timestamp = int(timestamp)

             # Generate the HMAC hash
             data = f"{timestamp}:{request_body}"
             digest = hmac.new(client_secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

             # Compare the generated hash with the provided signature
             if not hmac.compare_digest(digest, provided_signature):
                 raise ValueError("Invalid signature")

             # Validate the timestamp
             current_time = int(time.time() * 1000)  # Convert current time to milliseconds
             if current_time - timestamp > 300000:  # 5 minutes in milliseconds
                 raise ValueError("Request is older than 5 minutes")

             return True  # The request is valid

         except Exception as e:
             print(f"Error verifying signature: {str(e)}")
             return False

     if __name__ == '__main__':
         app.run(port=5000)

     ```
   </CodeBlocks>
