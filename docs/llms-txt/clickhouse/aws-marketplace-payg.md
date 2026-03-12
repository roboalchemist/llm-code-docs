# Source: https://clickhouse.ferndocs.com/cloud/billing/marketplace/aws-marketplace-payg.md

---
slug: /cloud/billing/marketplace/aws-marketplace-payg
title: AWS Marketplace PAYG
description: Subscribe to ClickHouse Cloud through the AWS Marketplace (PAYG).
keywords:

- aws
- marketplace
- billing
- PAYG
doc_type: guide

---

Get started with ClickHouse Cloud on the [AWS Marketplace](https://aws.amazon.com/marketplace) via a PAYG (Pay-as-you-go) Public Offer.

## Prerequisites [#prerequisites]

- An AWS account that is enabled with purchasing rights by your billing administrator.
- To purchase, you must be logged into the AWS marketplace with this account.

## Steps to sign up [#steps-to-sign-up]

1. Go to the [AWS Marketplace](https://aws.amazon.com/marketplace) and search for ClickHouse Cloud.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c3b73ed0244db6637ade56d9f2c5890775bd4b2520f5b037d9c663fe8720a2c1/images/cloud/manage/billing/marketplace/aws-marketplace-payg-1.png" alt="AWS Marketplace home page"/>

<br />

1. Click on the [listing](https://aws.amazon.com/marketplace/pp/prodview-jettukeanwrfc) and then on **View purchase options**.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/cb4afb400d981c4dca827933918fd32542dce74c248d3758f636d0d646bba1d2/images/cloud/manage/billing/marketplace/aws-marketplace-payg-2.png" alt="AWS Marketplace search for ClickHouse"/>

<br />

1. On the next screen, configure the contract:

- **Length of contract** - PAYG contracts run month to month.
- **Renewal settings** - You can set the contract to auto-renew or not.
Note that we strongly recommend keeping your subscription set to auto-renew every month. However, if you don't enable auto renewal, your organization is automatically put into a grace period at the end of the billing cycle and then decommissioned.

- **Contract options** - You can input any number (or just 1) into this text box. This will not affect the price you pay as the price for these units for the public offer is $0. These units are usually used when accepting a private offer from ClickHouse Cloud.

- **Purchase order** - This is optional and you can ignore this.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/7ad47ead94b257d186f9ccb6b09440e2f32a06e1bdaf6ae94435f93b2819a80e/images/cloud/manage/billing/marketplace/aws-marketplace-payg-3.png" alt="AWS Marketplace configure contract"/>

<br />

After filling out the above information, click on **Create Contract**. You can confirm that the contract price displayed is zero dollars which essentially means that you have no payment due and will incur charges based on usage.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d5f8e8180d9dd477319b3e3da9145f24fbffdd226a47939b0a649d4ca285ea0e/images/cloud/manage/billing/marketplace/aws-marketplace-payg-4.png" alt="AWS Marketplace confirm contract"/>

<br />

1. Once you click **Create Contract**, you will see a modal to confirm and pay ($0 due).

2. Once you click **Pay now**, you will see a confirmation that you are now subscribed to the AWS Marketplace offering for ClickHouse Cloud.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/4303ed8d4d7c4d9472fa3192739690223f2383419288621497d772b57cec4227/images/cloud/manage/billing/marketplace/aws-marketplace-payg-5.png" alt="AWS Marketplace payment confirmation"/>

<br />

1. Note that at this point, the setup is not complete yet. You will need to redirect to ClickHouse Cloud by clicking on **Set up your account** and signing up on ClickHouse Cloud.

2. Once you redirect to ClickHouse Cloud, you can either login with an existing account, or register with a new account. This step is very important so we can bind your ClickHouse Cloud organization to the AWS Marketplace billing.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/456e9f4349c565fad9ecb887af68cff897cea41af22fcef57211da480b06ac4f/images/cloud/manage/billing/marketplace/aws-marketplace-payg-6.png" alt="ClickHouse Cloud sign in page"/>

<br />

If you are a new ClickHouse Cloud user, click **Register** at the bottom of the page. You will be prompted to create a new user and verify the email. After verifying your email, you can leave the ClickHouse Cloud login page and login using the new username at the [https://console.clickhouse.cloud](https://console.clickhouse.cloud).

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/747917f640d6b341f6945ee8f241723832ca5f265a1835ff81789f4619ade436/images/cloud/manage/billing/marketplace/aws-marketplace-payg-7.png" alt="ClickHouse Cloud sign up page"/>

<br />

Note that if you are a new user, you will also need to provide some basic information about your business. See the screenshots below.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/75cc7a4200498561b719996f94de317bc491f3f32516e89b99a80c3451bcd290/images/cloud/manage/billing/marketplace/aws-marketplace-payg-8.png" alt="ClickHouse Cloud sign up info form"/>

<br />

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fac70322f81c9626022cbf9900ec42f36ad09898a744ef1f7e229ff1d7cdcc2d/images/cloud/manage/billing/marketplace/aws-marketplace-payg-9.png" alt="ClickHouse Cloud sign up info form 2"/>

<br />

If you are an existing ClickHouse Cloud user, simply log in using your credentials.

1. After successfully logging in, a new ClickHouse Cloud organization will be created. This organization will be connected to your AWS billing account and all usage will be billed via your AWS account.

2. Once you login, you can confirm that your billing is in fact tied to the AWS Marketplace and start setting up your ClickHouse Cloud resources.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d97b126cd052c4da328646d8919f96c78a53242802ecb9c505f4a00fe9d27f34/images/cloud/manage/billing/marketplace/aws-marketplace-payg-10.png" alt="ClickHouse Cloud view AWS Marketplace billing"/>

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5830db16a0831990d40f5e0615f9a9381161da98f16e0d1224aa929bee6a1f17/images/cloud/manage/billing/marketplace/aws-marketplace-payg-11.png" alt="ClickHouse Cloud new services page"/>

<br />

1. You should receive an email confirming the sign up:

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a622bb0935979c14d24741692e8bd98c017b39d509ccfdf47aadaac80ac1134a/images/cloud/manage/billing/marketplace/aws-marketplace-payg-12.png" alt="AWS Marketplace confirmation email"/>

<br />

If you run into any issues, please do not hesitate to contact [our support team](https://clickhouse.com/support/program).
