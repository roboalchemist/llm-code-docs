# Source: https://docs.aws.amazon.com/b2bi/latest/userguide/llms.txt

# AWS B2B Data Interchange User Guide

> AWS B2B Data Interchange enables automated exchange of electronic data interchange (EDI)âbased business-critical transactions at cloud scale, with elasticity, and pay-as-you-go pricing.

- [What is AWS B2B Data Interchange?](https://docs.aws.amazon.com/b2bi/latest/userguide/what-is-b2bi.html)
- [AWS B2B Data Interchange concepts](https://docs.aws.amazon.com/b2bi/latest/userguide/b2bi-concepts.html)
- [Using Transfer Family with B2B Data Interchange](https://docs.aws.amazon.com/b2bi/latest/userguide/use-tf-with-b2b.html)
- [EDI Validation](https://docs.aws.amazon.com/b2bi/latest/userguide/edi-validation.html)
- [AWS CloudFormation resources](https://docs.aws.amazon.com/b2bi/latest/userguide/creating-resources-with-cloudformation.html)
- [AWS PrivateLink](https://docs.aws.amazon.com/b2bi/latest/userguide/vpc-interface-endpoints.html)
- [Quotas](https://docs.aws.amazon.com/b2bi/latest/userguide/b2bi-quotas.html)
- [Troubleshooting](https://docs.aws.amazon.com/b2bi/latest/userguide/troubleshooting.html)
- [X12 transaction sets](https://docs.aws.amazon.com/b2bi/latest/userguide/x12-transaction-sets.html)
- [Document history](https://docs.aws.amazon.com/b2bi/latest/userguide/doc-history.html)

## [Getting started with AWS B2B Data Interchange](https://docs.aws.amazon.com/b2bi/latest/userguide/getting-started.html)

- [Prerequisites for using AWS B2B Data Interchange](https://docs.aws.amazon.com/b2bi/latest/userguide/b2bi-prereq.html): Delineate the prerequisites for using B2B Data Interchange
- [Quick setup using the console](https://docs.aws.amazon.com/b2bi/latest/userguide/getting-started-quick.html): Use the B2B Data Interchange console for a quick setup that creates the necessary resources using default information.
- [Setting up using a template](https://docs.aws.amazon.com/b2bi/latest/userguide/quickstart-template.html): Use a CloudFormation template to quickly configure B2B Data Interchange.


## [AWS B2B Data Interchange: tutorials](https://docs.aws.amazon.com/b2bi/latest/userguide/b2b-tutorials.html)

### [Outbound EDI tutorial](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-edi-tutorial.html)

A comprehensive step-by-step tutorial for setting up an outbound B2B Data Interchange workflow that transforms JSON data into X12 EDI documents for sending to trading partners.

- [Step 1: Setting up Amazon S3 buckets](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step1-s3-setup.html): Create and configure input and output Amazon S3 buckets for your JSON and EDI documents.
- [Step 2: Creating your business profile](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step2-profile.html): Set up a profile containing your organization's contact information for trading partnerships.
- [Step 3: Creating an outbound transformer](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step3-transformer.html): Configure a transformer to convert JSON data to X12 EDI documents.
- [Step 4: Create a trading capability](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step4-capability.html): Set up a trading capability to automate outbound EDI processing
- [Step 5: Create a partnership with outbound EDI configuration](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step5-partnership.html): Establish a partnership with comprehensive outbound EDI header configuration
- [Step 6: Test your outbound configuration](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step6-testing.html): Validate your outbound workflow with test JSON data
- [Step 7: Monitor your outbound workflow](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-step7-monitoring.html): Set up monitoring and observability for your outbound EDI workflow
- [Cleanup steps](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-cleanup.html): Remove outbound tutorial resources to prevent ongoing charges
- [Next steps](https://docs.aws.amazon.com/b2bi/latest/userguide/outbound-tutorial-conclusion.html): This outbound tutorial provides a complete foundation for generating X12 EDI documents from JSON data using AWS B2B Data Interchange.

### [Inbound EDI tutorial](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-edi-tutorial.html)

A comprehensive step-by-step tutorial for setting up an inbound B2B Data Interchange workflow that transforms X12 EDI documents from trading partners into JSON format.

- [Step 1: Set up your Amazon S3 infrastructure](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step1-s3-setup.html): Create and configure Amazon S3 buckets for EDI input and JSON output documents
- [Step 2: Create your business profile](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step2-profile.html): Set up a profile with your business contact information
- [Step 3: Create an inbound transformer](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step3-transformer.html): Configure a transformer to convert X12 EDI documents to JSON
- [Step 4: Create a trading capability](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step4-capability.html): Set up a trading capability to automate EDI processing
- [Step 5: Create a partnership](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step5-partnership.html): Establish a partnership to represent your trading relationship
- [Step 6: Test your inbound configuration](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step6-testing.html): Validate your workflow with test EDI documents
- [Step 7: Monitor your inbound workflow](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-step7-monitoring.html): Set up monitoring and observability for your inbound EDI workflow
- [Cleanup steps](https://docs.aws.amazon.com/b2bi/latest/userguide/inbound-tutorial-cleanup.html): Remove tutorial resources to prevent ongoing charges


## [Transforming and generating EDI](https://docs.aws.amazon.com/b2bi/latest/userguide/transform-variations.html)

- [Generative AI-assisted EDI mapping](https://docs.aws.amazon.com/b2bi/latest/userguide/generative-ai-assisted-mapping.html): Learn how to use AI-assisted mapping for AWS B2B Data Interchange.

### [Inbound EDI](https://docs.aws.amazon.com/b2bi/latest/userguide/transform-inbound-variations.html)

Details for transforming customer EDI files into JSON or XML documents and storing them in Amazon S3.

- [EDI acknowledgements](https://docs.aws.amazon.com/b2bi/latest/userguide/edi-ack.html): Learn about return acknowledgements that AWS B2B Data Interchange supports.
- [EDI splitting](https://docs.aws.amazon.com/b2bi/latest/userguide/edi-split-overview.html): Learn about EDI splitting functionality in AWS B2B Data Interchange, which enables splitting inbound X12 EDI documents by individual transactions for improved processing capabilities and increased file size support.
- [Outbound EDI](https://docs.aws.amazon.com/b2bi/latest/userguide/transform-outbound-variations.html): Details for transforming stored JSON or XML documents into EDI documents that can be sent downstream.


## [Managing events using EventBridge](https://docs.aws.amazon.com/b2bi/latest/userguide/eventbridge.html)

- [Events detail reference](https://docs.aws.amazon.com/b2bi/latest/userguide/events-detail-reference.html): Descriptions for the fields containing metadata about the AWS B2B Data Interchange events.


## [Security](https://docs.aws.amazon.com/b2bi/latest/userguide/security.html)

- [Data protection](https://docs.aws.amazon.com/b2bi/latest/userguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS B2B Data Interchange.
- [Identity and access management](https://docs.aws.amazon.com/b2bi/latest/userguide/security-iam.html): How to authenticate requests and manage access your B2B Data Interchange resources.
- [Compliance validation](https://docs.aws.amazon.com/b2bi/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/b2bi/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS B2B Data Interchange features for data resiliency.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/b2bi/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Monitoring](https://docs.aws.amazon.com/b2bi/latest/userguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/b2bi/latest/userguide/monitoring-cloudwatch.html): Use CloudWatch to monitor events within AWS B2B Data Interchange
- [Processed input-output pairs](https://docs.aws.amazon.com/b2bi/latest/userguide/monitoring-processed-pairs.html): View and monitor the most recently processed input/output file pairs for partnerships.
- [CloudTrail logs](https://docs.aws.amazon.com/b2bi/latest/userguide/logging-using-cloudtrail.html): Learn about logging AWS B2B Data Interchange with AWS CloudTrail.
