# Source: https://docs.datadoghq.com/security/default_rules/7cf-b7e-cc9.md

---
title: CloudFront distribution should be integrated with WAF
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > CloudFront distribution should be
  integrated with WAF
---

# CloudFront distribution should be integrated with WAF
 
## Description{% #description %}

Verify that your [AWS CloudFront](https://aws.amazon.com/cloudfront/) distributions are integrated with [AWS Web Application Firewall](https://aws.amazon.com/waf/) (AWS WAF).

## Rationale{% #rationale %}

AWS WAF helps protect web applications from common exploits, such as SQL injection or cross-site scripting.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the [associate or disassociate an AWS WAF web ACL and an existing CloudFront distribution by using the CloudFront console](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html) docs to integrate with AWS WAF.

### From the command line{% #from-the-command-line %}

1. Run `aws waf get-change-token` to generate a token.

1. Run `aws waf create-ip-set` with your newly generated token. Additional information can be found in the [create-ip-set AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/wafv2/create-ip-set.html).

In the `create-ip-set.sh` file:

   ```bash
       create-ip-set
           --name test_ipset
           --change-token abcd0123-1234-a12b-1234-a0b1c2e3d4f5
       
```

1. Create an `IPSetDescriptor` JSON object in a new document and define the IP address or ranges you wish to block. Save the file.

In the `ip-set-descriptor.sh` file:

   ```bash
       [
         {
           "Action": "INSERT",
           "IPSetDescriptor": {
           "Type": "IPV4" | "IPV6",
           "Value": "192.0.2.0/24"
           }
         }
       ]
       
```

1. Run `aws waf update-ip-set` with the `change-token` (generated in step 1), `ip-set-id` (generated in step 2), and the file you just created. Additional information can be found in the [update-ip-set AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/waf/update-ip-set.html).

In the `update-ip-set.sh` file:

   ```bash
       aws waf update-ip-set
         --ip-set-id bd12ea6c-012a-4b7c-9342-80ab96e4b291
   	    --change-token abcd0123-1234-a12b-1234-a0b1c2e3d4f5
   	    --updates file://ip-set-descriptor.json
       
```

1. Run `aws waf create-rule` with a new rule `name` and your `change-token` (generated in step 1). Additional information can be found in the [create-rule AWS documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rule.html).

In the `create-rule.sh` file:

   ```bash
       aws waf create-rule
   	    --name NameOfRule
   	    --change-token abcd0123-1234-a12b-1234-a0b1c2e3d4f5
       
```

1. Run `aws waf create-web-acl` with a `name` and your `change-token` (generated in step 1), and set the default action to block. Additional information can be found in the [create-web-acl AWS documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-web-acl.html).

In the `create-web-acl.sh` file:

   ```bash
       aws waf create-web-acl
   	    --name NameOfACL
         --default-action Type=BLOCK
   	    --change-token abcd0123-1234-a12b-1234-a0b1c2e3d4f5
       
```

1. Create a new JSON file and define `ActivatedRule` as an object that references the ACL rule created in step 6. Assign it a default action, `INSERT`.

In the `actived-rule.json` file:

   ```json
       [
         {
           "Action": "INSERT",
           "ActivatedRule": {
             "RuleId": "your-rule-id",
             "Action": {
               "Type": "BLOCK"
             }
           }
         }
       ]
       
```

1. Run `update-web-acl` with the `web-acl-id` (generated in step 5), `change-token` (generated in step 1), and the file you just created in step 7.

In the `update-web-acl.sh` file:

   ```bash
       aws waf update-web-acl
           --web-acl-id webaclid
           --change-token 96836241-b667-4f0a-a655-e4bc49eaa2c4
           --update activated-rule.json
       
```

1. Run `get-distribution-config`.

1. In a new JSON file, modify the returned configuration information to attach the WAF ACL. Set the `WebACLId` as the ID you returned in step 5. Save the file.

In the `activated-rule.json` file:

   ```json
       {
         "ETag": "etag",
         "DistributionConfig": {
           ...
           "WebACLId": "webaclid",
           ...
         }
       }
       
```

1. Run `update-distribution` with the `id` and `etag` previously returned in step 9. Additional information can be found in the [update-distribution AWS documentation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution.html).

In the `update-distribution.sh` file:

   ```bash
       aws cloudfront update-distribution
           --id webaclid
           --distribution-config activated-ruled.json
           --if-match etag
       
```
