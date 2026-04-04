# Source: https://docs.together.ai/docs/deployment-options.md

# Deployment Options Overview

> Compare Together AI's deployment options: fully-managed cloud service vs. secure VPC deployment for enterprises.

Together AI offers a flexible and powerful platform that enables organizations to deploy in a way that best suits their needs. Whether you're looking for a fully-managed cloud solution, or secure VPC deployment on any cloud, Together AI provides robust tools, superior performance, and comprehensive support.

## Deployment Options Overview

Together AI provides two key deployment options:

* **Together AI Cloud**: A fully-managed, inference platform that is fast, scalable, and cost-efficient.
* **VPC Deployment**: Deploy Together AI's Enterprise Platform within your own Virtual Private Cloud (VPC) on any cloud platform for enhanced security and control.

The following sections provide an overview of each deployment type, along with a detailed responsibility matrix comparing the features and benefits of each option.

<ul class="not-prose h-1 mt-10min-w-full overflow-auto border-b border-[#5b616e33] dark:border-gray-200/10" />

## Together AI Cloud

Together AI Cloud is a fully-managed service that runs in Together AI's cloud infrastructure. With seamless access to Together's products, this option is ideal for companies that want to get started quickly without the overhead of managing their own infrastructure.

### Key Features

* **Fully Managed**: Together AI handles infrastructure, scaling, and orchestration.
* **Fast and Scalable**: Both Dedicated and Serverless API endpoints ensure optimal performance and scalability.
* **Cost-Effective**: Pay-as-you-go pricing with the option for reserved endpoints at a discount.
* **Privacy & Security**: Full control over your data; Together AI ensures SOC 2 and HIPAA compliance.
* **Ideal Use Case**: Best suited for AI-native startups and companies that need fast, easy deployment without infrastructure management.

For more information on Together AI Cloud, [contact our team](/docs/support-ticket-portal).

## Together AI VPC Deployment

Together AI VPC Deployment allows you to deploy the platform in your own Virtual Private Cloud (VPC) on any cloud provider (such as Google Cloud, Azure, AWS, or others). This option is ideal for enterprises that need enhanced security, control, and compliance while benefiting from Together AI's powerful AI stack.

### Key Features

* **Cloud-Agnostic**: Deploy within your VPC on any cloud platform of your choice (e.g., AWS, Azure, Google Cloud).
* **Full Control**: Complete administrative access, enabling you to manage and control ingress and egress traffic within your VPC.
* **High Performance**: Achieve up to 2x faster performance on your existing infrastructure, optimized for your environment.
* **Data Sovereignty**: Data never leaves your controlled environment, ensuring complete security and compliance.
* **Customization**: Tailor scaling, performance, and resource allocation to fit your infrastructure’s specific needs.
* **Ideal Use Case**: Perfect for enterprises with strict security, privacy, and compliance requirements who want to retain full control over their cloud infrastructure.

### Example: VPC Deployment in AWS

Below is an example of how Together AI VPC Deployment works in an AWS environment. This system diagram illustrates the architecture and flow:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ad0b55a56e9eaecf03c80d3a90ef66f" alt="" data-og-width="1342" width="1342" data-og-height="1070" height="1070" data-path="images/guides/34.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=884013b1f58f1f732c9aab0c0c7c6e00 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=643e3f65fc16039aa2ecb0c0a41f4ac2 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f77e787d3e26b454d7e9495371aaa3e9 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d1f99a659a9952d7fba4e10780f09baf 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ecd727b0a535236a4b923831192f12ff 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/34.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7b5c6567c0e45f31f15ec4d2918359bb 2500w" />
</Frame>

1. **Secure VPC Peering**: Together AI connects to your AWS environment via secure VPC peering, ensuring data remains entirely within your AWS account.
2. **Private Subnets**: All data processing and model inference happens within private subnets, isolating resources from the internet.
3. **Control of Ingress/Egress Traffic**: You have full control over all traffic entering and leaving your VPC, including restrictions on external network access.
4. **Data Sovereignty**: Since all computations are performed within your VPC, data never leaves your controlled environment.
5. **Custom Scaling**: Leverage AWS autoscaling groups to ensure that your AI workloads scale seamlessly with demand, while maintaining complete control over resources.

Although this example uses AWS, the architecture can be adapted to other cloud providers such as Azure or Google Cloud with similar capabilities.

For more information on VPC deployment, [get in touch with us](/docs/support-ticket-portal).

## Comparison of Deployment Options

| Feature                     | Together AI Cloud                                                                                                                                              | Together AI VPC Deployment                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **How It Works**            | Fully-managed, serverless API endpoints. On-demand and reserved dedicated endpoints for production workloads - with consistent performance and no rate limits. | Deploy Together's Platform and inference stack in your VPC on any cloud platform.                         |
| **Performance**             | Optimal performance with Together inference stack and Together Turbo Endpoints.                                                                                | Better performance on your infrastructure: Up to 2x better speed on existing infrastructure               |
| **Cost**                    | Pay-as-you-go, or discounts for reserved endpoints.                                                                                                            | Lower TCO through faster performance and optimized GPU usage.                                             |
| **Management**              | Fully-managed service, no infrastructure to manage.                                                                                                            | You manage your VPC, with Together AI’s support. Managed service offering also available.                 |
| **Scaling**                 | Automatic scaling to meet demand.                                                                                                                              | Intelligent scaling based on your infrastructure. Fully customizable.                                     |
| **Data Privacy & Security** | Data ownership with SOC 2 and HIPAA compliance.                                                                                                                | Data never leaves your environment.                                                                       |
| **Compliance**              | SOC 2 and HIPAA compliant.                                                                                                                                     | Implement security and compliance controls to match internal standards.                                   |
| **Support**                 | 24/7 support with guaranteed SLAs.                                                                                                                             | Dedicated support with engineers on call.                                                                 |
| **Ideal For**               | Startups and companies that want quick, easy access to AI infrastructure without managing it.                                                                  | Enterprises with stringent security and privacy needs, or those leveraging existing cloud infrastructure. |

## Next Steps

To get started with Together AI’s platform, **we recommend [trying the Together AI Cloud](https://api.together.ai/signin)** for quick deployment and experimentation. If your organization has specific security, infrastructure, or compliance needs, consider Together AI VPC.

For more information, or to find the best deployment option for your business, [contact our team](https://www.together.ai/forms/contact-sales).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt