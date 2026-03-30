# Source: https://docs.aws.amazon.com/comprehend-medical/latest/api/llms.txt

# Amazon Comprehend Medical API Reference

> This is the Amazon Comprehend Medical API Reference. Amazon Comprehend Medical extracts structured information from unstructured clinical text. For an introduction to the service, see the Amazon Comprehend Medical Developer Guide.

- [Welcome](https://docs.aws.amazon.com/comprehend-medical/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/comprehend-medical/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/comprehend-medical/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Operations.html)

- [DescribeEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeEntitiesDetectionV2Job.html): Gets the properties associated with a medical entities detection job.
- [DescribeICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeICD10CMInferenceJob.html): Gets the properties associated with an InferICD10CM job.
- [DescribePHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribePHIDetectionJob.html): Gets the properties associated with a protected health information (PHI) detection job.
- [DescribeRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeRxNormInferenceJob.html): Gets the properties associated with an InferRxNorm job.
- [DescribeSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DescribeSNOMEDCTInferenceJob.html): Gets the properties associated with an InferSNOMEDCT job.
- [DetectEntities](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectEntities.html): The DetectEntities operation is deprecated.
- [DetectEntitiesV2](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectEntitiesV2.html): Inspects the clinical text for a variety of medical entities and returns specific information about them such as entity category, location, and confidence score on that information.
- [DetectPHI](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_DetectPHI.html): Inspects the clinical text for protected health information (PHI) entities and returns the entity category, location, and confidence score for each entity.
- [InferICD10CM](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferICD10CM.html): InferICD10CM detects medical conditions as entities listed in a patient record and links those entities to normalized concept identifiers in the ICD-10-CM knowledge base from the Centers for Disease Control.
- [InferRxNorm](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferRxNorm.html): InferRxNorm detects medications as entities listed in a patient record and links to the normalized concept identifiers in the RxNorm database from the National Library of Medicine.
- [InferSNOMEDCT](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InferSNOMEDCT.html): InferSNOMEDCT detects possible medical concepts as entities and links them to codes from the Systematized Nomenclature of Medicine, Clinical Terms (SNOMED-CT) ontology.
- [ListEntitiesDetectionV2Jobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListEntitiesDetectionV2Jobs.html): Gets a list of medical entity detection jobs that you have submitted.
- [ListICD10CMInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListICD10CMInferenceJobs.html): Gets a list of InferICD10CM jobs that you have submitted.
- [ListPHIDetectionJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListPHIDetectionJobs.html): Gets a list of protected health information (PHI) detection jobs that you have submitted.
- [ListRxNormInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListRxNormInferenceJobs.html): Gets a list of InferRxNorm jobs that you have submitted.
- [ListSNOMEDCTInferenceJobs](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ListSNOMEDCTInferenceJobs.html): Gets a list of InferSNOMEDCT jobs a user has submitted.
- [StartEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartEntitiesDetectionV2Job.html): Starts an asynchronous medical entity detection job for a collection of documents.
- [StartICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartICD10CMInferenceJob.html): Starts an asynchronous job to detect medical conditions and link them to the ICD-10-CM ontology.
- [StartPHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartPHIDetectionJob.html): Starts an asynchronous job to detect protected health information (PHI).
- [StartRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartRxNormInferenceJob.html): Starts an asynchronous job to detect medication entities and link them to the RxNorm ontology.
- [StartSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StartSNOMEDCTInferenceJob.html): Starts an asynchronous job to detect medical concepts and link them to the SNOMED-CT ontology.
- [StopEntitiesDetectionV2Job](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopEntitiesDetectionV2Job.html): Stops a medical entities detection job in progress.
- [StopICD10CMInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopICD10CMInferenceJob.html): Stops an InferICD10CM inference job in progress.
- [StopPHIDetectionJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopPHIDetectionJob.html): Stops a protected health information (PHI) detection job in progress.
- [StopRxNormInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopRxNormInferenceJob.html): Stops an InferRxNorm inference job in progress.
- [StopSNOMEDCTInferenceJob](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopSNOMEDCTInferenceJob.html): Stops an InferSNOMEDCT inference job in progress.


## [Data Types](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Types.html)

- [Attribute](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Attribute.html): An extracted segment of the text that is an attribute of an entity, or otherwise related to an entity, such as the dosage of a medication taken.
- [Characters](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Characters.html): The number of characters in the input text to be analyzed.
- [ComprehendMedicalAsyncJobFilter](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ComprehendMedicalAsyncJobFilter.html): Provides information for filtering a list of detection jobs.
- [ComprehendMedicalAsyncJobProperties](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ComprehendMedicalAsyncJobProperties.html): Provides information about a detection job.
- [Entity](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Entity.html): Provides information about an extracted medical entity.
- [ICD10CMAttribute](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMAttribute.html): The detected attributes that relate to an entity.
- [ICD10CMConcept](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMConcept.html): The ICD-10-CM concepts that the entity could refer to, along with a score indicating the likelihood of the match.
- [ICD10CMEntity](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMEntity.html): The collection of medical entities extracted from the input text and their associated information.
- [ICD10CMTrait](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_ICD10CMTrait.html): Contextual information for the entity.
- [InputDataConfig](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_InputDataConfig.html): The input properties for an entities detection job.
- [OutputDataConfig](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_OutputDataConfig.html): The output properties for a detection job.
- [RxNormAttribute](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormAttribute.html): The extracted attributes that relate to this entity.
- [RxNormConcept](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormConcept.html): The RxNorm concept that the entity could refer to, along with a score indicating the likelihood of the match.
- [RxNormEntity](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormEntity.html): The collection of medical entities extracted from the input text and their associated information.
- [RxNormTrait](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_RxNormTrait.html): The contextual information for the entity.
- [SNOMEDCTAttribute](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTAttribute.html): The extracted attributes that relate to an entity.
- [SNOMEDCTConcept](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTConcept.html): The SNOMED-CT concepts that the entity could refer to, along with a score indicating the likelihood of the match.
- [SNOMEDCTDetails](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTDetails.html): The information about the revision of the SNOMED-CT ontology in the response.
- [SNOMEDCTEntity](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTEntity.html): The collection of medical entities extracted from the input text and their associated information.
- [SNOMEDCTTrait](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_SNOMEDCTTrait.html): Contextual information for an entity.
- [Trait](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_Trait.html): Provides contextual information about the extracted entity.
- [UnmappedAttribute](https://docs.aws.amazon.com/comprehend-medical/latest/api/API_UnmappedAttribute.html): An attribute that was extracted, but Comprehend Medical; was unable to relate to an entity.
