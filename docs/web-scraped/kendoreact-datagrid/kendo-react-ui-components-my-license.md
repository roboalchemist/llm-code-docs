# Source: https://www.telerik.com/kendo-react-ui/components/my-license

Title: React Licensing Activating Your License Key - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/my-license

Markdown Content:
New to KendoReact?[Start a free 30-day trial](https://www.telerik.com/try/kendo-react-ui)

Updated

on Feb 17, 2026

In this article, you’ll learn how to activate the KendoReact premium components and features by installing a license key.

KendoReact is an enterprise-grade UI library with 120+ free and premium components. You can use the [50+ free components and features of KendoReact](https://www.telerik.com/kendo-react-ui/components/free), even in production, no license required.

**Important**: To work with any premium KendoReact components and features, you must install a license key file in your project. This requirement applies to:

*   **Trial usage**: Download and install a trial license key file to evaluate premium features
*   **Commercial usage**: Download and install a commercial license key file for production use

Without a valid license key file, premium components will display licensing warnings and watermarks, which can interrupt your development and user experience.

The license key installation process involves the following steps:

1.   [Purchase](https://www.telerik.com/kendo-react-ui/pricing#subscription) a commercial license or [start a trial](https://www.telerik.com/try/kendo-react-ui).
2.   [Download a license key.](https://www.telerik.com/kendo-react-ui/components/my-license#download-your-license-key-file)
3.   [Install or update your license key file in your project.](https://www.telerik.com/kendo-react-ui/components/my-license#install-or-update-the-license-key-file-in-your-project)

If you’re in a hurry, skip the rest of the article and run this command sequence in your project terminal to download and activate your license:

sh

```
npm install --save @progress/kendo-licensing
npx kendo-ui-license refresh && npx kendo-ui-license activate
```

[Download Your License Key File](https://www.telerik.com/kendo-react-ui/components/my-license#download-your-license-key-file)
-----------------------------------------------------------------------------------------------------------------------------

> To download a license key for KendoReact, you must have either a developer license or a trial license. If you are new to KendoReact, [sign up for a free trial](https://www.telerik.com/try/kendo-react-ui) first and then follow the steps below.

Use the `refresh` command provided by the kendo-licensing package to download a fresh copy of your license key file. The command-line utility will launch your default browser and ask you to log in to telerik.com.

sh

`npx -y @progress/kendo-licensing refresh`

The license key file will be saved in the current user's home directory:

*   For Mac/Linux: `~/.telerik/telerik-license.txt`

To download the license key file to a different location, use the `--output` parameter and specify a path or file name:

sh

`npx -y @progress/kendo-licensing refresh --output kendo-ui-license.txt`

Alternatively, [use your browser to download the license key file](https://www.telerik.com/kendo-react-ui/components/knowledge-base/downloading-license-key) and place it in the current user's home directory.

[Install or Update the License Key File in Your Project](https://www.telerik.com/kendo-react-ui/components/my-license#install-or-update-the-license-key-file-in-your-project)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you start a new trial, purchase a new KendoReact license, or renew an existing one, always download and install a new license key. The new license key includes information about all previous license purchases. The procedure for the installation of a new license key and the update of a license key is the same:

1.   Install `@progress/kendo-licensing` as a project dependency:

sh `npm i @progress/kendo-licensing` 
2.   Run the activate command in the console:

sh `npx kendo-ui-license activate` 

If the invalid license attributes are still displayed after you have installed or updated the license key, see the [Troubleshooting License Activation](https://www.telerik.com/kendo-react-ui/components/my-license/license-errors-and-warnings) article and the [FAQ](https://www.telerik.com/kendo-react-ui/components/my-license/faq) page for more information.

> If both the `TELERIK_LICENSE` environment variable and the `telerik-license.txt` file are present, then the environment variable will be used.

> When renewing your subscription, always regenerate and reactivate the license key. This will allow you to update the KendoReact components in your application. Each licensing file contains information about the validity of your subscription and can be used for all KendoReact versions published before its expiration date.

[Automatic License Key File Management in Visual Studio Code](https://www.telerik.com/kendo-react-ui/components/my-license#automatic-license-key-file-management-in-visual-studio-code)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [Kendo UI Productivity Tools extension](https://marketplace.visualstudio.com/items?itemName=KendoUI.kendotemplatewizard) can automatically download and manage your license key file. Simply log in to your Telerik or Kendo UI account from Visual Studio Code to enable this feature. For more information, see the [Kendo UI Productivity Tools](https://www.telerik.com/kendo-react-ui/components/installation/vscode-extensions) documentation.

[Troubleshooting](https://www.telerik.com/kendo-react-ui/components/my-license#troubleshooting)
-----------------------------------------------------------------------------------------------

If you have a valid license key, and the `License activation failed` warning appears in the terminal, performing a clean, fresh install usually resolves it. To do this, follow these instructions:

1.   Run `rm -rf node_modules` to remove all installed packages.

sh `rm -rf node_modules package-lock.json yarn.lock` 
2.   Install all packages in the project.

sh `npm i` 
3.   Run the activate command again:

sh `npx kendo-ui-license activate` 

If the invalid license attributes are still displayed after you have installed or updated the license key, see the [License Activation Errors and Warnings](https://www.telerik.com/kendo-react-ui/components/my-license/license-errors-and-warnings) and the [FAQs](https://www.telerik.com/kendo-react-ui/components/my-license/faq) articles for more information.

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/my-license#suggested-links)
-----------------------------------------------------------------------------------------------

*   [Adding the License Key to CI Services](https://www.telerik.com/kendo-react-ui/components/my-license/ci-services)
*   [Per-Project License Key Setup](https://www.telerik.com/kendo-react-ui/components/knowledge-base/license-per-project-setup)
*   [License Activation Errors and Warnings](https://www.telerik.com/kendo-react-ui/components/my-license/license-errors-and-warnings)
*   [Frequently Asked Questions](https://www.telerik.com/kendo-react-ui/components/my-license/faq)
*   [Get Started with KendoReact Free](https://www.telerik.com/kendo-react-ui/components/free)
