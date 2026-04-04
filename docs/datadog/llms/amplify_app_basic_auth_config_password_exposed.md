# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/amplify_app_basic_auth_config_password_exposed.md

---
title: Amplify app basic auth config password exposed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Amplify app basic auth config password exposed
---

# Amplify app basic auth config password exposed

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `71493c8b-3014-404c-9802-078b74496fb7`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amplify-app-basicauthconfig.html)

### Description{% #description %}

Amplify apps with BasicAuth enabled must not embed the password as a plaintext string or as a parameter `Default` because embedded secrets in templates or defaults can be exposed via source control, CloudFormation templates/stack history, or the AWS Console and enable unauthorized access.

This rule checks resources of type `AWS::Amplify::App` where `Properties.BasicAuthConfig.EnableBasicAuth` is set to `true`.

- `Resources.<name>.Properties.BasicAuthConfig.Password` must not be a literal string.
- `Resources.<name>.Properties.BasicAuthConfig.Password` must not be a `Ref` to a parameter whose `Parameters.<param>.Default` contains the secret.

Instead, store the credential in a secrets service and reference it from the template (or supply the value at deploy time without a `Default`). Templates that reference AWS Secrets Manager for the password or omit embedded/default secrets will satisfy this requirement.

Secure example using AWS Secrets Manager dynamic reference:

```yaml
MySecret:
  Type: AWS::SecretsManager::Secret
  Properties:
    Name: my-amplify-basic-auth
    SecretString: '{"password":"REPLACE_WITH_SECURE_VALUE"}'

MyAmplifyApp:
  Type: AWS::Amplify::App
  Properties:
    BasicAuthConfig:
      EnableBasicAuth: true
      Username: admin
      Password: '{{resolve:secretsmanager:my-amplify-basic-auth:SecretString:password}}'
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
     NewAmpApp-2:
        Type: AWS::Amplify::App
        Properties:
          BuildSpec: String
          CustomHeaders: String
          Description: String
          EnableBranchAutoDeletion: true
          IAMServiceRole: String
          Name: NewAmpApp
          OauthToken: String
          Repository: String
          BasicAuthConfig :
            EnableBasicAuth: true
            Password: !Sub '{{resolve:secretsmanager:${MyAmpAppSecretManagerRotater}::password}}'
            Username: !Sub '{{resolve:secretsmanager:${MyAmpAppSecretManagerRotater}::username}}'
     MyAmpAppSecretManagerRotater:
        Type: AWS::SecretsManager::Secret
        Properties:
          Description: 'This is my amp app instance secret'
          GenerateSecretString:
            SecretStringTemplate: '{"username": "admin"}'
            GenerateStringKey: 'password'
            PasswordLength: 16
            ExcludeCharacters: '"@/\'
```

```json
{
  "Parameters": {
    "ParentPassword": {
      "Description": "Password",
      "Type": "String",
      "Default": ""
    },
    "ParentUsername": {
      "Description": "Username",
      "Type": "String",
      "Default": ""
    }
  },
  "Resources": {
    "NewAmpApp-4": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "BuildSpec": "String",
        "Description": "String",
        "EnableBranchAutoDeletion": true,
        "Repository": "String",
        "BasicAuthConfig": {
          "EnableBasicAuth": true,
          "Password": "ParentPassword",
          "Username": "ParentUsername"
        },
        "CustomHeaders": "String",
        "IAMServiceRole": "String",
        "Name": "NewAmpApp",
        "OauthToken": "String"
      }
    }
  }
}
```

```json
{
  "Resources": {
    "NewAmpApp-1": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "BasicAuthConfig": {
          "EnableBasicAuth": true,
          "Password": "ParentPassword",
          "Username": "ParentUsername"
        },
        "BuildSpec": "String",
        "Name": "NewAmpApp",
        "OauthToken": "String",
        "Repository": "String",
        "CustomHeaders": "String",
        "Description": "String",
        "EnableBranchAutoDeletion": true,
        "IAMServiceRole": "String"
      }
    }
  },
  "Parameters": {
    "ParentPassword": {
      "Description": "Password",
      "Type": "String"
    },
    "ParentUsername": {
      "Description": "Username",
      "Type": "String"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ParentPassword:
    Description: 'Password'
    Type: String
    Default: "@skdsjdk0234!AB"
  ParentUsername:
    Description: 'Username'
    Type: String
    Default: ""
Resources:
  NewAmpApp-4:
    Type: AWS::Amplify::App
    Properties:
      BuildSpec: String
      CustomHeaders: String
      Description: String
      EnableBranchAutoDeletion: true
      IAMServiceRole: String
      Name: NewAmpApp
      OauthToken: String
      Repository: String
      BasicAuthConfig:
        EnableBasicAuth: true
        Password: !Ref ParentPassword
        Username: !Ref ParentUsername
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "NewAmpApp-1": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "OauthToken": "String",
        "Repository": "String",
        "BasicAuthConfig": {
          "Username": "admin",
          "EnableBasicAuth": true,
          "Password": "@skdsjdk0234!AB"
        },
        "CustomHeaders": "String",
        "Description": "String",
        "Name": "NewAmpApp",
        "BuildSpec": "String",
        "EnableBranchAutoDeletion": true,
        "IAMServiceRole": "String"
      }
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Parameters": {
    "ParentUsername": {
      "Description": "Username",
      "Type": "String",
      "Default": ""
    },
    "ParentPassword": {
      "Description": "Password",
      "Type": "String",
      "Default": "@skdsjdk0234!AB"
    }
  },
  "Resources": {
    "NewAmpApp-4": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "CustomHeaders": "String",
        "EnableBranchAutoDeletion": true,
        "IAMServiceRole": "String",
        "OauthToken": "String",
        "Repository": "String",
        "BuildSpec": "String",
        "Description": "String",
        "Name": "NewAmpApp",
        "BasicAuthConfig": {
          "Password": "ParentPassword",
          "Username": "ParentUsername",
          "EnableBasicAuth": true
        }
      }
    }
  }
}
```
