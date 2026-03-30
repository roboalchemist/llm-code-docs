# Source: https://clickhouse.ferndocs.com/cloud/billing/marketplace/azure-marketplace-committed-contract.md

---
slug: /cloud/billing/marketplace/azure-marketplace-committed-contract
title: Azure Marketplace Committed Contract
description: >-
  Subscribe to ClickHouse Cloud through the Azure Marketplace (Committed
  Contract)
keywords:
  - Microsoft
  - Azure
  - marketplace
  - billing
  - committed
  - committed contract
doc_type: guide
---

Get started with ClickHouse Cloud on the [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps) via a committed contract. A committed contract, also known as a a Private Offer, allows customers to commit to spending a certain amount on ClickHouse Cloud over a period of time.

## Prerequisites [#prerequisites]

- A Private Offer from ClickHouse based on specific contract terms.

## Steps to sign up [#steps-to-sign-up]

1. You should have received an email with a link to review and accept your private offer.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/ccc76e786894ec8ca705814d69227c4f96311ca33360a22d83029e1621fe7e8c/images/cloud/manage/billing/marketplace/azure-marketplace-committed-1.png" alt="Azure Marketplace private offer email"/>

<br />

2. Click on the **Review Private Offer** link in the email. This should take you to your GCP Marketplace page with the private offer details.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4c2c5700f394da1fd32aea1ef57a2887ada697e5a2461d07e357287e85c75b1c/images/cloud/manage/billing/marketplace/azure-marketplace-committed-2.png" alt="Azure Marketplace private offer details"/>

<br />

3. Once you accept the offer, you will be taken to a **Private Offer Management** screen. Azure may take some time to prepare the offer for purchase.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d95fd754927b3418244d3d33ca41428aeff5da42f3ff313bde3f364edb6e783a/images/cloud/manage/billing/marketplace/azure-marketplace-committed-3.png" alt="Azure Marketplace Private Offer Management page"/>

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/8a7409fbc9d9b20837da9cfeef546f8ee35be176ec4f2cd2961cf0d144fad26e/images/cloud/manage/billing/marketplace/azure-marketplace-committed-4.png" alt="Azure Marketplace Private Offer Management page loading"/>

<br />

4. After a few minutes, refresh the page. The offer should be ready for **Purchase**.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b1ee45673dc0092f5aa088ba3fe534967707fe821689905f2cde743e8ad6314e/images/cloud/manage/billing/marketplace/azure-marketplace-committed-5.png" alt="Azure Marketplace Private Offer Management page purchase enabled"/>

<br />

5. Click on **Purchase** - you will see a flyout open. Complete the following:

<br />

- Subscription and resource group 
- Provide a name for the SaaS subscription
- Choose the billing plan that you have a private offer for. Only the term that the private offer was created (for example, 1 year) will have an amount against it. Other billing term options will be for $0 amounts. 
- Choose whether you want recurring billing or not. If recurring billing is not selected, the contract will end at the end of the billing period and the resources will be set to decommissioned.
- Click on **Review + subscribe**.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/db563eb24bb09f1bff1bdc5f8e13eafbb2314f8befd94482f3eeb95981319e23/images/cloud/manage/billing/marketplace/azure-marketplace-committed-6.png" alt="Azure Marketplace subscription form"/>

<br />

6. On the next screen, review all the details and hit **Subscribe**.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7f630dac63008c26db0b631a1b2e95bcc0463006947bb8d0e9e9da59226cd274/images/cloud/manage/billing/marketplace/azure-marketplace-committed-7.png" alt="Azure Marketplace subscription confirmation"/>

<br />

7. On the next screen, you will see **Your SaaS subscription in progress**.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d6fd934c5584c186b60851b02d1019acdc0fda32d5e469e873b676b97154cfc9/images/cloud/manage/billing/marketplace/azure-marketplace-committed-8.png" alt="Azure Marketplace subscription submitting page"/>

<br />

8. Once ready, you can click on **Configure account now**. Note that is a critical step that binds the Azure subscription to a ClickHouse Cloud organization for your account. Without this step, your Marketplace subscription is not complete.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e3a6c6bd628ab7d6bd63ed695de2c4f0ed4776f92b8162e65126985207a00fc3/images/cloud/manage/billing/marketplace/azure-marketplace-committed-9.png" alt="Azure Marketplace configure account now button"/>

<br />

9. You will be redirected to the ClickHouse Cloud sign up or sign in page. You can either sign up using a new account or sign in using an existing account. Once you are signed in, a new organization will be created that is ready to be used and billed via the Azure Marketplace.

10. You will need to answer a few questions - address and company details - before you can proceed.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/75cc7a4200498561b719996f94de317bc491f3f32516e89b99a80c3451bcd290/images/cloud/manage/billing/marketplace/aws-marketplace-payg-8.png" alt="ClickHouse Cloud sign up info form"/>

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fac70322f81c9626022cbf9900ec42f36ad09898a744ef1f7e229ff1d7cdcc2d/images/cloud/manage/billing/marketplace/aws-marketplace-payg-9.png" alt="ClickHouse Cloud sign up info form 2"/>

<br />

11. Once you hit **Complete sign up**, you will be taken to your organization within ClickHouse Cloud where you can view the billing screen to ensure you are being billed via the Azure Marketplace and can create services.

<br />

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fd3fe9a0f43dcc07b9c37a46b9ce5362ae5f5d116b0a5354aee80ab0a3d73bdd/images/cloud/manage/billing/marketplace/azure-marketplace-payg-11.png" alt="ClickHouse Cloud sign up info form"/>

<br />

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5d89d0571fc0d2038ff60530e5029f7d1cc1854404471567128749af6b776a1a/images/cloud/manage/billing/marketplace/azure-marketplace-payg-12.png" alt="ClickHouse Cloud sign up info form"/>

<br />

If you run into any issues, please do not hesitate to contact [our support team](https://clickhouse.com/support/program).
