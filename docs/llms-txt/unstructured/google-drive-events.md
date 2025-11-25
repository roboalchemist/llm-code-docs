# Source: https://docs.unstructured.io/examplecode/tools/google-drive-events.md

# Google Drive event triggers

You can use Google Drive events, such as adding new files to—or updating existing files in—Google Drive shared folders or shared drives, to automatically run Unstructured ETL+ workflows
that rely on those folders or drives as sources. This enables a no-touch approach to having Unstructured automatically process new and updated files in Google Drive as they are added or updated.

This example shows how to automate this process by adding a custom [Google Apps Script](https://developers.google.com/apps-script) project in your Google account. This project runs
a script on a regular time interval. This script automatically checks for new or updated files within the specified Google Drive shared folder or shared drive. If the script
detects at least one new or updated file, it then calls the [Unstructured Workflow Endpoint](/api-reference/workflow/overview) to automatically run the
specified corresponding Unstructured ETL+ workflow in your Unstructured account.

<Note>
  This example uses a custom Google Apps Script that you create and maintain.
  Any issues with file detection, timing, or script execution could be related to your custom script,
  rather than with Unstructured. If you are getting unexpected or no results, be sure to check your custom
  script's execution logs first for any informational and error messages.
</Note>

## Requirements

To use this example, you will need the following:

* An Unstructured account, and an Unstructured API key for your account, as follows:

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

* The Unstructured Workflow Endpoint URL for your account, as follows:

  1. In the Unstructured UI, click **API Keys** on the sidebar.<br />
  2. Note the value of the **Unstructured Workflow Endpoint** field.

* A Google Drive source connector in your Unstructured account. [Learn how](/ui/sources/google-drive).

* Some available [destination connector](/ui/destinations/overview) in your Unstructured account.

* A workflow that uses the preceding source and destination connectors. [Learn how](/ui/workflows).

## Step 1: Create the Google Apps Script project

1. Sign in to your Google account.
2. Go to [http://script.google.com/](http://script.google.com/).
3. Click **+ New project**.
4. Click the new project's default name (such as **Untitled project**), and change it to something more descriptive, such as **Unstructured ETL Scripts**.

## Step 2: Add the script

1. With the project still open, on the sidebar, click the **\< >** (**Editor**) icon.

2. In the **Files** tab, click **Code.gs**.

3. Replace the contents of the `Code.gs` file with the following code instead:

   ```javascript  theme={null}
   function checkForNewOrUpdatedFiles() {
     const folder = DriveApp.getFolderById(FOLDER_ID);
     const files = folder.getFiles();
     const now = new Date();
     const thresholdMillis = 5 * 60 * 1000; // 5 minutes (adjust as needed).
     
     while (files.hasNext()) {
       const file = files.next();
       const created = file.getDateCreated();
       const lastUpdated = file.getLastUpdated();
       const fileName = file.getName();

       // Calculate time differences.
       const millisSinceCreated = now - created;
       const createdWithinThreshold = millisSinceCreated < thresholdMillis;
       const millisSinceUpdated = now - lastUpdated;
       const updatedWithinThreshold = millisSinceUpdated < thresholdMillis;

       // Log file details and calculations.
       console.log('File Name:                       ' + fileName);
       console.log('Created:                         ' + created);
       console.log('Last updated:                    ' + lastUpdated);
       console.log('Milliseconds since created:      ' + millisSinceCreated);
       console.log('Milliseconds since last updated: ' + millisSinceUpdated);
       console.log('Created within threshold of ' + thresholdMillis + ' milliseconds? ' + createdWithinThreshold);
       console.log('Updated within threshold of ' + thresholdMillis + ' milliseconds? ' + updatedWithinThreshold);
       console.log('-----')

       // If at least one file was created or updated within the last 5 minutes...
       if ((createdWithinThreshold) || (updatedWithinThreshold)) {
         // ...then make the HTTP POST request.
         UrlFetchApp.fetch(UNSTRUCTURED_API_URL, {
           method: 'post',
           headers: {
             'accept': 'application/json',
             'unstructured-api-key': UNSTRUCTURED_API_KEY
           }
         });
         // Then stop the script after the first fetch (no need to check any more files).
         console.log('At least one file created or updated within threshold of ' + thresholdMillis + ' milliseconds.')
         console.log('Unstructured workflow request sent to ' + UNSTRUCTURED_API_URL)
         return;
       }
     }
     console.log('No files created or updated within threshold of ' + thresholdMillis + ' milliseconds. No Unstructured workflow request sent.')
   }
   ```

4. Click the **Save project to Drive** button.

## Step 3: Customize the script for your workflow

1. With the project still open, on the **Files** tab, click the **Add a file** button, and then click **Script**.

2. Name the new file `Constants`. The `.gs` extension is added automatically.

3. Replace the contents of the `Constants.gs` file with the following code instead:

   ```javascript  theme={null}
   const FOLDER_ID = '<folder-id>';
   const UNSTRUCTURED_API_URL = '<unstructured-api-url>' + '/workflows/<workflow-id>/run';
   const UNSTRUCTURED_API_KEY = '<unstructured-api-key>';
   ```

   Replace the following placeholders:

   * Replace `<folder-id>` with the ID of your Google Drive shared folder or shared drive. This is the same ID that you specified
     when you created your Google Drive source connector in your Unstructured account.
   * Replace `<unstructured-api-url>` with your Unstructured API URL value.
   * Replace `<workflow-id>` with the ID of your Unstructured workflow.
   * Replace `<unstructured-api-key>` with your Unstructured API key value.

4. Click the disk (**Save project to Drive**) icon.

## Step 4: Create the script trigger

1. With the project still open, on the sidebar, click the alarm clock (**Triggers**) icon.

2. Click the **+ Add Trigger** button.

3. Set the following values:

   * For **Choose which function to run**, select `checkForNewOrUpdatedFiles`.

   * For **Choose which deployment should run**, select **Head**.

   * For **Select event source**, select **Time-driven**.

   * For **Select type of time based trigger**, select **Minutes timer**.

   * For **Select minute interval**, select **Every 5 minutes**.

     <Note>
       If you change **Minutes timer** or **Every 5 minutes** to a different interval, you should also go back and change the number `5` in the following
       line of code in the `checkForNewOrUpdatedFiles` function. Change the number `5` to the number of minutes that correspond to the alternate interval you
       selected:

       ```javascript  theme={null}
       const thresholdMillis = 5 * 60 * 1000;
       ```
     </Note>

   * For **Failure notification settings**, select an interval such as immediately, hourly, or daily.

4. Click **Save**.

## Step 5: View trigger results

1. With the project still open, on the sidebar, click the three lines (**Executions**) icon.

2. As soon as the first script execution completes, you should see a corresponding message appear in the **Executions** list. If the **Status** column shows
   **Completed**, then keep going with this procedure.

   If the **Status** column shows **Failed**, expand the message to
   get any details about the failure. Fix the failure, and then wait for the next script execution to complete.

3. When the **Status** column shows **Completed** then, in your Unstructured account, click **Jobs** on the sidebar to see if a new job
   is running for that worklow.

   If no new job is running for that workflow, then add at least one new file to—or update at least one existing file in—the Google Drive shared folder or shared drive,
   within 5 minutes of the next script execution. After the next script execution, check the **Jobs** list again.

## Step 6 (Optional): Delete the trigger

1. To stop the script from automatically executing on a regular basis, with the project still open, on the sidebar, click the alarm clock (**Triggers**) icon.
2. Rest your mouse pointer on the trigger you created in Step 4.
3. Click the ellipsis (three dots) icon, and then click **Delete trigger**.
