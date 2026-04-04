# Source: https://docs.aws.amazon.com/artifact/latest/APIReference/llms.txt

# AWS Artifact Welcome

> This reference provides descriptions of the low-level AWS Artifact Service API.

- [Welcome](https://docs.aws.amazon.com/artifact/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/artifact/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/artifact/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/artifact/latest/APIReference/API_Operations.html)

- [AcceptAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptAgreement.html): Accept an agreement.
- [AcceptNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptNdaForAgreement.html): Accept the NDA document for an agreement.
- [GetAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAccountSettings.html): Get the account settings for Artifact.
- [GetAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAgreement.html): Retrieve an agreement document.
- [GetCustomerAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetCustomerAgreement.html): Retrieve a customer-agreement document.
- [GetNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetNdaForAgreement.html): Retrieve the NDA document for an agreement.
- [GetReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReport.html): Get the content for a single report.
- [GetReportMetadata](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReportMetadata.html): Get the metadata for a single report.
- [GetTermForReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetTermForReport.html): Get the Term content associated with a single report.
- [ListAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListAgreements.html): List available agreements.
- [ListCustomerAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListCustomerAgreements.html): List active customer-agreements applicable to calling identity.
- [ListReports](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReports.html): List available reports.
- [ListReportVersions](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReportVersions.html): List available report versions for a given report.
- [PutAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_PutAccountSettings.html): Put the account settings for Artifact.
- [TerminateAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateAgreement.html): Terminate an existing customer-agreement.


## [Data Types](https://docs.aws.amazon.com/artifact/latest/APIReference/API_Types.html)

- [AccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AccountSettings.html): Account settings for the customer.
- [AgreementSummary](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AgreementSummary.html): Summary for agreement resource.
- [CustomerAgreementSummary](https://docs.aws.amazon.com/artifact/latest/APIReference/API_CustomerAgreementSummary.html): Summary for customer-agreement resource.
- [ReportDetail](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ReportDetail.html): Full detail for report resource metadata.
- [ReportSummary](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ReportSummary.html): Summary for report resource.
- [TerminateCustomerAgreementSummary](https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateCustomerAgreementSummary.html): Summary returned when terminating an agreement.
- [ValidationExceptionField](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ValidationExceptionField.html): Validation exception message and name.
