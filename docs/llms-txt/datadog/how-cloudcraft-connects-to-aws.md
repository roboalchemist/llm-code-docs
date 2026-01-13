# Source: https://docs.datadoghq.com/cloudcraft/faq/how-cloudcraft-connects-to-aws.md

---
title: How does Cloudcraft connect to my AWS account?
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > FAQ > How does Cloudcraft connect to my AWS
  account?
source_url: https://docs.datadoghq.com/faq/how-cloudcraft-connects-to-aws/index.html
---

# How does Cloudcraft connect to my AWS account?

Cloudcraft uses cross-account roles to access your AWS account, which is considered [the secure way to access your AWS environment](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html) by AWS themselves. Because of this, you must create a secure read-only role in your AWS account that is specific to Cloudcraft and can easily be revoked at any time.

To restrict the access that Cloudcraft has even further, you can [create a stricter minimal access policy](https://docs.datadoghq.com/cloudcraft/advanced/minimal-iam-policy/) that gives read-only access to the components you want to use with Cloudcraft, further minimizing the amount of data the Cloudcraft role could theoretically access.

By design, Cloudcraft does not store the data from a live scan of your environment. The generated blueprints only contain the minimal information required for the graphical blueprint representation, as well as ARN identifiers for AWS resources that link the diagram components to the live data at runtime.

The data from your AWS environment is streamed in real-time to your browser via Cloudcraft's own AWS environment using role-based access, and is stored client-side while you are using the application. When you close the application, the live data is removed.

While not having write access to your account prevents Cloudcraft from offering certain features â like deleting an EC2 instance on both the diagram and your account â it is simply a more secure approach.

Cloudcraft implements rigorous security processes and controls as part of the SOC2 compliance program. You can read more about Cloudcraft's security program and controls on the [security page](https://www.cloudcraft.co/security).
