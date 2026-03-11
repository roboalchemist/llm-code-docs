# Source: https://docs.base44.com/Integrations/Zapier-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Zapier

> Automate your Base44 app by connecting it to Zapier, so actions in your app can trigger tasks in thousands of other apps like sending calendar invites, updating spreadsheets, or posting messages.

<Info>
  **Note:** Zapier integrations require the **Builder** plan or higher. If you’re on the Free tier, you’ll need to upgrade before proceeding. You will also need a premium Zapier account to use webhooks.
</Info>

# **Step‑by‑step setup**

This integration can be added in two ways:

<CardGroup cols={2}>
  <Card icon="sparkle" href="https://docs.base44.com/Integrations/Zapier-integration#part-1%3A-ready-made-integration-for-new-apps" title="Option A: Ready-made integration (preferred)">
    * Choose this path if you are starting a new app from scratch.
  </Card>

  <Card icon="bolt" href="https://docs.base44.com/Integrations/Zapier-integration#part-2%3A-instant-integration-add-zapier-to-an-existing-app" title="Option B: Instant integration">
    * Choose this path if you are already in the midst of building and would like to integrate Zapier into an existing app.
  </Card>
</CardGroup>

## Part 1: Ready-made integration (for new apps)

<Steps>
  <Step title="Create a Zap and catch hook">
    * Sign in to Zapier and click **Create Zap**.

      <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/CreateZap.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=0927353caa6b30a75f6262160f061c51" alt="Create Zap Pn" width="1881" height="785" data-path="images/CreateZap.png" />
    * Choose **Webhooks by Zapier → Catch Hook** as the trigger.

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/Webhooks.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=0542c15e6407e32dbf8a3bd38bfd8b76" alt="Webhooks Pn" width="1858" height="994" data-path="images/Webhooks.png" />
    * Leave the **Pick off a Child Key** field blank to capture the full payload.

      <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/CatchHook.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=5f0c377dfdccda8942bbaeb18b3d50a7" alt="Catch Hook Pn" width="1903" height="989" data-path="images/CatchHook.png" />
    * Continue and copy the webhook URL.
  </Step>

  <Step title="Start a new Base44 app and add Zapier from the catalog">
    * In a new browser tab, go to Base44 and click **Integrations**.

      <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />
    * Find **Zapier** and click **Use this integration**.

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/ZapierCatalog.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=ba5d4610c0e1999c04cc6b636d88e588" alt="Zapier Catalog Pn" width="1879" height="977" data-path="images/ZapierCatalog.png" />

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/UseZapier.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=93708cd4b0175911daa0375417676312" alt="Use Zapier Pn" width="1894" height="987" data-path="images/UseZapier.png" />
    * When prompted, paste the webhook URL into the **ZAPIER\_WEBHOOK\_URL** field.

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/WebhookURL.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=c05fe3d323b4fa4bd611e125847408db" alt="Webhook URL Pn" width="1876" height="914" data-path="images/WebhookURL.png" />
    * Describe your app in natural language. For example: \
      `I am a therapist. Build an app to manage my schedule and let my clients book meeting.`
  </Step>

  <Step title="Book one test meeting">
    * After the app is created, open the app preview and book a test meeting:
      * Choose a date and time a few minutes in the future.
      * Use your real email.
      * Submit once and wait 2 to 5 seconds.

    This sends a sample payload to your Zap so Zapier can load real fields during setup.

    #### **Data to send from Base44 to Zapier**

    Make sure the payload is detailed so Zap can create the right calendar event. Include and save these in your Meetings collection:

    * **start\_iso**: an ISO 8601 datetime that combines the chosen date and time.

      <Tip>
        Example: new Date(\$dateT\$time:00).toISOString()
      </Tip>
    * **end\_iso** or **duration\_minutes**: either send an explicit end time as ISO, or send duration\_minutes so Zapier can compute +30m in the action
    * **time\_zone**: your app or user time zone, preferably an IANA name like Asia/Jerusalem; if you cannot provide a name, include the numeric offset
    * **meeting\_id**: a stable id to avoid duplicates, for example \$client\_email|\$start\_iso
    * **client\_name**, **client\_email,** **notes**

    Saving these fields ensures you can audit bookings and Zapier maps the event correctly every time.
  </Step>

  <Step title="Tell Zapier to fetch the sample">
    * Back in Zapier, go to the Test tab of your trigger.
    * Click **Find new records**, select the sample request your app sent, and continue.
    * If nothing appears, submit another test meeting and click **Find new records** again.
  </Step>

  <Step title="Create the Google Calendar event">
    * Add an action: **Google Calendar → Create Detailed Event**.
    * Map the fields from your sample to the event fields:
      * **Summary:** `Meeting with client_name`
      * **Description:** `notes`
      * **Start Date & Time:** `start_iso`
      * **End Date & Time:** `start_iso + 30m` (or compute using duration\_minutes)
      * **Guests:** `client_email`
      * **Time Zone:** choose your calendar’s zone
    * Click **Test** to ensure the event appears and that an invite is sent.
  </Step>

  <Step title="Publish your Zap">
    Click **Publish** to turn the Zap on. From now on, each new meeting in your app will automatically create a calendar event.
  </Step>
</Steps>

***

## Part 2: Instant integration (add Zapier to an existing app)

Use this method if your app already exists and you want to connect Zapier mid‑build.

<Steps>
  <Step stepNumber={1} title="Select your existing app">
    * Here's the prompt that we typed out in the AI chat to build our sample app: :

      `I am a therapist. Build an app to manage my schedule and let my clients book meeting.`
  </Step>

  <Step stepNumber={2} title="Ask Base44 to add Zapier">
    * In the chat window of your app, say something like:

      `I want to connect my app to Zapier. Please make an integration that sends booking data to Zapier from the backend only. Never call Zapier from the browser.`
    * Keep the chat open while you complete the next step.
  </Step>

  <Step stepNumber={3} title="Create the webhook URL in Zapier">
    * In Zapier, **create a new Zap** with **Webhooks by Zapier → Catch Hook** and copy the webhook URL (just like in Part 1).

      <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/CreateZap.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=0927353caa6b30a75f6262160f061c51" alt="Create Zap Pn" width="1881" height="785" data-path="images/CreateZap.png" />

      <img src="https://mintcdn.com/base44/x7uieDiv9xNLARBF/images/Webhooks.png?fit=max&auto=format&n=x7uieDiv9xNLARBF&q=85&s=0542c15e6407e32dbf8a3bd38bfd8b76" alt="Webhooks Pn" width="1858" height="994" data-path="images/Webhooks.png" />

      <img src="https://mintcdn.com/base44/UsrMcs9B3MEl2R91/images/CatchHook.png?fit=max&auto=format&n=UsrMcs9B3MEl2R91&q=85&s=5f0c377dfdccda8942bbaeb18b3d50a7" alt="Catch Hook Pn" width="1903" height="989" data-path="images/CatchHook.png" />
    * Paste this URL into the Base44 chat when prompted. The integration will save it securely and wire up a backend route to post booking data to Zapier.
  </Step>

  <Step stepNumber={4} title="Create one sample meeting">
    * After the app is created, open the app preview and book a test meeting:
      * Choose a date and time a few minutes in the future.
      * Use your real email.
      * Submit once and wait 2 to 5 seconds.

    This sends a sample payload to your Zap so Zapier can load real fields during setup.

    #### **Data to send from Base44 to Zapier**

    Make sure the payload is detailed so Zap can create the right calendar event. Include and save these in your Meetings collection:

    * **start\_iso**: an ISO 8601 datetime that combines the chosen date and time.

      <Tip>
        Example: new Date(\$dateT\$time:00).toISOString()
      </Tip>
    * **end\_iso** or **duration\_minutes**: either send an explicit end time as ISO, or send duration\_minutes so Zapier can compute +30m in the action
    * **time\_zone**: your app or user time zone, preferably an IANA name like Asia/Jerusalem; if you cannot provide a name, include the numeric offset
    * **meeting\_id**: a stable id to avoid duplicates, for example \$client\_email|\$start\_iso
    * **client\_name**, **client\_email,** **notes**

    Saving these fields ensures you can audit bookings and Zapier maps the event correctly every time.
  </Step>

  <Step stepNumber={5} title="Tell Zapier to fetch the sample">
    * In your Zap trigger, go to the **Test** tab and click **Find new records**.
    * Select the latest request and continue. If nothing appears, submit another test, then click **Find new records** again.
  </Step>

  <Step stepNumber={6} title="Create the Google Calendar event">
    * Add an action: **Google Calendar → Create Detailed Event**.
    * Map the fields from your sample to the event fields:
      * **Summary:** `Meeting with client_name`
      * **Description:** `notes`
      * **Start Date & Time:** `start_iso`
      * **End Date & Time:** `start_iso + 30m` (or compute using duration\_minutes)
      * **Guests:** `client_email`
      * **Time Zone:** choose your calendar’s zone
    * Click **Test** to ensure the event appears and that an invite is sent.
  </Step>

  <Step stepNumber={7} title="Publish your Zap">
    * Turn on the Zap. New bookings will now trigger calendar events automatically.
  </Step>
</Steps>

***

# **Troubleshooting**

* **No sample in Zapier:** Make sure you’ve booked one test meeting before testing.
* **401 or CORS errors:** Only post to Zapier from the backend; never call Zapier from the browser.
* **Wrong times:** Ensure you combine the date and time into a proper ISO datetime (start\_iso) and set the correct time zone when creating the calendar event.
* **Zap not running:** Confirm that you clicked **Publish** to turn the Zap on.

***

## **Quick checklist**

Use this list to make sure you haven’t missed anything:

* Catch Hook created with **Pick off a Child Key** left blank
* Webhook URL saved as **ZAPIER\_WEBHOOK\_URL** in Base44
* Builder tier or higher
* One sample meeting booked before testing
* Google Calendar action mapped and tested
* Zap published and turned on

***


Built with [Mintlify](https://mintlify.com).