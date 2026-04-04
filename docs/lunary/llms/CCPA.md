# Source: https://docs.lunary.ai/docs/more/security/CCPA.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# CCPA compliance guide

For those serving Californian users, grasping the nuances of secure and private data handling is crucial. Lunary, capable of being integrated into your own infrastructure without accessing your data, stands as a highly compliant CCPA observability solution.

This guide delves into [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa), the types of data that need safeguarding, and how to to ensure your logs collection align with CCPA standards.

## What is the CCPA?

The CCPA empowers consumers with control over their personal data held by businesses, offering:

* Knowledge of, and details on, how their personal data is collected, utilized, and shared
* The ability to erase their personal data, subject to certain conditions
* The option to refuse the sale of their personal data
* Protection against discrimination when they exercise their CCPA rights.

## What data is protected under CCPA?

CCPA rights are exclusive to individuals residing in California, including those temporarily away from the state.

For-profit entities are subject to CCPA if they meet any of the criteria below:

* Their annual gross revenue exceeds \$25 million.
* They engage in buying, receiving, or selling the personal data of more than 50,000 California residents, households, or devices.
* At least 50% of their yearly revenue comes from selling the personal data of California residents.

Under CCPA, personal information encompasses data that can identify or be associated with an individual.

Essentially, personal information includes anything linked to an identifiable person, ranging from social security numbers and license plates to photographs, email addresses, web addresses, IP addresses, or pseudonyms.

## What is the impact of CCPA on observability?

Under CCPA, businesses are mandated to provide a "notice at collection" to consumers. This entails informing users upon registration about the utilization of their data to enhance the product.

Such a notice should enumerate the types of personal information collected and the reasons for its collection. Additionally, it must include a link to the privacy policy for further information on privacy practices.

CCPA also mandates the ability for users to request the deletion of their personal information, with businesses required to comply within 45 days.

## How to set Lunary up for CCPA compliance

Lunary can be hosted on your onwn infrastructure, giving you complete control over data management. This includes deciding the hosting location for personal information and full authority over the database, enabling straightforward sharing or deletion of individual data.

### Step 1: Choose how to host Lunary

For complete control of end-users' data, we recommend hosting Lunary on your own infrastructure, or a private cloud such as AWS, Google Cloud Platform or Microsoft Azure. A simpler alternative is to use Lunary Cloud, where we handle the infrastructure and security for you.

### Step 2: Deploy Lunary

If using Lunary Cloud, simply follow the steps in the onboarding process to start sending events. Read our [getting started guide](/docs/get-started) for more information on sending logs to Lunary. 

Setting up Lunary on your own infrastructure is simple, and our team is here to assist with any issues that arise. Begin by consulting our [self-hosting guide](/docs/more/self-hosting/docker).

### Step 3: Security configuration

Our SDKs used with Lunary Cloud utilize HTTPS to ensure the security of data during transmission. When self-hosting Lunary, we strongly recommend using HTTPS as well to secure data transmission.

It is highly advised to restrict access to Lunary and its underlying infrastructure strictly to individuals who have authorization and a legitimate need to interact with the data, this includes links to shared dashboards.

## Deleting personal information in Lunary

Users should have the capability to demand the deletion of their data. The method through which you accommodate such requests is at your discretion. For instance, you might choose to receive these requests through email or by a form.

You can remove a user from a Lunary instance via the Lunary user interface. To do this:

* Select "Users" from the sidebar menu
* Search and click on the concerned user
* Click "Delete" to remove them and all their associated data from Lunary.
