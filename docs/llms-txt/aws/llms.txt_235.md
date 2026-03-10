# Source: https://docs.aws.amazon.com/comprehend-medical/latest/dev/llms.txt

# Amazon Comprehend Medical Developer Guide

> Extract insights about a document with Amazon Comprehend Medical.

- [What is Amazon Comprehend Medical?](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html)
- [How it works](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-howitworks.html)
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-vpcendpoints.html)
- [Guidelines and quotas](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-quotas.html)
- [Document history](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-releases.html)

## [Getting Started](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-gettingstarted.html)

- [Step 1: Set Up an Account](https://docs.aws.amazon.com/comprehend-medical/latest/dev/gettingstarted-setup.html): Before you use Amazon Comprehend Medical for the first time, complete the following tasks:
- [Step 2: Set Up the AWS CLI](https://docs.aws.amazon.com/comprehend-medical/latest/dev/gettingstarted-awscli.html): You don't need the AWS CLI to perform the steps in the Getting Started exercises.

### [Step 3: Getting Started Using the Console](https://docs.aws.amazon.com/comprehend-medical/latest/dev/gettingstarted-console.html)

How to get started using the Comprehend Medical console.

- [Analyzing clinical text using the console](https://docs.aws.amazon.com/comprehend-medical/latest/dev/gettingstarted-console-analysis.html): The Comprehend Medical console enables you to analyze the contents of clinical text, up to 20,000 characters long.
- [Step 4: Getting Started Using the API](https://docs.aws.amazon.com/comprehend-medical/latest/dev/gettingstarted-api.html): Examples for using the Amazon Comprehend Medical APIs.


## [Text analysis APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-textanalysis.html)

- [Detect entities (Version 2)](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-entitiesv2.html): Use the DetectEntitiesV2 to detect entities in single files or StartEntitiesDetectionV2Job for batch analysis on multiple files.
- [Detect PHI](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-phi.html): Use the DetectPHI operation when you only want to detect Protected Health Information (PHI) data when scanning the clinical text.
- [Text analysis batch APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/textanalysis-batchapi.html): Use Amazon Comprehend Medical to analyze medical text stored in an Amazon S3 bucket.


## [Ontology Linking APIs](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-ontologies.html)

- [InferICD10CM](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-icd10.html): Use InferICD10CM to detect possible medical conditions as entities and link them to codes from the 2026 version of the International Classification of Diseases, 10th Revision, Clinical Modification (ICD-10-CM).
- [InferRxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-RxNorm.html): Use the InferRxNorm operation to identify medications that are listed in a patient record as entities.
- [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontology-linking-snomed.html): Use InferSNOMEDCT to detect medical entities and link them to concepts from the 2022-03 version of the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT).
- [Ontology linking batch analysis](https://docs.aws.amazon.com/comprehend-medical/latest/dev/ontologies-batchapi.html): Use Amazon Comprehend Medical to detect entities in clinical text stored in an Amazon Simple Storage Service (Amazon S3) bucket and to link those entities to standardized ontologies.


## [Security](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-security.html)

- [Data Protection](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-dataprotection.html): Learn how the AWS shared responsibility model applies to data protection in Amazon Comprehend Medical.

### [Authentication and access control](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam.html)

Identifies methods for controlling access to your Amazon Comprehend Medical resources.

- [Overview of managing access](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam-accesscontrol.html): Permissions policies govern the access to an action.
- [Using Identity-Based policies (IAM policies) for Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam-permissions.html): This topic shows example identity-based policies.
- [Amazon Comprehend Medical API Permissions Reference](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam-resources.html): Use the following table as a reference when setting up and writing a permissions' policy that you can attach to a user.
- [AWS managed policies](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Comprehend Medical and recent changes to those policies.
- [Logging Amazon Comprehend Medical API calls by using AWS CloudTrail](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-cloudtrail.html): Learn about logging Amazon Comprehend Medical with AWS CloudTrail.
- [Compliance Validation](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-compliance.html): Learn which compliance programs are in scope for Comprehend Medical.
- [Resilience](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-resilience.html): Learn how AWS architecture supports data redundancy, and which Amazon Comprehend Medical features support data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/comprehend-medical/latest/dev/security-infrastructure.html): Learn how Amazon Comprehend Medical isolates service traffic.
