# API Reference | Cloudflare API

Source: https://developers.cloudflare.com/api/

# API Reference

### Libraries
  TypeScript6.0.0-beta.1
```
npm install cloudflare
```
 [][Read Docs]Python5.0.0-beta.1
```
pip install cloudflare
```
 [][Read Docs]Go6.8.0
```
go get -u 'github.com/cloudflare/cloudflare-go@v0.0.1'
```
 [][Read Docs]Terraform5.19.0-beta.4
```
cloudflare = { source = "cloudflare/cloudflare" }
```
 [][Read Docs]
### API Overview

#### Accounts

##### [List Accounts]
GET/accounts
##### [Account Details]
GET/accounts/{account_id}
##### [Create an account]
POST/accounts
##### [Update Account]
PUT/accounts/{account_id}
##### [Delete a specific account]
DELETE/accounts/{account_id}
#### AccountsAccount Organizations

##### [Move account]
POST/accounts/{account_id}/move
#### AccountsAccount Profile

##### [Get account profile]
GET/accounts/{account_id}/profile
##### [Modify account profile]
PUT/accounts/{account_id}/profile
#### AccountsMembers

##### [List Members]
GET/accounts/{account_id}/members
##### [Member Details]
GET/accounts/{account_id}/members/{member_id}
##### [Add Member]
POST/accounts/{account_id}/members
##### [Update Member]
PUT/accounts/{account_id}/members/{member_id}
##### [Remove Member]
DELETE/accounts/{account_id}/members/{member_id}
#### AccountsRoles

##### [List Roles]
GET/accounts/{account_id}/roles
##### [Role Details]
GET/accounts/{account_id}/roles/{role_id}
#### AccountsSubscriptions

##### [List Subscriptions]
GET/accounts/{account_id}/subscriptions
##### [Create Subscription]
POST/accounts/{account_id}/subscriptions
##### [Update Subscription]
PUT/accounts/{account_id}/subscriptions/{subscription_identifier}
##### [Delete Subscription]
DELETE/accounts/{account_id}/subscriptions/{subscription_identifier}
#### AccountsTokens

##### [List Tokens]
GET/accounts/{account_id}/tokens
##### [Token Details]
GET/accounts/{account_id}/tokens/{token_id}
##### [Create Token]
POST/accounts/{account_id}/tokens
##### [Update Token]
PUT/accounts/{account_id}/tokens/{token_id}
##### [Delete Token]
DELETE/accounts/{account_id}/tokens/{token_id}
##### [Verify Token]
GET/accounts/{account_id}/tokens/verify
#### AccountsTokensPermission Groups

##### [List Permission Groups]
GET/accounts/{account_id}/tokens/permission_groups
##### [List Permission Groups]
GET/accounts/{account_id}/tokens/permission_groups
#### AccountsTokensValue

##### [Roll Token]
PUT/accounts/{account_id}/tokens/{token_id}/value
#### AccountsLogs

#### AccountsLogsAudit

##### [Get account audit logs (Version 2)]
GET/accounts/{account_id}/logs/audit
#### Organizations

##### [List organizations the user has access to]
GET/organizations
##### [Get organization]
GET/organizations/{organization_id}
##### [Create organization]
POST/organizations
##### [Modify organization.]
PUT/organizations/{organization_id}
##### [Delete organization.]
DELETE/organizations/{organization_id}
#### OrganizationsOrganization Accounts

##### [Get organization accounts]
GET/organizations/{organization_id}/accounts
#### OrganizationsOrganization Profile

##### [Get organization profile]
GET/organizations/{organization_id}/profile
##### [Modify organization profile.]
PUT/organizations/{organization_id}/profile
#### OrganizationsMembers

##### [List organization members]
GET/organizations/{organization_id}/members
##### [Get organization member]
GET/organizations/{organization_id}/members/{member_id}
##### [Create organization member]
POST/organizations/{organization_id}/members
##### [Delete organization member]
DELETE/organizations/{organization_id}/members/{member_id}
#### Origin CA Certificates

##### [List Certificates]
GET/certificates
##### [Get Certificate]
GET/certificates/{certificate_id}
##### [Create Certificate]
POST/certificates
##### [Revoke Certificate]
DELETE/certificates/{certificate_id}
#### IPs

##### [Cloudflare/JD Cloud IP Details]
GET/ips
#### Memberships

##### [List Memberships]
GET/memberships
##### [Membership Details]
GET/memberships/{membership_id}
##### [Update Membership]
PUT/memberships/{membership_id}
##### [Delete Membership]
DELETE/memberships/{membership_id}
#### User

##### [User Details]
GET/user
##### [Edit User]
PATCH/user
#### UserAudit Logs

##### [Get user audit logs]
GET/user/audit_logs
#### UserBilling

#### UserBillingHistory

##### [Billing History Details]
DeprecatedGET/user/billing/history
#### UserBillingProfile

##### [Billing Profile Details]
DeprecatedGET/user/billing/profile
#### UserInvites

##### [List Invitations]
GET/user/invites
##### [Invitation Details]
GET/user/invites/{invite_id}
##### [Respond to Invitation]
PATCH/user/invites/{invite_id}
#### UserOrganizations

##### [List Organizations]
DeprecatedGET/user/organizations
##### [Organization Details]
DeprecatedGET/user/organizations/{organization_id}
##### [Leave Organization]
DeprecatedDELETE/user/organizations/{organization_id}
#### UserSubscriptions

##### [Get User Subscriptions]
GET/user/subscriptions
##### [Update User Subscription]
PUT/user/subscriptions/{identifier}
##### [Delete User Subscription]
DELETE/user/subscriptions/{identifier}
#### UserTokens

##### [List Tokens]
GET/user/tokens
##### [Token Details]
GET/user/tokens/{token_id}
##### [Create Token]
POST/user/tokens
##### [Update Token]
PUT/user/tokens/{token_id}
##### [Delete Token]
DELETE/user/tokens/{token_id}
##### [Verify Token]
GET/user/tokens/verify
#### UserTokensPermission Groups

##### [List Token Permission Groups]
GET/user/tokens/permission_groups
#### UserTokensValue

##### [Roll Token]
PUT/user/tokens/{token_id}/value
#### Zones

##### [List Zones]
GET/zones
##### [Zone Details]
GET/zones/{zone_id}
##### [Create Zone]
POST/zones
##### [Edit Zone]
PATCH/zones/{zone_id}
##### [Delete Zone]
DELETE/zones/{zone_id}
#### ZonesActivation Check

##### [Rerun the Activation Check]
PUT/zones/{zone_id}/activation_check
#### ZonesSettings

##### [Get all zone settings]
DeprecatedGET/zones/{zone_id}/settings
##### [Get zone setting]
GET/zones/{zone_id}/settings/{setting_id}
##### [Edit zone setting]
PATCH/zones/{zone_id}/settings/{setting_id}
##### [Edit multiple zone settings]
DeprecatedPATCH/zones/{zone_id}/settings
#### ZonesEnvironments

##### [List zone environments]
GET/zones/{zone_id}/environments
##### [Create zone environments]
POST/zones/{zone_id}/environments
##### [Upsert zone environments]
PUT/zones/{zone_id}/environments
##### [Partially update zone environments]
PATCH/zones/{zone_id}/environments
##### [Delete zone environment]
DELETE/zones/{zone_id}/environments/{environment_id}
##### [Roll back zone environment]
POST/zones/{zone_id}/environments/{environment_id}/rollback
#### ZonesCustom Nameservers

##### [Get Account Custom Nameserver Related Zone Metadata]
DeprecatedGET/zones/{zone_id}/custom_ns
##### [Set Account Custom Nameserver Related Zone Metadata]
DeprecatedPUT/zones/{zone_id}/custom_ns
#### ZonesHolds

##### [Get Zone Hold]
GET/zones/{zone_id}/hold
##### [Create Zone Hold]
POST/zones/{zone_id}/hold
##### [Update Zone Hold]
PATCH/zones/{zone_id}/hold
##### [Remove Zone Hold]
DELETE/zones/{zone_id}/hold
#### ZonesSubscriptions

##### [Zone Subscription Details]
GET/zones/{zone_id}/subscription
##### [Create Zone Subscription]
POST/zones/{zone_id}/subscription
##### [Update Zone Subscription]
PUT/zones/{zone_id}/subscription
#### ZonesPlans

##### [List Available Plans]
GET/zones/{zone_id}/available_plans
##### [Available Plan Details]
GET/zones/{zone_id}/available_plans/{plan_identifier}
#### ZonesRate Plans

##### [List Available Rate Plans]
GET/zones/{zone_id}/available_rate_plans
#### Load Balancers

##### [List Load Balancers]
GET/zones/{zone_id}/load_balancers
##### [Load Balancer Details]
GET/zones/{zone_id}/load_balancers/{load_balancer_id}
##### [Create Load Balancer]
POST/zones/{zone_id}/load_balancers
##### [Update Load Balancer]
PUT/zones/{zone_id}/load_balancers/{load_balancer_id}
##### [Patch Load Balancer]
PATCH/zones/{zone_id}/load_balancers/{load_balancer_id}
##### [Delete Load Balancer]
DELETE/zones/{zone_id}/load_balancers/{load_balancer_id}
#### Load BalancersMonitors

##### [List Monitors]
GET/accounts/{account_id}/load_balancers/monitors
##### [Monitor Details]
GET/accounts/{account_id}/load_balancers/monitors/{monitor_id}
##### [Create Monitor]
POST/accounts/{account_id}/load_balancers/monitors
##### [Update Monitor]
PUT/accounts/{account_id}/load_balancers/monitors/{monitor_id}
##### [Patch Monitor]
PATCH/accounts/{account_id}/load_balancers/monitors/{monitor_id}
##### [Delete Monitor]
DELETE/accounts/{account_id}/load_balancers/monitors/{monitor_id}
#### Load BalancersMonitorsPreviews

##### [Preview Monitor]
POST/accounts/{account_id}/load_balancers/monitors/{monitor_id}/preview
#### Load BalancersMonitorsReferences

##### [List Monitor References]
GET/accounts/{account_id}/load_balancers/monitors/{monitor_id}/references
#### Load BalancersMonitor Groups

##### [List Monitor Groups]
GET/accounts/{account_id}/load_balancers/monitor_groups
##### [Monitor Group Details]
GET/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}
##### [Create Monitor Group]
POST/accounts/{account_id}/load_balancers/monitor_groups
##### [Update Monitor Group]
PUT/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}
##### [Patch Monitor Group]
PATCH/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}
##### [Delete Monitor Group]
DELETE/accounts/{account_id}/load_balancers/monitor_groups/{monitor_group_id}
#### Load BalancersPools

##### [List Pools]
GET/accounts/{account_id}/load_balancers/pools
##### [Pool Details]
GET/accounts/{account_id}/load_balancers/pools/{pool_id}
##### [Create Pool]
POST/accounts/{account_id}/load_balancers/pools
##### [Update Pool]
PUT/accounts/{account_id}/load_balancers/pools/{pool_id}
##### [Patch Pool]
PATCH/accounts/{account_id}/load_balancers/pools/{pool_id}
##### [Delete Pool]
DELETE/accounts/{account_id}/load_balancers/pools/{pool_id}
##### [Patch Pools]
PATCH/accounts/{account_id}/load_balancers/pools
#### Load BalancersPoolsHealth

##### [Pool Health Details]
GET/accounts/{account_id}/load_balancers/pools/{pool_id}/health
##### [Preview Pool]
POST/accounts/{account_id}/load_balancers/pools/{pool_id}/preview
#### Load BalancersPoolsReferences

##### [List Pool References]
GET/accounts/{account_id}/load_balancers/pools/{pool_id}/references
#### Load BalancersPreviews

##### [Preview Result]
GET/accounts/{account_id}/load_balancers/preview/{preview_id}
#### Load BalancersRegions

##### [List Regions]
GET/accounts/{account_id}/load_balancers/regions
##### [Get Region]
GET/accounts/{account_id}/load_balancers/regions/{region_id}
#### Load BalancersSearches

##### [Search Resources]
GET/accounts/{account_id}/load_balancers/search
#### Cache

##### [Purge Cached Content]
POST/zones/{zone_id}/purge_cache
#### CacheCache Reserve

##### [Get Cache Reserve setting]
GET/zones/{zone_id}/cache/cache_reserve
##### [Change Cache Reserve setting]
PATCH/zones/{zone_id}/cache/cache_reserve
##### [Get Cache Reserve Clear]
GET/zones/{zone_id}/cache/cache_reserve_clear
##### [Start Cache Reserve Clear]
POST/zones/{zone_id}/cache/cache_reserve_clear
#### CacheSmart Tiered Cache

##### [Get Smart Tiered Cache setting]
GET/zones/{zone_id}/cache/tiered_cache_smart_topology_enable
##### [Patch Smart Tiered Cache setting]
PATCH/zones/{zone_id}/cache/tiered_cache_smart_topology_enable
##### [Delete Smart Tiered Cache setting]
DELETE/zones/{zone_id}/cache/tiered_cache_smart_topology_enable
#### CacheVariants

##### [Get variants setting]
GET/zones/{zone_id}/cache/variants
##### [Change variants setting]
PATCH/zones/{zone_id}/cache/variants
##### [Delete variants setting]
DELETE/zones/{zone_id}/cache/variants
#### CacheRegional Tiered Cache

##### [Get Regional Tiered Cache setting]
GET/zones/{zone_id}/cache/regional_tiered_cache
##### [Change Regional Tiered Cache setting]
PATCH/zones/{zone_id}/cache/regional_tiered_cache
#### SSL

#### SSLAnalyze

##### [Analyze Certificate]
POST/zones/{zone_id}/ssl/analyze
#### SSLCertificate Packs

##### [List Certificate Packs]
GET/zones/{zone_id}/ssl/certificate_packs
##### [Get Certificate Pack]
GET/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
##### [Order Advanced Certificate Manager Certificate Pack]
POST/zones/{zone_id}/ssl/certificate_packs/order
##### [Restart Validation or Update Advanced Certificate Manager Certificate Pack]
PATCH/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
##### [Delete Advanced Certificate Manager Certificate Pack]
DELETE/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
#### SSLCertificate PacksQuota

##### [Get Certificate Pack Quotas]
GET/zones/{zone_id}/ssl/certificate_packs/quota
#### SSLRecommendations

##### [SSL/TLS Recommendation]
DeprecatedGET/zones/{zone_id}/ssl/recommendation
#### SSLAutomatic Upgrader

##### [Get Automatic SSL/TLS enrollment status for the given zone]
GET/zones/{zone_id}/settings/ssl_automatic_mode
##### [Patch Automatic SSL/TLS Enrollment status for given zone]
PATCH/zones/{zone_id}/settings/ssl_automatic_mode
#### SSLUniversal

#### SSLUniversalSettings

##### [Universal SSL Settings Details]
GET/zones/{zone_id}/ssl/universal/settings
##### [Edit Universal SSL Settings]
PATCH/zones/{zone_id}/ssl/universal/settings
#### SSLVerification

##### [SSL Verification Details]
GET/zones/{zone_id}/ssl/verification
##### [Edit SSL Certificate Pack Validation Method]
PATCH/zones/{zone_id}/ssl/verification/{certificate_pack_id}
#### ACM

#### ACMTotal TLS

##### [Total TLS Settings Details]
GET/zones/{zone_id}/acm/total_tls
##### [Enable or Disable Total TLS]
POST/zones/{zone_id}/acm/total_tls
##### [Enable or Disable Total TLS]
POST/zones/{zone_id}/acm/total_tls
#### ACMCustom Trust Store

##### [List Custom Origin Trust Store Details]
GET/zones/{zone_id}/acm/custom_trust_store
##### [Upload Custom Origin Trust Store]
POST/zones/{zone_id}/acm/custom_trust_store
##### [Custom Origin Trust Store Details]
GET/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}
##### [Delete Custom Origin Trust Store]
DELETE/zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}
#### Argo

#### ArgoSmart Routing

##### [Get Argo Smart Routing setting]
GET/zones/{zone_id}/argo/smart_routing
##### [Patch Argo Smart Routing setting]
PATCH/zones/{zone_id}/argo/smart_routing
#### ArgoTiered Caching

##### [Get Tiered Caching setting]
GET/zones/{zone_id}/argo/tiered_caching
##### [Patch Tiered Caching setting]
PATCH/zones/{zone_id}/argo/tiered_caching
#### Certificate Authorities

#### Certificate AuthoritiesHostname Associations

##### [List Hostname Associations]
GET/zones/{zone_id}/certificate_authorities/hostname_associations
##### [Replace Hostname Associations]
PUT/zones/{zone_id}/certificate_authorities/hostname_associations
#### Client Certificates

##### [List Client Certificates]
GET/zones/{zone_id}/client_certificates
##### [Client Certificate Details]
GET/zones/{zone_id}/client_certificates/{client_certificate_id}
##### [Create Client Certificate]
POST/zones/{zone_id}/client_certificates
##### [Reactivate Client Certificate]
PATCH/zones/{zone_id}/client_certificates/{client_certificate_id}
##### [Revoke Client Certificate]
DELETE/zones/{zone_id}/client_certificates/{client_certificate_id}
#### Custom Certificates

##### [List SSL Configurations]
GET/zones/{zone_id}/custom_certificates
##### [SSL Configuration Details]
GET/zones/{zone_id}/custom_certificates/{custom_certificate_id}
##### [Create SSL Configuration]
POST/zones/{zone_id}/custom_certificates
##### [Edit SSL Configuration]
PATCH/zones/{zone_id}/custom_certificates/{custom_certificate_id}
##### [Delete SSL Configuration]
DELETE/zones/{zone_id}/custom_certificates/{custom_certificate_id}
#### Custom CertificatesPrioritize

##### [Re-prioritize SSL Certificates]
PUT/zones/{zone_id}/custom_certificates/prioritize
#### Custom Hostnames

##### [List Custom Hostnames]
GET/zones/{zone_id}/custom_hostnames
##### [Custom Hostname Details]
GET/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
##### [Create Custom Hostname]
POST/zones/{zone_id}/custom_hostnames
##### [Edit Custom Hostname]
PATCH/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
##### [Delete Custom Hostname (and any issued SSL certificates)]
DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}
#### Custom HostnamesFallback Origin

##### [Get Fallback Origin for Custom Hostnames]
GET/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Update Fallback Origin for Custom Hostnames]
PUT/zones/{zone_id}/custom_hostnames/fallback_origin
##### [Delete Fallback Origin for Custom Hostnames]
DELETE/zones/{zone_id}/custom_hostnames/fallback_origin
#### Custom HostnamesCertificate Pack

#### Custom HostnamesCertificate PackCertificates

##### [Replace Custom Certificate and Custom Key In Custom Hostname]
PUT/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}
##### [Delete Single Certificate And Key For Custom Hostname]
DELETE/zones/{zone_id}/custom_hostnames/{custom_hostname_id}/certificate_pack/{certificate_pack_id}/certificates/{certificate_id}
#### Account Custom Nameservers

##### [List Account Custom Nameservers]
GET/accounts/{account_id}/custom_ns
##### [Add Account Custom Nameserver]
POST/accounts/{account_id}/custom_ns
##### [Delete Account Custom Nameserver]
DELETE/accounts/{account_id}/custom_ns/{custom_ns_id}
#### DNS Firewall

##### [List DNS Firewall Clusters]
GET/accounts/{account_id}/dns_firewall
##### [DNS Firewall Cluster Details]
GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}
##### [Create DNS Firewall Cluster]
POST/accounts/{account_id}/dns_firewall
##### [Update DNS Firewall Cluster]
PATCH/accounts/{account_id}/dns_firewall/{dns_firewall_id}
##### [Delete DNS Firewall Cluster]
DELETE/accounts/{account_id}/dns_firewall/{dns_firewall_id}
#### DNS FirewallAnalytics

#### DNS FirewallAnalyticsReports

##### [Table]
GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report
#### DNS FirewallAnalyticsReportsBytimes

##### [By Time]
GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report/bytime
#### DNS FirewallReverse DNS

##### [Show DNS Firewall Cluster Reverse DNS]
GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns
##### [Update DNS Firewall Cluster Reverse DNS]
PATCH/accounts/{account_id}/dns_firewall/{dns_firewall_id}/reverse_dns
#### DNS

#### DNSDNSSEC

##### [DNSSEC Details]
GET/zones/{zone_id}/dnssec
##### [Edit DNSSEC Status]
PATCH/zones/{zone_id}/dnssec
##### [Delete DNSSEC records]
DELETE/zones/{zone_id}/dnssec
#### DNSRecords

##### [List DNS Records]
GET/zones/{zone_id}/dns_records
##### [DNS Record Details]
GET/zones/{zone_id}/dns_records/{dns_record_id}
##### [Create DNS Record]
POST/zones/{zone_id}/dns_records
##### [Overwrite DNS Record]
PUT/zones/{zone_id}/dns_records/{dns_record_id}
##### [Update DNS Record]
PATCH/zones/{zone_id}/dns_records/{dns_record_id}
##### [Delete DNS Record]
DELETE/zones/{zone_id}/dns_records/{dns_record_id}
##### [Export DNS Records]
GET/zones/{zone_id}/dns_records/export
##### [Import DNS Records]
POST/zones/{zone_id}/dns_records/import
##### [Scan DNS Records]
DeprecatedPOST/zones/{zone_id}/dns_records/scan
##### [Trigger DNS Record Scan]
POST/zones/{zone_id}/dns_records/scan/trigger
##### [Review Scanned DNS Records]
POST/zones/{zone_id}/dns_records/scan/review
##### [List Scanned DNS Records]
GET/zones/{zone_id}/dns_records/scan/review
##### [Batch DNS Records]
POST/zones/{zone_id}/dns_records/batch
#### DNSUsage

#### DNSUsageZone

#### DNSUsageAccount

#### DNSSettings

#### DNSSettingsZone

##### [Show DNS Settings]
GET/zones/{zone_id}/dns_settings
##### [Update DNS Settings]
PATCH/zones/{zone_id}/dns_settings
#### DNSSettingsAccount

##### [Show DNS Settings]
GET/accounts/{account_id}/dns_settings
##### [Update DNS Settings]
PATCH/accounts/{account_id}/dns_settings
#### DNSSettingsAccountViews

##### [List Internal DNS Views]
GET/accounts/{account_id}/dns_settings/views
##### [DNS Internal View Details]
GET/accounts/{account_id}/dns_settings/views/{view_id}
##### [Create Internal DNS View]
POST/accounts/{account_id}/dns_settings/views
##### [Update Internal DNS View]
PATCH/accounts/{account_id}/dns_settings/views/{view_id}
##### [Delete Internal DNS View]
DELETE/accounts/{account_id}/dns_settings/views/{view_id}
#### DNSAnalytics

#### DNSAnalyticsReports

##### [Table]
GET/zones/{zone_id}/dns_analytics/report
#### DNSAnalyticsReportsBytimes

##### [By Time]
GET/zones/{zone_id}/dns_analytics/report/bytime
#### DNSZone Transfers

#### DNSZone TransfersForce AXFR

##### [Force AXFR]
POST/zones/{zone_id}/secondary_dns/force_axfr
#### DNSZone TransfersIncoming

##### [Secondary Zone Configuration Details]
GET/zones/{zone_id}/secondary_dns/incoming
##### [Create Secondary Zone Configuration]
POST/zones/{zone_id}/secondary_dns/incoming
##### [Update Secondary Zone Configuration]
PUT/zones/{zone_id}/secondary_dns/incoming
##### [Delete Secondary Zone Configuration]
DELETE/zones/{zone_id}/secondary_dns/incoming
#### DNSZone TransfersOutgoing

##### [Primary Zone Configuration Details]
GET/zones/{zone_id}/secondary_dns/outgoing
##### [Create Primary Zone Configuration]
POST/zones/{zone_id}/secondary_dns/outgoing
##### [Update Primary Zone Configuration]
PUT/zones/{zone_id}/secondary_dns/outgoing
##### [Delete Primary Zone Configuration]
DELETE/zones/{zone_id}/secondary_dns/outgoing
##### [Disable Outgoing Zone Transfers]
POST/zones/{zone_id}/secondary_dns/outgoing/disable
##### [Enable Outgoing Zone Transfers]
POST/zones/{zone_id}/secondary_dns/outgoing/enable
##### [Force DNS NOTIFY]
POST/zones/{zone_id}/secondary_dns/outgoing/force_notify
#### DNSZone TransfersOutgoingStatus

##### [Get Outgoing Zone Transfer Status]
GET/zones/{zone_id}/secondary_dns/outgoing/status
#### DNSZone TransfersACLs

##### [List ACLs]
GET/accounts/{account_id}/secondary_dns/acls
##### [ACL Details]
GET/accounts/{account_id}/secondary_dns/acls/{acl_id}
##### [Create ACL]
POST/accounts/{account_id}/secondary_dns/acls
##### [Update ACL]
PUT/accounts/{account_id}/secondary_dns/acls/{acl_id}
##### [Delete ACL]
DELETE/accounts/{account_id}/secondary_dns/acls/{acl_id}
#### DNSZone TransfersPeers

##### [List Peers]
GET/accounts/{account_id}/secondary_dns/peers
##### [Peer Details]
GET/accounts/{account_id}/secondary_dns/peers/{peer_id}
##### [Create Peer]
POST/accounts/{account_id}/secondary_dns/peers
##### [Update Peer]
PUT/accounts/{account_id}/secondary_dns/peers/{peer_id}
##### [Delete Peer]
DELETE/accounts/{account_id}/secondary_dns/peers/{peer_id}
#### DNSZone TransfersTSIGs

##### [List TSIGs]
GET/accounts/{account_id}/secondary_dns/tsigs
##### [TSIG Details]
GET/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}
##### [Create TSIG]
POST/accounts/{account_id}/secondary_dns/tsigs
##### [Update TSIG]
PUT/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}
##### [Delete TSIG]
DELETE/accounts/{account_id}/secondary_dns/tsigs/{tsig_id}
#### Email Security

#### Email SecurityInvestigate

##### [Search email messages]
GET/accounts/{account_id}/email-security/investigate
##### [Get message details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}
#### Email SecurityInvestigateDetections

##### [Get message detection details]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/detections
#### Email SecurityInvestigatePreview

##### [Get email preview]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/preview
##### [Preview for non-detection messages]
POST/accounts/{account_id}/email-security/investigate/preview
#### Email SecurityInvestigateRaw

##### [Get raw email content]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/raw
#### Email SecurityInvestigateTrace

##### [Get email trace]
GET/accounts/{account_id}/email-security/investigate/{postfix_id}/trace
#### Email SecurityInvestigateMove

##### [Move a message]
POST/accounts/{account_id}/email-security/investigate/{postfix_id}/move
##### [Move multiple messages]
POST/accounts/{account_id}/email-security/investigate/move
#### Email SecurityInvestigateReclassify

##### [Change email classification]
POST/accounts/{account_id}/email-security/investigate/{postfix_id}/reclassify
#### Email SecurityInvestigateRelease

##### [Release messages from quarantine]
POST/accounts/{account_id}/email-security/investigate/release
#### Email SecurityPhishguard

#### Email SecurityPhishguardReports

##### [Get `PhishGuard` reports]
GET/accounts/{account_id}/email-security/phishguard/reports
#### Email SecuritySettings

#### Email SecuritySettingsAllow Policies

##### [List email allow policies]
GET/accounts/{account_id}/email-security/settings/allow_policies
##### [Get an email allow policy]
GET/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
##### [Create an email allow policy]
POST/accounts/{account_id}/email-security/settings/allow_policies
##### [Update an email allow policy]
PATCH/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
##### [Delete an email allow policy]
DELETE/accounts/{account_id}/email-security/settings/allow_policies/{policy_id}
#### Email SecuritySettingsBlock Senders

##### [List blocked email senders]
GET/accounts/{account_id}/email-security/settings/block_senders
##### [Get a blocked email sender]
GET/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
##### [Create a blocked email sender]
POST/accounts/{account_id}/email-security/settings/block_senders
##### [Update a blocked email sender]
PATCH/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
##### [Delete a blocked email sender]
DELETE/accounts/{account_id}/email-security/settings/block_senders/{pattern_id}
#### Email SecuritySettingsDomains

##### [List protected email domains]
GET/accounts/{account_id}/email-security/settings/domains
##### [Get an email domain]
GET/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Update an email domain]
PATCH/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Unprotect an email domain]
DELETE/accounts/{account_id}/email-security/settings/domains/{domain_id}
##### [Unprotect multiple email domains]
DELETE/accounts/{account_id}/email-security/settings/domains
#### Email SecuritySettingsImpersonation Registry

##### [List entries in impersonation registry]
GET/accounts/{account_id}/email-security/settings/impersonation_registry
##### [Get an entry in impersonation registry]
GET/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
##### [Create an entry in impersonation registry]
POST/accounts/{account_id}/email-security/settings/impersonation_registry
##### [Update an entry in impersonation registry]
PATCH/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
##### [Delete an entry from impersonation registry]
DELETE/accounts/{account_id}/email-security/settings/impersonation_registry/{display_name_id}
#### Email SecuritySettingsTrusted Domains

##### [List trusted email domains]
GET/accounts/{account_id}/email-security/settings/trusted_domains
##### [Get a trusted email domain]
GET/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
##### [Create a trusted email domain]
POST/accounts/{account_id}/email-security/settings/trusted_domains
##### [Update a trusted email domain]
PATCH/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
##### [Delete a trusted email domain]
DELETE/accounts/{account_id}/email-security/settings/trusted_domains/{trusted_domain_id}
#### Email SecuritySubmissions

##### [Get reclassify submissions]
GET/accounts/{account_id}/email-security/submissions
#### Email Routing

##### [Get Email Routing settings]
GET/zones/{zone_id}/email/routing
##### [Disable Email Routing]
DeprecatedPOST/zones/{zone_id}/email/routing/disable
##### [Enable Email Routing]
DeprecatedPOST/zones/{zone_id}/email/routing/enable
#### Email RoutingDNS

##### [Email Routing - DNS settings]
GET/zones/{zone_id}/email/routing/dns
##### [Enable Email Routing]
POST/zones/{zone_id}/email/routing/dns
##### [Unlock Email Routing]
PATCH/zones/{zone_id}/email/routing/dns
##### [Disable Email Routing]
DELETE/zones/{zone_id}/email/routing/dns
#### Email RoutingRules

##### [List routing rules]
GET/zones/{zone_id}/email/routing/rules
##### [Get routing rule]
GET/zones/{zone_id}/email/routing/rules/{rule_identifier}
##### [Create routing rule]
POST/zones/{zone_id}/email/routing/rules
##### [Update routing rule]
PUT/zones/{zone_id}/email/routing/rules/{rule_identifier}
##### [Delete routing rule]
DELETE/zones/{zone_id}/email/routing/rules/{rule_identifier}
#### Email RoutingRulesCatch Alls

##### [Get catch-all rule]
GET/zones/{zone_id}/email/routing/rules/catch_all
##### [Update catch-all rule]
PUT/zones/{zone_id}/email/routing/rules/catch_all
#### Email RoutingAddresses

##### [List destination addresses]
GET/accounts/{account_id}/email/routing/addresses
##### [Get a destination address]
GET/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}
##### [Create a destination address]
POST/accounts/{account_id}/email/routing/addresses
##### [Delete destination address]
DELETE/accounts/{account_id}/email/routing/addresses/{destination_address_identifier}
#### Email Sending

##### [Send an email using the builder.]
POST/accounts/{account_id}/email/sending/send
##### [Send a raw MIME email message.]
POST/accounts/{account_id}/email/sending/send_raw
#### Email SendingSubdomains

##### [List sending subdomains]
GET/zones/{zone_id}/email/sending/subdomains
##### [Get a sending subdomain]
GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}
##### [Create a sending subdomain]
POST/zones/{zone_id}/email/sending/subdomains
##### [Delete a sending subdomain]
DELETE/zones/{zone_id}/email/sending/subdomains/{subdomain_id}
#### Email SendingSubdomainsDNS

##### [Get sending subdomain DNS records]
GET/zones/{zone_id}/email/sending/subdomains/{subdomain_id}/dns
#### Filters

##### [List filters]
DeprecatedGET/zones/{zone_id}/filters
##### [Get a filter]
DeprecatedGET/zones/{zone_id}/filters/{filter_id}
##### [Create filters]
DeprecatedPOST/zones/{zone_id}/filters
##### [Update a filter]
DeprecatedPUT/zones/{zone_id}/filters/{filter_id}
##### [Delete a filter]
DeprecatedDELETE/zones/{zone_id}/filters/{filter_id}
##### [Update filters]
DeprecatedPUT/zones/{zone_id}/filters
##### [Delete filters]
DeprecatedDELETE/zones/{zone_id}/filters
#### Firewall

#### FirewallLockdowns

##### [List Zone Lockdown rules]
GET/zones/{zone_id}/firewall/lockdowns
##### [Get a Zone Lockdown rule]
GET/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}
##### [Create a Zone Lockdown rule]
POST/zones/{zone_id}/firewall/lockdowns
##### [Update a Zone Lockdown rule]
PUT/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}
##### [Delete a Zone Lockdown rule]
DELETE/zones/{zone_id}/firewall/lockdowns/{lock_downs_id}
#### FirewallRules

##### [List firewall rules]
DeprecatedGET/zones/{zone_id}/firewall/rules
##### [Get a firewall rule]
DeprecatedGET/zones/{zone_id}/firewall/rules/{rule_id}
##### [Create firewall rules]
DeprecatedPOST/zones/{zone_id}/firewall/rules
##### [Update a firewall rule]
DeprecatedPUT/zones/{zone_id}/firewall/rules/{rule_id}
##### [Update priority of a firewall rule]
DeprecatedPATCH/zones/{zone_id}/firewall/rules/{rule_id}
##### [Delete a firewall rule]
DeprecatedDELETE/zones/{zone_id}/firewall/rules/{rule_id}
##### [Update firewall rules]
DeprecatedPUT/zones/{zone_id}/firewall/rules
##### [Update priority of firewall rules]
DeprecatedPATCH/zones/{zone_id}/firewall/rules
##### [Delete firewall rules]
DeprecatedDELETE/zones/{zone_id}/firewall/rules
#### FirewallAccess Rules

##### [List IP Access rules]
GET/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules
##### [Get an IP Access rule]
GET/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}
##### [Create an IP Access rule]
POST/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules
##### [Update an IP Access rule]
PATCH/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}
##### [Delete an IP Access rule]
DELETE/{accounts_or_zones}/{account_or_zone_id}/firewall/access_rules/rules/{rule_id}
#### FirewallUA Rules

##### [List User Agent Blocking rules]
GET/zones/{zone_id}/firewall/ua_rules
##### [Get a User Agent Blocking rule]
GET/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}
##### [Create a User Agent Blocking rule]
POST/zones/{zone_id}/firewall/ua_rules
##### [Update a User Agent Blocking rule]
PUT/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}
##### [Delete a User Agent Blocking rule]
DELETE/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}
#### FirewallWAF

#### FirewallWAFOverrides

##### [List WAF overrides]
DeprecatedGET/zones/{zone_id}/firewall/waf/overrides
##### [Get a WAF override]
DeprecatedGET/zones/{zone_id}/firewall/waf/overrides/{overrides_id}
##### [Create a WAF override]
DeprecatedPOST/zones/{zone_id}/firewall/waf/overrides
##### [Update WAF override]
DeprecatedPUT/zones/{zone_id}/firewall/waf/overrides/{overrides_id}
##### [Delete a WAF override]
DeprecatedDELETE/zones/{zone_id}/firewall/waf/overrides/{overrides_id}
#### FirewallWAFPackages

##### [List WAF packages]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages
##### [Get a WAF package]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages/{package_id}
#### FirewallWAFPackagesGroups

##### [List WAF rule groups]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages/{package_id}/groups
##### [Get a WAF rule group]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}
##### [Update a WAF rule group]
DeprecatedPATCH/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}
#### FirewallWAFPackagesRules

##### [List WAF rules]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages/{package_id}/rules
##### [Get a WAF rule]
DeprecatedGET/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}
##### [Update a WAF rule]
DeprecatedPATCH/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}
#### Healthchecks

##### [List Health Checks]
GET/zones/{zone_id}/healthchecks
##### [Health Check Details]
GET/zones/{zone_id}/healthchecks/{healthcheck_id}
##### [Create Health Check]
POST/zones/{zone_id}/healthchecks
##### [Update Health Check]
PUT/zones/{zone_id}/healthchecks/{healthcheck_id}
##### [Patch Health Check]
PATCH/zones/{zone_id}/healthchecks/{healthcheck_id}
##### [Delete Health Check]
DELETE/zones/{zone_id}/healthchecks/{healthcheck_id}
#### HealthchecksPreviews

##### [Health Check Preview Details]
GET/zones/{zone_id}/healthchecks/preview/{healthcheck_id}
##### [Create Preview Health Check]
POST/zones/{zone_id}/healthchecks/preview
##### [Delete Preview Health Check]
DELETE/zones/{zone_id}/healthchecks/preview/{healthcheck_id}
#### Keyless Certificates

##### [List Keyless SSL Configurations]
GET/zones/{zone_id}/keyless_certificates
##### [Get Keyless SSL Configuration]
GET/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
##### [Create Keyless SSL Configuration]
POST/zones/{zone_id}/keyless_certificates
##### [Edit Keyless SSL Configuration]
PATCH/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
##### [Delete Keyless SSL Configuration]
DELETE/zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
#### Logpush

#### LogpushDatasets

#### LogpushDatasetsFields

##### [List fields]
GET/{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/fields
#### LogpushDatasetsJobs

##### [List Logpush jobs for a dataset]
GET/{accounts_or_zones}/{account_or_zone_id}/logpush/datasets/{dataset_id}/jobs
#### LogpushEdge

##### [List Instant Logs jobs]
GET/zones/{zone_id}/logpush/edge/jobs
##### [Create Instant Logs job]
POST/zones/{zone_id}/logpush/edge/jobs
#### LogpushJobs

##### [List Logpush jobs]
GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs
##### [Get Logpush job details]
GET/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}
##### [Create Logpush job]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs
##### [Update Logpush job]
PUT/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}
##### [Delete Logpush job]
DELETE/{accounts_or_zones}/{account_or_zone_id}/logpush/jobs/{job_id}
#### LogpushOwnership

##### [Get ownership challenge]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/ownership
##### [Validate ownership challenge]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/ownership/validate
#### LogpushValidate

##### [Validate destination]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination
##### [Check destination exists]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/destination/exists
##### [Validate origin]
POST/{accounts_or_zones}/{account_or_zone_id}/logpush/validate/origin
#### Logs

#### LogsControl

#### LogsControlRetention

##### [Get log retention flag]
GET/zones/{zone_id}/logs/control/retention/flag
##### [Update log retention flag]
POST/zones/{zone_id}/logs/control/retention/flag
#### LogsControlCmb

#### LogsControlCmbConfig

##### [Get CMB config]
GET/accounts/{account_id}/logs/control/cmb/config
##### [Update CMB config]
POST/accounts/{account_id}/logs/control/cmb/config
##### [Delete CMB config]
DELETE/accounts/{account_id}/logs/control/cmb/config
#### LogsRayID

##### [Get logs RayIDs]
GET/zones/{zone_id}/logs/rayids/{ray_id}
#### LogsReceived

##### [Get logs received]
GET/zones/{zone_id}/logs/received
#### LogsReceivedFields

##### [List fields]
GET/zones/{zone_id}/logs/received/fields
#### Origin TLS Client Auth

##### [List Certificates]
DeprecatedGET/zones/{zone_id}/origin_tls_client_auth
##### [Get Certificate Details]
DeprecatedGET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### [Upload Certificate]
DeprecatedPOST/zones/{zone_id}/origin_tls_client_auth
##### [Delete Certificate]
DeprecatedDELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
#### Origin TLS Client AuthZone Certificates

##### [List Certificates]
GET/zones/{zone_id}/origin_tls_client_auth
##### [Get Certificate Details]
GET/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
##### [Upload Certificate]
POST/zones/{zone_id}/origin_tls_client_auth
##### [Delete Certificate]
DELETE/zones/{zone_id}/origin_tls_client_auth/{certificate_id}
#### Origin TLS Client AuthHostnames

##### [Get the Hostname Status for Client Authentication]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}
##### [Enable or Disable a Hostname for Client Authentication]
PUT/zones/{zone_id}/origin_tls_client_auth/hostnames
#### Origin TLS Client AuthHostname Certificates

##### [List Certificates]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
##### [Get the Hostname Client Certificate]
GET/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
##### [Upload a Hostname Client Certificate]
POST/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
##### [Delete Hostname Client Certificate]
DELETE/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
#### Origin TLS Client AuthSettings

##### [Get Enablement Setting for Zone]
GET/zones/{zone_id}/origin_tls_client_auth/settings
##### [Set Enablement for Zone]
PUT/zones/{zone_id}/origin_tls_client_auth/settings
#### Page Rules

##### [List Page Rules]
GET/zones/{zone_id}/pagerules
##### [Get a Page Rule]
GET/zones/{zone_id}/pagerules/{pagerule_id}
##### [Create a Page Rule]
POST/zones/{zone_id}/pagerules
##### [Update a Page Rule]
PUT/zones/{zone_id}/pagerules/{pagerule_id}
##### [Edit a Page Rule]
PATCH/zones/{zone_id}/pagerules/{pagerule_id}
##### [Delete a Page Rule]
DELETE/zones/{zone_id}/pagerules/{pagerule_id}
#### Rate Limits

##### [List rate limits]
DeprecatedGET/zones/{zone_id}/rate_limits
##### [Get a rate limit]
DeprecatedGET/zones/{zone_id}/rate_limits/{rate_limit_id}
##### [Create a rate limit]
DeprecatedPOST/zones/{zone_id}/rate_limits
##### [Update a rate limit]
DeprecatedPUT/zones/{zone_id}/rate_limits/{rate_limit_id}
##### [Delete a rate limit]
DeprecatedDELETE/zones/{zone_id}/rate_limits/{rate_limit_id}
#### Smart Shield

##### [Get Smart Shield Settings]
GET/zones/{zone_id}/smart_shield
##### [Patch Smart Shield Settings]
PATCH/zones/{zone_id}/smart_shield
#### Smart ShieldHealth Checks

##### [List Health Checks]
GET/zones/{zone_id}/smart_shield/healthchecks
##### [Health Check Details]
GET/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}
##### [Create Health Check]
POST/zones/{zone_id}/smart_shield/healthchecks
##### [Update Health Check]
PUT/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}
##### [Patch Health Check]
PATCH/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}
##### [Delete Health Check]
DELETE/zones/{zone_id}/smart_shield/healthchecks/{healthcheck_id}
#### Smart ShieldCache Reserve Clear

##### [Get Cache Reserve Clear]
GET/zones/{zone_id}/smart_shield/cache_reserve_clear
##### [Start Cache Reserve Clear]
POST/zones/{zone_id}/smart_shield/cache_reserve_clear
#### Waiting Rooms

##### [List waiting rooms for account or zone]
GET/{accounts_or_zones}/{account_or_zone_id}/waiting_rooms
##### [Waiting room details]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}
##### [Create waiting room]
POST/zones/{zone_id}/waiting_rooms
##### [Update waiting room]
PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}
##### [Patch waiting room]
PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}
##### [Delete waiting room]
DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}
#### Waiting RoomsPage

##### [Create a custom waiting room page preview]
POST/zones/{zone_id}/waiting_rooms/preview
#### Waiting RoomsEvents

##### [List events]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events
##### [Event details]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}
##### [Create event]
POST/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events
##### [Update event]
PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}
##### [Patch event]
PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}
##### [Delete event]
DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}
#### Waiting RoomsEventsDetails

##### [Preview active event details]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}/details
#### Waiting RoomsRules

##### [List Waiting Room Rules]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules
##### [Create Waiting Room Rule]
POST/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules
##### [Replace Waiting Room Rules]
PUT/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules
##### [Patch Waiting Room Rule]
PATCH/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}
##### [Delete Waiting Room Rule]
DELETE/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}
#### Waiting RoomsStatuses

##### [Get waiting room status]
GET/zones/{zone_id}/waiting_rooms/{waiting_room_id}/status
#### Waiting RoomsSettings

##### [Get zone-level Waiting Room settings]
GET/zones/{zone_id}/waiting_rooms/settings
##### [Update zone-level Waiting Room settings]
PUT/zones/{zone_id}/waiting_rooms/settings
##### [Patch zone-level Waiting Room settings]
PATCH/zones/{zone_id}/waiting_rooms/settings
#### Web3

#### Web3Hostnames

##### [List Web3 Hostnames]
GET/zones/{zone_id}/web3/hostnames
##### [Web3 Hostname Details]
GET/zones/{zone_id}/web3/hostnames/{identifier}
##### [Create Web3 Hostname]
POST/zones/{zone_id}/web3/hostnames
##### [Edit Web3 Hostname]
PATCH/zones/{zone_id}/web3/hostnames/{identifier}
##### [Delete Web3 Hostname]
DELETE/zones/{zone_id}/web3/hostnames/{identifier}
#### Web3HostnamesIPFS Universal Paths

#### Web3HostnamesIPFS Universal PathsContent Lists

##### [IPFS Universal Path Gateway Content List Details]
GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list
##### [Update IPFS Universal Path Gateway Content List]
PUT/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list
#### Web3HostnamesIPFS Universal PathsContent ListsEntries

##### [List IPFS Universal Path Gateway Content List Entries]
GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries
##### [IPFS Universal Path Gateway Content List Entry Details]
GET/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}
##### [Create IPFS Universal Path Gateway Content List Entry]
POST/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries
##### [Edit IPFS Universal Path Gateway Content List Entry]
PUT/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}
##### [Delete IPFS Universal Path Gateway Content List Entry]
DELETE/zones/{zone_id}/web3/hostnames/{identifier}/ipfs_universal_path/content_list/entries/{content_list_entry_identifier}
#### Workers

#### WorkersBeta

#### WorkersBetaWorkers

##### [List Workers]
GET/accounts/{account_id}/workers/workers
##### [Get Worker]
GET/accounts/{account_id}/workers/workers/{worker_id}
##### [Create Worker]
POST/accounts/{account_id}/workers/workers
##### [Update Worker]
PUT/accounts/{account_id}/workers/workers/{worker_id}
##### [Edit Worker]
PATCH/accounts/{account_id}/workers/workers/{worker_id}
##### [Delete Worker]
DELETE/accounts/{account_id}/workers/workers/{worker_id}
#### WorkersBetaWorkersVersions

##### [List Versions]
GET/accounts/{account_id}/workers/workers/{worker_id}/versions
##### [Get Version]
GET/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}
##### [Create Version]
POST/accounts/{account_id}/workers/workers/{worker_id}/versions
##### [Delete Version]
DELETE/accounts/{account_id}/workers/workers/{worker_id}/versions/{version_id}
#### WorkersRoutes

##### [List Routes]
GET/zones/{zone_id}/workers/routes
##### [Get Route]
GET/zones/{zone_id}/workers/routes/{route_id}
##### [Create Route]
POST/zones/{zone_id}/workers/routes
##### [Update Route]
PUT/zones/{zone_id}/workers/routes/{route_id}
##### [Delete Route]
DELETE/zones/{zone_id}/workers/routes/{route_id}
#### WorkersAssets

#### WorkersAssetsUpload

##### [Upload Assets]
POST/accounts/{account_id}/workers/assets/upload
#### WorkersScripts

##### [List Workers]
GET/accounts/{account_id}/workers/scripts
##### [Search Workers]
GET/accounts/{account_id}/workers/scripts-search
##### [Download Worker]
GET/accounts/{account_id}/workers/scripts/{script_name}
##### [Upload Worker Module]
PUT/accounts/{account_id}/workers/scripts/{script_name}
##### [Delete Worker]
DELETE/accounts/{account_id}/workers/scripts/{script_name}
#### WorkersScriptsAssets

#### WorkersScriptsAssetsUpload

##### [Create Assets Upload Session]
POST/accounts/{account_id}/workers/scripts/{script_name}/assets-upload-session
#### WorkersScriptsSubdomain

##### [Get Worker subdomain]
GET/accounts/{account_id}/workers/scripts/{script_name}/subdomain
##### [Post Worker subdomain]
POST/accounts/{account_id}/workers/scripts/{script_name}/subdomain
##### [Delete Worker subdomain]
DELETE/accounts/{account_id}/workers/scripts/{script_name}/subdomain
#### WorkersScriptsSchedules

##### [Get Cron Triggers]
GET/accounts/{account_id}/workers/scripts/{script_name}/schedules
##### [Update Cron Triggers]
PUT/accounts/{account_id}/workers/scripts/{script_name}/schedules
#### WorkersScriptsTail

##### [List Tails]
GET/accounts/{account_id}/workers/scripts/{script_name}/tails
##### [Start Tail]
POST/accounts/{account_id}/workers/scripts/{script_name}/tails
##### [Delete Tail]
DELETE/accounts/{account_id}/workers/scripts/{script_name}/tails/{id}
#### WorkersScriptsContent

##### [Get script content]
GET/accounts/{account_id}/workers/scripts/{script_name}/content/v2
##### [Put script content]
PUT/accounts/{account_id}/workers/scripts/{script_name}/content
#### WorkersScriptsSettings

##### [Get Script Settings]
GET/accounts/{account_id}/workers/scripts/{script_name}/script-settings
##### [Patch Script Settings]
PATCH/accounts/{account_id}/workers/scripts/{script_name}/script-settings
#### WorkersScriptsDeployments

##### [List Deployments]
GET/accounts/{account_id}/workers/scripts/{script_name}/deployments
##### [Create Deployment]
POST/accounts/{account_id}/workers/scripts/{script_name}/deployments
##### [Get Deployment]
GET/accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}
##### [Delete Deployment]
DELETE/accounts/{account_id}/workers/scripts/{script_name}/deployments/{deployment_id}
#### WorkersScriptsVersions

##### [List Versions]
GET/accounts/{account_id}/workers/scripts/{script_name}/versions
##### [Get Version Detail]
GET/accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}
##### [Upload Version]
POST/accounts/{account_id}/workers/scripts/{script_name}/versions
#### WorkersScriptsSecrets

##### [List script secrets]
GET/accounts/{account_id}/workers/scripts/{script_name}/secrets
##### [Get secret binding]
GET/accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}
##### [Add script secret]
PUT/accounts/{account_id}/workers/scripts/{script_name}/secrets
##### [Delete script secret]
DELETE/accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}
#### WorkersScriptsScript And Version Settings

##### [Get Settings]
GET/accounts/{account_id}/workers/scripts/{script_name}/settings
##### [Patch Settings]
PATCH/accounts/{account_id}/workers/scripts/{script_name}/settings
#### WorkersAccount Settings

##### [Fetch Worker Account Settings]
GET/accounts/{account_id}/workers/account-settings
##### [Create Worker Account Settings]
PUT/accounts/{account_id}/workers/account-settings
#### WorkersDomains

##### [List Domains]
GET/accounts/{account_id}/workers/domains
##### [Get Domain]
GET/accounts/{account_id}/workers/domains/{domain_id}
##### [Attach Domain]
PUT/accounts/{account_id}/workers/domains
##### [Detach Domain]
DELETE/accounts/{account_id}/workers/domains/{domain_id}
#### WorkersSubdomains

##### [Get Subdomain]
GET/accounts/{account_id}/workers/subdomain
##### [Create Subdomain]
PUT/accounts/{account_id}/workers/subdomain
##### [Delete Subdomain]
DELETE/accounts/{account_id}/workers/subdomain
#### WorkersObservability

#### WorkersObservabilityTelemetry

##### [List keys]
POST/accounts/{account_id}/workers/observability/telemetry/keys
##### [Run a query]
POST/accounts/{account_id}/workers/observability/telemetry/query
##### [List values]
POST/accounts/{account_id}/workers/observability/telemetry/values
#### WorkersObservabilityDestinations

##### [Get Destinations]
GET/accounts/{account_id}/workers/observability/destinations
##### [Create Destination]
POST/accounts/{account_id}/workers/observability/destinations
##### [Update Destination]
PATCH/accounts/{account_id}/workers/observability/destinations/{slug}
##### [Delete Destination]
DELETE/accounts/{account_id}/workers/observability/destinations/{slug}
#### KV

#### KVNamespaces

##### [List Namespaces]
GET/accounts/{account_id}/storage/kv/namespaces
##### [Get a Namespace]
GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}
##### [Create a Namespace]
POST/accounts/{account_id}/storage/kv/namespaces
##### [Rename a Namespace]
PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}
##### [Remove a Namespace]
DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}
##### [Write multiple key-value pairs]
PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk
##### [Delete multiple key-value pairs]
POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete
##### [Get multiple key-value pairs]
POST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get
#### KVNamespacesKeys

##### [List a Namespace's Keys]
GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys
##### [Write multiple key-value pairs]
DeprecatedPUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk
##### [Delete multiple key-value pairs]
DeprecatedPOST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/delete
##### [Get multiple key-value pairs]
DeprecatedPOST/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/bulk/get
#### KVNamespacesMetadata

##### [Read the metadata for a key]
GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}
#### KVNamespacesValues

##### [Read key-value pair]
GET/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}
##### [Write key-value pair with optional metadata]
PUT/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}
##### [Delete key-value pair]
DELETE/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}
#### Durable Objects

#### Durable ObjectsNamespaces

##### [List Namespaces]
GET/accounts/{account_id}/workers/durable_objects/namespaces
#### Durable ObjectsNamespacesObjects

##### [List Objects]
GET/accounts/{account_id}/workers/durable_objects/namespaces/{id}/objects
#### Queues

##### [List Queues]
GET/accounts/{account_id}/queues
##### [Get Queue]
GET/accounts/{account_id}/queues/{queue_id}
##### [Create Queue]
POST/accounts/{account_id}/queues
##### [Update Queue]
PUT/accounts/{account_id}/queues/{queue_id}
##### [Update Queue]
PATCH/accounts/{account_id}/queues/{queue_id}
##### [Delete Queue]
DELETE/accounts/{account_id}/queues/{queue_id}
#### QueuesMessages

##### [Push Message]
POST/accounts/{account_id}/queues/{queue_id}/messages
##### [Acknowledge + Retry Queue Messages]
POST/accounts/{account_id}/queues/{queue_id}/messages/ack
##### [Pull Queue Messages]
POST/accounts/{account_id}/queues/{queue_id}/messages/pull
##### [Push Message Batch]
POST/accounts/{account_id}/queues/{queue_id}/messages/batch
#### QueuesPurge

##### [Get Queue Purge Status]
GET/accounts/{account_id}/queues/{queue_id}/purge
##### [Purge Queue]
POST/accounts/{account_id}/queues/{queue_id}/purge
#### QueuesConsumers

##### [List Queue Consumers]
GET/accounts/{account_id}/queues/{queue_id}/consumers
##### [Get Queue Consumer]
GET/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}
##### [Create a Queue Consumer]
POST/accounts/{account_id}/queues/{queue_id}/consumers
##### [Update Queue Consumer]
PUT/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}
##### [Delete Queue Consumer]
DELETE/accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}
#### QueuesSubscriptions

##### [List Event Subscriptions]
GET/accounts/{account_id}/event_subscriptions/subscriptions
##### [Get Event Subscription]
GET/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}
##### [Create Event Subscription]
POST/accounts/{account_id}/event_subscriptions/subscriptions
##### [Update Event Subscription]
PATCH/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}
##### [Delete Event Subscription]
DELETE/accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}
#### API Gateway

#### API GatewayConfigurations

##### [Retrieve information about specific configuration properties]
GET/zones/{zone_id}/api_gateway/configuration
##### [Update configuration properties]
PUT/zones/{zone_id}/api_gateway/configuration
#### API GatewayDiscovery

##### [Retrieve discovered operations on a zone rendered as OpenAPI schemas]
GET/zones/{zone_id}/api_gateway/discovery
#### API GatewayDiscoveryOperations

##### [Retrieve discovered operations on a zone]
GET/zones/{zone_id}/api_gateway/discovery/operations
##### [Patch discovered operation]
PATCH/zones/{zone_id}/api_gateway/discovery/operations/{operation_id}
##### [Patch discovered operations]
PATCH/zones/{zone_id}/api_gateway/discovery/operations
#### API GatewayLabels

##### [Retrieve all labels]
GET/zones/{zone_id}/api_gateway/labels
#### API GatewayLabelsUser

##### [Create user labels]
POST/zones/{zone_id}/api_gateway/labels/user
##### [Delete user labels]
DELETE/zones/{zone_id}/api_gateway/labels/user
##### [Retrieve user label]
GET/zones/{zone_id}/api_gateway/labels/user/{name}
##### [Update user label]
PUT/zones/{zone_id}/api_gateway/labels/user/{name}
##### [Patch user label]
PATCH/zones/{zone_id}/api_gateway/labels/user/{name}
##### [Delete user label]
DELETE/zones/{zone_id}/api_gateway/labels/user/{name}
#### API GatewayLabelsUserResources

#### API GatewayLabelsUserResourcesOperation

##### [Replace operation(s) attached to a user label]
PUT/zones/{zone_id}/api_gateway/labels/user/{name}/resources/operation
#### API GatewayLabelsManaged

##### [Retrieve managed label]
GET/zones/{zone_id}/api_gateway/labels/managed/{name}
#### API GatewayLabelsManagedResources

#### API GatewayLabelsManagedResourcesOperation

##### [Replace operation(s) attached to a managed label]
PUT/zones/{zone_id}/api_gateway/labels/managed/{name}/resources/operation
#### API GatewayOperations

##### [Retrieve information about all operations on a zone]
GET/zones/{zone_id}/api_gateway/operations
##### [Retrieve information about an operation]
GET/zones/{zone_id}/api_gateway/operations/{operation_id}
##### [Add one operation to a zone]
POST/zones/{zone_id}/api_gateway/operations/item
##### [Delete an operation]
DELETE/zones/{zone_id}/api_gateway/operations/{operation_id}
##### [Add operations to a zone]
POST/zones/{zone_id}/api_gateway/operations
##### [Delete multiple operations]
DELETE/zones/{zone_id}/api_gateway/operations
#### API GatewayOperationsLabels

##### [Replace label(s) on an operation in endpoint management]
PUT/zones/{zone_id}/api_gateway/operations/{operation_id}/labels
##### [Attach label(s) on an operation in endpoint management]
POST/zones/{zone_id}/api_gateway/operations/{operation_id}/labels
##### [Remove label(s) on an operation in endpoint management]
DELETE/zones/{zone_id}/api_gateway/operations/{operation_id}/labels
##### [Bulk replace label(s) on operation(s) in endpoint management]
PUT/zones/{zone_id}/api_gateway/operations/labels
##### [Bulk attach label(s) on operation(s) in endpoint management]
POST/zones/{zone_id}/api_gateway/operations/labels
##### [Bulk remove label(s) on operation(s) in endpoint management]
DELETE/zones/{zone_id}/api_gateway/operations/labels
#### API GatewayOperationsSchema Validation

##### [Retrieve operation-level schema validation settings]
DeprecatedGET/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation
##### [Update operation-level schema validation settings]
DeprecatedPUT/zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation
##### [Update multiple operation-level schema validation settings]
DeprecatedPATCH/zones/{zone_id}/api_gateway/operations/schema_validation
#### API GatewaySchemas

##### [Retrieve operations and features as OpenAPI schemas]
GET/zones/{zone_id}/api_gateway/schemas
#### API GatewaySettings

#### API GatewaySettingsSchema Validation

##### [Retrieve zone level schema validation settings]
DeprecatedGET/zones/{zone_id}/api_gateway/settings/schema_validation
##### [Update zone level schema validation settings]
DeprecatedPUT/zones/{zone_id}/api_gateway/settings/schema_validation
##### [Update zone level schema validation settings]
DeprecatedPATCH/zones/{zone_id}/api_gateway/settings/schema_validation
#### API GatewayUser Schemas

##### [Retrieve information about all schemas on a zone]
DeprecatedGET/zones/{zone_id}/api_gateway/user_schemas
##### [Retrieve information about a specific schema on a zone]
DeprecatedGET/zones/{zone_id}/api_gateway/user_schemas/{schema_id}
##### [Upload a schema to a zone]
DeprecatedPOST/zones/{zone_id}/api_gateway/user_schemas
##### [Enable validation for a schema]
DeprecatedPATCH/zones/{zone_id}/api_gateway/user_schemas/{schema_id}
##### [Delete a schema]
DeprecatedDELETE/zones/{zone_id}/api_gateway/user_schemas/{schema_id}
#### API GatewayUser SchemasOperations

##### [Retrieve all operations from a schema.]
DeprecatedGET/zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations
#### API GatewayUser SchemasHosts

##### [Retrieve schema hosts in a zone]
DeprecatedGET/zones/{zone_id}/api_gateway/user_schemas/hosts
#### API GatewayExpression Template

#### API GatewayExpression TemplateFallthrough

##### [Generate fallthrough WAF expression template from a set of API hosts]
POST/zones/{zone_id}/api_gateway/expression-template/fallthrough
#### Managed Transforms

##### [List Managed Transforms]
GET/zones/{zone_id}/managed_headers
##### [Update Managed Transforms]
PATCH/zones/{zone_id}/managed_headers
##### [Delete Managed Transforms]
DELETE/zones/{zone_id}/managed_headers
#### Page Shield

##### [Get Page Shield settings]
GET/zones/{zone_id}/page_shield
##### [Update Page Shield settings]
PUT/zones/{zone_id}/page_shield
#### Page ShieldPolicies

##### [List Page Shield policies]
GET/zones/{zone_id}/page_shield/policies
##### [Get a Page Shield policy]
GET/zones/{zone_id}/page_shield/policies/{policy_id}
##### [Create a Page Shield policy]
POST/zones/{zone_id}/page_shield/policies
##### [Update a Page Shield policy]
PUT/zones/{zone_id}/page_shield/policies/{policy_id}
##### [Delete a Page Shield policy]
DELETE/zones/{zone_id}/page_shield/policies/{policy_id}
#### Page ShieldConnections

##### [List Page Shield connections]
GET/zones/{zone_id}/page_shield/connections
##### [Get a Page Shield connection]
GET/zones/{zone_id}/page_shield/connections/{connection_id}
#### Page ShieldScripts

##### [List Page Shield scripts]
GET/zones/{zone_id}/page_shield/scripts
##### [Get a Page Shield script]
GET/zones/{zone_id}/page_shield/scripts/{script_id}
#### Page ShieldCookies

##### [List Page Shield Cookies]
GET/zones/{zone_id}/page_shield/cookies
##### [Get a Page Shield cookie]
GET/zones/{zone_id}/page_shield/cookies/{cookie_id}
#### Rulesets

##### [List account or zone rulesets]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets
##### [Get an account or zone ruleset]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}
##### [Create an account or zone ruleset]
POST/{accounts_or_zones}/{account_or_zone_id}/rulesets
##### [Update an account or zone ruleset]
PUT/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}
##### [Delete an account or zone ruleset]
DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}
#### RulesetsPhases

##### [Get an account or zone entry point ruleset]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint
##### [Update an account or zone entry point ruleset]
PUT/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint
#### RulesetsPhasesVersions

##### [List an account or zone entry point ruleset's versions]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions
##### [Get an account or zone entry point ruleset version]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}
#### RulesetsRules

##### [Create an account or zone ruleset rule]
POST/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules
##### [Update an account or zone ruleset rule]
PATCH/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}
##### [Delete an account or zone ruleset rule]
DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}
#### RulesetsVersions

##### [List an account or zone ruleset's versions]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions
##### [Get an account or zone ruleset version]
GET/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}
##### [Delete an account or zone ruleset version]
DELETE/{accounts_or_zones}/{account_or_zone_id}/rulesets/{ruleset_id}/versions/{ruleset_version}
#### URL Normalization

##### [Get URL Normalization settings]
GET/zones/{zone_id}/url_normalization
##### [Update URL Normalization settings]
PUT/zones/{zone_id}/url_normalization
##### [Delete URL Normalization settings]
DELETE/zones/{zone_id}/url_normalization
#### Spectrum

#### SpectrumAnalytics

#### SpectrumAnalyticsAggregates

#### SpectrumAnalyticsAggregatesCurrents

##### [Get current aggregated analytics]
GET/zones/{zone_id}/spectrum/analytics/aggregate/current
#### SpectrumAnalyticsEvents

#### SpectrumAnalyticsEventsBytimes

##### [Get analytics by time]
GET/zones/{zone_id}/spectrum/analytics/events/bytime
#### SpectrumAnalyticsEventsSummaries

##### [Get analytics summary]
GET/zones/{zone_id}/spectrum/analytics/events/summary
#### SpectrumApps

##### [List Spectrum applications]
GET/zones/{zone_id}/spectrum/apps
##### [Get Spectrum application configuration]
GET/zones/{zone_id}/spectrum/apps/{app_id}
##### [Create Spectrum application using a name for the origin]
POST/zones/{zone_id}/spectrum/apps
##### [Update Spectrum application configuration using a name for the origin]
PUT/zones/{zone_id}/spectrum/apps/{app_id}
##### [Delete Spectrum application]
DELETE/zones/{zone_id}/spectrum/apps/{app_id}
#### Addressing

#### AddressingRegional Hostnames

##### [List Regional Hostnames]
GET/zones/{zone_id}/addressing/regional_hostnames
##### [Fetch Regional Hostname]
GET/zones/{zone_id}/addressing/regional_hostnames/{hostname}
##### [Create Regional Hostname]
POST/zones/{zone_id}/addressing/regional_hostnames
##### [Update Regional Hostname]
PATCH/zones/{zone_id}/addressing/regional_hostnames/{hostname}
##### [Delete Regional Hostname]
DELETE/zones/{zone_id}/addressing/regional_hostnames/{hostname}
#### AddressingRegional HostnamesRegions

##### [List Regions]
GET/accounts/{account_id}/addressing/regional_hostnames/regions
#### AddressingServices

##### [List Services]
GET/accounts/{account_id}/addressing/services
#### AddressingAddress Maps

##### [List Address Maps]
GET/accounts/{account_id}/addressing/address_maps
##### [Address Map Details]
GET/accounts/{account_id}/addressing/address_maps/{address_map_id}
##### [Create Address Map]
POST/accounts/{account_id}/addressing/address_maps
##### [Update Address Map]
PATCH/accounts/{account_id}/addressing/address_maps/{address_map_id}
##### [Delete Address Map]
DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}
#### AddressingAddress MapsAccounts

##### [Add an account membership to an Address Map]
PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}
##### [Remove an account membership from an Address Map]
DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/accounts/{account_id}
#### AddressingAddress MapsIPs

##### [Add an IP to an Address Map]
PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}
##### [Remove an IP from an Address Map]
DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/ips/{ip_address}
#### AddressingAddress MapsZones

##### [Add a zone membership to an Address Map]
PUT/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}
##### [Remove a zone membership from an Address Map]
DELETE/accounts/{account_id}/addressing/address_maps/{address_map_id}/zones/{zone_id}
#### AddressingLOA Documents

##### [Download LOA Document]
GET/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download
##### [Upload LOA Document]
POST/accounts/{account_id}/addressing/loa_documents
#### AddressingPrefixes

##### [List Prefixes]
GET/accounts/{account_id}/addressing/prefixes
##### [Prefix Details]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}
##### [Add Prefix]
POST/accounts/{account_id}/addressing/prefixes
##### [Update Prefix Description]
PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}
##### [Delete Prefix]
DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}
#### AddressingPrefixesService Bindings

##### [List Service Bindings]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings
##### [Get Service Binding]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}
##### [Create Service Binding]
POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings
##### [Delete Service Binding]
DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings/{binding_id}
#### AddressingPrefixesBGP Prefixes

##### [List BGP Prefixes]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes
##### [Fetch BGP Prefix]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}
##### [Create BGP Prefix]
POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes
##### [Update BGP Prefix]
PATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}
#### AddressingPrefixesAdvertisement Status

##### [Get Advertisement Status]
DeprecatedGET/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status
##### [Update Prefix Dynamic Advertisement Status]
DeprecatedPATCH/accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status
#### AddressingPrefixesDelegations

##### [List Prefix Delegations]
GET/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations
##### [Create Prefix Delegation]
POST/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations
##### [Delete Prefix Delegation]
DELETE/accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations/{delegation_id}
#### Audit Logs

##### [Get account audit logs]
GET/accounts/{account_id}/audit_logs
#### Billing

#### BillingProfiles

##### [Billing Profile Details]
DeprecatedGET/accounts/{account_id}/billing/profile
#### BillingUsage

##### [Get PayGo Account Billable Usage (Beta)]
GET/accounts/{account_id}/billing/usage/paygo
#### Brand Protection

##### [Create new URL submissions]
POST/accounts/{account_id}/brand-protection/submit
##### [Read submitted URLs by ID]
GET/accounts/{account_id}/brand-protection/url-info
#### Brand ProtectionQueries

##### [Create new saved string queries]
POST/accounts/{account_id}/brand-protection/queries
##### [Delete saved string queries by ID]
DELETE/accounts/{account_id}/brand-protection/queries
##### [Create new saved string queries in bulk]
POST/accounts/{account_id}/brand-protection/queries/bulk
#### Brand ProtectionMatches

##### [Read matches for string queries by ID]
GET/accounts/{account_id}/brand-protection/matches
##### [Download matches for string queries by ID]
GET/accounts/{account_id}/brand-protection/matches/download
#### Brand ProtectionLogos

##### [Create new saved logo queries from image files]
POST/accounts/{account_id}/brand-protection/logos
##### [Delete saved logo queries by ID]
DELETE/accounts/{account_id}/brand-protection/logos/{logo_id}
#### Brand ProtectionLogo Matches

##### [Read matches for logo queries by ID]
GET/accounts/{account_id}/brand-protection/logo-matches
##### [Download matches for logo queries by ID]
GET/accounts/{account_id}/brand-protection/logo-matches/download
#### Brand ProtectionV2

#### Brand ProtectionV2Queries

##### [Get queries]
GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/queries
#### Brand ProtectionV2Matches

##### [List saved query matches]
GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/domain/matches
#### Brand ProtectionV2Logos

##### [Insert logo query]
POST/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries
##### [Delete logo query]
DELETE/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}
##### [Get logo queries]
GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries
#### Brand ProtectionV2Logo Matches

##### [List logo matches]
GET/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/matches
#### Diagnostics

#### DiagnosticsTraceroutes

##### [Traceroute]
POST/accounts/{account_id}/diagnostics/traceroute
#### DiagnosticsEndpoint Healthchecks

##### [List Endpoint Health Checks]
GET/accounts/{account_id}/diagnostics/endpoint-healthchecks
##### [Endpoint Health Check]
POST/accounts/{account_id}/diagnostics/endpoint-healthchecks
##### [Get Endpoint Health Check]
GET/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}
##### [Delete Endpoint Health Check]
DELETE/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}
##### [Update Endpoint Health Check]
PUT/accounts/{account_id}/diagnostics/endpoint-healthchecks/{id}
#### Images

#### ImagesV1

##### [List images]
DeprecatedGET/accounts/{account_id}/images/v1
##### [Image details]
GET/accounts/{account_id}/images/v1/{image_id}
##### [Upload an image]
POST/accounts/{account_id}/images/v1
##### [Update image]
PATCH/accounts/{account_id}/images/v1/{image_id}
##### [Delete image]
DELETE/accounts/{account_id}/images/v1/{image_id}
#### ImagesV1Keys

##### [List Signing Keys]
GET/accounts/{account_id}/images/v1/keys
##### [Create a new Signing Key]
PUT/accounts/{account_id}/images/v1/keys/{signing_key_name}
##### [Delete Signing Key]
DELETE/accounts/{account_id}/images/v1/keys/{signing_key_name}
#### ImagesV1Stats

##### [Images usage statistics]
GET/accounts/{account_id}/images/v1/stats
#### ImagesV1Variants

##### [List variants]
GET/accounts/{account_id}/images/v1/variants
##### [Variant details]
GET/accounts/{account_id}/images/v1/variants/{variant_id}
##### [Create a variant]
POST/accounts/{account_id}/images/v1/variants
##### [Update a variant]
PATCH/accounts/{account_id}/images/v1/variants/{variant_id}
##### [Delete a variant]
DELETE/accounts/{account_id}/images/v1/variants/{variant_id}
#### ImagesV1Blobs

##### [Base image]
GET/accounts/{account_id}/images/v1/{image_id}/blob
#### ImagesV2

##### [List images V2]
GET/accounts/{account_id}/images/v2
#### ImagesV2Direct Uploads

##### [Create authenticated direct upload URL V2]
POST/accounts/{account_id}/images/v2/direct_upload
#### Intel

#### IntelASN

##### [Get ASN Overview.]
GET/accounts/{account_id}/intel/asn/{asn}
#### IntelASNSubnets

##### [Get ASN Subnets]
GET/accounts/{account_id}/intel/asn/{asn}/subnets
#### IntelDNS

##### [Get Passive DNS by IP]
GET/accounts/{account_id}/intel/dns
#### IntelDomains

##### [Get Domain Details]
GET/accounts/{account_id}/intel/domain
#### IntelDomainsBulks

##### [Get Multiple Domain Details]
GET/accounts/{account_id}/intel/domain/bulk
#### IntelDomain History

##### [Get Domain History]
GET/accounts/{account_id}/intel/domain-history
#### IntelIPs

##### [Get IP Overview]
GET/accounts/{account_id}/intel/ip
#### IntelIP Lists

#### IntelMiscategorizations

##### [Create Miscategorization]
POST/accounts/{account_id}/intel/miscategorization
#### IntelWhois

##### [Get WHOIS Record]
GET/accounts/{account_id}/intel/whois
#### IntelIndicator Feeds

##### [Get indicator feeds owned by this account]
GET/accounts/{account_id}/intel/indicator-feeds
##### [Get indicator feed metadata]
GET/accounts/{account_id}/intel/indicator-feeds/{feed_id}
##### [Create new indicator feed]
POST/accounts/{account_id}/intel/indicator-feeds
##### [Update indicator feed metadata]
PUT/accounts/{account_id}/intel/indicator-feeds/{feed_id}
##### [Get indicator feed data]
GET/accounts/{account_id}/intel/indicator-feeds/{feed_id}/data
#### IntelIndicator FeedsSnapshots

##### [Update indicator feed data]
PUT/accounts/{account_id}/intel/indicator-feeds/{feed_id}/snapshot
#### IntelIndicator FeedsPermissions

##### [List indicator feed permissions]
GET/accounts/{account_id}/intel/indicator-feeds/permissions/view
##### [Grant permission to indicator feed]
PUT/accounts/{account_id}/intel/indicator-feeds/permissions/add
##### [Revoke permission to indicator feed]
PUT/accounts/{account_id}/intel/indicator-feeds/permissions/remove
#### IntelIndicator FeedsDownloads

#### IntelSinkholes

##### [List sinkholes owned by this account]
GET/accounts/{account_id}/intel/sinkholes
#### IntelAttack Surface Report

#### IntelAttack Surface ReportIssue Types

##### [Retrieves Security Center Issues Types]
GET/accounts/{account_id}/intel/attack-surface-report/issue-types
#### IntelAttack Surface ReportIssues

##### [Retrieves Security Center Issues]
DeprecatedGET/accounts/{account_id}/intel/attack-surface-report/issues
##### [Retrieves Security Center Issue Counts by Class]
DeprecatedGET/accounts/{account_id}/intel/attack-surface-report/issues/class
##### [Retrieves Security Center Issue Counts by Severity]
DeprecatedGET/accounts/{account_id}/intel/attack-surface-report/issues/severity
##### [Retrieves Security Center Issue Counts by Type]
DeprecatedGET/accounts/{account_id}/intel/attack-surface-report/issues/type
##### [Archives Security Center Insight]
DeprecatedPUT/accounts/{account_id}/intel/attack-surface-report/{issue_id}/dismiss
#### Magic Transit

#### Magic TransitApps

##### [List Apps]
GET/accounts/{account_id}/magic/apps
##### [Create a new App]
POST/accounts/{account_id}/magic/apps
##### [Update an App]
PUT/accounts/{account_id}/magic/apps/{account_app_id}
##### [Update an App]
PATCH/accounts/{account_id}/magic/apps/{account_app_id}
##### [Delete Account App]
DELETE/accounts/{account_id}/magic/apps/{account_app_id}
#### Magic TransitCf Interconnects

##### [List interconnects]
GET/accounts/{account_id}/magic/cf_interconnects
##### [List interconnect Details]
GET/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}
##### [Update interconnect]
PUT/accounts/{account_id}/magic/cf_interconnects/{cf_interconnect_id}
##### [Update multiple interconnects]
PUT/accounts/{account_id}/magic/cf_interconnects
#### Magic TransitGRE Tunnels

##### [List GRE tunnels]
GET/accounts/{account_id}/magic/gre_tunnels
##### [List GRE Tunnel Details]
GET/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}
##### [Create a GRE tunnel]
POST/accounts/{account_id}/magic/gre_tunnels
##### [Update GRE Tunnel]
PUT/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}
##### [Delete GRE Tunnel]
DELETE/accounts/{account_id}/magic/gre_tunnels/{gre_tunnel_id}
##### [Update multiple GRE tunnels]
PUT/accounts/{account_id}/magic/gre_tunnels
#### Magic TransitIPSEC Tunnels

##### [List IPsec tunnels]
GET/accounts/{account_id}/magic/ipsec_tunnels
##### [List IPsec tunnel details]
GET/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}
##### [Create an IPsec tunnel]
POST/accounts/{account_id}/magic/ipsec_tunnels
##### [Update IPsec Tunnel]
PUT/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}
##### [Delete IPsec Tunnel]
DELETE/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}
##### [Update multiple IPsec tunnels]
PUT/accounts/{account_id}/magic/ipsec_tunnels
##### [Generate Pre Shared Key (PSK) for IPsec tunnels]
POST/accounts/{account_id}/magic/ipsec_tunnels/{ipsec_tunnel_id}/psk_generate
#### Magic TransitRoutes

##### [List Routes]
GET/accounts/{account_id}/magic/routes
##### [Route Details]
GET/accounts/{account_id}/magic/routes/{route_id}
##### [Create a Route]
POST/accounts/{account_id}/magic/routes
##### [Update Route]
PUT/accounts/{account_id}/magic/routes/{route_id}
##### [Delete Route]
DELETE/accounts/{account_id}/magic/routes/{route_id}
##### [Update Many Routes]
PUT/accounts/{account_id}/magic/routes
##### [Delete Many Routes]
DELETE/accounts/{account_id}/magic/routes
#### Magic TransitSites

##### [List Sites]
GET/accounts/{account_id}/magic/sites
##### [Site Details]
GET/accounts/{account_id}/magic/sites/{site_id}
##### [Create a new Site]
POST/accounts/{account_id}/magic/sites
##### [Update Site]
PUT/accounts/{account_id}/magic/sites/{site_id}
##### [Patch Site]
PATCH/accounts/{account_id}/magic/sites/{site_id}
##### [Delete Site]
DELETE/accounts/{account_id}/magic/sites/{site_id}
#### Magic TransitSitesApp Configuration

##### [List App Configs]
GET/accounts/{account_id}/magic/sites/{site_id}/app_configs
##### [Create a new App Config]
POST/accounts/{account_id}/magic/sites/{site_id}/app_configs
##### [Update an App Config]
PUT/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}
##### [Update an App Config]
PATCH/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}
##### [Delete App Config]
DELETE/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}
#### Magic TransitSitesACLs

##### [List Site ACLs]
GET/accounts/{account_id}/magic/sites/{site_id}/acls
##### [Site ACL Details]
GET/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}
##### [Create a new Site ACL]
POST/accounts/{account_id}/magic/sites/{site_id}/acls
##### [Update Site ACL]
PUT/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}
##### [Patch Site ACL]
PATCH/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}
##### [Delete Site ACL]
DELETE/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}
#### Magic TransitSitesLANs

##### [List Site LANs]
GET/accounts/{account_id}/magic/sites/{site_id}/lans
##### [Site LAN Details]
GET/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}
##### [Create a new Site LAN]
POST/accounts/{account_id}/magic/sites/{site_id}/lans
##### [Update Site LAN]
PUT/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}
##### [Patch Site LAN]
PATCH/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}
##### [Delete Site LAN]
DELETE/accounts/{account_id}/magic/sites/{site_id}/lans/{lan_id}
#### Magic TransitSitesWANs

##### [List Site WANs]
GET/accounts/{account_id}/magic/sites/{site_id}/wans
##### [Site WAN Details]
GET/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}
##### [Create a new Site WAN]
POST/accounts/{account_id}/magic/sites/{site_id}/wans
##### [Update Site WAN]
PUT/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}
##### [Patch Site WAN]
PATCH/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}
##### [Delete Site WAN]
DELETE/accounts/{account_id}/magic/sites/{site_id}/wans/{wan_id}
#### Magic TransitConnectors

##### [List Connectors]
GET/accounts/{account_id}/magic/connectors
##### [Fetch Connector]
GET/accounts/{account_id}/magic/connectors/{connector_id}
##### [Add a connector to your account]
POST/accounts/{account_id}/magic/connectors
##### [Replace Connector or Re-provision License Key]
PUT/accounts/{account_id}/magic/connectors/{connector_id}
##### [Edit Connector to update specific properties or Re-provision License Key]
PATCH/accounts/{account_id}/magic/connectors/{connector_id}
##### [Remove a connector from your account]
DELETE/accounts/{account_id}/magic/connectors/{connector_id}
#### Magic TransitConnectorsEvents

##### [List Events]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events
##### [Get Event]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/{event_t}.{event_n}
#### Magic TransitConnectorsEventsLatest

##### [Get latest Events]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/events/latest
#### Magic TransitConnectorsSnapshots

##### [List Snapshots]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots
##### [Get Snapshot]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/{snapshot_t}
#### Magic TransitConnectorsSnapshotsLatest

##### [Get latest Snapshots]
GET/accounts/{account_id}/magic/connectors/{connector_id}/telemetry/snapshots/latest
#### Magic TransitPCAPs

##### [List packet capture requests]
GET/accounts/{account_id}/pcaps
##### [Get PCAP request]
GET/accounts/{account_id}/pcaps/{pcap_id}
##### [Create PCAP request]
POST/accounts/{account_id}/pcaps
##### [Stop full PCAP]
PUT/accounts/{account_id}/pcaps/{pcap_id}/stop
#### Magic TransitPCAPsOwnership

##### [List PCAPs Bucket Ownership]
GET/accounts/{account_id}/pcaps/ownership
##### [Add buckets for full packet captures]
POST/accounts/{account_id}/pcaps/ownership
##### [Delete buckets for full packet captures]
DELETE/accounts/{account_id}/pcaps/ownership/{ownership_id}
##### [Validate buckets for full packet captures]
POST/accounts/{account_id}/pcaps/ownership/validate
#### Magic TransitPCAPsDownload

##### [Download Simple PCAP]
GET/accounts/{account_id}/pcaps/{pcap_id}/download
#### Magic Network Monitoring

#### Magic Network MonitoringVPC Flows

#### Magic Network MonitoringVPC FlowsTokens

##### [Generate authentication token for VPC flow logs export.]
POST/accounts/{account_id}/mnm/vpc-flows/token
#### Magic Network MonitoringConfigs

##### [List account configuration]
GET/accounts/{account_id}/mnm/config
##### [Create account configuration]
POST/accounts/{account_id}/mnm/config
##### [Update an entire account configuration]
PUT/accounts/{account_id}/mnm/config
##### [Update account configuration fields]
PATCH/accounts/{account_id}/mnm/config
##### [Delete account configuration]
DELETE/accounts/{account_id}/mnm/config
#### Magic Network MonitoringConfigsFull

##### [List rules and account configuration]
GET/accounts/{account_id}/mnm/config/full
#### Magic Network MonitoringRules

##### [List rules]
GET/accounts/{account_id}/mnm/rules
##### [Get rule]
GET/accounts/{account_id}/mnm/rules/{rule_id}
##### [Create rules]
POST/accounts/{account_id}/mnm/rules
##### [Update rules]
PUT/accounts/{account_id}/mnm/rules
##### [Update rule]
PATCH/accounts/{account_id}/mnm/rules/{rule_id}
##### [Delete rule]
DELETE/accounts/{account_id}/mnm/rules/{rule_id}
#### Magic Network MonitoringRulesAdvertisements

##### [Update advertisement for rule]
PATCH/accounts/{account_id}/mnm/rules/{rule_id}/advertisement
#### Magic Cloud Networking

#### Magic Cloud NetworkingCatalog Syncs

##### [List Catalog Syncs]
GET/accounts/{account_id}/magic/cloud/catalog-syncs
##### [Read Catalog Sync]
GET/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}
##### [Create Catalog Sync]
POST/accounts/{account_id}/magic/cloud/catalog-syncs
##### [Update Catalog Sync]
PUT/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}
##### [Patch Catalog Sync]
PATCH/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}
##### [Delete Catalog Sync]
DELETE/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}
##### [Run Catalog Sync]
POST/accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}/refresh
#### Magic Cloud NetworkingCatalog SyncsPrebuilt Policies

##### [List Prebuilt Policies]
GET/accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies
#### Magic Cloud NetworkingOn Ramps

##### [List On-ramps]
GET/accounts/{account_id}/magic/cloud/onramps
##### [Read On-ramp]
GET/accounts/{account_id}/magic/cloud/onramps/{onramp_id}
##### [Create On-ramp]
POST/accounts/{account_id}/magic/cloud/onramps
##### [Update On-ramp]
PUT/accounts/{account_id}/magic/cloud/onramps/{onramp_id}
##### [Patch On-ramp]
PATCH/accounts/{account_id}/magic/cloud/onramps/{onramp_id}
##### [Delete On-ramp]
DELETE/accounts/{account_id}/magic/cloud/onramps/{onramp_id}
##### [Apply On-ramp]
POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/apply
##### [Export as Terraform]
POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export
##### [Plan On-ramp]
POST/accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan
#### Magic Cloud NetworkingOn RampsAddress Spaces

##### [Read Magic WAN Address Space]
GET/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space
##### [Update Magic WAN Address Space]
PUT/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space
##### [Patch Magic WAN Address Space]
PATCH/accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space
#### Magic Cloud NetworkingCloud Integrations

##### [List Cloud Integrations]
GET/accounts/{account_id}/magic/cloud/providers
##### [Read Cloud Integration]
GET/accounts/{account_id}/magic/cloud/providers/{provider_id}
##### [Create Cloud Integration]
POST/accounts/{account_id}/magic/cloud/providers
##### [Update Cloud Integration]
PUT/accounts/{account_id}/magic/cloud/providers/{provider_id}
##### [Patch Cloud Integration]
PATCH/accounts/{account_id}/magic/cloud/providers/{provider_id}
##### [Delete Cloud Integration]
DELETE/accounts/{account_id}/magic/cloud/providers/{provider_id}
##### [Run Discovery for All Integrations]
POST/accounts/{account_id}/magic/cloud/providers/discover
##### [Run Discovery]
POST/accounts/{account_id}/magic/cloud/providers/{provider_id}/discover
##### [Get Cloud Integration Setup Config]
GET/accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup
#### Magic Cloud NetworkingResources

##### [List Resources]
GET/accounts/{account_id}/magic/cloud/resources
##### [Read Resource]
GET/accounts/{account_id}/magic/cloud/resources/{resource_id}
##### [Export Resources]
GET/accounts/{account_id}/magic/cloud/resources/export
##### [Preview Rego Query]
POST/accounts/{account_id}/magic/cloud/resources/policy-preview
#### Network Interconnects

#### Network InterconnectsCNIs

##### [List existing CNI objects]
GET/accounts/{account_id}/cni/cnis
##### [Get information about a CNI object]
GET/accounts/{account_id}/cni/cnis/{cni}
##### [Create a new CNI object]
POST/accounts/{account_id}/cni/cnis
##### [Modify stored information about a CNI object]
PUT/accounts/{account_id}/cni/cnis/{cni}
##### [Delete a specified CNI object]
DELETE/accounts/{account_id}/cni/cnis/{cni}
#### Network InterconnectsInterconnects

##### [List existing interconnects]
GET/accounts/{account_id}/cni/interconnects
##### [Get information about an interconnect object]
GET/accounts/{account_id}/cni/interconnects/{icon}
##### [Create a new interconnect]
POST/accounts/{account_id}/cni/interconnects
##### [Delete an interconnect object]
DELETE/accounts/{account_id}/cni/interconnects/{icon}
##### [Generate the Letter of Authorization (LOA) for a given interconnect]
GET/accounts/{account_id}/cni/interconnects/{icon}/loa
##### [Get the current status of an interconnect object]
GET/accounts/{account_id}/cni/interconnects/{icon}/status
#### Network InterconnectsSettings

##### [Get the current settings for the active account]
GET/accounts/{account_id}/cni/settings
##### [Update the current settings for the active account]
PUT/accounts/{account_id}/cni/settings
#### Network InterconnectsSlots

##### [Retrieve a list of all slots matching the specified parameters]
GET/accounts/{account_id}/cni/slots
##### [Get information about the specified slot]
GET/accounts/{account_id}/cni/slots/{slot}
#### MTLS Certificates

##### [List mTLS certificates]
GET/accounts/{account_id}/mtls_certificates
##### [Get mTLS certificate]
GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}
##### [Upload mTLS certificate]
POST/accounts/{account_id}/mtls_certificates
##### [Delete mTLS certificate]
DELETE/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}
#### MTLS CertificatesAssociations

##### [List mTLS certificate associations]
GET/accounts/{account_id}/mtls_certificates/{mtls_certificate_id}/associations
#### Pages

#### PagesProjects

##### [Get projects]
GET/accounts/{account_id}/pages/projects
##### [Get project]
GET/accounts/{account_id}/pages/projects/{project_name}
##### [Create project]
POST/accounts/{account_id}/pages/projects
##### [Update project]
PATCH/accounts/{account_id}/pages/projects/{project_name}
##### [Delete project]
DELETE/accounts/{account_id}/pages/projects/{project_name}
##### [Purge build cache]
POST/accounts/{account_id}/pages/projects/{project_name}/purge_build_cache
#### PagesProjectsDeployments

##### [Get deployments]
GET/accounts/{account_id}/pages/projects/{project_name}/deployments
##### [Get deployment info]
GET/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}
##### [Create deployment]
POST/accounts/{account_id}/pages/projects/{project_name}/deployments
##### [Delete deployment]
DELETE/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}
##### [Retry deployment]
POST/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry
##### [Rollback deployment]
POST/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback
#### PagesProjectsDeploymentsHistory

#### PagesProjectsDeploymentsHistoryLogs

##### [Get deployment logs]
GET/accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs
#### PagesProjectsDomains

##### [Get domains]
GET/accounts/{account_id}/pages/projects/{project_name}/domains
##### [Get domain]
GET/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
##### [Add domain]
POST/accounts/{account_id}/pages/projects/{project_name}/domains
##### [Patch domain]
PATCH/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
##### [Delete domain]
DELETE/accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
#### Registrar

#### RegistrarDomains

##### [List domains]
GET/accounts/{account_id}/registrar/domains
##### [Get domain]
GET/accounts/{account_id}/registrar/domains/{domain_name}
##### [Update domain]
PUT/accounts/{account_id}/registrar/domains/{domain_name}
#### Rules Trace

#### Rules TraceTraces

##### [Request Trace]
POST/accounts/{account_id}/request-tracer/trace
#### Rules Lists

#### Rules ListsLists

##### [Get lists]
GET/accounts/{account_id}/rules/lists
##### [Get a list]
GET/accounts/{account_id}/rules/lists/{list_id}
##### [Create a list]
POST/accounts/{account_id}/rules/lists
##### [Update a list]
PUT/accounts/{account_id}/rules/lists/{list_id}
##### [Delete a list]
DELETE/accounts/{account_id}/rules/lists/{list_id}
#### Rules ListsListsBulk Operations

##### [Get bulk operation status]
GET/accounts/{account_id}/rules/lists/bulk_operations/{operation_id}
#### Rules ListsListsItems

##### [Get list items]
GET/accounts/{account_id}/rules/lists/{list_id}/items
##### [Get a list item]
GET/accounts/{account_id}/rules/lists/{list_id}/items/{item_id}
##### [Create list items]
POST/accounts/{account_id}/rules/lists/{list_id}/items
##### [Update all list items]
PUT/accounts/{account_id}/rules/lists/{list_id}/items
##### [Delete list items]
DELETE/accounts/{account_id}/rules/lists/{list_id}/items
#### Stream

##### [List videos]
GET/accounts/{account_id}/stream
##### [Retrieve video details]
GET/accounts/{account_id}/stream/{identifier}
##### [Initiate video uploads using TUS]
POST/accounts/{account_id}/stream
##### [Edit video details]
POST/accounts/{account_id}/stream/{identifier}
##### [Delete video]
DELETE/accounts/{account_id}/stream/{identifier}
#### StreamAudio Tracks

##### [List additional audio tracks on a video]
GET/accounts/{account_id}/stream/{identifier}/audio
##### [Edit additional audio tracks on a video]
PATCH/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}
##### [Delete additional audio tracks on a video]
DELETE/accounts/{account_id}/stream/{identifier}/audio/{audio_identifier}
##### [Add audio tracks to a video]
POST/accounts/{account_id}/stream/{identifier}/audio/copy
#### StreamVideos

##### [Storage use]
GET/accounts/{account_id}/stream/storage-usage
#### StreamClip

##### [Clip videos given a start and end time]
POST/accounts/{account_id}/stream/clip
#### StreamCopy

##### [Upload videos from a URL]
POST/accounts/{account_id}/stream/copy
#### StreamDirect Upload

##### [Upload videos via direct upload URLs]
POST/accounts/{account_id}/stream/direct_upload
#### StreamKeys

##### [List signing keys]
GET/accounts/{account_id}/stream/keys
##### [Create signing keys]
POST/accounts/{account_id}/stream/keys
##### [Delete signing keys]
DELETE/accounts/{account_id}/stream/keys/{identifier}
#### StreamLive Inputs

##### [List live inputs]
GET/accounts/{account_id}/stream/live_inputs
##### [Retrieve a live input]
GET/accounts/{account_id}/stream/live_inputs/{live_input_identifier}
##### [Create a live input]
POST/accounts/{account_id}/stream/live_inputs
##### [Update a live input]
PUT/accounts/{account_id}/stream/live_inputs/{live_input_identifier}
##### [Delete a live input]
DELETE/accounts/{account_id}/stream/live_inputs/{live_input_identifier}
#### StreamLive InputsOutputs

##### [List all outputs associated with a specified live input]
GET/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs
##### [Create a new output, connected to a live input]
POST/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs
##### [Update an output]
PUT/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}
##### [Delete an output]
DELETE/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}
#### StreamWatermarks

##### [List watermark profiles]
GET/accounts/{account_id}/stream/watermarks
##### [Watermark profile details]
GET/accounts/{account_id}/stream/watermarks/{identifier}
##### [Create watermark profiles via basic upload]
POST/accounts/{account_id}/stream/watermarks
##### [Delete watermark profiles]
DELETE/accounts/{account_id}/stream/watermarks/{identifier}
#### StreamWebhooks

##### [View webhooks]
GET/accounts/{account_id}/stream/webhook
##### [Create webhooks]
PUT/accounts/{account_id}/stream/webhook
##### [Delete webhooks]
DELETE/accounts/{account_id}/stream/webhook
#### StreamCaptions

##### [List captions or subtitles]
GET/accounts/{account_id}/stream/{identifier}/captions
#### StreamCaptionsLanguage

##### [List captions or subtitles for a provided language]
GET/accounts/{account_id}/stream/{identifier}/captions/{language}
##### [Generate captions or subtitles for a provided language via AI]
POST/accounts/{account_id}/stream/{identifier}/captions/{language}/generate
##### [Upload captions or subtitles]
PUT/accounts/{account_id}/stream/{identifier}/captions/{language}
##### [Delete captions or subtitles]
DELETE/accounts/{account_id}/stream/{identifier}/captions/{language}
#### StreamCaptionsLanguageVtt

##### [Return WebVTT captions for a provided language]
GET/accounts/{account_id}/stream/{identifier}/captions/{language}/vtt
#### StreamDownloads

##### [List downloads]
GET/accounts/{account_id}/stream/{identifier}/downloads
##### [Create downloads]
POST/accounts/{account_id}/stream/{identifier}/downloads
##### [Delete downloads]
DELETE/accounts/{account_id}/stream/{identifier}/downloads
#### StreamEmbed

##### [Retrieve embed Code HTML]
GET/accounts/{account_id}/stream/{identifier}/embed
#### StreamToken

##### [Create signed URL tokens for videos]
POST/accounts/{account_id}/stream/{identifier}/token
#### Alerting

#### AlertingAvailable Alerts

##### [Get Alert Types]
GET/accounts/{account_id}/alerting/v3/available_alerts
#### AlertingDestinations

#### AlertingDestinationsEligible

##### [Get delivery mechanism eligibility]
GET/accounts/{account_id}/alerting/v3/destinations/eligible
#### AlertingDestinationsPagerduty

##### [List PagerDuty services]
GET/accounts/{account_id}/alerting/v3/destinations/pagerduty
##### [Create PagerDuty integration token]
POST/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect
##### [Delete PagerDuty Services]
DELETE/accounts/{account_id}/alerting/v3/destinations/pagerduty
##### [Connect PagerDuty]
GET/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}
#### AlertingDestinationsWebhooks

##### [List webhooks]
GET/accounts/{account_id}/alerting/v3/destinations/webhooks
##### [Get a webhook]
GET/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
##### [Create a webhook]
POST/accounts/{account_id}/alerting/v3/destinations/webhooks
##### [Update a webhook]
PUT/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
##### [Delete a webhook]
DELETE/accounts/{account_id}/alerting/v3/destinations/webhooks/{webhook_id}
#### AlertingHistory

##### [List History]
GET/accounts/{account_id}/alerting/v3/history
#### AlertingPolicies

##### [List Notification policies]
GET/accounts/{account_id}/alerting/v3/policies
##### [Get a Notification policy]
GET/accounts/{account_id}/alerting/v3/policies/{policy_id}
##### [Create a Notification policy]
POST/accounts/{account_id}/alerting/v3/policies
##### [Update a Notification policy]
PUT/accounts/{account_id}/alerting/v3/policies/{policy_id}
##### [Delete a Notification policy]
DELETE/accounts/{account_id}/alerting/v3/policies/{policy_id}
#### AlertingSilences

##### [List Silences]
GET/accounts/{account_id}/alerting/v3/silences
##### [Get Silence]
GET/accounts/{account_id}/alerting/v3/silences/{silence_id}
##### [Create Silences]
POST/accounts/{account_id}/alerting/v3/silences
##### [Update Silences]
PUT/accounts/{account_id}/alerting/v3/silences
##### [Delete Silence]
DELETE/accounts/{account_id}/alerting/v3/silences/{silence_id}
#### D1

#### D1Database

##### [List D1 Databases]
GET/accounts/{account_id}/d1/database
##### [Get D1 Database]
GET/accounts/{account_id}/d1/database/{database_id}
##### [Create D1 Database]
POST/accounts/{account_id}/d1/database
##### [Update D1 Database]
PUT/accounts/{account_id}/d1/database/{database_id}
##### [Update D1 Database partially]
PATCH/accounts/{account_id}/d1/database/{database_id}
##### [Delete D1 Database]
DELETE/accounts/{account_id}/d1/database/{database_id}
##### [Query D1 Database]
POST/accounts/{account_id}/d1/database/{database_id}/query
##### [Raw D1 Database query]
POST/accounts/{account_id}/d1/database/{database_id}/raw
##### [Export D1 Database as SQL]
POST/accounts/{account_id}/d1/database/{database_id}/export
##### [Import SQL into your D1 Database]
POST/accounts/{account_id}/d1/database/{database_id}/import
#### D1DatabaseTime Travel

##### [Get D1 database bookmark]
GET/accounts/{account_id}/d1/database/{database_id}/time_travel/bookmark
##### [Restore D1 Database to a bookmark or point in time]
POST/accounts/{account_id}/d1/database/{database_id}/time_travel/restore
#### R2

#### R2Buckets

##### [List Buckets]
GET/accounts/{account_id}/r2/buckets
##### [Get Bucket]
GET/accounts/{account_id}/r2/buckets/{bucket_name}
##### [Create Bucket]
POST/accounts/{account_id}/r2/buckets
##### [Patch Bucket]
PATCH/accounts/{account_id}/r2/buckets/{bucket_name}
##### [Delete Bucket]
DELETE/accounts/{account_id}/r2/buckets/{bucket_name}
#### R2BucketsLifecycle

##### [Get Object Lifecycle Rules]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle
##### [Put Object Lifecycle Rules]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/lifecycle
#### R2BucketsCORS

##### [Get Bucket CORS Policy]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/cors
##### [Put Bucket CORS Policy]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/cors
##### [Delete Bucket CORS Policy]
DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/cors
#### R2BucketsDomains

#### R2BucketsDomainsCustom

##### [List Custom Domains of Bucket]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom
##### [Get Custom Domain Settings]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}
##### [Attach Custom Domain To Bucket]
POST/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom
##### [Configure Custom Domain Settings]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}
##### [Remove Custom Domain From Bucket]
DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/domains/custom/{domain}
#### R2BucketsDomainsManaged

##### [Get r2.dev Domain of Bucket]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed
##### [Update r2.dev Domain of Bucket]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/domains/managed
#### R2BucketsEvent Notifications

##### [List Event Notification Rules]
GET/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration
##### [Get Event Notification Rule]
GET/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}
##### [Create Event Notification Rule]
PUT/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}
##### [Delete Event Notification Rules]
DELETE/accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}
#### R2BucketsLocks

##### [Get Bucket Lock Rules]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/lock
##### [Put Bucket Lock Rules]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/lock
#### R2BucketsMetrics

##### [Get Account-Level Metrics]
GET/accounts/{account_id}/r2/metrics
#### R2BucketsSippy

##### [Get Sippy Configuration]
GET/accounts/{account_id}/r2/buckets/{bucket_name}/sippy
##### [Enable Sippy]
PUT/accounts/{account_id}/r2/buckets/{bucket_name}/sippy
##### [Disable Sippy]
DELETE/accounts/{account_id}/r2/buckets/{bucket_name}/sippy
#### R2Temporary Credentials

##### [Create Temporary Access Credentials]
POST/accounts/{account_id}/r2/temp-access-credentials
#### R2Super Slurper

#### R2Super SlurperJobs

##### [List jobs]
GET/accounts/{account_id}/slurper/jobs
##### [Get job details]
GET/accounts/{account_id}/slurper/jobs/{job_id}
##### [Create a job]
POST/accounts/{account_id}/slurper/jobs
##### [Abort all jobs]
PUT/accounts/{account_id}/slurper/jobs/abortAll
##### [Abort a job]
PUT/accounts/{account_id}/slurper/jobs/{job_id}/abort
##### [Pause a job]
PUT/accounts/{account_id}/slurper/jobs/{job_id}/pause
##### [Get job progress]
GET/accounts/{account_id}/slurper/jobs/{job_id}/progress
##### [Resume a job]
PUT/accounts/{account_id}/slurper/jobs/{job_id}/resume
#### R2Super SlurperJobsLogs

##### [Get job logs]
GET/accounts/{account_id}/slurper/jobs/{job_id}/logs
#### R2Super SlurperConnectivity Precheck

##### [Check source connectivity]
PUT/accounts/{account_id}/slurper/source/connectivity-precheck
##### [Check target connectivity]
PUT/accounts/{account_id}/slurper/target/connectivity-precheck
#### R2 Data Catalog

##### [List R2 catalogs]
GET/accounts/{account_id}/r2-catalog
##### [Get R2 catalog details]
GET/accounts/{account_id}/r2-catalog/{bucket_name}
##### [Enable R2 bucket as a catalog]
POST/accounts/{account_id}/r2-catalog/{bucket_name}/enable
##### [Disable R2 catalog]
POST/accounts/{account_id}/r2-catalog/{bucket_name}/disable
#### R2 Data CatalogMaintenance Configs

##### [Get catalog maintenance configuration]
GET/accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs
##### [Update catalog maintenance configuration]
POST/accounts/{account_id}/r2-catalog/{bucket_name}/maintenance-configs
#### R2 Data CatalogCredentials

##### [Store catalog credentials]
POST/accounts/{account_id}/r2-catalog/{bucket_name}/credential
#### R2 Data CatalogNamespaces

##### [List namespaces in catalog]
GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces
#### R2 Data CatalogNamespacesTables

##### [List tables in namespace]
GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables
#### R2 Data CatalogNamespacesTablesMaintenance Configs

##### [Get table maintenance configuration]
GET/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs
##### [Update table maintenance configuration]
POST/accounts/{account_id}/r2-catalog/{bucket_name}/namespaces/{namespace}/tables/{table_name}/maintenance-configs
#### Workers For Platforms

#### Workers For PlatformsDispatch

#### Workers For PlatformsDispatchNamespaces

##### [List dispatch namespaces]
GET/accounts/{account_id}/workers/dispatch/namespaces
##### [Get dispatch namespace]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}
##### [Create dispatch namespace]
POST/accounts/{account_id}/workers/dispatch/namespaces
##### [Delete dispatch namespace]
DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}
#### Workers For PlatformsDispatchNamespacesScripts

##### [Worker Details]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}
##### [Upload Worker Module]
PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}
##### [Delete Worker]
DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}
#### Workers For PlatformsDispatchNamespacesScriptsAsset Upload

##### [Create Assets Upload Session]
POST/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/assets-upload-session
#### Workers For PlatformsDispatchNamespacesScriptsContent

##### [Get Script Content]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content
##### [Put Script Content]
PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/content
#### Workers For PlatformsDispatchNamespacesScriptsSettings

##### [Get Script Settings]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings
##### [Patch Script Settings]
PATCH/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/settings
#### Workers For PlatformsDispatchNamespacesScriptsBindings

##### [Get Script Bindings]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/bindings
#### Workers For PlatformsDispatchNamespacesScriptsSecrets

##### [List Script Secrets]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets
##### [Get secret binding]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}
##### [Add script secret]
PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets
##### [Delete script secret]
DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/secrets/{secret_name}
#### Workers For PlatformsDispatchNamespacesScriptsTags

##### [Get Script Tags]
GET/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags
##### [Put Script Tags]
PUT/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags
##### [Delete Script Tag]
DELETE/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}/scripts/{script_name}/tags/{tag}
#### Zero Trust

#### Zero TrustDevices

##### [List devices (deprecated)]
DeprecatedGET/accounts/{account_id}/devices
##### [Get device (deprecated)]
DeprecatedGET/accounts/{account_id}/devices/{device_id}
#### Zero TrustDevicesDevices

##### [List devices]
GET/accounts/{account_id}/devices/physical-devices
##### [Get device]
GET/accounts/{account_id}/devices/physical-devices/{device_id}
##### [Delete device]
DELETE/accounts/{account_id}/devices/physical-devices/{device_id}
##### [Revoke device registrations]
POST/accounts/{account_id}/devices/physical-devices/{device_id}/revoke
#### Zero TrustDevicesResilience

#### Zero TrustDevicesResilienceGlobal WARP Override

##### [Retrieve Global WARP override state]
GET/accounts/{account_id}/devices/resilience/disconnect
##### [Set Global WARP override state]
POST/accounts/{account_id}/devices/resilience/disconnect
#### Zero TrustDevicesRegistrations

##### [List registrations]
GET/accounts/{account_id}/devices/registrations
##### [Get registration]
GET/accounts/{account_id}/devices/registrations/{registration_id}
##### [Delete registration]
DELETE/accounts/{account_id}/devices/registrations/{registration_id}
##### [Delete registrations]
DELETE/accounts/{account_id}/devices/registrations
##### [Revoke registrations]
POST/accounts/{account_id}/devices/registrations/revoke
##### [Unrevoke registrations]
POST/accounts/{account_id}/devices/registrations/unrevoke
#### Zero TrustDevicesDEX Tests

##### [List Device DEX tests]
GET/accounts/{account_id}/dex/devices/dex_tests
##### [Get Device DEX test]
GET/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Create Device DEX test]
POST/accounts/{account_id}/dex/devices/dex_tests
##### [Update Device DEX test]
PUT/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
##### [Delete Device DEX test]
DELETE/accounts/{account_id}/dex/devices/dex_tests/{dex_test_id}
#### Zero TrustDevicesIP Profiles

##### [List IP profiles]
GET/accounts/{account_id}/devices/ip-profiles
##### [Get IP profile]
GET/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Create IP profile]
POST/accounts/{account_id}/devices/ip-profiles
##### [Update IP profile]
PATCH/accounts/{account_id}/devices/ip-profiles/{profile_id}
##### [Delete IP profile]
DELETE/accounts/{account_id}/devices/ip-profiles/{profile_id}
#### Zero TrustDevicesNetworks

##### [List your device managed networks]
GET/accounts/{account_id}/devices/networks
##### [Get device managed network details]
GET/accounts/{account_id}/devices/networks/{network_id}
##### [Create a device managed network]
POST/accounts/{account_id}/devices/networks
##### [Update a device managed network]
PUT/accounts/{account_id}/devices/networks/{network_id}
##### [Delete a device managed network]
DELETE/accounts/{account_id}/devices/networks/{network_id}
#### Zero TrustDevicesFleet Status

##### [Get the live status of a latest device]
GET/accounts/{account_id}/dex/devices/{device_id}/fleet-status/live
#### Zero TrustDevicesPolicies

#### Zero TrustDevicesPoliciesDefault

##### [Get the default device settings profile]
GET/accounts/{account_id}/devices/policy
##### [Update the default device settings profile]
PATCH/accounts/{account_id}/devices/policy
#### Zero TrustDevicesPoliciesDefaultExcludes

##### [Get the Split Tunnel exclude list]
GET/accounts/{account_id}/devices/policy/exclude
##### [Set the Split Tunnel exclude list]
PUT/accounts/{account_id}/devices/policy/exclude
#### Zero TrustDevicesPoliciesDefaultIncludes

##### [Get the Split Tunnel include list]
GET/accounts/{account_id}/devices/policy/include
##### [Set the Split Tunnel include list]
PUT/accounts/{account_id}/devices/policy/include
#### Zero TrustDevicesPoliciesDefaultFallback Domains

##### [Get your Local Domain Fallback list]
GET/accounts/{account_id}/devices/policy/fallback_domains
##### [Set your Local Domain Fallback list]
PUT/accounts/{account_id}/devices/policy/fallback_domains
#### Zero TrustDevicesPoliciesDefaultCertificates

##### [Get device certificate provisioning status]
GET/zones/{zone_id}/devices/policy/certificates
##### [Update device certificate provisioning status]
PATCH/zones/{zone_id}/devices/policy/certificates
#### Zero TrustDevicesPoliciesCustom

##### [List device settings profiles]
GET/accounts/{account_id}/devices/policies
##### [Get device settings profile by ID]
GET/accounts/{account_id}/devices/policy/{policy_id}
##### [Create a device settings profile]
POST/accounts/{account_id}/devices/policy
##### [Update a device settings profile]
PATCH/accounts/{account_id}/devices/policy/{policy_id}
##### [Delete a device settings profile]
DELETE/accounts/{account_id}/devices/policy/{policy_id}
#### Zero TrustDevicesPoliciesCustomExcludes

##### [Get the Split Tunnel exclude list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/exclude
##### [Set the Split Tunnel exclude list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/exclude
#### Zero TrustDevicesPoliciesCustomIncludes

##### [Get the Split Tunnel include list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/include
##### [Set the Split Tunnel include list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/include
#### Zero TrustDevicesPoliciesCustomFallback Domains

##### [Get the Local Domain Fallback list for a device settings profile]
GET/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains
##### [Set the Local Domain Fallback list for a device settings profile]
PUT/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains
#### Zero TrustDevicesPosture

##### [List device posture rules]
GET/accounts/{account_id}/devices/posture
##### [Get device posture rule details]
GET/accounts/{account_id}/devices/posture/{rule_id}
##### [Create a device posture rule]
POST/accounts/{account_id}/devices/posture
##### [Update a device posture rule]
PUT/accounts/{account_id}/devices/posture/{rule_id}
##### [Delete a device posture rule]
DELETE/accounts/{account_id}/devices/posture/{rule_id}
#### Zero TrustDevicesPostureIntegrations

##### [List your device posture integrations]
GET/accounts/{account_id}/devices/posture/integration
##### [Get device posture integration details]
GET/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Create a device posture integration]
POST/accounts/{account_id}/devices/posture/integration
##### [Update a device posture integration]
PATCH/accounts/{account_id}/devices/posture/integration/{integration_id}
##### [Delete a device posture integration]
DELETE/accounts/{account_id}/devices/posture/integration/{integration_id}
#### Zero TrustDevicesRevoke

##### [Revoke devices (deprecated)]
DeprecatedPOST/accounts/{account_id}/devices/revoke
#### Zero TrustDevicesSettings

##### [Get device settings for a Zero Trust account]
GET/accounts/{account_id}/devices/settings
##### [Update device settings for a Zero Trust account]
PUT/accounts/{account_id}/devices/settings
##### [Patch device settings for a Zero Trust account]
PATCH/accounts/{account_id}/devices/settings
##### [Reset device settings for a Zero Trust account with defaults. This turns off all proxying.]
DELETE/accounts/{account_id}/devices/settings
#### Zero TrustDevicesUnrevoke

##### [Unrevoke devices (deprecated)]
DeprecatedPOST/accounts/{account_id}/devices/unrevoke
#### Zero TrustDevicesOverride Codes

##### [Get override codes (deprecated)
]
DeprecatedGET/accounts/{account_id}/devices/{device_id}/override_codes
##### [Get override codes]
GET/accounts/{account_id}/devices/registrations/{registration_id}/override_codes
#### Zero TrustIdentity Providers

##### [List Access identity providers]
GET/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers
##### [Get an Access identity provider]
GET/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}
##### [Add an Access identity provider]
POST/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers
##### [Update an Access identity provider]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}
##### [Delete an Access identity provider]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/identity_providers/{identity_provider_id}
#### Zero TrustIdentity ProvidersSCIM

#### Zero TrustIdentity ProvidersSCIMGroups

##### [List SCIM Group resources]
GET/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups
#### Zero TrustIdentity ProvidersSCIMUsers

##### [List SCIM User resources]
GET/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/users
#### Zero TrustOrganizations

##### [Get your Zero Trust organization]
GET/{accounts_or_zones}/{account_or_zone_id}/access/organizations
##### [Create your Zero Trust organization]
POST/{accounts_or_zones}/{account_or_zone_id}/access/organizations
##### [Update your Zero Trust organization]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/organizations
##### [Revoke all Access tokens for a user]
POST/{accounts_or_zones}/{account_or_zone_id}/access/organizations/revoke_user
#### Zero TrustOrganizationsDOH

##### [Get your Zero Trust organization DoH settings]
GET/accounts/{account_id}/access/organizations/doh
##### [Update your Zero Trust organization DoH settings]
PUT/accounts/{account_id}/access/organizations/doh
#### Zero TrustSeats

##### [Update a user seat]
PATCH/accounts/{account_id}/access/seats
#### Zero TrustAccess

#### Zero TrustAccessAI Controls

#### Zero TrustAccessAI ControlsMcp

#### Zero TrustAccessAI ControlsMcpPortals

##### [List MCP Portals]
GET/accounts/{account_id}/access/ai-controls/mcp/portals
##### [Create a new MCP Portal]
POST/accounts/{account_id}/access/ai-controls/mcp/portals
##### [Read details of an MCP Portal]
GET/accounts/{account_id}/access/ai-controls/mcp/portals/{id}
##### [Update a MCP Portal]
PUT/accounts/{account_id}/access/ai-controls/mcp/portals/{id}
##### [Delete a MCP Portal]
DELETE/accounts/{account_id}/access/ai-controls/mcp/portals/{id}
#### Zero TrustAccessAI ControlsMcpServers

##### [List MCP Servers]
GET/accounts/{account_id}/access/ai-controls/mcp/servers
##### [Create a new MCP Server]
POST/accounts/{account_id}/access/ai-controls/mcp/servers
##### [Read the details of a MCP Server]
GET/accounts/{account_id}/access/ai-controls/mcp/servers/{id}
##### [Update a MCP Server]
PUT/accounts/{account_id}/access/ai-controls/mcp/servers/{id}
##### [Delete a MCP Server]
DELETE/accounts/{account_id}/access/ai-controls/mcp/servers/{id}
##### [Sync MCP Server Capabilities]
POST/accounts/{account_id}/access/ai-controls/mcp/servers/{id}/sync
#### Zero TrustAccessGateway CA

##### [List SSH Certificate Authorities (CA)]
GET/accounts/{account_id}/access/gateway_ca
##### [Add a new SSH Certificate Authority (CA)]
POST/accounts/{account_id}/access/gateway_ca
##### [Delete an SSH Certificate Authority (CA)]
DELETE/accounts/{account_id}/access/gateway_ca/{certificate_id}
#### Zero TrustAccessInfrastructure

#### Zero TrustAccessInfrastructureTargets

##### [List all targets]
GET/accounts/{account_id}/infrastructure/targets
##### [Get target]
GET/accounts/{account_id}/infrastructure/targets/{target_id}
##### [Create new target]
POST/accounts/{account_id}/infrastructure/targets
##### [Update target]
PUT/accounts/{account_id}/infrastructure/targets/{target_id}
##### [Delete target]
DELETE/accounts/{account_id}/infrastructure/targets/{target_id}
##### [Create new targets]
PUT/accounts/{account_id}/infrastructure/targets/batch
##### [Delete targets (Deprecated)]
DeprecatedDELETE/accounts/{account_id}/infrastructure/targets/batch
##### [Delete targets]
POST/accounts/{account_id}/infrastructure/targets/batch_delete
#### Zero TrustAccessApplications

##### [List Access applications]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps
##### [Get an Access application]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}
##### [Add an Access application]
POST/{accounts_or_zones}/{account_or_zone_id}/access/apps
##### [Update an Access application]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}
##### [Delete an Access application]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}
##### [Revoke application tokens]
POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/revoke_tokens
#### Zero TrustAccessApplicationsCAs

##### [List short-lived certificate CAs]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/ca
##### [Get a short-lived certificate CA]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca
##### [Create a short-lived certificate CA]
POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca
##### [Delete a short-lived certificate CA]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/ca
#### Zero TrustAccessApplicationsUser Policy Checks

##### [Test Access policies]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks
#### Zero TrustAccessApplicationsPolicies

##### [List Access application policies]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies
##### [Get an Access application policy]
GET/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}
##### [Create an Access application policy]
POST/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies
##### [Update an Access application policy]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}
##### [Delete an Access application policy]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/policies/{policy_id}
#### Zero TrustAccessApplicationsPolicy Tests

##### [Get the current status of a given Access policy test]
GET/accounts/{account_id}/access/policy-tests/{policy_test_id}
##### [Start Access policy test]
POST/accounts/{account_id}/access/policy-tests
#### Zero TrustAccessApplicationsPolicy TestsUsers

##### [Get an Access policy test users page]
GET/accounts/{account_id}/access/policy-tests/{policy_test_id}/users
#### Zero TrustAccessApplicationsSettings

##### [Update Access application settings]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings
##### [Update Access application settings]
PATCH/{accounts_or_zones}/{account_or_zone_id}/access/apps/{app_id}/settings
#### Zero TrustAccessCertificates

##### [List mTLS certificates]
GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates
##### [Get an mTLS certificate]
GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}
##### [Add an mTLS certificate]
POST/{accounts_or_zones}/{account_or_zone_id}/access/certificates
##### [Update an mTLS certificate]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}
##### [Delete an mTLS certificate]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/certificates/{certificate_id}
#### Zero TrustAccessCertificatesSettings

##### [List all mTLS hostname settings]
GET/{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings
##### [Update an mTLS certificate's hostname settings]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/certificates/settings
#### Zero TrustAccessGroups

##### [List Access groups]
GET/{accounts_or_zones}/{account_or_zone_id}/access/groups
##### [Get an Access group]
GET/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}
##### [Create an Access group]
POST/{accounts_or_zones}/{account_or_zone_id}/access/groups
##### [Update an Access group]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}
##### [Delete an Access group]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/groups/{group_id}
#### Zero TrustAccessService Tokens

##### [List service tokens]
GET/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens
##### [Get a service token]
GET/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}
##### [Create a service token]
POST/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens
##### [Update a service token]
PUT/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}
##### [Delete a service token]
DELETE/{accounts_or_zones}/{account_or_zone_id}/access/service_tokens/{service_token_id}
##### [Refresh a service token]
POST/accounts/{account_id}/access/service_tokens/{service_token_id}/refresh
##### [Rotate a service token]
POST/accounts/{account_id}/access/service_tokens/{service_token_id}/rotate
#### Zero TrustAccessBookmarks

##### [List Bookmark applications]
DeprecatedGET/accounts/{account_id}/access/bookmarks
##### [Get a Bookmark application]
DeprecatedGET/accounts/{account_id}/access/bookmarks/{bookmark_id}
##### [Create a Bookmark application]
DeprecatedPOST/accounts/{account_id}/access/bookmarks/{bookmark_id}
##### [Update a Bookmark application]
DeprecatedPUT/accounts/{account_id}/access/bookmarks/{bookmark_id}
##### [Delete a Bookmark application]
DeprecatedDELETE/accounts/{account_id}/access/bookmarks/{bookmark_id}
#### Zero TrustAccessKeys

##### [Get the Access key configuration]
GET/accounts/{account_id}/access/keys
##### [Update the Access key configuration]
PUT/accounts/{account_id}/access/keys
##### [Rotate Access keys]
POST/accounts/{account_id}/access/keys/rotate
#### Zero TrustAccessLogs

#### Zero TrustAccessLogsAccess Requests

##### [Get Access authentication logs]
GET/accounts/{account_id}/access/logs/access_requests
#### Zero TrustAccessLogsSCIM

#### Zero TrustAccessLogsSCIMUpdates

##### [List Access SCIM update logs]
GET/accounts/{account_id}/access/logs/scim/updates
#### Zero TrustAccessUsers

##### [Get users]
GET/accounts/{account_id}/access/users
##### [Get a user]
GET/accounts/{account_id}/access/users/{user_id}
##### [Create a user]
POST/accounts/{account_id}/access/users
##### [Update a user]
PUT/accounts/{account_id}/access/users/{user_id}
##### [Delete a user]
DELETE/accounts/{account_id}/access/users/{user_id}
#### Zero TrustAccessUsersActive Sessions

##### [Get active sessions]
GET/accounts/{account_id}/access/users/{user_id}/active_sessions
##### [Get single active session]
GET/accounts/{account_id}/access/users/{user_id}/active_sessions/{nonce}
#### Zero TrustAccessUsersLast Seen Identity

##### [Get last seen identity]
GET/accounts/{account_id}/access/users/{user_id}/last_seen_identity
#### Zero TrustAccessUsersFailed Logins

##### [Get failed logins]
GET/accounts/{account_id}/access/users/{user_id}/failed_logins
#### Zero TrustAccessCustom Pages

##### [List custom pages]
GET/accounts/{account_id}/access/custom_pages
##### [Get a custom page]
GET/accounts/{account_id}/access/custom_pages/{custom_page_id}
##### [Create a custom page]
POST/accounts/{account_id}/access/custom_pages
##### [Update a custom page]
PUT/accounts/{account_id}/access/custom_pages/{custom_page_id}
##### [Delete a custom page]
DELETE/accounts/{account_id}/access/custom_pages/{custom_page_id}
#### Zero TrustAccessTags

##### [List tags]
GET/accounts/{account_id}/access/tags
##### [Get a tag]
GET/accounts/{account_id}/access/tags/{tag_name}
##### [Create a tag]
POST/accounts/{account_id}/access/tags
##### [Update a tag]
PUT/accounts/{account_id}/access/tags/{tag_name}
##### [Delete a tag]
DELETE/accounts/{account_id}/access/tags/{tag_name}
#### Zero TrustAccessPolicies

##### [List Access reusable policies]
GET/accounts/{account_id}/access/policies
##### [Get an Access reusable policy]
GET/accounts/{account_id}/access/policies/{policy_id}
##### [Create an Access reusable policy]
POST/accounts/{account_id}/access/policies
##### [Update an Access reusable policy]
PUT/accounts/{account_id}/access/policies/{policy_id}
##### [Delete an Access reusable policy]
DELETE/accounts/{account_id}/access/policies/{policy_id}
#### Zero TrustDEX

#### Zero TrustDEXWARP Change Events

##### [List WARP change events.]
GET/accounts/{account_id}/dex/warp-change-events
#### Zero TrustDEXCommands

##### [List account commands]
GET/accounts/{account_id}/dex/commands
##### [Create account commands]
POST/accounts/{account_id}/dex/commands
#### Zero TrustDEXCommandsDevices

##### [List devices eligible for remote captures]
GET/accounts/{account_id}/dex/commands/devices
#### Zero TrustDEXCommandsDownloads

##### [Download command output file]
GET/accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}
#### Zero TrustDEXCommandsQuota

##### [Returns account commands usage, quota, and reset time]
GET/accounts/{account_id}/dex/commands/quota
#### Zero TrustDEXColos

##### [List Cloudflare colos]
GET/accounts/{account_id}/dex/colos
#### Zero TrustDEXFleet Status

##### [List fleet status details by dimension]
GET/accounts/{account_id}/dex/fleet-status/live
##### [List fleet status aggregate details by dimension]
GET/accounts/{account_id}/dex/fleet-status/over-time
#### Zero TrustDEXFleet StatusDevices

##### [List fleet status devices]
GET/accounts/{account_id}/dex/fleet-status/devices
#### Zero TrustDEXHTTP Tests

##### [Get details and aggregate metrics for an http test]
GET/accounts/{account_id}/dex/http-tests/{test_id}
#### Zero TrustDEXHTTP TestsPercentiles

##### [Get percentiles for an http test]
GET/accounts/{account_id}/dex/http-tests/{test_id}/percentiles
#### Zero TrustDEXTests

##### [List DEX test analytics]
GET/accounts/{account_id}/dex/tests/overview
#### Zero TrustDEXTestsUnique Devices

##### [Get count of devices targeted]
GET/accounts/{account_id}/dex/tests/unique-devices
#### Zero TrustDEXTraceroute Test Results

#### Zero TrustDEXTraceroute Test ResultsNetwork Path

##### [Get details for a specific traceroute test run]
GET/accounts/{account_id}/dex/traceroute-test-results/{test_result_id}/network-path
#### Zero TrustDEXTraceroute Tests

##### [Get details and aggregate metrics for a traceroute test]
GET/accounts/{account_id}/dex/traceroute-tests/{test_id}
##### [Get percentiles for a traceroute test]
GET/accounts/{account_id}/dex/traceroute-tests/{test_id}/percentiles
##### [Get network path breakdown for a traceroute test]
GET/accounts/{account_id}/dex/traceroute-tests/{test_id}/network-path
#### Zero TrustDEXRules

##### [Get DEX Rule]
GET/accounts/{account_id}/dex/rules/{rule_id}
##### [Delete a DEX Rule]
DELETE/accounts/{account_id}/dex/rules/{rule_id}
##### [Update a DEX Rule]
PATCH/accounts/{account_id}/dex/rules/{rule_id}
##### [Create a DEX Rule]
POST/accounts/{account_id}/dex/rules
##### [List DEX Rules]
GET/accounts/{account_id}/dex/rules
#### Zero TrustTunnels

##### [List All Tunnels]
GET/accounts/{account_id}/tunnels
#### Zero TrustTunnelsCloudflared

##### [List Cloudflare Tunnels]
GET/accounts/{account_id}/cfd_tunnel
##### [Get a Cloudflare Tunnel]
GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}
##### [Create a Cloudflare Tunnel]
POST/accounts/{account_id}/cfd_tunnel
##### [Update a Cloudflare Tunnel]
PATCH/accounts/{account_id}/cfd_tunnel/{tunnel_id}
##### [Delete a Cloudflare Tunnel]
DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}
#### Zero TrustTunnelsCloudflaredConfigurations

##### [Get configuration]
GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations
##### [Put configuration]
PUT/accounts/{account_id}/cfd_tunnel/{tunnel_id}/configurations
#### Zero TrustTunnelsCloudflaredConnections

##### [List Cloudflare Tunnel connections]
GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections
##### [Clean up Cloudflare Tunnel connections]
DELETE/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections
#### Zero TrustTunnelsCloudflaredToken

##### [Get a Cloudflare Tunnel token]
GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/token
#### Zero TrustTunnelsCloudflaredConnectors

##### [Get Cloudflare Tunnel connector]
GET/accounts/{account_id}/cfd_tunnel/{tunnel_id}/connectors/{connector_id}
#### Zero TrustTunnelsCloudflaredManagement

##### [Get a Cloudflare Tunnel management token]
POST/accounts/{account_id}/cfd_tunnel/{tunnel_id}/management
#### Zero TrustTunnelsWARP Connector

##### [List Warp Connector Tunnels]
GET/accounts/{account_id}/warp_connector
##### [Get a Warp Connector Tunnel]
GET/accounts/{account_id}/warp_connector/{tunnel_id}
##### [Create a Warp Connector Tunnel]
POST/accounts/{account_id}/warp_connector
##### [Update a Warp Connector Tunnel]
PATCH/accounts/{account_id}/warp_connector/{tunnel_id}
##### [Delete a Warp Connector Tunnel]
DELETE/accounts/{account_id}/warp_connector/{tunnel_id}
#### Zero TrustTunnelsWARP ConnectorToken

##### [Get a Warp Connector Tunnel token]
GET/accounts/{account_id}/warp_connector/{tunnel_id}/token
#### Zero TrustTunnelsWARP ConnectorConnections

##### [List WARP Connector Tunnel connections]
GET/accounts/{account_id}/warp_connector/{tunnel_id}/connections
#### Zero TrustTunnelsWARP ConnectorConnectors

##### [Get WARP Connector Tunnel connector]
GET/accounts/{account_id}/warp_connector/{tunnel_id}/connectors/{connector_id}
#### Zero TrustTunnelsWARP ConnectorFailover

##### [Trigger a manual failover for a WARP Connector Tunnel]
PUT/accounts/{account_id}/warp_connector/{tunnel_id}/failover
#### Zero TrustConnectivity Settings

##### [Get Zero Trust Connectivity Settings]
GET/accounts/{account_id}/zerotrust/connectivity_settings
##### [Updates the Zero Trust Connectivity Settings]
PATCH/accounts/{account_id}/zerotrust/connectivity_settings
#### Zero TrustDLP

#### Zero TrustDLPDatasets

##### [Fetch all datasets]
GET/accounts/{account_id}/dlp/datasets
##### [Fetch a specific dataset]
GET/accounts/{account_id}/dlp/datasets/{dataset_id}
##### [Create a new dataset]
POST/accounts/{account_id}/dlp/datasets
##### [Update details about a dataset]
PUT/accounts/{account_id}/dlp/datasets/{dataset_id}
##### [Delete a dataset]
DELETE/accounts/{account_id}/dlp/datasets/{dataset_id}
#### Zero TrustDLPDatasetsUpload

##### [Prepare to upload a new version of a dataset]
POST/accounts/{account_id}/dlp/datasets/{dataset_id}/upload
##### [Upload a new version of a dataset]
POST/accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}
#### Zero TrustDLPDatasetsVersions

##### [Sets the column information for a multi-column upload]
POST/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}
#### Zero TrustDLPDatasetsVersionsEntries

##### [Upload a new version of a multi-column dataset]
POST/accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}/entries/{entry_id}
#### Zero TrustDLPPatterns

##### [Validate a DLP regex pattern]
POST/accounts/{account_id}/dlp/patterns/validate
#### Zero TrustDLPPayload Logs

##### [Get payload log settings]
GET/accounts/{account_id}/dlp/payload_log
##### [Set payload log settings]
PUT/accounts/{account_id}/dlp/payload_log
#### Zero TrustDLPEmail

#### Zero TrustDLPEmailAccount Mapping

##### [Get mapping]
GET/accounts/{account_id}/dlp/email/account_mapping
##### [Create mapping]
POST/accounts/{account_id}/dlp/email/account_mapping
#### Zero TrustDLPEmailRules

##### [List all email scanner rules]
GET/accounts/{account_id}/dlp/email/rules
##### [Get an email scanner rule]
GET/accounts/{account_id}/dlp/email/rules/{rule_id}
##### [Create email scanner rule]
POST/accounts/{account_id}/dlp/email/rules
##### [Update email scanner rule]
PUT/accounts/{account_id}/dlp/email/rules/{rule_id}
##### [Delete email scanner rule]
DELETE/accounts/{account_id}/dlp/email/rules/{rule_id}
##### [Update email scanner rule priorities]
PATCH/accounts/{account_id}/dlp/email/rules
#### Zero TrustDLPProfiles

##### [List all profiles]
GET/accounts/{account_id}/dlp/profiles
##### [Get DLP Profile]
GET/accounts/{account_id}/dlp/profiles/{profile_id}
#### Zero TrustDLPProfilesCustom

##### [Get custom profile]
GET/accounts/{account_id}/dlp/profiles/custom/{profile_id}
##### [Create custom profile]
POST/accounts/{account_id}/dlp/profiles/custom
##### [Update custom profile]
PUT/accounts/{account_id}/dlp/profiles/custom/{profile_id}
##### [Delete custom profile]
DELETE/accounts/{account_id}/dlp/profiles/custom/{profile_id}
#### Zero TrustDLPProfilesPredefined

##### [Get predefined profile config]
GET/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config
##### [Update predefined profile config]
PUT/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config
##### [Delete predefined profile]
DELETE/accounts/{account_id}/dlp/profiles/predefined/{profile_id}
#### Zero TrustDLPLimits

##### [Fetch limits associated with DLP for account]
GET/accounts/{account_id}/dlp/limits
#### Zero TrustDLPEntries

##### [List all entries]
GET/accounts/{account_id}/dlp/entries
##### [Get DLP Entry]
GET/accounts/{account_id}/dlp/entries/{entry_id}
##### [Create custom entry]
POST/accounts/{account_id}/dlp/entries
##### [Update entry]
PUT/accounts/{account_id}/dlp/entries/{entry_id}
##### [Delete custom entry]
DELETE/accounts/{account_id}/dlp/entries/{entry_id}
#### Zero TrustDLPEntriesCustom

##### [Create custom entry]
POST/accounts/{account_id}/dlp/entries
##### [Update custom entry]
PUT/accounts/{account_id}/dlp/entries/custom/{entry_id}
##### [Delete custom entry]
DELETE/accounts/{account_id}/dlp/entries/{entry_id}
##### [Get DLP Entry]
GET/accounts/{account_id}/dlp/entries/{entry_id}
##### [List all entries]
GET/accounts/{account_id}/dlp/entries
#### Zero TrustDLPEntriesPredefined

##### [Create predefined entry]
POST/accounts/{account_id}/dlp/entries/predefined
##### [Update predefined entry]
PUT/accounts/{account_id}/dlp/entries/predefined/{entry_id}
##### [Delete predefined entry]
DELETE/accounts/{account_id}/dlp/entries/predefined/{entry_id}
##### [Get DLP Entry]
GET/accounts/{account_id}/dlp/entries/{entry_id}
##### [List all entries]
GET/accounts/{account_id}/dlp/entries
#### Zero TrustDLPEntriesIntegration

##### [Create integration entry]
POST/accounts/{account_id}/dlp/entries/integration
##### [Update integration entry]
PUT/accounts/{account_id}/dlp/entries/integration/{entry_id}
##### [Delete integration entry]
DELETE/accounts/{account_id}/dlp/entries/integration/{entry_id}
##### [Get DLP Entry]
GET/accounts/{account_id}/dlp/entries/{entry_id}
##### [List all entries]
GET/accounts/{account_id}/dlp/entries
#### Zero TrustGateway

##### [Get Zero Trust account information]
GET/accounts/{account_id}/gateway
##### [Create Zero Trust account]
POST/accounts/{account_id}/gateway
#### Zero TrustGatewayAudit SSH Settings

##### [Get Zero Trust SSH settings]
GET/accounts/{account_id}/gateway/audit_ssh_settings
##### [Update Zero Trust SSH settings]
PUT/accounts/{account_id}/gateway/audit_ssh_settings
##### [Rotate Zero Trust SSH account seed]
POST/accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed
#### Zero TrustGatewayCategories

##### [List categories]
GET/accounts/{account_id}/gateway/categories
#### Zero TrustGatewayApp Types

##### [List application and application type mappings]
GET/accounts/{account_id}/gateway/app_types
#### Zero TrustGatewayConfigurations

##### [Get Zero Trust account configuration]
GET/accounts/{account_id}/gateway/configuration
##### [Update Zero Trust account configuration]
PUT/accounts/{account_id}/gateway/configuration
##### [Patch Zero Trust account configuration]
PATCH/accounts/{account_id}/gateway/configuration
#### Zero TrustGatewayConfigurationsCustom Certificate

##### [Get Zero Trust certificate configuration]
DeprecatedGET/accounts/{account_id}/gateway/configuration/custom_certificate
#### Zero TrustGatewayLists

##### [List Zero Trust lists]
GET/accounts/{account_id}/gateway/lists
##### [Get Zero Trust list details]
GET/accounts/{account_id}/gateway/lists/{list_id}
##### [Create Zero Trust list]
POST/accounts/{account_id}/gateway/lists
##### [Update Zero Trust list]
PUT/accounts/{account_id}/gateway/lists/{list_id}
##### [Patch Zero Trust list.]
PATCH/accounts/{account_id}/gateway/lists/{list_id}
##### [Delete Zero Trust list]
DELETE/accounts/{account_id}/gateway/lists/{list_id}
#### Zero TrustGatewayListsItems

##### [Get Zero Trust list items]
GET/accounts/{account_id}/gateway/lists/{list_id}/items
#### Zero TrustGatewayLocations

##### [List Zero Trust Gateway locations]
GET/accounts/{account_id}/gateway/locations
##### [Get Zero Trust Gateway location details]
GET/accounts/{account_id}/gateway/locations/{location_id}
##### [Create a Zero Trust Gateway location]
POST/accounts/{account_id}/gateway/locations
##### [Update a Zero Trust Gateway location]
PUT/accounts/{account_id}/gateway/locations/{location_id}
##### [Delete a Zero Trust Gateway location]
DELETE/accounts/{account_id}/gateway/locations/{location_id}
#### Zero TrustGatewayLogging

##### [Get logging settings for the Zero Trust account]
GET/accounts/{account_id}/gateway/logging
##### [Update Zero Trust account logging settings]
PUT/accounts/{account_id}/gateway/logging
#### Zero TrustGatewayProxy Endpoints

##### [List proxy endpoints]
GET/accounts/{account_id}/gateway/proxy_endpoints
##### [Get a proxy endpoint]
GET/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}
##### [Create a proxy endpoint]
POST/accounts/{account_id}/gateway/proxy_endpoints
##### [Update a proxy endpoint]
PATCH/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}
##### [Delete a proxy endpoint]
DELETE/accounts/{account_id}/gateway/proxy_endpoints/{proxy_endpoint_id}
#### Zero TrustGatewayRules

##### [List Zero Trust Gateway rules]
GET/accounts/{account_id}/gateway/rules
##### [Get Zero Trust Gateway rule details.]
GET/accounts/{account_id}/gateway/rules/{rule_id}
##### [Create a Zero Trust Gateway rule]
POST/accounts/{account_id}/gateway/rules
##### [Update a Zero Trust Gateway rule]
PUT/accounts/{account_id}/gateway/rules/{rule_id}
##### [Delete a Zero Trust Gateway rule]
DELETE/accounts/{account_id}/gateway/rules/{rule_id}
##### [List Zero Trust Gateway rules inherited from the parent account]
GET/accounts/{account_id}/gateway/rules/tenant
##### [Reset the expiration of a Zero Trust Gateway Rule]
POST/accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration
#### Zero TrustGatewayCertificates

##### [List Zero Trust certificates]
GET/accounts/{account_id}/gateway/certificates
##### [Get Zero Trust certificate details]
GET/accounts/{account_id}/gateway/certificates/{certificate_id}
##### [Create Zero Trust certificate]
POST/accounts/{account_id}/gateway/certificates
##### [Delete Zero Trust certificate]
DELETE/accounts/{account_id}/gateway/certificates/{certificate_id}
##### [Activate a Zero Trust certificate]
POST/accounts/{account_id}/gateway/certificates/{certificate_id}/activate
##### [Deactivate a Zero Trust certificate]
POST/accounts/{account_id}/gateway/certificates/{certificate_id}/deactivate
#### Zero TrustGatewayPacfiles

##### [List PAC files]
GET/accounts/{account_id}/gateway/pacfiles
##### [Get a PAC file]
GET/accounts/{account_id}/gateway/pacfiles/{pacfile_id}
##### [Create a PAC file]
POST/accounts/{account_id}/gateway/pacfiles
##### [Update a Zero Trust Gateway PAC file]
PUT/accounts/{account_id}/gateway/pacfiles/{pacfile_id}
##### [Delete a PAC file]
DELETE/accounts/{account_id}/gateway/pacfiles/{pacfile_id}
#### Zero TrustNetworks

#### Zero TrustNetworksRoutes

##### [List tunnel routes]
GET/accounts/{account_id}/teamnet/routes
##### [Get tunnel route]
GET/accounts/{account_id}/teamnet/routes/{route_id}
##### [Create a tunnel route]
POST/accounts/{account_id}/teamnet/routes
##### [Update a tunnel route]
PATCH/accounts/{account_id}/teamnet/routes/{route_id}
##### [Delete a tunnel route]
DELETE/accounts/{account_id}/teamnet/routes/{route_id}
#### Zero TrustNetworksRoutesIPs

##### [Get tunnel route by IP]
GET/accounts/{account_id}/teamnet/routes/ip/{ip}
#### Zero TrustNetworksRoutesNetworks

##### [Create a tunnel route (CIDR Endpoint)]
DeprecatedPOST/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}
##### [Update a tunnel route (CIDR Endpoint)]
DeprecatedPATCH/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}
##### [Delete a tunnel route (CIDR Endpoint)]
DeprecatedDELETE/accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}
#### Zero TrustNetworksVirtual Networks

##### [List virtual networks]
GET/accounts/{account_id}/teamnet/virtual_networks
##### [Get a virtual network]
GET/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}
##### [Create a virtual network]
POST/accounts/{account_id}/teamnet/virtual_networks
##### [Update a virtual network]
PATCH/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}
##### [Delete a virtual network]
DELETE/accounts/{account_id}/teamnet/virtual_networks/{virtual_network_id}
#### Zero TrustNetworksSubnets

##### [List Subnets]
GET/accounts/{account_id}/zerotrust/subnets
#### Zero TrustNetworksSubnetsWARP

##### [Create WARP IP subnet]
POST/accounts/{account_id}/zerotrust/subnets/warp
##### [Get WARP IP subnet]
GET/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}
##### [Update WARP IP subnet]
PATCH/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}
##### [Delete WARP IP subnet]
DELETE/accounts/{account_id}/zerotrust/subnets/warp/{subnet_id}
#### Zero TrustNetworksSubnetsCloudflare Source

##### [Update Cloudflare Source Subnet]
PATCH/accounts/{account_id}/zerotrust/subnets/cloudflare_source/{address_family}
#### Zero TrustNetworksHostname Routes

##### [List hostname routes]
GET/accounts/{account_id}/zerotrust/routes/hostname
##### [Get hostname route]
GET/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}
##### [Create hostname route]
POST/accounts/{account_id}/zerotrust/routes/hostname
##### [Update hostname route]
PATCH/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}
##### [Delete hostname route]
DELETE/accounts/{account_id}/zerotrust/routes/hostname/{hostname_route_id}
#### Zero TrustRisk Scoring

##### [Get risk event/score information for a specific user]
GET/accounts/{account_id}/zt_risk_scoring/{user_id}
##### [Clear the risk score for a particular user]
POST/accounts/{account_id}/zt_risk_scoring/{user_id}/reset
#### Zero TrustRisk ScoringBehaviours

##### [Get all behaviors and associated configuration]
GET/accounts/{account_id}/zt_risk_scoring/behaviors
##### [Update configuration for risk behaviors]
PUT/accounts/{account_id}/zt_risk_scoring/behaviors
#### Zero TrustRisk ScoringSummary

##### [Get risk score info for all users in the account]
GET/accounts/{account_id}/zt_risk_scoring/summary
#### Zero TrustRisk ScoringIntegrations

##### [List all risk score integrations for the account.]
GET/accounts/{account_id}/zt_risk_scoring/integrations
##### [Get risk score integration by id.]
GET/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}
##### [Create new risk score integration.]
POST/accounts/{account_id}/zt_risk_scoring/integrations
##### [Update a risk score integration.]
PUT/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}
##### [Delete a risk score integration.]
DELETE/accounts/{account_id}/zt_risk_scoring/integrations/{integration_id}
#### Zero TrustRisk ScoringIntegrationsReferences

##### [Get risk score integration by reference id.]
GET/accounts/{account_id}/zt_risk_scoring/integrations/reference_id/{reference_id}
#### Turnstile

#### TurnstileWidgets

##### [List Turnstile Widgets]
GET/accounts/{account_id}/challenges/widgets
##### [Turnstile Widget Details]
GET/accounts/{account_id}/challenges/widgets/{sitekey}
##### [Create a Turnstile Widget]
POST/accounts/{account_id}/challenges/widgets
##### [Update a Turnstile Widget]
PUT/accounts/{account_id}/challenges/widgets/{sitekey}
##### [Delete a Turnstile Widget]
DELETE/accounts/{account_id}/challenges/widgets/{sitekey}
##### [Rotate Secret for a Turnstile Widget]
POST/accounts/{account_id}/challenges/widgets/{sitekey}/rotate_secret
#### Connectivity

#### ConnectivityDirectory

#### ConnectivityDirectoryServices

##### [List Workers VPC connectivity services]
GET/accounts/{account_id}/connectivity/directory/services
##### [Create Workers VPC connectivity service]
POST/accounts/{account_id}/connectivity/directory/services
##### [Get Workers VPC connectivity service]
GET/accounts/{account_id}/connectivity/directory/services/{service_id}
##### [Update Workers VPC connectivity service]
PUT/accounts/{account_id}/connectivity/directory/services/{service_id}
##### [Delete Workers VPC connectivity service]
DELETE/accounts/{account_id}/connectivity/directory/services/{service_id}
#### Hyperdrive

#### HyperdriveConfigs

##### [List Hyperdrives]
GET/accounts/{account_id}/hyperdrive/configs
##### [Get Hyperdrive]
GET/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}
##### [Create Hyperdrive]
POST/accounts/{account_id}/hyperdrive/configs
##### [Update Hyperdrive]
PUT/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}
##### [Patch Hyperdrive]
PATCH/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}
##### [Delete Hyperdrive]
DELETE/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}
#### RUM

#### RUMSite Info

##### [List Web Analytics sites]
GET/accounts/{account_id}/rum/site_info/list
##### [Get a Web Analytics site]
GET/accounts/{account_id}/rum/site_info/{site_id}
##### [Create a Web Analytics site]
POST/accounts/{account_id}/rum/site_info
##### [Update a Web Analytics site]
PUT/accounts/{account_id}/rum/site_info/{site_id}
##### [Delete a Web Analytics site]
DELETE/accounts/{account_id}/rum/site_info/{site_id}
#### RUMRules

##### [List rules in Web Analytics ruleset]
GET/accounts/{account_id}/rum/v2/{ruleset_id}/rules
##### [Create a Web Analytics rule]
POST/accounts/{account_id}/rum/v2/{ruleset_id}/rule
##### [Update a Web Analytics rule]
PUT/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}
##### [Delete a Web Analytics rule]
DELETE/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}
##### [Update Web Analytics rules]
POST/accounts/{account_id}/rum/v2/{ruleset_id}/rules
#### Vectorize

#### VectorizeIndexes

##### [List Vectorize Indexes]
GET/accounts/{account_id}/vectorize/v2/indexes
##### [Get Vectorize Index]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}
##### [Create Vectorize Index]
POST/accounts/{account_id}/vectorize/v2/indexes
##### [Delete Vectorize Index]
DELETE/accounts/{account_id}/vectorize/v2/indexes/{index_name}
##### [Insert Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/insert
##### [Query Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/query
##### [Upsert Vectors]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/upsert
##### [Delete Vectors By Identifier]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/delete_by_ids
##### [Get Vectors By Identifier]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/get_by_ids
##### [Get Vectorize Index Info]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/info
##### [List Vectors]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/list
#### VectorizeIndexesMetadata Index

##### [List Metadata Indexes]
GET/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/list
##### [Create Metadata Index]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/create
##### [Delete Metadata Index]
POST/accounts/{account_id}/vectorize/v2/indexes/{index_name}/metadata_index/delete
#### URL Scanner

#### URL ScannerResponses

##### [Get raw response]
GET/accounts/{account_id}/urlscanner/v2/responses/{response_id}
#### URL ScannerScans

##### [Search URL scans]
GET/accounts/{account_id}/urlscanner/v2/search
##### [Get URL scan]
GET/accounts/{account_id}/urlscanner/v2/result/{scan_id}
##### [Create URL Scan]
POST/accounts/{account_id}/urlscanner/v2/scan
##### [Bulk create URL Scans]
POST/accounts/{account_id}/urlscanner/v2/bulk
##### [Get URL scan's HAR]
GET/accounts/{account_id}/urlscanner/v2/har/{scan_id}
##### [Get screenshot]
GET/accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png
##### [Get URL scan's DOM]
GET/accounts/{account_id}/urlscanner/v2/dom/{scan_id}
#### Radar

#### RadarAI

#### RadarAITo Markdown

##### [Convert Files into Markdown]
DeprecatedPOST/accounts/{account_id}/ai/tomarkdown
#### RadarAIInference

##### [Get Workers AI inference distribution by dimension]
GET/radar/ai/inference/summary/{dimension}
##### [Get time series distribution of Workers AI inference by dimension.]
GET/radar/ai/inference/timeseries_groups/{dimension}
#### RadarAIInferenceSummary

##### [Get Workers AI models summary]
DeprecatedGET/radar/ai/inference/summary/model
##### [Get Workers AI tasks summary]
DeprecatedGET/radar/ai/inference/summary/task
#### RadarAIInferenceTimeseries Groups

#### RadarAIInferenceTimeseries GroupsSummary

##### [Get Workers AI models time series]
DeprecatedGET/radar/ai/inference/timeseries_groups/model
##### [Get Workers AI tasks time series]
DeprecatedGET/radar/ai/inference/timeseries_groups/task
#### RadarAIBots

##### [Get AI bots HTTP requests distribution by dimension]
GET/radar/ai/bots/summary/{dimension}
##### [Get AI bots HTTP requests time series]
GET/radar/ai/bots/timeseries
##### [Get time series distribution of AI bots HTTP requests by dimension.]
GET/radar/ai/bots/timeseries_groups/{dimension}
#### RadarAIBotsSummary

##### [Get AI user agents summary]
DeprecatedGET/radar/ai/bots/summary/user_agent
#### RadarAITimeseries Groups

##### [Get AI user agents time series]
DeprecatedGET/radar/ai/bots/timeseries_groups/user_agent
##### [Get AI bots HTTP requests distribution by dimension]
DeprecatedGET/radar/ai/bots/summary/{dimension}
##### [Get AI bots HTTP requests time series]
DeprecatedGET/radar/ai/bots/timeseries
##### [Get time series distribution of AI bots HTTP requests by dimension.]
DeprecatedGET/radar/ai/bots/timeseries_groups/{dimension}
#### RadarCT

##### [Get certificate distribution by dimension]
GET/radar/ct/summary/{dimension}
##### [Get certificates time series]
GET/radar/ct/timeseries
##### [Get time series of certificate distribution by dimension]
GET/radar/ct/timeseries_groups/{dimension}
#### RadarCTAuthorities

##### [Get certificate authority details]
GET/radar/ct/authorities/{ca_slug}
##### [List certificate authorities]
GET/radar/ct/authorities
#### RadarCTLogs

##### [Get certificate log details]
GET/radar/ct/logs/{log_slug}
##### [List certificate logs]
GET/radar/ct/logs
#### RadarAnnotations

##### [Get latest annotations]
GET/radar/annotations
#### RadarAnnotationsOutages

##### [Get latest Internet outages and anomalies]
GET/radar/annotations/outages
##### [Get the number of outages by location]
GET/radar/annotations/outages/locations
#### RadarBGP

##### [Get BGP time series]
GET/radar/bgp/timeseries
#### RadarBGPLeaks

#### RadarBGPLeaksEvents

##### [Get BGP route leak events]
GET/radar/bgp/leaks/events
#### RadarBGPTop

##### [Get top prefixes by BGP updates]
GET/radar/bgp/top/prefixes
#### RadarBGPTopAses

##### [Get top ASes by BGP updates]
GET/radar/bgp/top/ases
##### [Get top ASes by prefix count]
GET/radar/bgp/top/ases/prefixes
#### RadarBGPHijacks

#### RadarBGPHijacksEvents

##### [Get BGP hijack events]
GET/radar/bgp/hijacks/events
#### RadarBGPRoutes

##### [Get Multi-Origin AS (MOAS) prefixes]
GET/radar/bgp/routes/moas
##### [Get prefix-to-ASN mapping]
GET/radar/bgp/routes/pfx2as
##### [Get BGP routing table stats ]
GET/radar/bgp/routes/stats
##### [List ASes from global routing tables]
GET/radar/bgp/routes/ases
##### [Get real-time BGP routes for a prefix]
GET/radar/bgp/routes/realtime
#### RadarBGPIPs

##### [Get announced IP address space time series]
GET/radar/bgp/ips/timeseries
#### RadarBGPRPKI

#### RadarBGPRPKIASPA

##### [Get ASPA objects snapshot]
GET/radar/bgp/rpki/aspa/snapshot
##### [Get ASPA changes over time]
GET/radar/bgp/rpki/aspa/changes
##### [Get ASPA count time series]
GET/radar/bgp/rpki/aspa/timeseries
#### RadarBots

##### [List bots]
GET/radar/bots
##### [Get bot details]
GET/radar/bots/{bot_slug}
##### [Get bots HTTP requests distribution by dimension]
GET/radar/bots/summary/{dimension}
##### [Get bots HTTP requests time series]
GET/radar/bots/timeseries
##### [Get time series distribution of bots HTTP requests by dimension.]
GET/radar/bots/timeseries_groups/{dimension}
#### RadarBotsWeb Crawlers

##### [Get crawler HTTP request distribution by dimension]
GET/radar/bots/crawlers/summary/{dimension}
##### [Get time series of crawler HTTP request distribution by dimension]
GET/radar/bots/crawlers/timeseries_groups/{dimension}
#### RadarDatasets

##### [List datasets]
GET/radar/datasets
##### [Get dataset CSV stream]
GET/radar/datasets/{alias}
##### [Get dataset download URL]
POST/radar/datasets/download
#### RadarDNS

##### [Get DNS summary by dimension]
GET/radar/dns/summary/{dimension}
##### [Get DNS queries time series]
GET/radar/dns/timeseries
##### [Get DNS time series grouped by dimension]
GET/radar/dns/timeseries_groups/{dimension}
#### RadarDNSTop

##### [Get top ASes by DNS queries]
GET/radar/dns/top/ases
##### [Get top locations by DNS queries]
GET/radar/dns/top/locations
#### RadarDNSSummary

##### [Get DNS queries by cache status summary]
DeprecatedGET/radar/dns/summary/cache_hit
##### [Get DNS queries by DNSSEC support summary]
DeprecatedGET/radar/dns/summary/dnssec
##### [Get DNS queries by DNSSEC awareness summary]
DeprecatedGET/radar/dns/summary/dnssec_aware
##### [Get DNS queries by DNSSEC end-to-end summary]
DeprecatedGET/radar/dns/summary/dnssec_e2e
##### [Get DNS queries by IP version summary]
DeprecatedGET/radar/dns/summary/ip_version
##### [Get DNS queries by matching answer summary]
DeprecatedGET/radar/dns/summary/matching_answer
##### [Get DNS queries by protocol summary]
DeprecatedGET/radar/dns/summary/protocol
##### [Get DNS queries by type summary]
DeprecatedGET/radar/dns/summary/query_type
##### [Get DNS queries by response code summary]
DeprecatedGET/radar/dns/summary/response_code
##### [Get DNS queries by response TTL summary]
DeprecatedGET/radar/dns/summary/response_ttl
#### RadarDNSTimeseries Groups

##### [Get DNS queries by cache status time series]
DeprecatedGET/radar/dns/timeseries_groups/cache_hit
##### [Get DNS queries by DNSSEC support time series]
DeprecatedGET/radar/dns/timeseries_groups/dnssec
##### [Get DNS queries by DNSSEC awareness time series]
DeprecatedGET/radar/dns/timeseries_groups/dnssec_aware
##### [Get DNS queries by DNSSEC end-to-end time series]
DeprecatedGET/radar/dns/timeseries_groups/dnssec_e2e
##### [Get DNS queries by IP version time series]
DeprecatedGET/radar/dns/timeseries_groups/ip_version
##### [Get DNS queries by matching answer time series]
DeprecatedGET/radar/dns/timeseries_groups/matching_answer
##### [Get DNS queries by protocol time series]
DeprecatedGET/radar/dns/timeseries_groups/protocol
##### [Get DNS queries by type time series]
DeprecatedGET/radar/dns/timeseries_groups/query_type
##### [Get DNS queries by response code time series]
DeprecatedGET/radar/dns/timeseries_groups/response_code
##### [Get DNS queries by response TTL time series]
DeprecatedGET/radar/dns/timeseries_groups/response_ttl
#### RadarNetFlows

##### [Get network traffic time series]
GET/radar/netflows/timeseries
##### [Get network traffic summary]
DeprecatedGET/radar/netflows/summary
##### [Get network traffic distribution by dimension]
GET/radar/netflows/summary/{dimension}
##### [Get time series distribution of network traffic by dimension]
GET/radar/netflows/timeseries_groups/{dimension}
#### RadarNetFlowsTop

##### [Get top ASes by network traffic]
GET/radar/netflows/top/ases
##### [Get top locations by network traffic]
GET/radar/netflows/top/locations
#### RadarPost Quantum

#### RadarPost QuantumOrigin

##### [Get Origin Post-Quantum Data Summary]
GET/radar/post_quantum/origin/summary/{dimension}
##### [Get Origin Post-Quantum Data Over Time]
GET/radar/post_quantum/origin/timeseries_groups/{dimension}
#### RadarPost QuantumTLS

##### [Check Post-Quantum TLS support]
GET/radar/post_quantum/tls/support
#### RadarSearch

##### [Search for locations, ASes, reports, and more]
GET/radar/search/global
#### RadarVerified Bots

#### RadarVerified BotsTop

##### [Get top verified bots by HTTP requests]
DeprecatedGET/radar/verified_bots/top/bots
##### [Get top verified bot categories by HTTP requests]
DeprecatedGET/radar/verified_bots/top/categories
#### RadarAS112

##### [Get AS112 DNS queries time series]
GET/radar/as112/timeseries
##### [Get AS112 summary by dimension]
GET/radar/as112/summary/{dimension}
##### [Get AS112 time series grouped by dimension]
GET/radar/as112/timeseries_groups/{dimension}
#### RadarAS112Summary

##### [Get AS112 DNS queries by DNSSEC summary]
DeprecatedGET/radar/as112/summary/dnssec
##### [Get AS112 DNS queries by EDNS summary]
DeprecatedGET/radar/as112/summary/edns
##### [Get AS112 DNS queries by IP version summary]
DeprecatedGET/radar/as112/summary/ip_version
##### [Get AS112 DNS queries by DNS protocol summary]
DeprecatedGET/radar/as112/summary/protocol
##### [Get AS112 DNS queries by type summary]
DeprecatedGET/radar/as112/summary/query_type
##### [Get AS112 DNS queries by response code summary]
DeprecatedGET/radar/as112/summary/response_codes
#### RadarAS112Timeseries Groups

##### [Get AS112 DNS queries by DNS protocol time series]
DeprecatedGET/radar/as112/timeseries_groups/protocol
##### [Get AS112 DNS queries by type time series]
DeprecatedGET/radar/as112/timeseries_groups/query_type
##### [Get AS112 DNS queries by response code time series]
DeprecatedGET/radar/as112/timeseries_groups/response_codes
##### [Get AS112 DNS queries by DNSSEC support time series]
DeprecatedGET/radar/as112/timeseries_groups/dnssec
##### [Get AS112 DNS queries by EDNS support summary]
DeprecatedGET/radar/as112/timeseries_groups/edns
##### [Get AS112 DNS queries by IP version time series]
DeprecatedGET/radar/as112/timeseries_groups/ip_version
#### RadarAS112Top

##### [Get top locations by AS112 DNS queries]
GET/radar/as112/top/locations
##### [Get top locations by AS112 DNS queries with DNSSEC support]
GET/radar/as112/top/locations/dnssec/{dnssec}
##### [Get top locations by AS112 DNS queries with EDNS support]
GET/radar/as112/top/locations/edns/{edns}
##### [Get top locations by AS112 DNS queries for an IP version]
GET/radar/as112/top/locations/ip_version/{ip_version}
#### RadarEmail

#### RadarEmailRouting

##### [Get email routing summary by dimension]
GET/radar/email/routing/summary/{dimension}
##### [Get email routing time series grouped by dimension]
GET/radar/email/routing/timeseries_groups/{dimension}
#### RadarEmailRoutingSummary

##### [Get email ARC validation summary]
DeprecatedGET/radar/email/routing/summary/arc
##### [Get email DKIM validation summary]
DeprecatedGET/radar/email/routing/summary/dkim
##### [Get email DMARC validation summary]
DeprecatedGET/radar/email/routing/summary/dmarc
##### [Get email encryption status summary]
DeprecatedGET/radar/email/routing/summary/encrypted
##### [Get email IP version summary]
DeprecatedGET/radar/email/routing/summary/ip_version
##### [Get email SPF validation summary]
DeprecatedGET/radar/email/routing/summary/spf
#### RadarEmailRoutingTimeseries Groups

##### [Get email ARC validation time series]
DeprecatedGET/radar/email/routing/timeseries_groups/arc
##### [Get email DKIM validation time series]
DeprecatedGET/radar/email/routing/timeseries_groups/dkim
##### [Get email DMARC validation time series]
DeprecatedGET/radar/email/routing/timeseries_groups/dmarc
##### [Get email encryption status time series]
DeprecatedGET/radar/email/routing/timeseries_groups/encrypted
##### [Get email IP version time series]
DeprecatedGET/radar/email/routing/timeseries_groups/ip_version
##### [Get email SPF validation time series]
DeprecatedGET/radar/email/routing/timeseries_groups/spf
#### RadarEmailSecurity

##### [Get email security summary by dimension]
GET/radar/email/security/summary/{dimension}
##### [Get email security time series grouped by dimension]
GET/radar/email/security/timeseries_groups/{dimension}
#### RadarEmailSecurityTop

#### RadarEmailSecurityTopTLDs

##### [Get top TLDs by email message volume]
GET/radar/email/security/top/tlds
#### RadarEmailSecurityTopTLDsMalicious

##### [Get top TLDs by email malicious classification]
GET/radar/email/security/top/tlds/malicious/{malicious}
#### RadarEmailSecurityTopTLDsSpam

##### [Get top TLDs by email spam classification]
GET/radar/email/security/top/tlds/spam/{spam}
#### RadarEmailSecurityTopTLDsSpoof

##### [Get top TLDs by email spoof classification]
GET/radar/email/security/top/tlds/spoof/{spoof}
#### RadarEmailSecuritySummary

##### [Get email ARC validation summary]
DeprecatedGET/radar/email/security/summary/arc
##### [Get email DKIM validation summary]
DeprecatedGET/radar/email/security/summary/dkim
##### [Get email DMARC validation summary]
DeprecatedGET/radar/email/security/summary/dmarc
##### [Get email malicious classification summary]
DeprecatedGET/radar/email/security/summary/malicious
##### [Get email spam classification summary]
DeprecatedGET/radar/email/security/summary/spam
##### [Get email SPF validation summary]
DeprecatedGET/radar/email/security/summary/spf
##### [Get email threat category summary]
DeprecatedGET/radar/email/security/summary/threat_category
##### [Get email spoof classification summary]
DeprecatedGET/radar/email/security/summary/spoof
##### [Get email TLS version summary]
DeprecatedGET/radar/email/security/summary/tls_version
#### RadarEmailSecurityTimeseries Groups

##### [Get email ARC validation time series]
DeprecatedGET/radar/email/security/timeseries_groups/arc
##### [Get email DKIM validation time series]
DeprecatedGET/radar/email/security/timeseries_groups/dkim
##### [Get email DMARC validation time series]
DeprecatedGET/radar/email/security/timeseries_groups/dmarc
##### [Get email malicious classification time series]
DeprecatedGET/radar/email/security/timeseries_groups/malicious
##### [Get email spam classification time series]
DeprecatedGET/radar/email/security/timeseries_groups/spam
##### [Get email SPF validation time series]
DeprecatedGET/radar/email/security/timeseries_groups/spf
##### [Get email threat category time series]
DeprecatedGET/radar/email/security/timeseries_groups/threat_category
##### [Get email spoof classification time series]
DeprecatedGET/radar/email/security/timeseries_groups/spoof
##### [Get email TLS version time series]
DeprecatedGET/radar/email/security/timeseries_groups/tls_version
#### RadarAttacks

#### RadarAttacksLayer3

##### [Get layer 3 attacks summary by dimension]
GET/radar/attacks/layer3/summary/{dimension}
##### [Get layer 3 attacks by bytes time series]
GET/radar/attacks/layer3/timeseries
##### [Get layer 3 attacks time series grouped by dimension]
GET/radar/attacks/layer3/timeseries_groups/{dimension}
#### RadarAttacksLayer3Summary

##### [Get layer 3 attacks by bitrate summary]
DeprecatedGET/radar/attacks/layer3/summary/bitrate
##### [Get layer 3 attacks by duration summary]
DeprecatedGET/radar/attacks/layer3/summary/duration
##### [Get layer 3 attacks by IP version summary]
DeprecatedGET/radar/attacks/layer3/summary/ip_version
##### [Get layer 3 attacks by protocol summary]
DeprecatedGET/radar/attacks/layer3/summary/protocol
##### [Get layer 3 attacks by vector summary]
DeprecatedGET/radar/attacks/layer3/summary/vector
##### [Get layer 3 attacks by targeted industry summary]
DeprecatedGET/radar/attacks/layer3/summary/industry
##### [Get layer 3 attacks by targeted vertical summary]
DeprecatedGET/radar/attacks/layer3/summary/vertical
#### RadarAttacksLayer3Timeseries Groups

##### [Get layer 3 attacks by target industries time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/industry
##### [Get layer 3 attacks by IP version time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/ip_version
##### [Get layer 3 attacks by protocol time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/protocol
##### [Get layer 3 attacks by vector time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/vector
##### [Get layer 3 attacks by vertical time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/vertical
##### [Get layer 3 attacks by bitrate time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/bitrate
##### [Get layer 3 attacks by duration time series]
DeprecatedGET/radar/attacks/layer3/timeseries_groups/duration
#### RadarAttacksLayer3Top

##### [Get top layer 3 attack pairs (origin and target locations)]
GET/radar/attacks/layer3/top/attacks
##### [Get top industries targeted by layer 3 attacks]
DeprecatedGET/radar/attacks/layer3/top/industry
##### [Get top verticals targeted by layer 3 attacks]
DeprecatedGET/radar/attacks/layer3/top/vertical
#### RadarAttacksLayer3TopLocations

##### [Get top origin locations of layer 3 attacks]
GET/radar/attacks/layer3/top/locations/origin
##### [Get top target locations of layer 3 attacks]
GET/radar/attacks/layer3/top/locations/target
#### RadarAttacksLayer7

##### [Get layer 7 attacks summary by dimension]
GET/radar/attacks/layer7/summary/{dimension}
##### [Get layer 7 attacks time series]
GET/radar/attacks/layer7/timeseries
##### [Get layer 7 attacks time series grouped by dimension]
GET/radar/attacks/layer7/timeseries_groups/{dimension}
#### RadarAttacksLayer7Summary

##### [Get layer 7 attacks by IP version summary]
DeprecatedGET/radar/attacks/layer7/summary/ip_version
##### [Get layer 7 attacks by HTTP method summary]
DeprecatedGET/radar/attacks/layer7/summary/http_method
##### [Get layer 7 attacks by HTTP version summary]
DeprecatedGET/radar/attacks/layer7/summary/http_version
##### [Get layer 7 attacks by managed rules summary]
DeprecatedGET/radar/attacks/layer7/summary/managed_rules
##### [Get layer 7 attacks by mitigation product summary]
DeprecatedGET/radar/attacks/layer7/summary/mitigation_product
##### [Get layer 7 attacks by targeted industry summary]
DeprecatedGET/radar/attacks/layer7/summary/industry
##### [Get layer 7 attacks by targeted vertical summary]
DeprecatedGET/radar/attacks/layer7/summary/vertical
#### RadarAttacksLayer7Timeseries Groups

##### [Get layer 7 attacks by target industries time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/industry
##### [Get layer 7 attacks by IP version time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/ip_version
##### [Get layer 7 attacks by vertical time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/vertical
##### [Get layer 7 attacks by HTTP method time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/http_method
##### [Get layer 7 attacks by HTTP version time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/http_version
##### [Get layer 7 attacks by managed rules time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/managed_rules
##### [Get layer 7 attacks by mitigation product time series]
DeprecatedGET/radar/attacks/layer7/timeseries_groups/mitigation_product
#### RadarAttacksLayer7Top

##### [Get top layer 7 attack pairs (origin and target locations)]
GET/radar/attacks/layer7/top/attacks
##### [Get top industries targeted by layer 7 attacks]
DeprecatedGET/radar/attacks/layer7/top/industry
##### [Get top verticals targeted by layer 7 attacks]
DeprecatedGET/radar/attacks/layer7/top/vertical
#### RadarAttacksLayer7TopLocations

##### [Get top origin locations of layer 7 attacks]
GET/radar/attacks/layer7/top/locations/origin
##### [Get top target locations of layer 7 attacks]
GET/radar/attacks/layer7/top/locations/target
#### RadarAttacksLayer7TopAses

##### [Get top origin ASes of layer 7 attacks]
GET/radar/attacks/layer7/top/ases/origin
#### RadarEntities

##### [Get IP address details]
GET/radar/entities/ip
#### RadarEntitiesASNs

##### [List autonomous systems]
GET/radar/entities/asns
##### [Get AS details by ASN]
GET/radar/entities/asns/{asn}
##### [Get AS-level relationships by ASN]
GET/radar/entities/asns/{asn}/rel
##### [Get IRR AS-SETs that an AS is a member of]
GET/radar/entities/asns/{asn}/as_set
##### [Get AS details by IP address]
GET/radar/entities/asns/ip
##### [Get AS rankings by botnet threat feed activity]
GET/radar/entities/asns/botnet_threat_feed
#### RadarEntitiesLocations

##### [List locations]
GET/radar/entities/locations
##### [Get location details]
GET/radar/entities/locations/{location}
#### RadarGeolocations

##### [List Geolocations]
GET/radar/geolocations
##### [Get Geolocation details]
GET/radar/geolocations/{geo_id}
#### RadarHTTP

##### [Get HTTP requests summary by dimension]
GET/radar/http/summary/{dimension}
##### [Get HTTP requests time series]
GET/radar/http/timeseries
##### [Get HTTP requests time series grouped by dimension]
GET/radar/http/timeseries_groups/{dimension}
#### RadarHTTPLocations

##### [Get top locations by HTTP requests]
GET/radar/http/top/locations
#### RadarHTTPLocationsBot Class

##### [Get top locations by HTTP requests for a bot class]
GET/radar/http/top/locations/bot_class/{bot_class}
#### RadarHTTPLocationsDevice Type

##### [Get top locations by HTTP requests for a device type]
GET/radar/http/top/locations/device_type/{device_type}
#### RadarHTTPLocationsHTTP Protocol

##### [Get top locations by HTTP requests for an HTTP protocol]
GET/radar/http/top/locations/http_protocol/{http_protocol}
#### RadarHTTPLocationsHTTP Method

##### [Get top locations by HTTP requests for an HTTP version]
GET/radar/http/top/locations/http_version/{http_version}
#### RadarHTTPLocationsIP Version

##### [Get top locations by HTTP requests for an IP version]
GET/radar/http/top/locations/ip_version/{ip_version}
#### RadarHTTPLocationsOS

##### [Get top locations by HTTP requests for an OS]
GET/radar/http/top/locations/os/{os}
#### RadarHTTPLocationsTLS Version

##### [Get top locations by HTTP requests for a TLS version]
GET/radar/http/top/locations/tls_version/{tls_version}
#### RadarHTTPLocationsBrowser Family

##### [Get top locations by HTTP requests for a browser family]
GET/radar/http/top/locations/browser_family/{browser_family}
#### RadarHTTPAses

##### [Get top ASes by HTTP requests]
GET/radar/http/top/ases
#### RadarHTTPAsesBot Class

##### [Get top ASes by HTTP requests for a bot class]
GET/radar/http/top/ases/bot_class/{bot_class}
#### RadarHTTPAsesDevice Type

##### [Get top ASes by HTTP requests for a device type]
GET/radar/http/top/ases/device_type/{device_type}
#### RadarHTTPAsesHTTP Protocol

##### [Get top ASes by HTTP requests for an HTTP protocol]
GET/radar/http/top/ases/http_protocol/{http_protocol}
#### RadarHTTPAsesHTTP Method

##### [Get top ASes by HTTP requests for an HTTP version]
GET/radar/http/top/ases/http_version/{http_version}
#### RadarHTTPAsesIP Version

##### [Get top ASes by HTTP requests for an IP version]
GET/radar/http/top/ases/ip_version/{ip_version}
#### RadarHTTPAsesOS

##### [Get top ASes by HTTP requests for an OS]
GET/radar/http/top/ases/os/{os}
#### RadarHTTPAsesTLS Version

##### [Get top ASes by HTTP requests for a TLS version]
GET/radar/http/top/ases/tls_version/{tls_version}
#### RadarHTTPAsesBrowser Family

##### [Get top ASes by HTTP requests for a browser family]
GET/radar/http/top/ases/browser_family/{browser_family}
#### RadarHTTPSummary

##### [Get HTTP requests by bot class summary]
DeprecatedGET/radar/http/summary/bot_class
##### [Get HTTP requests by device type summary]
DeprecatedGET/radar/http/summary/device_type
##### [Get HTTP requests by HTTP/HTTPS summary]
DeprecatedGET/radar/http/summary/http_protocol
##### [Get HTTP requests by HTTP version summary]
DeprecatedGET/radar/http/summary/http_version
##### [Get HTTP requests by IP version summary]
DeprecatedGET/radar/http/summary/ip_version
##### [Get HTTP requests by OS summary]
DeprecatedGET/radar/http/summary/os
##### [Get HTTP requests by TLS version summary]
DeprecatedGET/radar/http/summary/tls_version
##### [Get HTTP requests by post-quantum support summary]
DeprecatedGET/radar/http/summary/post_quantum
#### RadarHTTPTimeseries Groups

##### [Get HTTP requests by TLS version time series]
DeprecatedGET/radar/http/timeseries_groups/tls_version
##### [Get HTTP requests by bot class time series]
DeprecatedGET/radar/http/timeseries_groups/bot_class
##### [Get HTTP requests by user agent time series]
DeprecatedGET/radar/http/timeseries_groups/browser
##### [Get HTTP requests by user agent family time series]
DeprecatedGET/radar/http/timeseries_groups/browser_family
##### [Get HTTP requests by device type time series]
DeprecatedGET/radar/http/timeseries_groups/device_type
##### [Get HTTP requests by HTTP/HTTPS time series]
DeprecatedGET/radar/http/timeseries_groups/http_protocol
##### [Get HTTP requests by HTTP version time series]
DeprecatedGET/radar/http/timeseries_groups/http_version
##### [Get HTTP requests by IP version time series]
DeprecatedGET/radar/http/timeseries_groups/ip_version
##### [Get HTTP requests by OS time series]
DeprecatedGET/radar/http/timeseries_groups/os
##### [Get HTTP requests by post-quantum support time series]
DeprecatedGET/radar/http/timeseries_groups/post_quantum
#### RadarHTTPTop

##### [Get top user agents by HTTP requests]
DeprecatedGET/radar/http/top/browser
##### [Get top user agent families by HTTP requests]
DeprecatedGET/radar/http/top/browser_family
#### RadarOrigins

##### [List Origins]
GET/radar/origins
##### [Get Origin details]
GET/radar/origins/{slug}
##### [Get origin metrics time series]
GET/radar/origins/timeseries
##### [Get origin metrics distribution by dimension]
GET/radar/origins/summary/{dimension}
##### [Get origin metrics time series grouped by dimension]
GET/radar/origins/timeseries_groups/{dimension}
#### RadarQuality

#### RadarQualityIQI

##### [Get Internet Quality Index (IQI) summary]
GET/radar/quality/iqi/summary
##### [Get Internet Quality Index (IQI) time series]
GET/radar/quality/iqi/timeseries_groups
#### RadarQualitySpeed

##### [Get speed tests summary]
GET/radar/quality/speed/summary
##### [Get speed tests histogram]
GET/radar/quality/speed/histogram
#### RadarQualitySpeedTop

##### [Get top ASes by speed test results]
GET/radar/quality/speed/top/ases
##### [Get top locations by speed test results]
GET/radar/quality/speed/top/locations
#### RadarRanking

##### [Get domains rank time series]
GET/radar/ranking/timeseries_groups
##### [Get top or trending domains]
GET/radar/ranking/top
#### RadarRankingDomain

##### [Get domain rank details]
GET/radar/ranking/domain/{domain}
#### RadarRankingInternet Services

##### [Get Internet services rank time series]
GET/radar/ranking/internet_services/timeseries_groups
##### [Get top Internet services]
GET/radar/ranking/internet_services/top
##### [List Internet services categories]
GET/radar/ranking/internet_services/categories
#### RadarTraffic Anomalies

##### [Get latest Internet traffic anomalies]
GET/radar/traffic_anomalies
#### RadarTraffic AnomaliesLocations

##### [Get top locations by total traffic anomalies]
GET/radar/traffic_anomalies/locations
#### RadarTCP Resets Timeouts

##### [Get TCP resets and timeouts summary]
GET/radar/tcp_resets_timeouts/summary
##### [Get TCP resets and timeouts time series]
GET/radar/tcp_resets_timeouts/timeseries_groups
#### RadarTLDs

##### [List TLDs]
GET/radar/tlds
##### [Get TLD details]
GET/radar/tlds/{tld}
#### RadarRobots TXT

#### RadarRobots TXTTop

##### [Get top domain categories by robots.txt files parsed]
GET/radar/robots_txt/top/domain_categories
#### RadarRobots TXTTopUser Agents

##### [Get top user agents on robots.txt files]
GET/radar/robots_txt/top/user_agents/directive
#### RadarLeaked Credentials

##### [Get HTTP authentication requests distribution by dimension]
GET/radar/leaked_credential_checks/summary/{dimension}
##### [Get time series distribution of HTTP authentication requests by dimension.]
GET/radar/leaked_credential_checks/timeseries_groups/{dimension}
#### RadarLeaked CredentialsSummary

##### [Get HTTP authentication requests by bot class summary]
DeprecatedGET/radar/leaked_credential_checks/summary/bot_class
##### [Get HTTP authentication requests by compromised credential status summary]
DeprecatedGET/radar/leaked_credential_checks/summary/compromised
#### RadarLeaked CredentialsTimeseries Groups

##### [Get HTTP authentication requests by bot class time series]
DeprecatedGET/radar/leaked_credential_checks/timeseries_groups/bot_class
##### [Get HTTP authentication requests by compromised credential status time series]
DeprecatedGET/radar/leaked_credential_checks/timeseries_groups/compromised
#### Bot Management

##### [Get Zone Bot Management Config]
GET/zones/{zone_id}/bot_management
##### [Update Zone Bot Management Config]
PUT/zones/{zone_id}/bot_management
#### Bot ManagementFeedback

##### [List zone feedback reports]
GET/zones/{zone_id}/bot_management/feedback
##### [Submit a feedback report]
POST/zones/{zone_id}/bot_management/feedback
#### Fraud

##### [Get Fraud Detection Settings]
GET/zones/{zone_id}/fraud_detection/settings
##### [Update Fraud Detection Settings]
PUT/zones/{zone_id}/fraud_detection/settings
#### Origin Post Quantum Encryption

##### [Get Origin Post-Quantum Encryption setting]
GET/zones/{zone_id}/cache/origin_post_quantum_encryption
##### [Change Origin Post-Quantum Encryption setting]
PUT/zones/{zone_id}/cache/origin_post_quantum_encryption
#### Google Tag Gateway

#### Google Tag GatewayConfig

##### [Get Google Tag Gateway configuration]
GET/zones/{zone_id}/settings/google-tag-gateway/config
##### [Update Google Tag Gateway configuration]
PUT/zones/{zone_id}/settings/google-tag-gateway/config
#### Zaraz

##### [Update Zaraz workflow]
PUT/zones/{zone_id}/settings/zaraz/workflow
#### ZarazConfig

##### [Get Zaraz configuration]
GET/zones/{zone_id}/settings/zaraz/config
##### [Update Zaraz configuration]
PUT/zones/{zone_id}/settings/zaraz/config
#### ZarazDefault

##### [Get default Zaraz configuration]
GET/zones/{zone_id}/settings/zaraz/default
#### ZarazExport

##### [Export Zaraz configuration]
GET/zones/{zone_id}/settings/zaraz/export
#### ZarazHistory

##### [List Zaraz historical configuration records]
GET/zones/{zone_id}/settings/zaraz/history
##### [Restore Zaraz historical configuration by ID]
PUT/zones/{zone_id}/settings/zaraz/history
#### ZarazHistoryConfigs

##### [Get Zaraz historical configurations by ID(s)]
GET/zones/{zone_id}/settings/zaraz/history/configs
#### ZarazPublish

##### [Publish Zaraz preview configuration]
POST/zones/{zone_id}/settings/zaraz/publish
#### ZarazWorkflow

##### [Get Zaraz workflow]
GET/zones/{zone_id}/settings/zaraz/workflow
#### Speed

#### SpeedSchedule

##### [Get a page test schedule]
GET/zones/{zone_id}/speed_api/schedule/{url}
##### [Create scheduled page test]
POST/zones/{zone_id}/speed_api/schedule/{url}
##### [Delete scheduled page test]
DELETE/zones/{zone_id}/speed_api/schedule/{url}
#### SpeedAvailabilities

##### [Get quota and availability]
GET/zones/{zone_id}/speed_api/availabilities
#### SpeedPages

##### [List tested webpages]
GET/zones/{zone_id}/speed_api/pages
##### [List core web vital metrics trend]
GET/zones/{zone_id}/speed_api/pages/{url}/trend
#### SpeedPagesTests

##### [List page test history]
GET/zones/{zone_id}/speed_api/pages/{url}/tests
##### [Get a page test result]
GET/zones/{zone_id}/speed_api/pages/{url}/tests/{test_id}
##### [Start page test]
POST/zones/{zone_id}/speed_api/pages/{url}/tests
##### [Delete all page tests]
DELETE/zones/{zone_id}/speed_api/pages/{url}/tests
#### DCV Delegation

##### [Retrieve the DCV Delegation unique identifier.]
GET/zones/{zone_id}/dcv_delegation/uuid
#### Hostnames

#### HostnamesSettings

#### HostnamesSettingsTLS

##### [List TLS setting for hostnames]
GET/zones/{zone_id}/hostnames/settings/{setting_id}
##### [Edit TLS setting for hostname]
PUT/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
##### [Delete TLS setting for hostname]
DELETE/zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
#### Snippets

##### [List zone snippets]
GET/zones/{zone_id}/snippets
##### [Get a zone snippet]
GET/zones/{zone_id}/snippets/{snippet_name}
##### [Update a zone snippet]
PUT/zones/{zone_id}/snippets/{snippet_name}
##### [Delete a zone snippet]
DELETE/zones/{zone_id}/snippets/{snippet_name}
#### SnippetsContent

##### [Get a zone snippet content]
GET/zones/{zone_id}/snippets/{snippet_name}/content
#### SnippetsRules

##### [List zone snippet rules]
GET/zones/{zone_id}/snippets/snippet_rules
##### [Update zone snippet rules]
PUT/zones/{zone_id}/snippets/snippet_rules
##### [Delete zone snippet rules]
DELETE/zones/{zone_id}/snippets/snippet_rules
#### Realtime Kit

#### Realtime KitApps

##### [Fetch all apps]
GET/accounts/{account_id}/realtime/kit/apps
##### [Create App]
POST/accounts/{account_id}/realtime/kit/apps
#### Realtime KitMeetings

##### [Fetch all meetings for an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings
##### [Create a meeting]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings
##### [Fetch a meeting for an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}
##### [Update a meeting]
PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}
##### [Replace a meeting]
PUT/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}
##### [Fetch all participants of a meeting]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants
##### [Add a participant]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants
##### [Fetch a participant's detail]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}
##### [Edit a participant's detail]
PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}
##### [Delete a participant]
DELETE/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}
##### [Refresh participant's authentication token]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token
#### Realtime KitPresets

##### [Fetch all presets]
GET/accounts/{account_id}/realtime/kit/{app_id}/presets
##### [Create a preset]
POST/accounts/{account_id}/realtime/kit/{app_id}/presets
##### [Fetch details of a preset]
GET/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}
##### [Delete a preset]
DELETE/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}
##### [Update a preset]
PATCH/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}
#### Realtime KitSessions

##### [Fetch all sessions of an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions
##### [Fetch details of a session]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}
##### [Fetch participants list of a session]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants
##### [Fetch details of a participant]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}
##### [Fetch all chat messages of a session]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat
##### [Fetch the complete transcript for a session]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript
##### [Fetch summary of transcripts for a session]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary
##### [Generate summary of Transcripts for the session]
POST/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary
##### [Fetch details of peer]
GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}
#### Realtime KitRecordings

##### [Fetch all recordings for an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/recordings
##### [Start recording a meeting]
POST/accounts/{account_id}/realtime/kit/{app_id}/recordings
##### [Fetch active recording]
GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}
##### [Fetch details of a recording]
GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}
##### [Pause/Resume/Stop recording]
PUT/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}
##### [Start recording audio and video tracks]
POST/accounts/{account_id}/realtime/kit/{app_id}/recordings/track
#### Realtime KitWebhooks

##### [Fetch all webhooks details]
GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks
##### [Add a webhook]
POST/accounts/{account_id}/realtime/kit/{app_id}/webhooks
##### [Fetch details of a webhook]
GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}
##### [Replace a webhook]
PUT/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}
##### [Edit a webhook]
PATCH/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}
##### [Delete a webhook]
DELETE/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}
#### Realtime KitActive Session

##### [Fetch details of an active session]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session
##### [Kick participants from an active session]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick
##### [Kick all participants]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all
##### [Create a poll]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll
#### Realtime KitLivestreams

##### [Create an independent livestream]
POST/accounts/{account_id}/realtime/kit/{app_id}/livestreams
##### [Fetch all livestreams]
GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams
##### [Stop livestreaming a meeting]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop
##### [Start livestreaming a meeting]
POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams
##### [Fetch complete analytics data for your livestreams]
GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall
##### [Fetch day-wise session and recording analytics data for an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise
##### [Fetch active livestreams for a meeting]
GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream
##### [Fetch livestream session details using livestream session ID]
GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream-session-id}
##### [Fetch active livestream session details]
GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session
##### [Fetch livestream details using livestream ID]
GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}
#### Realtime KitAnalytics

##### [Fetch day-wise session and recording analytics data for an App]
GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise
#### Calls

#### CallsSFU

##### [List apps]
GET/accounts/{account_id}/calls/apps
##### [Retrieve app details]
GET/accounts/{account_id}/calls/apps/{app_id}
##### [Create a new app]
POST/accounts/{account_id}/calls/apps
##### [Edit app details]
PUT/accounts/{account_id}/calls/apps/{app_id}
##### [Delete app]
DELETE/accounts/{account_id}/calls/apps/{app_id}
#### CallsTURN

##### [List TURN Keys]
GET/accounts/{account_id}/calls/turn_keys
##### [Retrieve TURN key details]
GET/accounts/{account_id}/calls/turn_keys/{key_id}
##### [Create a new TURN key]
POST/accounts/{account_id}/calls/turn_keys
##### [Edit TURN key details]
PUT/accounts/{account_id}/calls/turn_keys/{key_id}
##### [Delete TURN key]
DELETE/accounts/{account_id}/calls/turn_keys/{key_id}
#### Cloudforce One

#### Cloudforce OneScans

#### Cloudforce OneScansResults

##### [Get the Latest Scan Result]
GET/accounts/{account_id}/cloudforce-one/scans/results/{config_id}
#### Cloudforce OneScansConfig

##### [List Scan Configs]
GET/accounts/{account_id}/cloudforce-one/scans/config
##### [Create a new Scan Config]
POST/accounts/{account_id}/cloudforce-one/scans/config
##### [Update an existing Scan Config]
PATCH/accounts/{account_id}/cloudforce-one/scans/config/{config_id}
##### [Delete a Scan Config]
DELETE/accounts/{account_id}/cloudforce-one/scans/config/{config_id}
#### Cloudforce OneBinary Storage

##### [Retrieves a file from Binary Storage]
GET/accounts/{account_id}/cloudforce-one/binary/{hash}
##### [Posts a file to Binary Storage]
POST/accounts/{account_id}/cloudforce-one/binary
#### Cloudforce OneRequests

##### [List Requests]
POST/accounts/{account_id}/cloudforce-one/requests
##### [Get a Request]
GET/accounts/{account_id}/cloudforce-one/requests/{request_id}
##### [Create a New Request.]
POST/accounts/{account_id}/cloudforce-one/requests/new
##### [Update a Request]
PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}
##### [Delete a Request]
DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}
##### [Get Request Quota]
GET/accounts/{account_id}/cloudforce-one/requests/quota
##### [Get Request Types]
GET/accounts/{account_id}/cloudforce-one/requests/types
##### [Get Request Priority, Status, and TLP constants]
GET/accounts/{account_id}/cloudforce-one/requests/constants
#### Cloudforce OneRequestsMessage

##### [List Request Messages]
POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/message
##### [Create a New Request Message]
POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/new
##### [Update a Request Message]
PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}
##### [Delete a Request Message]
DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}
#### Cloudforce OneRequestsPriority

##### [Get a Priority Intelligence Requirement]
GET/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}
##### [Create a New Priority Intelligence Requirement]
POST/accounts/{account_id}/cloudforce-one/requests/priority/new
##### [Update a Priority Intelligence Requirement]
PUT/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}
##### [Delete a Priority Intelligence Requirement]
DELETE/accounts/{account_id}/cloudforce-one/requests/priority/{priority_id}
##### [Get Priority Intelligence Requirement Quota]
GET/accounts/{account_id}/cloudforce-one/requests/priority/quota
#### Cloudforce OneRequestsAssets

##### [Get a Request Asset]
GET/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}
##### [List Request Assets]
POST/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset
##### [Update a Request Asset]
PUT/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}
##### [Delete a Request Asset]
DELETE/accounts/{account_id}/cloudforce-one/requests/{request_id}/asset/{asset_id}
#### Cloudforce OneThreat Events

##### [Filter and list events]
GET/accounts/{account_id}/cloudforce-one/events
##### [Reads an event]
DeprecatedGET/accounts/{account_id}/cloudforce-one/events/{event_id}
##### [Creates a new event]
POST/accounts/{account_id}/cloudforce-one/events/create
##### [Updates an event]
PATCH/accounts/{account_id}/cloudforce-one/events/{event_id}
##### [Creates bulk events]
POST/accounts/{account_id}/cloudforce-one/events/create/bulk
#### Cloudforce OneThreat EventsAttackers

##### [Lists attackers across multiple datasets]
GET/accounts/{account_id}/cloudforce-one/events/attackers
#### Cloudforce OneThreat EventsCategories

##### [Lists categories across multiple datasets]
GET/accounts/{account_id}/cloudforce-one/events/categories
##### [Reads a category]
GET/accounts/{account_id}/cloudforce-one/events/categories/{category_id}
##### [Creates a new category]
POST/accounts/{account_id}/cloudforce-one/events/categories/create
##### [Updates a category]
PATCH/accounts/{account_id}/cloudforce-one/events/categories/{category_id}
##### [Deletes a category]
DELETE/accounts/{account_id}/cloudforce-one/events/categories/{category_id}
#### Cloudforce OneThreat EventsCountries

##### [Retrieves countries information for all countries]
GET/accounts/{account_id}/cloudforce-one/events/countries
#### Cloudforce OneThreat EventsCrons

#### Cloudforce OneThreat EventsDatasets

##### [Lists all datasets in an account]
GET/accounts/{account_id}/cloudforce-one/events/dataset
##### [Reads a dataset]
GET/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}
##### [Creates a dataset]
POST/accounts/{account_id}/cloudforce-one/events/dataset/create
##### [Updates an existing dataset]
PATCH/accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}
##### [Reads raw data for an event by UUID]
GET/accounts/{account_id}/cloudforce-one/events/raw/{dataset_id}/{event_id}
#### Cloudforce OneThreat EventsDatasetsHealth

#### Cloudforce OneThreat EventsIndicator Types

##### [Lists all indicator types]
DeprecatedGET/accounts/{account_id}/cloudforce-one/events/indicatorTypes
#### Cloudforce OneThreat EventsRaw

##### [Reads data for a raw event]
GET/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}
##### [Updates a raw event]
PATCH/accounts/{account_id}/cloudforce-one/events/{event_id}/raw/{raw_id}
#### Cloudforce OneThreat EventsRelate

##### [Removes an event reference]
DELETE/accounts/{account_id}/cloudforce-one/events/relate/{event_id}
#### Cloudforce OneThreat EventsTags

##### [Creates a new tag]
POST/accounts/{account_id}/cloudforce-one/events/tags/create
#### Cloudforce OneThreat EventsEvent Tags

##### [Adds a tag to an event]
POST/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}/create
##### [Removes a tag from an event]
DELETE/accounts/{account_id}/cloudforce-one/events/event_tag/{event_id}
#### Cloudforce OneThreat EventsTarget Industries

##### [Lists target industries across multiple datasets]
GET/accounts/{account_id}/cloudforce-one/events/targetIndustries
#### Cloudforce OneThreat EventsInsights

#### AI Gateway

##### [List Gateways]
GET/accounts/{account_id}/ai-gateway/gateways
##### [Fetch a Gateway]
GET/accounts/{account_id}/ai-gateway/gateways/{id}
##### [Create a new Gateway]
POST/accounts/{account_id}/ai-gateway/gateways
##### [Update a Gateway]
PUT/accounts/{account_id}/ai-gateway/gateways/{id}
##### [Delete a Gateway]
DELETE/accounts/{account_id}/ai-gateway/gateways/{id}
#### AI GatewayEvaluation Types

##### [List Evaluators]
GET/accounts/{account_id}/ai-gateway/evaluation-types
#### AI GatewayLogs

##### [List Gateway Logs]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs
##### [Get Gateway Log Detail]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}
##### [Patch Gateway Log]
PATCH/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}
##### [Delete Gateway Logs]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs
##### [Get Gateway Log Request]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request
##### [Get Gateway Log Response]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response
#### AI GatewayDatasets

##### [List Datasets]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets
##### [Fetch a Dataset]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
##### [Create a new Dataset]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets
##### [Update a Dataset]
PUT/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
##### [Delete a Dataset]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}
#### AI GatewayEvaluations

##### [List Evaluations]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations
##### [Fetch a Evaluation]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}
##### [Create a new Evaluation]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations
##### [Delete a Evaluation]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}
#### AI GatewayDynamic Routing

##### [List all AI Gateway Dynamic Routes.]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes
##### [Get an AI Gateway Dynamic Route.]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}
##### [Create a new AI Gateway Dynamic Route.]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes
##### [Update an AI Gateway Dynamic Route.]
PATCH/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}
##### [Delete an AI Gateway Dynamic Route.]
DELETE/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}
##### [List all AI Gateway Dynamic Route Deployments.]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments
##### [Create a new AI Gateway Dynamic Route Deployment.]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments
##### [List all AI Gateway Dynamic Route Versions.]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions
##### [Create a new AI Gateway Dynamic Route Version.]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions
##### [Get an AI Gateway Dynamic Route Version.]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions/{version_id}
#### AI GatewayProvider Configs

##### [List Provider Configs]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs
##### [Create a new Provider Configs]
POST/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs
#### AI GatewayURLs

##### [Get Gateway URL]
GET/accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}
#### IAM

#### IAMPermission Groups

##### [List Account Permission Groups]
GET/accounts/{account_id}/iam/permission_groups
##### [Permission Group Details]
GET/accounts/{account_id}/iam/permission_groups/{permission_group_id}
#### IAMResource Groups

##### [List Resource Groups]
GET/accounts/{account_id}/iam/resource_groups
##### [Resource Group Details]
GET/accounts/{account_id}/iam/resource_groups/{resource_group_id}
##### [Create Resource Group]
POST/accounts/{account_id}/iam/resource_groups
##### [Update Resource Group]
PUT/accounts/{account_id}/iam/resource_groups/{resource_group_id}
##### [Remove Resource Group]
DELETE/accounts/{account_id}/iam/resource_groups/{resource_group_id}
#### IAMUser Groups

##### [List User Groups]
GET/accounts/{account_id}/iam/user_groups
##### [User Group Details]
GET/accounts/{account_id}/iam/user_groups/{user_group_id}
##### [Create User Group]
POST/accounts/{account_id}/iam/user_groups
##### [Update User Group]
PUT/accounts/{account_id}/iam/user_groups/{user_group_id}
##### [Remove User Group]
DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}
#### IAMUser GroupsMembers

##### [List User Group Members]
GET/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Add User Group Members]
POST/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Update User Group Members]
PUT/accounts/{account_id}/iam/user_groups/{user_group_id}/members
##### [Remove User Group Member]
DELETE/accounts/{account_id}/iam/user_groups/{user_group_id}/members/{member_id}
#### IAMSSO

##### [Get all SSO connectors]
GET/accounts/{account_id}/sso_connectors
##### [Get single SSO connector]
GET/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Initialize new SSO connector]
POST/accounts/{account_id}/sso_connectors
##### [Update SSO connector state]
PATCH/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Delete SSO connector]
DELETE/accounts/{account_id}/sso_connectors/{sso_connector_id}
##### [Begin SSO connector verification]
POST/accounts/{account_id}/sso_connectors/{sso_connector_id}/begin_verification
#### Cloud Connector

#### Cloud ConnectorRules

##### [Rules]
GET/zones/{zone_id}/cloud_connector/rules
##### [Put Rules]
PUT/zones/{zone_id}/cloud_connector/rules
#### Botnet Feed

#### Botnet FeedASN

##### [Get daily report]
GET/accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report
##### [Get full report]
GET/accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report
#### Botnet FeedConfigs

#### Botnet FeedConfigsASN

##### [Get list of ASNs]
GET/accounts/{account_id}/botnet_feed/configs/asn
##### [Delete an ASN]
DELETE/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}
#### Security TXT

##### [Retrieves security.txt]
GET/zones/{zone_id}/security-center/securitytxt
##### [Updates security.txt]
PUT/zones/{zone_id}/security-center/securitytxt
##### [Deletes security.txt]
DELETE/zones/{zone_id}/security-center/securitytxt
#### Workflows

##### [List all Workflows]
GET/accounts/{account_id}/workflows
##### [Get Workflow details]
GET/accounts/{account_id}/workflows/{workflow_name}
##### [Create/modify Workflow]
PUT/accounts/{account_id}/workflows/{workflow_name}
##### [Deletes a Workflow]
DELETE/accounts/{account_id}/workflows/{workflow_name}
#### WorkflowsInstances

##### [List of workflow instances]
GET/accounts/{account_id}/workflows/{workflow_name}/instances
##### [Get logs and status from instance]
GET/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}
##### [Create a new workflow instance]
POST/accounts/{account_id}/workflows/{workflow_name}/instances
##### [Batch create new Workflow instances]
POST/accounts/{account_id}/workflows/{workflow_name}/instances/batch
#### WorkflowsInstancesStatus

##### [Change status of instance]
PATCH/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/status
#### WorkflowsInstancesEvents

##### [Send event to instance]
POST/accounts/{account_id}/workflows/{workflow_name}/instances/{instance_id}/events/{event_type}
#### WorkflowsVersions

##### [List deployed Workflow versions]
GET/accounts/{account_id}/workflows/{workflow_name}/versions
##### [Get Workflow version details]
GET/accounts/{account_id}/workflows/{workflow_name}/versions/{version_id}
#### Workers Builds

##### [Get latest builds by script IDs]
GET/accounts/{account_id}/builds/builds/latest
##### [Get builds by version IDs]
GET/accounts/{account_id}/builds/builds
##### [Get account limits]
GET/accounts/{account_id}/builds/account/limits
#### Workers BuildsTriggers

##### [List triggers by script]
GET/accounts/{account_id}/builds/workers/{external_script_id}/triggers
##### [Create trigger]
POST/accounts/{account_id}/builds/triggers
##### [Update trigger]
PATCH/accounts/{account_id}/builds/triggers/{trigger_uuid}
##### [Delete trigger]
DELETE/accounts/{account_id}/builds/triggers/{trigger_uuid}
##### [Purge build cache]
POST/accounts/{account_id}/builds/triggers/{trigger_uuid}/purge_build_cache
##### [Create manual build]
POST/accounts/{account_id}/builds/triggers/{trigger_uuid}/builds
#### Workers BuildsTriggersEnvironment Variables

##### [List environment variables]
GET/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables
##### [Upsert environment variables]
PATCH/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables
##### [Delete environment variable]
DELETE/accounts/{account_id}/builds/triggers/{trigger_uuid}/environment_variables/{environment_variable_key}
#### Workers BuildsTokens

##### [Create build token]
POST/accounts/{account_id}/builds/tokens
##### [List build tokens]
GET/accounts/{account_id}/builds/tokens
##### [Delete build token]
DELETE/accounts/{account_id}/builds/tokens/{build_token_uuid}
#### Workers BuildsRepos

#### Workers BuildsReposConnections

##### [Create or update repository connection]
PUT/accounts/{account_id}/builds/repos/connections
##### [Delete repository connection]
DELETE/accounts/{account_id}/builds/repos/connections/{repo_connection_uuid}
#### Workers BuildsReposConfig Autofill

##### [Get repository configuration autofill]
GET/accounts/{account_id}/builds/repos/{provider_type}/{provider_account_id}/{repo_id}/config_autofill
#### Workers BuildsBuilds

##### [List builds by script]
GET/accounts/{account_id}/builds/workers/{external_script_id}/builds
##### [Get build by UUID]
GET/accounts/{account_id}/builds/builds/{build_uuid}
##### [Cancel build]
PUT/accounts/{account_id}/builds/builds/{build_uuid}/cancel
#### Workers BuildsBuildsLogs

##### [Get build logs]
GET/accounts/{account_id}/builds/builds/{build_uuid}/logs
#### Resource Sharing

##### [List account shares]
GET/accounts/{account_id}/shares
##### [Get account share by ID]
GET/accounts/{account_id}/shares/{share_id}
##### [Create a new share]
POST/accounts/{account_id}/shares
##### [Update a share]
PUT/accounts/{account_id}/shares/{share_id}
##### [Delete a share]
DELETE/accounts/{account_id}/shares/{share_id}
#### Resource SharingRecipients

##### [List share recipients by share ID]
GET/accounts/{account_id}/shares/{share_id}/recipients
##### [Get share recipient by ID]
GET/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}
##### [Create a new share recipient]
POST/accounts/{account_id}/shares/{share_id}/recipients
##### [Delete a share recipient]
DELETE/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}
#### Resource SharingResources

##### [List share resources by share ID]
GET/accounts/{account_id}/shares/{share_id}/resources
##### [Get share resource by ID]
GET/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
##### [Create a new share resource]
POST/accounts/{account_id}/shares/{share_id}/resources
##### [Update a share resource]
PUT/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
##### [Delete a share resource]
DELETE/accounts/{account_id}/shares/{share_id}/resources/{resource_id}
#### Resource Tagging

##### [List tagged resources]
GET/accounts/{account_id}/tags/resources
#### Resource TaggingAccount Tags

##### [Get tags for an account-level resource]
GET/accounts/{account_id}/tags
##### [Set tags for an account-level resource]
PUT/accounts/{account_id}/tags
##### [Delete tags from an account-level resource]
DELETE/accounts/{account_id}/tags
#### Resource TaggingZone Tags

##### [Get tags for a zone-level resource]
GET/zones/{zone_id}/tags
##### [Set tags for a zone-level resource]
PUT/zones/{zone_id}/tags
##### [Delete tags from a zone-level resource]
DELETE/zones/{zone_id}/tags
#### Resource TaggingKeys

##### [List tag keys]
GET/accounts/{account_id}/tags/keys
#### Resource TaggingValues

##### [List tag values]
GET/accounts/{account_id}/tags/values/{tag_key}
#### Leaked Credential Checks

##### [Get Leaked Credential Checks Status]
GET/zones/{zone_id}/leaked-credential-checks
##### [Set Leaked Credential Checks Status]
POST/zones/{zone_id}/leaked-credential-checks
#### Leaked Credential ChecksDetections

##### [List Leaked Credential Checks Custom Detections]
GET/zones/{zone_id}/leaked-credential-checks/detections
##### [Create Leaked Credential Checks Custom Detection]
POST/zones/{zone_id}/leaked-credential-checks/detections
##### [Get Leaked Credential Checks Custom Detection]
GET/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}
##### [Update Leaked Credential Checks Custom Detection]
PUT/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}
##### [Delete Leaked Credential Checks Custom Detection]
DELETE/zones/{zone_id}/leaked-credential-checks/detections/{detection_id}
#### Content Scanning

##### [Enable Content Scanning]
POST/zones/{zone_id}/content-upload-scan/enable
##### [Disable Content Scanning]
POST/zones/{zone_id}/content-upload-scan/disable
##### [Update Content Scanning Status]
PUT/zones/{zone_id}/content-upload-scan/settings
##### [Update Content Scanning Status]
PUT/zones/{zone_id}/content-upload-scan/settings
##### [Get Content Scanning Status]
GET/zones/{zone_id}/content-upload-scan/settings
#### Content ScanningPayloads

##### [List Existing Custom Scan Expressions]
GET/zones/{zone_id}/content-upload-scan/payloads
##### [Add Custom Scan Expressions]
POST/zones/{zone_id}/content-upload-scan/payloads
##### [Delete a Custom Scan Expression]
DELETE/zones/{zone_id}/content-upload-scan/payloads/{expression_id}
#### Content ScanningSettings

##### [Get Content Scanning Status]
GET/zones/{zone_id}/content-upload-scan/settings
#### Abuse Reports

##### [Submit an abuse report]
POST/accounts/{account_id}/abuse-reports/{report_param}
##### [Abuse Report Details]
GET/accounts/{account_id}/abuse-reports/{report_param}
##### [List abuse reports]
GET/accounts/{account_id}/abuse-reports
#### Abuse ReportsMitigations

##### [List abuse report mitigations]
GET/accounts/{account_id}/abuse-reports/{report_id}/mitigations
##### [Request review on mitigations]
POST/accounts/{account_id}/abuse-reports/{report_id}/mitigations/appeal
#### AI

##### [Execute AI model]
POST/accounts/{account_id}/ai/run/{model_name}
#### AIFinetunes

##### [List Finetunes]
GET/accounts/{account_id}/ai/finetunes
##### [Create a new Finetune]
POST/accounts/{account_id}/ai/finetunes
#### AIFinetunesAssets

##### [Upload a Finetune Asset]
POST/accounts/{account_id}/ai/finetunes/{finetune_id}/finetune-assets
#### AIFinetunesPublic

##### [List Public Finetunes]
GET/accounts/{account_id}/ai/finetunes/public
#### AIAuthors

##### [Author Search]
GET/accounts/{account_id}/ai/authors/search
#### AITasks

##### [Task Search]
GET/accounts/{account_id}/ai/tasks/search
#### AIModels

##### [Model Search]
GET/accounts/{account_id}/ai/models/search
#### AIModelsSchema

##### [Get Model Schema]
GET/accounts/{account_id}/ai/models/schema
#### AITo Markdown

##### [Convert Files into Markdown]
POST/accounts/{account_id}/ai/tomarkdown
##### [Get all converted formats supported]
GET/accounts/{account_id}/ai/tomarkdown/supported
#### AI Search

#### AI SearchInstances

##### [List instances.]
GET/accounts/{account_id}/ai-search/instances
##### [Create new instances.]
POST/accounts/{account_id}/ai-search/instances
##### [Read instances.]
GET/accounts/{account_id}/ai-search/instances/{id}
##### [Update instances.]
PUT/accounts/{account_id}/ai-search/instances/{id}
##### [Delete instances.]
DELETE/accounts/{account_id}/ai-search/instances/{id}
##### [Stats]
GET/accounts/{account_id}/ai-search/instances/{id}/stats
##### [Search]
POST/accounts/{account_id}/ai-search/instances/{id}/search
##### [Chat Completions]
POST/accounts/{account_id}/ai-search/instances/{id}/chat/completions
#### AI SearchInstancesItems

#### AI SearchInstancesJobs

##### [List Jobs]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs
##### [Create new job]
POST/accounts/{account_id}/ai-search/instances/{id}/jobs
##### [Get a Job Details]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}
##### [List Job Logs]
GET/accounts/{account_id}/ai-search/instances/{id}/jobs/{job_id}/logs
#### AI SearchTokens

##### [List tokens.]
GET/accounts/{account_id}/ai-search/tokens
##### [Create new tokens.]
POST/accounts/{account_id}/ai-search/tokens
##### [Read tokens.]
GET/accounts/{account_id}/ai-search/tokens/{id}
##### [Update tokens.]
PUT/accounts/{account_id}/ai-search/tokens/{id}
##### [Delete tokens.]
DELETE/accounts/{account_id}/ai-search/tokens/{id}
#### AutoRAG

##### [AI Search]
DeprecatedPOST/accounts/{account_id}/autorag/rags/{id}/ai-search
##### [Search]
DeprecatedPOST/accounts/{account_id}/autorag/rags/{id}/search
##### [Sync]
DeprecatedPATCH/accounts/{account_id}/autorag/rags/{id}/sync
##### [Files]
DeprecatedGET/accounts/{account_id}/autorag/rags/{id}/files
#### AutoRAGJobs

##### [List Jobs]
DeprecatedGET/accounts/{account_id}/autorag/rags/{id}/jobs
##### [Get a Job Details]
DeprecatedGET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}
##### [List Job Logs]
DeprecatedGET/accounts/{account_id}/autorag/rags/{id}/jobs/{job_id}/logs
#### Security Center

#### Security CenterInsights

##### [Retrieves Security Center Insights]
GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights
##### [Archives Security Center Insight]
PUT/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/{issue_id}/dismiss
#### Security CenterInsightsClass

##### [Retrieves Security Center Insight Counts by Class]
GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/class
#### Security CenterInsightsSeverity

##### [Retrieves Security Center Insight Counts by Severity]
GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/severity
#### Security CenterInsightsType

##### [Retrieves Security Center Insight Counts by Type]
GET/{accounts_or_zones}/{account_or_zone_id}/security-center/insights/type
#### Browser Rendering

#### Browser RenderingContent

##### [Get HTML content.]
POST/accounts/{account_id}/browser-rendering/content
#### Browser RenderingPDF

##### [Get PDF.]
POST/accounts/{account_id}/browser-rendering/pdf
#### Browser RenderingScrape

##### [Scrape elements.]
POST/accounts/{account_id}/browser-rendering/scrape
#### Browser RenderingScreenshot

##### [Get screenshot.]
POST/accounts/{account_id}/browser-rendering/screenshot
#### Browser RenderingSnapshot

##### [Get HTML content and screenshot.]
POST/accounts/{account_id}/browser-rendering/snapshot
#### Browser RenderingJson

##### [Get json.]
POST/accounts/{account_id}/browser-rendering/json
#### Browser RenderingLinks

##### [Get Links.]
POST/accounts/{account_id}/browser-rendering/links
#### Browser RenderingMarkdown

##### [Get markdown.]
POST/accounts/{account_id}/browser-rendering/markdown
#### Browser RenderingCrawl

##### [Crawl websites.]
POST/accounts/{account_id}/browser-rendering/crawl
##### [Get crawl result.]
GET/accounts/{account_id}/browser-rendering/crawl/{job_id}
##### [Cancel a crawl job.]
DELETE/accounts/{account_id}/browser-rendering/crawl/{job_id}
#### Custom Pages

##### [List custom pages]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages
##### [Get a custom page]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}
##### [Update a custom page]
PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}
#### Custom PagesAssets

##### [List custom assets]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets
##### [Get a custom asset]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
##### [Create a custom asset]
POST/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets
##### [Update a custom asset]
PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
##### [Delete a custom asset]
DELETE/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
#### Secrets Store

#### Secrets StoreStores

##### [List account stores]
GET/accounts/{account_id}/secrets_store/stores
##### [Create a store]
POST/accounts/{account_id}/secrets_store/stores
##### [Delete a store]
DELETE/accounts/{account_id}/secrets_store/stores/{store_id}
#### Secrets StoreStoresSecrets

##### [List store secrets]
GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets
##### [Get a secret by ID]
GET/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}
##### [Create a secret]
POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets
##### [Patch a secret]
PATCH/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}
##### [Delete a secret]
DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}
##### [Delete secrets]
DELETE/accounts/{account_id}/secrets_store/stores/{store_id}/secrets
##### [Duplicate Secret]
POST/accounts/{account_id}/secrets_store/stores/{store_id}/secrets/{secret_id}/duplicate
#### Secrets StoreQuota

##### [View secret usage]
GET/accounts/{account_id}/secrets_store/quota
#### Pipelines

##### [[DEPRECATED] List Pipelines]
DeprecatedGET/accounts/{account_id}/pipelines
##### [[DEPRECATED] Get Pipeline]
DeprecatedGET/accounts/{account_id}/pipelines/{pipeline_name}
##### [[DEPRECATED] Create Pipeline]
DeprecatedPOST/accounts/{account_id}/pipelines
##### [[DEPRECATED] Update Pipeline]
DeprecatedPUT/accounts/{account_id}/pipelines/{pipeline_name}
##### [[DEPRECATED] Delete Pipeline]
DeprecatedDELETE/accounts/{account_id}/pipelines/{pipeline_name}
##### [List Pipelines]
GET/accounts/{account_id}/pipelines/v1/pipelines
##### [Get Pipeline Details]
GET/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}
##### [Create Pipeline]
POST/accounts/{account_id}/pipelines/v1/pipelines
##### [Delete Pipelines]
DELETE/accounts/{account_id}/pipelines/v1/pipelines/{pipeline_id}
##### [Validate SQL]
POST/accounts/{account_id}/pipelines/v1/validate_sql
#### PipelinesSinks

##### [List Sinks]
GET/accounts/{account_id}/pipelines/v1/sinks
##### [Get Sink Details]
GET/accounts/{account_id}/pipelines/v1/sinks/{sink_id}
##### [Create Sink]
POST/accounts/{account_id}/pipelines/v1/sinks
##### [Delete Sink]
DELETE/accounts/{account_id}/pipelines/v1/sinks/{sink_id}
#### PipelinesStreams

##### [List Streams]
GET/accounts/{account_id}/pipelines/v1/streams
##### [Get Stream Details]
GET/accounts/{account_id}/pipelines/v1/streams/{stream_id}
##### [Create Stream]
POST/accounts/{account_id}/pipelines/v1/streams
##### [Update Stream]
PATCH/accounts/{account_id}/pipelines/v1/streams/{stream_id}
##### [Delete Stream]
DELETE/accounts/{account_id}/pipelines/v1/streams/{stream_id}
#### Schema Validation

#### Schema ValidationSchemas

##### [List all uploaded schemas]
GET/zones/{zone_id}/schema_validation/schemas
##### [Get details of a schema]
GET/zones/{zone_id}/schema_validation/schemas/{schema_id}
##### [Upload a schema]
POST/zones/{zone_id}/schema_validation/schemas
##### [Edit details of a schema to enable validation]
PATCH/zones/{zone_id}/schema_validation/schemas/{schema_id}
##### [Delete a schema]
DELETE/zones/{zone_id}/schema_validation/schemas/{schema_id}
#### Schema ValidationSettings

##### [Get global schema validation settings]
GET/zones/{zone_id}/schema_validation/settings
##### [Update global schema validation settings]
PUT/zones/{zone_id}/schema_validation/settings
##### [Edit global schema validation settings]
PATCH/zones/{zone_id}/schema_validation/settings
#### Schema ValidationSettingsOperations

##### [List per-operation schema validation settings]
GET/zones/{zone_id}/schema_validation/settings/operations
##### [Get per-operation schema validation setting]
GET/zones/{zone_id}/schema_validation/settings/operations/{operation_id}
##### [Update per-operation schema validation setting]
PUT/zones/{zone_id}/schema_validation/settings/operations/{operation_id}
##### [Bulk edit per-operation schema validation settings]
PATCH/zones/{zone_id}/schema_validation/settings/operations
##### [Delete per-operation schema validation setting]
DELETE/zones/{zone_id}/schema_validation/settings/operations/{operation_id}
#### Token Validation

#### Token ValidationConfiguration

##### [List token validation configurations]
GET/zones/{zone_id}/token_validation/config
##### [Get a single Token Configuration]
GET/zones/{zone_id}/token_validation/config/{config_id}
##### [Create a new Token Validation configuration]
POST/zones/{zone_id}/token_validation/config
##### [Edit an existing Token Configuration]
PATCH/zones/{zone_id}/token_validation/config/{config_id}
##### [Delete Token Configuration]
DELETE/zones/{zone_id}/token_validation/config/{config_id}
#### Token ValidationConfigurationCredentials

##### [Update Token Configuration credentials]
PUT/zones/{zone_id}/token_validation/config/{config_id}/credentials
#### Token ValidationRules

##### [List token validation rules]
GET/zones/{zone_id}/token_validation/rules
##### [Create a token validation rule]
POST/zones/{zone_id}/token_validation/rules
##### [Bulk create token validation rules]
POST/zones/{zone_id}/token_validation/rules/bulk
##### [Bulk edit token validation rules]
PATCH/zones/{zone_id}/token_validation/rules/bulk
##### [Get a zone token validation rule]
GET/zones/{zone_id}/token_validation/rules/{rule_id}
##### [Delete a zone token validation rule]
DELETE/zones/{zone_id}/token_validation/rules/{rule_id}
##### [Edit a zone token validation rule]
PATCH/zones/{zone_id}/token_validation/rules/{rule_id}