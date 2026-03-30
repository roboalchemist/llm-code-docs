# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/adobe-commerce-magento/update-extension.mdx

***

## stoplight-id: hlb5cl65tzfgo

# Adobe Commerce - Update Extension

**How can I update my Adobe Commerce Extension?**

***

The Cash App Afterpay extension update method depends on how you, the merchant, have originally installed the Cash App Afterpay module.

If you used [Composer](https://getcomposer.org/) to install the Cash App Afterpay module, then use Composer to update it. If you used a manual process to install the Cash App Afterpay module, then use a [manual update](#manual-update) to update it.

The Cash App Afterpay extension update process depends on whether you want to use [Composer](https://getcomposer.org/) to make the update, or do a [manual update](#manual-update). We recommend that you [update with Composer](#update-with-composer).

In either case, backup your system files before you start an update.

## Update with Composer

<Note>
  In the instructions below, the 

  `[ADOBE-COMMERCE]`

   folder refers to the root folder where Adobe Commerce/Magento is installed.
</Note>

1. Open the Command Line Interface (CLI) and go to the `[ADOBE-COMMERCE]` folder on your server.

2. Run one of the following commands in the table to update the Cash App Afterpay module, depending on the Magento version:

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

<Note>
  In the instructions below, the 

  `[CASH-APP-PAY]`

   folder refers to the root folder where Cash App Pay is installed.
</Note>

1. Open the Command Line Interface (CLI) and go to the `[CASH-APP-PAY]` folder on your server.

2. Run one of the following commands in the table to update Cash App Pay module, depending on the Magento version:

| Magento version | Command to run                                      |
| --------------- | --------------------------------------------------- |
| 2.4             | composer require afterpay-global/module-afterpay:^5 |
| 2.3             | composer require afterpay-global/module-afterpay:^4 |

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

1. Remove all the files in: `[ADOBE-COMMERCE]/app/code/Afterpay/Afterpay`. Then you are ready to download the Cash App Afterpay Extension.

### Download the Cash App Afterpay Extension

The extension is on GitHub. Do the following:

1. Go to GitHub for the link to [Magento 2](https://github.com/afterpay/afterpay-magento-2). The source code needed depends on your version of Magento. For these details, see the [Readme file](https://github.com/afterpay/afterpay-magento-2#readme).

2. Under the green *Code* heading, click **Download ZIP**. See screenshot below:

![adobe-comm-manual-install.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/adobe-comm-manual-install.png)

3. Unzip your files and put them into a temporary folder.

<Info title="Install Folder">
  You can install Adobe Commerce in any folder on your server. In this guide, `[ADOBE-COMMERCE]` is the name of the root folder where Adobe Commerce is installed.
</Info>

### Run the Commands

1. Copy the files from your temporary folder to the `[ADOBE-COMMERCE]/app/code/Afterpay/Afterpay` folder. The temporary folder is the one you created in Step 3 in the *Download the Cash App Afterpay Extension* section above.

2. Open the Command Line Interface (CLI) and make sure you are the owner of the `[ADOBE-COMMERCE]` folder. Run all CLI commands as the owner of the folder, not `root` and without `sudo`.

3. From the CLI, run the commands below:

| Command                                          | Description                                    |
| :----------------------------------------------- | :--------------------------------------------- |
| php bin/magento module:enable Afterpay\_Afterpay | Enable Cash App Afterpay extension.            |
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

You can find a table of the Cash App Afterpay Plugins for Adobe Commerce/Magento 2 [here](https://github.com/afterpay/afterpay-magento-2#install-manually). It also contains useful information on the manual installation process.
