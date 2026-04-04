# Source: https://docs.unstructured.io/ui/sources/dropbox-source-quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Dropbox source connector quickstart

Unstructured can connect to several types of [sources](/ui/connectors#sources). In this quickstart, you create a [Dropbox](https://www.dropbox.com/) source connector that you can add to your Unstructured [workflows](/ui/workflows).
This source connector enables your Unstructured workflows to process your files that you store in a Dropbox account.

In this quickstart, you will:

* Create a free Dropbox Basic account.
* Create a Dropbox app in your Dropbox account. This app will provide the connection between your Dropbox account and your Unstructured account.
* Get specific information about your Dropbox app that Unstructured needs to connect to the app.
* Create a Dropbox source connector in your Unstructured account.
* Add the Dropbox source connector to a workflow in your Unstructured account.

If you are not able to complete the following steps, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

## Step 1: Create your Dropbox account

In this step, you create a [free Dropbox Basic account](https://www.dropbox.com/basic). This account is limited to a single user and 2 GB of storage.

If you already have a Dropbox account and want to use it instead, then skip ahead to Step 2.

1. Go to the Dropbox account sign up page, at [https://www.dropbox.com/register](https://www.dropbox.com/register).
2. Enter your email address, and then click **Continue**.
3. Enter your name and then, for **Password**, enter some password for your new account. Be sure to save this password to some secure location,
   as you will need it to access your Dropbox account later.
4. Click **Agree and sign up**.
5. To create a Dropbox Basic account, click the **Personal** tile.
6. When you are prompted to install the Dropbox desktop app or mobile app, click **Skip step**. (You can always install these apps later.)
7. To create a Dropbox Basic account, click **Continue with 2 GB Dropbox Basic plan** at the bottom of the account type selectionpage.
8. You are automatically signed in to your new Dropbox Basic account, and the Dropbox user interface (UI) appears.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=0beca3a2af745ab441706f123aa4e800" alt="Dropbox user interface" data-og-width="1877" width="1877" data-og-height="730" height="730" data-path="img/dropbox-quickstart/Dropbox-UI.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=83ae530f25a13af5484b5a08d186458d 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=67fbec1d3597b5de23b2a71b598dc4fe 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=9be6af38fc30b729026c07f8eaded821 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a3309ad6cc63ab22d9e5cf7eb9db3e20 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1f758ca3da4cb8a754676ebfc71e28b8 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Dropbox-UI.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=4429f5bbbd6c70df4aea7161ba42beca 2500w" />

## Step 2: Create a Dropbox app

In this step, you create a Dropbox app in your Dropbox account. Unstructured will use this app to access your Dropbox account.

1. From a new tab in your web browser, open the Dropbox Developers page, at [https://www.dropbox.com/developers](https://www.dropbox.com/developers).

2. Click **Create apps**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=df03181b070dc3b781aefc899268aed0" alt="Begin creating a Dropbox app" data-og-width="1318" width="1318" data-og-height="1206" height="1206" data-path="img/dropbox-quickstart/Create-Apps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f0c4dd3c7f20fbec293c9748156db2d3 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=538190fa3b5f0e58e2f2086ae1d97694 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ccc3280febfe8da9ca2cf8c67d1a3d28 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a5962c771cc0b5cbf06ef56bd29d54a8 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=8d28f988433f5378b526121c563c9980 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7ddb665b12319931e25c9fca463878ca 2500w" />

   <Tip>
     If **Create apps** is not visible then, on the top navigation bar, click **App Console**, and then click **Create app**.
   </Tip>

3. For **Choose an API**, select the **Scoped access** radio button.

4. For **Choose the type of access you need**, select the **App folder** radio button.

5. For **Name your app**, enter some name for your Dropbox app.

6. Check the box labelled **I agree to Dropbox API Terms and Conditions**, if it appears.

7. Click **Create app**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=70fe95f66275eb274501c245bd6090c3" alt="Finish creating the Dropbox app" data-og-width="1100" width="1100" data-og-height="779" height="779" data-path="img/dropbox-quickstart/Create-App.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6a3c51438c2ea30a4f47dcf73e957a06 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=11096fd858977ffeb44e86d69671ef20 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2dc24c6a5cf7f4688ae3cbee6d75d13e 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a4ac96570b34a9eafa78cae4e91bdbd0 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d89c3c7989858a52fc68e105ba59ffde 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-App.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2d4658f81da51559ce3b270570d6d51c 2500w" />

8. On the Dropbox app's **Permissions** tab, under **Files and folders**, check the box labelled **files.content.read**, and then click **Submit**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6f3a9d2df452cd419eb248e2823e490e" alt="Setting files.content.read for the Dropbox app" data-og-width="1096" width="1096" data-og-height="741" height="741" data-path="img/dropbox-quickstart/Files-Content-Read.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=09cf672b43953cf6cec7c5a25c951d90 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e090a83a7f1645963a80101c18c91de1 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b72f8b1bcaa4b6ac6dc2a8456d414c27 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1d47802fd4a63d3d9580741b1d6f314e 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=4d5bf278fa7fdd42cb1c638105fef81a 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Files-Content-Read.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1c9fbfa772ac07535971b8530912810a 2500w" />

9. On the app's **Settings** tab, note the value of the **App folder name** field. This is the name of the subfolder that Dropbox will create under the `Apps` top-level folder in your Dropbox account. Your new Dropbox app will use this subfolder for access.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=43d6e899019d1e071dc94d1e472ad5ca" alt="Noting the app folder's name" data-og-width="1092" width="1092" data-og-height="764" height="764" data-path="img/dropbox-quickstart/App-Folder-Name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=241170fc4054b02d8a442c1aa7193413 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d8132327f6cef89a1ae0365760b39ce6 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=026270ae66b1edda7f8ca9cf8d698a2d 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f24f8158101d5f22edc5530f535b6c75 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cf95976ab7e72ba2a7e2a78c0b4a9ae7 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Folder-Name.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=bc93581d2e82e88250e22101a10fbbc4 2500w" />

10. With the app's **Settings** tab still showing, scroll down to **App key**.

11. Next to **App secret**, click **Show**.

12. Note the values of **App key** and **App secret**, as you will need them later for Steps 3 and 5.

    <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b807f7a326c3eed8e0c0c2df66c5c4ae" alt="Noting the app's key and secret" data-og-width="1102" width="1102" data-og-height="766" height="766" data-path="img/dropbox-quickstart/App-Key-App-Secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cf2e50c38649436db2c5e2c3a9f43f41 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=42d2c32ed4eb28199d0013d38deed327 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b3da426a67b041732c75108e3073a5a9 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=5a633560d637a3b1a9dd078a3454c3f3 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=676f7de1eccab82091d58aa7a3e0dbfe 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/App-Key-App-Secret.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=628cee357caa73dced3b4730833557d6 2500w" />

## Step 3: Get a refresh token for your Dropbox app

In this step, you get a refresh token for your Dropbox app. Unstructured needs this refresh token, along with the
**App key** and **App secret** from the previous step, to be able to use your Dropbox app to connect to your Dropbox account.

1. In a new tab in your web browser, enter the following address. In this address,
   replace `<app-key>` with the **App key** you noted in Step 2:

   ```bash  theme={null}
   https://www.dropbox.com/oauth2/authorize?client_id=<app-key>&response_type=code&token_access_type=offline
   ```

   For example, if your **App key** is `aaa1aaaaaa1aaaa`, then your address should look like this:

   ```bash  theme={null}
   https://www.dropbox.com/oauth2/authorize?client_id=aaa1aaaaaa1aaaa&response_type=code&token_access_type=offline
   ```

2. Click **Continue**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=5512ebe1a9c77eb88d0884adfbb60a4d" alt="Continuing to get the access code" data-og-width="655" width="655" data-og-height="523" height="523" data-path="img/dropbox-quickstart/Access-Code-Continue.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d240178f9e1187d4d6c8f59a3dba9af4 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ba5aa07174b4d523c2319b02419f8dc4 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b12fcde35f2ca2e7bd9c8e2f1430b33b 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=8f1c0fc56a40e89b6a05d450d04829f5 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=c8bad370f16aa76068f90b2fc73da5d0 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Continue.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e22a5c11bc6a598b6217b488c71e9f47 2500w" />

3. Click **Allow**.

   <img src="https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=5ee6666f40638018e4d7d714ec6f2ea2" alt="Allowing the access code to be generated" data-og-width="633" width="633" data-og-height="447" height="447" data-path="img/dropbox-quickstart/Access-Code-Allow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=280&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=dd7bbd671704e6dd5af9a0382c3f8b5f 280w, https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=560&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=a0c064a5901cbe857cfcdc862564eda3 560w, https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=840&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=67662d82ee46621461b18d1bb8386369 840w, https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=1100&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=275f1b9a307a6414cef9fcf9b6910675 1100w, https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=1650&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=46ac8a544e8a1f30db7a04e3859cf803 1650w, https://mintcdn.com/unstructured-53/sm3rwRONB4yNpTK7/img/dropbox-quickstart/Access-Code-Allow.png?w=2500&fit=max&auto=format&n=sm3rwRONB4yNpTK7&q=85&s=48fe0774aafe5948090e82e825cbdf42 2500w" />

4. Note the value in the **Access Code Generated** box.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=97ec73db8b40ea3bbc34c928bbe86828" alt="Viewing the generated access code" data-og-width="648" width="648" data-og-height="319" height="319" data-path="img/dropbox-quickstart/Access-Code-Generated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d306c988134824762a162f81777d3c32 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=bd03db23304e0cf09ad1c74301523d79 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=4ad73a83a027d954824213dac9412f28 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ddc120c263c87cf0d265a136ce4bd4ac 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=dc241c587e30fd5f7233c627efc467c3 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Access-Code-Generated.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ba8b0a1e217d2f73a1ce4df1cd635423 2500w" />

   <Tip>
     This same access code value also appears in the **auth\_code** parameter from the address bar. For example, if the address bar shows this:

     ```bash  theme={null}
     https://www.dropbox.com/oauth2/authorize_success?auth_code=ccc1ccc1ccc1-1cc-1cc&client_id=aaa1aaaaaa1aaaa&version=1
     ```

     Then the **auth\_code** value is `ccc1ccc1ccc1-1cc-1cc`.
   </Tip>

5. On your computer, open the Terminal if you're using macOS, a terminal window if you're using Linux, or the Command Prompt if you're using Windows.

6. Check to see if the `curl` utility is alredy installed on your computer by running the following command:

   ```bash  theme={null}
   curl --version
   ```

7. If the `curl` utility is already installed, then you will see the `curl` version number and some other information about `curl`.

   If some kind of error message appears instead, then install `curl` on your computer by following [instructions for your operating system](https://ec.haxx.se/install/index.html).

8. From your Terminal, terminal window, or Command Prompt, run the following `curl` command. In this command,
   replace the following placeholders:

   * Replace `<app-key>` with the **App key** you noted in Step 2.
   * Replace `<app-secret>` with the **App secret** you noted in Step 2.
   * Replace `<access-code>` with the **Access Code Generated** (or `auth_code`, if you followed the Tip) that you noted earlier in this step.

   <Icon icon="apple" />  <Icon icon="linux" />  For macOS or Linux, run this `curl` command:

   ```bash  theme={null}
   curl --location --request POST 'https://api.dropbox.com/oauth2/token' \
   --user '<app-key>:<app-secret>' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'code=<access-code>' \
   --data-urlencode 'grant_type=authorization_code'
   ```

   <Icon icon="apple" />  <Icon icon="linux" />  For example, if your **App key** is `aaa1aaaaaa1aaaa`, your **App secret** is `bbb1bbb1bbb1bbb1`, and your **Access Code Generated** or `auth_code` value is `ccc1ccc1ccc1-1cc-1cc`, then your command should look like this:

   ```bash  theme={null}
   curl --location --request POST 'https://api.dropbox.com/oauth2/token' \
   --user 'aaa1aaaaaa1aaaa:bbb1bbb1bbb1bbb1' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'code=ccc1ccc1ccc1-1cc-1cc' \
   --data-urlencode 'grant_type=authorization_code'
   ```

   <Icon icon="windows" />  For Windows, run this `curl` command:

   ```bash  theme={null}
   curl --location --request POST "https://api.dropbox.com/oauth2/token" ^
   --user "<app-key>:<app-secret>" ^
   --header "Content-Type: application/x-www-form-urlencoded" ^
   --data-urlencode "code=<access-code>" ^
   --data-urlencode "grant_type=authorization_code"
   ```

   <Icon icon="windows" />  For example, if your **App key** is `aaa1aaaaaa1aaaa`, your **App secret** is `bbb1bbb1bbb1bbb1`, and your **Access Code Generated** or `auth_code` value is `ccc1ccc1ccc1-1cc-1cc`, then your command should look like this:

   ```bash  theme={null}
   curl --location --request POST "https://api.dropbox.com/oauth2/token" ^
   --user "aaa1aaaaaa1aaaa:bbb1bbb1bbb1bbb1" ^
   --header "Content-Type: application/x-www-form-urlencoded" ^
   --data-urlencode "code=ccc1ccc1ccc1-1cc-1cc" ^
   --data-urlencode "grant_type=authorization_code"
   ```

9. In the response, note the vaue of the `refresh_token` field, which you will need later for Step 5. For example, if the response looks like this
   (line breaks are added here for readability—the actual response will not have these line breaks):

   ```bash  theme={null}
   {
       "access_token": "sl.u.AF-aaa1aaa1", 
       "token_type": "bearer", 
       "expires_in": 14400, 
       "refresh_token": "ddd1ddd1ddd1ddd1", <-- Note this value.
       "scope": "account_info.read files.content.read files.metadata.read", 
       "uid": "1111111111", 
       "account_id": "dbid:aaa1aaa1aaa1"
   }
   ```

   Then the value of the `refresh_token` field is `ddd1ddd1ddd1ddd1`.

## Step 4: Upload documents to your Dropbox app folder

In this step, you add your documents to your Dropbox app folder in your Dropbox account.

1. In the Dropbox UI from Step 1, expand `Apps`, and then click the folder that matches the **App folder name** field you noted in Step 2.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=fd18c9539cb6b109a95e28d0c37eab65" alt="Selecting the app folder" data-og-width="680" width="680" data-og-height="470" height="470" data-path="img/dropbox-quickstart/Select-App-Folder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=eac05f03b10cdcf436919be572a23703 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=02801ec26e52b8d7f25995a90aae6e83 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=c4e879b05130505f20391614d93b3538 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=960ae8ce6e13ab01d073dc7f52d2a0d8 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=3c4e4df14cfdd92937ce5e45ee303461 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-App-Folder.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d20f651b0da0753ccfcc09eda56b45bc 2500w" />

   <Tip>
     If the `Apps` folder is not clickable, or if Dropbox reports that the folder is not found,
     then try refreshing the page and clicking the `Apps` folder again.
   </Tip>

2. Click **Create folder**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=76e91e850f97fc97b3203bc89cc75392" alt="Begin creating the subfolder" data-og-width="1958" width="1958" data-og-height="522" height="522" data-path="img/dropbox-quickstart/Create-Folder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=10d497357a505be443d8290a0d4d4bb9 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=3f917c48c6f01c4ed5a567646697ef0a 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e085f42e3ab391f6d74dea61ca76341b 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1a42788df2b6670106872ad332e53b13 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=74dd379b8925a27dd1b439df1df4d65f 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Folder.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=05c7419474732d2e9548fe7b6d7a2a57 2500w" />

3. Give the subfolder a name, and then click **Create**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b2ffe53e59fa04c3dcbe4535d95b8d24" alt="Finish creating the subfolder" data-og-width="389" width="389" data-og-height="407" height="407" data-path="img/dropbox-quickstart/Create-Apps-Subfolder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=397ed6556d2d2799f958ac1549f5e4e2 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e1f4a01a05a2ba0b5167c9c78567da83 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6604b1d902fbc815697fb58fe021e239 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2923ebcb345275cf0b8e6da1313fa82a 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=adbcb4f05ee0a230a060e132f7c8f5a5 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Create-Apps-Subfolder.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=5c52ab5250f73394df1125f1df87cc8a 2500w" />

4. Click **Upload or drop** (or **Upload > Files** or **Upload > Folder**), and then follow the on-screen instructions to upload some documents to this subfolder in your Dropbox app folder.
   For a Dropbox Basic account, the total size of all of the files you upload and store in your Dropbox account (not just this subfolder) cannot exceed 2 GB.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1f78b1fc056da0384b33718748e3cc4c" alt="Upload files to subfolder" data-og-width="1194" width="1194" data-og-height="688" height="688" data-path="img/dropbox-quickstart/Upload-To-Apps-Subfolder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=61331b2f4c01178b79f991ab2ed4272a 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=55170b33b1b37b6302314a728adbd161 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=30110f1e0242e419700e64e799fc2286 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=9f6023e93ee13cbe795ca4d69bc41da4 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=9480fb585ec42dd36e8c84ac807f1bcc 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Upload-To-Apps-Subfolder.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=41b8a6159650d0fb6b7ded55af0594cc 2500w" />

## Step 5: Create the Dropbox source connector

In this step, you create a Dropbox source connector in your Unstructured account. This source connector
is used by Unstructured to connect to your Dropbox account and then process the documents in the specified folder.

1. If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
   After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/ui/overview#how-am-i-billed%3F).
   </Note>

2. If you have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at [https://platform.unstructured.io](https://platform.unstructured.io).

   <Note>
     For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
     or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
   </Note>

3. On the sidebar, click **Connectors**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7809fcd7555999c5923ea46a1b589db4" alt="Connectors sidebar icon" data-og-width="77" width="77" data-og-height="216" height="216" data-path="img/dropbox-quickstart/Sidebar-Connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cac397b00d8d715257b7415daec8a1ac 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=90e5ff953095c78bca22fd48b79fd00f 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=66abd4a711415f1fcbcb97755461e61a 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=88a7b3ae33a818ddbfb5a4f30d12c0a5 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=250ba3ba3b1c9dae9f3974406a333d07 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=376f4cad7cbd7ba944087988b1b33c6a 2500w" />

4. Click **+ New**.

5. Enter some unique name for this connector, for example `dropbox-source-connector`.

6. For **Type**, click **Source**.

7. For **Provider**, click **Dropbox**.

8. Click **Continue**.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=846a52dd2e971b4acb98136cc83b4afb" alt="Selecting the connector type" data-og-width="701" width="701" data-og-height="673" height="673" data-path="img/dropbox-quickstart/Select-Connector-Type.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b29dc78b6047e92f1514dfbe4efc013e 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cc6e4d1188488eacf1392a27211d66d3 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=110a0a631f1b752b4594e6921c41b69b 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=29b4200e4ffa7f2945e9ef58b0c32941 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a949f858ce74a0937073a21e65e84afd 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Connector-Type.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=bb8f43093583200a73ed8a29164d5da0 2500w" />

9. For **Data URL**, enter `dropbox://`, followed by the name of the subfolder you created in the previous step. For example,
   if the name of the subfolder is `my-folder`, then the data URL would be `dropbox://my-folder`.

   <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a1a545f6fb42c712a3baa8276cbc8539" alt="Forming the data URL" data-og-width="571" width="571" data-og-height="303" height="303" data-path="img/dropbox-quickstart/Apps-Subfolder-Name.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=4344e66bd9ac57072b664e26e68f26ab 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f4efb44145c0b750adc311ef8173ac3d 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=3ac38a5c92d1bf87b7f514a865afb21e 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a210e774b62180a80aca705f0e449437 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=46f85b40bca38dde5d46b3bb952d9800 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Apps-Subfolder-Name.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=403cd8c0c7c309fa6208d412e2f99865 2500w" />

10. For **App key**, enter the **App key** you noted in Step 2.

11. For **App secret**, enter the **App secret** you noted in Step 2.

12. For **Refresh token**, enter the **Refresh token** you noted in Step 3.

13. Click **Save and Test**, and wait while Unstructured tests the connector.

<img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7ce24fc4dd787e378839a9bd6d82490c" alt="Entering connector settings" data-og-width="701" width="701" data-og-height="719" height="719" data-path="img/dropbox-quickstart/Source-Connector-Settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7908754b2e486ef8e3a7fe7c6e855212 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=57a9a4e3483e89a9c44b90aa4c5bf5ab 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1b59cb576e15e4e27dc66688a5d44ea4 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d7c1af20e209987f679d19e2b526ea34 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=8f163878e136a8c906a0d858753b1be1 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Connector-Settings.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cb8f6bb49f7d5ddd0d0dd23a40482e91 2500w" />

14. If a green **Successful** message appears, then you have successfully created the connector.

    <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=96a856445d7d7fe19a4da6528ca6d4db" alt="Successful connector test" data-og-width="927" width="927" data-og-height="161" height="161" data-path="img/dropbox-quickstart/Connector-Test-Success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=06c54f4baa5152f6be9644a9167ff081 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b223df60d77ddd1cbd730510478e3928 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2374d62c4af0da0d98ca231adebc1df8 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=37f8aa49bec955be73f60595b014c721 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=48a535b024e773f001820710f1b7bc1d 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Connector-Test-Success.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=63e0637d07d72a1f76b87cfd1943c51d 2500w" />

    If, however, a red error message appears, fix the issue, and try this step again.

    If you cannot fix the issue, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

Congratulations! You have successfully created a Dropbox source connector in your Unstructured account.

If you are not able to complete these steps, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

## Next steps

* If you do not have a destination connector in your Unstructured account, then complete the [Pinecone destination connector quickstart](/ui/destinations/pinecone-destination-quickstart).

  If you're not sure if you have a destination connector, click **Connectors** in your Unstructured account's sidebar, and then click **Destinations** to see if there are any listed.

  <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7809fcd7555999c5923ea46a1b589db4" alt="Connectors sidebar icon" data-og-width="77" width="77" data-og-height="216" height="216" data-path="img/dropbox-quickstart/Sidebar-Connectors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cac397b00d8d715257b7415daec8a1ac 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=90e5ff953095c78bca22fd48b79fd00f 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=66abd4a711415f1fcbcb97755461e61a 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=88a7b3ae33a818ddbfb5a4f30d12c0a5 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=250ba3ba3b1c9dae9f3974406a333d07 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Connectors.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=376f4cad7cbd7ba944087988b1b33c6a 2500w" />

* If you already have a destination connector, then you can add this Dropbox source connector as well as your destination connector to a workflow in your Unstructured account. To do this:

  1. Click **Workflows** in your Unstructured account's sidebar.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=fe6cae91b1bbb6657edc98fd739ad060" alt="Workflows sidebar icon" data-og-width="75" width="75" data-og-height="279" height="279" data-path="img/dropbox-quickstart/Sidebar-Workflows.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ebac804ce00f68186ce2c5318609ecc9 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e3eb968f82e57ef4f06477ca1df42bd2 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e240139d5635f7b89d260559df190960 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e86fadd7176e1624e17db70070512c2f 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=492b7387bccc0164296220f148b9f5fd 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Workflows.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f620470f39e7e725b5dacf1bbd37496c 2500w" />

  2. Click **New Workflow +**.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=acef2a97aa6a38127834f0f681fec8a5" alt="Begin creating a workflow" data-og-width="2612" width="2612" data-og-height="250" height="250" data-path="img/dropbox-quickstart/New-Workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2b7e81208e7741a4bfecbb2a65cd3a78 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=af62730df3d6c59500cbbe7b3ae23af8 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=02cc67b6aa23b47d2b0858787f4841a2 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=172af9b01c5324cdd3b138a4f495312e 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1ee1a185e5e9c89909a5fa58b53dbcbc 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/New-Workflow.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=60905eb7f776a98953af9912f5f2926e 2500w" />

  3. With **Build it Myself** already selected, click **Continue**.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f39c417338fdc42b6d1762ab9b41e5c7" alt="Build it myself workflow type" data-og-width="1162" width="1162" data-og-height="846" height="846" data-path="img/dropbox-quickstart/Build-It-Myself.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=f608ebcea60ba91f393ac8e00c02e851 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=91365c5854818955c30f7350a6843172 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d36c295c9a5f1286f0ed37cdc6ea7e2d 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e7228156bf7ff5cdfa7f00848f6f2d1a 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d3871592459cc92067577f6ff10342e1 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Build-It-Myself.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ff959f43b4f1c851b15ac7ee23a19a51 2500w" />

  4. Click the **Source** node. (Do not click **Drop file to test**.)

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=22df9f41b4db6897fb15e543f391c92c" alt="Workflow source node" data-og-width="237" width="237" data-og-height="182" height="182" data-path="img/dropbox-quickstart/Source-Node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ac528908f9756e3688722343622992e2 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=70546577bdd29b73e55f0393d3976ad5 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=c8eca1cd848309c58c7cbd4a62ee5242 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=49d237824e6b06ea75a85c993343872d 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=07a8ea27ee57de806d9a98156102d9e4 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Source-Node.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=be37167f4d94ebb177ca272040c8b752 2500w" />

  5. On the **Details** tab, click **Connectors**, and then click the name of your Dropbox source connector.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1da059d0b2bf301372663becd411578b" alt="Selecting the source connector" data-og-width="530" width="530" data-og-height="311" height="311" data-path="img/dropbox-quickstart/Select-Source-Connector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=286e537f62cfb37911d6e39e87de8a19 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b8ce7eb59d82ed2e9cd69342c6bb7a9f 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=110c32ddd23c6378d15b8ce7c73943f4 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1dca60cb1771bbb624528eb2a6bf1296 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=353a8a3ad23881c394a07113d218da5d 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Source-Connector.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6994adfbb3a05cfa1edd51a49283b172 2500w" />

  6. Click the **Destination** node.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7f4fed222a8f2fd3499e1986cfc552dc" alt="Workflow destination node" data-og-width="287" width="287" data-og-height="118" height="118" data-path="img/dropbox-quickstart/Destination-Node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=8940a2e174a4e09efc205593b66880c8 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=8f4ddd6998728191b1e8bb4db97e437f 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=aa0a7286a2a033f51a8a34e14382f6d2 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7a85c73b480c54332044a7d4abaf3336 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=91ee05c1d90cd9e6473e2b458cf24771 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Destination-Node.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6224a7daff25ce5f360eb443526e43fb 2500w" />

  7. On the **Details** tab, click the name of your destination connector.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=700084df5d3f878428e707860a96099a" alt="Selecting the destination connector" data-og-width="524" width="524" data-og-height="133" height="133" data-path="img/dropbox-quickstart/Select-Destination-Connector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=599854572e812a11d32bbdd4a05ca174 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=6b75cc27ad2fbd62e0ca98a79203a8f6 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7e367af7239054bcd2bb27a42c76ad15 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cc1ed12ad23ea0cd234c2f10a12c7a7e 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2b20ccd9ce443adb01ccb22f27aab4f0 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Select-Destination-Connector.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=21bc2408c40c47b20240e2fcf14c2955 2500w" />

  8. Switch **Active** to on, and then click **Save**.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=13b389cafe579fff4ef97899850201d8" alt="Making the workflow active" data-og-width="192" width="192" data-og-height="45" height="45" data-path="img/dropbox-quickstart/Make-Workflow-Active.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=67f2a3c3bd42b621c510615c7f36a580 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=1fd84c28d846aaba3fb88a2f0791900c 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b6b0d9fcc2fe46520377cb7ecfa353a9 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=2a9d3550f2f876baddaafe585483e6dd 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=70628c310653183beacda00e6cf4f824 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Make-Workflow-Active.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=e32edb8b00da2ad3026c34e14fbcedd7 2500w" />

  9. Next to your workflow's name, click **Run**.

     <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b11755bcce69512120501e991414f31a" alt="Running the workflow" data-og-width="1457" width="1457" data-og-height="176" height="176" data-path="img/dropbox-quickstart/Run-Workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=93d0bb71b6fc209f1ef9cdede453ac51 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b67f0d5bcb7fc463d251de3cb7b5319a 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=510de50a2a7665649eb8df387413cdd0 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=7319a1f4d84569a90863084b233044d4 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=5053333465dc5bdfb0769800310a4caf 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Run-Workflow.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b032acb155befecf42bd5ffcab6feed2 2500w" />

  10. Click **Jobs** in your Unstructured account's sidebar.

      <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=c2fae030bdd046d1a8de983ab3939371" alt="Jobs sidebar icon" data-og-width="78" width="78" data-og-height="364" height="364" data-path="img/dropbox-quickstart/Sidebar-Jobs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=aff1efcd8966fc59af383827eee66906 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=9e773fd9792a88b78299695e5d0c5e9c 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=61890d011b45e43bba7e5d3f01ebc456 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ae38f96ea981889bafc1782e90631cfc 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=c9b287ae715cdf51c414625f3b459d15 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Sidebar-Jobs.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=757012b87d165854ed64e42f4fb0d87d 2500w" />

  11. After the job shows **Finished** with a green checkmark, go to your destination's location to see Unstructured's processed data output.

  <img src="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=d4f62ceee8057bab11846eb8788ed205" alt="Finished job status" data-og-width="786" width="786" data-og-height="382" height="382" data-path="img/dropbox-quickstart/Finished-Job.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=280&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=b82e7673d32051f0be4beb705fae9843 280w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=560&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=a8efa3d651e2959ea336f259ec7c957f 560w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=840&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=662f20e52c4b9513d03b854b70dacffc 840w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=1100&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=ca58cbc3ace98f66fbb7373016e388e9 1100w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=1650&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=cc42487ad1b04f8f1e72a5e08c984901 1650w, https://mintcdn.com/unstructured-53/vQCKW1wFRcqqOuSd/img/dropbox-quickstart/Finished-Job.png?w=2500&fit=max&auto=format&n=vQCKW1wFRcqqOuSd&q=85&s=bec116353e726af4d39ceba0696abb49 2500w" />

If you are not able to complete these steps, contact Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
