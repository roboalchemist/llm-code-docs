# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/workspace_without_encryption.md

---
title: Workspace without encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Workspace without encryption
---

# Workspace without encryption

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `89827c57-5a8a-49eb-9731-976a606d70db`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Encryption

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html)

### Description{% #description %}

User volumes for Amazon WorkSpaces must be encrypted to protect sensitive user data at rest and to reduce the risk of data exposure if storage media, snapshots, or backups are compromised.

In CloudFormation, `AWS::WorkSpaces::Workspace` resources must include `Properties.UserVolumeEncryptionEnabled` set to `true`. Resources that omit this property or set it to `false` will be flagged. Ensure the property is explicitly defined as a boolean `true` in your template so encryption is enforced for user volumes.

Secure configuration example:

```yaml
MyWorkSpace:
  Type: AWS::WorkSpaces::Workspace
  Properties:
    BundleId: ws-bundle-id
    DirectoryId: d-xxxxxxxxx
    UserName: example-user
    UserVolumeEncryptionEnabled: true
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
  MyWorkSpace:
    Type: AWS::WorkSpaces::Workspace
    Properties:
      BundleId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - BundleId
      DirectoryId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - DirectoryId
      UserName: !Ref 'UserName'
      UserVolumeEncryptionEnabled: true
```

```json
{
  "Resources": {
    "MyWorkSpace2": {
      "Type": "AWS::WorkSpaces::Workspace",
      "Properties": {
        "BundleId": [
          "WSTypeMap",
          "WorkstationType",
          "BundleId"
        ],
        "DirectoryId": [
          "WSTypeMap",
          "WorkstationType",
          "DirectoryId"
        ],
        "UserName": "UserName",
        "UserVolumeEncryptionEnabled": "true"
      }
    }
  }
}
```

```yaml
Resources:
  MyWorkSpace2:
    Type: AWS::WorkSpaces::Workspace
    Properties:
      BundleId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - BundleId
      DirectoryId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - DirectoryId
      UserName: !Ref 'UserName'
      UserVolumeEncryptionEnabled: 'true'
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
Resources:
  MyWorkSpace2:
    Type: AWS::WorkSpaces::Workspace
    Properties:
      BundleId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - BundleId
      DirectoryId: !FindInMap
        - WSTypeMap
        - !Ref 'WorkstationType'
        - DirectoryId
      UserName: !Ref 'UserName'
      UserVolumeEncryptionEnabled: false
```

```json
{
  "Resources": {
    "MyWorkSpace": {
      "Type": "AWS::WorkSpaces::Workspace",
      "Properties": {
        "BundleId": [
          "WSTypeMap",
          "WorkstationType",
          "BundleId"
        ],
        "DirectoryId": [
          "WSTypeMap",
          "WorkstationType",
          "DirectoryId"
        ],
        "UserName": "UserName"
      }
    }
  }
}
```

```json
{
  "Resources": {
    "MyWorkSpace2": {
      "Type": "AWS::WorkSpaces::Workspace",
      "Properties": {
        "BundleId": [
          "WSTypeMap",
          "WorkstationType",
          "BundleId"
        ],
        "DirectoryId": [
          "WSTypeMap",
          "WorkstationType",
          "DirectoryId"
        ],
        "UserName": "UserName",
        "UserVolumeEncryptionEnabled": false
      }
    }
  }
}
```
