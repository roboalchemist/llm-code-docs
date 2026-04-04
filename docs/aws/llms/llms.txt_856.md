# Source: https://docs.aws.amazon.com/waf/latest/developerguide/llms.txt

# AWS WAF, AWS Firewall Manager, AWS Shield Advanced, and AWS Shield network security director Developer Guide

> Describes how to get started with AWS WAF and AWS Firewall Manager, the AWS web application firewall services, Shield Advanced, which provides expanded DDoS attack protection, and AWS Shield network security director, which runs network analysiss and evaluates the security of AWS resources.

- [What are AWS WAF, Shield Advanced, AWS Shield network security director and Firewall Manager?](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
- [Setting up your account](https://docs.aws.amazon.com/waf/latest/developerguide/setting-up-waf.html)
- [Related information](https://docs.aws.amazon.com/waf/latest/developerguide/resources.html)

## [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

### [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

Learn how to set up and configure AWS WAF to protect your web applications and APIs.

- [Set up AWS WAF (new console)](https://docs.aws.amazon.com/waf/latest/developerguide/setup-iap-console.html): This section guides you through setting up AWS WAF using the new new console experience, which provides simplified configuration workflows and enhanced security management capabilities.
- [Set up AWS WAF (standard console)](https://docs.aws.amazon.com/waf/latest/developerguide/setup-existing-console.html): Follow this tutorial to set up AWS WAF using the standard console experience.

### [How AWS WAF works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html)

You use AWS WAF to control how your protected resources respond to HTTP(S) web requests.

- [Resources that you can protect with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works-resources.html): Understand what resources you can protect with a AWS WAF protection pack (web ACL).
- [Working with the updated console experience](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html): AWS WAF offers two options for using the console:

### [Configuring protection](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)

This page explains what protection packs (web ACLs) are and how they work.

- [Creating a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-creating.html)
- [Editing a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-editing.html)
- [Managing rule group behavior](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-rule-group-settings.html): This section describes your options for modifying how you use a rule group in your protection pack (web ACL).

### [Associating or disassociating protection with an AWS resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)

You can use AWS WAF to create the following associations between protection packs (web ACLs) and your resources:

- [Associating protection with an AWS resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating.html)
- [Disassociating a protection from an AWS resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-dissociating-aws-resource.html)

### [Using protection packs (web ACLs) with rules and rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-processing.html)

This section introduces how protection packs (web ACLs) and web ACLs work with rules and rule groups.

- [Setting rule priority](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-processing-order.html): This section explains how AWS WAF uses numeric priority settings to set the evaluation order for rules.
- [Rule and rule group actions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-rule-actions.html): This section explains how AWS WAF uses rules and rule groups to handle actions.
- [Overriding rule group actions](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-rule-group-override-options.html): This section explains how to override rule group actions.
- [Setting the protection pack (web ACL) default action](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-default-action.html): This section explains how protection pack (web ACL) default actions work.
- [Body inspection considerations](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-setting-body-inspection-limit.html): The body inspection size limit is the maximum request body size that AWS WAF can inspect.
- [Configuring CAPTCHA, challenge, and tokens](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-captcha-challenge-token-domains.html): You can configure options in your protection pack (web ACL) for the rules that use the CAPTCHA or Challenge rule actions and for the application integration SDKs that manage silent client challenges for AWS WAF managed protections.
- [Viewing web traffic metrics](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-working-with.html): This section explains how to access summaries of web traffic metrics.
- [Deleting a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-deleting.html): This section provides procedures for deleting protection packs (web ACLs) through the AWS console.

### [AWS WAF rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html)

Use AWS WAF to control access to your content and to monitor the requests that are forwarded to an Amazon CloudFront distribution, an Amazon API Gateway REST API, an Application Load Balancer, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, AWS Amplify, or an AWS Verified Access instance.

- [Using rule actions](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-action.html): The rule action tells AWS WAF what to do with a web request when it matches the rule.

### [Using rule statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements.html)

Rule statements tell AWS WAF how to inspect a web request.

### [Adjusting rule statement settings](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields.html)

Settings that are used to specify the web request component to inspect and how to handle it.

- [Request components options](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html): Components of the web request that you can inspect.
- [Using forwarded IP addresses](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-forwarded-ip-address.html): Specify the location where AWS WAF looks for the client IP address.
- [Inspecting HTTP/2 pseudo headers](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-request-components-for-http2-pseudo-headers.html): Understand how to inspect HTTP/2 pseudo headers.
- [Using text transformations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-transformation.html): Specify transformations for AWS WAF to apply to the request before inspecting them.
- [Using scope-down statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-scope-down-statements.html): Use scope-down statements to narrow the scope of the requests that rate-based and managed rule group statements evaluate.
- [Referencing reusable entities](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-reusable-entities.html): Rule statements that reference a set or a rule group.

### [Using match rule statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-match.html)

Match rule statements.

- [Geographic match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-geo-match.html): The geographic match statement matches web requests that originate from specific countries.
- [IP set match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-ipset-match.html): The IP set match statement inspects the IP address of a web request against a set of IP addresses and address ranges.
- [ASN match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-asn-match.html): This section explains what an Autonomous System Number (ASN) match statement is and how it works.
- [Label match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-label-match.html): The label match statement inspects the labels that have been added to a web request by other rules that have run before in the same protection pack (web ACL).
- [Regex match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-regex-match.html): The regex match statement matches the designated part of a web request against the specified regex pattern.
- [Regex pattern set](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-regex-pattern-set-match.html): The regex pattern set match statement matches designated part of a web request against the regex patterns in a pattern set.
- [Size constraint](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-size-constraint-match.html): The size constraint statement inspects a part of the web request for size.
- [SQLi attack](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-sqli-match.html): The SQL injection match statement inspects the designated part of a web request for SQL injection attacks.
- [String match](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-string-match.html): The string match statement inspects designated part of a web request for a specific string.
- [XSS scripting attack](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-xss-match.html): The cross-site scripting match statement inspects a designated part of a web request for specific malicious scripts.

### [Using logical rule statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-logical.html)

Logical rule statements.

- [AND logic](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-and.html): The AND rule statement combines nested statements with AND logic.
- [NOT logic](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-not.html): The NOT rule statement logically negates the results of a single nested statement.
- [OR logic](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-or.html): The OR rule statement combines nested statements with OR logic.

### [Using rate-based rule statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)

The rate-based rule restricts incoming requests based on a count of requests grouped by aggregation keys, such as IP addresses and header values.

- [Rate-based rule high-level settings](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-high-level-settings.html): Understand the high level options for rate-based rules.
- [Rate-based rule caveats](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-caveats.html): Understand the caveats for using rate-based rules.
- [Aggregating rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-options.html): Understand the options for request aggregation.
- [Aggregation instances and counts](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-aggregation-instances.html): Understand aggregation instances and counts in request aggregation.
- [Applying rate limiting](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-request-limiting.html): Understand how the limiting behavior works for rate-based rules.

### [Rate-based rule examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based-examples.html)

See example use cases for rate-based rules.

- [Rate limit the requests to a login page](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-login-page.html): Rate-based rule example: Rate limit the requests to a login page.
- [Rate limit the requests to a login page from any IP address, user agent pair](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-login-page-keys.html): Rate-based rule example: Rate limit the requests to a login page from any IP address, user agent pair.
- [Rate limit the requests that are missing a specific header](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-missing-header.html): Rate-based rule example: Rate limit the requests that are missing a specific header.
- [Rate limit the requests with specific labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-labels.html): Rate-based rule example: Rate limit the requests with specific labels.
- [Rate limit the requests for labels that have a specified label namespace](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-label-aggregation.html): Rate-based rule example: Rate limit the requests for labels with a label namespace.
- [Rate limit the requests with specific ASNs](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-based-example-limit-asn.html): Learn how to configure rate-based rules to limit requests from specific ASNs using custom key aggregation.
- [Listing rate limited IP addresses](https://docs.aws.amazon.com/waf/latest/developerguide/listing-managed-ips.html): Find out how to access the list of IP addresses that are currently rate-limited by a rate-based rule by using the CLI, the API, or any of the SDKs.

### [Using rule group rule statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-rule-group.html)

Rule group rule statements.

- [Using managed rule group statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-managed-rule-group.html): The managed rule group rule statement references a managed rule group in your protection pack (web ACL).
- [Using rule group statements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rule-group.html): The rule group rule statement adds a reference to your protection pack (web ACL) rules list to a rule group that you manage.

### [AWS WAF rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html)

Understand how to manage and use reusable sets of rules that are defined in rule groups.

### [Using managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html)

Protect your resources with AWS Managed Rules rule groups and AWS Marketplace rule groups, which are collections of predefined rules.

### [Using versioned managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-versioning.html)

Understand how versioning is handled for managed rule groups and the best practices to apply in your versioning choices.

- [Version life cycle](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-versioning-lifecycle.html): Understand the life cycle of a versioned managed rule group.
- [Version expiration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-versioning-expiration.html): Understand how version expiration works for a versioned managed rule group.
- [Best practices for managed rule group versions](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-best-practice.html): Follow this best practice guidance for handling versioning when you use a versioned managed rule group.

### [Working with managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups.html)

Understand your options for using managed rule groups that are maintained for you by AWS and AWS Marketplace sellers.

- [Retrieving the list of managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-list.html): You can retrieve the list of managed rule groups that are available for you to use in your protection packs (web ACLs).
- [Retrieving a managed rule group's rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-rules.html): You can retrieve a list of the rules in a managed rule group.
- [Retrieving a managed rule group's versions](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-versions.html): The available versions of a managed rule group are versions that haven't yet been scheduled to expire.
- [Adding a managed rule group to a protection pack (web ACL) through the console](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-group.html): This section explains how to add a managed rule group to a protection pack (web ACL) through the console.
- [Getting notified of new versions and updates](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-sns-topic.html): This section explains how to receive Amazon SNS notifications of new versions and updates.
- [Tracking version expiration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-expiration.html): This section explains how to monitor expiration scheduling for a managed rule group through Amazon CloudWatch.
- [Example configurations in JSON and YAML](https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-json-yaml.html): This section provides example managed rule group configurations.

### [AWS Managed Rules for AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html)

Protect your resources with AWS Managed Rules rule groups.

### [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html)

The list of available AWS Managed Rules rule groups.

- [Baseline rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html): Baseline rule groups available from AWS Managed Rules.
- [Use-case specific rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html): Use-case specific rule groups available from AWS Managed Rules.
- [IP reputation rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html): The IP reputation rule groups available from AWS Managed Rules.
- [Account creation fraud prevention rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-acfp.html): Learn about the AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group available from AWS Managed Rules.
- [Account takeover prevention rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html): Learn about the AWS WAF Fraud Control account takeover prevention (ATP) managed rule group available from AWS Managed Rules.
- [Bot Control rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html): Learn about the Bot Control managed rule group available from AWS Managed Rules.
- [Anti-DDoS rule group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-anti-ddos.html): Learn about the Anti-DDoS managed rule group available from AWS Managed Rules.

### [Deployments for versioned AWS Managed Rules rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments.html)

Understand how AWS deploys updates to AWS Managed Rules rule groups.

- [Deployment notifications](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-notifications.html): This section explains how Amazon SNS notifications work with AWS Managed Rules rule groups.
- [Standard deployments overview](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-standard.html): AWS rolls out new AWS Managed Rules functionality using three standard deployment stages: release candidate, static version, and default version.
- [Typical version states](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-typical-version-states.html): Normally, a versioned managed rule group has a number of unexpired static versions, and the default version points to the static version that AWS recommends.
- [Release candidate deployments](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-release-candidate.html): This section explains how a temporary release candidate deployment works.
- [Static version deployments](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-static-version.html): When AWS determines that a release candidate provides valuable changes to the rule group, AWS deploys a new static version for the rule group based on the release candidate.
- [Default version deployments](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-default-version.html): When AWS determines that a new static version provides improved protections for the rule group compared to the current default, AWS updates the default version to the new static version.
- [Exception deployments](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-exceptions.html): AWS might bypass the standard deployment stages in order to quickly deploy updates that address critical security risks.
- [Default deployment rollbacks](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups-deployments-default-rollbacks.html): Under certain conditions, AWS might roll back the default version to its prior setting.
- [AWS Managed Rules changelog](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-changelog.html): Changelog for AWS Managed Rules.

### [Managing your own rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)

Protect your resources with your own rule groups, which are collections of predefined rules that you can reuse in multiple protection packs (web ACLs).

- [Creating a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-creating.html): To create a new rule group, follow the procedure on this page.
- [Editing a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-editing.html): To add or remove rules from a rule group or change configuration settings, access the rule group using the procedure on this page.
- [Using your rule group in a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-using.html): To use a rule group in a protection pack (web ACL), you add it to the protection pack (web ACL) in a rule group reference statement.
- [Deleting a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-deleting.html): Follow the guidance in this section to delete a rule group.
- [Sharing a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-sharing.html): You can share a rule group with other acccounts, for use by those accounts.
- [AWS Marketplace rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/marketplace-rule-groups.html): This section explains how to use AWS Marketplace rule groups.
- [Recognizing rule groups from other services](https://docs.aws.amazon.com/waf/latest/developerguide/waf-service-owned-rule-groups.html): Understand the rule groups and protection packs (web ACLs) that other services own and provide, which you might see in your account.
- [Web ACL capacity units (WCUs)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html): Understand how AWS WAF controls processing capacity for your rules, rules groups, protection packs (web ACLs), and web ACLs.
- [Oversize web request components](https://docs.aws.amazon.com/waf/latest/developerguide/waf-oversize-request-components.html): Manage the size limits on inspecting the web request body, headers, and cookies in AWS WAF.
- [Supported regular expression syntax](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-support.html): AWS WAF supports the regular expression pattern syntax used by the PCRE library libpcre.

### [IP sets and regex pattern sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)

This section introduces the topics of IP sets and regex pattern sets.

- [Creating and managing an IP set](https://docs.aws.amazon.com/waf/latest/developerguide/waf-ip-set-managing.html): An IP set provides a collection of IP addresses and IP address ranges that you want to use together in a rule statement.
- [Creating and managing a regex pattern set](https://docs.aws.amazon.com/waf/latest/developerguide/waf-regex-pattern-set-managing.html): A regex pattern set provides a collection of regular expressions that you want to use together in a rule statement.

### [Customized web requests and responses](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html)

This section explains how to add custom web request and response handling behavior to your AWS WAF rule actions and default protection pack (web ACL) actions.

- [Inserting custom request headers](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-incoming-request.html): Add custom request headers for rules that don't block requests.
- [Sending custom responses](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-for-blocked-requests.html): Customize responses when you block a request with the Block rule action.
- [Supported response status codes](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html): View the status codes that you can use in a custom response.

### [Web request labeling](https://docs.aws.amazon.com/waf/latest/developerguide/waf-labels.html)

Use labels to create complex, multi-rule evaluations of your web requests.

- [How labeling works](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-overview.html): Understand how AWS WAF labeling works.
- [Label syntax and naming requirements](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-requirements.html): Understand how to construct and match against an AWS WAF label.
- [Rules that add labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-add.html): Understand how you can configure your rule to add a label to a web request.

### [Rules that match labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-match.html)

Understand how to match against an AWS WAF label.

- [Label match examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-match-examples.html): Label match examples.

### [Intelligent threat mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections.html)

Understand how to use the intelligent threat mitigation features of AWS WAF.

### [Mitigation options](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-comparison-table.html)

Understand the differences between the options for intelligent threat mitigation.

- [Challenges and token acquisition](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-comparison-table-token.html): Understand the differences between the challenge and token management options for intelligent threat mitigation.
- [Managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-comparison-table-rg.html): Understand the differences between the rule groups that provide intelligent threat mitigation.
- [Rate limiting](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rate-limiting-options.html): Understand the options available in AWS WAF for rate-based mitigations.
- [Best practices](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections-best-practices.html): Understand the best practices for your intelligent threat mitigation implementation.

### [Tokens in intelligent threat mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens.html)

Understand how AWS WAF uses tokens for intelligent threat mitigation.

- [How AWS WAF uses tokens](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-usage.html): Understand when AWS WAF uses tokens.
- [Token characteristics](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-details.html): Understand token characteristics.

### [Setting timestamp expiration and token immunity times](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-immunity-times.html)

Understand how challenge and CAPTCHA timestamps expire.

- [Where to set the immunity times](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-immunity-times-setting.html): Understand how to set challenge and CAPTCHA timestamps expiration.
- [Specifying token domains and domain lists](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-domains.html): Understand how to configure the domains that AWS WAF uses in tokens and that it accepts in tokens.
- [Types of token labels](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-labeling.html): Understand when and how web requests with tokens are labeled by the bot and fraud intelligent threat mitigation managed rule groups.
- [Blocking requests that don't have a valid token](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-block-missing-tokens.html): Understand how to block login requests that are missing their tokens when using the AWS WAF mobile SDK.
- [Configuration for Application Load Balancers that are CloudFront origins](https://docs.aws.amazon.com/waf/latest/developerguide/waf-tokens-with-alb-and-cf.html): Understand how to ensure that your tokens are passed to AWS WAF when you protect an Application Load Balancer, and deploy the Application Load Balancer as the origin for a CloudFront distribution.

### [AWS WAF Fraud Control account creation fraud prevention (ACFP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp.html)

Understand how to use the account creation fraud prevention features in AWS WAF.

- [ACFP components](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-components.html): Understand the main components available for your ACFP implementation.
- [Using application integration SDKs with ACFP](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-with-tokens.html): Understand the importance of implementing the application integration SDKs with ACFP.
- [Adding the ACFP managed rule group to your protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-rg-using.html): Understand how to add and configure the AWSManagedRulesACFPRuleSet rule group.
- [Testing and deploying ACFP](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-deploying.html): Understand how to test, and deploy your AWS WAF Fraud Control account creation fraud prevention (ACFP) implementation.

### [ACFP examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-control-examples.html)

Understand how to configure your protection pack (web ACL) for common AWS WAF Fraud Control account creation fraud prevention (ACFP) use cases.

- [Simple configuration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-control-example-basic.html): Add an AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group to your protection pack (web ACL).
- [Custom response for compromised credentials](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-control-example-compromised-credentials.html): Override the rule group's Block action for compromised credentials in order to send a custom response to the end user.
- [Response inspection configuration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-acfp-control-example-response-inspection.html): Add an AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group to your protection pack (web ACL), with response inspection configured.

### [AWS WAF Fraud Control account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp.html)

Understand how to use the account takeover prevention features in AWS WAF.

- [ATP components](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-components.html): Understand the main components available for your ATP implementation.
- [Using application integration SDKs with ATP](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-with-tokens.html): Understand the importance of implementing the application integration SDKs with ATP.
- [Adding the ATP managed rule group to your web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-rg-using.html): Understand how to add and configure the AWSManagedRulesATPRuleSet rule group.
- [Testing and deploying ATP](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-deploying.html): Understand how to test, and deploy your AWS WAF Fraud Control account takeover prevention (ATP) implementation.

### [ATP examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-control-examples.html)

Understand how to configure your protection pack (web ACL) for common AWS WAF Fraud Control account takeover prevention (ATP) use cases.

- [Simple configuration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-control-example-basic.html): Add an AWS WAF Fraud Control account takeover prevention (ATP) managed rule group to your protection pack (web ACL).
- [Custom handling for missing or compromised credentials](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-control-example-user-agent-exception.html): Override the rule group's Block action on missing credentials and perform a custom action.
- [Response inspection configuration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-atp-control-example-response-inspection.html): Add an AWS WAF Fraud Control account takeover prevention (ATP) managed rule group to your protection pack (web ACL), with response inspection configured.

### [AWS WAF Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control.html)

Understand how to use AWS WAF Bot Control to filter and control requests from bots.

- [Bot Control components](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-components.html): Understand the main components available for your Bot Control implementation.
- [Using application integration SDKs with Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-with-tokens.html): Understand the importance of implementing the application integration SDKs with Bot Control.
- [Adding the Bot Control managed rule group to your protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-rg-using.html): Understand how to add and configure the AWSManagedRulesBotControlRuleSet rule group.
- [False positives with Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-false-positives.html): Understand when you might encounter false positives with AWS WAF Bot Control.
- [Testing and deploying Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-deploying.html): Understand how to configure, test, and deploy your AWS WAF Bot Control implementation.

### [Bot Control examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-examples.html)

Understand how to configure your protection pack (web ACL) for common AWS WAF Bot Control use cases.

- [Simple configuration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-basic.html): Add an AWS WAF Bot Control managed rule group to your protection pack (web ACL).
- [Explicitly allowing verified bots](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-allow-verified-bots.html): Explicitly allow verified bots with AWS WAF Bot Control.
- [Blocking verified bots](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-block-verified-bots.html): Block verified bots with AWS WAF Bot Control.
- [Allowing a specific blocked bot](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-allow-blocked-bot.html): Allow a specific bot that would normally be blocked by AWS WAF Bot Control.
- [Creating an exception for a blocked user agent](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-user-agent-exception.html): Exclude a user agent from AWS WAF Bot Control management.
- [Using Bot Control only for the login page](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-scope-down-login.html): Use the AWS WAF Bot Control managed rule group only on your login page.
- [Using Bot Control only for dynamic content](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-scope-down-dynamic-content.html): Use the AWS WAF Bot Control managed rule group only on dynamic content.
- [Excluding IP range from bot management](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-scope-down-ip.html): Block most bots normally with AWS WAF Bot Control, but exclude traffic from a specific IP range.
- [Allowing traffic from a bot that you control](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-scope-down-your-bot.html): Exclude a bot that you control from AWS WAF Bot Control management.
- [Enabling targeted inspection level](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-targeted-inspection-level.html): Add an AWS WAF Bot Control managed rule group statement to your protection pack (web ACL) with targeted inspection level enabled.
- [Using two statements to limit the use of targeted inspection level](https://docs.aws.amazon.com/waf/latest/developerguide/waf-bot-control-example-common-and-targeted-inspection-level.html): Use two AWS WAF Bot Control managed rule group statements in your protection pack (web ACL) to limit the use of the targeted inspection level.

### [Distributed Denial of Service (DDoS) prevention](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos.html)

Learn how to protect your applications using DDoS protection features in AWS WAF.

- [Resource-level DDoS protection](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos-alb.html): Understand how to use the standard tier of Anti-DDoS protection with Application Load Balancers.

### [Using the Anti-DDoS managed rule group](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos-advanced.html)

Learn how to implement advanced Anti-DDoS protection using the AWSManagedRulesAntiDDoSRuleSet.

- [Adding the Anti-DDoS managed rule group to your protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos-rg-using.html): Understand how to add and configure the AWSManagedRulesAntiDDoSRuleSet rule group.
- [Testing and deploying Anti-DDoS](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos-deploying.html): Understand how to test, and deploy your AWS WAF Distributed Denial of Service (DDoS) prevention implementation.
- [Best Practices for Anti-DDoS](https://docs.aws.amazon.com/waf/latest/developerguide/waf-anti-ddos-best-practices.html)

### [Client application integrations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration.html)

Understand how to use the intelligent threat integration APIs and JavaScript CAPTCHA integration APIs with your AWS WAF features.

- [Intelligent threat integration and AWS Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration-with-AMRs.html): Understand how the intelligent threat integration APIs work with the AWS Managed Rules rule groups
- [Accessing the integration APIs](https://docs.aws.amazon.com/waf/latest/developerguide/waf-application-integration-location-in-console.html): Understand where to find the application integration APIs in the AWS WAF console.

### [JavaScript integrations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-javascript-api.html)

Understand how to use the AWS WAF JavaScript integrations.

- [Providing domains for use in the tokens](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-set-token-domain.html): This section explains how to provide additional domains for tokens.
- [Content security policies](https://docs.aws.amazon.com/waf/latest/developerguide/waf-javascript-api-csp.html): This section provides an example configuration to allowlist the AWS WAF apex domain.

### [Using the intelligent threat API](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api.html)

Understand how to use the intelligent threat JavaScript API in your client application.

- [Intelligent threat API specification](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-specification.html): Understand the components of the JavaScript APIs for intelligent threat mitigation.
- [How to use the fetch wrapper](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-fetch-wrapper.html): This section provides instructions for using the integration fetch wrapper.
- [How to use getToken](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-challenge-api-get-token.html): This section explains how to use the getToken operation.

### [Using the CAPTCHA JavaScript API](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api.html)

Understand how to use the CAPTCHA API in your JavaScript application.

- [CAPTCHA JavaScript API specification](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api-specification.html): Understand the components of the JavaScript APIs for CAPTCHA.
- [How to render the CAPTCHA puzzle](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api-render.html): This section provides an example renderCaptcha implementation.
- [Handling a CAPTCHA response from AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api-conditional.html): This section provides an example of handling a CAPTCHA response.
- [Managing JS CAPTCHA API keys](https://docs.aws.amazon.com/waf/latest/developerguide/waf-js-captcha-api-key.html): This section provides instructions for generating and deleting API keys.

### [Mobile application integration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-mobile-sdk.html)

Understand how to use the AWS WAF mobile SDKs to integrate the silent challenge into your applications for intelligent threat mitigation.

- [Installing the mobile SDK](https://docs.aws.amazon.com/waf/latest/developerguide/waf-mobile-sdk-installing.html): Understand how to install an AWS WAF mobile SDK.
- [Mobile SDK specification](https://docs.aws.amazon.com/waf/latest/developerguide/waf-mobile-sdk-specification.html): Understand the classes, properties, and operations of the AWS WAF mobile SDK.
- [How the Mobile SDK works](https://docs.aws.amazon.com/waf/latest/developerguide/waf-mobile-sdk-how-it-works.html): Understand how the AWS WAF mobile SDK classes, properties, and operations work together.
- [Code examples for the Mobile SDK](https://docs.aws.amazon.com/waf/latest/developerguide/waf-mobile-sdk-coding-examples.html): See code examples for using the AWS WAF mobile SDK.

### [CAPTCHA and Challenge](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge.html)

Use the CAPTCHA action to verify that web requests are being entered by human beings and use the Challenge action to verify that the sending clients are browsers.

### [CAPTCHA puzzles](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-puzzle.html)

Understand the features and functionality of the AWS WAF CAPTCHA puzzle.

- [Language support](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-puzzle-language-support.html): Understand what languages are supported in AWS WAF CAPTCHA puzzles.
- [Puzzle examples](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-puzzle-examples.html): See examples of the captcha; puzzles that AWS WAF supports.

### [How the rule actions work](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-how-it-works.html)

Understand how CAPTCHA and Challenge work.

- [Action behavior](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-actions.html): Understand what the CAPTCHA and Challenge actions do.
- [Logs and metrics](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-logs-metrics.html): Understand how AWS WAF handles logging and metrics for the CAPTCHA and Challenge actions.
- [CAPTCHA and Challenge best practices](https://docs.aws.amazon.com/waf/latest/developerguide/waf-captcha-and-challenge-best-practices.html): Understand best practice recommendations for CAPTCHA and Challenge actions.

### [Data protection and logging for web traffic](https://docs.aws.amazon.com/waf/latest/developerguide/waf-data-protection-and-logging.html)

This section explains the data logging, collection, and protection options that you can use with AWS WAF.

### [Logging](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)

This section explains the logging options for your AWS WAF protection packs (web ACLs).

- [Pricing for logging](https://docs.aws.amazon.com/waf/latest/developerguide/logging-pricing.html): Understand the pricing considerations for using protection pack (web ACL) traffic logs.

### [AWS WAF logging destinations](https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html)

Configure logging for AWS WAF logs and configure the permissions that are required for each logging option.

- [CloudWatch Logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging-cw-logs.html): Configure protection pack (web ACL) traffic logging to Amazon CloudWatch Logs.
- [Amazon S3](https://docs.aws.amazon.com/waf/latest/developerguide/logging-s3.html): Configure protection pack (web ACL) traffic logging to Amazon S3.
- [Firehose](https://docs.aws.amazon.com/waf/latest/developerguide/logging-kinesis.html): Configure protection pack (web ACL) logging to Amazon Data Firehose.
- [Configuring logging](https://docs.aws.amazon.com/waf/latest/developerguide/logging-management-configure.html): This section provides instructions for configuring data protection for a protection pack (web ACL).
- [Finding your protection pack (web ACL) records](https://docs.aws.amazon.com/waf/latest/developerguide/logging-management.html): This section explains how to find your protection pack (web ACL) records.
- [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html): The following list describes the possible log fields.
- [Log examples](https://docs.aws.amazon.com/waf/latest/developerguide/logging-examples.html): This section provides examples for logging protection pack (web ACL) traffic.

### [Data protection](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-masking.html)

Configure data protection to implement data protection to sensitive information in specific data fields for enhanced security and compliance.

- [Enabling data protection](https://docs.aws.amazon.com/waf/latest/developerguide/enable-protection.html): Learn about data protection and log configuration options available in the console for securing and monitoring your AWS resources.
- [Data protection exceptions](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-exceptions.html): Learn how to configure exceptions for data protection in AWS WAF to include protected content in RuleMatchDetails and rateBasedRuleList for troubleshooting purposes.
- [Data protection limitations](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-limitations.html): Learn about the limitations to consider when implementing data protection measures in your AWS WAF protection packs (web ACLs).
- [Examples of data protection](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-examples.html): Explore examples of AWS WAF protection pack (web ACL) traffic with data protection applied in logs.
- [Configuring data protection for a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection-configure.html): Configure data protection settings for your protection pack (web ACL) to enhance security and control access to your web applications.

### [Testing and tuning your protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html)

Understand how to test, monitor, and tune your protection packs (web ACLs).

- [Testing and tuning high-level steps](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-high-level.html): Understand the steps for testing and tuning your protection pack (web ACL).
- [Preparing for testing](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-prep.html): Understand the steps for preparing to test and tune your AWS WAF protections.

### [Monitoring and tuning your AWS WAF protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-activities.html)

Understand the steps for monitoring and tuning your AWS WAF protections.

- [Viewing protection pack (web ACL) metrics](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-view-metrics.html): This section describes how to view metrics for your protection pack (web ACL).

### [Traffic overview dashboards for protection packs (web ACLs)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-dashboards.html)

Understand how to view and interpret protection pack (web ACL) traffic overview dashboards.

- [Viewing the dashboards for a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-dashboards-accessing.html): Understand what you can see in the protection pack (web ACL) traffic overview dashboards.
- [Examples of the protection pack (web ACL) traffic dashboards](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-dashboards-screenshots.html): See various examples of the information available in the traffic overview dashboards.
- [Viewing a sample of web requests](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-view-sample.html): This section describes the protection pack (web ACL) Sampled requests tab in the AWS WAF console.
- [Enabling your protections in production](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing-enable-production.html): Understand the steps for enabling your tuned protections in production.

### [Using AWS WAF with Amazon CloudFront](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-features.html)

Learn how to configure AWS WAF to inspect web requests for different types of CloudFront distributions, including single tenant (standard) or multi-tenant (template) distributions.

- [Use cases](https://docs.aws.amazon.com/waf/latest/developerguide/cloudfront-waf-use-cases.html): Explore common use cases for enhancing CloudFront distribution security using AWS WAF to protect against web attacks.

### [Security in your use of the AWS WAF service](https://docs.aws.amazon.com/waf/latest/developerguide/security.html)

Configure AWS WAF to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your AWS WAF resources.

- [Protecting your data](https://docs.aws.amazon.com/waf/latest/developerguide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS WAF.

### [Using IAM with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/security-iam.html)

How to authenticate requests and manage access to your AWS WAF resources.

- [How AWS WAF works with IAM](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_service-with-iam.html): This section explains how to use the features of IAM with AWS WAF.
- [Identity-based policy examples](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_id-based-policy-examples.html): This section provides identity-based policy examples for AWS WAF.
- [AWS managed policies](https://docs.aws.amazon.com/waf/latest/developerguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS WAF and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS WAF and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/waf/latest/developerguide/using-service-linked-roles.html): How to use service-linked roles to give AWS WAF access to resources in your AWS account.
- [Logging and monitoring](https://docs.aws.amazon.com/waf/latest/developerguide/waf-incident-response.html): Use AWS tools for monitoring and responding to events.
- [Validating compliance](https://docs.aws.amazon.com/waf/latest/developerguide/waf-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Building for resilience](https://docs.aws.amazon.com/waf/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as any specific AWS WAF features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/waf/latest/developerguide/infrastructure-security.html): Learn how AWS WAF isolates service traffic.
- [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html)

### [Migrating your AWS WAF Classic resources to AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html)

- [Why migrate to AWS WAF?](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-why-migrate.html): The latest version of AWS WAF provides many improvements over the prior version, while maintaining most of the concepts and terminology that you're accustomed to.
- [Migration caveats](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-caveats.html): The migration only handles protection pack (web ACL) configurations, and the protection pack (web ACL) migration doesn't bring over all settings exactly as you have them in AWS WAF Classic.
- [How the migration works](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-how-it-works.html): Learn how to migrate your web ACLs from AWS WAF Classic to AWS WAF v2.

### [Migrating a protection pack (web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure.html)

The automated migration carries over most of your AWS WAF Classic protection pack (web ACL) configuration, leaving some things that you need to handle manually.

- [Automated migration](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure-automatic.html)
- [Manual follow-up](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure-manual-finish.html): After the automated migration is complete, review the newly created protection pack (web ACL) and fill in the components that the migration doesn't bring over for you.
- [Additional considerations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure-additional.html): Review your new protection pack (web ACL) and consider the options available to you in the new AWS WAF to be sure that the configuration is as efficient as possible and that it's using the latest available security options.
- [Switchover](https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-procedure-switchover.html): After you've verified your new protection pack (web ACL) settings, you can start to use it in place of your AWS WAF Classic protection pack (web ACL).


## [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html)

- [Setting up AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-setting-up-waf.html)
- [How AWS WAF Classic works](https://docs.aws.amazon.com/waf/latest/developerguide/classic-how-aws-waf-works.html)
- [AWS WAF Classic pricing](https://docs.aws.amazon.com/waf/latest/developerguide/classic-aws-waf-pricing.html)
- [Getting started with AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-getting-started.html)

### [Creating and configuring a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl.html)

### [Working with conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-create-condition.html)

- [Working with cross-site scripting match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-xss-conditions.html)
- [Working with IP match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-ip-conditions.html)
- [Working with geographic match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-geo-conditions.html)
- [Working with size constraint conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-size-conditions.html)
- [Working with SQL injection match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-sql-conditions.html)
- [Working with string match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-string-conditions.html)
- [Working with regex match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-regex-conditions.html)

### [Working with rules](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules.html)

- [Creating a rule and adding conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-creating.html)
- [Adding and removing conditions in a rule](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html)
- [Deleting a rule](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-deleting.html)
- [AWS Marketplace rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-managed-rule-groups.html): Protect your resources with AWS Marketplace rule groups, which are collections of predefined rules.

### [Working with web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-working-with.html)

- [Deciding on the default action for a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-default-action.html)
- [Creating a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-creating.html)
- [Associating or disassociating a Web ACL with an Amazon API Gateway API, a CloudFront distribution or an Application Load Balancer](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-associating-cloudfront-distribution.html)
- [Editing a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-editing.html)
- [Deleting a Web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-deleting.html)
- [Testing web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-testing.html)

### [Working with AWS WAF Classic rule groups for use with AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/classic-working-with-rule-groups.html)

- [Creating an AWS WAF Classic rule group](https://docs.aws.amazon.com/waf/latest/developerguide/classic-create-rule-group.html)
- [Adding and deleting rules from an AWS WAF Classic rule group](https://docs.aws.amazon.com/waf/latest/developerguide/classic-rule-group-editing.html)

### [Getting started with AWS Firewall Manager to enable AWS WAF Classic rules](https://docs.aws.amazon.com/waf/latest/developerguide/classic-getting-started-fms.html)

- [Step 1: Complete the prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/classic-complete-prereq.html)
- [Step 2: Create rules](https://docs.aws.amazon.com/waf/latest/developerguide/classic-get-started-fms-create-rules.html)
- [Step 3: Create a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/classic-get-started-fms-create-rule-group.html)
- [Step 4: Create and apply an AWS Firewall Manager AWS WAF Classic policy](https://docs.aws.amazon.com/waf/latest/developerguide/classic-get-started-fms-create-security-policy.html)
- [Tutorial: Creating an AWS Firewall Manager policy with hierarchical rules](https://docs.aws.amazon.com/waf/latest/developerguide/hierarchical-rules.html)
- [Logging Web ACL traffic information](https://docs.aws.amazon.com/waf/latest/developerguide/classic-logging.html)
- [Listing IP addresses blocked by rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/classic-listing-managed-ips.html)
- [How AWS WAF Classic works with Amazon CloudFront features](https://docs.aws.amazon.com/waf/latest/developerguide/classic-cloudfront-features.html)

### [Security](https://docs.aws.amazon.com/waf/latest/developerguide/classic-security.html)

Configure AWS WAF Classic to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your AWS WAF Classic resources.

- [Data protection](https://docs.aws.amazon.com/waf/latest/developerguide/classic-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS WAF Classic.

### [Identity and access management](https://docs.aws.amazon.com/waf/latest/developerguide/classic-security-iam.html)

How to authenticate requests and manage access to your AWS WAF Classic resources.

- [How AWS WAF Classic works with IAM](https://docs.aws.amazon.com/waf/latest/developerguide/classic-security_iam_service-with-iam.html)
- [Identity-based policy examples](https://docs.aws.amazon.com/waf/latest/developerguide/classic-security_iam_id-based-policy-examples.html)
- [Troubleshooting](https://docs.aws.amazon.com/waf/latest/developerguide/classic-security_iam_troubleshoot.html)
- [Using service-linked roles](https://docs.aws.amazon.com/waf/latest/developerguide/classic-using-service-linked-roles.html): How to use service-linked roles to give AWS WAF Classic access to resources in your AWS account.
- [Logging and monitoring](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-incident-response.html): Use AWS tools for monitoring and responding to events.
- [Compliance validation](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/waf/latest/developerguide/classic-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific AWS WAF Classic features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/waf/latest/developerguide/classic-infrastructure-security.html): Learn how AWS WAF Classic isolates service traffic.
- [AWS WAF Classic quotas](https://docs.aws.amazon.com/waf/latest/developerguide/classic-limits.html)


## [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)

### [How Shield and Shield Advanced work](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)

Understand how AWS Shield Advanced and Shield Advanced work and follow links to more detailed information.

- [AWS Shield Standard overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-summary.html): Understand the basic functionality of AWS Shield Standard.
- [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html): AWS Shield Advanced is a managed service that helps you protect your application against external threats, like DDoS attacks, volumetric bots, and vulnerability exploitation attempts.
- [Resources that Shield Advanced protects](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-protected-resources.html)
- [Shield Advanced capabilities and options](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-capabilities.html): AWS Shield Advanced subscription includes the following capabilities and options.
- [Deciding whether to subscribe to AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-deciding.html): Review the scenarios in this section for help deciding which accounts to subscribe to AWS Shield Advanced and where to apply additional protections.
- [Examples of DDoS attacks](https://docs.aws.amazon.com/waf/latest/developerguide/types-of-ddos-attacks.html): AWS Shield Advanced provides expanded protection against many types of attacks.

### [How Shield detects events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection.html)

Understand how AWS Shield event detection works.

- [Detection for infrastructure layer threats](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection-infrastructure.html): Understand how event detection works for the network and transport layers.
- [Detection for application layer threats](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection-application.html): Understand how event detection works for the application layer.
- [Detection for multiple resources in an application](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-detection-multiple-resources.html): Understand how event detection works for multiple resources in an application.

### [How Shield mitigates events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation.html)

Understand how AWS Shield event mitigation works.

- [Mitigation features](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-features.html): Understand the Shield event mitigation features.
- [Mitigation for CloudFront and RouteÂ 53](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-continuous-inspection.html): Understand Shield event mitigation logic for continuous inspection.
- [Mitigation for AWS Regions](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-regions.html): Understand Shield event mitigation logic in AWS Regions.
- [Mitigation for AWS Global Accelerator standard accelerators](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-gax.html): Understand Shield event mitigation logic for AWS Global Accelerator standard accelerators.
- [Mitigation for Elastic IPs](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-adv-eip.html): Understand Shield event mitigation logic for Elastic IPs with AWS Shield Advanced.
- [Mitigation for web applications](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-mitigation-logic-adv-web-app.html): Understand Shield event mitigation logic for web applications with AWS Shield Advanced.

### [Building DDoS resilient architectures](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency.html)

Understand how you can get started maximizing your resiliency against DDoS attacks.

- [DDoS resiliency architecture for web applications](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency-example-web.html): See an example architecture for maximizing resiliency against DDoS attacks with AWS web applications.
- [DDoS resiliency architecture for TCP and UDP applications](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resiliency-example-tcp-udp.html): See an example architecture for maximizing resiliency against DDoS attacks with AWS TCP and UDP applications.
- [Combining Shield Advanced with other AWS services](https://docs.aws.amazon.com/waf/latest/developerguide/aws-shield-use-case.html): You can use Shield Advanced to protect your resources in many types of scenarios.

### [Setting up AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html)

Understand the steps for getting started using Shield Advanced and adding protections to your resources.

- [Subscribing to Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html): Understand how to subscribe your accounts to Shield Advanced, to start using the service.

### [Adding and configuring resource protections](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html)

Understand how to add and configure protections for your resources.

- [Configuring application layer protections](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-get-started-web-acl-rbr.html): Understand how to configure application layer protections with AWS WAF web ACLs.
- [Configuring health-based detection](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-get-started-health-checks.html): Understand how to configure health-based detection for your protections.
- [Configuring alarms and notifications](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-get-started-create-alarms.html): Understand how to configure alarms and notifications for your protections.
- [Reviewing and finishing your protection configuration](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-get-started-review-and-configure.html): Understand how to review your configured protections before saving them.
- [Setting up SRT support](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-srt.html): Getting started option for SRT support.
- [Creating a DDoS dashboard](https://docs.aws.amazon.com/waf/latest/developerguide/deploy-waf-dashboard.html): Understand how to create a DDoS dashboard in CloudWatch and set CloudWatch alarms.

### [SRT support](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html)

This page describes the function of the Shield Response Team (SRT).

- [Granting access for the SRT](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-access.html): This page provides instructions for granting permission to the SRT to act on your behalf, so that they can access your AWS WAF logs and make calls to the AWS Shield Advanced and AWS WAF APIs to manage protections.
- [Setting up proactive engagement](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-proactive-engagement.html): This page provides instructions for setting up proactive engagement with the SRT.
- [Contacting the SRT](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-contacting.html): You can contact the SRT in one of the following ways:
- [Setting up custom mitigations with the SRT](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-custom-mitigations.html): This page provides instructions for working with the SRT to build custom mitigations against DDoS attacks.

### [Resource protections](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-resource-protections.html)

You can add and configure AWS Shield Advanced protections for your resources.

- [List of protected resources](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-protections-by-resource-type.html): Understand how to use AWS Shield Advanced protections for your specific resource types.
- [Protecting Amazon EC2 instances and Network Load Balancers](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-protections-ec2-nlb.html): Understand how to use AWS Shield Advanced protections for Amazon EC2 instances and Network Load Balancers.

### [Protecting the application layer (layer 7)](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-protections.html)

Understand your options for configuring Shield Advanced protections for application layer resources.

- [Factors that affect application layer event detection and mititgation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-detection-mitigation.html): Understand the factors that affect Shield Advanced application layer detection and mitigation.
- [Using AWS WAF web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-web-ACL-and-rbr.html): Understand your options for basic application layer protections using web ACLs.
- [Using AWS WAF rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-app-layer-rbr.html): Understand your options for basic application layer protections using rate-based rules.

### [Automating application layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html)

Understand your options for using Shield Advanced to automatically respond to application layer attacks.

- [Best practices](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response-bp.html): Understand best practices for using automatic application layer DDoS mitigation.
- [Enabling automatic mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response-config.html): Understand how to configure Shield Advanced to automatically respond to application layer attacks.
- [How Shield Advanced manages automatic mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response-behavior.html): Understand how Shield Advanced manages automatic application layer DDoS mitigation.
- [Using the Shield Advanced rule group](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response-rg.html): Understand the configuration of the Shield Advanced rule group with automatic mitigation.
- [Viewing the automatic mitigation configuration for a resource](https://docs.aws.amazon.com/waf/latest/developerguide/view-automatic-app-layer-response-configuration.html): Understand how to view the automatic response for a protected resource.
- [Enabling and disabling automatic mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/enable-disable-automatic-app-layer-response.html): Understand how to enable and disable automatic response for your protected resource.
- [Changing the action for automatic mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/change-action-of-automatic-app-layer-response.html): Understand how to change the action that Shield Advanced applies in its automatic mitigations for your protected application layer resource.
- [Using AWS CloudFormation with automatic mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/manage-automatic-mitigation-in-cfn.html): Understand how to manage automatic mitigations and web ACLs in CloudFormation.

### [Health-based detection using health checks](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html)

Understand how to use Amazon RouteÂ 53 health checks for event detection and response.

- [Best practices](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-best-practices.html): Follow the best practices guidance for using Shield Advanced health-based detection.
- [Metrics commonly used for health checks](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-metrics.html): Understand which metrics are available to calculate the health of your protected resources.
- [Associating a health check](https://docs.aws.amazon.com/waf/latest/developerguide/associate-health-check.html): Understand how to associate a health check with your protected resource.
- [Disassociating a health check](https://docs.aws.amazon.com/waf/latest/developerguide/disassociate-health-check.html): Understand how to disassociate a health check from your protected resource.
- [Viewing health check association status](https://docs.aws.amazon.com/waf/latest/developerguide/health-check-association-status.html): Understand health check association status and how to manage an Unavailable status.
- [Health check examples](https://docs.aws.amazon.com/waf/latest/developerguide/health-checks-examples.html): See examples of health checks for various resource types.
- [Adding protection to a resource](https://docs.aws.amazon.com/waf/latest/developerguide/configure-new-protection.html): Add Shield Advanced protection to one or more resources.
- [Editing protections](https://docs.aws.amazon.com/waf/latest/developerguide/manage-protection.html): Change the settings for your AWS Shield Advanced protections.
- [Creating alarms and notifications](https://docs.aws.amazon.com/waf/latest/developerguide/add-alarm-ddos.html): Manage CloudWatch alarms for protected resources.
- [Removing protection from a resource](https://docs.aws.amazon.com/waf/latest/developerguide/remove-protection.html): You can remove AWS Shield Advanced protection from any of your AWS resources at any time.

### [Protection groups](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-protection-groups.html)

Use protection groups to group multiple resources and protect them as a single unit.

- [Creating a protection group](https://docs.aws.amazon.com/waf/latest/developerguide/protection-group-creating.html): Create a protection group.
- [Updating a protection group](https://docs.aws.amazon.com/waf/latest/developerguide/protection-group-updating.html): Update a protection group.
- [Deleting a Shield Advanced protection group](https://docs.aws.amazon.com/waf/latest/developerguide/protection-group-deleting.html): Delete a protection group.
- [Tracking protection changes](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-add-config.html): This page explains how to record changes to the AWS Shield Advanced protection of your resources using AWS Config.

### [Visibility into DDoS events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-viewing-events.html)

Understand your options for getting notified of events and for viewing and understanding event details.

- [Global and account activity](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-standard-event-visibility.html): Understand the information available to all customers through the Shield console and API

### [Events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-events.html)

Understand the information in the Shield Advanced events pages.

- [Fields in event summaries](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-summaries.html): Understand the information in the Shield Advanced event summaries.

### [Viewing event details](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-details.html)

Understand the information available in Shield Advanced event details.

- [Application layer](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-details-application-layer.html): Understand the information available in Shield Advanced event details page for application layer events.
- [Infrastructure layer](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-event-details-infrastructure-layer.html): Understand the information available in Shield Advanced event details page for infrastructure layer events.
- [Event visibility across accounts](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-viewing-multiple-accounts.html): Understand how to use AWS Firewall Manager and AWS Security Hub CSPM for event visibility across multiple accounts.

### [Responding to DDoS events](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding.html)

This page explains how AWS responds to DDoS attacks, and provides options for how you can further respond.

- [Contacting support for an application layer attack](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding-contact-support.html): Contact the support center during an application layer DDoS attack.
- [Manually mitigating an application layer attack](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding-manual.html): Manually mitigate an application layer DDoS attack.
- [Requesting a credit after an attack](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-request-service-credit.html): If you're subscribed to AWS Shield Advanced and you experience a DDoS attack that increases utilization of a Shield Advanced protected resource, you can request a Shield Advanced service credit for charges related to the increased utilization, to the extent that it is not mitigated by Shield Advanced.

### [Security in your use of the Shield service](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security.html)

Configure Shield to meet your security and compliance objectives, and learn how to use other AWS services that help you to secure your Shield resources.

- [Protecting your data](https://docs.aws.amazon.com/waf/latest/developerguide/shd-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Shield.

### [Using IAM with Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security-iam.html)

How to authenticate requests and manage access to your Shield resources.

- [How AWS Shield works with IAM](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security_iam_service-with-iam.html): This section explains how to use the features of IAM with AWS Shield.
- [Identity-based policy examples](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Shield resources.
- [AWS managed policies](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security-iam-awsmanpol.html): Learn about AWS managed policies for Shield and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Shield and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/waf/latest/developerguide/shd-using-service-linked-roles.html): How to use service-linked roles to give Shield Advanced access to resources in your AWS account.
- [Logging and monitoring](https://docs.aws.amazon.com/waf/latest/developerguide/shd-incident-response.html): Use AWS tools for monitoring and responding to events.
- [Validating compliance](https://docs.aws.amazon.com/waf/latest/developerguide/shd-security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Building for resilience](https://docs.aws.amazon.com/waf/latest/developerguide/shd-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as any specific Shield features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/waf/latest/developerguide/shd-infrastructure-security.html): Learn how AWS Shield isolates service traffic.
- [AWS Shield Advanced quotas](https://docs.aws.amazon.com/waf/latest/developerguide/shield-limits.html): AWS Shield Advanced is subject to the quotas described here.


## [AWS Shield network security director (preview)](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-chapter.html)

- [Use cases](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-use-cases.html)
- [Key concepts](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-concepts.html)
- [Setting up your account](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-setting-up.html): Learn how to prepare your AWS environment for AWS Shield network security director by setting up AWS Organizations, designating a delegated administrator, and configuring the required IAM permissions.
- [Enabling AWS Shield network security director](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-enablement.html): This section explains how AWS Shield network security director is enabled for AWS accounts through AWS Organizations.
- [Exploring resources and findings](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-findings.html): AWS Shield network security director dashboard provides a summary of the most severe findings, a comparison of findings by included regions, a table of accounts that have been analyzed, a panel that appears when an account is selected, and a network topology that populates once a resource within that panel is selected.

### [Analyze network security with Amazon Q Developer](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-security-insights.html)

Learn how to use Amazon Q Developer to get additional insights about your network security and remediation options.

- [Data protection considerations](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-security-insights-protection.html): For information about how Amazon Q Developer stores your conversations, see Data protection in Amazon Q Developer in the Amazon Q Developer User Guide.
- [Troubleshooting AWS Shield network security director](https://docs.aws.amazon.com/waf/latest/developerguide/troubleshooting.html): This chapter helps you diagnose and solve issues you might encounter while using AWS Shield network security director.

### [Security](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-security.html)

- [Identity and Access Management](https://docs.aws.amazon.com/waf/latest/developerguide/nsd-iam.html)
- [Identity-based policy examples](https://docs.aws.amazon.com/waf/latest/developerguide/security-nsd-with-iam-id-based-policies.html)
- [Using service-linked roles](https://docs.aws.amazon.com/waf/latest/developerguide/security_iam_nsd-with-iam-roles-service-linked.html): How to use service-linked roles to give AWS Shield network security director access to resources in your AWS account.
- [Logging AWS Shield network security director API calls with AWS CloudTrail](https://docs.aws.amazon.com/waf/latest/developerguide/logging-cloudtrail.html): Learn how AWS Shield network security director integrates with AWS CloudTrail to log API calls and monitor service activity.


## [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)

### [AWS Firewall Manager prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html)

This topic shows you how to get ready to administer AWS Firewall Manager.

- [Joining and configuring AWS Organizations for using Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/join-aws-orgs.html): To use Firewall Manager, your account must be a member of the organization in the AWS Organizations service where you want to use your Firewall Manager policies.
- [Creating an AWS Firewall Manager default administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html): This page provides instructions for creating an AWS Firewall Manager default administrator account.
- [Enabling AWS Config for using Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/enable-config.html): To use Firewall Manager, you must enable AWS Config.
- [Subscribing in the AWS Marketplace and configuring third-party settings for Firewall Manager third-party policies](https://docs.aws.amazon.com/waf/latest/developerguide/fms-third-party-prerequisites.html): Complete the following prerequisites to set up Firewall Manager third-party firewall policies.
- [Enabling resource sharing for Network Firewall and DNS Firewall policies with AWS RAM](https://docs.aws.amazon.com/waf/latest/developerguide/enable-ram.html): To manage Firewall Manager Network Firewall and DNS Firewall policies, you must enable sharing with AWS Organizations in AWS Resource Access Manager.
- [Using AWS Firewall Manager in Regions that are disabled by default](https://docs.aws.amazon.com/waf/latest/developerguide/enable-disabled-region.html): To use Firewall Manager in a Region that's disabled by default, you must enable the Region for both the management account of your AWS organization and the Firewall Manager default administrator account.

### [Using Firewall Manager administrators](https://docs.aws.amazon.com/waf/latest/developerguide/fms-administrators.html)

This page explains what Firewall Manager administrators are and defines related terms.

- [Creating a Firewall Manager administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/fms-creating-administrators.html): The following procedure describes how to create a Firewall Manager administrator account using the Firewall Manager console.
- [Updating a Firewall Manager administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/fms-updating-administrators.html): The following procedure describes how to update a Firewall Manager administrator account using the Firewall Manager console.
- [Revoking a Firewall Manager administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/fms-deleting-administrators.html): The following procedure describes how to revoke a Firewall Manager administrator account.
- [Changing the default administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/fms-change-administrator.html): The following procedure describes how to change the default Firewall Manager administrator account.
- [Disqualifying changes to an administrator account](https://docs.aws.amazon.com/waf/latest/developerguide/disqualified-admin-account.html): Some changes to an administrator account can disqualify it from remaining an administrator account.

### [Setting up AWS Firewall Manager policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)

You can use AWS Firewall Manager to enable a number of different types of security policies.

- [Setting up AWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms.html): To use AWS Firewall Manager to enable AWS WAF rules across your organization, perform the following steps in sequence.
- [Setting up AWS Shield Advanced policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-shield.html): You can use AWS Firewall Manager to enable AWS Shield Advanced protections across your organization.
- [Setting up Amazon VPC security group policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-security-group.html): To use AWS Firewall Manager to enable Amazon VPC security groups across your organization, perform the following steps in sequence.
- [Setting up Amazon VPC network ACL policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-network-acl.html): To use AWS Firewall Manager to enable network ACLs across your organization, perform the steps in this section in sequence.
- [Setting up AWS Network Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-network-firewall.html): To use AWS Firewall Manager to enable an AWS Network Firewall firewall across your organization, perform the following steps in sequence.
- [Setting up DNS Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-dns-firewall.html): To use AWS Firewall Manager to enable Amazon RouteÂ 53 Resolver DNS Firewall across your organization, perform the following steps in sequence.
- [Setting up Palo Alto Networks Cloud NGFW policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-cloud-ngfw.html): To use AWS Firewall Manager to enable Palo Alto Networks Cloud Next Generation Firewall (NGFW) policies, perform the following steps in sequence.
- [Setting up Fortigate CNF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-fortigate-cnf.html): Fortigate Cloud Native Firewall (CNF) as a Service is a third-party firewall service that you can use for your AWS Firewall Manager policies.

### [Using AWS Firewall Manager policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html)

AWS Firewall Manager provides the following types of policies.

- [Creating a policy](https://docs.aws.amazon.com/waf/latest/developerguide/create-policy.html): The steps for creating a policy vary between the different policy types.
- [Deleting a policy](https://docs.aws.amazon.com/waf/latest/developerguide/policy-deleting.html): You can delete a Firewall Manager policy by performing the following steps.
- [Using the policy scope](https://docs.aws.amazon.com/waf/latest/developerguide/policy-scope.html): This page explains what the Firewall Manager policy scope is and how it works.

### [AWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies.html)

This section explains how to use AWS WAF policies with Firewall Manager.

- [Rule group management](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies-rule-groups.html): The web ACLs that are managed by Firewall Manager AWS WAF policies contain three sets of rules.
- [Web ACL management](https://docs.aws.amazon.com/waf/latest/developerguide/how-fms-manages-web-acls.html): Firewall Manager creates and manages web ACLs for in-scope resources according to your configuration settings and general policy management.

### [Logging](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies-logging-config.html)

You can enable centralized logging for your AWS WAF policies to get detailed information about traffic that's analyzed by your web ACL within your organization.

- [Logging destinations](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies-logging-destinations.html): This section describes the logging destinations that you can choose to send your AWS WAF policy logs.
- [Enabling logging](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies-enabling-logging.html): The following procedure describes how to enable logging for an AWS WAF policy in the Firewall Manager console.
- [Disabling logging](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policies-disabling-logging.html): The following procedure describes how to disable logging for an AWS WAF policy in the Firewall Manager console.

### [AWS Shield Advanced policies](https://docs.aws.amazon.com/waf/latest/developerguide/shield-policies.html)

This page explains how to use AWS Shield policies with Firewall Manager.

- [Automatic application layer mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/shield-policies-auto-app-layer-mitigation.html): Understand how Firewall Manager handles automatic application layer DDoS mitigation for Shield Advanced policies with Amazon CloudFront distributions and Application Load Balancers.
- [Determining the version of AWS WAF used by a Shield Advanced policy](https://docs.aws.amazon.com/waf/latest/developerguide/shield-policies-identify-waf-version.html): Understand how to determine which version of AWS WAF web ACL your Shield Advanced policy uses.

### [Security group policies](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies.html)

This page explains how to use AWS Firewall Manager security group policies to manage Amazon Virtual Private Cloud security groups for your organization in AWS Organizations.

- [Common security group policies](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies-common.html): This page explains how Firewall Manager common security group policies work.
- [Content audit security group policies](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies-audit.html): This page explains how Firewall Manager content audit security group policies work.
- [Usage audit security group policies](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-policies-usage.html): This page explains how Firewall Manager usage audit security group policies work.

### [Network ACL policies](https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html)

This section covers how AWS Firewall Manager network ACL policies work and provides guidance for using them.

- [Network ACL rules and tagging](https://docs.aws.amazon.com/waf/latest/developerguide/network-acls-fms-managed.html): Learn about the network ACL policy rule specifications and the network ACLs that are managed by Firewall Manager.
- [Initial network ACL management](https://docs.aws.amazon.com/waf/latest/developerguide/network-acls-initialization.html): Learn how Firewall Manager initiates network ACL management for a subnet.
- [Remediation for managed network ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/network-acls-remediation.html): Learn how Firewall Manager remediates its managed network ACLs when they're out of compliance with the policy.
- [Deleting a network ACL policy](https://docs.aws.amazon.com/waf/latest/developerguide/network-acls-deletion.html): Learn what happens in Firewall Manager when you delete a Firewall Manager network ACL policy.

### [Network Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/network-firewall-policies.html)

Learn how to use AWS Network Firewall policies in Firewall Manager.

- [Firewall endpoints](https://docs.aws.amazon.com/waf/latest/developerguide/fms-create-firewall-endpoints.html): Learn how creates Firewall Manager firewall endpoints.
- [Firewall subnets](https://docs.aws.amazon.com/waf/latest/developerguide/fms-manage-firewall-subnets.html): Learn how Firewall Manager manages your firewall subnets
- [Network Firewall resources](https://docs.aws.amazon.com/waf/latest/developerguide/fms-manage-network-firewall.html): Learn how Firewall Manager manages your Network Firewall resources
- [VPC route tables](https://docs.aws.amazon.com/waf/latest/developerguide/fms-manage-vpc-route-tables.html): Learn how Firewall Manager manages and monitors VPC route tables for your policy.
- [Configuring logging for an Network Firewall policy](https://docs.aws.amazon.com/waf/latest/developerguide/nwfw-policies-logging-config.html): Learn how you can enable centralized logging for your Network Firewall policies to get detailed information about traffic within your organization.

### [DNS Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/dns-firewall-policies.html)

This page describes how you can use AWS Firewall Manager DNS Firewall policies to manage associations between Amazon RouteÂ 53 Resolver DNS Firewall rule groups and your Amazon Virtual Private Cloud VPCs across your organization in AWS Organizations.

- [Deleting a rule group](https://docs.aws.amazon.com/waf/latest/developerguide/fms-delete-rule-group.html)
- [Palo Alto Networks Cloud NGFW policies](https://docs.aws.amazon.com/waf/latest/developerguide/cloud-ngfw-policies.html): The Palo Alto Networks Cloud Next Generation Firewall (NGFW) is a third-party firewall service that you can use for your AWS Firewall Manager policies.
- [Fortigate CNF policies](https://docs.aws.amazon.com/waf/latest/developerguide/fortigate-cnf-policies.html): Fortigate Cloud Native Firewall (CNF) as a Service is a third-party firewall service that you can use for your AWS Firewall Manager policies.
- [Resource sharing for Network Firewall and DNS Firewall policies](https://docs.aws.amazon.com/waf/latest/developerguide/resource-sharing.html): To manage Firewall Manager Network Firewall and DNS Firewall policies, you must enable resource sharing with AWS Organizations in AWS Resource Access Manager.

### [Using managed lists](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-managed-lists.html)

This section explains what managed lists are and how to use them.

- [Creating a custom managed list](https://docs.aws.amazon.com/waf/latest/developerguide/creating-managed-list.html): Create a new custom managed list.
- [Viewing a managed list](https://docs.aws.amazon.com/waf/latest/developerguide/viewing-managed-list.html): View the contents of a managed application list or protocol list.
- [Deleting a custom managed list](https://docs.aws.amazon.com/waf/latest/developerguide/deleting-custom-managed-list.html): Delete a custom managed application or protocol list.

### [Grouping your resources](https://docs.aws.amazon.com/waf/latest/developerguide/fms-resource-sets.html)

This section decribes what a resource set is and lists considerations for using resource sets.

- [Creating resource sets](https://docs.aws.amazon.com/waf/latest/developerguide/fms-creating-resource-set.html)
- [Deleting a resource set](https://docs.aws.amazon.com/waf/latest/developerguide/fms-deleting-resource-set.html): Before you can delete a resource set, the resource set must be disassociated from all policies using the resource set.
- [Viewing compliance for a policy](https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html): You can check the compliance status for accounts and resources that are in scope of an AWS Firewall Manager policy.

### [Firewall Manager integration with Security Hub CSPM](https://docs.aws.amazon.com/waf/latest/developerguide/fms-findings.html)

This page explains how to use Firewall Manager and Security Hub CSPM together.

- [AWS WAF policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/waf-policy-findings.html): AWS WAF Policy Findings
- [AWS Shield Advanced policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/shield-policy-findings.html): AWS Shield Advanced Policy Findings
- [Security group common policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-common-policy-findings.html): Security Group Common Policy Findings
- [Security group content audit policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-content-audit-policy-findings.html): Security Group Content Audit Policy Findings
- [Security group usage audit policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/security-group-usage-audit-policy-findings.html): Security Group Usage Audit Policy Findings
- [DNS Firewall policy findings](https://docs.aws.amazon.com/waf/latest/developerguide/dns-firewall-policy-findings.html): Amazon RouteÂ 53 Resolver DNS Firewall policy findings
- [AWS Config findings](https://docs.aws.amazon.com/waf/latest/developerguide/aws-config-firewall-manager-findings.html): AWS Config Firewall Manager findings

### [Security in your use of the Firewall Manager service](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security.html)

Configure Firewall Manager to meet your AWS security and compliance objectives, and learn how to use other AWS services that help you to secure your Firewall Manager resources.

- [Data protection](https://docs.aws.amazon.com/waf/latest/developerguide/fms-data-protection.html): Learn how the AWS shared responsibility model applies to data protection in Firewall Manager.

### [Identity and Access Management](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security-iam.html)

How to authenticate requests and manage access to your Firewall Manager resources.

- [How AWS Firewall Manager works with IAM](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security_iam_service-with-iam.html): Before you use IAM to manage access to Firewall Manager, learn what IAM features are available to use with Firewall Manager.
- [Identity-based policy examples](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Firewall Manager resources.
- [AWS managed policies](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security-iam-awsmanpol.html): Learn about AWS managed policies for Firewall Manager and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Firewall Manager and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/waf/latest/developerguide/fms-using-service-linked-roles.html): How to use service-linked roles to give Firewall Manager access to resources in your AWS account.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/waf/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Logging and monitoring](https://docs.aws.amazon.com/waf/latest/developerguide/fms-incident-response.html): Use AWS tools for monitoring and responding to events.
- [Compliance validation](https://docs.aws.amazon.com/waf/latest/developerguide/fms-security-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/waf/latest/developerguide/fms-disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as any specific Firewall Manager features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/waf/latest/developerguide/fms-infrastructure-security.html): Learn how AWS Firewall Manager isolates service traffic.
- [AWS Firewall Manager quotas](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html): AWS Firewall Manager is subject to the following quotas (formerly referred to as limits).
- [Migrating AWS WAF Classic Web ACLs in Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/migrate-waf-classic-fms.html): This section describes how to migrate AWS WAF Classic web ACLs that are managed by Firewall Manager to AWS WAF (v2) web ACLs.


## [Monitoring](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring_overview.html)

- [Monitoring tools](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring_automated_manual.html): Configure AWS tools to monitor AWS WAF and Shield Advanced.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html)

You can monitor web requests and web ACLs and rules using Amazon CloudWatch, which collects and processes raw data from AWS WAF and AWS Shield Advanced into readable, near real-time metrics.

- [Viewing metrics and dimensions](https://docs.aws.amazon.com/waf/latest/developerguide/metrics_dimensions.html): Metrics are grouped first by the service namespace, and then by the various dimension combinations within each namespace.
- [AWS WAF metrics and dimensions](https://docs.aws.amazon.com/waf/latest/developerguide/waf-metrics.html): AWS WAF reports metrics once a minute.
- [AWS Shield Advanced metrics](https://docs.aws.amazon.com/waf/latest/developerguide/shield-metrics.html): Shield Advanced publishes Amazon CloudWatch detection, mitigation, and top contributor metrics for all resources that it protects.
- [AWS Firewall Manager notifications](https://docs.aws.amazon.com/waf/latest/developerguide/set-fms-alarms.html): AWS Firewall Manager doesn't record metrics, so you can't create Amazon CloudWatch alarms specifically for Firewall Manager.

### [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/waf/latest/developerguide/logging-using-cloudtrail.html)

AWS WAF, AWS Shield Advanced, and AWS Firewall Manager are integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service.

- [AWS WAF information in AWS CloudTrail](https://docs.aws.amazon.com/waf/latest/developerguide/understanding-waf-entries.html): All AWS WAF actions are logged by AWS CloudTrail and are documented in the AWS WAF API Reference.
- [AWS Shield Advanced information in CloudTrail](https://docs.aws.amazon.com/waf/latest/developerguide/shield-info-in-cloudtrail.html): AWS Shield Advanced supports logging the following actions as events in CloudTrail log files:
- [AWS Firewall Manager information in CloudTrail](https://docs.aws.amazon.com/waf/latest/developerguide/cloudtrail-fms.html): AWS Firewall Manager supports logging the following actions as events in CloudTrail log files:


## [Using the AWS WAF and AWS Shield Advanced API](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-using.html)

- [Using the AWS SDKs](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-sdk.html): If you use a language that AWS provides an SDK for, use the SDK rather than trying to work your way through the APIs.
- [Making HTTPS requests to AWS WAF or Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-making-requests.html): AWS WAF and Shield Advanced requests are HTTPS requests, as defined by RFC 2616.
- [HTTP responses](https://docs.aws.amazon.com/waf/latest/developerguide/waf-api-making-requests-response.html): All AWS WAF and Shield Advanced API actions include JSON-formatted data in the response.
- [Authenticating requests](https://docs.aws.amazon.com/waf/latest/developerguide/authenticating-requests.html): If you use a language that AWS provides an SDK for, we recommend that you use the SDK.


## [Document history](https://docs.aws.amazon.com/waf/latest/developerguide/doc-history.html)

- [Updates before 2018](https://docs.aws.amazon.com/waf/latest/developerguide/doc-history-early-changes.html): The following table describes important changes in each release of the AWS WAF Developer Guide that were made before 2018.
