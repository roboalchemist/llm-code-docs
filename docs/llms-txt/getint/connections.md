# Source: https://docs.getint.io/getintio-platform/connections.md

# Connections

A connection is the link between getint and an external platform, such as Jira, HubSpot, Salesforce, or another supported system. It defines how getint authenticates with that platform and enables data to flow between the two systems. Each connection includes configuration details, permissions, and credentials that allow integrations to run smoothly and securely.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FK09WCDwms9SDMgKitqQk%2FSeeing%20existing%20connections.png?alt=media&#x26;token=6a52712c-70bb-4059-a158-7f2e9578b23c" alt=""><figcaption></figcaption></figure>

### Accessing Connection Views

* **Navigate to Workflows**: Begin by accessing the "Workflows (lightning bold icon)" section within the Getint app.
* **Click Connections**: Navigate to "Connections" to access a comprehensive overview of your connections.
* **Open the Actions**: Click the 3-dot button located on the right edge of the screen to view all options that can be modified from the existing connections.
* **Available options**: The list includes several actions, which are Debug Requests, Delete, Edit, and Export.

### What Each Action Does

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F1Rd6Bi05Jp4BxnhKxGUV%2FWhat%20each%20action%20does.png?alt=media&#x26;token=546bbf66-dd40-4c5b-be69-9424dacd06d5" alt=""><figcaption></figcaption></figure>

#### Debug Requests

In Getint, "debug requests" refers to the ability to view and analyze the raw communication between Getint and the connected platform (e.g., Jira, HubSpot, Salesforce). It's essentially a troubleshooting tool that helps you understand:

* What data is being sent or received during an integration sync.
* Whether an API call failed and why.
* How is the integration behaving internally when something doesn't work as expected.

When enabled, debug requests typically show request/response payloads, status codes, and error messages. This makes it easier to pinpoint issues such as authentication failures, missing fields, permission problems, or unexpected API responses.

Teams usually use this feature when:

* An integration isn't syncing correctly.
* A field mapping isn't behaving as expected.
* They need to confirm what Getint is sending to or receiving from the external system.

#### **Delete**

Delete permanently removes the connection from getint, including all associated settings and authorization details.

Once deleted, the connection can no longer be used in any integrations until it is recreated and re‑authorized.

#### Edit

Edit allows you to update the connection's configuration, such as changing its name, adjusting settings, or modifying authentication details.

This action lets you maintain or correct the connection without deleting or recreating it.

#### Export

Export lets you download the connection’s configuration details so you can review or reuse them outside of getint.

This is typically used for documentation, troubleshooting, or replicating a similar setup in another environment.

### Connection Details

See essential information such as the API Token, App access creation, associated email, and the App and URL name.

#### Understanding Access Permissions

It's crucial to grasp the available access permissions associated with each connection. These permissions determine the level of access users have:

* "View" permission grants read-only access. This is also the Default permission for all New connections, not allowing others to use or modify it.
* "Use" permission allows users to interact with the connection, incorporate it into their integrations, and make changes to those integrations.
* "Edit" permission allows users to make modifications to the connection.

#### Modifications

You can make changes to the connection, such as modifying an expired token, adding further access, modifying the URL, or changing the associated email.

Changing the URL is likely to affect integrations, as it alters the endpoint through which data is transmitted. Similarly, updating credentials, such as switching accounts, can disrupt integrations if the new user lacks access to the integrated projects.

**Team access:**

* Click the three dots, then select "Edit." A sidebar will also appear. You can change the name of the connection.
* In the dropdown menu, select the view you want to give for this connection.

{% embed url="<https://www.loom.com/share/f0dfed8884a542f5852f7812b64f841e>" %}

**Changing the Token or Email:**

* Click the three dots, then select "Edit." A new sidebar will appear. If necessary, modify the URL.
* Select "Next." You can then see the options to edit the connection name, the email address, the personal token, and the type of access the team will have to that connection. Select your preferred options and select update.

{% embed url="<https://www.loom.com/share/b51b27e0888c4a3aaf75e34cc9912c13>" %}

#### Importing and Exporting Connections

Now, you have the option to "Import" and "Export" your Connection. This functionality proves invaluable when you need to transfer the connection to a new Getint instance. For instance, it's handy when transitioning from Cloud to On-premise or from Server to Cloud environments.

**Exporting the Connection:**

* Go to Workflows, select Connection, and find the one you want to export. Select the 3 dots on the right side and "Export." Create an encryption key, which will work like a password when importing it.
* Copy the script that will appear on the next screen and take note of the encryption key created.

{% embed url="<https://www.loom.com/share/0bdb7a797bca4adb990c7316d806a783>" %}

**Importing the Connection:**

* In the instance where you would like the connection created, go to "Workflows," select connection, and "Import" at the top of the page.
* Give the connection a name and paste the script copied when exporting the connection.
* Write the encryption key and select "Import."

{% embed url="<https://www.loom.com/share/0b57c4ba5c134d2bbd2242fcdd3feaa0>" %}

If you need help with exporting a connection or run into any issues, please contact our support team through the [Help Center](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
