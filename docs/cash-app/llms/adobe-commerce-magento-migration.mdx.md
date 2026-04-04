# Source: https://developers.cash.app/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/platforms/adobe-commerce-magento-migration.mdx

***

## stoplight-id: w4i05f5nej0j5

# Adobe Commerce Migration

To use the Cash App Afterpay product with Adobe Commerce (Magento 2), upgrade your extension to the latest version. Specifically:

* Minimum v5.4.2 for Magento 2.4

* Minimum v4.3.3 for Magento 2.3

* Minimum v1.2.4 for Adobe PWA (Progressive Web Application) Studio

If you are on a lower version than these, please update. See the [Update My Adobe Commerce Extension](#update-my-adobe-commerce-extension) section below if you are not sure how to upgrade your extension to the latest version.

If you are on minimum or higher version, existing settings and configurations continue to work as before; there is no need to change them.

See the [Adobe Commerce Getting Started](/cash-app-afterpay/guides/platforms/adobe-commerce-magento) page for detailed technical information on the Cash App Afterpay integration with Adobe Commerce.

***

## Update My Adobe Commerce Extension

***

The Cash App Afterpay extension update method depends on how you, the merchant, have originally installed the Afterpay module.

If you used [Composer](https://getcomposer.org/) to install the Afterpay module, then use Composer to update it. If you used a manual process to install theAfterpay module, then use a [manual update](#manual-update) to update it.

The extension update process depends on whether you want to use [Composer](https://getcomposer.org/) to make the update, or do a [manual update](#manual-update). We recommend that you [update with Composer](#update-with-composer).

In either case, backup your system files before you start an update.

<Note>
  The module used to update to Cash App Afterpay is still called Afterpay. This doesn't affect any of the instructions or advice below.
</Note>

### Update with Composer

<Note>
  In the instructions below, the 

  `[ADOBE-COMMERCE]`

   folder refers to the root folder where Adobe Commerce/Magento is installed.
</Note>

1. Open the Command Line Interface (CLI) and go to the `[ADOBE-COMMERCE]` folder on your server.

2. Run one of the following commands in the table to update the Afterpay module, depending on the Magento version:

| Magento version | Command to run                                      |
| --------------- | --------------------------------------------------- |
| 2.4             | composer require afterpay-global/module-afterpay:^5 |
| 2.3             | composer require afterpay-global/module-afterpay:^4 |
| \< 2.3.0        | composer require afterpay-global/module-afterpay:^4 |

3. Make sure that Composer finishes the installation without errors.

4. Run the Adobe Commerce setup upgrade: `php bin/magento setup:upgrade`.

5. Run the Adobe Commerce Dependencies Injection Compile: `php bin/magento setup:di:compile`.

6. Run the Adobe Commerce Static Content deployment: `php bin/magento setup:static-content:deploy`.

7. Run the Adobe Commerce System Cache Flush: `php bin/magento cache:flush`.

### Cash App Pay Update with Composer

This section only applies if you have Cash App Pay installed together with Afterpay.

<Note>
  In the instructions below, the 

  `[CASH-APP-PAY]`

   folder refers to the root folder where Cash App Pay is installed.
</Note>

1. Open the Command Line Interface (CLI) and go to the `[CASH-APP-PAY]` folder on your server.

2. Run one of the following commands in the table to update the Cash App Pay module, depending on the Magento version:

| Magento version | Command to run                                      |
| --------------- | --------------------------------------------------- |
| 2.4             | composer require afterpay-global/module-afterpay:^5 |
| 2.3             | composer require afterpay-global/module-afterpay:^4 |
| \< 2.3.0        | composer require afterpay-global/module-afterpay:^4 |

Then:

3. Make sure that Composer finishes the installation without errors.

4. Run the Adobe Commerce setup upgrade: `php bin/magento setup:upgrade`.

5. Run the Adobe Commerce Dependencies Injection Compile: `php bin/magento setup:di:compile`.

6. Run the Adobe Commerce Static Content deployment: `php bin/magento setup:static-content:deploy`.

7. Run the Adobe Commerce System Cache Flush: `php bin/magento cache:flush`.

## Manual Update

This method does not use Composer. It is more complex than using Composer, but just as effective when done correctly. Follow the instructions below.

### Remove old Afterpay files/folders

<Note>
  In the instructions below, the 

  `[ADOBE-COMMERCE]`

   folder refers to the root folder where Adobe Commerce/Magento is installed.
</Note>

1. Remove all the files in: `[ADOBE-COMMERCE]/app/code/Afterpay/Afterpay`. Then you are ready to download the Afterpay Extension.

### Download the Afterpay Extension

The extension is on GitHub. Do the following:

1. Go to GitHub for the link to [Magento 2](https://github.com/afterpay/afterpay-magento-2). The source code needed depends on your version of Magento. For these details, see the [Readme file](https://github.com/afterpay/afterpay-magento-2#readme).

2. Under the green *Code* heading, click **Download ZIP**. See the screenshot below:

   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/adobe-comm-manual-install.png" alt="adobe-comm-manual-install.png" noZoom />

3. Unzip your files and put them into a temporary folder.

<Info title="Install Folder">
  You can install Adobe Commerce in any folder on your server. In this guide, `[ADOBE-COMMERCE]` is the name of the root folder where Adobe Commerce is installed.
</Info>

#### Run the Commands

1. Copy the files from your temporary folder to the `[ADOBE-COMMERCE]/app/code/Afterpay/Afterpay` folder. The temporary folder is the one you created in Step 3 in the *Download the Afterpay Extension* section above.

2. Open the Command Line Interface (CLI) and make sure you are the owner of the `[ADOBE-COMMERCE]` folder. Run all CLI commands as the owner of the folder, not `root` and without `sudo`.

3. From the CLI, run the commands below:

| Command                                          | Description                                    |
| :----------------------------------------------- | :--------------------------------------------- |
| php bin/magento module:enable Afterpay\_Afterpay | Enable Afterpay extension.                     |
| php bin/magento setup:upgrade                    | Adobe Commerce setup upgrade.                  |
| php bin/magento setup:di:compile                 | Adobe Commerce dependencies injection compile. |
| php bin/magento setup:static-content:deploy      | Adobe Commerce static content deployment.      |
| php bin/magento cache:flush                      | Adobe Commerce system cache flush.             |

Now you need to repeat the process for the *Cash App Pay Extension for Magento 2*:

1. Remove the existing files in the `[ADOBE-COMMERCE]/app/code/Afterpay/CashApp` folder.

2. Download and copy the files to the `[ADOBE-COMMERCE]/app/code/Afterpay/CashApp` folder. The source code path is based on the Magento version [here](https://github.com/afterpay/cash-app-pay-magento-2).

3. Open the Command Line Interface (CLI) and run the commands below:

| Command                                         | Description                                    |
| :---------------------------------------------- | :--------------------------------------------- |
| php bin/magento module:enable Afterpay\_CashApp | Enable the Cash App Pay extension.             |
| php bin/magento setup:upgrade                   | Adobe Commerce setup upgrade.                  |
| php bin/magento setup:di:compile                | Adobe Commerce dependencies injection compile. |
| php bin/magento setup:static-content:deploy     | Adobe Commerce static content deployment.      |
| php bin/magento cache:flush                     | Adobe Commerce system cache flush.             |

You can find a table of the Afterpay Plugins for Adobe Commerce/Magento 2 [here](https://github.com/afterpay/afterpay-magento-2#install-manually). It also contains useful information on the manual installation process.

## Brand Assets

There are some new Cash App Afterpay brand assets to use at checkout and across your site. See the [Brand Assets](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/brand-assets) page in this guide for these new assets.

The table below has examples of the changes:

|         | Afterpay                                                | Cash App Afterpay                                       |
| ------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Logos   | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-logo-resized.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-white-logo-resized.png" /> |
| Buttons | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-button.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-button.png" /> |

## Messaging

Messaging is automatically updated if you use On-Site Messaging, our current messaging product, or its predecessor that used the JavaScript library for messaging. In both cases wait for the automatic update process to occur. Monitor your email for advance notice of this automatic update.

See the table below for an example of the changes:

| Afterpay                                                | Cash App Afterpay                                       |
| ------------------------------------------------------- | ------------------------------------------------------- |
| <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/ap-mess-2.png" /> | <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/caap-mess-1.png" /> |

The automatic Messaging update includes changes to *learn more*/lightbox asset if you use that.

If you use elements of Afterpay Messaging but not the standard Onsite Messaging Widget, then update the Afterpay elements with new Cash App Afterpay elements. See the [Brand Assets](#brand-assets) section above.

Any custom messaging updates must be reviewed by your Account Manager.

## FAQs

If you have a technical question on the migration, see our [FAQs for the Migration](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/migration-fa-qs) page.
