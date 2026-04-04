# Source: https://docs.curator.interworks.com/setup/trial_quick_start_guide/adding_your_first_dashboard.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding Your First Dashboard

> Step-by-step guide to create your first analytics connection and add dashboards to Curator.

Click on **Integrations → Connections**

Click on **New Connection button**

* **Name**
  * Name your connection
* **Slug**
  * This slug (url extension) will auto-generate but can be customized
* **Description**
* **Platform**
  * Options include: Tableau, Power BI, ThoughtSpot
  * After selecting an option, fill out the platform specific connection information and credentials

## Tableau

### Tableau Server

1. **Enter Site name** (e.g. `https://analytics.acme.com`)
2. **Enter Service Account credentials or Personal Access Token**. To enter Personal Access Token, follow the below steps:
   1. Log onto your Tableau Server
   2. Click account icon on top right of screen (by default, will by a circle with your initials in it)
   3. Select My Account Settings
   4. Scroll to Personal Access Token
   5. Enter a Name for your Token and click Create Token

Additional information on Personal Access Tokens can be found in [Tableau’s documentation](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).

### Tableau Cloud

1. **Select the Tableau Cloud Host region** (found in the server url)
2. **Enter the Site name** (found in the server url after logging in)
3. **Enter your Personal Access Token**
4. **To enter Personal Access Token, follow the below steps:**
   1. Log onto your Tableau Server
   2. Click account icon on top right of screen (by default, will by a circle with your initials in it)
   3. Select My Account Settings
   4. Scroll to Personal Access Token
   5. Enter a Name for your Token and click Create Token

Additional information on Personal Access Tokens can be found in [Tableau’s documentation](https://help.tableau.com/current/pro/desktop/en-us/useracct.htm#create-and-revoke-personal-access-tokens).

#### Power BI

**Enter your Tenant ID in Azure**. To find your Tenant ID, follow this [documentation](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/how-to-find-tenant).

#### ThoughtSpot

1. Enter your ThoughtSpot URL
2. Enter your ThoughtSpot credentials

## Adding a Dashboard From Your Server

Once you have established a connection to your server you can begin adding individual Dashboard connections. For our
example we will follow along with a Tableau Dashboard but the instructions are similar for other BI platforms.

1. **Click Tableau** (or your BI Platform Option) → **Dashboards**
2. **Click the New Dashboard Button**

Select desired Server, Site, Project, Workbook, and Dashboard then click create to establish a connection.
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=5b4f6ae029eaa05f70d65c2e05edbfb5" alt="Dashboard dropdowns" data-og-width="1806" width="1806" data-og-height="474" height="474" data-path="assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=50ab3f613212bf766f2e80b6e8d632e4 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a4caf4d58012368c329808a6dddb7669 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8179350e0722672b95b6cc205d3f0e12 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=2cb633b8a850c0a3150a7b08caa33b87 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=75a69271e8f42275644bdc31dc460c70 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/adding-dashboard-from-server-1.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=68f6deb6728817894d82dd9afeaeedc2 2500w" />

Connect dashboards will be listed in the Tableau → Dashboard menu:
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4d5bec7ca5b712512cb0bd83092ef3e6" alt="Dashboard list" data-og-width="1851" width="1851" data-og-height="351" height="351" data-path="assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a5ce260d725ffa5dbeb912d97396070d 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4d326a560dea17bc44900465b06864ca 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=da429ed086073f08d00ac68dfd8a15b7 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c8f3df93a00b78cb44ec8a0e8de7c1da 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=fbb2852e17594f2e21d895b5f9c6cafa 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-133321.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=dd5b2994d4081e7359aca8dca3b5cf48 2500w" />

## Adding a Menu Link to the Navigation

After a connection to a Dashboard has been established, the simplest method is to add a menu link to the navigation pane
at the top of your environment.
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f66ed94a76584cd2c1fdf5a5384ab5fe" alt="homepage hero image and menu" data-og-width="1503" width="1503" data-og-height="361" height="361" data-path="assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=99a2ecc8b5fc2dbc2e3f0fc764f7a52d 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=d8c7bfc8a132471c51749f32f6620280 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ad14132f632957b0d74d504087d29b3b 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=8018bc583b275807497475ed2722d33a 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=41d1cd556b859a2207de516dbd20d6af 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-123206.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ebb3caf1497fbdf7f12954a78caee590 2500w" />

Click **Content → Navigation**

1. Select New Menu Link
2. Select your Dashboard Link Type
3. Select your Dashboard
4. Select Create

Once you create the link you will be brought to a page that displays the navigation hierarchy. You can control the
navigation pane’s order and drop down menus here:
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=146744102f74015990c6603190c1611a" alt="navigation reorder view" data-og-width="1359" width="1359" data-og-height="493" height="493" data-path="assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=e34f21dcd42c1d95cc51711b061d9f9b 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=cb705ff8b9388ec934511931b49f2f01 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=08bb75d2230e2bef48fd050afd35e28c 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c5b42c70f18e516567163b256570a8f2 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=a8b181b6cccc5e0dbd1658656ec01899 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124312.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=cf6e052c78937d31fce73995eea7e6ed 2500w" />
After you have decided on hierarchy, navigate to the front end and see your new navigation menu items that lead to your dashboards:
<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ff233cba5eb018185e46fb5d53c4aea6" alt="homepage hero image and menu" data-og-width="1334" width="1334" data-og-height="362" height="362" data-path="assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=bb8962c7ab877f3e8947a3e3931d61b9 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=51f4a4259c5aa63e785626412839c497 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=099d8d06cd591f62cd316493430b4ca2 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=4f82b10ee629a3b6c25907832f118f54 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6305d7c60beb9b770c57d0c7d1ec3546 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/setup/trial_quick_start_guide/box-notes-image-2023-08-07-124522.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=417bd6bac34311d879ebf4ab21608c3a 2500w" />
