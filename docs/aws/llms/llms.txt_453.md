# Source: https://docs.aws.amazon.com/healthlake/latest/APIReference/llms.txt

# AWS HealthLake API Reference

> This is the AWS HealthLake API Reference. For an introduction to the service, see What is AWS HealthLake? in the AWS HealthLake Developer Guide.

- [Welcome](https://docs.aws.amazon.com/healthlake/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/healthlake/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/healthlake/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_Operations.html)

- [CreateFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateFHIRDatastore.html): Create a FHIR-enabled data store.
- [DeleteFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteFHIRDatastore.html): Delete a FHIR-enabled data store.
- [DescribeFHIRDatastore](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRDatastore.html): Get properties for a FHIR-enabled data store.
- [DescribeFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRExportJob.html): Get FHIR export job properties.
- [DescribeFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DescribeFHIRImportJob.html): Get the import job properties to learn more about the job or job progress.
- [ListFHIRDatastores](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRDatastores.html): List all FHIR-enabled data stores in a userâs account, regardless of data store status.
- [ListFHIRExportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRExportJobs.html): Lists all FHIR export jobs associated with an account and their statuses.
- [ListFHIRImportJobs](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListFHIRImportJobs.html): List all FHIR import jobs associated with an account and their statuses.
- [ListTagsForResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ListTagsForResource.html): Returns a list of all existing tags associated with a data store.
- [StartFHIRExportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartFHIRExportJob.html): Start a FHIR export job.
- [StartFHIRImportJob](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_StartFHIRImportJob.html): Start importing bulk FHIR data into an ACTIVE data store.
- [TagResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_TagResource.html): Add a user-specifed key and value tag to a data store.
- [UntagResource](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UntagResource.html): Remove a user-specifed key and value tag from a data store.


## [Data Types](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_Types.html)

- [DatastoreFilter](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreFilter.html): The filters applied to a data store query.
- [DatastoreProperties](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DatastoreProperties.html): The data store properties.
- [ErrorCause](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ErrorCause.html): The error information for CreateFHIRDatastore and DeleteFHIRDatastore actions.
- [ExportJobProperties](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ExportJobProperties.html): The properties of a FHIR export job.
- [IdentityProviderConfiguration](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_IdentityProviderConfiguration.html): The identity provider configuration selected when the data store was created.
- [ImportJobProperties](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_ImportJobProperties.html): The import job properties.
- [InputDataConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_InputDataConfig.html): The import job input properties.
- [JobProgressReport](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_JobProgressReport.html): The progress report for the import job.
- [KmsEncryptionConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html): The customer-managed-key (CMK) used when creating a data store.
- [OutputDataConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_OutputDataConfig.html): The output data configuration supplied when the export job was created.
- [PreloadDataConfig](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_PreloadDataConfig.html): The input properties for the preloaded (Synthea) data store.
- [S3Configuration](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_S3Configuration.html): The configuration of the S3 bucket for either an import or export job.
- [SseConfiguration](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_SseConfiguration.html): The server-side encryption key configuration for a customer-provided encryption key.
- [Tag](https://docs.aws.amazon.com/healthlake/latest/APIReference/API_Tag.html): A label consisting of a user-defined key and value.
