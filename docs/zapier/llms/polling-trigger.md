# Source: https://docs.zapier.com/platform/build/polling-trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add a polling trigger

> Set up your polling trigger in the Platform UI with the Settings, Input Designer and API Configuration tabs.

## Prerequisites

* Understanding of the [concept of deduplication](/platform/build/deduplication) and familiarity with how it is [explained to users](https://zapier.com/help/create/basics/data-deduplication-in-zaps)

## 1. Add the trigger settings

* Open the *Triggers* tab in Zapier's Platform UI and select **Add Trigger**.
* On the Settings page, specify the following:

– **Key**: A unique identifier for this trigger to be referenced inside Zapier. This is not shown to users. This cannot be edited once saved.

– **Name**: A human-friendly name for this trigger, typically with an adjective such as *New or Updated* followed by the name of the item that the trigger watches for inside your app. The title-case name is shown inside the Zap editor and on Zapier's app directory marketing pages.

– **Noun**: A single noun that describes what this trigger watches for, used by Zapier to auto-generate text in Zaps about your trigger.

– **Description**: A plain text sentence that describes what the trigger does and when it should be used. Shown inside the Zap editor and on Zapier's app directory marketing pages. Starts with the phrase “Triggers when”.

– **Visibility in Editor**: An option to select when this trigger will be shown. *Shown* is chosen by default. Choose `Hidden` if this trigger should not be shown to users. `Hidden` is usually selected when the trigger is not ready to be used in the integration, or for polling triggers that power [dynamic dropdown](/platform/build/add-fields#dynamic-dropdown) fields.

– **Directions** is used for [static webhooks](/platform/publish/integration-checks-reference#d017---static-hook-is-discouraged) only to describe how and where to copy-paste the static webhook URL for the trigger within your app. **Directions** will not show to users in other cases. Static webhooks are not permitted in public integrations.

* Click on the **Save and continue** button.

## 2. Complete the Input Designer

On the Input Designer page, add user [input fields](/platform/build/add-fields) needed by your API to watch for the triggering item.

Trigger input fields allow users to enter filters, tags, and other details to filter through new or updated data at the endpoint.

If no input data is needed for this trigger's endpoint, continue.

## 3. Set up the API Configuration

Platform UI selects a *Polling* trigger type by default.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=a7cd8f0c4cb9f6b8d593d5df97d62857" data-og-width="1508" width="1508" data-og-height="1085" height="1085" data-path="images/0f08230cffa8a3a568d4847e35e42d0c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=eee7455cecff64b51db475409cfa841e 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=572780f82dca320888e7bd2cda976264 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=350d740ee4cdb1ec4a75aea68f1ab1de 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=4110ffb8f44e99717392e12d1addf6a7 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=50f3ccd29403025f2866bfa7fe1e6d7c 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/0f08230cffa8a3a568d4847e35e42d0c.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5eb8723bbdcd194640e09c6124e51ba1 2500w" />
</Frame>

Enter your API URL in the *API Endpoint* field. If your API URL requires specific data in the URL path, enter the following text in the URL where your API expects that data, replacing `key` with the input field key containing the relevant input field you created in the previous step:

`{{bundle.inputData.key}}`

Otherwise, Zapier will automatically include any input field data with the API call as URL parameters (for GET requests), or in the request body as JSON (for POST requests).

If your API requires any additional data to return the new or updated items in the [expected response type](/platform/build/response-types) of an array sorted in reverse chronological order, add it using the *Show Options* button to expose more detailed request configuration. Alternatively select *Switch to Code Mode* to [further customize the API call](/platform/build/code-mode) in JavaScript code.

Only if you plan to use this trigger to power dynamic dropdown menus in other Zap steps (such as to find users, projects, folders, and other app data often used to create new items), and if your API call can paginate data, select *Support Paging* (see [more details on dropdowns](/platform/build/add-fields#dynamic-dropdown) below).

Once you've added your trigger settings, click *Save API Request & Continue*.

## 4. Test your API request

Configure test data to [test the polling trigger](/platform/build/test-triggers-actions).

## 5. Define your output

Define sample data and output fields following [the guide](/platform/build/sample-data).

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
