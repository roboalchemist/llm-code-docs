# Source: https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/viewing-billing-and-usage.md

# Viewing billing or usage information

This page explains how to view your billing and usage information. If you are concerned that you might be close to the LOC (number of lines of code) limit defined in your subscription plan, you can check your current consumption as described below. For more information, see [#loc-based-pricing](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/subscription-plans#loc-based-pricing "mention"). To change the LOC limit, see [changing-plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/changing-plan "mention").

{% hint style="info" %}
The LOC is a metric (`ncloc`) that you can also retrieve through the [web-api](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/web-api "mention") by using the `/api/measures` endpoint. See [metric-definitions](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions "mention") for more information.
{% endhint %}

### Viewing your organization’s billing and usage information <a href="#organization-information" id="organization-information"></a>

To view your organization’s billing and usage information, you must be an admin of the organization. Proceed as follows:

1. Retrieve your organization. See [viewing-organizations](https://docs.sonarsource.com/sonarqube-cloud/getting-started/viewing-organizations "mention") for more details.
2. Select the **Billing & Usage** tab.\
   The dashboard shows details of the total LOC analyzed to date and the total number of projects.\
   If your organization belongs to an enterprise:
   * &#x20;If your organization uses the shared LOCs, you will see the usage of the shared LOCs. For more information about shared LOCs, see [#about-enterprise-loc-limit](https://docs.sonarsource.com/sonarqube-cloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise#about-enterprise-loc-limit "mention").
   * You will see the subscription status of the enterprise add-ons.
3. Click on the number of projects to view a breakdown of the number of lines of code contained in each project within your organization.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-56221cea9fe6f1244c6b607449bd59a1d9b7ee76%2F9f6e27334c63cf8cec863b69365ee536b9a8c4e3.png?alt=media" alt="SonarQube Cloud shows you the lines of code distribution per project." width="375"><figcaption></figcaption></figure></div>

### Viewing your enterprise’s billing and usage information <a href="#enterprise-information" id="enterprise-information"></a>

To view your enterprise’s billing and usage information, you must be an admin of the enterprise. Proceed as follows:

1. Retrieve your enterprise. See [retrieving-and-viewing-your-enterprise](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-enterprise/retrieving-and-viewing-your-enterprise "mention") for more details.
2. Select the **Billing and Usage** tab.&#x20;

The dashboard shows:

1. The characteristics of your enterprise plan with the subscription status of the enterprise add-ons (add-ons require a separate subscription to your Enterprise license).
2. Usage information:
   * An overview of the lines of code consumption. For more details, see [#loc-consumption](https://docs.sonarsource.com/sonarqube-cloud/managing-enterprise/managing-the-lines-of-code-within-your-enterprise#loc-consumption "mention").

<figure><img src="broken-reference" alt="The Billing and Usage tab of your enterprise shows (1) your current plan&#x27;s characteristics and (2) your usage information."><figcaption></figcaption></figure>

### Related pages <a href="#related-pages" id="related-pages"></a>

* [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention")
* [billing-model](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/billing-model "mention")
* [signing-up-for-plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/signing-up-for-plan "mention")
* [changing-plan](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/changing-plan "mention")
* [updating-billing-payment-details](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/updating-billing-payment-details "mention")
* [viewing-taxes-and-invoices](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/viewing-taxes-and-invoices "mention")
