# Source: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/llms.txt

# Amazon WorkSpaces Secure Browser Administration Guide

- [Document history](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/doc-history.html)

## [What is Amazon WorkSpaces Secure Browser?](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-secure-browser.html)

- [Release history](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/version-history.html): On May 20, 2024, Amazon WorkSpaces Web was renamed to Amazon WorkSpaces Secure Browser.
- [Terms to know](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/terms.html): To help you get started with WorkSpaces Secure Browser, you should get familiar with the following concepts.
- [Related services](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/related-services.html): There are several AWS services that are related to WorkSpaces Secure Browser.
- [Architecture](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/architecture.html): The following diagram shows the architecture of WorkSpaces Secure Browser.
- [Access](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/accessing-servicename.html): You can access WorkSpaces Secure Browser in several ways.


## [Setting up](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/setting-up.html)

- [Signing up and creating a user](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started-signup.html)
- [Granting programmatic access](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started-iam-user-access-keys.html): Users need programmatic access if they want to interact with AWS outside of the AWS Management Console.

### [Networking](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/setup-vpc.html)

The following topics explain how to set up WorkSpaces Secure Browser streaming instances so that users can connect to them.

### [VPC setup](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/general-requirements.html)

To set up and configure a VPC for WorkSpaces Secure Browser complete the following steps.

- [VPC requirements](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-reqs.html): During WorkSpaces Secure Browser portal creation, you'll select a VPC in your account.

### [Creating a new VPC](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-vpc.html)

This section describes how to use the VPC wizard to quickly create a VPC with public and private subnets.

- [Quick VPC Setup](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-step1.html): Complete the following steps to quickly create a dedicated VPC for WorkSpaces Secure Browser with public and private subnets for internet access.
- [Subnet route tables](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-step2.html): The VPC wizard automatically configures the route tables for you.

### [Enabling internet browsing](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/internet-browsing.html)

You can choose to enable unrestricted internet browsing (the recommended option) or restricted internet browsing.

- [Unrestricted internet browsing](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/unrestricted-internet-browsing.html): Follow these steps to configure a VPC with a NAT gateway for unrestricted internet browsing.

### [Restricted internet browsing](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-internet-browsing.html)

The recommended network setup of a WorkSpaces Secure Browser portal is to use private subnets with NAT gateway, so that the portal can browse both public internet and private content.

- [Restricted internet browsing architecture](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-architecture.html): The following is an example of a typical proxy setup in your VPC.
- [Restricted internet browsing prerequisites](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-prerequisites.html): Before you get started, make sure that you meet the following prerequisites:
- [HTTP outbound proxy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-setup.html): To set up an HTTP outbound proxy for WorkSpaces Secure Browser, follow these steps.
- [Troubleshooting restricted internet browsing](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricted-troubleshooting.html): After Chrome policy is applied, if your WorkSpaces Secure Browser session still can't access the internet, follow these steps to try to resolve your issue:
- [Internet connectivity ports](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-connection.html): Each WorkSpaces Secure Browser streaming instance has a customer network interface that provides connectivity to the resources within your VPC, as well as to the internet if private subnets with NAT gateway are set up.
- [VPC best practices](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-setup-recommendations.html): The following recommendations can help you configure your VPC more effectively and securely.
- [Availability Zones](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html): When you are creating a virtual private cloud (VPC) for use with WorkSpaces Secure Browser, your VPC's subnets must reside in different Availability Zones in the Region where you're launching WorkSpaces Secure Browser.

### [User connections](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/client.html)

WorkSpaces Secure Browser is configured to route streaming connections over the public internet.

- [IP address and port requirements](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/address.html): To access WorkSpaces Secure Browser instances, user devices require outbound access on the following ports:
- [Allowed domains](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/allowed.html): For users to be able to access web portals from their local browser, you must add the following domains to the allow list on the network the user is trying to access the service from.


## [Getting started](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started.html)

### [Web portal creation](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started-step1.html)

Follow these steps to create a web portal.

- [Network settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/network-settings.html): To configuring network settings for WorkSpaces Secure Browser follow these steps.
- [Portal settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/portal-settings.html): On the Step 2: Configure web portal settings page, complete the following steps to customize your users' browsing experience when they start a session.
- [User settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-settings.html): On the Step 3: Select user settings page, complete the following steps to choose which features your users can access from the top navigation bar during their session, and then choose Next:

### [Identity provider configuration](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/identity-settings.html)

Use the following steps to configure your identity provider (IdP).

### [Choose identity provider type](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/choose-type.html)

WorkSpaces Secure Browser offers two authentication types: Standard and AWS IAM Identity Center.

### [Standard authentication type](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-standard.html)

The standard authentication type is the default authentication type.

- [IdP configuration on WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-idp-step1.html): Complete the following steps to configure your identity provider:
- [IdP configuration on your IdP](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-idp-step2.html): To configure your IdP on your own IdP, follow these steps.
- [Finishing IdP configuration on WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/upload-metadata.html): To finish IdP configuration on WorkSpaces Secure Browser follow these steps.
- [Guidance for specific IdPs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/idp-guidance.html): To make sure you correctly configure the SAML federation for your portal, see the links below for documentation from commonly used IdPs.

### [IAM Identity Center authentication type](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-iam.html)

For the IAM Identity Center type (advanced), you federate IAM Identity Center with your portal.

- [Creating a web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/web-portal-IAM.html): To create a web portal with IAM Identity Center, follow these steps.
- [Managing your web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/manage-IAM.html): To manage your web portal with IAM Identity Center, follow these steps.
- [Adding additional users and groups](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/add-users-groups.html): To add additional users and groups to an existing web portal, follow these steps.
- [Viewing or removing users and groups](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/remove-users-groups.html): To view or remove users and groups for your web portal, use the actions available in the Assigned users table.
- [Change identity provider type](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/change-type.html): You can change the authentication type of your portal at any time.
- [Launch](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/review-settings.html): When you are finished configuring your web portal, you can follow these steps to launch it.
- [Web portal testing](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started-step2.html): After you create a web portal, you can sign into the WorkSpaces Secure Browser endpoint to browse your connected websites as an end user would.
- [Web portal distribution](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/getting-started-step3.html): When you are ready for your users to begin using WorkSpaces Secure Browser, you choose from the following options to distribute the portal:


## [Managing your web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/managing-web-portals.html)

- [Viewing web portal details](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/view-portal-details.html): To view web portal details, follow these steps.
- [Editing a web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/edit-portals.html): To edit a web portal, follow these steps.
- [Deleting a web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/delete-portals.html): To delete a web portal, follow these steps.

### [Managing service quotas](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/request-service-quota.html)

When you create your AWS account, we automatically set default service quotas (also referred to as limits) for resource usage with AWS services.

- [Requesting a service quota increase](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/quota-increase.html): To request a service quota increase follow these steps.
- [Requesting a portal increase](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/request-portal-increase.html): A portal is the serviceâs foundational resource.
- [Requesting a maximum concurrent sessions increase](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/request-max-concurrent-session.html): The maximum concurrent sessions quota is the highest amount of users that can be connected at the same time to a portal.
- [Limit example](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/limit-example.html): As an example, assume an administrator is configuring two web portals in US East (N.
- [Other service quotas](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/other-quotas.html): You can view and request increases for other quotas listed on the Service Quotas page.
- [Re-authenticating a SAML IdP token](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/control-interval.html): When a user visits a WorkSpaces Secure Browser portal, they can sign in to launch a streaming session.

### [Setting up user activity logging](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-logging.html)

WorkSpaces Secure Browser offers two options for logging user activity and security-related events:

- [Setting up Session Logger](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-logger.html)
- [Setting up User Access logging](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-access-logging.html): To activate user access logging in the WorkSpaces Secure Browser console, under User access logging, select the Kinesis Stream ID that you want to use to receive data.

### [Managing browser policy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/browser-policies.html)

You can set any custom browser policy using Chrome policies available for the latest stable version to WorkSpaces Secure Browser.

- [Tutorial: Setting a custom browser policy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/browser-policies-custom.html): You can set any supported Chrome policy for Linux by uploading a JSON file.
- [Editing the baseline browser policy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/browser-policies-baseline.html): In order to deliver the service, WorkSpaces Secure Browser applies a baseline browser policy to all portals.
- [Configuring the Input Method Editor](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/input-method-editor.html): An Input Method Editor (IME) is a utility that provides options to the end user to input text in languages that use a keyboard layout other than a QWERTY keyboard.

### [Configuring in-session localization](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-loc.html)

When a user starts a session, WorkSpaces Secure Browser detects the userâs local browser language and time zone settings and applies them to the session.

- [Supported language codes](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/language-codes.html): The following list shows the language codes currently supported by WorkSpaces Secure Browser.
- [User browser settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/local-browser-settings.html): To set a user's local browser settings, follow the appropriate steps.

### [Managing IP access controls](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/ip-access-controls.html)

- [Creating an IP access control group](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-ip-access-controls.html)
- [Associating an IP access setting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/associate-ip-access-controls.html)
- [Editing an IP access control group](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/edit-ip-access-controls.html): You can delete a rule from an IP access setting at any time.
- [Deleting an IP access control group](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/delete-ip-access-controls.html): You can delete a rule from an IP access control group at any time.

### [Managing the single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/allow-extension.html)

You can enable an extension for your end users to have a better portal sign-on experience.

- [Identifying domains for the single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/identify-domains.html): First, determine which domains you need for your SAML IdP and websites.
- [Adding the single sign-on extension to a new web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension-new.html): To allow the extension when creating a new web portal, follow these steps.
- [Adding the single sign-on extension to an existing web portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension-existing.html): To add the extension to an existing web portal, follow these steps.
- [Editing or removing the single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/remove-extension.html): To edit domains or remove the extension, follow these steps.

### [Web content filtering](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/web-content-filtering.html)

Web Content Filtering is a security and compliance feature that enables your organization to define policies and regulate content access within WorkSpaces Secure Browser.

- [Restricting browsing to specific URLs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/restricting-browsing.html): You can implement a "default deny" policy where only explicitly approved websites and URLs are accessible.
- [Blocking specific URLs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/blocking-specific-urls.html): You can balance security with productivity by maintaining open internet access while blocking known problematic sites.
- [Blocking categories](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/blocking-categories.html): In addition to blocking specific URLs, you can also automatically block groups of URLs based on content categories.
- [Example of URLs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/example-urls.html): The following types of URLs can be provided in the AllowedUrls or BlockedUrls
- [Transferring Chrome policies](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/transferring-chrome-policies.html): In case you already have Chrome policies set up to allow or block specific domains, we recommend that you transfer them to the Web Content Filtering feature.

### [Deep links](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/deep-links.html)

When a user signs into WorkSpaces Secure Browser, they start the session on a home page set by the administrator.

- [Setting up deep links](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/add-deep-links.html): To allow permission for deep links, choose Allowed when creating user settings.
- [Using URL filtering for deep links](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/filtering-deep-links.html): Any user you share this portal link with can manipulate the deep link value to visit a website, if that domain is reachable from the portal and not on the URL blocklist.
- [Session management dashboard](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-management.html): Use the session management dashboard on your WorkSpaces Secure Browser console to monitor and manage active and complete sessions.
- [Protecting data in transit](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/fips-endpoints.html): By default, when you communicate with the WorkSpaces Secure Browser service as an administrator using the console, the AWS Command Line Interface (AWS CLI), or an AWS SDK, or during a userâs session, all data in transit is encrypted using TLS 1.2.

### [Data protection settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/data-protection-settings.html)

Data Protection Settings are used to help protect data from being shared during a session.

- [Inline data redaction](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/inline-data-redaction.html): By adding inline data redaction to a portal, you can automatically predict and redact certain data from a string of text displayed in web pages.
- [Default redaction configuration](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/default-redaction-configuration.html): The default redaction configuration will automatically apply a confidence level and URL enforcement for all built-in data types in the data protection settings.
- [Base inline redaction](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/base-inline-redaction.html): Inline data redaction has support for built-in patterns (such as social security numbers and credit card numbers), which you can find listed under Base inline redaction.
- [Custom inline redaction](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/custom-inline-redaction.html): Customers can define their own patterns using regular expression, such as custom internal application IDs.
- [Create data protection settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-data-protection-settings.html): You can create data protection settings in WorkSpaces Secure Browser.
- [Associate data protection settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/associate-data-protection-settings.html): You can associate data protection settings in WorkSpaces Secure Browser.
- [Edit data protection settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/edit-data-protection-settings.html): You can edit data protection settings in WorkSpaces Secure Browser.
- [Delete data protection settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/delete-data-protection-settings.html): You can delete data protection settings in WorkSpaces Secure Browser.

### [Branding customization](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/branding-customization.html)

You can customize the sign-in and loading screens that appear to your end users by modifying visual elements, text content, and terms of service.

- [Configuring branding customization for your portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-branding-customization.html)
- [Customization guidelines](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/customization-guideline.html): Customize the sign-in and loading experience for your end users by updating the branding elements and text on sign-in and loading pages.

### [Web authentication redirection](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/web-authentication.html)

- [Enable WebAuthn redirection in portal settings](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/enable-webauthn-portal.html): To enable WebAuthn redirection for websites accessed within the remote browser session, follow these steps.
- [Configure local browser policy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-local-browser-policy.html): In addition to enabling WebAuthn redirection in your portal settings, the local browser policy must be configured to allow WebAuthn redirection between the user's local device and the remote browser session and vice versa.
- [WebAuthn redirection usage](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/webauthn-usage.html): Once WebAuthn redirection is enabled in the portal settings and the local browser policy is configured, users can use WebAuthn authentication on websites within their WorkSpaces Secure Browser remote browser sessions.

### [WebAuthn redirection troubleshooting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/webauthn-troubleshooting.html)

If users experience issues with WebAuthn redirection in their remote browser sessions, use the following troubleshooting steps to identify and resolve common problems.

- [WebAuthn redirection not working](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/webauthn-not-working.html): If WebAuthn authentication prompts do not appear or fail to work:
- [Common error messages](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/common-error-messages.html): The following are common error messages and their resolutions:
- [Toolbar controls](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/toolbar-controls.html): With Toolbar controls, you can configure the toolbar presentation for end user sessions, including the following options:

### [Custom domain](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/custom-domains.html)

You can configure a custom domain for a WorkSpaces Secure Browser portal to enable access through your own domain name instead of the default portal URL.

- [Configuring custom domain for your portal](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/configure-custom-domains.html)

### [Custom domain troubleshooting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/custom-domains-troubleshooting.html)

If users experience issues with portal access through custom domain in their remote browser sessions, use the following troubleshooting steps to identify and resolve common problems.

- [Common error messages](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/common-errors.html): The following are common error messages and their resolutions when setting up custom domains:


## [Security](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security.html)

### [Data protection](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon WorkSpaces Secure Browser.

### [Data encryption](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/data-encryption.html)

Amazon WorkSpaces Secure Browser collects portal customization data, such as browser settings, user settings, network settings, identity provider information, trust store data, and trust store certificate data.

- [Encryption at rest](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/encryption-rest.html): Encryption at rest is configured by default and all customer data (for example, browser policy statements, usernames, logging, or IP addresses) used in WorkSpaces Secure Browser is encrypted using AWS KMS.
- [Encryption in transit](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/encryption-transit.html): WorkSpaces Secure Browser encrypts data in transit over HTTPS and TLS 1.2.
- [Key management](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/key-management.html): You can supply your own Customer Managed AWS KMS Key to encrypt your customer information.
- [Inter-network traffic privacy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/inter-network-traffic-privacy.html): To secure connections between WorkSpaces Secure Browser and on-premise applications, you use WorkSpaces Secure Browser to launch browser sessions inside of your own VPC.
- [User access logging](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/data-protection-logging.html): Administrators are able to record WorkSpaces Secure Browser session events, including start, stop, and URL visits.

### [Identity and Access Management](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam.html)

How to authenticate requests and manage access your WorkSpaces Secure Browser resources.

### [How Amazon WorkSpaces Secure Browser works with IAM](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam.html)

Before you use IAM to manage access to WorkSpaces Secure Browser, learn what IAM features are available to use with WorkSpaces Secure Browser.

- [Identity-based policies](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-id-based-policies.html): Supports identity-based policies: Yes
- [Resource-based policies](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-resource-based-policies.html): Supports resource-based policies: No
- [Policy actions](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-id-based-policies-actions.html): Supports policy actions: Yes
- [Policy resources](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-id-based-policies-resources.html): Supports policy resources: Yes
- [Policy condition keys](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-id-based-policies-conditionkeys.html): Supports service-specific policy condition keys: Yes
- [ACLs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-acls.html): Supports ACLs: No
- [ABAC](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-tags.html): Supports ABAC (tags in policies): Partial
- [Temporary credentials](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-roles-tempcreds.html): Supports temporary credentials: Yes
- [Principal permissions](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-principal-permissions.html): Supports forward access sessions (FAS): Yes
- [Service roles](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-roles-service.html): Supports service roles: No
- [Service-linked roles](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-roles-service-linked.html): Supports service-linked roles: Yes

### [Identity-based policy examples](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_id-based-policy-examples.html)

By default, users and roles don't have permission to create or modify WorkSpaces Secure Browser resources.

- [Policy best practices](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_service-with-iam-policy-best-practices.html): Identity-based policies determine whether someone can create, access, or delete WorkSpaces Secure Browser resources in your account.
- [Using the console](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_id-based-policy-examples-console.html): To access the Amazon WorkSpaces Secure Browser console, you must have a minimum set of permissions.
- [Allowing users to view their own permissions](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_id-based-policy-examples-view-own-permissions.html): This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity.

### [AWS managed policies](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam-awsmanpol.html)

Learn about AWS managed policies for WorkSpaces Secure Browser and recent changes to those policies.

- [AmazonWorkSpacesWebServiceRolePolicy](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam-awsmanpol-AmazonWorkSpacesWebServiceRolePolicy.html)
- [AmazonWorkSpacesSecureBrowserReadOnly](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam-awsmanpol-AmazonWorkSpacesSecureBrowserReadOnly.html)
- [AmazonWorkSpacesWebReadOnly](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam-awsmanpol-AmazonWorkSpacesWebReadOnly.html)
- [Policy updates](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-iam-awsmanpol-updates.html)

### [Troubleshooting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_troubleshoot.html)

Use the following information to help you diagnose and fix common issues that you might encounter when working with WorkSpaces Secure Browser and IAM.

- [I am not authorized to perform an action in WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_troubleshoot-no-permissions.html): If you receive an error that you're not authorized to perform an action, your policies must be updated to allow you to perform the action.
- [I am not authorized to perform iam:PassRole](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_troubleshoot-passrole.html): If you receive an error that you're not authorized to perform the iam:PassRole action, your policies must be updated to allow you to pass a role to WorkSpaces Secure Browser.
- [I want to allow people outside of my AWS account to access my WorkSpaces Secure Browser resources](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security_iam_troubleshoot-cross-account-access.html): You can create a role that users in other accounts or people outside of your organization can use to access your resources.

### [Using service-linked roles](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/using-service-linked-roles.html)

How to use service-linked roles to give WorkSpaces Secure Browser access to resources in your AWS account.

- [Service-linked role permissions](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/slr-permissions.html): WorkSpaces Secure Browser uses the service-linked role named AWSServiceRoleForAmazonWorkSpacesWeb â WorkSpaces Secure Browser uses this service-linked role to access Amazon EC2 resources of customer accounts for streaming instances and CloudWatch metrics.
- [Creating a service-linked role](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-slr.html): You don't need to manually create a service-linked role.
- [Editing a service-linked role](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/edit-slr.html): WorkSpaces Secure Browser doesn't allow you to edit the AWSServiceRoleForAmazonWorkSpacesWeb service-linked role.
- [Deleting a service-linked role](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/delete-slr.html): If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
- [Supported regions](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/slr-regions.html): WorkSpaces Secure Browser supports using service-linked roles in all of the regions where the service is available.
- [Incident response](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/incident-response.html): Learn about incident response in Amazon WorkSpaces Secure Browser.
- [Compliance validation](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon WorkSpaces Secure Browser features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/infrastructure-security.html): Learn how Amazon WorkSpaces Secure Browser isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vulnerability-analysis-and-management.html): Learn how Amazon WorkSpaces Secure Browser handles configuration and vulnerability analysis.

### [Interface VPC endpoint (AWS PrivateLink)](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/private-link.html)

Directly call Amazon WorkSpaces Secure Browser API endpoint from within a private cloud (VPC) instead of connecting over the internet.

- [Considerations for Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-endpoint-considerations.html): Before you set up an interface VPC endpoint for Amazon WorkSpaces Secure Browser APIs, make sure to review the "Prerequisites" in Access AWS services through AWS PrivateLink.
- [Creating an interface VPC endpoint for Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-endpoint-create.html): You can create an interface VPC endpoint for the Amazon WorkSpaces Secure Browser service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI).
- [Creating an endpoint policy for your interface VPC endpoint](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/vpc-endpoint-policy.html): An endpoint policy is an IAM resource that you can attach to an interface VPC endpoint.
- [Troubleshooting](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/privatelink-troubleshooting.html): If your calls to the Amazon WorkSpaces Secure Browser APIs are hanging, there is likely a misconfiguration in your VPC Endpoint Service security group or IAM role setup.
- [Security best practices](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/security-best-practices.html): Security best practices for Amazon WorkSpaces Secure Browser.


## [Monitoring](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-cloudwatch.html): You can monitor Amazon WorkSpaces Secure Browser using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

### [CloudTrail logs](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/logging-using-cloudtrail.html)

Learn about logging WorkSpaces Secure Browser with AWS CloudTrail.

- [Information in CloudTrail](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/service-name-info-in-cloudtrail.html): CloudTrail is enabled on your AWS account when you create the account.
- [Log file entries](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/understanding-service-name-entries.html): A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

### [User activity logging](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/monitoring-logging.html)

Amazon WorkSpaces Secure Browser enables customers to log session events related to user activities in the Secure browser sessions.

- [Session events in Session Logger](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-events-session-logger.html): Session Logger captures various session-related events for monitoring and auditing purposes.
- [Session events in User Access logging](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-events-logging.html): The following session events are available for User Acess logging:


## [User guidance](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-guide.html)

- [Browser and device compatibility](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/browser-device-compatibility.html): Amazon WorkSpaces Secure Browser is powered by the Amazon DCV web browser client, which runs inside a web browser, so no installation is required.
- [Web portal access](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-access.html): Your administrator can provide access to your web portal with the following options:

### [Session guidance](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/session-guidance.html)

After you sign into the web portal, you can launch a session and perform various actions during your session.

- [Starting a session](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/start-session.html): After you sign in to launch a session, you will see the Launching session message and progress bar.
- [Using the toolbar](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/use-toolbar.html): To learn how to use the toolbar, follow these steps.
- [Using the browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/use-browser.html): When you start your session, the browser displays the Startup URL, which is a URL chosen by your administrator.
- [Ending a session](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/end-session.html): To end a session, choose Profile and End session.
- [Troubleshooting user issues](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-troubleshooting.html): If you encounter any of the following issues while using WorkSpaces Secure Browser, try the following resolutions.

### [Single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension.html)

Amazon WorkSpaces Secure Browser offers an extension for single sign-on with Chrome and Firefox browsers on desktop computers.

- [Single sign-on extension compatibility](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension-compatibility.html): The single sign-on extension works with the following devices and browsers:
- [Installing the single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension-install.html): To install the single sign-on extension, follow these steps.
- [Troubleshooting the single sign-on extension](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/extension-troubleshooting.html): While using the single sign-on extension, you might encounter the following issue.
