# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/amplify_app_access_token_exposed.md

---
title: Amplify app access token exposed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > Amplify app access token exposed
---

# Amplify app access token exposed

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `73980e43-f399-4fcc-a373-658228f7adf7`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** High

**Category:** Secret Management

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html)

### Description{% #description %}

Storing an Amplify access token in plaintext or as a parameter `Default` risks accidental disclosure (for example, via source control, template exports, or build logs) and can allow unauthorized access to connected repositories or services.

This rule checks `AWS::Amplify::App` resources and the `Properties.AccessToken` value.

- The access token must not be a literal token string.
- The access token must not be supplied via a parameter `Default` containing a token-like value.

Instead, `AccessToken` should reference a secure secret (for example, an AWS Secrets Manager dynamic reference) or be supplied via a template parameter without a `Default` and with `NoEcho` set to `true` so the token is not embedded in the template.

This rule flags tokens that resemble JWTs or long token strings (for example, >`50` characters and dot-separated) when they appear inline or as parameter defaults and when there is no Secrets Manager reference.

Secure example using Secrets Manager dynamic reference:

```yaml
MySecret:
  Type: AWS::SecretsManager::Secret
  Properties:
    Name: amplify/access-token

MyApp:
  Type: AWS::Amplify::App
  Properties:
    Name: my-app
    AccessToken: '{{resolve:secretsmanager:amplify/access-token:SecretString:accessToken}}'
```

Secure example using a parameter without a Default:

```yaml
Parameters:
  AmplifyAccessToken:
    Type: String
    NoEcho: true

MyApp:
  Type: AWS::Amplify::App
  Properties:
    Name: my-app
    AccessToken: !Ref AmplifyAccessToken
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
Resources:
     NewAmpApp:
        Type: AWS::Amplify::App
        Properties:
          AccessToken: !Sub '{{resolve:secretsmanager:${MyAmpAppSecretManagerRotater}::password}}'
          BuildSpec: String
          CustomHeaders: String
          Description: String
          EnableBranchAutoDeletion: true
          IAMServiceRole: String
          Name: NewAmpApp
          OauthToken: String
          Repository: String
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
    "ParentAccessToken": {
      "Description": "Access Token",
      "Type": "String",
      "Default": ""
    }
  },
  "Resources": {
    "AmpApp": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "AccessToken": "ParentAccessToken",
        "BuildSpec": "String",
        "Repository": "String",
        "OauthToken": "String",
        "CustomHeaders": "String",
        "Description": "String",
        "EnableBranchAutoDeletion": true,
        "IAMServiceRole": "String",
        "Name": "NewAmpApp"
      }
    }
  }
}
```

```json
{
  "Parameters": {
    "ParentAccessToken": {
      "Description": "Access Token",
      "Type": "String"
    }
  },
  "Resources": {
    "NewAmp": {
      "Properties": {
        "Name": "NewAmpApp",
        "AccessToken": "ParentAccessToken",
        "BuildSpec": "String",
        "Description": "String",
        "EnableBranchAutoDeletion": true,
        "CustomHeaders": "String",
        "IAMServiceRole": "String",
        "OauthToken": "String",
        "Repository": "String"
      },
      "Type": "AWS::Amplify::App"
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ParentAccessToken:
    Description: 'Access Token'
    Type: String
    Default: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyMzkwMjJ9.tbDepxpstvGdW8TC3G8zg4B6rUYAOvfzdceoH48wgRQ'
Resources:
  AmpApp:
    Type: AWS::Amplify::App
    Properties:
      AccessToken: !Ref ParentAccessToken
      BuildSpec: String
      CustomHeaders: String
      Description: String
      EnableBranchAutoDeletion: true
      IAMServiceRole: String
      Name: NewAmpApp
      OauthToken: String
      Repository: String
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  ParentUserToken:
    Description: 'UserToken'
    Type: String
Resources:
  NewApp:
    Type: AWS::Amplify::App
    Properties:
      AccessToken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyMzkwMjJ9.tbDepxpstvGdW8TC3G8zg4B6rUYAOvfzdceoH48wgRQ
      BuildSpec: String
      CustomHeaders: String
      Description: String
      EnableBranchAutoDeletion: true
      IAMServiceRole: String
      Name: NewAmpApp
      OauthToken: String
      Repository: String
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Parameters": {
    "ParentAccessToken": {
      "Description": "Access Token",
      "Type": "String",
      "Default": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1MTYyMzkwMjJ9.tbDepxpstvGdW8TC3G8zg4B6rUYAOvfzdceoH48wgRQ"
    }
  },
  "Resources": {
    "AmpApp": {
      "Type": "AWS::Amplify::App",
      "Properties": {
        "OauthToken": "String",
        "AccessToken": "ParentAccessToken",
        "Description": "String",
        "EnableBranchAutoDeletion": true,
        "IAMServiceRole": "String",
        "BuildSpec": "String",
        "CustomHeaders": "String",
        "Name": "NewAmpApp",
        "Repository": "String"
      }
    }
  }
}
```
