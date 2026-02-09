# Source: https://docs.replit.com/getting-started/quickstarts/object-storage-javascript.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage App Storage in JavaScript

> Learn how to use the JavaScript App Storage client library to manage files from your Replit App.

This guide demonstrates how to use the JavaScript client library to upload, list, download, and delete files in your App Storage bucket.

<Note>
  This client library, written in TypeScript, can be used for projects that use JavaScript runtimes such as Bun, Deno, and Node.js 14 and later.
</Note>

## Create a TypeScript Replit App

1. Select <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a6613ac9b303fa6dea65e5cf08ddca06" alt="plus sign" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/create-app-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0f0aa42a2a63cca6629fe393ffb100e4 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e6cce9e17a54ec2279d57d255e5233ba 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6a6f30d08c7ab4811ba927af66ca7311 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f7249d48a50a7db0713ea3f92f4c422f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f2a12316d646b72674a837cbe70a10f8 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6cc3b1f288cf5086a84aadaa9b1d4fba 2500w" /> **Create App** from the home screen.
2. Navigate to the **Choose a Template** tab.
3. Type "TypeScript" in the template search field and select it as shown below:
   <Frame>
     <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=20d5c2a7d84cafe0bbcb2488abad6623" alt="TypeScript template selection screen" data-og-width="2590" width="2590" data-og-height="1064" height="1064" data-path="images/tutorials/typescript-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2009d52e7c62428dfbdeaac67d4c76b7 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4688223d56cbd924ebe5e0d5fa307d33 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5c9e52fee4cf2b0f91e77d43cfe7f73d 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=0b95cc7fc800d73e2fa5eddf7bc572b2 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c306db4a9b98697c639b88bc08da4fcc 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/typescript-template.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d3daef19ef4d0b3cbdee842e5fecde50 2500w" />
   </Frame>
4. Select <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a6613ac9b303fa6dea65e5cf08ddca06" alt="plus sign" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/create-app-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0f0aa42a2a63cca6629fe393ffb100e4 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e6cce9e17a54ec2279d57d255e5233ba 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6a6f30d08c7ab4811ba927af66ca7311 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f7249d48a50a7db0713ea3f92f4c422f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f2a12316d646b72674a837cbe70a10f8 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6cc3b1f288cf5086a84aadaa9b1d4fba 2500w" /> **Create App**.

## Install the official client library

To install the client library, follow the one-click setup or package manager instructions below.

<Tabs>
  <Tab title="One-click setup">
    <Steps>
      <Step title="Access the App Storage tool">
        1. Navigate to the **App Storage** tab.
        2. Select the <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=aa97c1d6b9eae7dfa4af01802636a8a5" alt="angled brackets icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/angled-brackets.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=27b4cca399aa3b3514339fe68a009a48 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=550894bc46ebe65b7d45c4d53f2a9b68 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4743dfbd26844b1b4482a41e40b79f66 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=84f1640fb44502b77f4db2a553341bef 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=eeb65fe53c551e5a3f2358c28dff9524 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/angled-brackets.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=d2661b0703d206906cd198357bd20efd 2500w" /> **Commands** view in the **App Storage** tab.

        The installation screen should resemble the following screenshot:

        <Frame>
          <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ea700a62d5ea5818372343210d0e832c" alt="screenshot of App Storage dependencies installation" data-og-width="2428" width="2428" data-og-height="648" height="648" data-path="images/tutorials/install-javascript-object-storage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=47cc9c9a9f0d774712bb628565b8acd1 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1f99137786a0d184e19a935c4b37eb13 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=0decdb409f172102fbbe482e8e24bc47 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7fc303c714863c866335d138d637f7b9 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3acb277fd457db01ebb22a99d6bb6e30 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/install-javascript-object-storage.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8148259630bfa71d115708487eec6fa2 2500w" />
        </Frame>
      </Step>

      <Step title="Install the dependencies">
        1. Select "JavaScript" from the programming language dropdown on the top left.
        2. Select **Install @replit/object-storage package**.
        3. When completed, the button text should read **Package installed**.
      </Step>
    </Steps>
  </Tab>

  <Tab title="npm">
    Use this option if your Replit App uses Node Package Manager (`npm`) to manage its dependencies.

    Open the **Shell** tool in your workspace and enter the following command:

    ```sh  theme={null}
    npm install @replit/object-storage
    ```
  </Tab>

  <Tab title="yarn">
    Use this option if your Replit App uses `yarn` to manage its dependencies.

    Open the **Shell** tool in your workspace and enter the following command:

    ```sh  theme={null}
    yarn add @replit/object-storage
    ```
  </Tab>
</Tabs>

## Create a bucket

Before storing files, you must create a bucket. Follow the steps below to create a new bucket:

1. Navigate to the **App Storage** tool
2. Select **Create new bucket**
3. Enter a name for the bucket in the **Name** field
4. Select **Create bucket**

## Add and run the example code

<Steps>
  <Step title="Locate index.ts">
    Open the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=dcf170c63430088fc4e28058849eec4f" alt="files icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/files-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b72e6d298af9f96117a8a5492b9d8a42 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=af6a952cc85e5f742968c8a91b1e5137 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7f13cd1bcab1279e81e042c7a80d3033 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c4b325c9fc5e0e80d3e98b68715f2aa1 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=dcefa4a3a120cf6be1af51a67430632f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=78a61e721c9d71f1d41541aea469befc 2500w" /> **Files** tool from the left dock.

    Select `index.ts` to open it in a file editor.
  </Step>

  <Step title="Add the client code">
    Replace the contents of `index.ts` with the following code:

    ```javascript  theme={null}
    import { Client } from "@replit/object-storage";
    const client = new Client();

    // Upload a text file that contains the text "Hello, World!"
    const { ok: uploadOk, error: uploadError } = await client.uploadFromText(
      "file.txt",
      "Hello World!",
    );
    if (!uploadOk) console.error("Upload failed:", uploadError);

    // List the files in the bucket
    const { ok: listOk, value: listValue, error: listError } = await client.list();
    if (!listOk) console.error("List failed:", listError);
    else console.log("Bucket contents:", listValue);

    // Retrieve and print the contents of the uploaded file
    const {
      ok: downloadOk,
      value,
      error: downloadError,
    } = await client.downloadAsText("file.txt");
    if (!downloadOk) console.error("Download failed:", downloadError);
    else console.log("file.txt contents:", value);
    ```
  </Step>

  <Step title="Run the app">
    Select **Run** to execute the example code.

    Navigate to the **Console** tab to view the output, which should resemble the output below:

    ```
    Bucket contents: [ { name: 'file.txt' } ]
    file.txt contents: Hello World!
    ```

    Confirm that the `file.txt` file appears in your bucket in the **Objects** view of the
    **App Storage** tool.

    <Tip>
      Reload the page to update the object list if `file.txt` fails to appear.
    </Tip>
  </Step>
</Steps>

## Delete the object

To remove the `file.txt` file from the bucket,

1. Replace the content of `index.ts` with the following code:

   ```javascript  theme={null}
   import { Client } from "@replit/object-storage";
   const client = new Client();

   // Delete file.txt from the bucket
   const { ok: deleteOk, error: deleteError } = await client.delete("file.txt");
   if (!deleteOk) console.error("Delete failed:", deleteError);
   else console.log("Delete succeeded");
   ```
2. Select **Run** to execute the example code.
3. Navigate to the **Console** tab to view the output, which should resemble the output below:
   ```
   Delete succeeded
   ```
4. Verify that the `file.txt` object no longer appears in the bucket.

## Next steps

To learn more about Replit App Storage, see the following resources:

* [App Storage](/cloud-services/storage-and-databases/object-storage/): Learn more about the App Storage feature and workspace tool
* [App Storage JavaScript SDK](/reference/object-storage-javascript-sdk): Learn about the `Client` class and its methods
