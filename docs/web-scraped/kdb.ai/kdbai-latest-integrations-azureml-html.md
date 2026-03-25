# Source: https://code.kx.com/kdbai/latest/integrations/azureml.html

Title: KDB.AI on Azure Machine Learning

URL Source: https://code.kx.com/kdbai/latest/integrations/azureml.html

Markdown Content:
KDB.AI Server on Azure AI Tech Stack
------------------------------------

_This section details how to utilize Microsoft Azure OpenAI with KDB.AI Server._

You can significantly speed up the process of building and deploying AI applications by accessing fully configured instances of [KDB.AI](https://kdb.ai/), [Azure Machine Learning (AzureML)](https://azure.microsoft.com/en-us/products/machine-learning/), and [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service).

This guide shows you how to deploy a complete technical stack and start building AI-powered applications with [KDB.AI](https://kdb.ai/) samples already loaded.

Prerequisites
-------------

Before you can [deploy](https://code.kx.com/kdbai/latest/integrations/azureml.html#deploy) and [setup](https://code.kx.com/kdbai/latest/integrations/azureml.html#setup) KDB.AI on Azure Machine Learning Studio, ensure you have fulfilled the following prerequisites.

### Azure account and permissions

*   Ensure you have an active account for [Azure Machine Learning Studio](https://ml.azure.com/).
*   Enable the [Azure OpenAI](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) service in the subscription you wish to use. To submit an application, navigate [here](https://aka.ms/oai/access).
*   Deploy to the Sweden Central region ONLY due to [model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?view=azureml-api-2#model-summary-table-and-region-availability).
*   Ensure the person deploying from Azure Marketplace has set the following role based access control permissions for you:
    *   If you are creating a new resource group, you need **Owner** role on the subscription you want to deploy into.
    *   If you have an existing resource group, you need the **User Access Administrator** role on the subscription and **Owner** role on the resource group that you want to deploy into.

*   Have at least four Dedicated Cores within Azure ML available in your region. This can be checked [here](https://ml.azure.com/quota).

Only the user deploying the solution is able to access and use the Azure ML workspace. A [compute instance](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#training-compute-targets) cannot be shared with other users in your workspace.

### KDB.AI license

Ensure you have signed up for a [KDB.AI license](https://kx.com/kdb-ai-server-download) and have accepted KX's end user license agreement. After accepting the KDB.AI license agreement, you will receive an email containing setup instructions and your license file. The license file is needed as part of the deployment process workflow.

Bearer token
------------

Once you receive your registration email, you need to obtain a bearer token.

1.   Log into the [KX downloads portal](https://portal.dl.kx.com/).
2.   Once authenticated, navigate to [https://portal.dl.kx.com/auth/token](https://portal.dl.kx.com/auth/token).
3.   Click **ADD NEW BEARER TOKEN**.
4.   Click **COPY BEARER**.
5.   Paste this somewhere until you need it later; you can only view the bearer token once.

Deploy
------

Once the prerequisites are met, do the following.

You can watch an overview video [here](https://vimeo.com/901470192/fae3716b62) or follow the steps below.

1.   Login to [Azure Marketplace](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/selectedMenuItemId/home).
2.   Enter **KDB.AI** into the **Search the Marketplace** field on the **Get Started** page.
3.   On the **KDB.AI Server** plan, click **Create > KDB.AI Server with Azure AI Services**.

![Image 1: Launch Azure Marketplace](https://code.kx.com/kdbai/latest/images/launch-azure-ml.png)

### Basics tab

1.   In the **Project details** area, select the **Subscription** that has the OpenAI Service enabled.
2.   Then either select an existing **Resource group**, or create a new one.
3.   In the **Instance details** area, ensure the **Region** is set to **Sweden Central**.
4.   Enter a **Base resource name** that is unique across your deployments.
5.   Click **Next**.

### Credentials tab

1.   Add your **KX License** as received in your registration email.
2.   Enter your **Username for KX Downloads portal**.
3.   Add your **Bearer token for KX Downloads portal**.
4.   Confirm your **Bearer token for KX Downloads portal**.

### Configuration tab

1.   Select your **Compute SKU** requirement.
2.   Select your required **Storage Size (GB)**.
3.   In the **IP address of the client connecting to Azure ML Studio** field, enter the Public IP address of the machine from which you wish to connect to Azure AI Machine Learning Studio.
4.   Optional: enter the **Object Id** of a Group whose members can later upgrade KDB.AI to a newer version.
5.   Click **Next**.

### API Keys tab

To enable all notebook features, enter your API keys. These keys are securely stored in the Azure Key Vault for automatic loading. Alternatively, you can leave these fields blank and enter the keys later when needed.

### Review + create tab

Review your details and click **Create**.

If you have any difficulty during sign-up, please contact [Support](mailto:support@kdb.ai) or join our [Slack channel](http://kx.com/slack) so we can help resolve your issues.

Setup
-----

Now you have deployed the product and logged into Azure, follow the steps to start using KDB.AI.

1.   Navigate to your ![Image 2: Azure Machine Learning workspace](https://code.kx.com/kdbai/latest/images/AzureMLworkspace.svg)**Azure Machine Learning workspace** in the newly created **Resource Group** and click the ![Image 3: Launch studio](https://code.kx.com/kdbai/latest/images/LaunchStudio.png) button.
2.   Open **Notebooks** from the **Authoring** section in the left-hand side menu.
3.   Navigate to the **KDBAI** folder under the **Files** tab, which contains a set of samples.
4.   Open the Jupyter Notebook you wish to run.
5.   Check the selected kernel is **Python 3.10 - SDK v2** in the top right-hand area of the window. If it is not, select it from the drop down menu.
6.   To run the sample, you can either run each cell individually or click **Run all cells**.
7.   Once the Notebook runs you should see the output of each step below the cell.

Troubleshooting
---------------

If you cannot see the **Files** tab in **Authoring**/**Notebooks** it may be because your Public IP has changed since the deployment.

*   Navigate to the ![Image 4: Storage Accounts](https://code.kx.com/kdbai/latest/images/StorageAccounts.svg)**Storage account** called **st** + **Base resource name** in the newly created **Resource Group**.
*   Follow this [tutorial](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-from-an-internet-ip-range) to **Add your client IP address** and **Save** it.

If you need help, feel free to reach out to the KDB.AI [Slack community](http://kx.com/slack) or email [support@kdb.ai](mailto:support@kdb.ai).

Next steps
----------

Now that you have KDB.AI running on Azure ML, read our [KDB.AI documentation](https://code.kx.com/kdbai) to learn how to set up your tables and insert some data, or walk through our [Quickstart Guide](https://code.kx.com/kdbai/latest/gettingStarted/quickstart.html), which outlines how you can create a vector index and query it with semantic search.

If you are new to vector databases, read our [Fundamentals](https://kdb.ai/learning-hub#fundamentals) articles to give you the rundown. These include a vector embeddings explainer, methods of similarity search, vector indexing basics, and more.

You are responsible for procuring and for the cost of cloud services, which are subject to their own terms and conditions. Cloud services pricing is based on [Azure’s pricing calculator](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/).

Azure links
-----------

Here are some useful links to information on using the Azure services.

*   [Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/?view=azureml-api-2)
*   [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
*   [Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)
