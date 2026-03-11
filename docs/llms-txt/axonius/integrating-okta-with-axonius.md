# Source: https://docs.axonius.com/docs/integrating-okta-with-axonius.md

# Integrating Okta with Axonius for Workflows

Before you add an Okta event to a Workflow the first time (or after the URL or Private Secure Key has changed in System Settings), you must do the following:

1. In Axonius:[Set up Axonius to receive hook events from Okta](#setting-up-axonius-to-receive-hook-events-from-okta).
2. In Okta:[Register the Axonius Okta Webhook URL with Okta and configure event hook parameters](#registering-axonius-custom-webhook-in-okta).
3. In Okta:[Verify and activate the event hook](#verifying-the-event-hook).
4. In Axonius:[Begin receiving ongoing event notifications](#okta-event-delivery-to-axonius).

The following sections describe how to integrate Okta with Axonius on both the Axonius and Okta sides.

## Setting Up Axonius to Receive Hook Events From Okta

Axonius supports setting up a Webhook URL at the Axonius destination to receive hook events from Okta.

The Okta event settings, including the Webhook URL, are configured in **System Settings> External Integrations> Workflow Events**, with **Okta** selected in the **Select Product** dropdown.

The **Workflows Events** dialog includes the following information for **Okta**:

* The URL of the Axonius Webhook that receives Okta hook events, with an adjacent Copy icon. This URL is predefined in the system.
* **Private Secure Key (X-API-Key)** - This field holds the secure key string value to be compared to the value in the custom header of each HTTP Post request of Okta events sent to Axonius, provided that a custom header is configured in Okta. It must be at least 16 characters long and contain only lowercase letters (a-z) and at least one number (0-9).
  This secure key value is used for extra authorization security on both the Okta and Axonius sides. On the Okta side it is used to verify that its hook events are being sent to the Axonius webhook URL and on the Axonius side to verify that hook events arriving at the Axonius webhook URL are from Okta. The hook event is accepted at the Axonius webhook only if the custom header in the HTTP Post request contains this secure key value.

## Registering Axonius Custom Webhook in Okta

Before Okta can begin sending events to Axonius, you must register in Okta:

* The Okta event types that you want to send  to Axonius. For example, *user.lifecycle.create*, *group.user\_membership.add*
* The destination of the Okta events, i.e., the Axonius webhook URL for Okta.
* The value of the **X-API-Key** private secure key.

You can copy the values for the Axonius webhook URL and **X-API-Key** from **System Settings> External Integrations> Workflow Events> Okta**.

<Callout icon="📘" theme="info">
  Note

  You need to configure the Axonius Custom webhook URL and the private secure key value in Okta once only, unless their values change.
</Callout>

Once this information is configured in Okta and the connection is verified, the Okta hook is activated, and the Okta app begins sending hook events to the Axonius webhook URL.

Okta sends each event in an HTTPS POST request with a custom header. You can add a field **X-API-Key** to the custom header and set it with the value that is configured for that key in the Axonius System Settings. Then, when Okta sends the event to the Axonius webhook URL, it checks if the **X-API-Key** value in its custom header matches the value configured for the key in Axonius System Settings, and similarly, Axonius accepts the event only if the values match. This provides enhanced security in the communication channel between Okta and Axonius.

**To register the Axonius Custom webhook in Okta**

1. Sign in to Okta org: [https://axonius.okta.com](https://axonius.okta.com) using your Okta account.

2. From the Admin Console left menu, navigate to **Workflow `>` Event Hooks**.

3. Click **Create Event Hook**. The **Add Event Hook Endpoint** dialog box opens.

4. In **Name**, enter a descriptive name for the event hook.

5. In **URL**, paste the [Axonius Okta Webhook URL](#setting-up-axonius-to-receive-hook-events-from-okta). This is where the event webhook sends the request.

6. For enhanced security and to secure the communication channel between Okta and Axonius, under **Custom header fields**, click **+ Add Field**, and then enter values for the new field:
   * In **Field Name**, type **X-API-Key**. This name, taken  from the Axonius Okta Webhook configuration screen (above), is the name of the custom HTTP header to be included in each POST request that the event sends.
   * In **Value**, type the same text string value of the **Private Secure Key (X-API-Key)** setting from the Axonius Okta Webhook configuration screen (above). This value serves as an API access key for Axonius and Okta provides it in every POST request, allowing Axonius to check for its presence as a security measure.

7. Click inside the **Subscribe to events** text box to show the list of events, and select the Okta event types you want to monitor and use in Workflows (for example, *device.lifecycle.deactivate*, *user.lifecycle.create*, *group.user\_membership.add*).

8. Click **Save & Continue**.

## Verifying the Event Hook

After you create or modify the Axonius webhook URL in Okta and save it, Okta must verify the Axonius event hook URL before it becomes activated and begins sending events of registered event types.\
This one-time verification works as follows:

1. Okta passes a verification value to Axonius.
2. Axonius returns the verification value to Okta.
3. Okta verifies that the values are the same.
4. Following successful verification, the newly created hook URL is listed as Active on the Event Hooks page.
5. After a short wait period, the Okta hook begins sending ongoing events to the Axonius webhook URL for Okta.

**To verify the event hook**

1. From the **Verify Endpoint Ownership** window that opens when you click **Save & Continue**, click **Verify**.
   Alternatively, verify the event hook at a later time by clicking the **Actions** dropdown menu of any unverified event webhook, and click **Verify**.

<Callout icon="📘" theme="info">
  Note

  After it is verified and activated, it may take several minutes before events are sent to the event hook.
</Callout>

For full instructions, including optional settings, see [Create an event hook](https://help.okta.com/en-us/content/topics/automation-hooks/add-event-hooks.htm?cshid=ext-add-event-hooks).

## Okta Event Delivery to Axonius

When an event monitored by the Okta hook (for example, *user.lifecycle.create*) occurs, the following describes how Okta sends the event to Axonius:

1. Okta hook is automatically triggered and then sends an HTTPS POST request to the dedicated Axonius Webhook URL.
2. If the secure key is configured, the Axonius webhook verifies that the secure key value in the **X-API-Key** field in the custom header matches the one configured in **Axonius System Settings> Workflow Events> Okta**,  and if yes, accepts and acknowledges Okta's POST request with either a 200 (Success) or 204 (Success no content) return code.
   * If there is a timeout or an error response from Axonius during the attempts, one request retry is sent. If a successful response isn't received after that, an HTTP 400 error is returned with more information about the failure.