# Source: https://docs.aws.amazon.com/awssupport/latest/APIReference/llms.txt

# AWS Support API Reference

> The AWS Support API Reference is intended for programmers who need detailed information about the Support operations and data types. You can use the API to manage your support cases programmatically. The AWS Support API uses HTTP methods that return results in JSON format.

- [Welcome](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/awssupport/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/awssupport/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Operations.html)

- [AddAttachmentsToSet](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddAttachmentsToSet.html): Adds one or more attachments to an attachment set.
- [AddCommunicationToCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddCommunicationToCase.html): Adds additional customer communication to an Support case.
- [CreateCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CreateCase.html): Creates a case in the Support Center.
- [DescribeAttachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeAttachment.html): Returns the attachment that has the specified ID.
- [DescribeCases](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCases.html): Returns a list of cases that you specify by passing one or more case IDs.
- [DescribeCommunications](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCommunications.html): Returns communications and attachments for one or more support cases.
- [DescribeCreateCaseOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeCreateCaseOptions.html): Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability.
- [DescribeServices](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeServices.html): Returns the current list of AWS services and a list of service categories for each service.
- [DescribeSeverityLevels](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSeverityLevels.html): Returns the list of severity levels that you can assign to a support case.
- [DescribeSupportedLanguages](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeSupportedLanguages.html): Returns a list of supported languages for a specified categoryCode, issueType and serviceCode.
- [DescribeTrustedAdvisorCheckRefreshStatuses](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckRefreshStatuses.html): Returns the refresh status of the AWS Trusted Advisor checks that have the specified check IDs.
- [DescribeTrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckResult.html): Returns the results of the AWS Trusted Advisor check that has the specified check ID.
- [DescribeTrustedAdvisorChecks](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorChecks.html): Returns information about all available AWS Trusted Advisor checks, including the name, ID, category, description, and metadata.
- [DescribeTrustedAdvisorCheckSummaries](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeTrustedAdvisorCheckSummaries.html): Returns the results for the AWS Trusted Advisor check summaries for the check IDs that you specified.
- [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_RefreshTrustedAdvisorCheck.html): Refreshes the AWS Trusted Advisor check that you specify using the check ID.
- [ResolveCase](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_ResolveCase.html): Resolves a support case.


## [Data Types](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Types.html)

- [Attachment](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Attachment.html): An attachment to a case communication.
- [AttachmentDetails](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AttachmentDetails.html): The file name and ID of an attachment to a case communication.
- [CaseDetails](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html): A JSON-formatted object that contains the metadata for a support case.
- [Category](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Category.html): A JSON-formatted name/value pair that represents the category name and category code of the problem, selected from the response for each AWS service.
- [Communication](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Communication.html): A communication associated with a support case.
- [CommunicationTypeOptions](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CommunicationTypeOptions.html): A JSON-formatted object that contains the CommunicationTypeOptions for creating a case for a certain communication channel.
- [DateInterval](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DateInterval.html): Date and time (UTC) format in RFC 3339 : 'yyyy-MM-dd'T'HH:mm:ss.SSSZZ'.
- [RecentCaseCommunications](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_RecentCaseCommunications.html): The five most recent communications associated with the case.
- [Service](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Service.html): Information about an AWS service returned by the operation.
- [SeverityLevel](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SeverityLevel.html): A code and name pair that represents the severity level of a support case.
- [SupportedHour](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SupportedHour.html): Time range object with startTime and endTime range in RFC 3339 format. 'HH:mm:ss.SSS'.
- [SupportedLanguage](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_SupportedLanguage.html): A JSON-formatted object that contains the available ISO 639-1 language code, language name and langauge display value.
- [ThrottlingReason](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_ThrottlingReason.html)
- [TrustedAdvisorCategorySpecificSummary](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCategorySpecificSummary.html): The container for summary information that relates to the category of the Trusted Advisor check.
- [TrustedAdvisorCheckDescription](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckDescription.html): The description and metadata for a Trusted Advisor check.
- [TrustedAdvisorCheckRefreshStatus](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckRefreshStatus.html): The refresh status of a Trusted Advisor check.
- [TrustedAdvisorCheckResult](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckResult.html): The results of a Trusted Advisor check returned by .
- [TrustedAdvisorCheckSummary](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCheckSummary.html): A summary of a Trusted Advisor check result, including the alert status, last refresh, and number of resources examined.
- [TrustedAdvisorCostOptimizingSummary](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorCostOptimizingSummary.html): The estimated cost savings that might be realized if the recommended operations are taken.
- [TrustedAdvisorResourceDetail](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorResourceDetail.html): Contains information about a resource identified by a Trusted Advisor check.
- [TrustedAdvisorResourcesSummary](https://docs.aws.amazon.com/awssupport/latest/APIReference/API_TrustedAdvisorResourcesSummary.html): Details about AWS resources that were analyzed in a call to Trusted Advisor .
