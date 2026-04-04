# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/alb_is_not_integrated_with_waf.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/alb_is_not_integrated_with_waf.md

---
title: ALB is not integrated with WAF
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ALB is not integrated with WAF
---

# ALB is not integrated with WAF

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `105ba098-1e34-48cd-b0f2-a8a43a51bf9b`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html)

### Description{% #description %}

Externally accessible Application Load Balancers must be protected by a web application firewall (WAF) to block common web attacks such as SQL injection, cross-site scripting, and HTTP-layer abuse that can lead to data exposure or service disruption. Check `AWS::ElasticLoadBalancingV2::LoadBalancer` resources where `Properties.Scheme` is not `internal` and ensure there is an `AWS::WAFRegional::WebACLAssociation` that associates a web ACL with the load balancer by setting `Properties.ResourceArn` to the load balancer ARN. Resources missing a corresponding `AWS::WAFRegional::WebACLAssociation` where `ResourceArn` references the load balancer will be flagged.

Secure CloudFormation example using the ALB ARN:

```yaml
MyLoadBalancer:
  Type: AWS::ElasticLoadBalancingV2::LoadBalancer
  Properties:
    Name: my-alb
    Scheme: internet-facing
    # other ALB properties...

MyWebACLAssociation:
  Type: AWS::WAFRegional::WebACLAssociation
  Properties:
    ResourceArn: !GetAtt MyLoadBalancer.LoadBalancerArn
    WebACLId: !Ref MyWebACL
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    MyLoadBalancer9:
        Type: AWS::ElasticLoadBalancing::LoadBalancer
        Properties:
          AvailabilityZones:
          - "us-east-2a"
          CrossZone: true
          Listeners:
          - InstancePort: '80'
            InstanceProtocol: HTTP
            LoadBalancerPort: '443'
            Protocol: HTTPS
            PolicyNames:
            - My-SSLNegotiation-Policy
            SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
          Scheme: internet-facing
    MyWebACLAssociation:
      Type: "AWS::WAFRegional::WebACLAssociation"
      Properties:
        ResourceArn:
          Ref: MyLoadBalancer9
        WebACLId:
          Ref: MyWebACL
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyLoadBalancer8": {
      "Properties": {
        "Listeners": [
          {
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate",
            "InstancePort": "80",
            "InstanceProtocol": "HTTP",
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS"
          }
        ],
        "Scheme": "internet-facing",
        "AvailabilityZones": [
          "us-east-2a"
        ],
        "CrossZone": true
      },
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer"
    },
    "MyWebACLAssociation": {
      "Type": "AWS::WAFRegional::WebACLAssociation",
      "Properties": {
        "WebACLId": {
          "Ref": "MyWebACL"
        },
        "ResourceArn": {
          "Ref": "MyLoadBalancer8"
        }
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyLoadBalancerV2:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Name: myloadbalancerv2
      Scheme: internet-facing
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyLoadBalancer22222222": {
      "Properties": {
        "Listeners": [
          {
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate",
            "InstancePort": "80",
            "InstanceProtocol": "HTTP",
            "LoadBalancerPort": "443",
            "Protocol": "HTTPS",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ]
          }
        ],
        "Scheme": "internet-facing",
        "AvailabilityZones": [
          "us-east-2a"
        ],
        "CrossZone": true
      },
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer"
    }
  }
}
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyLoadBalancerV22222": {
      "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
      "Properties": {
        "Scheme": "internet-facing",
        "Name": "myloadbalancerv2"
      }
    }
  }
}
```
