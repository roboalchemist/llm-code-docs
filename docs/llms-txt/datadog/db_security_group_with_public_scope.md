# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/db_security_group_with_public_scope.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/db_security_group_with_public_scope.md

---
title: DB security group with public scope
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > DB security group with public scope
---

# DB security group with public scope

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9564406d-e761-4e61-b8d7-5926e3ab8e79`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Critical

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html)

### Description{% #description %}

Databases and their associated security groups must not allow ingress from the entire internet. When a publicly accessible Amazon RDS instance allows `CidrIp` set to `0.0.0.0/0` or `CidrIpv6` set to `::/0`, it exposes the database to unauthorized access, brute-force attacks, and data exfiltration.

This rule applies when an `AWS::RDS::DBInstance` has `Properties.PubliclyAccessible` set to `true`. It flags:

- `AWS::EC2::SecurityGroup` resources with `Properties.SecurityGroupIngress` entries where `CidrIp` is `0.0.0.0/0` or `CidrIpv6` is `::/0`.
- `AWS::RDS::DBSecurityGroup` resources with `Properties.DBSecurityGroupIngress[]` entries where `CIDRIP` is `0.0.0.0/0`.

Resources matching these values will be flagged. Instead, restrict ingress to specific trusted CIDR ranges or reference other security group IDs as the source so only known hosts can connect.

Secure examples (restrict to a trusted CIDR or a security group):

```yaml
MySecurityGroup:
  Type: AWS::EC2::SecurityGroup
  Properties:
    GroupDescription: "Allow DB access from trusted network"
    SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 5432
        ToPort: 5432
        CidrIp: 203.0.113.0/24
```

```yaml
MyDBSecurityGroup:
  Type: AWS::RDS::DBSecurityGroup
  Properties:
    DBSecurityGroupIngress:
      - CIDRIP: 203.0.113.5/32
    DBSecurityGroupName: my-db-sg
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
#this code is a correct code for which the query should not find any result
Resources:
  DBEC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Open database for access
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 1.2.3.4/24
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIpv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
      SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
  DBInstance:
    Type: AWS::RDS::DBInstance
    Properties:
      PubliclyAccessible: true
      DBName:
        Ref: DBName
      Engine: MySQL
      MultiAZ:
        Ref: MultiAZDatabase
      MasterUsername:
        Ref: DBUser
      DBInstanceClass:
        Ref: DBClass
      AllocatedStorage:
        Ref: DBAllocatedStorage
      MasterUserPassword:
        Ref: DBPassword
      VPCSecurityGroups:
      - !GetAtt DBEC2SecurityGroup.GroupId
```

```json
{
  "Resources": {
    "DBinstance": {
      "Type": "AWS::RDS::DBInstance",
      "Properties": {
        "AllocatedStorage": "5",
        "DBInstanceClass": "db.t3.small",
        "Engine": "MySQL",
        "MasterUsername": "YourName",
        "MasterUserPassword": "YourPassword",
        "PubliclyAccessible": true,
        "DBSecurityGroups": [
          {
            "Ref": "DbSecurityByEC2SecurityGroup"
          }
        ]
      },
      "DeletionPolicy": "Snapshot"
    },
    "DbSecurityByEC2SecurityGroup": {
      "Type": "AWS::RDS::DBSecurityGroup",
      "Properties": {
        "GroupDescription": "Ingress for Amazon EC2 security group",
        "DBSecurityGroupIngress": [
          {
            "CIDRIP": "1.2.3.4/24"
          }
        ]
      }
    }
  }
}
```

```yaml
Resources:
  DBinstance:
    Type: AWS::RDS::DBInstance
    Properties:
      PubliclyAccessible: true
      DBSecurityGroups:
        -
          Ref: "DbSecurityByEC2SecurityGroup"
      AllocatedStorage: "5"
      DBInstanceClass: "db.t3.small"
      Engine: "MySQL"
      MasterUsername: "YourName"
      MasterUserPassword: "YourPassword"
    DeletionPolicy: "Snapshot"
  DbSecurityByEC2SecurityGroup:
    Type: AWS::RDS::DBSecurityGroup
    Properties:
      GroupDescription: "Ingress for Amazon EC2 security group"
      DBSecurityGroupIngress:
        -
          CIDRIP: 1.2.3.4/24
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  DBinstance2:
    Type: AWS::RDS::DBInstance
    Properties:
      PubliclyAccessible: true
      DBSecurityGroups:
        -
          Ref: "DbSecurityByEC2SecurityGroup"
      AllocatedStorage: "5"
      DBInstanceClass: "db.t3.small"
      Engine: "MySQL"
      MasterUsername: "YourName"
      MasterUserPassword: "YourPassword"
    DeletionPolicy: "Snapshot"
  DbSecurityByEC2SecurityGroup:
    Type: AWS::RDS::DBSecurityGroup
    Properties:
      GroupDescription: "Ingress for Amazon EC2 security group"
      DBSecurityGroupIngress:
        -
          CIDRIP: 0.0.0.0/0
```

```yaml
Resources:
  DBEC2SecurityGroup2:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Open database for access
      SecurityGroupIngress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIpv6: ::/0
      SecurityGroupEgress:
      - IpProtocol: tcp
        FromPort: 80
        ToPort: 80
        CidrIp: 0.0.0.0/0
  DBInstance3:
    Type: AWS::RDS::DBInstance
    Properties:
      PubliclyAccessible: true
      DBName:
        Ref: DBName
      Engine: MySQL
      MultiAZ:
        Ref: MultiAZDatabase
      MasterUsername:
        Ref: DBUser
      DBInstanceClass:
        Ref: DBClass
      AllocatedStorage:
        Ref: DBAllocatedStorage
      MasterUserPassword:
        Ref: DBPassword
      VPCSecurityGroups:
      - !GetAtt DBEC2SecurityGroup2.GroupId
```

```json
{
  "Resources": {
    "DBinstance2": {
      "Type": "AWS::RDS::DBInstance",
      "Properties": {
        "PubliclyAccessible": true,
        "DBSecurityGroups": [
          {
            "Ref": "DbSecurityByEC2SecurityGroup"
          }
        ],
        "AllocatedStorage": "5",
        "DBInstanceClass": "db.t3.small",
        "Engine": "MySQL",
        "MasterUsername": "YourName",
        "MasterUserPassword": "YourPassword"
      },
      "DeletionPolicy": "Snapshot"
    },
    "DbSecurityByEC2SecurityGroup": {
      "Type": "AWS::RDS::DBSecurityGroup",
      "Properties": {
        "GroupDescription": "Ingress for Amazon EC2 security group",
        "DBSecurityGroupIngress": [
          {
            "CIDRIP": "0.0.0.0/0"
          }
        ]
      }
    }
  }
}
```
