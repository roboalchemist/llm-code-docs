# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/elasticache_using_default_port.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/elasticache_using_default_port.md

---
title: ElastiCache using default port
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ElastiCache using default port
---

# ElastiCache using default port

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `323db967-c68e-44e6-916c-a777f95af34b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Low

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html#cfn-elasticache-replicationgroup-port)

### Description{% #description %}

Amazon ElastiCache replication groups must not use engine default ports because default ports are easily discovered and increase the risk of automated scanning, brute-force attempts, and unauthorized access.

For `AWS::ElastiCache::ReplicationGroup` resources, ensure `Properties.Port` is not set to `6379` when `Properties.Engine` is `redis`, or to `11211` when `Properties.Engine` is `memcached`. Resources with those exact settings will be flagged.

Choose a non-default `Port` value if you require obscurity, but do not rely on port choice alone. Also restrict access with security groups, subnet/VPC controls, and parameter group settings.

Note that omitting the `Port` property typically causes the engine to use its default port. Explicitly configure a non-default port or enforce network-level restrictions to mitigate exposure.

Secure configuration example (CloudFormation YAML):

```yaml
MyReplicationGroup:
  Type: AWS::ElastiCache::ReplicationGroup
  Properties:
    Engine: redis
    Port: 6380
    ReplicationGroupId: my-redis-cluster
    ReplicationGroupDescription: "Redis cluster on non-default port"
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  BasicReplicationGroup:
    Type: 'AWS::ElastiCache::ReplicationGroup'
    Properties:
      AutomaticFailoverEnabled: true
      CacheNodeType: cache.r3.large
      CacheSubnetGroupName: !Ref CacheSubnetGroup
      Engine: redis
      EngineVersion: '3.2'
      NumNodeGroups: '2'
      ReplicasPerNodeGroup: '3'
      Port: 6380
      PreferredMaintenanceWindow: 'sun:05:00-sun:09:00'
      ReplicationGroupDescription: A sample replication group
      SecurityGroupIds:
        - !Ref ReplicationGroupSG
      SnapshotRetentionLimit: 5
      SnapshotWindow: '10:00-12:00'
```

```json
{
  "Resources": {
    "BasicReplicationGroup": {
      "Type": "AWS::ElastiCache::ReplicationGroup",
      "Properties": {
          "AutomaticFailoverEnabled": true,
          "CacheNodeType": "cache.r3.large",
          "CacheSubnetGroupName": {
              "Ref": "CacheSubnetGroup"
          },
          "Engine": "memcached",
          "EngineVersion": "3.2",
          "NumNodeGroups": "2",
          "ReplicasPerNodeGroup": "3",
          "Port": 11212,
          "PreferredMaintenanceWindow": "sun:05:00-sun:09:00",
          "ReplicationGroupDescription": "A sample replication group",
          "SecurityGroupIds": [
              {
                  "Ref": "ReplicationGroupSG"
              }
          ],
          "SnapshotRetentionLimit": 5,
          "SnapshotWindow": "10:00-12:00"
      }
    }
  }
}
```

```yaml
Resources:
  BasicReplicationGroup:
    Type: 'AWS::ElastiCache::ReplicationGroup'
    Properties:
      AutomaticFailoverEnabled: true
      CacheNodeType: cache.r3.large
      CacheSubnetGroupName: !Ref CacheSubnetGroup
      Engine: memcached
      EngineVersion: '3.2'
      NumNodeGroups: '2'
      ReplicasPerNodeGroup: '3'
      Port: 11212
      PreferredMaintenanceWindow: 'sun:05:00-sun:09:00'
      ReplicationGroupDescription: A sample replication group
      SecurityGroupIds:
        - !Ref ReplicationGroupSG
      SnapshotRetentionLimit: 5
      SnapshotWindow: '10:00-12:00'
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  BasicReplicationGroup:
    Type: 'AWS::ElastiCache::ReplicationGroup'
    Properties:
      AutomaticFailoverEnabled: true
      CacheNodeType: cache.r3.large
      CacheSubnetGroupName: !Ref CacheSubnetGroup
      Engine: memcached
      EngineVersion: '3.2'
      NumNodeGroups: '2'
      ReplicasPerNodeGroup: '3'
      Port: 11211
      PreferredMaintenanceWindow: 'sun:05:00-sun:09:00'
      ReplicationGroupDescription: A sample replication group
      SecurityGroupIds:
        - !Ref ReplicationGroupSG
      SnapshotRetentionLimit: 5
      SnapshotWindow: '10:00-12:00'
```

```json
{
  "Resources": {
    "BasicReplicationGroup": {
      "Type": "AWS::ElastiCache::ReplicationGroup",
      "Properties": {
          "AutomaticFailoverEnabled": true,
          "CacheNodeType": "cache.r3.large",
          "CacheSubnetGroupName": {
              "Ref": "CacheSubnetGroup"
          },
          "Engine": "redis",
          "EngineVersion": "3.2",
          "NumNodeGroups": "2",
          "ReplicasPerNodeGroup": "3",
          "Port": 6379,
          "PreferredMaintenanceWindow": "sun:05:00-sun:09:00",
          "ReplicationGroupDescription": "A sample replication group",
          "SecurityGroupIds": [
              {
                  "Ref": "ReplicationGroupSG"
              }
          ],
          "SnapshotRetentionLimit": 5,
          "SnapshotWindow": "10:00-12:00"
      }
    }
  }
}
```

```json
{
  "Resources": {
    "BasicReplicationGroup": {
      "Type": "AWS::ElastiCache::ReplicationGroup",
      "Properties": {
          "AutomaticFailoverEnabled": true,
          "CacheNodeType": "cache.r3.large",
          "CacheSubnetGroupName": {
              "Ref": "CacheSubnetGroup"
          },
          "Engine": "memcached",
          "EngineVersion": "3.2",
          "NumNodeGroups": "2",
          "ReplicasPerNodeGroup": "3",
          "Port": 11211,
          "PreferredMaintenanceWindow": "sun:05:00-sun:09:00",
          "ReplicationGroupDescription": "A sample replication group",
          "SecurityGroupIds": [
              {
                  "Ref": "ReplicationGroupSG"
              }
          ],
          "SnapshotRetentionLimit": 5,
          "SnapshotWindow": "10:00-12:00"
      }
    }
  }
}
```
