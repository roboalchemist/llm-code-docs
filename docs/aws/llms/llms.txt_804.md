# Source: https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/llms.txt

# AWS Systems Manager GUI Connect API Reference

> AWS Systems Manager GUI Connect, a component of Fleet Manager, lets you connect to your Window Server-type Amazon Elastic Compute Cloud (Amazon EC2) instances using the Remote Desktop Protocol (RDP). GUI Connect, which is powered by Amazon DCV, provides you with secure connectivity to your Windows Server instances directly from the Systems Manager console. You can have up to four simultaneous connections in a single browser window. In the console, GUI Connect is also referred to as Fleet Manager Remote Desktop.

- [Welcome](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_Operations.html)

- [DeleteConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_DeleteConnectionRecordingPreferences.html): Deletes the preferences for recording RDP connections.
- [GetConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_GetConnectionRecordingPreferences.html): Returns the preferences specified for recording RDP connections in the requesting AWS account and AWS Region.
- [UpdateConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_UpdateConnectionRecordingPreferences.html): Updates the preferences for recording RDP connections.


## [Data Types](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_Types.html)

- [ConnectionRecordingPreferences](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_ConnectionRecordingPreferences.html): The set of preferences used for recording RDP connections in the requesting AWS account and AWS Region.
- [RecordingDestinations](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_RecordingDestinations.html): Determines where recordings of RDP connections are stored.
- [S3Bucket](https://docs.aws.amazon.com/ssm-guiconnect/latest/APIReference/API_S3Bucket.html): The S3 bucket where RDP connection recordings are stored.
