# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_readiness_resource_set.dataset.md

---
title: Route 53 Recovery Readiness Resource Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Readiness Resource
  Set
---

# Route 53 Recovery Readiness Resource Set

This table represents the Route 53 Recovery Readiness Resource Set resource from Amazon Web Services.

```
aws.route53_recovery_readiness_resource_set
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| resource_set_arn  | core | string     | The Amazon Resource Name (ARN) for the resource set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| resource_set_name | core | string     | The name of the resource set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| resource_set_type | core | string     | The resource type of the resources in the resource set. Enter one of the following values for resource type: AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource |
| resources         | core | json       | A list of resource objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| tags              | core | hstore_csv |
