# Source: https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/llms.txt

# AWS CloudTrail API Reference

> The CloudTrail Data Service lets you ingest events into CloudTrail from any source in your hybrid environments, such as in-house or SaaS applications hosted on-premises or in the cloud, virtual machines, or containers. You can store, access, analyze, troubleshoot and take action on this data without maintaining multiple log aggregators and reporting tools. After you run PutAuditEvents to ingest your application activity into CloudTrail, you can use CloudTrail Lake to search, query, and analyze the data that is logged from your applications.

- [Welcome](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_Operations.html)

- [PutAuditEvents](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_PutAuditEvents.html): Ingests your application events into CloudTrail Lake.


## [Data Types](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_Types.html)

- [AuditEvent](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_AuditEvent.html): An event from a source outside of AWS that you want CloudTrail to log.
- [AuditEventResultEntry](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_AuditEventResultEntry.html): A response that includes successful and failed event results.
- [ResultErrorEntry](https://docs.aws.amazon.com/awscloudtraildata/latest/APIReference/API_ResultErrorEntry.html): Includes the error code and error message for events that could not be ingested by CloudTrail.
