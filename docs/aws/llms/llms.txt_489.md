# Source: https://docs.aws.amazon.com/iotevents/latest/apireference/llms.txt

# AWS IoT Events API Reference

## [AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/apireference/Welcome_AWS_IoT_Events.html)

AWS IoT Events monitors your equipment or device fleets for failures or changes in operation, and triggers actions when such events occur. You can use AWS IoT Events API operations to create, read, update, and delete inputs and detector models, and to list their versions.

### Actions

- [CreateAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateAlarmModel.html)
- [CreateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateDetectorModel.html)
- [CreateInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateInput.html)
- [DeleteAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteAlarmModel.html)
- [DeleteDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteDetectorModel.html)
- [DeleteInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DeleteInput.html)
- [DescribeAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeAlarmModel.html)
- [DescribeDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeDetectorModel.html)
- [DescribeDetectorModelAnalysis](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeDetectorModelAnalysis.html)
- [DescribeInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeInput.html)
- [DescribeLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DescribeLoggingOptions.html)
- [GetDetectorModelAnalysisResults](https://docs.aws.amazon.com/iotevents/latest/apireference/API_GetDetectorModelAnalysisResults.html)
- [ListAlarmModels](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListAlarmModels.html)
- [ListAlarmModelVersions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListAlarmModelVersions.html)
- [ListDetectorModels](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListDetectorModels.html)
- [ListDetectorModelVersions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListDetectorModelVersions.html)
- [ListInputRoutings](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListInputRoutings.html)
- [ListInputs](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListInputs.html)
- [ListTagsForResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ListTagsForResource.html)
- [PutLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_PutLoggingOptions.html)
- [StartDetectorModelAnalysis](https://docs.aws.amazon.com/iotevents/latest/apireference/API_StartDetectorModelAnalysis.html)
- [TagResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_TagResource.html)
- [UntagResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UntagResource.html)
- [UpdateAlarmModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateAlarmModel.html)
- [UpdateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateDetectorModel.html)
- [UpdateInput](https://docs.aws.amazon.com/iotevents/latest/apireference/API_UpdateInput.html)

### Data Types

- [AcknowledgeFlow](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AcknowledgeFlow.html): Specifies whether to get notified for alarm state changes.
- [Action](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Action.html): An action to be performed when the condition is TRUE.
- [AlarmAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmAction.html): Specifies one of the following actions to receive notifications when the alarm state changes.
- [AlarmCapabilities](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmCapabilities.html): Contains the configuration information of alarm state changes.
- [AlarmEventActions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmEventActions.html): Contains information about one or more alarm actions.
- [AlarmModelSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmModelSummary.html): Contains a summary of an alarm model.
- [AlarmModelVersionSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmModelVersionSummary.html): Contains a summary of an alarm model version.
- [AlarmNotification](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmNotification.html): Contains information about one or more notification actions.
- [AlarmRule](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AlarmRule.html): Defines when your alarm is invoked.
- [AnalysisResult](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AnalysisResult.html): Contains the result of the analysis.
- [AnalysisResultLocation](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AnalysisResultLocation.html): Contains information that you can use to locate the field in your detector model that the analysis result references.
- [AssetPropertyTimestamp](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AssetPropertyTimestamp.html): A structure that contains timestamp information.
- [AssetPropertyValue](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AssetPropertyValue.html): A structure that contains value information.
- [AssetPropertyVariant](https://docs.aws.amazon.com/iotevents/latest/apireference/API_AssetPropertyVariant.html): A structure that contains an asset property value.
- [Attribute](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Attribute.html): The attributes from the JSON payload that are made available by the input.
- [ClearTimerAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ClearTimerAction.html): Information needed to clear the timer.
- [DetectorDebugOption](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorDebugOption.html): The detector model and the specific detectors (instances) for which the logging level is given.
- [DetectorModel](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorModel.html): Information about the detector model.
- [DetectorModelConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorModelConfiguration.html): Information about how the detector model is configured.
- [DetectorModelDefinition](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorModelDefinition.html): Information that defines how a detector operates.
- [DetectorModelSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorModelSummary.html): Information about the detector model.
- [DetectorModelVersionSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DetectorModelVersionSummary.html): Information about the detector model version.
- [DynamoDBAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DynamoDBAction.html): Defines an action to write to the Amazon DynamoDB table that you created.
- [DynamoDBv2Action](https://docs.aws.amazon.com/iotevents/latest/apireference/API_DynamoDBv2Action.html): Defines an action to write to the Amazon DynamoDB table that you created.
- [EmailConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_EmailConfiguration.html): Contains the configuration information of email notifications.
- [EmailContent](https://docs.aws.amazon.com/iotevents/latest/apireference/API_EmailContent.html): Contains the subject and message of an email.
- [EmailRecipients](https://docs.aws.amazon.com/iotevents/latest/apireference/API_EmailRecipients.html): Contains the information of one or more recipients who receive the emails.
- [Event](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Event.html): Specifies the actions to be performed when the condition evaluates to TRUE.
- [FirehoseAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_FirehoseAction.html): Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.
- [InitializationConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_InitializationConfiguration.html): Specifies the default alarm state.
- [Input](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html): Information about the input.
- [InputConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_InputConfiguration.html): Information about the configuration of an input.
- [InputDefinition](https://docs.aws.amazon.com/iotevents/latest/apireference/API_InputDefinition.html): The definition of the input.
- [InputIdentifier](https://docs.aws.amazon.com/iotevents/latest/apireference/API_InputIdentifier.html): The identifier of the input.
- [InputSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_InputSummary.html): Information about the input.
- [IotEventsAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotEventsAction.html): Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.
- [IotEventsInputIdentifier](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotEventsInputIdentifier.html): The identifier of the input routed to AWS IoT Events.
- [IotSiteWiseAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotSiteWiseAction.html): Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise.
- [IotSiteWiseAssetModelPropertyIdentifier](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotSiteWiseAssetModelPropertyIdentifier.html): The asset model property identifier of the input routed from AWS IoT SiteWise.
- [IotSiteWiseInputIdentifier](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotSiteWiseInputIdentifier.html): The identifier of the input routed from AWS IoT SiteWise.
- [IotTopicPublishAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_IotTopicPublishAction.html): Information required to publish the MQTT message through the AWS IoT message broker.
- [LambdaAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_LambdaAction.html): Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.
- [LoggingOptions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_LoggingOptions.html): The values of the AWS IoT Events logging options.
- [NotificationAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_NotificationAction.html): Contains the notification settings of an alarm model.
- [NotificationTargetActions](https://docs.aws.amazon.com/iotevents/latest/apireference/API_NotificationTargetActions.html): Specifies an AWS Lambda function to manage alarm notifications.
- [OnEnterLifecycle](https://docs.aws.amazon.com/iotevents/latest/apireference/API_OnEnterLifecycle.html): When entering this state, perform these actions if the condition is TRUE.
- [OnExitLifecycle](https://docs.aws.amazon.com/iotevents/latest/apireference/API_OnExitLifecycle.html): When exiting this state, perform these actions if the specified condition is TRUE.
- [OnInputLifecycle](https://docs.aws.amazon.com/iotevents/latest/apireference/API_OnInputLifecycle.html): Specifies the actions performed when the condition evaluates to TRUE.
- [Payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html): Information needed to configure the payload.
- [RecipientDetail](https://docs.aws.amazon.com/iotevents/latest/apireference/API_RecipientDetail.html): The information that identifies the recipient.
- [ResetTimerAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_ResetTimerAction.html): Information required to reset the timer.
- [RoutedResource](https://docs.aws.amazon.com/iotevents/latest/apireference/API_RoutedResource.html): Contains information about the routed resource.
- [SetTimerAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SetTimerAction.html): Information needed to set the timer.
- [SetVariableAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SetVariableAction.html): Information about the variable and its new value.
- [SimpleRule](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SimpleRule.html): A rule that compares an input property value to a threshold value with a comparison operator.
- [SMSConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SMSConfiguration.html): Contains the configuration information of SMS notifications.
- [SNSTopicPublishAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SNSTopicPublishAction.html): Information required to publish the Amazon SNS message.
- [SqsAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SqsAction.html): Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.
- [SSOIdentity](https://docs.aws.amazon.com/iotevents/latest/apireference/API_SSOIdentity.html): Contains information about your identity source in AWS IAM Identity Center.
- [State](https://docs.aws.amazon.com/iotevents/latest/apireference/API_State.html): Information that defines a state of a detector.
- [Tag](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Tag.html): Metadata that can be used to manage the resource.
- [TransitionEvent](https://docs.aws.amazon.com/iotevents/latest/apireference/API_TransitionEvent.html): Specifies the actions performed and the next state entered when a condition evaluates to TRUE.

## [AWS IoT Events Data](https://docs.aws.amazon.com/iotevents/latest/apireference/Welcome_AWS_IoT_Events_Data.html)

AWS IoT Events monitors your equipment or device fleets for failures or changes in operation, and triggers actions when such events occur. You can use AWS IoT Events Data API commands to send inputs to detectors, list detectors, and view or update a detector's status.

For more information, see [What is AWS IoT Events?](https://docs.aws.amazon.com/iotevents/latest/developerguide/what-is-iotevents.html)in the AWS IoT Events Developer Guide.

### Actions

- [BatchAcknowledgeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchAcknowledgeAlarm.html)
- [BatchDeleteDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDeleteDetector.html)
- [BatchDisableAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDisableAlarm.html)
- [BatchEnableAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchEnableAlarm.html)
- [BatchPutMessage](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html)
- [BatchResetAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchResetAlarm.html)
- [BatchSnoozeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchSnoozeAlarm.html)
- [BatchUpdateDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchUpdateDetector.html)
- [DescribeAlarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DescribeAlarm.html)
- [DescribeDetector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DescribeDetector.html)
- [ListAlarms](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListAlarms.html)
- [ListDetectors](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ListDetectors.html)

### Data Types

- [AcknowledgeActionConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_AcknowledgeActionConfiguration.html): Contains the configuration information of an acknowledge action.
- [AcknowledgeAlarmActionRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_AcknowledgeAlarmActionRequest.html): Information needed to acknowledge the alarm.
- [Alarm](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_Alarm.html): Contains information about an alarm.
- [AlarmState](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_AlarmState.html): Contains information about the current state of the alarm.
- [AlarmSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_AlarmSummary.html): Contains a summary of an alarm.
- [BatchAlarmActionErrorEntry](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchAlarmActionErrorEntry.html): Contains error messages associated with one of the following requests:
- [BatchDeleteDetectorErrorEntry](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchDeleteDetectorErrorEntry.html): Contains error messages associated with the deletion request.
- [BatchPutMessageErrorEntry](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessageErrorEntry.html): Contains information about the errors encountered.
- [BatchUpdateDetectorErrorEntry](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchUpdateDetectorErrorEntry.html): Information about the error that occurred when attempting to update a detector.
- [CustomerAction](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_CustomerAction.html): Contains information about the action that you can take to respond to the alarm.
- [DeleteDetectorRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DeleteDetectorRequest.html): Information used to delete the detector model.
- [Detector](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_Detector.html): Information about the detector (instance).
- [DetectorState](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DetectorState.html): Information about the current state of the detector instance.
- [DetectorStateDefinition](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DetectorStateDefinition.html): The new state, variable values, and timer settings of the detector (instance).
- [DetectorStateSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DetectorStateSummary.html): Information about the detector state.
- [DetectorSummary](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DetectorSummary.html): Information about the detector (instance).
- [DisableActionConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DisableActionConfiguration.html): Contains the configuration information of a disable action.
- [DisableAlarmActionRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_DisableAlarmActionRequest.html): Information used to disable the alarm.
- [EnableActionConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_EnableActionConfiguration.html): Contains the configuration information of an enable action.
- [EnableAlarmActionRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_EnableAlarmActionRequest.html): Information needed to enable the alarm.
- [Message](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_Message.html): Information about a message.
- [ResetActionConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ResetActionConfiguration.html): Contains the configuration information of a reset action.
- [ResetAlarmActionRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_ResetAlarmActionRequest.html): Information needed to reset the alarm.
- [RuleEvaluation](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_RuleEvaluation.html): Information needed to evaluate data.
- [SimpleRuleEvaluation](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_SimpleRuleEvaluation.html): Information needed to compare two values with a comparison operator.
- [SnoozeActionConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_SnoozeActionConfiguration.html): Contains the configuration information of a snooze action.
- [SnoozeAlarmActionRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_SnoozeAlarmActionRequest.html): Information needed to snooze the alarm.
- [StateChangeConfiguration](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_StateChangeConfiguration.html): Contains the configuration information of alarm state changes.
- [SystemEvent](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_SystemEvent.html): Contains information about alarm state changes.
- [Timer](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_Timer.html): The current state of a timer.
- [TimerDefinition](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_TimerDefinition.html): The new setting of a timer.
- [TimestampValue](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_TimestampValue.html): Contains information about a timestamp.
- [UpdateDetectorRequest](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_UpdateDetectorRequest.html): Information used to update the detector (instance).
- [Variable](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_Variable.html): The current state of the variable.
- [VariableDefinition](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_VariableDefinition.html): The new value of the variable.

## Common

- [Common Parameters](https://docs.aws.amazon.com/iotevents/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/iotevents/latest/apireference/CommonErrors.html)