# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/adobe-commerce-magento/install-extension.mdx

***

## stoplight-id: qo08aj1ek0h22

# Adobe Commerce - Install Extension

**How Can I Install and Enable the Adobe Commerce Extension?**

***

## Overview

There are two ways to install and enable the Adobe Commerce Cash App Afterpay Extension:

* Use [Composer](https://getcomposer.org) to automatically download and install the files it gets from [Packagist](https://packagist.org/). We recommend this method

* Do a manual install

Both these ways involve locating and installing the Cash App Afterpay Extension for Adobe Commerce (Magento 2). Composer does this task automatically. For manual installations, you must locate and download these public repos for Adobe Commerce (Magento 2):

* [Cash App Afterpay Extension for Magento 2](https://github.com/afterpay/afterpay-magento-2)

* [Cash App Pay Extension for Magento 2](https://github.com/afterpay/cash-app-pay-magento-2)

You can also use the "headless" methods, GraphQL and REST API. See the [Headless Support](#headless-support) section below.

## Composer

We recommend you use [Composer](https://getcomposer.org) to manage your repos and dependencies. This is a recommendation, not a requirement.

If you use Composer, make sure you install the correct module version that corresponds to your Adobe Commerce/Magento version. For example, module version 5.x works with Magento 2.4.x. The various modules and their corresponding Commerce/Magento version appear in this [GitHub table](https://github.com/afterpay/afterpay-magento-2#install-using-composer-recommended). See Step 2 below.

Do the following:

1. In Composer, open the Command Line Interface (CLI) and go to the *Adobe Commerce* project root directory on your server.

2. In the CLI, run this command to install the Cash App Afterpay module:  `composer require afterpay-global/module-afterpay`. See the [GitHub table](https://github.com/afterpay/afterpay-magento-2#install-using-composer-recommended) for the specific Cash App Afterpay module you need to specify.

3. Make sure that Composer finishes the installation without errors.

4. Run the Adobe Commerce setup upgrade: `php bin/magento setup:upgrade`.

5. Run the Adobe Commerce Dependencies Injection Compile: `php bin/magento setup:di:compile`.

6. Run the Adobe Commerce Static Content deployment: `php bin/magento setup:static-content:deploy`.

7. Run the Adobe Commerce System Cache Flush: `php bin/magento cache:flush`.

## Manual Procedure

This method does not use Composer. It is a more complex than using Composer, but just as effective when done correctly. Follow the instructions below.

### Download the Cash App Afterpay Extension

The extension is on the GitHub. Do the following:

1. Go to the GitHub for the link to [Magento 2](https://github.com/afterpay/afterpay-magento-2) for the most up-to-date version.

<Note>
  The Cash App Afterpay plugins and associated information are all in the [Afterpay-Magento-2](https://github.com/afterpay/afterpay-magento-2) part of the GitHub.
</Note>

The source code needed depends on your version of Magento. See the Readme file in the [Afterpay-Magento-2](https://github.com/afterpay/afterpay-magento-2) part of GitHub.

2. Under the green *Code* heading, click **HTTPS** and click **Download ZIP**. See screenshot below:

![adobe-comm-manual-install.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/adobe-comm-manual-install.png)

3. Unzip your files and put them into a temporary folder.

<Info title="Install Folder">
  You can install Adobe Commerce in any folder on your server. In this guide, \[ADOBE-COMMERCE] is the name of the root folder where Adobe Commerce is installed.
</Info>

## Run the Commands

1. Create the folder `Afterpay/Afterpay` in \[ADOBE-COMMERCE]/app/code.

2. Copy the files from your temporary folder to the `Afterpay/Afterpay` folder. The temporary folder is the one you created in Step 3 in the *Download the Afterpay Extension* section above.

3. Open the Command Line Interface (CLI) and make sure you are the owner of the \[ADOBE-COMMERCE] folder. Run all the CLI commands as the owner of the folder, not `root` and without `sudo`.

4. From the CLI, run the commands below:

| Command                                          | Description                                    |
| :----------------------------------------------- | :--------------------------------------------- |
| php bin/magento module:enable Afterpay\_Afterpay | Enable Afterpay extension.                     |
| php bin/magento setup:upgrade                    | Adobe Commerce setup upgrade.                  |
| php bin/magento setup:di:compile                 | Adobe Commerce dependencies injection compile. |
| php bin/magento setup:static-content:deploy      | Adobe Commerce static content deployment.      |
| php bin/magento cache:flush                      | Adobe Commerce system cache flush.             |

Now you need to repeat the process for the *Cash App Pay Extension for Magento 2*:

1. Create the folder `Afterpay/CashApp` in \[ADOBE-COMMERCE]/app/code.

2. Download and copy the files to the `Afterpay/CashApp` folder. The source code path is based on the Magento version [here](https://github.com/afterpay/cash-app-pay-magento-2).

3. Open the Command Line Interface (CLI) and run the commands below:

| Command                                         | Description                                    |
| :---------------------------------------------- | :--------------------------------------------- |
| php bin/magento module:enable Afterpay\_CashApp | Enable the Cash App Pay extension.             |
| php bin/magento setup:upgrade                   | Adobe Commerce setup upgrade.                  |
| php bin/magento setup:di:compile                | Adobe Commerce dependencies injection compile. |
| php bin/magento setup:static-content:deploy     | Adobe Commerce static content deployment.      |
| php bin/magento cache:flush                     | Adobe Commerce system cache flush.             |

You can find a table of the Afterpay Plugins for Adobe Commerce/Magento 2 [here](https://github.com/afterpay/afterpay-magento-2#install-manually). It also contains useful information on the manual installation process.

## Headless Support

You can also use [GraphQL](https://graphql.org/) or the [REST API](https://en.wikipedia.org/wiki/REST) to use Cash App Afterpay together with Adobe Commerce.

For details, see the following web pages on the GitHub:

* [Afterpay GraphQL Support page](https://github.com/afterpay/afterpay-magento-2/blob/main/Docs/GraphQL.md)

* [REST API page](https://github.com/afterpay/afterpay-magento-2/blob/main/Docs/RestAPI.md)
