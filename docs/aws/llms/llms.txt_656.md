# Source: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/llms.txt

# AWS Private CA Connector for SCEP Welcome

> Connector for SCEP creates a connector between AWS Private CA and your SCEP-enabled clients and devices. For more information, see Connector for SCEP in the AWS Private CA User Guide.

- [Welcome](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Operations.html)

- [CreateChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateChallenge.html): For general-purpose connectors.
- [CreateConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_CreateConnector.html): Creates a SCEP connector.
- [DeleteChallenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_DeleteChallenge.html): Deletes the specified Challenge.
- [DeleteConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_DeleteConnector.html): Deletes the specified Connector.
- [GetChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengeMetadata.html): Retrieves the metadata for the specified Challenge.
- [GetChallengePassword](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetChallengePassword.html): Retrieves the challenge password for the specified Challenge.
- [GetConnector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_GetConnector.html): Retrieves details about the specified Connector.
- [ListChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListChallengeMetadata.html): Retrieves the challenge metadata for the specified ARN.
- [ListConnectors](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html): Lists the connectors belonging to your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListTagsForResource.html): Retrieves the tags associated with the specified resource.
- [TagResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_TagResource.html): Adds one or more tags to your resource.
- [UntagResource](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_UntagResource.html): Removes one or more tags from your resource.


## [Data Types](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Types.html)

- [Challenge](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html): For Connector for SCEP for general-purpose.
- [ChallengeMetadata](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ChallengeMetadata.html): Contains details about the connector's challenge.
- [ChallengeMetadataSummary](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ChallengeMetadataSummary.html): Details about the specified challenge, returned by the GetChallengeMetadata action.
- [Connector](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Connector.html): Connector for SCEP is a service that links AWS Private Certificate Authority to your SCEP-enabled devices.
- [ConnectorSummary](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ConnectorSummary.html): Lists the AWS Private CA SCEP connectors belonging to your AWS account.
- [IntuneConfiguration](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_IntuneConfiguration.html): Contains configuration details for use with Microsoft Intune.
- [MobileDeviceManagement](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_MobileDeviceManagement.html): If you don't supply a value, by default Connector for SCEP creates a connector for general-purpose use.
- [OpenIdConfiguration](https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_OpenIdConfiguration.html): Contains OpenID Connect (OIDC) parameters for use with Microsoft Intune.
