# Source: https://docs.base44.com/documentation/managing-app-data/testing-your-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing your data

> Test your data in a safe environment before changing your live production records

Test your data using a safe database where you can try changes without affecting your live production data. After you turn on the **Test Data** toggle in **App Settings**, you can switch between production and test data, so you can see how your app behaves with test records before you use them in production.

For example, if you are building a bookings app, you can use test data to create fake services and test bookings, cancellations, and reminders without filling your real schedule. You can check that your flows, prices, and emails look right with test data, and keep your production calendar for real clients only.

<Warning>
  **Important:**

  * This feature is available on the **Builder** plan and higher.
  * Your published app always uses production data. Turning on testing mode only affects data in the dashboard and in preview.
</Warning>

***

## Turning on testing mode

Turn on the **Test Data** setting in **App Settings** to create a separate test database for your app and access the testing mode in preview.

<Note>
  **Note:** When you turn on Test Data, it creates a new, empty database. Existing production data is not copied to the test database.
</Note>

**To turn on the testing mode:**

1. Click **Dashboard** in your app editor.
2. Click **Settings**.
3. Click **App Settings**.
4. Turn on the **Test Data** toggle.

<Frame caption="Turning on Test Data in App Settings">
    <img src="https://mintcdn.com/base44/4dqNl8YqGbHrLXZT/images/testdatatoggle.png?fit=max&auto=format&n=4dqNl8YqGbHrLXZT&q=85&s=27125e7668bc1b1a0d701fd359dd5bf6" alt="Turning on Test Data in App Settings" width="2432" height="830" data-path="images/testdatatoggle.png" />
</Frame>

***

## Accessing your test data

Go to the **Data** tab to view and edit records in your tables and choose whether you are working with production or test data. You can keep production as your source of truth while you experiment with structure or content in the test environment.

<Frame caption="Switching between production and test data in the Data tab">
    <img src="https://mintcdn.com/base44/4k2CfxhN_xrEuFeU/images/prodandtestdata.png?fit=max&auto=format&n=4k2CfxhN_xrEuFeU&q=85&s=088110dda3f621bc5fa00bb4e6c62588" alt="Switching between production and test data in the Data tab" width="2428" height="906" data-path="images/prodandtestdata.png" />
</Frame>

**To access your test data:**

1. Click **Dashboard** in your app editor.
2. Click **Data**.
3. Click the data table you want to work with on the left menu.
4. Click **Test** at the top.
5. Add, edit, or delete records.

<Tip>
  **Tip:** You can also ask the AI chat to add test data for you.
</Tip>

<Note>
  **Notes:**

  * Changes you make with **Production** selected affect only your production data.
  * Changes you make with **Test** selected affect only your test data.
  * Production and test data are completely separate. Updating one does not update the other.
</Note>

***

## Testing your app in preview

Use preview mode to see how your app behaves with real interactions while keeping your live data safe. At the top of your app preview, you can switch between production and testing mode so you control where preview reads and writes data.

If you make changes in the testing mode, you can go to the **Data** tab and select **Test** to see the records created.

<Frame caption="Turning on test data mode in the app preview">
    <img src="https://mintcdn.com/base44/4dqNl8YqGbHrLXZT/images/turnontestdata.png?fit=max&auto=format&n=4dqNl8YqGbHrLXZT&q=85&s=0dac94b0badf564a449fe08742dc658b" alt="Turning on test data mode in the app preview" width="2436" height="1474" data-path="images/turnontestdata.png" />
</Frame>

**To preview your app with testing mode:**

1. Click **Preview** in your app editor.
2. At the top of the preview, click the **Turn on test data** icon <Icon icon="database" />.
3. Use your preview as normal to create, update, or delete data.

<Note>
  **Notes:**

  * When testing mode is turned on in preview, all data reads and writes go to your test data.
  * When testing mode is turned off in preview, all data reads and writes go to your production data.
  * Turning the test mode on and off in preview does not affect which environment your published app uses. The live app always uses production data.
</Note>

***

## Sharing a testing link to your app

Share a testing link so teammates or clients can try your app with test data and unpublished changes. Anyone who opens the testing link interacts with your test database only, so your live app and production records stay safe.

**To share a testing link:**

1. Click **Share** <Icon icon="share-nodes" /> at the top right of your app editor.
2. Click **Copy Testing Link**.
3. Paste the link where you want to share it, such as in an email or chat.

<Frame caption="Copying a testing link to your app">
  <img src="https://mintcdn.com/base44/XJsK-p2PZ_k77tzf/images/copytestinglink.png?fit=max&auto=format&n=XJsK-p2PZ_k77tzf&q=85&s=58c26326da89e1da9ed0f20152ebe95a" alt="Copying a testing link to your app" title="Copying a testing link to your app" className="mx-auto" style={{ width:"88%" }} width="710" height="370" data-path="images/copytestinglink.png" />
</Frame>

<Note>
  **Notes:**

  * The testing link is available only after you turn on **Test Data** in **App Settings**.
  * People who open the testing link see your unpublished changes and interact with test data only. The link does not change your live app or production records.
</Note>

***

## FAQs

Click a question below to learn more about testing your data.

<AccordionGroup>
  <Accordion title="Why is my test database empty?">
    When you turn on testing mode, your test database starts empty. Records only appear after you add or edit the test data in the Data tab, or you create data in preview mode with testing mode turned on.
  </Accordion>

  <Accordion title="Can I use the same data in both production and testing mode?">
    There is no automatic sync between production and test data in either direction. If you want a record to exist in both environments, create or import it separately.
  </Accordion>

  <Accordion title="Can I turn off testing mode?">
    You can go back to **Settings** and **App Settings** at any time and turn off the **Test Data** toggle. When you turn it off, the test database is hidden from the Data tab, but existing test data is kept in case you turn it back on later.
  </Accordion>

  <Accordion title="Does the AI chat use production or test data?">
    When you use the AI chat to add or update data, it works with production data by default. However, you can also ask it to add, edit or delete test data:

        <img src="https://mintcdn.com/base44/BgK_OqaRJVORRqJx/images/testdatachat.png?fit=max&auto=format&n=BgK_OqaRJVORRqJx&q=85&s=87d9674193d3e98d3eedac75ba283757" alt="Testdatachat" width="3448" height="1912" data-path="images/testdatachat.png" />
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).