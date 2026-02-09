# Automate repetitive tasks using Postman Flows

You can use Postman Flows to complete repetitive tasks. Businesses often need to delete emails from multiple systems. Logging in, searching, and deleting emails from multiple locations can be time-consuming. This tutorial shows you how to create a flow that deletes an email from three locations each time you run the flow.

For this tutorial, the locations are [Stripe.com](https://stripe.com/), [Brevo.com](https://www.brevo.com/), and a Postman mock server that acts as a hypothetical internal system.

You can find the [complete flow](https://www.postman.com/postman/devops-flows/flow/6417a7608c4c54003a4ad899) in the [DevOps Flows](https://www.postman.com/postman/devops-flows/overview) workspace.

## Prerequisites

* A Stripe account with a customer with the `test@email.com` email address.
* A Brevo account with a contact with the `test@email.com` email address.
* A Stripe secret key.
* A Brevo API key.

## Fork the collections and environment

[Fork](https://www.postman.com/docs/collaborating-in-postman/using-workspaces/public-workspaces/public-workspaces/ "Fork") these collections from the [**DevOps Flows**](https://www.postman.com/postman/devops-flows/overview) workspace into your workspace:

* [**Stripe API**](https://www.postman.com/postman/devops-flows/collection/xuxoonj/stripe-api?action=share&creator=21580188)
* [**Brevo**](https://www.postman.com/postman/devops-flows/collection/lwjd0gh/brevo?action=share&creator=21580188)
* [**customer-list**](https://www.postman.com/postman/devops-flows/collection/inwryya/customer-list?action=share&creator=21580188)

Fork this environment into your workspace:

* [**gdpr-delete-email**](https://www.postman.com/postman/devops-flows/environment/21580188-d7306a24-e742-42e2-8bfd-d122bd1e52ca)

In the **gdpr-delete-email** environment, replace `your-brevo-api-key` with your Brevo API key. Replace `your-stripe-secret-key` with your Stripe secret key.

![Add API keys](https://assets.postman.com/postman-docs/v11/flows-tut-rep-update-env-v11.jpg)

## Create the flow

1. Part one: Delete the contact from Stripe

    * Create a new flow. Add a **String** block and enter `test@email.com`.
    
    * Connect a **Create Variable** block and enter `Customer Email`.
    
        ![Create a variable](https://assets.postman.com/postman-docs/v10/flows-tut-rep-create-variable-v10.gif)
    
    * Connect three **HTTP Request** blocks to the **Start** block, arranged vertically.
    
        ![Create three HTTP Request blocks](https://assets.postman.com/postman-docs/v10/flows-tut-rep-3send-requests-v10.jpg)
    
    * In the top **HTTP Request** block, select **Stripe API > Customers > Search customers**.
    * Select the **gdpr-delete-email** environment.
    * For the `email` variable, add a **Get Variable** block and click **Customer Email**.
    
        ![Get the variable](https://assets.postman.com/postman-docs/v10/flows-tut-rep-get-variable-v10.gif)
    
    * Create an **If** block next to the **HTTP Request** block. Add a **Select** block to the **If** block and change `value1` to `contacts`.
    
        ![Add an If block](https://assets.postman.com/postman-docs/v10/flows-tut-rep-if-block-v10-2.gif)
    
    * Connect the **HTTP Request** block's **Success** output to the **If** block's `contacts` and **Data** inputs. Next to `contacts`, select `body.data`. In the FQL window, enter `$count(contacts) > 0`.
    * Connect the **If** block's **FALSE** output to a **Display** block.
    * Rename the **Display** block `Contact not found` and select **Boolean** from the dropdown list.
    * Connect the **If** block's **TRUE** output to an **HTTP Request** block. Select **Stripe API > Customers > Delete a customer**.
    * Also connect the **If** block's **TRUE** output to the **HTTP Request** block's **customer_id** input and select `body.data.0.id`.
    * Connect the **HTTP Request** block's **Success** output to a **Display** block.
    * Rename the **Display** block `Contact deleted` and select **Boolean** from the dropdown list.
    
        ![Stripe contact deleted](https://assets.postman.com/postman-docs/v10/flows-tut-rep-stripe-deleted-v10.jpg)
    
2. Part two: Delete the contact from Brevo

    * In the middle **HTTP Request** block, select **Brevo > Contact management > Contacts > Get a contact's details**.
    * Select the **gdpr-delete-email** environment
    * For the `email` variable, add a **Get Variable** block and click **Customer Email**.
    * Connect this block's **Success** output to another **HTTP Request** block and select **Brevo > Contact management > Contacts > Delete a contact**. Also connect the middle **HTTP Request** block's **Success** output to the new **HTTP Request** block's **contact_id** input and select `body.id`
    
        ![Add Brevo requests](https://assets.postman.com/postman-docs/v10/flows-tut-rep-brevo-requests-v10.jpg)
    
    * Connect the **Delete a contact** block's **Success** output to a **Display** block. Rename the **Display** block `Contact deleted` and select **Boolean** from the dropdown list.
    * Connect a **Display** block to the **Get a contact's details** **HTTP Request** block's **Failure** output. Rename the **Display** block `Contact not found` and select **Boolean** from the dropdown list.
    
        ![Brevo contact deleted](https://assets.postman.com/postman-docs/v10/flows-tut-rep-brevo-deleted-v10.jpg)
    
3. Part three: Delete the contact from an internal system

    * In the bottom **HTTP Request** block, select **customer-list > customer/email**.
    * For the email variable, add a **Get Variable** block and click **Customer Email**.
    * Connect the **Success** output to an **HTTP Request** block and select **customer-list > customer/id**.
    * Also connect the **customer/email** **HTTP Request** block's **Success** output to the **id** input and select `body.id`.
    * Connect the **customer/id** **HTTP Request** block's **Success** output to a **Display** block. Rename the **Display** block `Contact deleted` and select **Boolean** from the dropdown list.
    * Connect the **customer/id** **HTTP Request** block's **Failure** output to a **Display** block. Rename the **Display** block `Contact not found` and select **Boolean** from the dropdown list.
    
        ![Internal contact deleted](https://assets.postman.com/postman-docs/v10/flows-tut-rep-internal-deleted-v10.jpg)
    

## Run the flow

Select **Run**. The flow finds and deletes the contact with the `test@email.com` email address on Brevo, Stripe, and the internal system. When the contact is deleted, the `Contact deleted` **Display** block shows **True**. If there is no contact with that email address, the `Contact not found` **Display** block shows **False**.