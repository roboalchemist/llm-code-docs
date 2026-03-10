# Source: https://docs.aws.amazon.com/autoscaling/application/APIReference/llms.txt

# Application Auto Scaling API Reference

> This is the Application Auto Scaling API Reference. With Application Auto Scaling, you can configure automatic scaling for the following resources:

- [Welcome](https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/autoscaling/application/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/autoscaling/application/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_Operations.html)

- [DeleteScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeleteScalingPolicy.html): Deletes the specified scaling policy for an Application Auto Scaling scalable target.
- [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeleteScheduledAction.html): Deletes the specified scheduled action for an Application Auto Scaling scalable target.
- [DeregisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html): Deregisters an Application Auto Scaling scalable target when you have finished using it.
- [DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html): Gets information about the scalable targets in the specified namespace.
- [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingActivities.html): Provides descriptive information about the scaling activities in the specified namespace from the previous six weeks.
- [DescribeScalingPolicies](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingPolicies.html): Describes the Application Auto Scaling scaling policies for the specified service namespace.
- [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScheduledActions.html): Describes the Application Auto Scaling scheduled actions for the specified service namespace.
- [GetPredictiveScalingForecast](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_GetPredictiveScalingForecast.html): Retrieves the forecast data for a predictive scaling policy.
- [ListTagsForResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ListTagsForResource.html): Returns all the tags on the specified Application Auto Scaling scalable target.
- [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html): Creates or updates a scaling policy for an Application Auto Scaling scalable target.
- [PutScheduledAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html): Creates or updates a scheduled action for an Application Auto Scaling scalable target.
- [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html): Registers or updates a scalable target, which is the resource that you want to scale.
- [TagResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TagResource.html): Adds or edits tags on an Application Auto Scaling scalable target.
- [UntagResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_UntagResource.html): Deletes tags from an Application Auto Scaling scalable target.


## [Data Types](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_Types.html)

- [Alarm](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_Alarm.html): Represents a CloudWatch alarm associated with a scaling policy.
- [CapacityForecast](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CapacityForecast.html): A GetPredictiveScalingForecast call returns the capacity forecast for a predictive scaling policy.
- [CustomizedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_CustomizedMetricSpecification.html): Represents a CloudWatch metric of your choosing for a target tracking scaling policy to use with Application Auto Scaling.
- [LoadForecast](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_LoadForecast.html): A GetPredictiveScalingForecast call returns the load forecast for a predictive scaling policy.
- [MetricDimension](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_MetricDimension.html): Describes the dimension names and values associated with a metric.
- [NotScaledReason](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_NotScaledReason.html): Describes the reason for an activity that isn't scaled (not scaled activity), in machine-readable format.
- [PredefinedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredefinedMetricSpecification.html): Represents a predefined metric for a target tracking scaling policy to use with Application Auto Scaling.
- [PredictiveScalingCustomizedMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingCustomizedMetricSpecification.html): Represents a CloudWatch metric of your choosing for a predictive scaling policy.
- [PredictiveScalingMetric](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetric.html): Describes the scaling metric.
- [PredictiveScalingMetricDataQuery](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricDataQuery.html): The metric data to return.
- [PredictiveScalingMetricDimension](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricDimension.html): Describes the dimension of a metric.
- [PredictiveScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricSpecification.html): This structure specifies the metrics and target utilization settings for a predictive scaling policy.
- [PredictiveScalingMetricStat](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricStat.html): This structure defines the CloudWatch metric to return, along with the statistic and unit.
- [PredictiveScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPolicyConfiguration.html): Represents a predictive scaling policy configuration.
- [PredictiveScalingPredefinedLoadMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPredefinedLoadMetricSpecification.html): Describes a load metric for a predictive scaling policy.
- [PredictiveScalingPredefinedMetricPairSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPredefinedMetricPairSpecification.html): Represents a metric pair for a predictive scaling policy.
- [PredictiveScalingPredefinedScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPredefinedScalingMetricSpecification.html): Describes a scaling metric for a predictive scaling policy.
- [ScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalableTarget.html): Represents a scalable target.
- [ScalableTargetAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalableTargetAction.html): Represents the minimum and maximum capacity for a scheduled action.
- [ScalingActivity](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingActivity.html): Represents a scaling activity.
- [ScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingPolicy.html): Represents a scaling policy to use with Application Auto Scaling.
- [ScheduledAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScheduledAction.html): Represents a scheduled action.
- [StepAdjustment](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepAdjustment.html): Represents a step adjustment for a StepScalingPolicyConfiguration.
- [StepScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_StepScalingPolicyConfiguration.html): Represents a step scaling policy configuration to use with Application Auto Scaling.
- [SuspendedState](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_SuspendedState.html): Specifies whether the scaling activities for a scalable target are in a suspended state.
- [TargetTrackingMetric](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetric.html): Represents a specific metric.
- [TargetTrackingMetricDataQuery](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetricDataQuery.html): The metric data to return.
- [TargetTrackingMetricDimension](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetricDimension.html): Describes the dimension of a metric.
- [TargetTrackingMetricStat](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetricStat.html): This structure defines the CloudWatch metric to return, along with the statistic and unit.
- [TargetTrackingScalingPolicyConfiguration](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingScalingPolicyConfiguration.html): Represents a target tracking scaling policy configuration to use with Application Auto Scaling.
