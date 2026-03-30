# Source: https://docs.aws.amazon.com/translate/latest/APIReference/llms.txt

# Amazon Translate API Reference 

> Details about operations and parameters in the Amazon Translate API Reference

## [Amazon Translate API Reference](https://docs.aws.amazon.com/translate/latest/APIReference/welcome.html)

### [Actions](https://docs.aws.amazon.com/translate/latest/APIReference/API_Operations.html)

The following actions are supported:

- [CreateParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_CreateParallelData.html): Creates a parallel data resource in Amazon Translate by importing an input file from Amazon S3.
- [DeleteParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_DeleteParallelData.html): Deletes a parallel data resource in Amazon Translate.
- [DeleteTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_DeleteTerminology.html): A synchronous action that deletes a custom terminology.
- [DescribeTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_DescribeTextTranslationJob.html): Gets the properties associated with an asynchronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.
- [GetParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_GetParallelData.html): Provides information about a parallel data resource.
- [GetTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_GetTerminology.html): Retrieves a custom terminology.
- [ImportTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_ImportTerminology.html): Creates or updates a custom terminology, depending on whether one already exists for the given terminology name.
- [ListLanguages](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListLanguages.html): Provides a list of languages (RFC-5646 codes and names) that Amazon Translate supports.
- [ListParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListParallelData.html): Provides a list of your parallel data resources in Amazon Translate.
- [ListTagsForResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTagsForResource.html): Lists all tags associated with a given Amazon Translate resource.
- [ListTerminologies](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTerminologies.html): Provides a list of custom terminologies associated with your account.
- [ListTextTranslationJobs](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTextTranslationJobs.html): Gets a list of the batch translation jobs that you have submitted.
- [StartTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_StartTextTranslationJob.html): Starts an asynchronous batch translation job.
- [StopTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_StopTextTranslationJob.html): Stops an asynchronous batch translation job that is in progress.
- [TagResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_TagResource.html): Associates a specific tag with a resource.
- [TranslateDocument](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateDocument.html): Translates the input document from the source language to the target language.
- [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html): Translates input text from the source language to the target language.
- [UntagResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_UntagResource.html): Removes a specific tag associated with an Amazon Translate resource.
- [UpdateParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_UpdateParallelData.html): Updates a previously created parallel data resource by importing a new input file from Amazon S3.

### [Data Types](https://docs.aws.amazon.com/translate/latest/APIReference/API_Types.html)

The following data types are supported:

- [AppliedTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_AppliedTerminology.html): The custom terminology applied to the input text by Amazon Translate for the translated text response.
- [Document](https://docs.aws.amazon.com/translate/latest/APIReference/API_Document.html): The content and content type of a document.
- [EncryptionKey](https://docs.aws.amazon.com/translate/latest/APIReference/API_EncryptionKey.html): The encryption key used to encrypt this object.
- [InputDataConfig](https://docs.aws.amazon.com/translate/latest/APIReference/API_InputDataConfig.html): The input configuration properties for requesting a batch translation job.
- [JobDetails](https://docs.aws.amazon.com/translate/latest/APIReference/API_JobDetails.html): The number of documents successfully and unsuccessfully processed during a translation job.
- [Language](https://docs.aws.amazon.com/translate/latest/APIReference/API_Language.html): A supported language.
- [OutputDataConfig](https://docs.aws.amazon.com/translate/latest/APIReference/API_OutputDataConfig.html): The output configuration properties for a batch translation job.
- [ParallelDataConfig](https://docs.aws.amazon.com/translate/latest/APIReference/API_ParallelDataConfig.html): Specifies the format and S3 location of the parallel data input file.
- [ParallelDataDataLocation](https://docs.aws.amazon.com/translate/latest/APIReference/API_ParallelDataDataLocation.html): The location of the most recent parallel data input file that was successfully imported into Amazon Translate.
- [ParallelDataProperties](https://docs.aws.amazon.com/translate/latest/APIReference/API_ParallelDataProperties.html): The properties of a parallel data resource.
- [Tag](https://docs.aws.amazon.com/translate/latest/APIReference/API_Tag.html): A key-value pair that adds as a metadata to a resource used by Amazon Translate.
- [Term](https://docs.aws.amazon.com/translate/latest/APIReference/API_Term.html): The term being translated by the custom terminology.
- [TerminologyData](https://docs.aws.amazon.com/translate/latest/APIReference/API_TerminologyData.html): The data associated with the custom terminology.
- [TerminologyDataLocation](https://docs.aws.amazon.com/translate/latest/APIReference/API_TerminologyDataLocation.html): The location of the custom terminology data.
- [TerminologyProperties](https://docs.aws.amazon.com/translate/latest/APIReference/API_TerminologyProperties.html): The properties of the custom terminology.
- [TextTranslationJobFilter](https://docs.aws.amazon.com/translate/latest/APIReference/API_TextTranslationJobFilter.html): Provides information for filtering a list of translation jobs.
- [TextTranslationJobProperties](https://docs.aws.amazon.com/translate/latest/APIReference/API_TextTranslationJobProperties.html): Provides information about a translation job.
- [TranslatedDocument](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslatedDocument.html): The translated content.
- [TranslationSettings](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslationSettings.html): Settings to configure your translation output.
- [Common Parameters](https://docs.aws.amazon.com/translate/latest/APIReference/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
- [Common Errors](https://docs.aws.amazon.com/translate/latest/APIReference/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
