# Source: https://clickhouse.ferndocs.com/cloud/billing/marketplace/aws-marketplace-committed-contract.md

---
slug: /cloud/billing/marketplace/aws-marketplace-committed-contract
title: AWS Marketplace Committed Contract
description: Subscribe to ClickHouse Cloud through the AWS Marketplace (Committed Contract)
keywords:
  - aws
  - amazon
  - marketplace
  - billing
  - committed
  - committed contract
doc_type: guide
---

Get started with ClickHouse Cloud on the [AWS Marketplace](https://aws.amazon.com/marketplace) via a committed contract. A committed contract, also known as a a Private Offer, allows customers to commit to spending a certain amount on ClickHouse Cloud over a period of time.

## Prerequisites [#prerequisites]

- A Private Offer from ClickHouse based on specific contract terms.
- To connect a ClickHouse organization to your committed spend offer, you must be an admin of that organization.

[Required permissions to view and accept your committed contract in AWS](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-offers-page.html#private-offers-page-permissions):
- If you use AWS managed policies it is required to have the following permissions: `AWSMarketplaceRead-only`, `AWSMarketplaceManageSubscriptions`, or `AWSMarketplaceFullAccess`.
- If you aren't using AWS managed policies it is required to have the following permissions: IAM action `aws-marketplace:ListPrivateListings` and `aws-marketplace:ViewSubscriptions`.

## Steps to sign up [#steps-to-sign-up]

1. You should have received an email with a link to review and accept your private offer.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/1248ca0912219768198de910cff4fb4c7a85fc73cd264d306aa07f85669b0083/images/cloud/manage/billing/marketplace/aws-marketplace-committed-1.png" alt="AWS Marketplace private offer email"/>

<br />

2. Click on the **Review Offer** link in the email. This should take you to your AWS Marketplace page with the private offer details. While accepting the private offer, choose a value of 1 for the number of units in the Contract Options picklist. 

3. Complete the steps to subscribe on the AWS portal and click on **Set up your account**.
It is critical to redirect to ClickHouse Cloud at this point and either register for a new account, or sign in with an existing account. Without completing this step, we will not be able to link your AWS Marketplace subscription to ClickHouse Cloud.

4. Once you redirect to ClickHouse Cloud, you can either login with an existing account, or register with a new account. This step is very important so we can bind your ClickHouse Cloud organization to the AWS Marketplace billing.

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

5. After successfully logging in, a new ClickHouse Cloud organization will be created. This organization will be connected to your AWS billing account and all usage will be billed via your AWS account.

6. Once you login, you can confirm that your billing is in fact tied to the AWS Marketplace and start setting up your ClickHouse Cloud resources.

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d97b126cd052c4da328646d8919f96c78a53242802ecb9c505f4a00fe9d27f34/images/cloud/manage/billing/marketplace/aws-marketplace-payg-10.png" alt="ClickHouse Cloud view AWS Marketplace billing"/>

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5830db16a0831990d40f5e0615f9a9381161da98f16e0d1224aa929bee6a1f17/images/cloud/manage/billing/marketplace/aws-marketplace-payg-11.png" alt="ClickHouse Cloud new services page"/>

<br />

6. You should receive an email confirming the sign up:

<br />

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/a622bb0935979c14d24741692e8bd98c017b39d509ccfdf47aadaac80ac1134a/images/cloud/manage/billing/marketplace/aws-marketplace-payg-12.png" alt="AWS Marketplace confirmation email"/>

<br />

If you run into any issues, please do not hesitate to contact [our support team](https://clickhouse.com/support/program).
