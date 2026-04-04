# Source: https://docs.fiddler.ai/getting-started/aws-sagemaker-partner-ai-app.md

# AWS SageMaker Partner AI App

### Introduction

The [Fiddler Partner AI App for Amazon SageMaker](https://aws.amazon.com/marketplace/pp/prodview-caia5ckldtyhs) brings enterprise-grade AI observability directly into your SageMaker environment. As a fully integrated Partner AI App, Fiddler enables data scientists and ML engineers to monitor, analyze, and protect their ML models, LLM applications, GenAI systems, and AI agents in a unified platform without leaving the SageMaker ecosystem. This seamless integration allows you to leverage Fiddler's powerful monitoring capabilities—including drift detection, performance tracking, and root cause analysis features—while maintaining your existing SageMaker workflows and security boundaries.

### What is a Partner AI App?

Amazon SageMaker Partner AI Apps are fully managed AI/ML applications from AWS partners that run natively within your SageMaker environment. Think of them as pre-built, enterprise-ready applications that integrate seamlessly with your existing AWS infrastructure—no complex deployments or external accounts required.

<figure><img src="https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-9a9a7962596d58515b653a709b40f69deb26f89c%2Ffiddler-and-amazon-sagemaker-ai-integration%20(1).png?alt=media" alt="Diagram showing AWS Cloud VPC containing SageMaker AI workflows and integration points with Fiddler AI"><figcaption></figcaption></figure>

**Key Benefits**:

* **Secure by Design**: Applications run entirely within your AWS account, maintaining your existing security boundaries and compliance requirements
* **Unified Experience**: Access partner tools directly from SageMaker Studio alongside your notebooks, models, and datasets
* **Simplified Procurement**: Subscribe through AWS Marketplace with consolidated billing on your AWS invoice
* **Managed Infrastructure**: AWS handles the underlying infrastructure while you focus on using the application

**How It Works**: When subscribing to a Partner AI App like Fiddler, AWS provisions the application within your SageMaker domain. Your team can then access it through SageMaker Studio with single sign-on, use it via APIs from notebooks, and integrate it into your ML workflows—all while keeping your data within your AWS environment.

This approach eliminates the traditional challenges of third-party tool integration: no separate accounts to manage, no data movement across boundaries, and no complex networking configurations.

### For Administrators

If you are an AWS administrator responsible for deploying and managing applications, our [Overview](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker) and [Admin Guide](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker/partner-ai-app-admin-guide) supplements the official AWS SageMaker documentation with Fiddler-specific configuration details and best practices. Use our guide alongside the official [Partner AI App Setup](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-app-onboard.html) and [Provisioning](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps-provision.html) documentation for a complete deployment experience.

* [Fiddler Partner AI App Overview](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker) - Introduction of the new Amazon SageMaker Partner AI Apps offering and overview of the subscription and deployment processes
* [**Fiddler Partner AI App Admin Guide**](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker/partner-ai-app-admin-guide) - Fiddler-specific configuration, troubleshooting, and deployment tips
* [**Quick Setup Script**](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker/partner-ai-app-quick-setup-script) - Automated script to configure IAM roles and permissions for quick demo purposes

### For Users

Once your administrator has deployed the Fiddler Partner AI App, you can begin monitoring, analyzing, and protecting your ML models and AI applications. Our [User Guide](https://app.gitbook.com/s/kcq97TxAnbTVaNJOQHbQ/cloud-platforms-and-deployment/aws-sagemaker/partner-ai-app-user-guide) provides step-by-step instructions for accessing the Fiddler interface through SageMaker Studio and connecting via the Python client SDK from your notebooks.

**Note**: Before getting started, confirm with your administrator that:

* The Fiddler Partner AI App has been deployed and is in "Deployed" status
* Your username has been granted appropriate access permissions
* You have been assigned the necessary IAM roles for Partner AI App access
* You understand which access method is available in your organization:
  * **SageMaker Studio access**: Launch Fiddler directly from the Studio interface
  * **Direct link access**: Access Fiddler via a pre-signed URL generated through AWS CLI

Some organizations may only permit direct link access, while others allow both. Your administrator will inform you which option(s) are available.

### Additional Resources

For a complete overview and detailed technical information, please refer to Amazon's SageMaker Partner AI App documentation:

* [Amazon SageMaker Partner AI Apps Overview](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-apps.html)
* [Amazon SageMaker Partner AI Apps Setup Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/partner-app-onboard.html)

***

:question: Questions? [Talk](https://www.fiddler.ai/contact-sales) to a product expert or [request](https://www.fiddler.ai/demo) a demo.

:bulb: Need help? Contact us at <support@fiddler.ai>.
