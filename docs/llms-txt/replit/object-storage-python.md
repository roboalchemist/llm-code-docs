# Source: https://docs.replit.com/getting-started/quickstarts/object-storage-python.md

# Manage App Storage in Python

> Learn how to use the Python App Storage client library to manage files from your Replit App.

This guide demonstrates how to use the Python client library to upload, list, download, and delete files in your App Storage bucket.

## Create a Python Replit App

1. Select <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=a6613ac9b303fa6dea65e5cf08ddca06" alt="plus sign" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/create-app-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0f0aa42a2a63cca6629fe393ffb100e4 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=e6cce9e17a54ec2279d57d255e5233ba 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6a6f30d08c7ab4811ba927af66ca7311 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f7249d48a50a7db0713ea3f92f4c422f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f2a12316d646b72674a837cbe70a10f8 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/create-app-icon.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6cc3b1f288cf5086a84aadaa9b1d4fba 2500w" /> **Create App** from the home screen.
2. Navigate to the **Choose a Template** tab.
3. Type "Python" in the template search field and select it as shown below:
   <Frame>
     <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3d09d96320ab531aedf15df7894f1234" alt="Python template selection screen" data-og-width="2660" width="2660" data-og-height="1110" height="1110" data-path="images/tutorials/python-template.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=99cf29da1d08f91373f25b2ae2fda816 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=af19b79e5bb55049de9164b9196d2779 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=442a0cbff0f0ba108aac818d1b094cb6 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5bc6d317357624b52b0df92007f83c2b 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4677b5f853201d0acf98d5965685fb28 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/python-template.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9ff1ec092477367a3a1af5c60d694964 2500w" />
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
          <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=c948e6bfa611ee9f80f6392e4931d212" alt="screenshot of App Storage package installation" data-og-width="1954" width="1954" data-og-height="560" height="560" data-path="images/databases/install-object-storage-deps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=88009a8f0a1af0f01eae08087cbf259b 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=f47a835c6375877ea3ce6c833552e413 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b7a190ec85851cf595cfb9a8d67cba3e 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=ec413c2d49eee6eaeccb46209d8d7dba 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=877244f2eb1391c0e27b06112460b30e 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/databases/install-object-storage-deps.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=49ee3a78d595c6a38ca6c8fb8e896bca 2500w" />
        </Frame>
      </Step>

      <Step title="Install the dependencies">
        1. Select "Python" from the programming language dropdown on the top left.
        2. Select **Install replit-object-storage package**.
        3. When completed, the button text should read **Package installed**.
      </Step>
    </Steps>
  </Tab>

  <Tab title="upm">
    Use this option if your Replit App uses the Universal Package Manager (`upm`) to manage its dependencies.

    Open the **Shell** tool in your workspace and enter the following command:

    ```sh  theme={null}
    upm --lang python add replit-object-storage
    ```
  </Tab>

  <Tab title="pip">
    Use this option if your Replit App uses `pip` to manage its dependencies.

    Open the **Shell** tool in your workspace and enter the following command:

    ```sh  theme={null}
    pip install replit-object-storage
    ```
  </Tab>
</Tabs>

## Create a bucket

Before storing objects, you must create a bucket. Follow the steps below to create a new bucket:

1. Navigate to the **App Storage** tool
2. Select **Create new bucket**
3. Enter a name for the bucket in the **Name** field
4. Select **Create bucket**

## Add and run the example code

<Steps>
  <Step title="Locate main.py">
    Open the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=dcf170c63430088fc4e28058849eec4f" alt="files icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/files-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b72e6d298af9f96117a8a5492b9d8a42 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=af6a952cc85e5f742968c8a91b1e5137 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7f13cd1bcab1279e81e042c7a80d3033 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c4b325c9fc5e0e80d3e98b68715f2aa1 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=dcefa4a3a120cf6be1af51a67430632f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/files-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=78a61e721c9d71f1d41541aea469befc 2500w" /> **Files** tool from the left dock.

    Select `main.py` to open it in a file editor.
  </Step>

  <Step title="Add the client code">
    Copy and paste the following code into `main.py`:

    ```python  theme={null}
    # Instantiate a Client
    from replit.object_storage import Client
    client = Client()

    # Upload a text file that contains the text "Hello, World!"
    client.upload_from_text("file.txt", "Hello World!")

    # List the objects in the bucket
    objects = client.list()
    print("Bucket contents:", objects)

    # Retrieve and print the contents of the uploaded file
    contents = client.download_as_text("file.txt")
    print("file.txt contents: ", contents)
    ```
  </Step>

  <Step title="Run the app">
    Select **Run** to execute the example code.

    Navigate to the **Console** tab to view the output, which should resemble the output below:

    ```
    Bucket contents: [Object(name='file.txt')]
    file.txt contents:  Hello World!
    ```

    Confirm that the `file.txt` object appears in your bucket in the **Objects** view of the
    **Object Storage** tool.

    <Tip>
      Reload the page to update the object list if `file.txt` fails to appear.
    </Tip>
  </Step>
</Steps>

## Delete the object

To remove the `file.txt` file from the bucket,

1. Replace the content of `main.py` with the following code:

   ```python  theme={null}
   from replit.object_storage import Client
   client = Client()

   # Delete file.txt from the bucket
   client.delete("file.txt")
   print("Delete succeeded")
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
* [App Storage Python SDK](/reference/object-storage-python-sdk): Learn about the `Client` class and its methods
