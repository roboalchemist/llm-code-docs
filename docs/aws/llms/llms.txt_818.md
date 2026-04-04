# Source: https://docs.aws.amazon.com/textract/latest/dg/llms.txt

# Amazon Textract Developer Guide

> Use Amazon Textract to detect and analyze text in your documents.

- [What is Amazon Textract?](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)
- [Handling Connection Errors](https://docs.aws.amazon.com/textract/latest/dg/handling-errors.html)
- [Document History](https://docs.aws.amazon.com/textract/latest/dg/document-history.html)

## [Getting Started](https://docs.aws.amazon.com/textract/latest/dg/getting-started.html)

- [Step 1: Set Up a User](https://docs.aws.amazon.com/textract/latest/dg/setting-up.html)

### [Step 2: Set Up the AWS CLI and AWS SDKs](https://docs.aws.amazon.com/textract/latest/dg/setup-awscli-sdk.html)

The following steps show you how to install the AWS Command Line Interface (AWS CLI) and AWS SDKs that the examples in this documentation use.

- [Granting Programmatic Access](https://docs.aws.amazon.com/textract/latest/dg/program-access.html): You can run the AWS CLI and code examples in this guide on your local computer or other AWS enviroments, such as an Amazon Elastic Compute Cloud instance.
- [Step 3: Get Started Using the AWS CLI and AWS SDK API](https://docs.aws.amazon.com/textract/latest/dg/get-started-exercise.html): After you've set up the AWS CLI and AWS SDKs that you want to use, you can build applications that use Amazon Textract.


## [Identifying Your Use Case](https://docs.aws.amazon.com/textract/latest/dg/how-it-works.html)

- [Detecting Text](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-detecting.html): Amazon Textract provides synchronous and asynchronous operations that return only the text detected in a document.
- [Analyzing Documents](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-analyzing.html): Amazon Textract analyzes documents and forms for relationships among detected text.
- [Analyzing Invoices and Receipts](https://docs.aws.amazon.com/textract/latest/dg/invoices-receipts.html): AnalyzeExpense explanation, focusing on unique response elements.
- [Analyzing Identity Documents](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-identity.html): Amazon Textract can extract relevant information from passports, driver licenses, and other identity documentation issued by the US Government using the AnalyzeID API.
- [Analyzing Lending Documents](https://docs.aws.amazon.com/textract/latest/dg/lending-document-classification-extraction.html): Analyze Lending is a document processing API for mortgage documents.
- [Customizing Outputs](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-custom-queries.html)


## [Interpreting Responses](https://docs.aws.amazon.com/textract/latest/dg/document-response.html)

- [Locating Items on a Document Page](https://docs.aws.amazon.com/textract/latest/dg/text-location.html): Amazon Textract operations return the location and geometry of items found on a document page. and return the location and geometry for lines and words, while and return the location and geometry of key-value pairs, tables, cells, and selection elements.

### [Text Detection and Document Analysis Response Objects](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-document-layout.html)

When Amazon Textract processes a document, it creates a list of objects for the detected or analyzed text.

- [Pages](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-pages.html): A document consists of one or more pages.
- [Lines and Words of Text](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-lines-words.html): Detected text that's returned by Amazon Textract operations is returned in a list of objects.
- [Form Data (Key-Value Pairs)](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-kvp.html): Amazon Textract can extract form data from documents as key-value pairs.
- [Tables](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-tables.html): Use Amazon Textract to extract tables in a document and extract cells, merged cells, column headers, titles, section titles, footers, table type (structured or semistructured), and summary cells within a table.
- [Selection Elements](https://docs.aws.amazon.com/textract/latest/dg/how-it-works-selectables.html): Amazon Textract can detect selection elements such as option buttons (radio buttons), check boxes, underlined, and circled text on a document page.
- [Queries](https://docs.aws.amazon.com/textract/latest/dg/queryresponse.html): When provided a query, Amazon Textract provides a specialized response object.
- [Layout Response Objects](https://docs.aws.amazon.com/textract/latest/dg/layoutresponse.html): When using Layout on a document with Amazon Textract, the different layout elements are returned as a BlockType in the Block object.
- [Invoice and Receipt Response Objects](https://docs.aws.amazon.com/textract/latest/dg/expensedocuments.html): When you submit an invoice or a receipt to the AnalyzeExpense API, it returns a series of ExpenseDocuments objects.
- [Identity Documentation Response Objects](https://docs.aws.amazon.com/textract/latest/dg/identitydocumentfields.html): When you submit an identity document to the AnalyzeID API, it returns a series of IdentityDocumentField objects.
- [Analyze Lending Response Objects](https://docs.aws.amazon.com/textract/latest/dg/lending-response-objects.html): When you submit a document to the Analyze Lending workflow, the document is split apart into individual pages and the pages are classified.


## [Processing Documents Synchronously](https://docs.aws.amazon.com/textract/latest/dg/sync.html)

- [Calling Amazon Textract Synchronous Operations](https://docs.aws.amazon.com/textract/latest/dg/sync-calling.html): Amazon Textract operations process document images that are stored on a local file system, or document images stored in an Amazon S3 bucket.
- [Detecting Document Text](https://docs.aws.amazon.com/textract/latest/dg/detecting-document-text.html): Describes how to detect document text with Amazon Textract.
- [Analyzing Document Text](https://docs.aws.amazon.com/textract/latest/dg/analyzing-document-text.html): Describes how to analyze document text with Amazon Textract.
- [Analyzing Invoice and Receipt Documents](https://docs.aws.amazon.com/textract/latest/dg/analyzing-document-expense.html): Describes how to use the Amazon Textract AnalyzeExpense API operation.
- [Analyzing ID Documents](https://docs.aws.amazon.com/textract/latest/dg/analyzing-document-identity.html): Describes how to use the Amazon Textract AnalyzeID API operation.


## [Processing Documents Asynchronously](https://docs.aws.amazon.com/textract/latest/dg/async.html)

- [Calling Asynchronous Operations](https://docs.aws.amazon.com/textract/latest/dg/api-async.html): Amazon Textract provides an asynchronous API that you can use to process multipage documents in PDF or TIFF format.
- [Configuring Asynchronous Operations](https://docs.aws.amazon.com/textract/latest/dg/api-async-roles.html): The following procedures show you how to configure Amazon Textract to use with an Amazon Simple Notification Service (Amazon SNS) topic and an Amazon Simple Queue Service (Amazon SQS) queue.
- [Detecting or Analyzing Text in a Multipage Document](https://docs.aws.amazon.com/textract/latest/dg/async-analyzing-with-sqs.html): This procedure shows you how to detect or analyze text in a multipage document by using Amazon Textract detection operations, a document stored in an Amazon S3 bucket, an Amazon SNS topic, and an Amazon SQS queue.
- [Using the Analyze Lending Workflow](https://docs.aws.amazon.com/textract/latest/dg/async-using-lending.html): To detect text in, or analyze multipage lending documents, using the Analyze Lending workflow, you do the following:
- [Amazon Textract Results Notification](https://docs.aws.amazon.com/textract/latest/dg/async-notification-payload.html): Amazon Textract sends the status of an analysis request to an Amazon Simple Notification Service (Amazon SNS) topic.


## [Customizing your Queries Responses](https://docs.aws.amazon.com/textract/latest/dg/textract-using-adapters.html)

### [Creating adapters](https://docs.aws.amazon.com/textract/latest/dg/textract-creating-using-adapters.html)

Before you can train an adapter, you must create an adapter.

- [Create an Adapter](https://docs.aws.amazon.com/textract/latest/dg/textract-create-adapter.html): To customize the Amazon Textract base model, create an adapter.
- [Get adapter](https://docs.aws.amazon.com/textract/latest/dg/textract-get-adapter.html): You can retrieve configuration information for an adapter at any time by calling the operation and specifying an AdapterId.
- [List adapters](https://docs.aws.amazon.com/textract/latest/dg/textract-list-adapter.html): You can list all of the adapters associated with your account by using the operation.
- [Update adapter](https://docs.aws.amazon.com/textract/latest/dg/textract-update-adapter.html): With Amazon Textract, you can update some configuration options of an adapter.
- [Delete an Adapter](https://docs.aws.amazon.com/textract/latest/dg/textract-delete-adapter.html): You can delete a custom Amazon Textract adapter at any time by calling the API operation.
- [Preparing training and testing datasets](https://docs.aws.amazon.com/textract/latest/dg/textract-preparing-training-testing.html)

### [Training adapter versions](https://docs.aws.amazon.com/textract/latest/dg/training-adapter-versions.html)

After you have created an adapter and created training and testing datasets, you can train a version of that adapter using the operation.

- [Create adapter version](https://docs.aws.amazon.com/textract/latest/dg/textract-create-adapter-version.html): To customize the Amazon Textract base model to fit your specific use cases, create an adapter.

### [Evaluating and improving your adapters](https://docs.aws.amazon.com/textract/latest/dg/textract-evaluating-improving-adapters.html)

Once you have finished the training process and created your adapter, it's important to evaluate how well the adapter is extracting information from your documents.

- [List adapter versions](https://docs.aws.amazon.com/textract/latest/dg/textract-list-adapter-version.html): An Amazon Textract adapter can have a number of different versions associated with it.
- [Get an Adapter version](https://docs.aws.amazon.com/textract/latest/dg/textract-get-adapter-version.html): You can retrieve configuration information and the current status of an adapter version by calling the operation.
- [Delete adapter version](https://docs.aws.amazon.com/textract/latest/dg/textract-delete-adapter-version.html): You can delete an adapter version youâre no longer using by calling .
- [Debugging training failures](https://docs.aws.amazon.com/textract/latest/dg/textract-debugging-failures-adapters.html): If you are notified on the adapter details page that training has failed, refer to the status message to understand the error and correct it.
- [Using Adapters during Inference](https://docs.aws.amazon.com/textract/latest/dg/textract-adapter-inference.html): After creating an adapter, you are provided with an ID and version for your custom adapter.
- [Custom Queries tutorial](https://docs.aws.amazon.com/textract/latest/dg/textract-adapters-tutorial.html): This tutorial shows you how to create, train, evaluate, use, and manage adapters.
- [Copying adapters](https://docs.aws.amazon.com/textract/latest/dg/textract-copy-adapters.html): Adapter Versions can be copied from one AWS account to another within AWS Regions.


## [Best Practices](https://docs.aws.amazon.com/textract/latest/dg/textract-best-practices.html)

- [Best Practices for Queries](https://docs.aws.amazon.com/textract/latest/dg/bestqueries.html)
- [Best Practices for Bulk Document Uploader](https://docs.aws.amazon.com/textract/latest/dg/bulk-uploader-best-practices.html): The Bulk Document Uploader is an AWS Management Console tool intended to help you quickly evaluate how Textract performs on a set of your own documents, without the need to write any code.
- [Best practices for Amazon Textract Custom Queries](https://docs.aws.amazon.com/textract/latest/dg/best-practices-adapters.html): Amazon Textract lets you customize the output of its pretrained Queries feature by training and using an adapter for its base model.


## [Tutorials](https://docs.aws.amazon.com/textract/latest/dg/examples-blocks.html)

- [Extracting Key-Value Pairs from a Form Document](https://docs.aws.amazon.com/textract/latest/dg/examples-extract-kvp.html): The following Python example shows how to extract key-value pairs in form documents from objects that are stored in a map.
- [Exporting Tables into a CSV File](https://docs.aws.amazon.com/textract/latest/dg/examples-export-table-csv.html): These Python examples show how to export tables from an image of a document into a comma-separated values (CSV) file.
- [Detecting text with an AWS Lambda function](https://docs.aws.amazon.com/textract/latest/dg/lambda.html): Shows how to create an AWS Lambda function that detects document text with Amazon Textract
- [Extracting and Sending Text to AWS Comprehend for Analysis](https://docs.aws.amazon.com/textract/latest/dg/textract-to-comprehend.html): Amazon Textract lets you include document text detection and analysis in your applications.
- [Additional Code Samples](https://docs.aws.amazon.com/textract/latest/dg/other-examples.html): The following table provides links to more Amazon Textract code examples.


## [Security](https://docs.aws.amazon.com/textract/latest/dg/security.html)

### [Data Protection](https://docs.aws.amazon.com/textract/latest/dg/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Textract.

- [Encryption in Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/encryption.html): Data encryption refers to protecting data while in transit and at rest.

### [Identity and Access Management](https://docs.aws.amazon.com/textract/latest/dg/security-iam.html)

How to authenticate requests and manage access your Amazon Textract resources.

- [How Amazon Textract Works with IAM](https://docs.aws.amazon.com/textract/latest/dg/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Textract, you should understand what IAM features are available to use with Amazon Textract.
- [Identity-Based Policy Examples](https://docs.aws.amazon.com/textract/latest/dg/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Textract resources.
- [Troubleshooting](https://docs.aws.amazon.com/textract/latest/dg/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Textract and IAM.

### [Logging and Monitoring](https://docs.aws.amazon.com/textract/latest/dg/textract_monitoring.html)

Describes how to monitor Amazon Textract.

- [Monitoring](https://docs.aws.amazon.com/textract/latest/dg/textract-monitoring.html): With CloudWatch, you can get metrics for individual Amazon Textract operations or global Amazon Textract metrics for your account.
- [CloudWatch Metrics for Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/cloudwatch-metricsdim.html): This section contains information about the Amazon CloudWatch metrics and the Operation dimension that are available for Amazon Textract.
- [Logging Amazon Textract API Calls with AWS CloudTrail](https://docs.aws.amazon.com/textract/latest/dg/logging-using-cloudtrail.html): Learn about logging Amazon Textract with AWS CloudTrail.

### [Tagging resources](https://docs.aws.amazon.com/textract/latest/dg/tagging-adapters.html)

With Amazon Textract, you can tag resources like adapters for the purposes of managing secure access.

- [Tag resource](https://docs.aws.amazon.com/textract/latest/dg/w2aac46c25b5.html): Amazon Textract resources like adapters can be tagged using the operation.
- [List tags for resource](https://docs.aws.amazon.com/textract/latest/dg/w2aac46c25b7.html): Amazon Textract resources like adapters can be tagged using the operation.
- [Untag resource](https://docs.aws.amazon.com/textract/latest/dg/w2aac46c25b9.html): Amazon Textract resources like adapters can be tagged using the operation.
- [Compliance Validation](https://docs.aws.amazon.com/textract/latest/dg/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/textract/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Textract features for data resiliency.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/textract/latest/dg/cross-service-confused-deputy-prevention.html): In AWS, cross-service impersonation can occur when one service (the calling service) calls another service (the called service).
- [Infrastructure Security](https://docs.aws.amazon.com/textract/latest/dg/infrastructure-security.html): Learn how Amazon Textract isolates service traffic.
- [Configuration and Vulnerability Analysis](https://docs.aws.amazon.com/textract/latest/dg/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/textract/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and Amazon Textract without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.


## [API Reference](https://docs.aws.amazon.com/textract/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/textract/latest/dg/API_Operations.html)

The following actions are supported:

- [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeDocument.html): Analyzes an input document for relationships between detected items.
- [AnalyzeExpense](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeExpense.html): AnalyzeExpense synchronously analyzes an input document for financially related relationships between text.
- [AnalyzeID](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeID.html): Analyzes identity documents for relevant information.
- [CreateAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_CreateAdapter.html): Creates an adapter, which can be fine-tuned for enhanced performance on user provided documents.
- [CreateAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_CreateAdapterVersion.html): Creates a new version of an adapter.
- [DeleteAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_DeleteAdapter.html): Deletes an Amazon Textract adapter.
- [DeleteAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_DeleteAdapterVersion.html): Deletes an Amazon Textract adapter version.
- [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html): Detects text in the input document.
- [GetAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_GetAdapter.html): Gets configuration information for an adapter specified by an AdapterId, returning information on AdapterName, Description, CreationTime, AutoUpdate status, and FeatureTypes.
- [GetAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_GetAdapterVersion.html): Gets configuration information for the specified adapter version, including: AdapterId, AdapterVersion, FeatureTypes, Status, StatusMessage, DatasetConfig, KMSKeyId, OutputConfig, Tags and EvaluationMetrics.
- [GetDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetDocumentAnalysis.html): Gets the results for an Amazon Textract asynchronous operation that analyzes text in a document.
- [GetDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/dg/API_GetDocumentTextDetection.html): Gets the results for an Amazon Textract asynchronous operation that detects text in a document.
- [GetExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetExpenseAnalysis.html): Gets the results for an Amazon Textract asynchronous operation that analyzes invoices and receipts.
- [GetLendingAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetLendingAnalysis.html): Gets the results for an Amazon Textract asynchronous operation that analyzes text in a lending document.
- [GetLendingAnalysisSummary](https://docs.aws.amazon.com/textract/latest/dg/API_GetLendingAnalysisSummary.html): Gets summarized results for the StartLendingAnalysis operation, which analyzes text in a lending document.
- [ListAdapters](https://docs.aws.amazon.com/textract/latest/dg/API_ListAdapters.html): Lists all adapters that match the specified filtration criteria.
- [ListAdapterVersions](https://docs.aws.amazon.com/textract/latest/dg/API_ListAdapterVersions.html): List all version of an adapter that meet the specified filtration criteria.
- [ListTagsForResource](https://docs.aws.amazon.com/textract/latest/dg/API_ListTagsForResource.html): Lists all tags for an Amazon Textract resource.
- [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentAnalysis.html): Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.
- [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentTextDetection.html): Starts the asynchronous detection of text in a document.
- [StartExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartExpenseAnalysis.html): Starts the asynchronous analysis of invoices or receipts for data like contact information, items purchased, and vendor names.
- [StartLendingAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartLendingAnalysis.html): Starts the classification and analysis of an input document.
- [TagResource](https://docs.aws.amazon.com/textract/latest/dg/API_TagResource.html): Adds one or more tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/textract/latest/dg/API_UntagResource.html): Removes any tags with the specified keys from the specified resource.
- [UpdateAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_UpdateAdapter.html): Update the configuration for an adapter.

### [Data Types](https://docs.aws.amazon.com/textract/latest/dg/API_Types.html)

The following data types are supported:

- [Adapter](https://docs.aws.amazon.com/textract/latest/dg/API_Adapter.html): An adapter selected for use when analyzing documents.
- [AdapterOverview](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterOverview.html): Contains information on the adapter, including the adapter ID, Name, Creation time, and feature types.
- [AdaptersConfig](https://docs.aws.amazon.com/textract/latest/dg/API_AdaptersConfig.html): Contains information about adapters used when analyzing a document, with each adapter specified using an AdapterId and version
- [AdapterVersionDatasetConfig](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionDatasetConfig.html): The dataset configuration options for a given version of an adapter.
- [AdapterVersionEvaluationMetric](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionEvaluationMetric.html): Contains information on the metrics used to evalute the peformance of a given adapter version.
- [AdapterVersionOverview](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionOverview.html): Summary info for an adapter version.
- [AnalyzeIDDetections](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeIDDetections.html): Used to contain the information detected by an AnalyzeID operation.
- [Block](https://docs.aws.amazon.com/textract/latest/dg/API_Block.html): A Block represents items that are recognized in a document within a group of pixels close to each other.
- [BoundingBox](https://docs.aws.amazon.com/textract/latest/dg/API_BoundingBox.html): The bounding box around the detected page, text, key-value pair, table, table cell, or selection element on a document page.
- [DetectedSignature](https://docs.aws.amazon.com/textract/latest/dg/API_DetectedSignature.html): A structure that holds information regarding a detected signature on a page.
- [Document](https://docs.aws.amazon.com/textract/latest/dg/API_Document.html): The input document, either as bytes or as an S3 object.
- [DocumentGroup](https://docs.aws.amazon.com/textract/latest/dg/API_DocumentGroup.html): Summary information about documents grouped by the same document type.
- [DocumentLocation](https://docs.aws.amazon.com/textract/latest/dg/API_DocumentLocation.html): The Amazon S3 bucket that contains the document to be processed.
- [DocumentMetadata](https://docs.aws.amazon.com/textract/latest/dg/API_DocumentMetadata.html): Information about the input document.
- [EvaluationMetric](https://docs.aws.amazon.com/textract/latest/dg/API_EvaluationMetric.html): The evaluation metrics (F1 score, Precision, and Recall) for an adapter version.
- [ExpenseCurrency](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseCurrency.html): Returns the kind of currency detected.
- [ExpenseDetection](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseDetection.html): An object used to store information about the Value or Label detected by Amazon Textract.
- [ExpenseDocument](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseDocument.html): The structure holding all the information returned by AnalyzeExpense
- [ExpenseField](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseField.html): Breakdown of detected information, seperated into the catagories Type, LabelDetection, and ValueDetection
- [ExpenseGroupProperty](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseGroupProperty.html): Shows the group that a certain key belongs to.
- [ExpenseType](https://docs.aws.amazon.com/textract/latest/dg/API_ExpenseType.html): An object used to store information about the Type detected by Amazon Textract.
- [Extraction](https://docs.aws.amazon.com/textract/latest/dg/API_Extraction.html): Contains information extracted by an analysis operation after using StartLendingAnalysis.
- [Geometry](https://docs.aws.amazon.com/textract/latest/dg/API_Geometry.html): Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.
- [HumanLoopActivationOutput](https://docs.aws.amazon.com/textract/latest/dg/API_HumanLoopActivationOutput.html): Shows the results of the human in the loop evaluation.
- [HumanLoopConfig](https://docs.aws.amazon.com/textract/latest/dg/API_HumanLoopConfig.html): Sets up the human review workflow the document will be sent to if one of the conditions is met.
- [HumanLoopDataAttributes](https://docs.aws.amazon.com/textract/latest/dg/API_HumanLoopDataAttributes.html): Allows you to set attributes of the image.
- [IdentityDocument](https://docs.aws.amazon.com/textract/latest/dg/API_IdentityDocument.html): The structure that lists each document processed in an AnalyzeID operation.
- [IdentityDocumentField](https://docs.aws.amazon.com/textract/latest/dg/API_IdentityDocumentField.html): Structure containing both the normalized type of the extracted information and the text associated with it.
- [LendingDetection](https://docs.aws.amazon.com/textract/latest/dg/API_LendingDetection.html): The results extracted for a lending document.
- [LendingDocument](https://docs.aws.amazon.com/textract/latest/dg/API_LendingDocument.html): Holds the structured data returned by AnalyzeDocument for lending documents.
- [LendingField](https://docs.aws.amazon.com/textract/latest/dg/API_LendingField.html): Holds the normalized key-value pairs returned by AnalyzeDocument, including the document type, detected text, and geometry.
- [LendingResult](https://docs.aws.amazon.com/textract/latest/dg/API_LendingResult.html): Contains the detections for each page analyzed through the Analyze Lending API.
- [LendingSummary](https://docs.aws.amazon.com/textract/latest/dg/API_LendingSummary.html): Contains information regarding DocumentGroups and UndetectedDocumentTypes.
- [LineItemFields](https://docs.aws.amazon.com/textract/latest/dg/API_LineItemFields.html): A structure that holds information about the different lines found in a document's tables.
- [LineItemGroup](https://docs.aws.amazon.com/textract/latest/dg/API_LineItemGroup.html): A grouping of tables which contain LineItems, with each table identified by the table's LineItemGroupIndex.
- [NormalizedValue](https://docs.aws.amazon.com/textract/latest/dg/API_NormalizedValue.html): Contains information relating to dates in a document, including the type of value, and the value.
- [NotificationChannel](https://docs.aws.amazon.com/textract/latest/dg/API_NotificationChannel.html): The Amazon Simple Notification Service (Amazon SNS) topic to which Amazon Textract publishes the completion status of an asynchronous document operation.
- [OutputConfig](https://docs.aws.amazon.com/textract/latest/dg/API_OutputConfig.html): Sets whether or not your output will go to a user created bucket.
- [PageClassification](https://docs.aws.amazon.com/textract/latest/dg/API_PageClassification.html): The class assigned to a Page object detected in an input document.
- [Point](https://docs.aws.amazon.com/textract/latest/dg/API_Point.html): The X and Y coordinates of a point on a document page.
- [Prediction](https://docs.aws.amazon.com/textract/latest/dg/API_Prediction.html): Contains information regarding predicted values returned by Amazon Textract operations, including the predicted value and the confidence in the predicted value.
- [QueriesConfig](https://docs.aws.amazon.com/textract/latest/dg/API_QueriesConfig.html)
- [Query](https://docs.aws.amazon.com/textract/latest/dg/API_Query.html): Each query contains the question you want to ask in the Text and the alias you want to associate.
- [Relationship](https://docs.aws.amazon.com/textract/latest/dg/API_Relationship.html): Information about how blocks are related to each other.
- [S3Object](https://docs.aws.amazon.com/textract/latest/dg/API_S3Object.html): The S3 bucket name and file name that identifies the document.
- [SignatureDetection](https://docs.aws.amazon.com/textract/latest/dg/API_SignatureDetection.html): Information regarding a detected signature on a page.
- [SplitDocument](https://docs.aws.amazon.com/textract/latest/dg/API_SplitDocument.html): Contains information about the pages of a document, defined by logical boundary.
- [UndetectedSignature](https://docs.aws.amazon.com/textract/latest/dg/API_UndetectedSignature.html): A structure containing information about an undetected signature on a page where it was expected but not found.
- [Warning](https://docs.aws.amazon.com/textract/latest/dg/API_Warning.html): A warning about an issue that occurred during asynchronous text analysis () or asynchronous document text detection ().


## [Quotas](https://docs.aws.amazon.com/textract/latest/dg/limits.html)

- [Set Quotas](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html): The following is a list of set quotas in Amazon Textract, which cannot be changed.
- [Modifying Default Quotas](https://docs.aws.amazon.com/textract/latest/dg/limits-quotas-explained.html): Your console account has default quotas for Amazon Textract operations.
