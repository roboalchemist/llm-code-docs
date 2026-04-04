# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/elb_access_log_disabled.md

---
title: ELB access log disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ELB access log disabled
---

# ELB access log disabled

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `ee12ad32-2863-4c0f-b13f-28272d115028`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Observability

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html)

### Description{% #description %}

Elastic Load Balancers must have access logging enabled so request logs are retained for incident investigation and auditing. Without logs, you cannot reconstruct traffic patterns or investigate unauthorized access.

For CloudFormation, the `AWS::ElasticLoadBalancing::LoadBalancer` resource must include the `AccessLoggingPolicy` property and its `Enabled` attribute must be set to `true`. Resources missing `AccessLoggingPolicy` or with `AccessLoggingPolicy.Enabled` set to `false` will be flagged.

Secure CloudFormation example:

```yaml
MyLoadBalancer:
  Type: AWS::ElasticLoadBalancing::LoadBalancer
  Properties:
    AccessLoggingPolicy:
      Enabled: true
      S3BucketName: my-elb-logs-bucket
      S3BucketPrefix: elb-logs/
      EmitInterval: 60
```

Ensure the target S3 bucket exists and allows the load balancer to write logs.

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A simple EC2 instance
Resources:
  MyLoadBalancer:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - "us-east-2a"
      CrossZone: true
      Listeners:
        - InstancePort: "80"
          InstanceProtocol: HTTP
          LoadBalancerPort: "443"
          Protocol: HTTPS
          PolicyNames:
            - My-SSLNegotiation-Policy
          SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
      HealthCheck:
        Target: HTTP:80/
        HealthyThreshold: "2"
        UnhealthyThreshold: "3"
        Interval: "10"
        Timeout: "5"
      Policies:
        - PolicyName: My-SSLNegotiation-Policy
          PolicyType: SSLNegotiationPolicyType
          Attributes:
            - Name: Reference-Security-Policy
              Value: ELBSecurityPolicy-TLS-1-2-2017-01
      AccessLoggingPolicy:
        - Enabled: true
          S3BucketName: teste
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A simple EC2 instance",
  "Resources": {
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "Policies": [
          {
            "PolicyName": "My-SSLNegotiation-Policy",
            "PolicyType": "SSLNegotiationPolicyType",
            "Attributes": [
              {
                "Name": "Reference-Security-Policy",
                "Value": "ELBSecurityPolicy-TLS-1-2-2017-01"
              }
            ]
          }
        ],
        "AccessLoggingPolicy": [
          {
            "Enabled": true,
            "S3BucketName": "teste"
          }
        ],
        "AvailabilityZones": [
          "us-east-2a"
        ],
        "CrossZone": true,
        "Listeners": [
          {
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate",
            "InstancePort": "80",
            "InstanceProtocol": "HTTP"
          }
        ],
        "HealthCheck": {
          "Timeout": "5",
          "Target": "HTTP:80/",
          "HealthyThreshold": "2",
          "UnhealthyThreshold": "3",
          "Interval": "10"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: A simple EC2 instance
Resources:
  MyLoadBalancer2:
    Type: AWS::ElasticLoadBalancing::LoadBalancer
    Properties:
      AvailabilityZones:
        - "us-east-2a"
      CrossZone: true
      Listeners:
        - InstancePort: "80"
          InstanceProtocol: HTTP
          LoadBalancerPort: "443"
          Protocol: HTTPS
          PolicyNames:
            - My-SSLNegotiation-Policy
          SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
      HealthCheck:
        Target: HTTP:80/
        HealthyThreshold: "2"
        UnhealthyThreshold: "3"
        Interval: "10"
        Timeout: "5"
      Policies:
        - PolicyName: My-SSLNegotiation-Policy
          PolicyType: SSLNegotiationPolicyType
          Attributes:
            - Name: Reference-Security-Policy
              Value: ELBSecurityPolicy-TLS-1-2-2017-01
      AccessLoggingPolicy:
        Enabled: false
        S3BucketName: teste
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A simple EC2 instance",
  "Resources": {
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "AvailabilityZones": [
          "us-east-2a"
        ],
        "CrossZone": true,
        "Listeners": [
          {
            "InstancePort": "80",
            "InstanceProtocol": "HTTP",
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate"
          }
        ],
        "HealthCheck": {
          "Target": "HTTP:80/",
          "HealthyThreshold": "2",
          "UnhealthyThreshold": "3",
          "Interval": "10",
          "Timeout": "5"
        },
        "Policies": [
          {
            "PolicyName": "My-SSLNegotiation-Policy",
            "PolicyType": "SSLNegotiationPolicyType",
            "Attributes": [
              {
                "Name": "Reference-Security-Policy",
                "Value": "ELBSecurityPolicy-TLS-1-2-2017-01"
              }
            ]
          }
        ]
      }
    }
  }
}
```

```json
{
  "Resources": {
    "MyLoadBalancer2": {
      "Properties": {
        "Policies": [
          {
            "PolicyType": "SSLNegotiationPolicyType",
            "Attributes": [
              {
                "Name": "Reference-Security-Policy",
                "Value": "ELBSecurityPolicy-TLS-1-2-2017-01"
              }
            ],
            "PolicyName": "My-SSLNegotiation-Policy"
          }
        ],
        "AccessLoggingPolicy": {
          "Enabled": false,
          "S3BucketName": "teste"
        },
        "AvailabilityZones": [
          "us-east-2a"
        ],
        "CrossZone": true,
        "Listeners": [
          {
            "InstancePort": "80",
            "InstanceProtocol": "HTTP",
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate"
          }
        ],
        "HealthCheck": {
          "Interval": "10",
          "Timeout": "5",
          "Target": "HTTP:80/",
          "HealthyThreshold": "2",
          "UnhealthyThreshold": "3"
        }
      },
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer"
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "A simple EC2 instance"
}
```
