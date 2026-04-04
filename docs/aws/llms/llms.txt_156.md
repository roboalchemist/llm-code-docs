# Source: https://docs.aws.amazon.com/b2bi/latest/APIReference/llms.txt

# AWS B2B Data Interchange API Reference

> This is the official Amazon Web Services API Reference for AWS B2B Data Interchange. TEST

- [Welcome](https://docs.aws.amazon.com/b2bi/latest/APIReference/api-welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/b2bi/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/b2bi/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Operations.html)

- [CreateCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateCapability.html): Instantiates a capability based on the specified parameters.
- [CreatePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreatePartnership.html): Creates a partnership between a customer and a trading partner, based on the supplied parameters.
- [CreateProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateProfile.html): Creates a customer profile.
- [CreateStarterMappingTemplate](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateStarterMappingTemplate.html): AWS B2B Data Interchange uses a mapping template in JSONata or XSLT format to transform a customer input file into a JSON or XML file that can be converted to EDI.
- [CreateTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateTransformer.html): Creates a transformer.
- [DeleteCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteCapability.html): Deletes the specified capability.
- [DeletePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeletePartnership.html): Deletes the specified partnership.
- [DeleteProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteProfile.html): Deletes the specified profile.
- [DeleteTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteTransformer.html): Deletes the specified transformer.
- [GenerateMapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GenerateMapping.html): Takes sample input and output documents and uses Amazon Bedrock to generate a mapping automatically.
- [GetCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetCapability.html): Retrieves the details for the specified capability.
- [GetPartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetPartnership.html): Retrieves the details for a partnership, based on the partner and profile IDs specified.
- [GetProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetProfile.html): Retrieves the details for the profile specified by the profile ID.
- [GetTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformer.html): Retrieves the details for the transformer specified by the transformer ID.
- [GetTransformerJob](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformerJob.html): Returns the details of the transformer run, based on the Transformer job ID.
- [ListCapabilities](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListCapabilities.html): Lists the capabilities associated with your AWS account for your current or specified region.
- [ListPartnerships](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListPartnerships.html): Lists the partnerships associated with your AWS account for your current or specified region.
- [ListProfiles](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListProfiles.html): Lists the profiles associated with your AWS account for your current or specified region.
- [ListTagsForResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTagsForResource.html): Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify.
- [ListTransformers](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTransformers.html): Lists the available transformers.
- [StartTransformerJob](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_StartTransformerJob.html): Runs a job, using a transformer, to parse input EDI (electronic data interchange) file into the output structures used by AWS B2B Data Interchange.
- [TagResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TagResource.html): Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN).
- [TestConversion](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestConversion.html): This operation mimics the latter half of a typical Outbound EDI request.
- [TestMapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestMapping.html): Maps the input file according to the provided template file.
- [TestParsing](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestParsing.html): Parses the input EDI (electronic data interchange) file.
- [UntagResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UntagResource.html): Detaches a key-value pair from the specified resource, as identified by its Amazon Resource Name (ARN).
- [UpdateCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateCapability.html): Updates some of the parameters for a capability, based on the specified parameters.
- [UpdatePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdatePartnership.html): Updates some of the parameters for a partnership between a customer and trading partner.
- [UpdateProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateProfile.html): Updates the specified parameters for a profile.
- [UpdateTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateTransformer.html): Updates the specified parameters for a transformer.


## [Data Types](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Types.html)

- [AdvancedOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_AdvancedOptions.html): A structure that contains advanced options for EDI processing.
- [CapabilityConfiguration](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilityConfiguration.html): A capability object.
- [CapabilityOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilityOptions.html): Contains the details for an Outbound EDI capability.
- [CapabilitySummary](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CapabilitySummary.html): Returns the capability summary details.
- [ConversionSource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionSource.html): Describes the input for an outbound transformation.
- [ConversionTarget](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionTarget.html): Provide a sample of what the output of the transformation should look like.
- [ConversionTargetFormatDetails](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ConversionTargetFormatDetails.html): Contains a structure describing the X12 details for the conversion target.
- [EdiConfiguration](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_EdiConfiguration.html): Specifies the details for the EDI (electronic data interchange) transformation.
- [EdiType](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_EdiType.html): Specifies the details for the EDI standard that is being used for the transformer.
- [FormatOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_FormatOptions.html): A structure that contains the X12 transaction set and version.
- [InboundEdiOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_InboundEdiOptions.html): Contains options for processing inbound EDI files.
- [InputConversion](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_InputConversion.html): Contains the input formatting options for an inbound transformer (takes an X12-formatted EDI document as input and converts it to JSON or XML.
- [InputFileSource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_InputFileSource.html): The input file to use for an outbound transformation.
- [Mapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html): Specifies the mapping template for the transformer.
- [OutboundEdiOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_OutboundEdiOptions.html): A container for outbound EDI options.
- [OutputConversion](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_OutputConversion.html): Contains the formatting options for an outbound transformer (takes JSON or XML as input and converts it to an EDI document (currently only X12 format is supported).
- [OutputSampleFileSource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_OutputSampleFileSource.html): Container for the location of a sample file used for outbound transformations.
- [PartnershipSummary](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_PartnershipSummary.html): A structure that contains the details for a partnership.
- [ProfileSummary](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ProfileSummary.html): Contains the details for a profile.
- [S3Location](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_S3Location.html): Specifies the details for the Amazon S3 file location that is being used with AWS B2B Data Interchange.
- [SampleDocumentKeys](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_SampleDocumentKeys.html): An array of the Amazon S3 keys used to identify the location for your sample documents.
- [SampleDocuments](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_SampleDocuments.html): Describes a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
- [Tag](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Tag.html): Creates a key-value pair for a specific resource.
- [TemplateDetails](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TemplateDetails.html): A data structure that contains the information to use when generating a mapping template.
- [TransformerSummary](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TransformerSummary.html): Contains the details for a transformer object.
- [WrapOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_WrapOptions.html): Contains options for wrapping (line folding) in X12 EDI files.
- [X12AcknowledgmentOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12AcknowledgmentOptions.html): Contains options for configuring X12 acknowledgments.
- [X12AdvancedOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12AdvancedOptions.html): Contains advanced options specific to X12 EDI processing, such as splitting large X12 files into smaller units.
- [X12CodeListValidationRule](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12CodeListValidationRule.html): Defines a validation rule that modifies the allowed code values for a specific X12 element.
- [X12ControlNumbers](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ControlNumbers.html): Contains configuration for X12 control numbers used in X12 EDI generation.
- [X12Delimiters](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12Delimiters.html): In X12 EDI messages, delimiters are used to mark the end of segments or elements, and are defined in the interchange control header.
- [X12Details](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12Details.html): A structure that contains the X12 transaction set and version.
- [X12ElementLengthValidationRule](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ElementLengthValidationRule.html): Defines a validation rule that specifies custom length constraints for a specific X12 element.
- [X12ElementRequirementValidationRule](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ElementRequirementValidationRule.html): Defines a validation rule that modifies the requirement status of a specific X12 element within a segment.
- [X12Envelope](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12Envelope.html): A wrapper structure for an X12 definition object.
- [X12FunctionalGroupHeaders](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12FunctionalGroupHeaders.html): Part of the X12 message structure.
- [X12InboundEdiOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12InboundEdiOptions.html): Contains options specific to processing inbound X12 EDI files.
- [X12InterchangeControlHeaders](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12InterchangeControlHeaders.html): In X12, the Interchange Control Header is the first segment of an EDI document and is part of the Interchange Envelope.
- [X12OutboundEdiHeaders](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12OutboundEdiHeaders.html): A structure containing the details for an outbound EDI object.
- [X12SplitOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12SplitOptions.html): Contains options for splitting X12 EDI files into smaller units.
- [X12ValidationOptions](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ValidationOptions.html): Contains configuration options for X12 EDI validation.
- [X12ValidationRule](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ValidationRule.html): Represents a single validation rule that can be applied during X12 EDI processing.
