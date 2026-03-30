# Source: https://help.aikido.dev/virtual-machine-scanning/azure/azure-virtual-machine-scanning-setup.md

# Azure Virtual Machine Scanning Setup

> This functionality is currently behind feature flag and available for Advanced plans only. [Contact us](https://www.aikido.dev/contact) for more information.

### Why should I scan my virtual machines? <a href="#why-should-i-scan-my-virtual-machines" id="why-should-i-scan-my-virtual-machines"></a>

With virtual machine scanning, Aikido can scan the hard drives of your virtual machines for vulnerable packages, outdated runtimes and risky licenses.

### Getting started <a href="#getting-started" id="getting-started"></a>

To enable the scanning of your virtual machines on Azure, you should first start by connecting your Azure Cloud to Aikido. To do this you can follow the steps outlined in [this article](https://help.aikido.dev/cloud-scanning/connect-your-cloud/azure/connect-azure-cloud-account-to-aikido).

Once your cloud is connected, you'll see a tab appear on the detail page called 'Virtual Machines'.

![Azure dashboard prompting to activate virtual machine scanning for security and compliance checks.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-464cc9ed19a44e341779fcfaf0e565656d4425e8%2Fazure-virtual-machine-scanning-setup_73f430a6-1621-4290-b258-dc4d89a3696b.png?alt=media)

When you click on 'Set Up VM Scanning' we'll take you to the following page:

![Azure VM scanning setup instructions with Application ID entry field.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7155800934971305220e41cabe27ba528fc737a8%2Fazure-virtual-machine-scanning-setup_8fe87a31-930a-43ab-a32c-6199bf0d4320.png?alt=media)

The setup wizard will guide you through creating a new App Registration inside of the Azure Portal with an API secret specifically for Aikido.

The API secret will be used by Aikido to make the necessary API requests to scan your resources. Aikido will notify you via email when the secret is about to expire.

Only the bare minimum of permissions are granted to the App Registration. This ensures that Aikido can perform its security checks without the risk of unintended altering of your resources.

Once you click 'save', Aikido will immediately start to discover any virtual machines in your account and scan them.
