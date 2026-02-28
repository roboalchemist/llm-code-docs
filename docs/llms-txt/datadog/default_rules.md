# Source: https://docs.datadoghq.com/security/default_rules.md

---
title: OOTB Rules
description: Datadog Security detection rules
breadcrumbs: Docs > Datadog Security > OOTB Rules
---

# OOTB Rules

Datadog provides out-of-the-box (OOTB) [detection rules](https://docs.datadoghq.com/security/detection_rules/) to flag attacker techniques and potential misconfigurations so you can immediately take steps to remediate. Datadog continuously develops new default rules, which are automatically imported into your account, your App and API Protection library, and the Agent, depending on your configuration.

{% alert level="info" %}
Datadog's Security Research team continuously adds new OOTB security detection rules. While the aim is to deliver high-quality detections with the release of integrations or other new features, the performance of these detections at scale often needs to be observed before making the rule generally available. These rules contain a Beta tag. This gives Datadog's Security Research team time to either refine or deprecate detection opportunities that do not meet Datadog's standards.
{% /alert %}

Click the following buttons to filter the detection rules. Security detection rules are available for:

- [App and API Protection](https://docs.datadoghq.com/security/application_security/)
- [Cloud SIEM](https://docs.datadoghq.com/security/cloud_siem/) (log detection and signal correlation)
- [Cloud Security Misconfigurations](https://docs.datadoghq.com/security/cloud_security_management/misconfigurations/) (cloud and infrastructure)Important alert (level: info): In Cloud Security, rules with the **infrastructure** label are applicable to Agent installations.
- [Workload Protection](https://docs.datadoghq.com/security/workload_protection/)
- [Cloud Security Identity Risks](https://docs.datadoghq.com/security/cloud_security_management/identity_risks/)
- [Attack Paths](https://docs.datadoghq.com/security/security_inbox/?s=attack%20path#types-of-findings-in-security-inbox)
1password
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 1Password activity observed from Tor client IP 1Password service account token activity observed 1Password vault export attempt by user Anomalous amount of failed sign-in attempts by 1Password user Attempt to exfiltrate a 1Password item by user Attempt to modify a 1Password item by user Impossible travel event observed from 1Password user Unusual 1Password device authorization activity Unusual 1Password item usage action observed from userAbnormal Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Email with malicious attachment opened by user Email with spam category opened by user Login attempt from new location detected Potential brute force attack detectedACM
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Certificate managed by ACM should be renewed within 30 days of expiration Certificate managed by ACM should be renewed within 7 days Certificate managed by ACM should not be expired Certificates managed by ACM should be validated RSA certificates managed by AWS ACM should use a key length of at least 2,048 bitsAcmpca
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS Private CA root certificate authority should be disabledAmazon Backup
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Backup recovery points should be encrypted at restAmazon Dms
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> DMS replication instances should not be publicAmazon Ec2
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EBS default encryption should be enabled EC2 launch templates should not configure network interfaces with public IPsAmazon Efs
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EFS access points should enforce a root directory EFS access points should enforce a user identity EFS data should be encrypted at rest EFS file systems should be in backup plansAmazon Emr
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EMR block public access setting should be enabledAmazon Event Bridge
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EventBridge custom event buses should have a resource-based policy attachedAmazon Fsx
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS FSx Excessive File DeniedAmazon Msk
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> MSK clusters should be encrypted in transit among broker nodesAmazon Network Firewall
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Network Firewall firewalls should have deletion protection enabled Network Firewall logging should be enabled Network Firewall policies should have at least one associated rule group Network Firewall policy default stateless action for fragmented packets should be drop or forward Network Firewall policy default stateless action for full packets should be drop or forward Network Firewall stateless rule groups should not be emptyAmazon Step Functions
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Step Functions state machines should have logging turned onAmazon Vpc
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> VPC flow logging should be enabled in all VPCsAmazon Workspaces
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Amazon Workspaces should enable volume encryptionApache
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Apache HTTP requests from security scannerAPI Gateway
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> API Gateway access logging should be enabled for V2 API stages API Gateway execution logging should be enabled for REST APIs API Gateway execution logging should be enabled for WebSocket APIs API Gateway REST API cache data should be encrypted at rest API Gateway REST API stages should be configured to use SSL certificates for backend authentication API Gateway routes should specify an authorization type API Gateway stage REST API should have AWS X-Ray tracing enabled API Gateways should be associated with a WAF Web ACLAPI Findings
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Admin endpoint without authentication Authenticated route returns sensitive data Authenticated route returns sensitive data using predictable IDs Authenticated route use expensive APIs without rate limiting Authentication route is not protected by AAP's ATO Detection Authentication route use Basic Auth Authentication route without HTTPS Endpoint exposes stack trace errors Improper collection of metadata on login requests Missing Access-Control-Allow-Origin HTTP header Missing Content Type HTTP header Missing Content-Security-Policy HTTP header Missing Referrer-Policy Security HTTP header Missing Strict Transport Security HTTP header Missing X-Frame-Options HTTP header Private endpoint lacks assigned owner Public endpoint exposes stack trace errors Public endpoint has no defined schema Public endpoint lacks assigned owner Read operation on route use predictable IDs Route processes payments without HTTPS Route returns non-sensitive PII data without HTTPS Route returns non-sensitive PII data without rate limit Route returns non-sensitive PII without setting Cache-Control HTTP header Route returns PCI regulated data without HTTPS Route returns PCI regulated data without setting Cache-Control HTTP header Route returns sensitive PII data without HTTPS Route returns sensitive PII data without rate limit Route returns sensitive PII without setting Cache-Control HTTP header Route uses expensive APIs without rate limiting Route uses HTTP to connect to external APIs Route vulnerable to Server-Side Request Forgery (SSRF) Service exposes publicly debugging endpoints Unauthenticated route is used to invite users Unauthenticated route processes payments Unauthenticated route returns non-sensitive PII data Unauthenticated route returns PCI regulated data Unauthenticated route returns sensitive data using predictable IDs Unauthenticated route returns sensitive PII Unauthenticated route use expensive APIs Unauthenticated route use predictable IDs Unauthenticated route with SQL injection vulnerability Unauthenticated route without rate limit Unauthenticated route write using predictable IDs Unwanted HTTP header in response User preferences endpoint without HTTPS User signup endpoint without HTTPS Write operation on route use predictable IDsApplication Threats
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> API scan detected on service Attack Tool Bruteforce attack Cassandra injection vulnerability triggered Command injection attempt detected Command injection exploited Commercial vulnerability scanner CQL injections attempts Credential Stuffing attack Distributed Credential Stuffing campaign (attacker fingerprint) Distributed Credential Stuffing campaign (attempt count) Distributed Credential Stuffing campaign (user count) Excessive account deletion from an IP Excessive payment failures from IP Excessive resource consumption of third-party API Excessive sensitive activity from an IP (SDK instrumented) Excessive sensitive activity from an IP (WAF instrumented) Feature returning private information abused by IP Impossible travel observed from business logic event Java code injections attempts JWT authentication bypass attempt Local File Inclusion (LFI) attack attempts Local file inclusion exploited Log4shell RCE attempts - CVE-2021-44228 Log4shell vulnerability triggered (RCE) - CVE-2021-44228 Mongo injections attempts OGNL injection attack attempts on routes parsing OGNL Password reset token bruteforce Reflected XSS attempts on routes returning HTML Resource enumeration detected Security scanner detected Spring4shell RCE attempts - CVE-2022-22963 SQL injection exploited SQL injections attempts SSRF attempts on routes executing network queries SSRF exploited Unauthenticated activity detected Unauthorized activity detected Unusual account creations from an IP Unusual password reset rate activity User activity detected from outside authorized countries User activity detected from unauthorized countries User activity from Tor User enumeration through password reset User has changed country User has used a disposable email addressAppsync
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AppSync GraphQL APIs should have field-level logging enabled AppSync GraphQL APIs should not use API keys for authenticationAsana
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Asana brute force attempt BETA Asana content export initiated by user BETA Asana impossible travel detected BETA Asana role change to admin or super-admin detected BETA Asana user multi-factor authentication method disabledAthena
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Athena workgroups should have logging enabledAtlassian Event Logs
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Atlassian administrative API token activity observed Atlassian administrator impersonated user Atlassian user added to administrative group Atlassian user added to organization administrative group Atlassian user invited to organization as an organization administratorAuth0
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Anomalous number of Auth0 Attack Protection events Auth0 breached password detection disabled Auth0 brute-force protection disabled Auth0 Guardian MFA push notifications rejected by user Auth0 Guardian MFA push notifications rejected by user followed by successful login Auth0 suspicious IP throttling disabled Auth0 tenant invitation sent to user Auth0 user logged in with a breached password Brute force attack on an Auth0 user Credential stuffing attack on Auth0 Impossible Travel Auth0 loginAutoscaling Group
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Auto Scaling group launch configuration should configure EC2 instances to require IMDSv2 Auto Scaling group launch configuration should not assign public IP addresses Auto Scaling groups associated with a Classic Load Balancer should use ELB health checks Auto Scaling groups should use multiple instance types across multiple Availability Zones EC2 Auto Scaling group should use multiple Availability Zones EC2 Auto Scaling groups should use Amazon EC2 launch templatesAWS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS Verified Access anomalous failed authentication attempts by host AWS Verified Access anomalous failed authentication attempts by IP AWS Verified Access anomalous failed authentication attempts by user Bedrock model invocation logging should be enabled and stored in restricted-access S3 buckets Brute forced ConsoleLogin event correlates with an assumed role event ConsoleLogin event correlates privileged policy applying to a roleAWS Logging Log Metric
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 'root' account access should be monitored AWS Config configuration changes should be monitored AWS Management Console authentication failures should be monitored AWS Management Console sign-ins without MFA should be monitored AWS Organizations changes should be monitored CloudTrail configuration changes should be monitored Disabling or deletion of Customer-Managed Keys should be monitored IAM policy changes should be monitored Network ACL changes should be monitored Network gateway changes should be monitored Route table changes should be monitored S3 bucket policy changes should be monitored Security group changes should be monitored Unauthorized API calls should be monitored VPC changes should be monitoredAWS Iam
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS accounts should be configured with security contact informationAzure
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure Active Directory risky sign-in Azure AD brute force login Azure AD escalation from Global Administrator to User Access Administrator Azure AD Identity Protection risky user Azure AD member assigned built-in Administrator role Azure AD member assigned Global Administrator role Azure AD MFA disabled Azure AD new verified domain added to tenant Azure AD possible MFA fatigue attack Azure AD possible MFA fatigue attack followed by successful login Azure AD Privileged Identity Management member assigned Azure AD sign in from AADinternals default user agent Azure AD sign in from AzureHound default user agent BETA Azure administrative unit created BETA Azure administrative unit modified BETA Azure AI API keys listed from previously unseen application BETA Azure AI API keys listed outside of known AI web portals BETA Azure AI models listed directly through API BETA Azure AI service high volume of chat requests BETA Azure Bastion shareable link created Azure Datadog Log Forwarder Deleted Azure diagnostic setting deleted or disabled Azure disk export URI created Azure Firewall Threat Intelligence Alert Azure Frontdoor WAF Blocked a Request Azure Frontdoor WAF Logged a Request Azure Function has administrative privileges over resources Azure group has access to a large number of resources Azure group has administrative privileges over resources Azure group has dangerous key vault role Azure Login Explicitly Denied MFA Azure managed identity has a large permissions gap Azure managed identity has access to a large number of resources Azure managed identity has administrative privileges over resources Azure managed identity has dangerous key vault role Azure Network Security Group Open to the World Azure Network Security Groups or Rules Created, Modified, or Deleted Azure new owner added for service principal Azure New Owner added to Azure Active Directory application Azure New Service Principal created Azure Policy Assignment Created BETA Azure restricted management administrative unit created Azure Service Principal was assigned a role Azure snapshot export URI created Azure SQL Server Firewall Rules Created or Modified BETA Azure user added to restricted management administrative unit BETA Azure user granted scoped role assignment over administrative unit Azure user has a large permissions gap Azure user has access to a large number of resources Azure user has administrative privileges over resources Azure user has dangerous key vault role Azure user invited an external user Azure user ran command on container instance BETA Azure user removed from restricted administrative unit Azure user viewed CosmosDB access keys Azure user viewed CosmosDB connection string Azure Virtual Machine instance has administrative privileges over resources Brute-forced user has assigned a role Credential added to Azure AD application Credential added to rarely used Azure AD application Credential Stuffing Attack on Azure Ensure that Azure Databricks is deployed in a customer-managed virtual network (VNet) Ensure that data at rest and in transit is encrypted in Azure Databricks using customer managed keys (CMK) Microsoft 365 - Modification of Trusted Domain Potential Illicit Consent Grant attack via Azure registered application Tor client IP address identified within Azure environment User ran a command on Azure ComputeAzure.active Directory
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure custom administrator roles should be disabledAzure.activity Log
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 'Create or Update Network Security Group' activity log alert should be configured 'Create or Update Public Ip Address' activity log alert should be configured 'Create or Update Security Solutions' activity log alert should be configured 'Create or Update SQL Server Firewall Rule' activity log alert should be configured 'Create Policy Assignment' activity log alert should be configured 'Delete Network Security Group' activity log alert should be configured 'Delete Policy Assignment' activity log alert should be configured 'Delete Public Ip Address Rule' activity log alert should be configured 'Delete Security Solution' activity log alert should be configured 'Delete SQL Server Firewall Rule' activity log alert should be configured 'Service Health' activity log alert should be configured Account should have a activity log alert configured for 'Create or Update Network Security Group' Account should have a activity log alert configured for 'Delete Load Balancer' Account should have a activity log alert configured for 'Delete Storage Accounts' Account should have a activity log alert configured for creating or updating storage accounts Account should have a activity log alert configured for creating or updating virtual machines Account should have a activity log alert configured for deallocating virtual machines Account should have a configured activity log alert for 'Delete Key Vault' Account should have a configured activity log alert for 'Delete MySQL Database' Account should have a configured activity log alert for 'Delete PostgreSQL Database' Account should have a configured activity log alert for 'Rename Azure SQL Database' Account should have a configured activity log alert for 'Update Key Vault' Account should have a configured activity log alert for 'Update Security Policy' Account should have a configured activity log alert for deleting Network Security Group Account should have a configured activity log alert for deleting policy assignments Account should have a configured activity log alert for deleting the SQL Server firewall rule Account should have a configured activity log alert for deleting VMs Account should have a configured activity log alert for load balancer updates Account should have a configured activity log alert for mysql database updates Account should have a configured activity log alert for PostgreSQL database updates Account should have a configured activity log alert for power off events Account should have a configured activity log alert for security solutions creation or updates Account should have a configured activity log alert for sql database updates The account should have a configured activity log alert for firewall rule creation or update The user should configure an activity log alert for SQL Database deletionAzure.app Services
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> App Service should use the latest version of TLS encryption Azure App Service should have authentication enabled Azure should use the latest HTTP version available Azure should use the latest Java version available Azure should use the latest Python version available FTP deployments should be disabled Incoming client certificates should be required to be 'On' The app service should enable registration with Azure Active Directory The Azure App Service should be enabled with 'always on' The web app should redirect all HTTP traffic to HTTPSAzure.appservice
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure App Service should have remote debugging disabledAzure.compute
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 'OS and Data' disks should be encrypted with Customer Managed Key (CMK) 'Unattached disks' should be encrypted with Customer Managed Key (CMK) Privileged Azure Entra user is a guest account Privileged Azure Entra user is synced from on-premises AD Publicly accessible Azure VM contains critical vulnerabilities found in CISA KEV with greater than 15 days exposure time Publicly accessible Azure VM contains critical vulnerabilities which have exploits available with greater than 30 days exposure time Publicly accessible Azure VM contains critical vulnerabilities with greater than 30 days exposure time Publicly accessible Azure VM contains high vulnerabilities with greater than 60 days exposure time Publicly accessible Azure VM has privileged role and password-based SSH authentication Publicly accessible Azure VM instance contains critical vulnerability CVE-2024-3094 (RCE in liblzma and xz versions 5.6.0 and 5.6.1) Publicly Accessible Azure VM instance has a critical vulnerability Publicly Accessible Azure VM instance has a privileged service account and a critical vulnerability Publicly accessible Azure VM uses password-based SSH authentication Publicly accessible Azure VM with privileged service account contains critical vulnerabilities with greater than 30 days exposure time Virtual machines in Azure should use SSH authentication keys for security Virtual Machines should utilize Azure Managed DisksAzure.container Registry
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure Container registries should use private linkAzure.db For Mysql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SSL connection on MySQL Database Server should be enabled TLS Version should be set to 'TLSV1.2' for MySQL flexible Database ServerAzure.db For Postgresql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Access to Azure services for PostgreSQL Database Server should be disabled Infrastructure double encryption for PostgreSQL Database Server should be enabled Server parameter 'connection_throttling' should be enabled for PostgreSQL Database Server Server parameter 'log_checkpoints' should be enabled for PostgreSQL Database Server Server parameter 'log_connections' should be enabled for PostgreSQL Database Server Server parameter 'log_disconnections' should be enabled for PostgreSQL Database Server Server parameter 'log_retention_days' should be greater than 3 days for PostgreSQL Database Server SSL connection on PostgreSQL Database Server should be enabledAzure.dbforpostgresql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> The Azure PostgreSQL database server should use geo-redundant backups The Azure PostgreSQL Database Server should use the current major version The server should have the 'log_duration' parameter set to 'ON'Azure.dbmysql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Private endpoint should be enabled for MySQL serversAzure.keyvault
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> All keys in non-RBAC Azure Key Vaults should have an expiration time set All keys in RBAC Azure Key Vault should have an expiration time set All secrets in Non-RBAC Azure Key Vault should have an expiration time set All secrets in RBAC Azure Key Vault should have an expiration time set Azure Key Vault should be recoverable Azure Key Vault should use RBAC Ensure that Role Based Access Control for Azure Key Vault is enabled Storage account encryption scopes should use customer-managed keys to encrypt data at restAzure.kubernetes
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AKS Cluster should have public access limited AKS cluster should use a network policy between nodes AKS Kubelet configuration file ownership should be assigned to root An AKS Cluster's kubelet configuration file ownership should be assigned to root An AKS Cluster's Kubelet configuration file should disable anonymous requests An AKS Cluster's kubelet configuration file should have permissions set to 644 or more restrictive An AKS Cluster's Kubelet should be allowed to manage iptables An AKS Cluster's Kubelet should have the eventRecordQPS entry set An AKS Cluster's Kubelet should not allow hostname overrides An AKS Cluster's Kubelet should only allow explicitly authorized requests An AKS Cluster's Kubelet should rotate client certificates automatically An AKS Cluster's Kubelet should rotate server certificates automatically An AKS Cluster's Kubelet's read-only port should be disabled An AKS's Kubelet should use TLS authentication The AKS kubeconfig file should have permissions set to 644 or more restrictive The Private Cluster feature for AKS should be enabled Timeouts for streaming connections in an AKS worker node should be enabledAzure.monitor
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Diagnostic Setting should capture appropriate categoriesAzure.network
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure Bastion host should exist Azure Bastion shareable links should not be permitted Subnets should be associated with a Network Security Group The network security group should allow specific port rulesAzure.networkwatcher
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Network Security Group Flow Log retention period should be 'greater than 90 days'Azure.security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Azure AppService HTTP Logs Enabled Azure function has admin level privileges at the subscription scope Azure managed identity has admin level privileges at the subscription scope Azure should be configured to send email notifications about security alerts with High severity Azure should be configured with a security contact email Azure should send security alert emails to subscription owners Ensure that logging for Azure Key Vault is Enabled Group has admin level privileges at the subscription scope PostgreSQL Database ingress traffic should be restricted to specified IP addresses Security Group should restrict HTTP(S) access from the internet Security Group should restrict RDP access from the internet Security Group should restrict SSH access from the internet Security Group should restrict UDP access from the internet SQL Databases should only allow ingress traffic from specific IP addresses User has admin level privileges at the subscription scopeAzure.sql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Audit data for Azure SQL Server should be retained for greater than 90 days Auditing on SQL Server should be enabled Azure Active Directory Admin should be configured for Azure SQL Data encryption for SQL Database Server should be enabled Microsoft Defender for SQL Server should be on for critical SQL Servers Periodic recurring vulnerability assessment scans should be enabled on SQL servers Private endpoint connections on Azure SQL Database should be enabled SQL Server Vulnerability Assessments should send scan reports to subscribed admins SQL server's Transparent Data Encryption (TDE) protector should be encrypted with a customer-managed key SQL servers should use customer-managed keys to encrypt data at rest Vulnerability Assessment (VA) setting 'Also send email notifications to admins and subscription owners' should be set for SQL servers Vulnerability Assessment should be enabled for SQL serverAzure.storage
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 'Allow storage account key access' setting for Azure Storage Accounts should be disabled 'Blob public access' should be disabled for storage accounts with blob containers 'Trusted Microsoft Services' should be enabled for Storage Account access Azure Blob Storage soft delete should be enabled Azure Blob Storage versioning should be enabled Azure storage accounts should not allow cross tenant replication Azure Storage should have soft delete enabled Blob Containers anonymous access should be restricted Blob Service storage logging should be enabled for 'Read', 'Write', and 'Delete' requests Default network access rule for storage accounts should be set to deny Default to Microsoft Entra authorization in the Azure portal should be enabled Minimum TLS version for storage accounts should be set to Version 1.2 Private Endpoints should be used to access Storage Accounts Public network access should be disabled for Azure Storage Accounts Secure transfer required should be enabled Storage account containing the blob container with activity logs should be encrypted with Customer Managed Key Storage containers storing activity logs should only be accessible by authorized personnel Storage for critical data should be encrypted with Customer Managed Key Table Service storage logging should be enabled for 'Read', 'Write', and 'Delete' requests The default network access rule for Storage Accounts should be set to denyBedrock
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Bedrock Agent Guardrails should have the Prompt Attack filter enabled and BLOCK prompt attacks at HIGH sensitivity Bedrock Agent Guardrails should have the Sensitive Information filter enabled and BLOCK highly sensitive PII entities Bedrock custom models should not output model data to publicly accessible s3 buckets Bedrock custom models should not train from publicly accessible s3 buckets IAM customer managed policies should enforce Bedrock Guardrails at runtime invocation IAM group inline policies should enforce Bedrock Guardrails at runtime invocation IAM role inline policies should enforce Bedrock Guardrails at runtime invocation IAM user inline policies should enforce Bedrock Guardrails at runtime invocationCheckpoint Harmony Email And Collaboration
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Check Point Harmony Email & Collaboration DLP policy violation in outgoing email BETA Check Point Harmony Email & Collaboration impossible travel detected BETA Check Point Harmony Email & Collaboration malicious URL clicked by user BETA Check Point Harmony Email & Collaboration malware attachments in email received by user BETA Check Point Harmony Email & Collaboration malware file shared by user in internal email BETA Check Point Harmony Email & Collaboration multiple phishing emails from external sender BETA Check Point Harmony Email & Collaboration multiple spam emails from external senderCheckpoint Quantum Firewall
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Checkpoint Quantum firewall ransomware infection detectedCisco Duo
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cisco Duo administrator locked out after too many failed login attempts Cisco Duo application enumeration by user Cisco Duo brute force attack on user Cisco Duo bypass code created by administrator Cisco Duo bypass code is used to authenticate user request Cisco Duo user marked authentication request as fraudulent Multiple Cisco Duo push notifications deniedCisco Secure Email Threat Defense
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Cisco Secure Email Threat Defense high number of threat emails received by an internal user BETA Cisco Secure Email Threat Defense high number of threat emails received from a particular domain BETA Cisco Secure Email Threat Defense high number of threat emails sent by an internal user BETA Cisco Secure Email Threat Defense unusual spike found for emails having `Domain brand impersonation` detection technique BETA Cisco Secure Email Threat Defense unusual spike found for emails having `Rare sender domain` detection technique BETA Cisco Secure Email Threat Defense unusual spike found for the high severity verdict techniquesCisco Secure Endpoint
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Cisco Secure Endpoint Alert BETA Cisco Secure Endpoint high number of malicious files from single host BETA Cisco Secure Endpoint malicious activity detected in system scan BETA Cisco Secure Endpoint malicious file detected on multiple hosts BETA Cisco Secure Endpoint rise in number of user login requests detectedCisco Umbrella DNS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cisco Umbrella - access to personal network detected Cisco Umbrella - allowed request to unsafe URL categoryCloudflare
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloudflare CASB Finding Cloudflare L7 DDOS detected Impossible travel scenario observed in Cloudflare logsCloudformation
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> CloudFormation stacks should have associated service roles CloudFormation stacks should have termination protection enabledCloudfront
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> CloudFront distribution contains S3 origin with external or nonexistent bucket Cloudfront distribution should be encrypted CloudFront distribution should be integrated with WAF CloudFront distribution should have a security policy requiring a secure version of TLS CloudFront distribution should have logging enabled CloudFront distributions should be configured for origin failover CloudFront distributions should be configured with a default root object CloudFront distributions should encrypt traffic to custom origins CloudFront distributions should use custom SSL/TLS certificates CloudFront distributions should use origin access control CloudFront distributions should use SNI to serve HTTPS requests CloudFront distributions should use trusted key groups for signed URLs and cookies CloudFront distributions that utilize HTTP POST Methods should have field-level encryption enabled CloudFront distributions using origin access identity should be migrated to origin access control CloudFront viewer should be encryptedCloudtrail
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> A user received an anomalous number of AccessDenied errors Additional AWS regions enabled Amazon Bedrock activity InvokeModel multiple regions Amazon Bedrock console activity Amazon Bedrock discovery attempt by long term access key Amazon Bedrock model invocations disabled Amazon EC2 AMI exfiltration attempt by IAM user Amazon S3 bucket policy modified Amazon SES enumeration attempt by previously unseen user Amazon SES modification attempt Amazon SNS enumeration attempt by previously unseen user Amazon SNS enumeration in multiple regions using a long-term access key An AWS account attempted to leave the AWS Organization An AWS S3 bucket lifecycle expiration policy was set to disabled An AWS S3 bucket lifecycle policy expiration is set to < 90 days An AWS S3 bucket mfaDelete is disabled An EC2 instance attempted to enumerate S3 bucket Anomalous amount of access denied events for AWS EC2 Instance Anomalous amount of Autoscaling Group events Anomalous API Gateway API key reads by user Anomalous number of assumed roles from user Anomalous number of AWS Lambda functions deleted Anomalous number of S3 buckets accessed Anomalous number of secrets retrieved from AWS Secrets Manager Anomalous S3 bucket activity from user ARN Attempt to create Xlarge EC2 instances in multiple AWS regions AWS access key creation by previously unseen identity AWS AMI Made Public AWS CloudTrail configuration modified AWS Cloudtrail possible secret enumeration in multiple regions and secret retrieval AWS CloudTrail trail should have global service events enabled AWS CloudWatch log group deleted AWS CloudWatch rule disabled or deleted AWS Config modified AWS console login without MFA AWS ConsoleLogin with MFA triggered Impossible Travel scenario AWS ConsoleLogin without MFA triggered Impossible Travel scenario AWS consoler detected BETA AWS CreateIndex by long term access key BETA AWS CreateIndex followed by ListResources via long term access key AWS Detective Graph deleted AWS Disable Cloudtrail with event selectors AWS EBS default encryption disabled AWS EBS Snapshot Made Public AWS EBS Snapshot possible exfiltration AWS EC2 key pair creation attempt with known suspicious naming convention AWS EC2 new event for application AWS EC2 new event for EKS Node Group AWS EC2 security group events observed with a suspicious naming convention AWS EC2 subnet deleted AWS ECS cluster deleted AWS ECS CreateCluster API calls in multiple regions AWS EventBridge rule disabled or deleted AWS GuardDuty detector deleted AWS GuardDuty publishing destination deleted AWS GuardDuty threat intel set deleted AWS IAM activity by S3 browser utility AWS IAM activity from EC2 instance AWS IAM AdministratorAccess policy was applied to a group AWS IAM AdministratorAccess policy was applied to a role AWS IAM AdministratorAccess policy was applied to a user AWS IAM AmazonSESFullAccess policy was applied to a group AWS IAM AmazonSESFullAccess policy was applied to a role AWS IAM AmazonSESFullAccess policy was applied to a user AWS IAM Identity Center SSO configuration updated AWS IAM policy modified AWS IAM Roles Anywhere trust anchor created AWS IAM Roles Anywhere User Profile Creation AWS IAM User created with AdministratorAccess policy attached AWS Java_Ghost security group creation attempt AWS Kinesis Firehose stream destination modified AWS KMS key deleted or scheduled for deletion AWS Lambda function modified by IAM user AWS Lambda function resource-based policy modified by IAM user BETA AWS ListResources by long term access key BETA AWS ListResources executed by new principal identity AWS Network Access Control List created or modified AWS Network Gateway created or modified AWS principal added to multiple EKS clusters AWS principal assigned administrative privileges in an EKS cluster AWS principal granted access to a EKS cluster then removed AWS RDS Cluster deleted AWS root account activity AWS Route 53 DNS query logging disabled AWS Route 53 VPC disassociated from query logging configuration AWS Route Table created or modified AWS S3 Bucket ACL made public AWS S3 Object encryption with SSE-C AWS S3 Public Access Block removed AWS security group created, modified or deleted AWS Security Hub disabled AWS SES add verified identity followed by the deletion of the identity AWS SES discovery attempt by long term access key AWS SES email sending enabled in current AWS region AWS VPC created or modified AWS VPC Flow Log deleted AWS WAF traffic blocked by specific rule AWS WAF traffic blocked by specific rule on multiple IPs AWS WAF web access control list deleted AWS WAF web access control list modified CloudTrail log file validation should be enabled CloudTrail logs S3 bucket should not be public accessible CloudTrail logs should be encrypted at rest using KMS CMKs Cloudtrail SecretsManager secret retrieved from AWS CloudShell environment CloudTrail trails should be integrated with CloudWatch Logs Compromised AWS EC2 Instance Creation of new AWS Bedrock long term access key with no expiration date EC2 instance created using risky AMI search pattern Encrypted administrator password retrieved for Windows EC2 instance High volume of AWS Sagemaker notebooks created in a short period of time Impossible travel observed on IAM User access key Indications of malicious key pair creation by long term access key Indications of malicious trust anchor creation Invitation sent to account to join AWS organization New Amazon EC2 Instance type New AWS account seen assuming a role into AWS account New Private Repository Container Image detected in AWS ECR New Public Repository Container Image detected in AWS ECR New user seen executing a command in an ECS task Object-level logging should be enabled for S3 bucket read events Object-level logging should be enabled for S3 bucket write events Password recovery request completed Possible AWS backup resource enumeration by long term access key Possible AWS EC2 privilege escalation via the modification of user data Possible privilege escalation via AWS login profile manipulation Possible RDS Snapshot exfiltration Potential administrative port open to the world via AWS security group Potential brute force attack on AWS ConsoleLogin Potential database port open to the world via AWS security group Primary email update request S3 bucket access logging should be enabled on the CloudTrail S3 bucket Security group open to the world Temporary AWS security credentials generated for user The AWS managed policy AWSCompromisedKeyQuarantine has been attached There should be at least one multi-region CloudTrail trail per AWS account Tor client IP address identified within AWS environment TruffleHog user agent observed in AWS Unfamiliar IAM user retrieved a decrypted AWS Systems Manager parameter Unfamiliar IAM user retrieved secret from AWS Secrets Manager Unfamiliar IAM user retrieved SSM parameter Unusual AWS identity requesting limit increase User enumerated AWS Secrets Manager - Anomaly User enumerated AWS Systems Manager parameters - AnomalyCodebuild
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> CodeBuild logs stored in S3 should be encrypted CodeBuild project environment variables should not contain plain text credentials CodeBuild projects should have logging enabled CodeBuild source credentials should be stored and transmitted securelyCognito
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cognito identity pool should not have the classic authentication flow enabled Cognito identity pools should only allow authenticated identities Cognito user pool password policies should have strong configurations Cognito user pools should have deletion protection enabled MFA should be enabled for Cognito user poolsConfluence Audit Records
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Atlassian Confluence admin key usage Atlassian Confluence global setting changed Atlassian Confluence public link turned on Atlassian Confluence site export Atlassian Confluence space exportCrowdstrike
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Crowdstrike AlertsDatadog Code Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Datadog Malicious PR ProtectionDatasync
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> DataSync tasks should have logging enabledDelinea Privilege Manager
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Delinea Privilege Manager detected a bad-rated application action event BETA Delinea Privilege Manager detected a newly discovered file marked as suspicious/bad by VirusTotal BETA Delinea Privilege Manager detected a password disclosure event BETA Delinea Privilege Manager detected a suspicious application justification event based on VirusTotal rating BETA Delinea Privilege Manager unusual spike in application justification events BETA Delinea Privilege Manager unusual spike in bad-rated application action events from a single computer BETA Delinea Privilege Manager unusual spike in password disclosure events by a requesting userDMS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> DMS endpoints should require SSL/TLS DMS replication instances should be configured to use multiple Availability Zones DMS replication instances should have automatic minor version upgrades enabled DMS replication tasks for the source database should have logging enabled DMS replication tasks for the target database should have logging enabledDnsfilter
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA DNSFilter high volume of `ANY` requests from a source BETA DNSFilter threat request allowedDocker
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> /usr/bin/containerd should be audited if applicable /var/lib/docker should be audited Container images should include HEALTHCHECK instructions Container runtime should include the --pids-limit flag for cgroup limit parameter Containers on the default network bridge should restrict network traffic Containers should have an enabled AppArmor profile Containers should have memory usage limits configured on Docker hosts Containers should not mount the Docker socket docker.sock inside them Containers should not run in privileged mode Containers should not share the host's user namespaces Containers should run as a non-root user Containers should use the cgroup configured in Docker Docker daemon activities should be audited Docker-related files should be audited in /etc/docker Incoming system calls should be filtered using enabled Seccomp profiles Kernel capabilities in Linux should only be granted when necessary Private registry should use TLS encryption for a secure Docker environment Privileged port mapping for containers should be restricted to increase security Processes in containers should have isolated Process ID (PID) namespaces SELinux security options should be properly configured for effective application security Sensitive host system directories should not be mounted on containers The /etc/default/docker file ownership should be set to root The /etc/default/docker file permissions should be set to 644 or stricter The /etc/docker directory permissions should be set to 755 or stricter The /etc/docker directory should be owned by root account The /etc/sysconfig/docker file permissions should be set to 644 or stricter The /etc/sysconfig/docker file should be owned by the root account and group The /usr/sbin/runc executable should be audited, if applicable The container should have a restart policy limited to 5 attempts The container should restrict acquiring additional privileges via suid or sgid bits The container's health should be constantly monitored The container's root filesystem should be set to read-only The critical containers should be configured to remain responsive The daemon.json file should have permissions set to 644 or stricter The daemon.json file should have user and group ownership set to root The default Docker configuration file should be audited on RHEL The default Docker configuration file should be audited, if applicable The Docker daemon configuration file should be audited if applicable The Docker daemon log level should be set to 'info' The Docker daemon should be allowed to configure the firewall rules The Docker daemon should only be controlled by root and Docker group The Docker instance should not use AUFS as its storage driver The Docker local storage partition should be separate from other partitions The Docker server certificate file should be owned by root The Docker server certificate file should have read-only or more restrictive permissions The Docker server certificate key file needs to have permissions of 400 The Docker server certificate key file should be owned by root The Docker socket file should be owned by root and Docker group The Docker socket file should have permissions of 660 or stricter The docker.service file ownership and group should be set to root The docker.service file permissions should be set to 644 The docker.service file should have auditing configured if applicable The docker.socket file should be audited, if applicable The docker.socket file should be owned by root The file permissions on docker.socket should be set to 644 or stricter The host's network namespace should be hidden from containers The IPC namespace on the host should remain isolated from containers The registry certificate files should be individually and group owned by root The registry certificate files should have read-only or stricter permissions The TLS CA certificate file should be owned by root account The TLS CA certificate file should have read-only or more restrictive permissions The UTS namespace should not be shared with the host TLS authentication should be enabled for Docker daemon to restrict remote accessDocumentdb
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> DocumentDB cluster snapshots should not be shared with external accounts DocumentDB clusters should be encrypted at rest DocumentDB clusters should have an appropriate backup retention period set DocumentDB clusters should have deletion protection enabled DocumentDB clusters should publish audit logs to CloudWatch LogsDynamodb
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> DynamoDB Accelerator (DAX) clusters should be encrypted at rest DynamoDB table replicates to a public S3 bucket DynamoDB tables should have deletion protection enabled DynamoDB tables should have point-in-time recovery enabled DynamoDB tables should scale automatically with demandEBS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EBS snapshot should be encrypted EBS volume snapshot should not be publicly shared EBS volume snapshot should not be shared with external accounts EBS volumes should be encryptedEC2
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Amazon Machine Image (AMI) should not be publicly shared Amazon Machine Image (AMI) should not be shared with external accounts or organizations Default VPC security group should restrict all traffic EC2 Client VPN endpoints should have client connection logging enabled EC2 instance should not have a highly-privileged IAM role attached to it EC2 instances and autoscaling groups should enforce IMDSv2 EC2 instances should not be publicly accessible EC2 instances should not use multiple ENIs EC2 launch templates should use Instance Metadata Service Version 2 (IMDSv2) EC2 paravirtual instance types should not be used EC2 setting 'Allowed AMIs' should be enabled and enforced by declarative policy EC2 setting 'Block public access for AMIs' should be enabled and enforced by declarative policy EC2 setting 'Block public access for EBS snapshots' should be enabled and enforced by declarative policy EC2 setting 'EBS encryption by default' should be enabled EC2 setting 'EC2 Serial Console access' should be disabled and be enforced by declarative policy EC2 setting 'IMDS Defaults' should enforce IMDSv2 by default and be enforced by declarative policy EC2 setting 'VPC Block Public Access' should be enabled and be enforced by declarative policy EC2 subnets should not automatically assign public IP addresses EC2 Transit Gateways should not automatically accept VPC attachment requests Inbound CIFS access should be restricted to trusted networks Inbound DNS access should be restricted Inbound FTP access should be restricted Inbound HTTP access should be restricted Inbound HTTPS access should be restricted Inbound ICMP access to the host should be restricted Inbound MongoDB access should be restricted Inbound MSSQL access should be restricted Inbound MySQL access should be restricted Inbound OpenSearch access should be restricted Inbound Oracle access should be restricted Inbound PostgreSQL access should be restricted Inbound RPC access should be restricted Inbound SMTP access should be restricted Inbound TCP NetBIOS access should be restricted Inbound Telnet access should be restricted Inbound UDP NetBIOS access should be restricted Instance roles should be used for AWS resource access from instances Outbound access on all ports should be restricted Publicly accessible AWS EC2 instance is vulnerable to CUPS remote code execution attack chain Publicly accessible EC2 contains critical vulnerabilities found in CISA KEV with greater than 15 days exposure time Publicly accessible EC2 contains critical vulnerabilities which have exploits available with greater than 30 days exposure time Publicly accessible EC2 contains critical vulnerabilities with greater than 30 days exposure time Publicly accessible EC2 contains high vulnerabilities with greater than 60 days exposure time Publicly accessible EC2 host is running IMDSv1 and has an SSRF vulnerability Publicly accessible EC2 instance contains critical vulnerability CVE-2024-3094 (RCE in liblzma and xz versions 5.6.0 and 5.6.1) Publicly Accessible EC2 instance has a critical vulnerability Publicly Accessible EC2 instance has a critical vulnerability has access to Redis ElasticCache with no AUTH Publicly accessible EC2 instance has access to an S3 bucket with sensitive data Publicly Accessible EC2 instance has privileged role and a critical vulnerability Publicly accessible EC2 instance should not have open administrative ports Publicly accessible EC2 instance uses IMDSv1 Publicly accessible EC2 instances should not have highly-privileged IAM roles Publicly accessible EC2 with privileged IAM role contains critical vulnerabilities with greater than 30 days exposure time Publicly accessible Lambda function has a critical vulnerability Security groups should not allow unrestricted access to ports with high risk Security groups should restrict traffic to trusted IPv4 addresses Security groups should restrict traffic to trusted IPv6 addresses Unused Network Access Control Lists should be removedECR
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Amazon ECR should be scanning all images for vulnerabilities ECR private repositories should have tag immutability enabled ECR private repositories should not grant public image downloads ECR private repositories should not grant public image uploadsECS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> ECS cluster logging should be enabled and encrypted ECS clusters should have Container Insights enabled ECS containers should be limited to read-only access to root filesystems ECS containers should run as non-privileged ECS Fargate services should automatically use the latest Fargate platform version ECS services should have volume encryption for mounted EFS volumes ECS services should not have public IP addresses assigned ECS task definitions should enable in transit encryption for EFS ECS task definitions should have a logging configuration ECS task definitions should have secure networking modes and user definitions ECS task definitions should maintain unique execution/task roles ECS task definitions should not share the host's process namespace Secrets should not be passed as container environment variablesEFS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EFS file systems should have encryption at rest enabledEKS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> An EKS Cluster's kubelet configuration file ownership should be assigned to root An EKS Cluster's Kubelet configuration file should disable anonymous requests An EKS Cluster's kubelet configuration file should have permissions set to 644 or more restrictive An EKS Cluster's Kubelet should be allowed to manage iptables An EKS Cluster's Kubelet should have the eventRecordQPS entry set An EKS Cluster's Kubelet should only allow explicitly authorized requests An EKS Cluster's Kubelet should rotate client certificates automatically An EKS Cluster's Kubelet should rotate server certificates automatically An EKS Cluster's Kubelet's read-only port should be disabled An EKS's Kubelet should use TLS authentication EKS Cluster Access Manager API should be enabled EKS Cluster secrets encryption should be enabled and use KMS CMKs EKS Cluster should have private endpoint enabled EKS Cluster should have public access limited EKS Cluster should have public access limited and managed nodegroups should use private subnets EKS cluster should use a network policy between nodes EKS clusters should have audit logs enabled EKS clusters should run on a supported version of Kubernetes Kubelet configuration file ownership should be assigned to root The kubeconfig file should have permissions set to 644 or more restrictive Timeouts for streaming connections in an EKS worker node should be enabledElasticache
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> ElastiCache clusters should be provisioned in a VPC ElastiCache clusters should not use the default subnet group ElastiCache clusters should use a non-default port for communication ElastiCache clusters should use the latest engine version available ElastiCache Redis clusters before version 6.0 should use Redis AUTH ElastiCache Redis clusters should be configured for automatic backup ElastiCache Redis clusters should have auto minor version upgrades enabled ElastiCache Redis replication groups should be encrypted at rest ElastiCache Redis replication groups should be encrypted in transit ElastiCache Redis replication groups should have automatic failover enabledElasticsearch
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Elasticsearch clusters should use the latest engine version Elasticsearch domain connections should be encrypted using a secure TLS version Elasticsearch domain should enable encryption Elasticsearch domain should only be accessible from an AWS VPC Elasticsearch domains should be encrypted with KMS Customer Master Keys Elasticsearch domains should encrypt data transmitted between nodes Elasticsearch domains should have at least three dedicated master nodes Elasticsearch domains should have audit logs enabled Elasticsearch domains should have error logging to CloudWatch Logs enabled Elasticsearch domains should use at least three data nodes The Elasticsearch domain should block unsigned requests over the public internetELB
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS ELB HTTP requests from security scanner Classic Load Balancer listener should use a secure configuration Classic Load Balancers should be configured to use Connection Draining Classic Load Balancers should be configured to use defensive or strictest desync mitigation mode Classic Load Balancers should span multiple Availability Zones Classic Load Balancers should utilize cross-zone load balancing Classic Load Balancers with SSL/HTTPS listeners should use a certificate issued by AWS Certificate Manager Logging and Audits should be configured for Load BalancersElbv2
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Application Load Balancers should be configured to use defensive or strictest desync mitigation mode Application Load Balancers should have Access logging enabled Application Load Balancers should have deletion protection enabled Application Load Balancers should use HTTPS Load Balancers should span multiple Availability Zones Load Balancers should use the latest security policy Private application load balancers should drop HTTP headers Public-facing application load balancers should drop HTTP headersExtrahop
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Extrahop security risk detectedFalco
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Falco findingFastly
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Fastly HTTP Requests from Security ScannerFile Integrity Monitoring
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Credentials file modified Critical system binary modified Cron job modified Kernel module directory modified Name Service Switch configuration modified RC scripts modified Shell command history modified SSH authorized keys modified SSL certificate tampering Sudoers policy file modified System authentication files modified Systemd service modifiedForcepoint Secure Web Gateway
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Forcepoint Secure Web Gateway abnormal number of blocked urls accessed by user BETA Forcepoint Secure Web Gateway threat indicator detected BETA Forcepoint Secure Web Gateway unusual spike found in requests for low reputation urls by users BETA Forcepoint Secure Web Gateway unusual spike found in web category urlsForcepoint Security Service Edge
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Forcepoint Security Service Edge alert event BETA Forcepoint Security Service Edge file quarantined event BETA Forcepoint Security Service Edge high number of download events from a user BETA Forcepoint Security Service Edge high volume of emails from a sender BETA Forcepoint Security Service Edge impossible travel detected in admin portal BETA Forcepoint Security Service Edge multiple DLP events detected for a particular file BETA Forcepoint Security Service Edge multiple files quarantined for a single userFortinet Fortimanager
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Fortinet Fortimanager alert BETA Fortinet Fortimanager successful brute force loginFSX
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> FSx Lustre file systems should copy tags to backups FSx OpenZFS file systems should copy tags to backups and volumesGCP
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Access denied for Google Cloud Service Account Anomalous number of Google Cloud Compute GPU virtual machines created Anomalous number of Google Cloud Storage Buckets Accessed Anomalous number of Google Cloud Storage Objects Accessed Anomalous number of Google Compute Engine instances created in multiple zones by user Attempt to add SSH key to Google Compute Engine project metadata by a previously unseen user GCP App Engine Default Service Account has overly permissive access to resources in the project GCP Compute Engine Default Service Account has overly permissive access to resources in the project GCP Group Account has overly permissive access to resources in the project GCP User Account has overly permissive access to resources in the project GCP User managed Service Account has overly permissive access to resources in the project Google App Engine service account used outside of Google Cloud Google Cloud BigQuery - query results saved to cloud storage Google Cloud BigQuery - query results saved to new table Google Cloud BigQuery results saved to cloud storage by a previously unseen user Google Cloud Compute Engine GPU virtual machine instance created Google Cloud exposed service account key Google Cloud GCE instance startup script added or modified Google Cloud IAM policy modified Google Cloud IAM role created Google Cloud IAM Role updated Google Cloud Logging Bucket deleted Google Cloud logging sink modified Google Cloud Project external principal added as project owner Google Cloud Pub/Sub Subscriber modified Google Cloud Pub/Sub topic deleted Google Cloud Service Account accessing anomalous number of Google Cloud APIs Google Cloud Service Account created Google Cloud Service Account Impersonation activity using access token generation Google Cloud Service Account Impersonation using GCPloit Exploitation Framework Google Cloud Service Account key created Google Cloud SQL database modified Google Cloud SQL instance data exported to cloud storage Google Cloud SQL instance data exported to cloud storage by a previously unseen user Google Cloud Storage Bucket contents downloaded without authentication Google Cloud Storage Bucket enumerated Google Cloud Storage Bucket modified Google Cloud Storage Bucket permissions modified Google Cloud unauthorized service account activity Google Cloud unauthorized user activity Google Compute Engine firewall egress rule opened to the world Google Compute Engine firewall rule modified Google Compute Engine image created Google Compute Engine instance metadata SSH key added or modified Google Compute Engine instances created in multiple zones by user Google Compute Engine network created Google Compute Engine network route created or modified Google Compute Engine project metadata SSH key added or modified Google Compute Engine service account used outside of Google Cloud Potential Google Cloud cryptomining attack from Tor IP Tor client IP address identified within Google Cloud environmentGcp.k8s.cluster
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Anonymous request authorizedGithub
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> GitHub PAT impossible travel event correlated with new user agent observedGithub Telemetry
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> GitHub a branch protection requirement was overridden by a repository administrator GitHub activity from automated scraping tool GitHub Advanced Security modification GitHub anomalous bot git activity GitHub anomalous bot org activity GitHub anomalous number of repositories cloned by user GitHub audit log streaming endpoint was deleted GitHub audit log streaming endpoint was modified GitHub branch protection disabled on branch GitHub critical resource enumeration activity via API GitHub Dependabot configuration changed GitHub enterprise or organization recovery codes activity GitHub enterprise owner added GitHub IP allow list GitHub large amount of classic personal access token use via suspicious VPN GitHub mass deletion of repositories GitHub mass exfiltration via cloning of repositories using a personal access token GitHub mass zip file exfiltration of repositories using a personal access token GitHub mass zip file exfiltration of repositories using an OAuth access token GitHub MFA requirement disabled GitHub OAuth access token compromise GitHub OAuth application access restrictions disabled GitHub organization was removed from enterprise GitHub organization was transferred between enterprise accounts GitHub payment method removed GitHub personal access token (PAT) auto approve policy modified GitHub Personal Access Token created by suspicious IP GitHub personal access token granted and used to clone large amount of repositories GitHub personal access token impossible travel detected from suspicious IP GitHub personal access token used by previously unseen user agent GitHub personal access token used to add collaborator GitHub PR review enforcement removed for main BETA GitHub private repository changed to public visibility GitHub repository activity from suspicious IP GitHub repository created with suspicious naming convention GitHub repository transfer GitHub review settings altered to skip review after PR push GitHub SAML/OIDC has been disabled BETA GitHub secret scanning alert generated GitHub secret scanning disabled or bypassed GitHub setting changed to fork private repository GitHub SSH certificate authority deleted GitHub SSH certificate requirement disabled GitHub SSH key added by suspicious IP GitHub Trufflehog user agent activity observed BETA GitHub unknown user cloned private repository BETA GitHub user anomalously downloaded data as a ZIP file GitHub user blocked from accessing organization repositoriesGitlab
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA GitLab brute force attack BETA GitLab deploy token created BETA GitLab group access token created GitLab group visibility changed to public BETA GitLab new administrator added BETA GitLab password reset from suspicious IP GitLab personal access token generated BETA GitLab project visibility changed BETA Gitlab SSO disabled BETA GitLab successive project or repository downloads BETA GitLab user changes associated email BETA GitLab user's multi-factor authentication disabled BETA Impossible travel GitLab event BETA Multiple GitLab OTP attempts deniedGKE
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Google Cloud Kubernetes Engine cluster should not be publicly accessibleGoogle Bigquery Dataset
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BigQuery data sets should specify a default customer-managed encryption key BigQuery Dataset should not be anonymously or publicly accessibleGoogle Bigquery Table
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BigQuery tables should be encrypted with customer-managed encryption keys (CMEK)Google Cloud Asset Inventory
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud Asset Inventory should be enabledGoogle Cloud SQL Instance
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SQL database instances should only use private IP addressesGoogle Compute Disk
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> VM disks for critical VMs should be encrypted with customer-supplied encryption keysGoogle Compute Firewall
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> RDP access should be restricted from the internet SSH access should be restricted from the internetGoogle Compute Instance
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Compute instances should be launched with Shielded VM enabled Compute instances should have confidential computing enabled Compute instances should only have internal IP addresses Instances should be configured to use a non-default service account with restricted API access Instances should have IP forwarding disabled Instances should use a non-default service account Instances should use instance-specific SSH keys instead of project-wide keys Projects should have OS Login enabled for SSH authentication Publicly accessible Google Compute instance has a critical severity vulnerability Publicly accessible Google Compute instance has a privileged service account and a critical severity vulnerability Publicly accessible Google Compute instance uses a privileged service account Publicly accessible Google VM instance contains critical vulnerabilities found in CISA KEV with greater than 15 days exposure time Publicly accessible Google VM instance contains critical vulnerabilities which have exploits available with greater than 30 days exposure time Publicly accessible Google VM instance contains critical vulnerabilities with greater than 30 days exposure time Publicly accessible Google VM instance contains critical vulnerability CVE-2024-3094 (RCE in liblzma and xz versions 5.6.0 and 5.6.1) Publicly accessible Google VM instance contains high vulnerabilities with greater than 60 days exposure time Publicly accessible Google VM instance with a privileged service account contains critical vulnerabilities with greater than 30 days exposure time Serial port connection for VM instances should be disabledGoogle Compute Network
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Projects should not have legacy networks configured for older projects Projects should only use non-default VPC networksGoogle Compute Subnetwork
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> VPC Flow Logs should be enabled for all VPC subnetsGoogle Dataproc Cluster
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Dataproc cluster should be encrypted using customer-managed encryption keyGoogle DNS Managed Zone
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud DNS DNSSEC should use a secure algorithm other than RSASHA1 Cloud DNS DNSSEC should use a zone-signing key with a secure algorithm other than RSASHA1 Cloud DNS should have DNSSEC enabledGoogle DNS Policy
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud DNS logging should be enabled for VPC networksGoogle Iam Policy
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud Audit Logging should be configured to track admin activity and data access Cloud Storage Bucket should not be anonymously or publicly accessible KMS roles assigned to users should utilize 'Separation of Duties'Google Kms Crypto Key
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> KMS encryption keys should be rotated every 90 days or lessGoogle Kubernetes Engine Cluster
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> 'Regular' or 'Stable' release channels should be used for GKE clusters Alpha clusters should not be used for production workloads Authentication using Client Certificates should be disabled Auto-Repair for nodes should be enabled in GKE clusters Auto-Upgrade for nodes should be enabled in GKE clusters Cluster should be created with Private Nodes Cluster should have Private Endpoint enabled and public access disabled Cluster VPC flow logs and intranode visibility should be enabled Clusters should use binary authorization Control plane authorized networks should be enabled GKE clusters should have monitoring and logging enabled Legacy authorization (ABAC) should be disabled The GKE cluster should be encrypted using customer-managed keys in KMS The Web UI Dashboard should be disabled VPC-native clusters should be usedGoogle Kubernetes Engine Node Pool
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Container-Optimized OS (cos_containerd) should be used for GKE node images Customer-Managed Encryption Keys (CMEK) should be used for boot disks Ensure GKE node pools do not use default service accounts GKE nodes should use the metadata server GKE Sandbox should be used for untrusted workloadsGoogle Kubernetes Worker Node
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> A GKE Cluster's kubelet configuration file ownership should be assigned to root A GKE Cluster's Kubelet configuration file should disable anonymous requests A GKE Cluster's kubelet configuration file should have permissions set to 600 or more restrictive A GKE Cluster's Kubelet should be allowed to manage iptables A GKE Cluster's Kubelet should have the eventRecordQPS entry set A GKE Cluster's Kubelet should only allow explicitly authorized requests A GKE Cluster's Kubelet should rotate client certificates automatically A GKE Cluster's Kubelet should rotate server certificates automatically A GKE Cluster's Kubelet's read-only port should be disabled A GKE's Cluster's Kubelet should use TLS authentication GKE Kubelet kubeconfig file ownership should be assigned to root The GKE kubeconfig file should have permissions set to 644 or more restrictive Timeouts for streaming connections in a GKE worker node should be enabledGoogle Logging Log Bucket
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Retention policies should be configured using bucket lock on log bucketsGoogle Logging Log Metric
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> A log metric filter and alert should exist for audit configuration changes A log metric filter and alert should exist for cloud storage bucket IAM changes A log metric filter and alert should exist for custom role changes A log metric filter and alert should exist for project ownership assignments/changes A log metric filter and alert should exist for SQL instance configuration changes A log metric filter and alert should exist for VPC network changes A log metric filter and alert should exist for VPC network firewall rule changes A log metric filter and alert should exist for VPC network route changesGoogle Logging Log Sink
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Log entries should have log sinks configured for exportingGoogle Service Account
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud KMS cryptokeys should restrict anonymous and/or public access Service accounts should keep the 'Service Account Admin' and 'Service Account User' roles separate Service accounts should only be bound to non-administrative roles Service Accounts should only use GCP managed keys Service accounts should rotate user-managed or external keys every 90 days or less Users should be assigned the 'Service Account User' or 'Service Account Token Creator' roles at the Service Account levelGoogle SQL Database Instance
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> MySQL instance should have the 'skip_show_database' flag set to 'on' MySQL instances should have the 'local_infile' database flag set to 'off' PostgreSQL instance should have the 'log_disconnections' database flag enabled PostgreSQL instances should have the 'log_connections' database flag set to 'on' PostgreSQL instances should have the 'log_error_verbosity' flag set to 'DEFAULT' or stricter PostgreSQL instances should have the 'log_hostname' database flag set to 'on' PostgreSQL instances should have the 'log_min_messages' database flag set to at least 'WARNING' PostgreSQL instances should have the 'log_statement' database flag set appropriately PostgreSQL instances should have the `log_min_duration_statement` flag set to '-1' (disabled) PostgreSQL instances should have the `log_min_error_statement` flag set to 'ERROR' or stricter SQL database instances should enforce SSL for all incoming connections SQL database instances should have automated backups enabled SQL Database instances should only allow ingress traffic from specific IP addresses SQL Server instances should have the 'contained database authentication' database flag set to 'off' SQL Server instances should have the 'cross db ownership chaining' database flag set to 'off' SQL Server instances should have the 'external scripts enabled' database flag set to 'off' SQL Server instances should have the 'remote access' database flag set to 'off' SQL Server instances should have the 'user connections' database flag set to a non-limiting value SQL Server instances should have the `3625 (trace flag)` database flag set to 'on' SQL Server instances should have the `user options` database flag disabledGoogle Storage Bucket
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cloud storage buckets should have uniform bucket-level access enabledGoogle.security.command.center
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Google Security Command Center Google Security Command Center finding mutedGoogle.workspace.alert.center
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Google Workspace Alert CenterGsuite
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Domain added to Google Workspace allowlisted domains Google Workspace accessed by Google Google Workspace admin role created Google Workspace administrator has disabled 2-step verification for organizational unit Google Workspace administrator initiated a data transfer request Google Workspace Tor client detected Google Workspace user assigned administrative role Google Workspace user disabled 2-step verification Google Workspace user edited account recovery information Google Workspace user forwarding email out of non Google Workspace domain Google Workspace user has unenrolled from Advanced Protection Large amount of downloads on Google Drive User attempted login with leaked passwordGuardduty
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS GuardDuty findingHave I Been Pwned
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Have I Been Pwned latest breach detectedHost Benchmarks
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> A remote time server for Chrony is configured Add nodev Option to /dev/shm Add nodev Option to /home Add nodev Option to /tmp Add nodev Option to /var Add nodev Option to /var/log Add nodev Option to /var/log/audit Add nodev Option to /var/tmp Add noexec Option to /dev/shm Add noexec Option to /tmp Add noexec Option to /var/log Add noexec Option to /var/log/audit Add noexec Option to /var/tmp Add nosuid Option to /dev/shm Add nosuid Option to /home Add nosuid Option to /tmp Add nosuid Option to /var Add nosuid Option to /var/log Add nosuid Option to /var/log/audit Add nosuid Option to /var/tmp All AppArmor Profiles are in enforce or complain mode All GIDs referenced in /etc/passwd must be defined in /etc/group All Interactive User Home Directories Must Be Group-Owned By The Primary Group All Interactive User Home Directories Must Be Owned By The Primary User All Interactive User Home Directories Must Have mode 0750 Or Less Permissive All Interactive Users Home Directories Must Exist Audit Configuration Files Must Be Owned By Group root Audit Configuration Files Must Be Owned By Root Avoid using remember in pam_unix module Build and Test AIDE Database Chrony Configure Pool and Server Configure Accepting Router Advertisements on All IPv6 Interfaces Configure AIDE to Verify the Audit Tools Configure Firewalld to Restrict Loopback Traffic Configure Firewalld to Trust Loopback Traffic Configure GNOME3 DConf User Profile Configure Kernel Parameter for Accepting Secure Redirects By Default Configure ntpd To Run As ntp User Configure Periodic Execution of AIDE Configure SELinux Policy Configure server restrictions for ntpd Configure SSH to use System Crypto Policy Configure System Cryptography Policy Configure Systemd Timer Execution of AIDE Configure Systemd Timesyncd Servers Configure systemd-journal-upload TLS parameters: ServerKeyFile, ServerCertificateFile and TrustedCertificateFile Configure systemd-journal-upload URL Configure the Use of the pam_faillock.so Module in the /etc/pam.d/password-auth File. Configure the Use of the pam_faillock.so Module in the /etc/pam.d/system-auth File. Deactivate Wireless Network Interfaces Disable Accepting ICMP Redirects for All IPv4 Interfaces Disable Accepting ICMP Redirects for All IPv6 Interfaces Disable Accepting Router Advertisements on all IPv6 Interfaces by Default Disable apache2 Service Disable Apport Service Disable Avahi Server Software Disable Bluetooth Service Disable core dump backtraces Disable Core Dumps for All Users Disable Core Dumps for SUID programs Disable DHCP Service Disable DHCPD6 Service Disable dnsmasq Service Disable Dovecot Service Disable GNOME3 Automount Opening Disable GNOME3 Automount running Disable GNOME3 Automounting Disable Host-Based Authentication Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv4 Interfaces Disable Kernel Parameter for Accepting ICMP Redirects by Default on IPv6 Interfaces Disable Kernel Parameter for Accepting Secure ICMP Redirects on all IPv4 Interfaces Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv4 Interfaces Disable Kernel Parameter for Accepting Source-Routed Packets on all IPv6 Interfaces Disable Kernel Parameter for Accepting Source-Routed Packets on IPv4 Interfaces by Default Disable Kernel Parameter for Accepting Source-Routed Packets on IPv6 Interfaces by Default Disable Kernel Parameter for IP Forwarding on IPv4 Interfaces Disable Kernel Parameter for IPv6 Forwarding Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces Disable Kernel Parameter for Sending ICMP Redirects on all IPv4 Interfaces by Default Disable LDAP Server (slapd) Disable Modprobe Loading of USB Storage Driver Disable Mounting of cramfs Disable Mounting of freevxfs Disable Mounting of hfs Disable Mounting of hfsplus Disable Mounting of jffs2 Disable Mounting of udf Disable named Service Disable Network File System (nfs) Disable nginx Service Disable Postfix Network Listening Disable rpcbind Service Disable Samba Disable snmpd Service Disable Squid Disable SSH Access via Empty Passwords Disable SSH Root Login Disable SSH Support for .rhosts Files Disable storing core dump Disable systemd_timesyncd Service Disable systemd-journal-remote Socket Disable tftpd-hpa Service Disable the Automounter Disable the CUPS Service Disable the GNOME3 Login User List Disable vsftpd Service Disable XDMCP in GDM Disable xinetd Service Disable ypserv Service Do Not Allow SSH Environment Options Enable authselect Enable cron Daemon Enable cron Service Enable GNOME3 Login Warning Banner Enable GNOME3 Screensaver Lock After Idle Period Enable Kernel Parameter to Ignore Bogus ICMP Error Responses on IPv4 Interfaces Enable Kernel Parameter to Ignore ICMP Broadcast Echo Requests on IPv4 Interfaces Enable Kernel Parameter to Log Martian Packets on all IPv4 Interfaces Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces Enable Kernel Parameter to Use Reverse Path Filtering on all IPv4 Interfaces by Default Enable Kernel Parameter to Use TCP Syncookies on Network Interfaces Enable Kernel Paremeter to Log Martian Packets on all IPv4 Interfaces by Default Enable PAM Enable Randomized Layout of Virtual Address Space Enable rsyslog Service Enable SSH Warning Banner Enable systemd_timesyncd Service Enable systemd-journal-upload Service Enable systemd-journald Service Enable the NTP Service Enforce Password History with use_authtok Enforce Usage of pam_wheel with Group Parameter for su Authentication Ensure /dev/shm is configured Ensure /tmp Located On Separate Partition Ensure a Single Time Synchronization Service is in Use Ensure a Table Exists for Nftables Ensure All Accounts on the System Have Unique Names Ensure All Accounts on the System Have Unique User IDs Ensure All Files Are Owned by a Group Ensure All Files Are Owned by a User Ensure All Groups on the System Have Unique Group ID Ensure All Groups on the System Have Unique Group Names Ensure All User Initialization Files Have Mode 0740 Or Less Permissive Ensure all users last password change date is in the past Ensure AppArmor is enabled in the bootloader configuration Ensure AppArmor is installed Ensure AppArmor Utils is installed Ensure Authentication Required for Single User Mode Ensure Base Chains Exist for Nftables Ensure gpgcheck Enabled for All yum Package Repositories Ensure gpgcheck Enabled In Main yum Configuration Ensure ip6tables Firewall Rules Exist for All Open Ports Ensure iptables Firewall Rules Exist for All Open Ports Ensure journald ForwardToSyslog is disabled Ensure journald is configured to compress large log files Ensure journald is configured to send logs to rsyslog Ensure journald is configured to write log files to persistent disk Ensure LDAP client is not installed Ensure Local Login Warning Banner Is Configured Properly Ensure Log Files Are Owned By Appropriate Group Ensure Log Files Are Owned By Appropriate User Ensure Logs Sent To Remote Host Ensure Mail Transfer Agent is not Listening on any non-loopback Address Ensure Message Of The Day Is Configured Properly Ensure network interfaces are assigned to appropriate zone Ensure nftables Default Deny Firewall Policy Ensure nftables Rules are Permanent Ensure No Daemons are Unconfined by SELinux Ensure No World-Writable Files Exist Ensure One Logging Service Is In Use Ensure Only One Firewall Service is Active Ensure Only Users Logged In To Real tty Can Execute Sudo - sudo use_pty Ensure PAM Enforces Password Requirements - Authentication Retry Prompts Permitted Per-Session Ensure PAM Enforces Password Requirements - Enforce for root User Ensure PAM Enforces Password Requirements - Enforcing Ensure PAM Enforces Password Requirements - Minimum Different Categories Ensure PAM Enforces Password Requirements - Minimum Different Characters Ensure PAM Enforces Password Requirements - Minimum Digit Characters Ensure PAM Enforces Password Requirements - Minimum Length Ensure PAM Enforces Password Requirements - Minimum Lowercase Characters Ensure PAM Enforces Password Requirements - Minimum Special Characters Ensure PAM Enforces Password Requirements - Minimum Uppercase Characters Ensure PAM Enforces Password Requirements - Prevent the Use of Dictionary Words Ensure pam_faillock module is enabled Ensure Remote Login Warning Banner Is Configured Properly Ensure root account access is controlled Ensure rsyncd service is disabled Ensure rsyslog Default File Permissions Configured Ensure rsyslog Does Not Accept Remote Messages Unless Acting As Log Server Ensure rsyslog is Installed Ensure SELinux is Not Disabled Ensure SELinux Not Disabled in /etc/default/grub Ensure shadow Group is Empty Ensure SSH LoginGraceTime is configured Ensure SSH MaxStartups is configured Ensure Sudo Logfile Exists - sudo logfile Ensure System Log Files Have Correct Permissions Ensure that /etc/at.allow exists Ensure that /etc/at.deny does not exist Ensure that /etc/cron.allow exists Ensure that /etc/cron.deny does not exist Ensure that All Entries in The Path of Root Are Directories Ensure that All Root's Path Directories Are Owned by Root Ensure that chronyd is running under chrony user account Ensure that Root's Path Does Not Include Relative Paths or Null Directories Ensure that Root's Path Does Not Include World or Group-Writable Directories Ensure that System Accounts Are Locked Ensure that System Accounts Do Not Run a Shell Upon Login Ensure the Default Bash Umask is Set Correctly Ensure the Default C Shell Umask is Set Correctly Ensure the Default Umask is Set Correctly For Interactive Users Ensure the Default Umask is Set Correctly in /etc/profile Ensure the Default Umask is Set Correctly in login.defs Ensure the Group Used by pam_wheel.so Module Exists on System and is Empty Ensure the Root Bash Umask is Set Correctly Ensure There Are No Accounts With Blank or Null Passwords Ensure ufw Default Deny Firewall Policy Ensure ufw Firewall Rules Exist for All Open Ports Ensure User Bash History File Has Correct Permissions Ensure Users Cannot Change GNOME3 Screensaver Settings Ensure Users Cannot Change GNOME3 Session Idle Settings Ensure Users Re-Authenticate for Privilege Escalation - sudo Ensure Users Re-Authenticate for Privilege Escalation - sudo !authenticate Ensure users' .netrc Files are not group or world accessible Install AIDE Install firewalld Package Install iptables Package Install iptables-persistent Package Install libselinux Package Install nftables Package Install pam_pwquality Package Install pam-modules Package Install pam-runtime Package Install sudo Package Install systemd-journal-remote Package Install the cron service Install the systemd_timesyncd Service Install ufw Package Limit Password Reuse Limit Password Reuse (STIGs - ubuntu2004) Limit Password Reuse (ubuntu2404) Limit Password Reuse: password-auth Limit Password Reuse: system-auth Limit the maximum number of sequential characters in passwords Limit Users' SSH Access Lock Accounts After Failed Password Attempts Make sure that the dconf databases are up-to-date with regards to respective keyfiles Modify the System Login Banner Modify the System Login Banner for Remote Connections Modify the System Message of the Day Banner Package "prelink" Must not be Installed Prevent Login to Accounts With Empty Password Prevent Login to Accounts With Empty Password (ubuntu2404) Remove autofs Package Remove ftp Package Remove iptables-persistent Package Remove NIS Client Remove Rsh Trust Files Remove telnet Clients Remove telnet Clients (ubuntu2404) Remove tftp Daemon Remove the GDM Package Group Remove the X Windows Package Group Remove tnftp Package Remove ufw Package Require Authentication for Emergency Systemd Target Require Authentication for Single User Mode Require Re-Authentication When Using the sudo Command Require use_authtok for pam_unix.so Restrict usage of ptrace to descendant processes Set Account Expiration Following Inactivity Set configuration for IPv6 loopback traffic Set configuration for loopback traffic Set Default ip6tables Policy for Incoming Packets Set Default iptables Policy for Incoming Packets Set Deny For Failed Password Attempts Set existing passwords a period of inactivity before they been locked Set Existing Passwords Maximum Age Set Existing Passwords Minimum Age Set Existing Passwords Warning Age Set GNOME3 Screensaver Inactivity Timeout Set GNOME3 Screensaver Lock Delay After Activation Period Set Interactive Session Timeout Set Interval For Counting Failed Password Attempts Set Lockout Time for Failed Password Attempts Set LogLevel to INFO Set nftables Configuration for Loopback Traffic Set PAM''s Password Hashing Algorithm Set PAM''s Password Hashing Algorithm - password-auth Set Password Hashing Algorithm in /etc/libuser.conf Set Password Hashing Algorithm in /etc/login.defs Set Password Maximum Age Set Password Maximum Consecutive Repeating Characters Set Password Minimum Age Set Password Warning Age Set SSH authentication attempt limit Set SSH Client Alive Count Max Set SSH Client Alive Interval Set SSH Daemon LogLevel to VERBOSE Set SSH MaxSessions limit Set the GNOME3 Login Warning Banner Text Set UFW Loopback Traffic System Audit Logs Must Be Group Owned By Root System Audit Logs Must Be Owned By Root System Audit Logs Must Have Mode 0640 or Less Permissive System Audit Logs Must Have Mode 0750 or Less Permissive The Chrony package is installed The Chronyd service is disabled The Chronyd service is enabled Uninstall apache2 Package Uninstall avahi Server Package Uninstall bind Package Uninstall CUPS Package Uninstall cyrus-imapd Package Uninstall DHCP Server Package Uninstall dnsmasq Package Uninstall dovecot Package Uninstall kea Package Uninstall mcstrans Package Uninstall net-snmp Package Uninstall nfs-kernel-server Package Uninstall nftables package Uninstall nginx Package Uninstall openldap-servers Package Uninstall rpcbind Package Uninstall rsh Package Uninstall rsync Package Uninstall Samba Package Uninstall setroubleshoot Package Uninstall squid Package Uninstall talk Package Uninstall telnet-server Package Uninstall tftpd-hpa Package Uninstall the nis package Uninstall vsftpd Package Uninstall xinetd Package Uninstall ypserv Package Use Only FIPS 140-2 Validated Ciphers Use Only FIPS 140-2 Validated MACs Use Only Strong Ciphers Use Only Strong Key Exchange algorithms Use Only Strong MACs User Initialization Files Must Be Group-Owned By The Primary Group User Initialization Files Must Be Owned By the Primary User User Initialization Files Must Not Run World-Writable Programs Verify /boot/efi/EFI/redhat/user.cfg Group Ownership Verify /boot/efi/EFI/redhat/user.cfg Permissions Verify /boot/efi/EFI/redhat/user.cfg User Ownership Verify /boot/grub/grub.cfg Permissions Verify /boot/grub/grub.cfg User Ownership Verify /boot/grub2/grub.cfg Group Ownership Verify /boot/grub2/user.cfg Group Ownership Verify /boot/grub2/user.cfg Permissions Verify /boot/grub2/user.cfg User Ownership Verify All Account Password Hashes are Shadowed Verify All Account Password Hashes are Shadowed with SHA512 Verify firewalld Enabled Verify Group Ownership of Message of the Day Banner Verify Group Ownership of System Login Banner Verify Group Ownership of System Login Banner for Remote Connections Verify Group Ownership on SSH Server Private *_key Key Files Verify Group Ownership on SSH Server Public *.pub Key Files Verify Group Who Owns /etc/at.allow file Verify Group Who Owns /etc/at.deny file Verify Group Who Owns /etc/cron.allow file Verify Group Who Owns /etc/security/opasswd File Verify Group Who Owns /etc/security/opasswd.old File Verify Group Who Owns /etc/shells File Verify Group Who Owns /var/log/(b|w)tmp(.*|-*) File Verify Group Who Owns /var/log/*.journal(~) File Verify Group Who Owns /var/log/auth.log File Verify Group Who Owns /var/log/cloud-init.log* File Verify Group Who Owns /var/log/lastlog File Verify Group Who Owns /var/log/localmessages* File Verify Group Who Owns /var/log/messages File Verify Group Who Owns /var/log/secure File Verify Group Who Owns /var/log/syslog File Verify Group Who Owns /var/log/waagent.log File Verify Group Who Owns Backup group File Verify Group Who Owns Backup gshadow File Verify Group Who Owns Backup passwd File Verify Group Who Owns Backup shadow File Verify Group Who Owns cron.d Verify Group Who Owns cron.daily Verify Group Who Owns cron.hourly Verify Group Who Owns cron.monthly Verify Group Who Owns cron.weekly Verify Group Who Owns Crontab Verify Group Who Owns group File Verify Group Who Owns gshadow File Verify Group Who Owns passwd File Verify Group Who Owns shadow File Verify Group Who Owns SSH Server config file Verify Grouponwership of Files in /var/log/sssd Verify Groupownership of Files in /var/log/apt Verify Groupownership of Files in /var/log/gdm Verify Groupownership of Files in /var/log/gdm3 Verify nftables Service is Disabled Verify nftables Service is Enabled Verify No .forward Files Exist Verify No netrc Files Exist Verify Non-Interactive Accounts Are Locked Verify Only Group Root Has GID 0 Verify Only Root Has UID 0 Verify Owner on cron.d Verify Owner on cron.daily Verify Owner on cron.hourly Verify Owner on cron.monthly Verify Owner on cron.weekly Verify Owner on crontab Verify Owner on SSH Server config file Verify Ownership of Files in /var/log/apt Verify Ownership of Files in /var/log/gdm Verify Ownership of Files in /var/log/gdm3 Verify Ownership of Files in /var/log/sssd Verify ownership of log files Verify ownership of log files (ubuntu2404) Verify ownership of Message of the Day Banner Verify ownership of System Login Banner Verify ownership of System Login Banner for Remote Connections Verify Ownership on SSH Server Private *_key Key Files Verify Ownership on SSH Server Public *.pub Key Files Verify pam_pwhistory module is activated Verify pam_pwquality module is activated Verify pam_unix module is activated Verify Permissions and Ownership of Old Passwords File Verify Permissions of Files in /var/log/gdm Verify Permissions of Files in /var/log/gdm3 Verify Permissions of Files in /var/log/sssd Verify permissions of log files Verify Permissions on /etc/at.allow file Verify Permissions on /etc/at.deny file Verify Permissions on /etc/audit/auditd.conf Verify Permissions on /etc/audit/rules.d/*.rules Verify Permissions on /etc/cron.allow file Verify Permissions on /etc/security/opasswd File Verify Permissions on /etc/security/opasswd.old File Verify Permissions on /etc/shells File Verify Permissions on /var/log/auth.log File Verify Permissions on /var/log/cloud-init.log(.*) Files Verify Permissions on /var/log/lastlog(.*) Files Verify Permissions on /var/log/localmessages(.*) Files Verify Permissions on /var/log/messages File Verify Permissions on /var/log/secure File Verify Permissions on /var/log/syslog File Verify Permissions on /var/log/waagent.log(.*) Files Verify Permissions on /var/log/wtmp(.*) Files Verify Permissions on Backup group File Verify Permissions on Backup gshadow File Verify Permissions on Backup passwd File Verify Permissions on Backup shadow File Verify Permissions on cron.d Verify Permissions on cron.daily Verify Permissions on cron.hourly Verify Permissions on cron.monthly Verify Permissions on cron.weekly Verify Permissions on crontab Verify Permissions on files in the /var/log/apt/.* directory Verify Permissions on group File Verify Permissions on gshadow File Verify permissions on Message of the Day Banner Verify Permissions on passwd File Verify Permissions on shadow File Verify Permissions on SSH Server config file Verify Permissions on SSH Server Private *_key Key Files Verify Permissions on SSH Server Public *.pub Key Files Verify permissions on System Login Banner Verify permissions on System Login Banner for Remote Connections Verify Root Has A Primary GID 0 Verify that All World-Writable Directories Have Sticky Bits Set Verify that audit tools are owned by group root Verify that audit tools are owned by root Verify that audit tools Have Mode 0755 or less Verify the UEFI Boot Loader grub.cfg Group Ownership Verify the UEFI Boot Loader grub.cfg Permissions Verify the UEFI Boot Loader grub.cfg User Ownership Verify ufw Active Verify ufw Enabled Verify User Who Owns /etc/at.allow file Verify User Who Owns /etc/at.deny file Verify User Who Owns /etc/cron.allow file Verify User Who Owns /etc/security/opasswd File Verify User Who Owns /etc/security/opasswd.old File Verify User Who Owns /var/log/(b|w)tmp(.*|-*) File Verify User Who Owns /var/log/*.journal(~) Files Verify User Who Owns /var/log/auth.log File Verify User Who Owns /var/log/cloud-init.log File Verify User Who Owns /var/log/lastlog File Verify User Who Owns /var/log/localmessages File Verify User Who Owns /var/log/messages File Verify User Who Owns /var/log/secure File Verify User Who Owns /var/log/syslog File Verify User Who Owns /var/log/waagent.log File Verify User Who Owns Backup group File Verify User Who Owns Backup gshadow File Verify User Who Owns Backup passwd File Verify User Who Owns Backup shadow File Verify User Who Owns group File Verify User Who Owns gshadow File Verify User Who Owns passwd File Verify User Who Owns shadow File Verify Who Owns /etc/shells FileIAM
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Access keys granting 'root' should be removed Access keys should be rotated every 90 days or less AWS Cognito identity pool has guest access configured for a role with administrative privileges AWS EC2 instance can assume a role with administrative privileges AWS EC2 instance can assume a role with administrative privileges cross-account AWS EC2 instance can assume multiple roles with administrative privileges cross-account AWS EC2 instance can create a login profile for an IAM user with administrative privileges AWS EC2 instance can create access keys for an IAM user with administrative privileges AWS EC2 instance can update a login profile for an IAM user with administrative privileges AWS EC2 instance can update the trust policy for a role with administrative privileges AWS EC2 instance has administrative privileges AWS IAM group can assume a role with administrative privileges AWS IAM group can create a login profile for an IAM user with administrative privileges AWS IAM group can create access keys for an IAM user with administrative privileges AWS IAM group can update a login profile for an IAM user with administrative privileges AWS IAM group can update the trust policy for a role with administrative privileges AWS IAM group has access to a large number of resources AWS IAM group has administrative privileges AWS IAM policy with administrative privileges is not attached to any principal AWS IAM role can assume a role with administrative privileges AWS IAM role can assume a role with administrative privileges cross-account AWS IAM role can assume multiple roles with administrative privileges cross-account AWS IAM role can create a login profile for an IAM user with administrative privileges AWS IAM role can create access keys for an IAM user with administrative privileges AWS IAM role can update a login profile for an IAM user with administrative privileges AWS IAM role can update the trust policy for a role with administrative privileges AWS IAM role has a large permissions gap AWS IAM role has a trust relationship with a wildcard principal AWS IAM role has access to a large number of resources AWS IAM role has administrative privileges AWS IAM role has administrative privileges and is inactive AWS IAM role with administrative privileges has a trust relationship with a wildcard principal AWS IAM role with external cross-account trust relationship does not use an external ID AWS IAM user can assume a role with administrative privileges AWS IAM user can assume a role with administrative privileges cross-account AWS IAM user can assume multiple roles with administrative privileges cross-account AWS IAM user can create a login profile for an IAM user with administrative privileges AWS IAM user can create access keys for an IAM user with administrative privileges AWS IAM user can update a login profile for an IAM user with administrative privileges AWS IAM user can update the trust policy for a role with administrative privileges AWS IAM user has a large permissions gap AWS IAM user has access to a large number of resources AWS IAM user has administrative privileges AWS IAM user has administrative privileges and is inactive AWS Lambda function has administrative privileges AWS Organizations centralized root credentials management feature should be enabled AWS Organizations member accounts should not have root user credentials when centralized access is enabled AWS Organizations root sessions feature should be enabled Bedrock Knowledge Base write access should be condition-scoped in IAM Customer-Managed policies Bedrock Knowledge Base write access should be condition-scoped in IAM group inline policies Bedrock Knowledge Base write access should be condition-scoped in IAM role inline policies Bedrock Knowledge Base write access should be condition-scoped in IAM user inline policies Expired SSL/TLS certificates should be removed from AWS IAM IAM Access Analyzer should be enabled in all active regions IAM access keys that are inactive and older than 1 year should be removed IAM customer managed policies should not allow decryption actions on all KMS keys IAM customer managed policies should not allow wildcard actions for services IAM groups should have assigned permissions IAM groups should have at least one user attached IAM groups should not have IAM inline policies that allow decryption actions on all KMS keys IAM groups should not have inline policies attached IAM password policy should require at least one lowercase letter IAM password policy should require at least one number in passwords IAM password policy should require at least one symbol IAM password policy should require uppercase characters IAM password policy should require user passwords to expire within 90 days IAM policies should adhere to least-privilege IAM policies should be attached and managed at the group level IAM policies should not use 'Effect: Allow' with 'NotAction' IAM role has trust policy containing cross-organization principal IAM role has trust policy containing cross-OU principal IAM role has trust policy containing external principal IAM roles should be used within the last 90 days IAM roles should not allow untrusted GitHub Actions to assume them IAM roles should not allow untrusted GitLab runners to assume them IAM roles should not have a trust policy that contains a wildcard principal IAM roles should not have IAM inline policies that allow decryption actions on all KMS keys IAM roles with policies attached should be used within the last 90 days IAM server certificate should be renewed 30 days before expiration IAM User access keys should be created after initial setup IAM users should have assigned permissions IAM users should not have both Console access and Access Keys IAM users should not have IAM inline policies that allow decryption actions on all KMS keys IAM users should not have the 'AdministratorAccess' policy attached Known compromised IAM users should not be present in the account MFA should be enabled for all users with console access MFA should be enabled for the 'root' account Only one active access key should exist per user Password policy should prevent password reuse Password policy should require at least 14 characters Support roles should be created to manage incidents with AWS Support The 'root' account should not be used for daily tasks The 'root' user account should use hardware-based MFA Unused credentials should be deactivated or removedIAM Account
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AWS Config should be enabled and recording in all active regionsIboss
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA iboss allowed malware activity detected BETA iboss multiple soft blocked requests detectedIIS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> IIS HTTP requests from security scannerIvanti Connect Secure
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Ivanti connect secure impossible travel detected BETA Ivanti connect secure multiple blocked web requests detected BETA Ivanti connect secure multiple failed login attempts followed by successful login BETA Ivanti connect secure severe events detectedIvanti Nzta
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Ivanti nZTA critical and major events detected BETA Ivanti nZTA device vulnerability risk detected BETA Ivanti nZTA multiple failed login attempts detected followed by successful loginJamfprotect
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Jamf Protect alerts Jamf Protect threat eventsJira Audit Records
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Atlassian Tor client activity detectedJumpcloud
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Credential stuffing attack on Jumpcloud Jumpcloud admin granted system privileges Jumpcloud admin login without MFA Jumpcloud admin triggered impossible travel scenario Jumpcloud administrator role assigned Jumpcloud brute force attack on user Jumpcloud password manager local export Jumpcloud policy created Jumpcloud policy modified Multiple Jumpcloud push notifications deniedKeeper
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Keeper activity observed from Tor client IP BETA Keeper brute force attempt BETA Keeper high risk password detected for user BETA Keeper records export detectedKeycloak
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Keycloak high number of error events from a realm BETA Keycloak impossible user travel detected BETA Keycloak multiple identity provider login errors detected on realm BETA Keycloak multiple login error events from the same IP address BETA Keycloak multiple users impersonated by single user BETA Keycloak user disabled by permanent lockout BETA Keycloak user disabled by temporary lockoutKinesis
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Kinesis streams should be encrypted at restKMS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> KMS key policy should not allow everyone to use it KMS keys should not be unintentionally deleted Symmetric CMKs should have encryption key rotation enabledKubernetes
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> [Deprecated The /etc/kubernetes/manifests/etcd.yaml file ownership should be root:root A Kubernetes audit policy should exist A Kubernetes user attempted to perform a high number of actions that were denied A Kubernetes user was assigned cluster administrator permissions A new Kubernetes admission controller was created All requests should not be allowed; explicit authorization should be enabled API server audit log files should be retained for at least 10 log file rotations API server audit logs should be enabled API server audit logs should be retained for at least 30 days API server should have the anonymous-auth argument set to false API server should only authorize explicitly authorized requests API server should verify the kubelet's certificate before establishing connection Application with a critical vulnerability in a container with elevated privileges Application with a critical vulnerability in a container with elevated privileges assigned to a privileged Kubernetes node Certificate-based kubelet authentication should be required Container with elevated privileges assigned to a privileged Kubernetes node Containers should not be allowed to share the host network namespace Containers should not be generally permitted to run with hostIPC flag Containers should not be run with allowPrivilegeEscalation flag set to true Containers should not be run with the hostPID flag set to true Controller Manager profiling should be disabled Each controller should use individual service account credentials Each controller should use individual service account credentials Etcd data directory should have permissions of 700 or more restrictive Etcd key-value store should be encrypted at rest Etcd key-value store should be encrypted at rest Etcd pod specification file should have permissions of 600 or more restrictive Etcd server should require API servers to present a client certificate and key when connecting etcd servers should make use of TLS encryption for client connections Etcd service should have client authentication enabled Etcd should be configured for peer authentication Etcd should be configured with TLS encryption Etcd should have client authentication enabled Etcd should have peer authentication configured Etcd should only allow the use of valid client certificates etcd should use TLS encryption for client connections Etcd should use TLS encryption for peer connections Etcd should use TLS encryption for peer connections Ingress NGINX Controller pod is vulnerable to critical remote code execution vulnerability (IngressNightmare) Kube-proxy configuration file ownership should be assigned to root Kube-proxy configuration file should have permissions of 600 or more restrictive Kubelet authentication should require certificate-based authentication Kubelet client certificate rotation should be enabled Kubelet connections should use HTTPS for enhanced security Kubelet default kernel parameter values should be protected from overriding. Kubelet nodes should only be authorized to read objects they are associated with Kubelet nodes should only read objects associated with them Kubelet server certificate rotation should be enabled Kubelet should be able to manage changes to iptables Kubelet should enable authentication using certificates for TLS client authentication Kubelet should only allow explicitly authorized requests Kubelet should require HTTPS connections Kubelet should use TLS certificate client authentication Kubelets should be allowed to manage changes to the iptables Kubelets should have HTTPS connections with TLS setup Kubernetes API server profiling should be disabled Kubernetes PKI certificate files should have permissions of 600 or more restrictive Kubernetes PKI certificate files should have permissions of 644 or more restrictive Kubernetes Pod Created in Kube Namespace Kubernetes Pod Created with hostNetwork Kubernetes principal attempted to enumerate their permissions Kubernetes Service Account Created in Kube Namespace Kubernetes Service Created with NodePort Log files for the API server should be rotated at 100 MB Logs for API server audits should be retained for 30 days Network policies should be defined to isolate traffic in cluster network New Kubernetes Namespace Created New Kubernetes privileged pod created Pods should use `root-ca-file` to pass serving certificates to the API server Pods should verify the API server's serving certificate before connecting PodSecurityPolicy should be enabled to reject non-compliant pod creations Profiling for API server should be disabled, if not needed Publicly accessible application in a container with elevated privileges assigned to a privileged Kubernetes node Publicly accessible application in container with elevated privileges Publicly accessible application with a critical vulnerability in a container with elevated privileges Publicly accessible application with a critical vulnerability running on a privileged Kubernetes node RBAC should be enabled for the API server RBAC should be enabled for the Kubernetes API server Resources should be created in a non-default namespace in Kubernetes Scheduler profiling should be disabled Scheduler profiling should be disabled Scheduler.conf file should only be alterable by owners with permissions of 644 or more restrictive Self-signed certificates should not be used for etcd TLS Service accounts management should be automated Service accounts on the controller manager should have a private key file set Streaming connections should have timeouts enabled Streaming connections should have timeouts enabled and not be disabled The --audit-policy-file flag should be set for Kubernetes logging to be enabled The /etc/kubernetes/manifests/etcd.yaml file should have permissions of 644 or stricter The `admin.conf` file should be owned by root The `admin.conf` file should have permissions of 600 or more restrictive The `controller-manager.conf` file should be owned by root The `controller-manager.conf` file should have permissions of 600 or more restrictive The admin.conf file should have permissions of 644 or more restrictive The API server audit log files should be rotated once the file reaches 100 MB or more The API server pod specification file ownership should be assigned to root The API server pod specification file should have permissions of 600 or more restrictive The API server should explicitly set a service account public key file The API server should have a TLS connection setup The API server should not allow anonymous requests to Kubelet The API server should not use basic authentication The API server should only bind to secure, known ports The API Server should require HTTPS connections The API server should set up TLS connection for client authentication The API server should use secure authentication methods without token based authentication The API server should validate the service account token in etcd The API server should verify the kubelet's certificate before connecting The certificate authorities file should be owned by root:root The certificate authorities file should have permissions of 600 or more restrictive The certificate authorities file should have permissions of 644 or stricter The client certificate authorities file should be owned by root The Controller Manager API service should be bound to localhost The Controller Manager API service should only bind to localhost The controller manager pod specification file ownership should be root:root The controller manager pod specification file should be owned by root The controller manager pod specification file should have permissions of 600 or more restrictive The Controller Manager profiling should be disabled The controller manager should have a service account private key file set The controller-manager.conf file should be owned by root:root The controller-manager.conf file should have permissions of 644 or more restrictive The default service account should not be used The etcd data directory should be owned by etcd:etcd The etcd data directory should be owned by the etcd user and group The etcd data directory should have permissions of 700 or more restrictive The etcd pod specification file should be owned by root The etcd server should require API servers to present an SSL CA file when connecting The etcd service should be configured with TLS encryption The global request timeout for API server requests should be set appropriately The insecure API service should not be bound The kube-proxy configuration file should be owned by root:root The kubelet client certificate rotation should be enabled The kubelet configuration file should be owned by root The kubelet configuration file should be owned by root:root The kubelet configuration file should have permissions of 600 or more restrictive The kubelet configuration file should have permissions of 644 or more restrictive The kubelet read-only port should be disabled The kubelet server certificate rotation on controller-manager should be enabled The kubelet server certificate rotation on the controller-manager should be enabled The kubelet server certificate rotation should be enabled The kubelet service file should be owned by root The kubelet service file should be owned by root:root The kubelet service file should have permissions of 600 or more restrictive The kubelet service file should have permissions of 644 or stricter The kubelet.conf file should be owned by root The kubelet.conf file should be owned by root The kubelet.conf file should have permissions of 600 or more restrictive The kubelet.conf file should have permissions of 644 or stricter The Kubernetes admission controller 'AlwaysAdmit' should be disabled The Kubernetes admission controller 'NamespaceLifecycle' should be enabled The Kubernetes admission controller 'NodeRestriction' should be enabled The Kubernetes API server request timeout should not exceed 60 seconds The Kubernetes API server secure port should be enabled The Kubernetes API Server should enable audit logs on its server The Kubernetes API server should only allow explicitly authorized requests The Kubernetes API server should use a service account public key file for service accounts The Kubernetes API server should use secure authentication methods and avoid using token-based authentication The Kubernetes API server should use TLS certificate client authentication The Kubernetes API server should validate that the service account token exists in etcd The Kubernetes PKI directories should be owned by root The Kubernetes PKI directory should be owned by root The misconfigured resource should retain at least 10 log file rotations The ownership of the admin.conf file should be root:root The proxy kubeconfig file should have permissions of 644 or stricter The read-only port should be disabled in Kubelet The scheduler API service should not be bound to non-loopback insecure addresses The scheduler configuration file ownership should be assigned to root The scheduler configuration file should only be alterable by owners The scheduler pod specification file ownership should be assigned to root The scheduler pod specification file ownership should be set to root The scheduler pod specification file should have permissions of 600 or more restrictive The scheduler pod specification file should have permissions of 644 or stricter The scheduler service should only be bound to localhost The scheduler.conf file should be owned by root:root The secure port should not be disabled for the API server TLS connections between etcd peers should not use self-signed certificates TLS connections between etcd peers should not use self-signed certificates that are automatically generated User Attached to a Pod User Exec into a PodLambda
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Lambda function should have access to VPC resources in configuration Lambda function should not be accessible over the public internet Lambda function should use the latest runtime environment version Lambda functions should not be configured with a privileged execution role Publicly accessible Lambda function uses a privileged IAM role Publicly accessible Lambda function with a critical vulnerability uses a privileged IAM role VPC Lambda functions should operate in multiple Availability ZonesLastpass
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> LastPass activity from a potentially malicious IP address LastPass activity from a Tor client IP address LastPass brute force attempt LastPass user impossible travel detected LastPass vault content export attemptMeraki
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Cisco Meraki organization appliance security IDS eventsMicrosoft 365
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> A Microsoft Teams member was made owner of multiple teams A new Microsoft 365 application was installed A new Microsoft Teams app or bot was observed A potentially malicious file was sent in a Microsoft Teams message Abnormal successful Microsoft 365 Exchange login event An external Microsoft Teams member was added then removed Consent given to application associated with business email compromise attacks in Microsoft 365 Exchange Online mail forwarding rule enabled Microsoft 365 Anomalous Amount of Deleted Emails Microsoft 365 Anomalous Amount of Downloaded files Microsoft 365 Copilot interaction flagged as indirect attack Microsoft 365 Copilot Studio agent access control policy set to open Microsoft 365 Copilot Studio agent authentication modified Microsoft 365 Copilot Studio agent sign-in topic modified Microsoft 365 Copilot Studio Application Insights logging modified Microsoft 365 Default or Anonymous user permissions added to mailbox folder Microsoft 365 eDiscovery content search started Microsoft 365 eDiscovery search export downloaded Microsoft 365 Exchange inbox rule name associated with business email compromise attacks Microsoft 365 Exchange inbox rule set up to automatically forward email Microsoft 365 Exchange inbox rule set up to hide email Microsoft 365 Exchange junk email settings modified by a suspicious VPN Microsoft 365 Exchange transport rule set up to automatically forward email Microsoft 365 Full Access delegate permissions added Microsoft 365 Inbound Connector added or modified Microsoft 365 mailbox audit logging bypass Microsoft 365 OneDrive anonymous link created Microsoft 365 Security and Compliance Microsoft 365 SendAs permissions added Microsoft 365 SharePoint object shared with guest Microsoft 365 Unified Audit Logging Disabled Multiple Microsoft Teams deleted Unusual Authentication by Microsoft 365 Azure AD Service PrincipalMicrosoft Defender For Cloud
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Microsoft Defender for CloudMicrosoft Graph
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Microsoft graph security alertsMimecast
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Mimecast Alert: email contains malicious file BETA Mimecast Alert: malicious URL clicked by user BETA Mimecast Alert: phishing email detected BETA Mimecast Alert: user responded to impersonation messageMulti Log Sources
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Activity observed from malicious IP BETA Activity observed to a malicious domain BETA Administrative privileges assigned to a user, group or role Base64 was detected in an http.user_agent or http.referrer BETA Brute force attack detected against user account BETA Brute force attempt from suspicious IP by user email Credential stuffing attack Impossible travel event observed across multiple sources Log4j Scanner detected in user agent or referrer Log4Shell Scanning Detected BETA Login activity observed from Tor client IP BETA Password spray attack observed BETA Penetration testing user agent identified Potential cryptomining detected through IP callback Scout Suite user agent observed Spring RCE post-exploitation activity attempted Stratus Red Team usage User agent associated with penetration testing tool observedMysql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Malicious IP connected to MySQL databaseNeptune
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Neptune cluster snapshots should not be shared with external accounts Neptune DB cluster snapshots should be encrypted at rest Neptune DB cluster snapshots should not be public Neptune DB clusters should be configured to copy tags to snapshots Neptune DB clusters should be deployed across multiple Availability Zones Neptune DB clusters should be encrypted at rest Neptune DB clusters should have automated backups enabled Neptune DB clusters should have deletion protection enabled Neptune DB clusters should have IAM database authentication enabled Neptune DB clusters should publish audit logs to CloudWatch LogsNetskope
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Netskope detected JA3 hash from multiple client IPsNginx
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> NGINX HTTP requests from security scannerNginx Ingress Controller
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> NGINX ingress controller HTTP requests from security scannerOkta
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Malicious authentication attempt detected by Okta ThreatInsight Multiple Okta push notifications denied followed by a successful login Okta Active Directory environment linked Okta admin console activity from new device Okta administrator role assigned to user Okta API Token Created or Enabled Okta application enumeration by user Okta blocked numerous requests from a malicious IP Okta Desktop Single Sign On (DSSO) from unexpected profile source Okta Identity Provider creation or modification Okta IDP creation followed by failed authentication attempts Okta Impersonation Okta MFA Bypass Attempted Okta MFA reset for user Okta OAuth mismatched URI Okta one-time refresh token reused Okta OPA server account password changed out of band Okta Org2Org application user syncing Okta phishing detection with FastPass origin check Okta phone number assigned to multiple users Okta policy rule deleted Okta policy rule modified to downgrade MFA BETA Okta session hijacking Okta temporary AWS credentials granted using open source tooling Okta temporary password granted and MFA reset Okta User Access Denied to Sign On Okta User Attempted to Access Unauthorized App Okta User Identity Verification failure Okta user reported suspicious activity Okta user's MFA factors reset followed by access to the administrative consoleOnelogin
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> OneLogin administrator assumed a user OneLogin API activity from malicious IP address OneLogin API Token Created OneLogin brute force attack on user OneLogin user granted administrative privileges OneLogin user locked out OneLogin user viewed secure noteOpensearch
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> OpenSearch domain connections should be encrypted using the latest TLS security policy OpenSearch domains should be deployed within a VPC OpenSearch domains should encrypt data sent between nodes OpenSearch domains should have at least three data nodes OpenSearch domains should have Audit Logging enabled OpenSearch domains should have encryption at rest enabled OpenSearch domains should have Error Logging enabled OpenSearch domains should have fine-grained access control enabled OpenSearch domains should have the latest software update installedOracle Cloud Infrastructure
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Anomalous number of instances with high GPU created BETA Anomalous number of OCI instances created in multiple availability domains BETA OCI ConsoleLogin without MFA triggered Impossible Travel scenario BETA Oracle Cloud user failed login followed by success BETA Oracle Cloud user requested to create or reset password from malicious IP BETA Possible brute force attempted against user BETA Possible enumeration activity from anomalous number of access denied errorsOrca Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Orca Security CDR alert detectedOssec Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA OSSEC Alert: Attack detected BETA OSSEC Alert: Multiple authentication failures BETA OSSEC Alert: Multiple authentication failures followed by a success BETA OSSEC Alert: OSSEC agent disconnected BETA OSSEC Alert: Possible attack detected BETA OSSEC Alert: Unusual spike in authentication failurePalo Alto Cortex Xdr
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Palo Alto Cortex XDR malware alert detected on multiple hosts BETA Palo Alto Cortex XDR: New incident detectedPan.firewall
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Palo Alto Networks Firewall - command and control traffic observed Palo Alto Networks Firewall - crypto mining activity observedPing Federate
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA PingFederate Admin Alert: impossible travel by user BETA PingFederate Admin Alert: multiple failed login attempts in a short time period BETA PingFederate Admin Alert: multiple login attempts by locked account in a short time period BETA PingFederate Audit Alert: multiple failed authentication attempts in a short time period BETA PingFederate Audit Alert: multiple failed slo login attempts in a short time period BETA PingFederate Audit Alert: multiple failed sso login attempts in a short time periodPing One
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA PingOne device locked out after too many failed attempts BETA PingOne impossible travel authentication attempt BETA PingOne impossible travel authentication attempts by OTP BETA PingOne multiple authentication assertions failed by FIDO device BETA PingOne multiple failed authentication attempts BETA PingOne multiple failed authentication attempts by OTP BETA PingOne multiple Kerberos check failed attempts BETA PingOne user locked after too many failed attemptsPostgresql
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Malicious IP connected to PostgreSQL databaseRDS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Aurora clusters should have backtracking enabled Aurora MySQL clusters should publish audit logs to CloudWatch Logs Neptune cluster replicates to a publicly accessible Neptune instance Publicly accessible RDS database stores sensitive data Publicly Accessible RDS instance uses a common master database username RDS cluster exports snapshots to publicly accessible S3 bucket RDS cluster replicates to a publicly accessible RDS instance RDS cluster snapshots should be encrypted at rest RDS cluster snapshots should not be publicly shared RDS cluster snapshots should not be shared with external accounts RDS clusters should be configured to copy tags to snapshots RDS clusters should be configured to use a custom administrator name RDS clusters should be configured to use multiple Availability Zones RDS clusters should have Auto Minor Version Upgrade enabled RDS clusters should have deletion protection enabled RDS clusters should have encryption at rest enabled RDS clusters should have IAM authentication enabled RDS clusters should use KMS encryption RDS databases should be encrypted RDS databases should have 'Auto Minor Version Upgrade' enabled RDS databases should not be publicly accessible RDS event subscriptions should be configured to notify for critical database parameter group events RDS event subscriptions should be configured to notify for critical database security group events RDS event subscriptions should be configured to notify for critical events RDS instance snapshots should be encrypted at rest RDS instance snapshots should not be publicly shared RDS instance snapshots should not be shared with external accounts RDS instances should be configured to copy tags to snapshots RDS instances should be configured to use a custom administrator name RDS instances should be configured to use Enhanced Monitoring RDS instances should be configured to use multiple Availability Zones RDS instances should be deployed inside of a VPC RDS instances should have automatic backups enabled RDS instances should have deletion protection enabled RDS instances should have IAM authentication enabled RDS instances should publish logs to CloudWatch Logs RDS instances should use a non-default port RDS logs should be collected and retained for no less than 90 daysRedshift
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Logging for Redshift clusters should be enabled Redshift cluster snapshots should not be shared with external accounts Redshift clusters should be encrypted Redshift clusters should enable SSL/TLS for client connections Redshift clusters should enforce encryption in transit Redshift clusters should have 'allow version upgrade' enabled Redshift clusters should have automatic snapshots enabled Redshift clusters should not be publicly accessible Redshift clusters should not use the default database name Redshift clusters should use a custom master username Redshift clusters should use a non-default port for communication Redshift clusters should use enhanced VPC routing Redshift clusters should use the EC2-VPC platform for better security Redshift Serverless snapshots should not be shared with external accountsRoute53
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Route 53 DNS record pointing to external or nonexistent S3 bucket Route 53 public hosted zones should log DNS queriesS3
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Default encryption should be enabled on S3 buckets Publicly accessible S3 bucket stores sensitive data S3 Block Public Access feature should be enabled at the account level S3 bucket ACLs should be restricted from public view S3 bucket ACLs should block public write actions S3 bucket contents should only be accessible by authorized principals S3 bucket objects should not allow public listing via ACL S3 bucket policies should restrict access from other AWS accounts S3 bucket policy should deny HTTP requests S3 bucket policy should prevent public write access S3 buckets should have 'Block Public Access' enabled S3 buckets should have 'MFA Delete' enabled S3 buckets should have versioning enabled S3 general purpose buckets should have a lifecycle configuration S3 general purpose buckets should have static website hosting disabledSagemaker
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SageMaker notebook instances should be launched in a custom VPC SageMaker notebook instances should not grant users root access SageMaker notebook instances should not have direct internet accessSalesforce
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Anomalous amount of Salesforce query results Anomalous amount of Salesforce records deleted Credential stuffing attack on Salesforce Salesforce anomalous amount of queried tables Salesforce Brute force attack on user Salesforce discovery of populated tables from unseen network and device Salesforce large-sized chunk exfiltration through GET requests Salesforce login from disabled account Salesforce login from unseen application Salesforce previously unseen network for application OAuth token login Salesforce unusual CLI activitySecretsmanager
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Remove unused Secrets Manager secrets Secrets Manager secrets configured with automatic rotation should rotate successfully Secrets Manager secrets should be rotated within 90 days Secrets Manager secrets should have automatic rotation enabledSentinelone
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Credential access via registry hive dumping BETA Process memory dumped using ProcDump BETA Process memory dumped using the minidump function of comsvcs.dll SentinelOne Alerts SentinelOne Threats BETA Unusual ntdsutil usage BETA Windows shadow copies deletedSES
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SES should use Email Address IdentitiesSignal Sciences
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Signal Sciences flagged an IPSlack
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Microsoft Intune Enterprise MDM disabled for Slack Slack anomaly event Slack Brute force attack on user Slack CLI login from suspicious IP address Slack data export download Slack data loss prevention rule modified Slack enterprise organization created or deleted Slack enterprise workspace created or deleted Slack IdP configuration changed Slack malicious content detected in uploaded file Slack private channel converted to public Slack SSO setting changed Slack two factor authentication requirement changed Slack user logout due to suspicious activity Slack user role elevated to administrative privileges Tor client IP address identified in SlackSnowflake
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Snowflake abnormal usage of OAuth access token Snowflake anomalous querying of data by user Snowflake brute force attack on user Snowflake external access occurred Snowflake known malicious client application session Snowflake login from anomalous location Snowflake network policy modified Snowflake new client application sessions Snowflake new data transfer to location Snowflake stage set to anomalous external cloud location Snowflake UI login via password Snowflake UI login via password from proxy or vpn Snowflake user granted admin roleSNS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SNS Topic should have access restrictions set for subscription SNS Topic should have restrictions set for publishing SNS Topic should have server-side encryption enabled SNS topic should not be accessible over the public internetSophos Central Cloud
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Sophos Alert: Core clean up failed BETA Sophos Central Cloud alertSQS
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> SQS queue should have server-side encryption SQS queue should not be accessible over the public internetSSH
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> IAM SSH public keys should be rotated at least every 90 days No more than one active SSH public key should be assigned to a single userSSM
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EC2 instances managed by SSM should have a compliant association status EC2 instances managed by SSM should have a compliant patch status EC2 instances should be managed by SSMSupply Chain Firewall
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Supply-Chain Firewall blocked package manager command Supply-Chain Firewall unverified package manager commandSuricata
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Suricata anomaly detected from source IP address Suricata baseline deviation from expected IP requests Suricata high number of bytes out detected Suricata high number of requests detected from single IP address Suricata possible ARP spoofing detectedSymantec Vip
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Symantec VIP multiple mobile push request denied by the user followed by successful login BETA Symantec VIP multiple numbers challenge failed events BETA Symantec VIP unusual spike in authentication failed eventsTailscale
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Tailscale API access token created Tailscale device approval configuration disabled Tailscale security email modified Tailscale user approval configuration disabled Tailscale user role updatedTrellix Endpoint Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Trellix Endpoint Security blocked web control violation detected BETA Trellix Endpoint Security suspicious call was detected and blocked BETA Trellix Endpoint Security tampering with exploit prevention has been detected BETA Trellix Endpoint Security unauthorized escalation of privilege was attempt detected BETA Trellix Endpoint Security unrestricted access protection rule violation detected BETA Trellix Endpoint Security unrestricted port blocking rule violation detectedTrend Micro Email Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Trend Micro Email Security alert: High volume of emails from sender BETA Trend Micro Email Security alert: High volume of emails to recipient BETA Trend Micro Email Security alert: Phishing email detectedTrend Micro Vision One Endpoint Security
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Trend Micro Vision One Endpoint Security alert: Content violation detected BETA Trend Micro Vision One Endpoint Security alert: Spyware or grayware detected BETA Trend Micro Vision One Endpoint Security alert: Suspicious file detected BETA Trend Micro Vision One Endpoint Security alert: Virus or malware detectedTrend Micro Vision One Xdr
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Trend Micro Vision One XDR alert BETA Trend Micro Vision One XDR impossible travel detected for identity activityTwilio
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Twilio account geographic permissions updated Twilio account token promoted Twilio bulk export from unusual locationTwistlock
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Container image vulnerability detected Container violated compliance standardsVault
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Vault root tokenVPC
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> EC2 should be configured to use AWS VPC endpoints created for the Amazon EC2 service Network ACLs should enforce inbound traffic restrictions Network ACLs should enforce outbound traffic restrictions Remote administration port access should be restricted to trusted networks VPC endpoint should restrict public access VPCs should have an interface VPC endpoint configured for SSM Incident Manager VPCs should have interface endpoint for Amazon ECR API VPCs should have interface endpoint for ECR Docker Registry VPCs should have interface endpoint for SSM VPCs should have interface endpoint for SSM ContactsVPN
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Site-to-Site VPN connection tunnels should be onlineWAF
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> WAF Classic rule groups should be migrated to WAFv2 WAF Classic rules should be migrated to WAFv2 WAF Classic web ACLs should be migrated to WAFv2 WAF rules should have CloudWatch metrics enabled WAF web ACLs should have at least one rule or rule groupWindows
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Multiple failed login attempts PsExec execution detected Suspicious named pipe created BETA Windows active directory object WriteDAC access BETA Windows active directory privileged users or groups reconnaissance BETA Windows active directory replication from non machine account BETA Windows active directory user assigned right to control user objects BETA Windows active directory user backdoors BETA Windows ANONYMOUS LOGON local account created Windows audit log cleared BETA Windows BITS transfer job download from direct IP BETA Windows BITS transfer job downloaded to suspicious folder BETA Windows CobaltStrike service installations BETA Windows CrackMapExec execution patterns BETA Windows credential dumping tools service execution BETA Windows credential dumping via WER application error BETA Windows critical hive in suspicious location access bits cleared BETA Windows delete volume shadow copies via WMI with PowerShell BETA Windows device installation blocked BETA Windows DHCP server error loaded CallOut DLL BETA Windows DHCP server loaded CallOut DLL BETA Windows DiagTrackEoP default login username BETA Windows DNS query to Tor Onion address Windows Domain Admin group changed BETA Windows eventlog cleared Windows firewall disabled BETA Windows fsutil suspicious invocation BETA Windows hidden local user creation BETA Windows HybridConnectionManager service running BETA Windows Impacket PsExec execution BETA Windows important scheduled task deleted or disabled BETA Windows Kerberoasting RC4 encrypted tickets BETA Windows malware protection engine crash BETA Windows moriya rootkit BETA Windows MSI installation from web BETA Windows MSSQL add sysadmin account BETA Windows MSSQL disable audit settings BETA Windows MSSQL SPProcoption set BETA Windows MSSQL XPCmdshell change Windows MSSQL XPCmdshell suspicious execution Windows Net command executed to enumerate administrators BETA Windows NoFilter tool execution BETA Windows OpenSSH brute force attempt BETA Windows OpenSSH server listening on socket BETA Windows password change on directory service restore account BETA Windows password protected ZIP file opened with suspicious email attachments BETA Windows password protected ZIP file opened with suspicious filenames BETA Windows persistence via sticky key backdoor BETA Windows potential lsass process dump via procdump BETA Windows potential powershell reverseshell connection BETA Windows PowerShell AADInternals cmdlets execution BETA Windows PowerShell create volume shadow copy BETA Windows PowerShell disable command history BETA Windows PowerShell disable ETW trace BETA Windows PowerShell Disable-WindowsOptionalFeature command BETA Windows PowerShell Invoke-Mimikatz script BETA Windows PowerShell PSAsyncShell asynchronous TCP reverse shell BETA Windows PowerShell Rubeus execution BETA Windows PowerShell scripts installed as services Windows PowerShell Set-Acl on folder BETA Windows PowerShell suspicious Get-ADDBAccount usage BETA Windows PowerShell Veeam backup servers credential dumping script execution BETA Windows PowerShell volume shadow copy deletion BETA Windows PowerShell web access installation using PsScript BETA Windows privilege escalation via local kerberos relay over LDAP BETA Windows protected storage service access BETA Windows PurpleSharp execution BETA Windows register new logon process by Rubeus BETA Windows remote access tool ScreenConnect file transfer BETA Windows replay attack detected BETA Windows restricted software access by the Software Restriction Policies BETA Windows RottenPotato like attack pattern BETA Windows SAM registry hive handle request BETA Windows self extraction directive file created BETA Windows service installed by suspicious client BETA Windows shadow copies deletion using operating systems utilities BETA Windows shimcache flush BETA Windows SMB create remote file admin share BETA Windows suspicious computer name containing Samtheadmin BETA Windows suspicious PowerShell mailbox export to share Windows suspicious Teams application related ObjectAccess event BETA Windows syskey registry keys access Windows user added to Domain Admin group BETA Windows VolumeShadowCopy symlink creation via mklink Windows vulnerable spn enumerated BETA Windows WCE wceaux.dll access BETA Windows WinPwn execution patterns BETA Windows WMI backdoor exchange transport agentWindows File Integrity Monitoring
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Critical windows file modified Windows boot registry key modified Windows COM RPC debugging registry key modified Windows explorer executable modified Windows firewall configuration registry key modified Windows hosts file modified Windows known DLLs registry key modified Windows registry hives file paths key modified Windows security essentials executable modified Windows shell folders registry key modified Windows system environment variables modified Winlogon registry key modifiedWindows Workload Protection
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Bitsadmin used to download or execute a file Certutil used to transmit or decode a file NTDS file referenced in command line Process memory dumped using procdump Process memory dumped using the minidump functions of comsvcs.dll Scheduled task created Suspicous ntdsutil usage WMI used to remotely execute contentWIZ
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Impossible travel scenario observed in Wiz authentication Wiz Defend Detections alert Wiz Defend Threats alert Wiz Issues alerts BETA Wiz threat findingWorkload Protection
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> AppArmor profile modified Auditd configuration modified Bring your own file system (BYOF) tool executed Cloud credentials accessed by network utility Compiler executed in container Compiler wrote suspicious file Container accessed using kubectl in another container Container breakout attempt using container management socket Container breakout using runc file descriptors Container management utility in container Crypto miner environment variables observed Crypto miner process observed Cryptocurrency miner attempted to boost CPU performance Database process spawned shell DNS lookup for cryptocurrency mining pool DNS lookup for IP lookup service DNS lookup for paste service Dynamic linker hijacking attempt Evidence hidden by deleting system log file Executable bit added to newly created file Exfiltration attempt via network utility Hash of known malware detected Interactive shell spawned in container Kubernetes DNS enumeration Kubernetes service account token created in container Local account password modified Looney Tunables (CVE-2023-4911) exploited for privilege escalation Memfd object created Network scanning utility executed Network utility executed Network utility executed in container Network utility executed with suspicious URI Offensive Kubernetes tool executed Package installed in container PAM authentication library hooked using eBPF Post compromise shell detected Potential rootkit compiled and then loaded Process hidden using mount Pwnkit privilege escalation attempt Python executed with suspicious arguments Recently written or modified suid file has been executed Redis modified cron job directory to execute commands Redis sandbox escape (CVE-2022-0543) Redis server wrote suspicious module file Resource provisioned using kubectl in container Runc binary modified SELinux enforcement disabled Sensitive namespace modified using kubectl Shell process created by Java application Unfamiliar kernel module loaded Unfamiliar kernel module loaded from memory Unfamiliar process accessed AWS EKS service account token Unfamiliar process created by web application User created interactivelyWorkload Activity
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Containers should not execute compilers Containers should not execute mount system calls Linux Hardening: LOCKDOWN mode should be 'none confidentiality' Verify Essential Linux Binary Modified in Container Verify Essential Linux Binary Modified on Host Verify Non-Root Password Modifications on Host Verify Root Account Password Modifications on Host Verify SSH Keys Modified on Host Verify SSL Certificate Modified on Host Verify Sudoers Policy File Modifications Verify Systemd Service Modified on Host Verify User Account Creation on Host Verify User Permission Modifications on HostZeek
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Anomalous failed SSH authentication attempts by a single IP address Generic DNS tunnel detected by Zeek SSH interesting hostname login notice from Zeek SSH login by password guesser from Zeek SSH password guessing notice from Zeek SSH watched country login notice from ZeekZendesk
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> Zendesk account assumption is enabled Zendesk API token is created Zendesk Automatic Redaction is disabled Zendesk IP restriction settings is disabled Zendesk user's suspension status is changedZoom
{% icon name="icon-click" /%}

{% icon name="icon-check-bold" /%}
\> BETA Zoom account sign in requirements changed BETA Zoom user updated to privileged role