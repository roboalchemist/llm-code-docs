# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/aws/alb_listening_on_http.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/terraform/alicloud/alb_listening_on_http.md

# Source: https://docs.datadoghq.com/security/code_security/iac_security/iac_rules/cloudformation/aws/alb_listening_on_http.md

---
title: ALB listening on HTTP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Infrastructure as Code (IaC)
  Security > IaC Security Rules > ALB listening on HTTP
---

# ALB listening on HTTP

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**Id:** `275a3217-ca37-40c1-a6cf-bb57d245ab32`

**Cloud Provider:** AWS

**Platform:** CloudFormation

**Severity:** Medium

**Category:** Networking and Firewall

#### Learn More{% #learn-more %}

- [Provider Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-protocol)

### Description{% #description %}

Listeners must not use plain HTTP because unencrypted traffic can be intercepted or modified in transit, exposing sensitive data and enabling session hijacking or credential theft.

For `AWS::ElasticLoadBalancing::LoadBalancer` resources, ensure no entry in `Properties.Listeners` has `Protocol` set to `HTTP`. Listeners should use `HTTPS` and include an SSL certificate (`SSLCertificateId`).

For `AWS::ElasticLoadBalancingV2::Listener` resources, ensure `Properties.Protocol` is not `HTTP`. Listeners should use `HTTPS` with a `Certificates` entry and an appropriate `SslPolicy`.

Resources with listeners configured as `HTTP` will be flagged. When migrating to HTTPS, also ensure backend/target group protocols and health checks are updated and a valid certificate ARN is provided.

Secure configuration examples:

```yaml
MyClassicLoadBalancer:
  Type: AWS::ElasticLoadBalancing::LoadBalancer
  Properties:
    Listeners:
      - Protocol: HTTPS
        LoadBalancerPort: 443
        InstanceProtocol: HTTPS
        InstancePort: 443
        SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-cert
```

```yaml
MyALBListener:
  Type: AWS::ElasticLoadBalancingV2::Listener
  Properties:
    Protocol: HTTPS
    Port: 443
    Certificates:
      - CertificateArn: arn:aws:acm:us-east-1:123456789012:certificate/abcd-ef01-2345
    DefaultActions:
      - Type: forward
        TargetGroupArn: !Ref MyTargetGroup
    SslPolicy: ELBSecurityPolicy-2016-08
```

## Compliant Code Examples{% #compliant-code-examples %}

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    MyLoadBalancer:
        Type: AWS::ElasticLoadBalancing::LoadBalancer
        Properties:
          AvailabilityZones:
          - "us-east-2a"
          CrossZone: true
          Listeners:
          - InstancePort: '80'
            InstanceProtocol: HTTPS
            LoadBalancerPort: '443'
            Protocol: HTTPS
            PolicyNames:
            - My-SSLNegotiation-Policy
            SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
          Scheme: internal
```

```json
{
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z",
  "Resources": {
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "CrossZone": true,
        "Listeners": [
          {
            "Protocol": "HTTPS",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate",
            "InstancePort": "80",
            "InstanceProtocol": "HTTPS",
            "LoadBalancerPort": "443"
          }
        ],
        "Scheme": "internal",
        "AvailabilityZones": [
          "us-east-2a"
        ]
      }
    }
  }
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```json
{
  "Resources": {
    "MyLoadBalancer": {
      "Type": "AWS::ElasticLoadBalancing::LoadBalancer",
      "Properties": {
        "CrossZone": true,
        "Listeners": [
          {
            "Protocol": "HTTP",
            "PolicyNames": [
              "My-SSLNegotiation-Policy"
            ],
            "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-certificate",
            "InstancePort": "80",
            "InstanceProtocol": "HTTPS",
            "LoadBalancerPort": "443"
          }
        ],
        "Scheme": "internal",
        "AvailabilityZones": [
          "us-east-2a"
        ]
      }
    },
    "HTTPlistener": {
      "Type": "AWS::ElasticLoadBalancingV2::Listener",
      "Properties": {
        "DefaultActions": [
          {
            "Type": "redirect"
          }
        ],
        "LoadBalancerArn": "myLoadBalancer",
        "Port": 80,
        "Protocol": "HTTP"
      }
    }
  },
  "AWSTemplateFormatVersion": "2010-09-09T00:00:00Z"
}
```

```yaml
Resources:
  HTTPlistener:
   Type: "AWS::ElasticLoadBalancingV2::Listener"
   Properties:
     DefaultActions:
       - Type: "redirect"
         RedirectConfig:
           Protocol: "HTTPS"
           Port: "443"
           Host: "#{host}"
           Path: "/#{path}"
           Query: "#{query}"
           StatusCode: "HTTP_301"
     LoadBalancerArn: !Ref myLoadBalancer
     Port: 80
     Protocol: "HTTP"
```

```yaml
AWSTemplateFormatVersion: 2010-09-09
Resources:
    MyLoadBalancer:
        Type: AWS::ElasticLoadBalancing::LoadBalancer
        Properties:
          AvailabilityZones:
          - "us-east-2a"
          CrossZone: true
          Listeners:
          - InstancePort: '80'
            InstanceProtocol: HTTPS
            LoadBalancerPort: '443'
            Protocol: HTTP
            PolicyNames:
            - My-SSLNegotiation-Policy
            SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
          - InstancePort: '80'
            InstanceProtocol: HTTPS
            LoadBalancerPort: '22'
            Protocol: HTTP
            PolicyNames:
            - My-SSLNegotiation-Policy
            SSLCertificateId: arn:aws:iam::123456789012:server-certificate/my-server-certificate
          Scheme: internal
    HTTPlistener:
        Type: "AWS::ElasticLoadBalancingV2::Listener"
        Properties:
            DefaultActions:
            - Type: redirect
            LoadBalancerArn: !Ref myLoadBalancer
            Port: 80
            Protocol: HTTP
```
