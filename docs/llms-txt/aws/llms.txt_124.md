# Source: https://docs.aws.amazon.com/autoscaling/plans/APIReference/llms.txt

# AWS Auto Scaling Scaling Plans API Reference

> This API reference describes the AWS Auto Scaling APIs used to create and manage scaling plans. You can use scaling plans to configure auto scaling for related or associated scalable resources in a matter of minutes.

- [Welcome](https://docs.aws.amazon.com/autoscaling/plans/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/autoscaling/plans/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/autoscaling/plans/APIReference/CommonErrors.html)
- [Logging API Calls with CloudTrail](https://docs.aws.amazon.com/autoscaling/plans/APIReference/logging-using-cloudtrail.html)

## [Actions](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_Operations.html)

- [CreateScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CreateScalingPlan.html): Creates a scaling plan.
- [DeleteScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DeleteScalingPlan.html): Deletes the specified scaling plan.
- [DescribeScalingPlanResources](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlanResources.html): Describes the scalable resources in the specified scaling plan.
- [DescribeScalingPlans](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_DescribeScalingPlans.html): Describes one or more of your scaling plans.
- [GetScalingPlanResourceForecastData](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_GetScalingPlanResourceForecastData.html): Retrieves the forecast data for a scalable resource.
- [UpdateScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_UpdateScalingPlan.html): Updates the specified scaling plan.


## [Data Types](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_Types.html)

- [ApplicationSource](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ApplicationSource.html): Represents an application source.
- [CustomizedLoadMetricSpecification](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CustomizedLoadMetricSpecification.html): Represents a CloudWatch metric of your choosing that can be used for predictive scaling.
- [CustomizedScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_CustomizedScalingMetricSpecification.html): Represents a CloudWatch metric of your choosing for a target tracking scaling policy to use with a scaling plan.
- [Datapoint](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_Datapoint.html): Represents a single value in the forecast data used for predictive scaling.
- [MetricDimension](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_MetricDimension.html): Represents a dimension for a customized metric.
- [PredefinedLoadMetricSpecification](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_PredefinedLoadMetricSpecification.html): Represents a predefined metric that can be used for predictive scaling.
- [PredefinedScalingMetricSpecification](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_PredefinedScalingMetricSpecification.html): Represents a predefined metric that can be used for dynamic scaling as part of a target tracking scaling policy.
- [ScalingInstruction](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingInstruction.html): Describes a scaling instruction for a scalable resource in a scaling plan.
- [ScalingPlan](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPlan.html): Represents a scaling plan.
- [ScalingPlanResource](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPlanResource.html): Represents a scalable resource.
- [ScalingPolicy](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_ScalingPolicy.html): Represents a scaling policy.
- [TagFilter](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_TagFilter.html): Represents a tag.
- [TargetTrackingConfiguration](https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_TargetTrackingConfiguration.html): Describes a target tracking configuration for a scalable resource.
