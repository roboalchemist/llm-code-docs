# Source: https://docs.aws.amazon.com/iotevents-data/latest/apireference/llms.txt

# AWS IoT Events Data API Reference

> AWS IoT Events monitors your equipment or device fleets for failures or changes in operation, and triggers actions when such events occur. You can use AWS IoT Events Data API commands to send inputs to detectors, list detectors, and view or update a detector's status.

- [Welcome](https://docs.aws.amazon.com/iotevents-data/latest/apireference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/iotevents-data/latest/apireference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/iotevents-data/latest/apireference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Operations.html)

- [BatchAcknowledgeAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchAcknowledgeAlarm.html)
- [BatchDeleteDetector](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchDeleteDetector.html)
- [BatchDisableAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchDisableAlarm.html)
- [BatchEnableAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchEnableAlarm.html)
- [BatchPutMessage](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchPutMessage.html)
- [BatchResetAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchResetAlarm.html)
- [BatchSnoozeAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchSnoozeAlarm.html)
- [BatchUpdateDetector](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchUpdateDetector.html)
- [DescribeAlarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DescribeAlarm.html)
- [DescribeDetector](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DescribeDetector.html)
- [ListAlarms](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_ListAlarms.html)
- [ListDetectors](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_ListDetectors.html)


## [Data Types](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Types.html)

- [AcknowledgeActionConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_AcknowledgeActionConfiguration.html): Contains the configuration information of an acknowledge action.
- [AcknowledgeAlarmActionRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_AcknowledgeAlarmActionRequest.html): Information needed to acknowledge the alarm.
- [Alarm](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Alarm.html): Contains information about an alarm.
- [AlarmState](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_AlarmState.html): Contains information about the current state of the alarm.
- [AlarmSummary](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_AlarmSummary.html): Contains a summary of an alarm.
- [BatchAlarmActionErrorEntry](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchAlarmActionErrorEntry.html): Contains error messages associated with one of the following requests:
- [BatchDeleteDetectorErrorEntry](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchDeleteDetectorErrorEntry.html): Contains error messages associated with the deletion request.
- [BatchPutMessageErrorEntry](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchPutMessageErrorEntry.html): Contains information about the errors encountered.
- [BatchUpdateDetectorErrorEntry](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_BatchUpdateDetectorErrorEntry.html): Information about the error that occurred when attempting to update a detector.
- [CustomerAction](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_CustomerAction.html): Contains information about the action that you can take to respond to the alarm.
- [DeleteDetectorRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DeleteDetectorRequest.html): Information used to delete the detector model.
- [Detector](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Detector.html): Information about the detector (instance).
- [DetectorState](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DetectorState.html): Information about the current state of the detector instance.
- [DetectorStateDefinition](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DetectorStateDefinition.html): The new state, variable values, and timer settings of the detector (instance).
- [DetectorStateSummary](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DetectorStateSummary.html): Information about the detector state.
- [DetectorSummary](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DetectorSummary.html): Information about the detector (instance).
- [DisableActionConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DisableActionConfiguration.html): Contains the configuration information of a disable action.
- [DisableAlarmActionRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_DisableAlarmActionRequest.html): Information used to disable the alarm.
- [EnableActionConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_EnableActionConfiguration.html): Contains the configuration information of an enable action.
- [EnableAlarmActionRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_EnableAlarmActionRequest.html): Information needed to enable the alarm.
- [Message](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Message.html): Information about a message.
- [ResetActionConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_ResetActionConfiguration.html): Contains the configuration information of a reset action.
- [ResetAlarmActionRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_ResetAlarmActionRequest.html): Information needed to reset the alarm.
- [RuleEvaluation](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_RuleEvaluation.html): Information needed to evaluate data.
- [SimpleRuleEvaluation](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_SimpleRuleEvaluation.html): Information needed to compare two values with a comparison operator.
- [SnoozeActionConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_SnoozeActionConfiguration.html): Contains the configuration information of a snooze action.
- [SnoozeAlarmActionRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_SnoozeAlarmActionRequest.html): Information needed to snooze the alarm.
- [StateChangeConfiguration](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_StateChangeConfiguration.html): Contains the configuration information of alarm state changes.
- [SystemEvent](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_SystemEvent.html): Contains information about alarm state changes.
- [Timer](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Timer.html): The current state of a timer.
- [TimerDefinition](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_TimerDefinition.html): The new setting of a timer.
- [TimestampValue](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_TimestampValue.html): Contains information about a timestamp.
- [UpdateDetectorRequest](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_UpdateDetectorRequest.html): Information used to update the detector (instance).
- [Variable](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_Variable.html): The current state of the variable.
- [VariableDefinition](https://docs.aws.amazon.com/iotevents-data/latest/apireference/API_VariableDefinition.html): The new value of the variable.
