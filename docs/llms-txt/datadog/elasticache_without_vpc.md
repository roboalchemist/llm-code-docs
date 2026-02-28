# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticache_without_vpc.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/elasticache_without_vpc.md

---
title: ElastiCache without VPC
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ElastiCache without VPC
---

# ElastiCache without VPC

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ba766c53-fe71-4bbb-be35-b6803f2ef13e`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html#cfn-elasticache-cachecluster-cachesubnetgroupname)

### Description{% #description %}

Amazon ElastiCache clusters must be launched inside a VPC to provide network isolation and reduce the risk of unintended public or cross-account access.

In CloudFormation, `AWS::ElastiCache::CacheCluster` resources must include the `CacheSubnetGroupName` property. Resources with this property missing or set to `null` will be flagged because they may be created outside a VPC.

Ensure `CacheSubnetGroupName` references an `AWS::ElastiCache::SubnetGroup` (or a valid subnet group name) that contains only VPC subnet IDs so the cluster is deployed into the intended VPC subnets.

Secure configuration example:

```yaml
MyCacheSubnetGroup:
  Type: AWS::ElastiCache::SubnetGroup
  Properties:
    Description: Subnet group for ElastiCache
    SubnetIds:
      - subnet-01234567
      - subnet-89abcdef

MyCacheCluster:
  Type: AWS::ElastiCache::CacheCluster
  Properties:
    CacheSubnetGroupName: !Ref MyCacheSubnetGroup
    Engine: redis
    CacheNodeType: cache.t3.micro
    NumCacheNodes: 1
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  ElasticacheCluster:
    Type: 'AWS::ElastiCache::CacheCluster'
    Properties:
      Engine: memcached
      CacheNodeType: cache.t2.micro
      NumCacheNodes: '1'
      CacheSubnetGroupName: default
```

```json
{
  "Resources": {
    "ElasticacheCluster": {
      "Type": "AWS::ElastiCache::CacheCluster",
      "Properties": {
          "CacheNodeType": "cache.m3.medium",
          "Engine": "memcached",
          "NumCacheNodes": "1",
          "CacheSubnetGroupName": "default"
      }
   }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "ElasticacheCluster": {
      "Type": "AWS::ElastiCache::CacheCluster",
      "Properties": {
          "CacheNodeType": "cache.m3.medium",
          "Engine": "memcached",
          "NumCacheNodes": "1"
      }
   }
  }
}
```

```yaml
Resources:
  ElasticacheCluster:
    Type: 'AWS::ElastiCache::CacheCluster'
    Properties:
      Engine: memcached
      CacheNodeType: cache.t2.micro
      NumCacheNodes: '1'
```
