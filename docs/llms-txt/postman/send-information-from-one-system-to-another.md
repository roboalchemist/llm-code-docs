# Send information from one system to another using Postman Flows

Developers often integrate multiple APIs to leverage their individual features. For example, you can get customer profiles from a payment services provider like [Stripe](http://www.stripe.com) and add those profiles as contacts on a marketing platform like [Brevo](http://www.brevo.com). This tutorial shows you how to do this with Postman Flows.

## Goal

Create a flow that gets a list of customer profiles from [Stripe](http://www.stripe.com) and adds them as contacts to a database in [Brevo](http://www.brevo.com).

## Prerequisites

* A [Stripe](http://www.stripe.com) account and API key.
* At least 15 Stripe customers.
* A [Brevo](http://www.brevo.com) account and API key.

## Create the flow, collections, and environment

1. Open the [**Integration Flows** public workspace](https://www.postman.com/postman/integration-flows/flows-get-started) and [fork](/docs/collaborating-in-postman/using-version-control/forking-elements/) the **Brevo API** collection, the **Stripe API** collection, and the **Stripe + Brevo** environment to your workspace.

1. In your workspace, [open the Stripe + Brevo environment](/docs/sending-requests/variables/managing-environments/#edit-an-environment).

1. [Replace](/docs/sending-requests/variables/environment-variables/#edit-environment-variables) the **stripe\_secret\_key** variable's value, **your key here**, with your Stripe API key.

1. [Create a new flow module](/docs/postman-flows/get-started/build-your-first-flow/) and click **Send a request**.

## Set up the initial Stripe request

1. Click **Find or create new request** and select **Stripe API > Customers > List all customers**.

1. Click **Add environment** and select **Stripe + Brevo**. The **HTTP Request** block shows the request's three variables. The `baseUrl` and `stripe_secret_key` variables are populated automatically from values stored in the request's collection and environment.

1. Next to the **limit** variable, click \[![Image 1: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon)\] **Add data blocks** and select **Number**. Enter "5" to specify how many contacts to include in each page of results. This tutorial uses 15 contacts, so a limit of 5 will send three pages of results.

    \[![Image 2: Create a new flow](https://assets.postman.com/postman-docs/v10/flows-tut-system-first-sr-v10.png)\]

1. Add pagination logic:

    1. Connect the **HTTP Request** block's **Success** output to a **Select** block.
    
    1. Click **Enter path** and enter "body.has_more".
    
    \[![Image 3: Select body.has_more](https://assets.postman.com/postman-docs/v10/flows-tut-select-has_more-v10.png)\]
    
    1. Connect the **HTTP Request** block's **Success** output to another **Select** block.
    
    1. Click **Enter path** and enter "body.data".
    
    \[![Image 4: Select body.data](https://assets.postman.com/postman-docs/v10/flows-tut-select-data-v10.png)\]
    
    1. Connect the `has_more` **Select** block's output to an **If** block's **variable** input and rename `value1` to `has_more`.
    
    1. Click **Start writing TypeScript** and enter "has_more".
    
    1. Connect the `body.data` **Select** block's output to the **If** block's **Data** input.
    
    \[![Image 5: Add an If block](https://assets.postman.com/postman-docs/v10/flows-tut-if-has_more-v10.png)\]
    
    1. Connect an **Evaluate** block's **variable** input to the **If** block's **THEN** output. Rename `value1` to `contacts`.
    
    1. Click **Start writing TypeScript** and enter "contacts[$count(`contacts`)-1].id". This gets the ID of the last object when there is at least one more contact in the original response.
    
    \[![Image 6: Add an Evaluate block](https://assets.postman.com/postman-docs/v10/flows-tut-eval-contacts-v10.png)\]
    
    ## Add a paginated request
    
    1. Connect an **HTTP Request** block to the **Evaluate** block's **Result** output.
    
    1. Click **Find or create new request** and select **Stripe API > Customers > List all customers pagination**. The block automatically selects the **Stripe + Brevo** environment.
    
    1. Next to the **limit** variable, click \[![Image 7: Add icon](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon)\] **Add data blocks** and select **Number**. Enter "5" to specify how many contacts to include in each page of results.
    
    1. Connect the **Evaluate** block's **Result** output to the `starting_after` variable in the **HTTP Request** block.
    
    1. Connect the **HTTP Request** block's **Success** output to both the `body.has_next` and the `body.data` **Select** blocks' inputs.
    
    \[![Image 8: Add another HTTP Request block](https://assets.postman.com/postman-docs/v10/flows-tut-send-request-pagination-v10.png)\]
    
    ## Add a loop to send contacts to Brevo
    
    1. Connect the **If** block's **THEN** and **ELSE** outputs to a **For** block's **List** input.
    
    1. Connect the **For** block's **Item** output to an **HTTP Request** block.
    
    \[![Image 9: Add a For block](https://assets.postman.com/postman-docs/v10/flows-tut-if-for-send-v10.png)\]
    
    1. In the **HTTP Request** block, click **Find or create new request** and select **Brevo API > Contact management > Contacts > POST Create a contact**. Click **Add environment** and select **Stripe + Brevo**.
    
    \[![Image 10: Select the POST request](https://assets.postman.com/postman-docs/v10/flows-tut-post-contact-v10.png)\]
    
    1. Connect the **For** block's **Item** output to the `email` and `first_name` variables' inputs. Enter "name" for the `first_name` variable and "email" for the `email` variable.
    
    \[![Image 11: Set variables](https://assets.postman.com/postman-docs/v10/flows-tut-email-name-v10.png)\]
    
    ## Run and verify the flow
    
    Run the flow and confirm the records are added to Brevo.

![Image 12: Postmanaut illustration for Postman Flows section.](https://voyager.postman.com/illustration/flows-postman-illustration.svg)