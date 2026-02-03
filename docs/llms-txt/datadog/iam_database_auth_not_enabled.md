# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/iam_database_auth_not_enabled.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/iam_database_auth_not_enabled.md

---
title: IAM database auth not enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > IAM database auth not enabled
---

# IAM database auth not enabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `9fcd0a0a-9b6f-4670-a215-d94e6bf3f184`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html#cfn-rds-dbinstance-enableiamdatabaseauthentication)

### Description{% #description %}

Amazon RDS instances should have IAM database authentication enabled for engines and versions that support it to avoid embedding longâlived database credentials in application code or configuration and to enable centralized credential management and rotation.

For CloudFormation, the `EnableIAMDatabaseAuthentication` property on `AWS::RDS::DBInstance` must be defined and set to `true` when the template's `Engine`, `EngineVersion`, and `DBInstanceClass` indicate IAM authentication compatibility. Resources missing `EnableIAMDatabaseAuthentication` or with `EnableIAMDatabaseAuthentication` set to `false` will be flagged.

Secure configuration example:

```yaml
MyDBInstance:
  Type: AWS::RDS::DBInstance
  Properties:
    Engine: mysql
    EngineVersion: "8.0"
    DBInstanceClass: db.t3.medium
    EnableIAMDatabaseAuthentication: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: RDS Storage Encrypted
Parameters:
  SourceDBInstanceIdentifier:
    Type: String
  DBInstanceType:
    Type: String
  SourceRegion:
    Type: String
Resources:
  MyDBSmall:
    Type: "AWS::RDS::DBInstance"
    Properties:
      DBInstanceClass: !Ref DBInstanceType
      SourceDBInstanceIdentifier: !Ref SourceDBInstanceIdentifier
      SourceRegion: !Ref SourceRegion
      DeletionProtection: false
      KmsKeyId: !Ref MyKey
      EnableIAMDatabaseAuthentication: true
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: RDS Storage Encrypted
Parameters:
  SourceDBInstanceIdentifier:
    Type: String
  DBInstanceType:
    Type: String
  SourceRegion:
    Type: String
Resources:
  MyDBSmall:
    Type: "AWS::RDS::DBInstance"
    Properties:
      DBInstanceClass: db.t2.small
      SourceDBInstanceIdentifier: !Ref SourceDBInstanceIdentifier
      SourceRegion: !Ref SourceRegion
      DeletionProtection: false
      KmsKeyId: !Ref MyKey
      EnableIAMDatabaseAuthentication: false
      Engine: mariadb
      EngineVersion: 10.2.43
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "RDS Storage Encrypted",
  "Parameters": {
      "SourceDBInstanceIdentifier": {
          "Type": "String"
      },
      "DBInstanceType": {
          "Type": "String"
      },
      "SourceRegion": {
          "Type": "String"
      }
  },
  "Resources": {
      "MyDBSmall": {
          "Type": "AWS::RDS::DBInstance",
          "Properties": {
              "DBInstanceClass": {
                  "Ref": "DBInstanceType"
              },
              "SourceDBInstanceIdentifier": {
                  "Ref": "SourceDBInstanceIdentifier"
              },
              "SourceRegion": {
                  "Ref": "SourceRegion"
              },
              "KmsKeyId": {
                  "Ref": "MyKey"
              },
              "EnableIAMDatabaseAuthentication" : true
          }
      }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "RDS Storage Encrypted",
  "Parameters": {
    "SourceDBInstanceIdentifier": {
      "Type": "String"
    },
    "DBInstanceType": {
      "Type": "String"
    },
    "SourceRegion": {
      "Type": "String"
    }
  },
  "Resources": {
    "MyDBSmall": {
      "Type": "AWS::RDS::DBInstance",
      "Properties": {
        "DBInstanceClass": {
          "Ref": "DBInstanceType"
        },
        "SourceDBInstanceIdentifier": {
          "Ref": "SourceDBInstanceIdentifier"
        },
        "SourceRegion": {
          "Ref": "SourceRegion"
        },
        "KmsKeyId": {
          "Ref": "MyKey"
        },
        "EnableIAMDatabaseAuthentication": false,
        "Engine": "mysql"
      }
    }
  }
}
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: RDS Storage Encrypted
Parameters:
  SourceDBInstanceIdentifier:
    Type: String
  DBInstanceType:
    Type: String
  SourceRegion:
    Type: String
Resources:
  MyDBSmall:
    Type: "AWS::RDS::DBInstance"
    Properties:
      DBInstanceClass: db.r3.xlarge
      SourceDBInstanceIdentifier: !Ref SourceDBInstanceIdentifier
      SourceRegion: !Ref SourceRegion
      DeletionProtection: false
      KmsKeyId: !Ref MyKey
      Engine: mysql
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "RDS Storage Encrypted",
  "Parameters": {
    "SourceDBInstanceIdentifier": {
      "Type": "String"
    },
    "DBInstanceType": {
      "Type": "String"
    },
    "SourceRegion": {
      "Type": "String"
    }
  },
  "Resources": {
    "MyDBSmall": {
      "Type": "AWS::RDS::DBInstance",
      "Properties": {
        "DBInstanceClass": {
          "Ref": "DBInstanceType"
        },
        "SourceDBInstanceIdentifier": {
          "Ref": "SourceDBInstanceIdentifier"
        },
        "SourceRegion": {
          "Ref": "SourceRegion"
        },
        "KmsKeyId": {
          "Ref": "MyKey"
        },
        "Engine": "mysql"
      }
    }
  }
}
```
