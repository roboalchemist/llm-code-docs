# Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/

Title: Configure IS as Key Manager

URL Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/

Markdown Content:
Configure IS as Key Manager - WSO2 API Manager Documentation
===============
- [x] - [x] 

[Skip to content](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#pattern-6-api-m-deployment-with-is-as-key-manager)

[![Image 1: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo.svg)![Image 2: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo-for-light.svg)](https://apim.docs.wso2.com/en/4.6.0/ "WSO2 API Manager Documentation")

 API Manager Documentation 

 Configure IS as Key Manager 

[4.6.0](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#!)
*   [4.6.0](https://apim.docs.wso2.com/en/latest)
*   [4.5.0](https://apim.docs.wso2.com/en/4.5.0)
*   [4.4.0](https://apim.docs.wso2.com/en/4.4.0)
*   [4.3.0](https://apim.docs.wso2.com/en/4.3.0)
*   [4.2.0](https://apim.docs.wso2.com/en/4.2.0)
*   [4.1.0](https://apim.docs.wso2.com/en/4.1.0)
*   [4.0.0](https://apim.docs.wso2.com/en/4.0.0)
*   [3.2.0](https://apim.docs.wso2.com/en/3.2.0)
*   [3.1.0](https://apim.docs.wso2.com/en/3.1.0)
*   [3.0.0](https://apim.docs.wso2.com/en/3.0.0)
*   [Show all](https://apim.docs.wso2.com/en/versions)

[](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/?q= "Share")

 Initializing search 

Get Help 

Report Issues 

[![Image 3: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo.svg)![Image 4: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo-for-light.svg)](https://apim.docs.wso2.com/en/4.6.0/ "WSO2 API Manager Documentation") WSO2 API Manager Documentation  

[wso2/docs-apim * 90 * 584](https://github.com/wso2/docs-apim "Go to repository")

*   [Home](https://apim.docs.wso2.com/en/4.6.0/)
*   - [x] Get Started   Get Started  
    *   [Introduction](https://apim.docs.wso2.com/en/4.6.0/get-started/overview/)
    *   [Key Concepts](https://apim.docs.wso2.com/en/4.6.0/get-started/key-concepts/)
    *   [Quick Start Guide](https://apim.docs.wso2.com/en/4.6.0/get-started/api-manager-quick-start-guide/)
    *   [Architecture](https://apim.docs.wso2.com/en/4.6.0/get-started/apim-architecture/)
    *   - [x]  Deployment Options   Deployment Options  
        *   [Deployment Platforms](https://apim.docs.wso2.com/en/4.6.0/get-started/deployment-platforms/)
        *   [Deployment Patterns](https://apim.docs.wso2.com/en/4.6.0/get-started/deployment-patterns/)

    *   [About this Release](https://apim.docs.wso2.com/en/4.6.0/get-started/about-this-release/)

* * *

*   - [x] Install & Setup   Install & Setup  
    *   [Overview](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install-and-setup-overview/)
    *   - [x]  Install   Install  
        *   [Installation Prerequisites](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installation-prerequisites/)
        *   - [x]  Install the API Manager Runtime   Install the API Manager Runtime  
            *   [Install API-M](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installing-the-product/installing-api-m-runtime/)
            *   [Run API-M](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installing-the-product/running-the-api-m/)
            *   [Run API-M as a Linux Service](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installing-the-product/installing-api-m-as-a-linux-service/)
            *   [Run API-M as a Windows Service](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installing-the-product/installing-api-m-as-a-windows-service/)

        *   [Installation Options](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installation-options/)

    *   - [x]  Setup   Setup  
        *   - [x]  Set up API Manager   Set up API Manager  
            *   [Update WSO2 API Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/updating-wso2-api-manager/)
            *   [Set up Kubernetes Gateway with APIM](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/configuring-apim-as-a-gateway/)
            *   - [x]  Set up a Key Manager   Set up a Key Manager  
                *   [Set up a Third-party Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/configure-a-third-party-key-manager/)
                *   [Set up WSO2 Identity Server as a Resident Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/configuring-wso2-identity-server-as-a-key-manager/)

            *   - [x]  Set up Databases   Set up Databases  
                *   [Overview](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/overview/)
                *   - [x]  Change Default Databases   Change Default Databases  
                    *   [Change to MySQL](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-mysql/)
                    *   [Change to MSSQL](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-mssql/)
                    *   [Change to PostgreSQL](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-postgresql/)
                    *   [Change to Oracle](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-oracle/)
                    *   [Change to IBM DB2](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-ibm-db2/)
                    *   [Change to Oracle RAC](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/changing-default-databases/changing-to-oracle-rac/)

                *   [Manage Data Growth and Improving Performance](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-databases/managing-data-growth-and-improving-performance/)

            *   - [x]  Set up Proxy Server and the Load Balancer   Set up Proxy Server and the Load Balancer  
                *   [Configure the Proxy Server and the Load Balancer](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-proxy-server-and-the-load-balancer/configuring-the-proxy-server-and-the-load-balancer/)
                *   [Add a custom Proxy Path](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/setting-up-proxy-server-and-the-load-balancer/adding-a-custom-proxy-path/)

            *   - [x]  Security   Security  
                *   - [x]  Logins and Passwords   Logins and Passwords  
                    *   [Maintain Logins and Passwords](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/maintaining-logins-and-passwords/)
                    *   - [x]  Secure Passwords   Secure Passwords  
                        *   [Customize Secure Vault](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/carbon-secure-vault-implementation/)
                        *   [Set Passwords Using Environment Variables/System Properties](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/set-passwords-using-vars-and-sys-props/)
                        *   [Work with Encrypted Passwords](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/working-with-encrypted-passwords/)
                        *   [Set Up ReCaptcha](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/setting-up-recaptcha/)
                        *   [Configure reCaptcha for Single Sign On](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/configuring-recaptcha-for-single-sign-on/)
                        *   [Integrate with HashiCorp Vault](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/harshicrop-vault-extension/)

                *   - [x]  Configure Keystores   Configure Keystores  
                    *   [Configure Keystores in API Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/configuring-keystores-in-wso2-api-manager/)
                    *   - [x]  Keystore Basics   Keystore Basics  
                        *   [Create a New Keystore](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/keystore-basics/creating-new-keystores/)
                        *   [Renew a CA Signed Certificate](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/keystore-basics/renewing-a-ca-signed-certificate-in-a-keystore/)
                        *   [About Asymetric Cryptography](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/keystore-basics/about-asymetric-cryptography/)

                *   [Enable HostName Verification](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/enabling-hostname-verification/)
                *   [Enable Java Security Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/enabling-java-security-manager/)
                *   [General Data Protection Regulation (GDPR) for WSO2 API Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/general-data-protection-regulation-gdpr-for-wso2-api-manager/)
                *   [Configure Transport Level Security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-transport-level-security/)
                *   [User Account Management](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/user-account-management/)
                *   [Secure Web Portals](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/securing-api-m-web-portals/)

            *   - [x]  Configure Userstores   Configure Userstores  
                *   [Introduction to User Stores](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/introduction-to-userstores/)
                *   - [x]  Configure Primary User Stores   Configure Primary User Stores  
                    *   [Configure Primary User Stores](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/configure-primary-user-store/configuring-the-primary-user-store/)
                    *   [Configure a JDBC User Store](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/configure-primary-user-store/configuring-a-jdbc-user-store/)
                    *   [Configure a Read-Write LDAP User Store](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/configure-primary-user-store/configuring-a-read-write-ldap-user-store/)
                    *   [Configure a Read-Only LDAP User Store](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/configure-primary-user-store/configuring-a-read-only-ldap-user-store/)
                    *   [Configure a Read-Write Active Directory User Store](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/configure-userstores/configure-primary-user-store/configuring-a-read-write-active-directory-user-store/)

            *   - [x]  SSO   SSO  
                *   [Configure Identity Server As External IDP with OIDC](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/sso/configuring-identity-server-as-external-idp-using-oidc/)
                *   [Configure Identity Server As External IDP with SAML](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/sso/configuring-identity-server-as-external-idp-using-saml/)
                *   [OKTA As An External IDP With OIDC](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/sso/okta-as-an-external-idp-using-oidc/)
                *   [OKTA As An External IDP With SAML](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/sso/okta-as-an-external-idp-using-saml/)

            *   - [x]  Advanced Configurations   Advanced Configurations  
                *   [Change the Default Transport](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/advance-configurations/changing-the-default-transport/)
                *   [Configure Caching](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/advance-configurations/configuring-caching/)
                *   [Customize the Management Console](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/advance-configurations/customizing-the-management-console/)
                *   [Configure the Crypto Provider](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/advance-configurations/configuring-the-crypto-provider/)

    *   - [x]  Deploy   Deploy  
        *   - [x]  Deploy on VMs   Deploy on VMs  
            *   - [x]  All-In-One Deployment   All-In-One Deployment  
                *   [Single Node Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/single-node/configuring-a-single-node/)
                *   [Active-Active Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/single-node/configuring-an-active-active-deployment/)

            *   - [x]  Distributed Deployment   Distributed Deployment  
                *   [Simple Scalable Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/deploying-wso2-api-m-in-a-simple-scalable-setup/)
                *   [Distributed Deployment (Recommended)](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/deploying-wso2-api-m-in-a-distributed-setup/)
                *   [Distributed Deployment with Key Manager Separation](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/distributed-deployment/deploying-wso2-api-m-in-a-distributed-setup-with-km-separated/)

            *   - [x]  Multi-DC Deployment   Multi-DC Deployment  
                *   [Patterns Overview](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/multi-dc-deployment-patterns-overview/)
                *   [Multi-DC Deployment - Pattern 1](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-1/)
                *   [Multi-DC Deployment - Pattern 2](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/multi-dc-deployment/configuring-multi-dc-deployment-pattern-2/)

        *   - [x]  Deploy on Kubernetes   Deploy on Kubernetes  
            *   - [x]  API-M on K8s   API-M on K8s  
                *   [Overview](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/kubernetes-overview/)
                *   - [x]  All-In-One Deployment   All-In-One Deployment  
                    *   [Single Node Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-0-all-in-one/)
                    *   [Active-Active Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-1-all-in-one-ha/)

                *   - [x]  Distributed Deployment   Distributed Deployment  
                    *   [Simple Scalable Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-2-all-in-one-gw/)
                    *   [Distributed Deployment (Recommended)](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-3-acp-tm-gw/)
                    *   [Distributed Deployment with Key Manager Separation](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-4-acp-tm-gw-km/)
                    *   [Simple Scalable Deployment with Key Manager Separation](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-5-all-in-one-gw-km/)
                    *   - [x]  Configure IS as Key Manager  [Configure IS as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/) Table of contents  
                        *   [Contents](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#contents)
                        *   [Prerequisites](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#prerequisites)
                            *   [Set Up Basic Configurations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#set-up-basic-configurations)
                            *   [Build WSO2 Identity Server Docker Image](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#build-wso2-identity-server-docker-image)
                            *   [Configure WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configure-wso2-identity-server-as-key-manager)

                        *   [Minimal Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#minimal-configuration)
                        *   [Further IS Customizations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#further-is-customizations)
                        *   [Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configuration)
                            *   [1. General Configuration of Helm Charts](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#1-general-configuration-of-helm-charts)
                            *   [2. Add WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#2-add-wso2-identity-server-as-key-manager)
                            *   [3. Add a DNS record mapping the hostnames and the external IP](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#3-add-a-dns-record-mapping-the-hostnames-and-the-external-ip)
                            *   [4. Access Management Consoles](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#4-access-management-consoles)

            *   [API-M on Openshift](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/openshift/openshift-deployment-overview/)
            *   [API-M on EKS](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/aws/deploying-wso2-api-m-on-eks/)

        *   - [x]  Deployment Best Practices   Deployment Best Practices  
            *   [Deployment Checklist](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/production-deployment-guidelines/)
            *   [Security Guidelines for a Production Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/)
            *   [Basic Health Checks](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/basic-health-checks/)
            *   [Change the Hostname](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/changing-the-hostname/)
            *   [Change the Default Ports](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/changing-the-default-ports-with-offset/)
            *   [Backup and Recovery](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/backup-recovery/)
            *   - [x]  Performance Tuning   Performance Tuning  
                *   [API-M Performance Tuning](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/tuning-performance/)

    *   [Upgrade](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/upgrading-wso2-api-manager/upgrading-api-manager/)

*   - [x] Tutorials   Tutorials  
    *   [Tutorials Overview](https://apim.docs.wso2.com/en/4.6.0/tutorials/tutorials-overview/)
    *   - [x]  Scenario Tutorials   Scenario Tutorials  
        *   [Scenario Overview](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario-overview/)
        *   [Scenario 1 - Create a REST API from an OpenAPI Definition](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario1-create-rest-api/)
        *   [Scenario 2 - Engage Access Control to the API](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario2-access-control/)
        *   [Scenario 3 - Implement an API](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario3-implementing-an-api/)
        *   [Scenario 4 - Sign Up a New User](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario4-user-signup-approval-flow/)
        *   [Scenario 5 - Get the Developer Community Involved](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario5-developer-community-feature/)
        *   [Scenario 6 - Integrate with Data Sources](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario6-integrating-with-data-sources/)
        *   [Scenario 7 - Analytics](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario7-analytics/)
        *   [Scenario 8 - Rate Limiting](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario8-rate-limiting/)
        *   [Scenario 9 - Realtime Data with WebSocket API](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario9-realtime-data/)
        *   [Scenario 10 - Notifications Using WebHooks](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario10-notifications-webhooks/)
        *   [Scenario 11 - GraphQL Support](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario11-graphql/)
        *   [Scenario 12 - Guaranteed Message Delivery](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario12-message-delivery/)
        *   [Scenario 13 - Integrate with Services via Connectors](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario13-integrate-with-connectors/)
        *   [Scenario 14 - External Key Manager Support](https://apim.docs.wso2.com/en/4.6.0/tutorials/scenarios/scenario14-external-key-manager/)

    *   - [x]  API Management Tutorials   API Management Tutorials  
        *   [Setting Up a Distributed Setup Using the APIM Enterprise Package](https://apim.docs.wso2.com/en/4.6.0/tutorials/create-distributed-setup-using-the-enterprise-package/)
        *   [Integrating API Manager with an External Broker and Gateway](https://apim.docs.wso2.com/en/4.6.0/tutorials/integrating-with-solace/)
        *   [Develop an Integration From a Managed API](https://apim.docs.wso2.com/en/4.6.0/tutorials/develop-an-integration-with-a-managed-api/)
        *   [The Single Control Plane for Multiple Gateways](https://apim.docs.wso2.com/en/4.6.0/tutorials/single-control-plane-for-multiple-gateways/)
        *   [Federated API Gateway Deployment](https://apim.docs.wso2.com/en/4.6.0/tutorials/deploying-apis-to-federated-gateways-with-wso2/)
        *   [Create and Publish a GraphQL API](https://apim.docs.wso2.com/en/4.6.0/tutorials/create-and-publish-a-graphql-api/)
        *   - [x]  Create and Publish a Streaming API   Create and Publish a Streaming API  
            *   [Create and Publish a WebSocket API](https://apim.docs.wso2.com/en/4.6.0/tutorials/streaming-api/create-and-publish-websocket-api/)
            *   [Create and Publish a WebSub/WebHook API](https://apim.docs.wso2.com/en/4.6.0/tutorials/streaming-api/create-and-publish-websub-api/)
            *   [Create and Publish a SSE API](https://apim.docs.wso2.com/en/4.6.0/tutorials/streaming-api/create-and-publish-sse-api/)

        *   [Create and Publish an AWS Lambda API](https://apim.docs.wso2.com/en/4.6.0/tutorials/create-and-publish-awslambda-api/)
        *   [Create and Publish an API with Sequence as a Backend](https://apim.docs.wso2.com/en/4.6.0/tutorials/create-and-publish-a-sequencebackend-api/)
        *   [Expose a SOAP Service as a REST API](https://apim.docs.wso2.com/en/4.6.0/tutorials/expose-a-soap-service-as-a-rest-api/)
        *   [Edit an API by Modifying the API Definition](https://apim.docs.wso2.com/en/4.6.0/tutorials/edit-an-api-by-modifyng-the-api-definition/)
        *   [Enforce Rate Limiting and Resource Access Policies](https://apim.docs.wso2.com/en/4.6.0/tutorials/enforce-throttling-and-resource-access-policies/)

* * *

*   - [x] API Design & Manage   API Design & Manage  
    *   - [x]  Design APIs   Design APIs  
        *   [Design APIs Overview](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/design-api-overview/)
        *   - [x]  Create APIs   Create APIs  
            *   - [x]  REST APIs   REST APIs  
                *   [Create a REST API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-rest-api/create-a-rest-api/)
                *   [Create a REST API from an OpenAPI Definition](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-rest-api/create-a-rest-api-from-an-openapi-definition/)
                *   [Expose a SOAP Service as a REST API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-rest-api/expose-a-soap-service-as-a-rest-api/)
                *   [Generate REST API from SOAP Backend](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-rest-api/generate-rest-api-from-soap-backend/)
                *   [Test a REST API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-rest-api/test-a-rest-api/)

            *   - [x]  GraphQL APIs   GraphQL APIs  
                *   [Create a GraphQL API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-a-graphql-api/)

            *   - [x]  Streaming APIs   Streaming APIs  
                *   [Streaming API Overview](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/streaming-api-overview/)
                *   [Create a WebSocket API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/create-a-websocket-streaming-api/)
                *   [Create a WebSub/WebHook API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/create-a-websub-streaming-api/)
                *   [Create a SSE API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/create-a-sse-streaming-api/)
                *   [Create a Streaming API from an AsyncAPI Definition](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/create-a-streaming-api-from-an-asyncapi-definition/)
                *   [Test a WebSub/WebHook API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-streaming-api/test-a-websub-api/)

            *   [Create an API Using a Service](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-an-api-using-a-service/)
            *   [AI APIs](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-ai-api/create-an-ai-api/)

        *   [Create APIs with AI](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-api-with-ai/)
        *   [Create API Revisions](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/create-api-revisions/)
        *   [Add Custom Properties to APIs](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/adding-custom-properties-to-apis/)
        *   [Change the Thumbnail of an API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api/change-api-thumbnail/)
        *   - [x]  Create Prototype APIs   Create Prototype APIs  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/prototype-api/overview/)
            *   - [x]  Mock Implementation   Mock Implementation  
                *   [With API Gateway](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/prototype-api/create-mocked-js-api/)

            *   [Existing Backend Implementation as a Prototype API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/prototype-api/backend-url-prototype-api/)

        *   - [x]  Create API Products   Create API Products  
            *   [API Product Overview](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api-product/api-product-overview/)
            *   [Create an API Product](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/create-api-product/create-api-product/)

        *   - [x]  Endpoints   Endpoints  
            *   [Endpoint Types](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/endpoint-types/)
            *   - [x]  Endpoint Security   Endpoint Security  
                *   [Basic Auth](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/endpoint-security/basic-auth/)
                *   [Digest Auth](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/endpoint-security/digest-auth/)
                *   [OAuth 2.0](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/endpoint-security/oauth-2.0/)

            *   - [x]  Resiliency   Resiliency  
                *   [Endpoint Timeouts](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/resiliency/endpoint-timeouts/)
                *   [Endpoint Suspension](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/resiliency/endpoint-suspension/)
                *   [Prevent API Suspension](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/resiliency/prevent-api-suspension/)

            *   [High Availability for Endpoints](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/high-availability-for-endpoints/)
            *   [Manage Certificates](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/endpoints/certificates/)

        *   - [x]  Lifecycle Management   Lifecycle Management  
            *   [API Lifecycle](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/lifecycle-management/api-lifecycle/)
            *   [Customize API Life Cycle](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/lifecycle-management/customize-api-life-cycle/)

        *   - [x]  API Versioning   API Versioning  
            *   [Create a New API Version](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-versioning/create-a-new-api-version/)
            *   [Deprecate the Old Version](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-versioning/deprecate-the-old-version/)
            *   [Backward Compatibility](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-versioning/backward-compatibility/)
            *   [Enable Notifications](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-versioning/enabling-notifications/)

        *   - [x]  API Documentation   API Documentation  
            *   [Add API Documentation](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-documentation/add-api-documentation/)
            *   [View Generated Documentation](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-documentation/view-generated-documentation/)

        *   - [x]  API Collaboration   API Collaboration  
            *   [Comment on an API via the Publisher](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-collaborations/comment-on-an-api-via-the-publisher/)
            *   [Enable Social Media Interaction](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-collaborations/enable-social-media-interaction/)

        *   - [x]  API Policies   API Policies  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-policies/overview/)
            *   [Attach Policy](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-policies/attach-policy/)
            *   [Create Policy](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/api-policies/create-policy/)

        *   - [x]  Rate Limiting   Rate Limiting  
            *   [Set API Operation Limits](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/set-api-level-throttling/)
            *   [Protect Backend Services](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/protect-backend-services/)
            *   [Assign Business Plans](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/assign-business-plans/)
            *   - [x]  Set GraphQL Query Limits   Set GraphQL Query Limits  
                *   [Limit Query Complexity](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/graphql-api/query-complexity-analysis/)
                *   [Limit Query Depth](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/graphql-api/query-depth-analysis/)

            *   [Set Streaming API Limits](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/rate-limiting/set-streaming-api-limits/)

        *   - [x]  Advanced Topics   Advanced Topics  
            *   [Enable Publisher Access Control](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/enable-publisher-access-control-in-api-publisher-portal/)
            *   [Control API Visibility and Subscription Availability](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/control-api-visibility-and-subscription-availability-in-developer-portal/)
            *   [Block Subscription to an API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/block-subscription-to-an-api/)
            *   [Disable Subscriptions for an API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/disable-subscriptions-for-an-api/)
            *   [Enabling CORS for APIs](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/enabling-cors-for-apis/)
            *   [Adding an API State Change Workflow](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/adding-an-api-state-change-workflow/)
            *   [Validate API Definitions with Linters](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/design/advanced-topics/validate-api-definitions-with-linters/)
            *   [API Creator/Publisher Governance Capabilities](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/governance/api-governance-api-creator-capabilities/)

    *   - [x]  Deploy and Publish APIs   Deploy and Publish APIs  
        *   - [x]  Deploy on Gateway   Deploy on Gateway  
            *   - [x]  Deploy API   Deploy API  
                *   [Deploy an API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/deploy-on-gateway/deploy-api/deploy-an-api/)
                *   [Expose APIs via Custom Hostnames](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/deploy-on-gateway/deploy-api/exposing-apis-via-custom-hostnames/)
                *   [Deploy Through Multiple API Gateways](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/deploy-on-gateway/deploy-api/deploy-through-multiple-api-gateways/)
                *   [Revision Deployment Workflow](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/deploy-on-gateway/deploy-api/revision-deployment-workflow/)

        *   - [x]  Publish on Developer Portal   Publish on Developer Portal  
            *   [Publish an API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/publish-on-dev-portal/publish-an-api/)
            *   [Add a Third-party API](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/publish-on-dev-portal/third-party-api-support/)
            *   [Publish to Multiple External API Developer Portals](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/publish-on-dev-portal/publish-to-multiple-external-api-stores/)
            *   [Import APIs From AWS API-Gateway to WSO2 API-M](https://apim.docs.wso2.com/en/4.6.0/api-design-manage/deploy-and-publish/publish-on-dev-portal/publish-aws-apis-in-the-dev-portal/)

*   - [x] API Developer Portal   API Developer Portal  
    *   [Publish an API to Developer Portal](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/publish-an-api-to-dev-portal/)
    *   [Consume APIs Overview](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/consume-api-overview/)
    *   - [x]  Discover APIs   Discover APIs  
        *   [Search](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/discover-apis/search/)
        *   [Marketplace Assistant](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/discover-apis/marketplace-assistant/)

    *   - [x]  Manage Applications   Manage Applications  
        *   [Create Application](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/create-application/)
        *   - [x]  Generate Keys   Generate Keys  
            *   [Application Keys](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/generate-keys/generate-api-keys/)

        *   - [x]  Obtain Access Token   Obtain Access Token  
            *   [Overview of Access Tokens](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/generate-keys/obtain-access-token/overview-of-access-tokens/)
            *   [Access Tokens Per Device](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/generate-keys/obtain-access-token/access-tokens-per-device/)
            *   [Change the Default Token Expiration Time](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/generate-keys/obtain-access-token/changing-the-default-token-expiration-time/)
            *   [Revoke OAuth2 Application](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/generate-keys/revoke-oauth2-application/)

        *   [Share Applications](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/sharing-applications/sharing-applications/)
        *   - [x]  Advanced Topics   Advanced Topics  
            *   [Add Custom Attributes to Applications](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/add-custom-attributes-to-applications/)
            *   [Change the Owner of an Application](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/changing-the-owner-of-an-application/)
            *   [Change the Provider of an Api](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/changing-the-provider-of-an-api/)
            *   [Add an Application Creation Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/adding-an-application-creation-workflow/)
            *   [Add an Application Update Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/adding-an-application-update-workflow/)
            *   [Add an Application Key Generation Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-application/advanced-topics/adding-an-application-key-generation-workflow/)

    *   - [x]  Manage Subscriptions   Manage Subscriptions  
        *   [Subscribe to an API](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-subscription/subscribe-to-an-api/)
        *   - [x]  Advanced Topics   Advanced Topics  
            *   [Add an API Subscription Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-subscription/advanced-topics/adding-an-api-subscription-workflow/)
            *   [Add an API Subscription Tier Update Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-subscription/advanced-topics/adding-an-api-subscription-tier-update-workflow/)
            *   [Add an API Subscription Deletion Workflow](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/manage-subscription/advanced-topics/adding-an-api-subscription-deletion-workflow/)

    *   - [x]  Test APIs   Test APIs  
        *   - [x]  Integrated API Console   Integrated API Console  
            *   [Test a REST API](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/invoke-an-api-using-the-integrated-api-console/)
            *   [Test a GraphQL API](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/invoke-an-graphql-api-using-the-integrated-graphql-console/)
            *   [Add Additional Headers to Test a REST API](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/include-additional-headers-in-the-api-console/)

        *   [SOAP Client](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/invoke-an-api-using-a-soap-client/)
        *   [Postman](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/try-out-using-postman/)
        *   [Test APIs with API Chat](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/invoke-apis/invoke-apis-using-tools/test-apis-with-apichat/)

    *   - [x]  Collaborations   Collaborations  
        *   [Interact with the Community](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/collaboration/interact-with-the-community/)

    *   - [x]  Generating SDKs   Generating SDKs  
        *   [Generate SDKs in Developer Portal](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/generating-sdks/generate-sdks-in-dev-portal/)
        *   [Write a Client Application Using the SDK](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/generating-sdks/write-a-client-application-using-the-sdk/)

    *   - [x]  User Account Management   User Account Management  
        *   [Recover Password](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/user-account-management/recover-password/)
        *   [Change Password](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/user-account-management/change-dev-portal-password/)

    *   - [x]  Rate Limiting   Rate Limiting  
        *   [Rate Limiting for App Developers](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/rate-limiting/rate-limiting-for-app-developers/)
        *   [Manage Application Rate Limits](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/rate-limiting/manage-application-rate-limits/)
        *   [Handle Rate Limiting Errors](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/rate-limiting/handle-rate-limiting-errors/)
        *   [Reset Application Throttling Policies](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/rate-limiting/resetting-application-throttling-policies/)

    *   - [x]  B2B API Consumption   B2B API Consumption  
        *   [B2B API Consumption](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/b2b-api-consumption/api-consumption/)
        *   [Setup WSO2 Identity Server as a Federated Authenticator](https://apim.docs.wso2.com/en/4.6.0/api-developer-portal/b2b-api-consumption/setup-identity-server/)

*   - [x] API Security   API Security  
    *   - [x]  Design-Time Security   Design-Time Security  
        *   [Configuring API Security Audit](https://apim.docs.wso2.com/en/4.6.0/api-security/design-time/configuring-api-security-audit/)

    *   - [x]  Runtime Security   Runtime Security  
        *   - [x]  Authentication   Authentication  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/api-authentication-overview/)
            *   [Disable Security](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/disable-security/)
            *   [Secure APIs Using API Keys](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/secure-apis-using-api-keys/)
            *   [Secure APIs Using Basic Authentication](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/secure-apis-using-basic-authentication/)
            *   [Secure APIs Using Mutual SSL](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/secure-apis-using-mutual-ssl/)
            *   [Secure APIs Using OAuth2 Tokens](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/secure-apis-using-oauth2-tokens/)
            *   [Securing APIs Using Certificate Bound Access Tokens](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-authentication/securing-apis-using-certificate-bound-access-tokens/)

        *   - [x]  Authorization   Authorization  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/authorization/api-authorization/)
            *   [Role-based Access Control Using XACML](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/authorization/role-based-access-control-using-xacml/)
            *   [Fine Grained Access Control with OAuth Scopes](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/authorization/oauth2-scopes/fine-grained-access-control-with-oauth-scopes/)
            *   [Application Scopes](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/authorization/oauth2-scopes/application-scopes/)
            *   [Scope Whitelisting](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/authorization/oauth2-scopes/scope-whitelisting/)

        *   - [x]  API Request Response Schema Validation   API Request Response Schema Validation  
            *   [JSON Schema Validator](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/api-request-response-schema-validation/json-schema-validator/)

        *   - [x]  OPA Validation   OPA Validation  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/opa-validation/overview/)
            *   [Custom OPA Policy for Regular Gateway](https://apim.docs.wso2.com/en/4.6.0/api-security/runtime/opa-validation/custom-opa-policy-for-regular-gateway/)

    *   - [x]  Key Management   Key Management  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/key-manager-overview/)
        *   - [x]  Grant Types   Grant Types  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/overview/)
            *   [Password Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/password-grant/)
            *   [Client Credentials Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/client-credentials-grant/)
            *   [Authorization Code Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/authorization-code-grant/)
            *   [Refresh Token Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/refresh-token-grant/)
            *   [JWT Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/jwt-grant/)
            *   [SAML Extension Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/saml-extension-grant/)
            *   [Kerberos OAuth2 Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/kerberos-oauth2-grant/)
            *   [NTLM Grant](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/authentication/grant-types/ntlm-grant/)

        *   - [x]  Tokens   Tokens  
            *   [JWT Tokens](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/jwt-tokens/)
            *   [Token Expiration](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/token-expiration/)
            *   [Token Persistence](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/token-persistence/)
            *   [Token Revocation](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/token-revocation/)
            *   [Encrypting OAuth2 Tokens](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/encrypting-oauth2-tokens/)
            *   [Hashing OAuth Keys](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/hashing-oauth-keys/)
            *   [Multiple Active Access Tokens](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/multiple-active-access-tokens/)
            *   [Securing OAuth Token with HMAC Validation](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/tokens/securing-oauth-token-with-hmac-validation/)

        *   - [x]  Applications   Applications  
            *   [Provisioning Out-of-Band OAuth Clients](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/applications/provisioning-out-of-band-oauth-clients/)
            *   [Federating OAuth Applications](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/applications/federating-oauth-applications/)

        *   - [x]  Identity   Identity  
            *   [Obtain User Profile Information with OpenID Connect](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/identity/obtaining-user-profile-information-with-openid-connect/)

        *   - [x]  Third-Party Key Managers   Third-Party Key Managers  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/overview/)
            *   [Configure WSO2 IS as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-wso2is-connector/)
            *   [Configure WSO2 IS 7.x as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-wso2is7-connector/)
            *   [Configure Keycloak as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-keycloak-connector/)
            *   [Configure Okta as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-okta-connector/)
            *   [Configure Auth0 as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-auth0-connector/)
            *   [Configure PingFederate as A Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-pingfederate-connector/)
            *   [Configure ForgeRock as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-forgerock-connector/)
            *   [Configure the Azure AD as a Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-azure-ad-key-manager/)
            *   [Configure a Custom Key Manager for Out-of-Band Provisioning](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-custom-km-out-of-band/)
            *   [Configure a Custom Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-custom-connector/)
            *   [Configure the Global Key Manager](https://apim.docs.wso2.com/en/4.6.0/api-security/key-management/third-party-key-managers/configure-global-key-manager/)

*   - [x] API Gateway   API Gateway  
    *   - [x]  Universal Gateway   Universal Gateway  
        *   [Overview of the WSO2 Universal Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/overview-of-the-api-gateway/)
        *   [Deploy an API to Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/deploy-api-to-gateway/)
        *   [Response Caching](https://apim.docs.wso2.com/en/4.6.0/api-gateway/response-caching/)
        *   [Pass End User Attributes to the Backend](https://apim.docs.wso2.com/en/4.6.0/api-gateway/passing-enduser-attributes-to-the-backend-via-api-gateway/)
        *   [Gateway Environments](https://apim.docs.wso2.com/en/4.6.0/api-gateway/maintaining-separate-production-and-sandbox-gateways/)
        *   [Scale the Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/scaling-the-gateway/)
        *   - [x]  Advanced Topics   Advanced Topics  
            *   [Universal Gateway with Dedicated Tenants](https://apim.docs.wso2.com/en/4.6.0/api-gateway/maintain-seperate-gateways-per-tenants/)
            *   [Universal Gateways with Dedicated Backends](https://apim.docs.wso2.com/en/4.6.0/api-gateway/api-gateways-with-dedicated-backends/)
            *   [Mutual SSL Between Universal Gateway and Backend](https://apim.docs.wso2.com/en/4.6.0/api-gateway/mutual-ssl-between-api-gateway-and-backend/)
            *   [Storing Custom Synapse Artifacts in the Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/custom-synapse-artifacts/)

        *   - [x]  Gateway Policies   Gateway Policies  
            *   [Adding Dynamic Endpoints](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/adding-dynamic-endpoints/)
            *   [Adding a Class Mediator](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/adding-a-class-mediator/)
            *   [Adding a Non-Blocking Send Operation](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/adding-a-non-blocking-send-operation/)
            *   [Configuring Message Builders Formatters](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/configuring-message-builders-formatters/)
            *   [Disabling Message Chunking](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/disabling-message-chunking/)
            *   [JWT Claim Based Access Validator](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/jwt-claim-based-access-validator/)
            *   [Mapping Backend URLs with Publisher URLs](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/mapping-the-parameters-of-your-backend-urls-with-the-api-publisher-urls/)
            *   [Passing Custom Authorization Token to Backend](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/passing-a-custom-authorization-token-to-the-backend/)
            *   [Removing Specific Request Headers from Response](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/removing-specific-request-headers-from-response/)
            *   [Revoke One Time Tokens Policy](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/revoke-one-time-tokens-policy/)
            *   [Transforming API Message Payload](https://apim.docs.wso2.com/en/4.6.0/api-gateway/policies/transforming-api-message-payload/)
            *   [Global Gateway Policies](https://apim.docs.wso2.com/en/4.6.0/api-gateway/gateway-policies/)

        *   - [x]  Threat Protectors   Threat Protectors  
            *   [Gateway Threat Protectors](https://apim.docs.wso2.com/en/4.6.0/api-gateway/threat-protectors/gateway-threat-protectors-for-api-manager/)
            *   [Regular Expression Threat Protection](https://apim.docs.wso2.com/en/4.6.0/api-gateway/threat-protectors/regular-expression-threat-protection-for-api-gateway/)
            *   [JSON Threat Protection](https://apim.docs.wso2.com/en/4.6.0/api-gateway/threat-protectors/json-threat-protection-for-api-gateway/)
            *   [XML Threat Protection](https://apim.docs.wso2.com/en/4.6.0/api-gateway/threat-protectors/xml-threat-protection-for-api-gateway/)
            *   [Bot Detection](https://apim.docs.wso2.com/en/4.6.0/api-gateway/threat-protectors/bot-detection/)

        *   - [x]  Rate Limiting   Rate Limiting  
            *   [Understand Rate Limit Enforcement](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/understand-rate-limit-enforcement/)
            *   [Enforce GraphQL Query Limits](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/enforce-graphql-query-limits/)
            *   [Enforce Streaming API Limits](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/enforce-streaming-api-limits/)
            *   [Enforce Custom Throttling](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/enforce-custom-throttling/)
            *   [Configure Distributed Burst Control & Backend Rate Limiting](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/configuring-rate-limiting-api-gateway-cluster/)
            *   [Configure Distributed Throttling](https://apim.docs.wso2.com/en/4.6.0/api-gateway/rate-limiting/distributed-throttling/)

    *   - [x]  Federated Gateways   Federated Gateways  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/overview/)
        *   - [x]  AWS   AWS  
            *   [Deploy on AWS API Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/aws/deploy-on-aws-api-gateway/)
            *   [Discover APIs on AWS API Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/aws/discover-apis-on-aws-api-gateway/)

        *   - [x]  Azure   Azure  
            *   [Deploy on Azure API Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/azure/deploy-on-azure-api-gateway/)
            *   [Discover APIs on Azure API Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/azure/discover-apis-on-azure-api-gateway/)

        *   - [x]  EnvoyGateway   EnvoyGateway  
            *   [Discover APIs on Envoy Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/envoygateway/eg-k8s/discover-apis-on-eg-gateway-in-kubernetes/)

        *   - [x]  Kong   Kong  
            *   - [x]  Kong Kubernetes   Kong Kubernetes  
                *   [Discover APIs on Kong Gateway in Kubernetes](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/kong/kong-kubernetes/discover-apis-on-kong-gateway-in-kubernetes/)

            *   - [x]  Kong Standalone   Kong Standalone  
                *   [Discover APIs on Kong Gateway](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/kong/kong-standalone/discover-apis-on-kong-gateway/)

        *   [Configure a Custom Gateway Agent](https://apim.docs.wso2.com/en/4.6.0/api-gateway/federated-gateways/configure-custom-gateway-agent/)

*   - [x] AI Gateway   AI Gateway  
    *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-gateway-overview/)
    *   - [x]  LLM Gateway   LLM Gateway  
        *   [Getting Started](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/getting-started-with-ai-gateway/)
        *   [AI Backend Security](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-backend-security/)
        *   [Rate Limiting](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/rate-limiting/)
        *   - [x]  Multi-Model Routing   Multi-Model Routing  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/multi-model-routing/overview/)
            *   [Load Balancing](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/multi-model-routing/load-balancing/)
            *   [Failover](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/multi-model-routing/failover/)

        *   - [x]  AI Service Provider Management   AI Service Provider Management  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/overview/)
            *   [Anthropic](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/anthropic/)
            *   [AWS Bedrock](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/aws-bedrock/)
            *   [Azure AI Foundry](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/azure-ai-foundry/)
            *   [Azure OpenAI](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/azure-openai/)
            *   [Gemini](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/gemini/)
            *   [Mistral AI](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/mistral-ai/)
            *   [OpenAI](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/openai/)
            *   - [x]  Custom AI Service Providers   Custom AI Service Providers  
                *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/custom-ai-vendors/overview/)
                *   [Custom Connector](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/custom-ai-vendors/custom-connector/)
                *   [Onboarding a Custom AI Service Provider](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-vendor-management/custom-ai-vendors/onboarding-custom-ai-service-provider/)

        *   - [x]  Prompt Management   Prompt Management  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/prompt-management/overview/)
            *   [Prompt Decorator](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/prompt-management/prompt-decorator/)
            *   [Prompt Template](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/prompt-management/prompt-template/)

        *   - [x]  AI Guardrails   AI Guardrails  
            *   [Overview](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/overview/)
            *   [Content Length Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/content-length-guardrail/)
            *   [Regex Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/regex-guardrail/)
            *   [JSON Schema Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/json-schema-guardrail/)
            *   [Sentence Count Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/sentence-count-guardrail/)
            *   [URL Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/url-guardrail/)
            *   [Word Count Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/word-count-guardrail/)
            *   [Semantic Prompt Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/semantic-prompt-guardrail/)
            *   [PII Masking with Regex](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/regex-pii-masking/)
            *   [Azure Content Safety](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/azure-content-safety/)
            *   [AWS Bedrock Guardrail](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/aws-bedrock-guardrail/)
            *   [Guardrail Error Response](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/ai-guardrails/guardrail-error-response/)

        *   [Semantic Caching](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/semantic-caching/)
        *   [AI APIs via SDKs](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/using-proxy-apis-in-sdks/)

    *   - [x]  MCP Gateway   MCP Gateway  
        *   [Getting Started](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/overview/)
        *   [Create from an OpenAPI Definition](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/create-from-openapi/)
        *   [Create from an Existing API](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/create-from-api/)
        *   [Proxy an Existing MCP Server](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/create-from-mcp-server/)
        *   [Update and Deploy a MCP Server](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/update-and-deploy-mcp-server/)
        *   [Subscribe to a MCP Server](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/subscribe-to-a-mcp-server/)
        *   [Consume MCP Servers from MCP Hub](https://apim.docs.wso2.com/en/4.6.0/ai-gateway/mcp-gateway/invoke-a-mcp-server-using-playground/)

*   - [x] API Analytics & Monetization   API Analytics & Monetization  
    *   - [x]  API Analytics   API Analytics  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/analytics-overview/)
        *   [Moesif Analytics](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/moesif-analytics/moesif-integration-guide/)
        *   - [x]  Other Analytics Solutions   Other Analytics Solutions  
            *   [ELK Based Analytics Installation Guide](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/on-prem/elk-installation-guide/)
            *   [Datadog Analytics Installation Guide](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/on-prem/datadog-installation-guide/)
            *   [OpenSearch Analytics Installation Guide](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/on-prem/opensearch-installation-guide/)
            *   - [x]  Choreo Based Analytics   Choreo Based Analytics  
                *   [Architecture](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/choreo-analytics/api-analytics-architecture/)
                *   [Getting Started Guide](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/choreo-analytics/getting-started-guide/)
                *   [Role-based Access Control](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/choreo-analytics/role-based-access-control/)
                *   [Alerts](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/choreo-analytics/configure-alerts/)
                *   [Choreo Based Analytics via Proxy](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/choreo-analytics/choreo-based-analytics-via-proxy/)

        *   [Publish Analytics Events to External Systems](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/samples/publishing-analytics-events-to-external-systems/)
        *   [Publish Custom Analytics Events Data](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-analytics/samples/publishing-custom-analytics-data/)

    *   - [x]  API Monetization   API Monetization  
        *   [Monetize an API](https://apim.docs.wso2.com/en/4.6.0/monitoring/api-monetization/monetizing-an-api/)

    *   - [x]  Observability   Observability  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/observability-overview/)
        *   - [x]  Logs   Logs  
            *   [Configure Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/configuring-logging/)
            *   [Correlation Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-correlation-logs/)
            *   [HTTP Access Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-http-access-logs/)
            *   [Audit Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-audit-logs/)
            *   [API Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-api-logs/)
            *   [Websocket Logs](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-websocket-logs/)
            *   - [x]  External Observability Solutions   External Observability Solutions  
                *   [OpenSearch](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/monitoring-with-opensearch/)

        *   - [x]  Traces   Traces  
            *   [OpenTracing](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/traces/monitoring-with-opentracing/)
            *   [OpenTelemetry](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/traces/monitoring-with-opentelemetry/)

        *   - [x]  Metrics   Metrics  
            *   [JMX-Based Monitoring](https://apim.docs.wso2.com/en/4.6.0/monitoring/observability/metrics/jmx-based-monitoring/)

*   - [x] Administration   Administration  
    *   [Overview](https://apim.docs.wso2.com/en/4.6.0/administer/admin-overview/)
    *   - [x]  Manage Users and Roles   Manage Users and Roles  
        *   [Introduction to User Management](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/introduction-to-user-management/)
        *   - [x]  Manage Users for API Manager   Manage Users for API Manager  
            *   [Manage User Roles](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-roles/)
            *   [Manage Users](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-users/)
            *   [Manage Role Permissions](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-permissions/)
            *   [Manage Users for Admin Portal](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-users-for-admin-portal/)

    *   - [x]  Manage User Stores   Manage User Stores  
        *   [Introduction to User Stores](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-stores/introduction-to-userstores/)
        *   [Configure Secondary User Stores](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-stores/configuring-secondary-user-stores/)
        *   [Write a Custom User Store Manager](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-stores/writing-a-custom-user-store-manager/)
        *   [Configure the Authorization Manager](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-stores/configuring-the-authorization-manager/)

    *   - [x]  API Manager Multitenancy   API Manager Multitenancy  
        *   [Introduction to Multitenancy](https://apim.docs.wso2.com/en/4.6.0/administer/multitenancy/introduction-to-multitenancy/)
        *   [Manage Tenants](https://apim.docs.wso2.com/en/4.6.0/administer/multitenancy/managing-tenants/)
        *   [Configure the Tenant Loading Policy](https://apim.docs.wso2.com/en/4.6.0/administer/multitenancy/configuring-the-tenant-loading-policy/)
        *   [Tenant Sharing with WSO2 Identity Server 7.x](https://apim.docs.wso2.com/en/4.6.0/administer/multitenancy/tenant-sharing-with-wso2is7/)

    *   - [x]  Monitoring API Manager   Monitoring API Manager  
        *   [Server Health](https://apim.docs.wso2.com/en/4.6.0/administer/logging-and-monitoring/monitoring/monitoring-server-health/)

    *   - [x]  Multiple Gateways   Multiple Gateways  
        *   [Configure a Gateway](https://apim.docs.wso2.com/en/4.6.0/administer/multiple-gateways/configure-gateway/)
        *   [Configure Gateway Visibility](https://apim.docs.wso2.com/en/4.6.0/administer/multiple-gateways/configure-gateway-visibility/)

    *   [Advanced Configurations](https://apim.docs.wso2.com/en/4.6.0/administer/advanced-configurations/)
    *   [Manage Role based access control for the Admin portal](https://apim.docs.wso2.com/en/4.6.0/administer/role-based-access-control/)
    *   - [x]  Rate Limiting   Rate Limiting  
        *   [Manage Subscription Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/manage-subscription-policies/)
        *   [Manage AI Subscription Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/manage-ai-subscription-policies/)
        *   [Manage Application Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/manage-application-policies/)
        *   [Manage Advanced Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/manage-advanced-policies/)
        *   [Manage Deny Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/manage-deny-policies/)
        *   [Implement Custom Policies](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/implement-custom-policies/)
        *   [Change Default Tiers](https://apim.docs.wso2.com/en/4.6.0/administer/rate-limiting/change-default-tiers/)

    *   - [x]  Governance   Governance  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/administer/governance/overview/)
        *   [Concepts](https://apim.docs.wso2.com/en/4.6.0/administer/governance/governance-concept/)
        *   [Administrative Capabilities](https://apim.docs.wso2.com/en/4.6.0/administer/governance/api-governance-admin-capabilities/)
        *   [CI/CD-Driven Governance](https://apim.docs.wso2.com/en/4.6.0/administer/governance/api-governance-cicd/)

    *   [Publisher Portal in Read Only Mode](https://apim.docs.wso2.com/en/4.6.0/administer/publisher-portal-in-read-only-mode/)

*   - [x] APIOps   APIOps  
    *   - [x]  CI/CD   CI/CD  
        *   [CI/CD for APIs - Overview](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/ci-cd-with-wso2-api-management/)
        *   [Build a CI/CD Pipeline for APIs Using the CLI](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/cicd-using-cli/)
        *   [Build a CI/CD Pipeline for APIs using Jenkins](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/building-jenkins-ci-cd-pipeline/)

    *   - [x]  CLI   CLI  
        *   [Getting Started with WSO2 API Controller (apictl)](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/getting-started-with-wso2-api-controller/)
        *   [API Governance CLI Tool](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/api-governance-cli-tool/)
        *   - [x]  Manage APIs and API Products   Manage APIs and API Products  
            *   [Manage APIs and API Products](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-apis-api-products/managing-apis-and-api-products/)
            *   [Import APIs Via Dev First Approach](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-apis-api-products/importing-apis-via-dev-first-approach/)
            *   [Migrate APIs to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-apis-api-products/migrating-apis-to-different-environments/)
            *   [Migrate API Products (with or without Dependent APIs) to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-apis-api-products/migrating-api-products-to-different-environments/)

        *   - [x]  Manage MCP Servers   Manage MCP Servers  
            *   [Manage MCP Servers](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-mcp-servers/managing-mcp-servers/)
            *   [Import MCP Servers Via Dev First Approach](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-mcp-servers/importing-mcp-servers-via-dev-first-approach/)
            *   [Migrate MCP Servers to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-mcp-servers/migrating-mcp-servers-to-different-environments/)

        *   - [x]  Manage Applications   Manage Applications  
            *   [Manage Applications](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-applications/managing-applications/)
            *   [Migrate Apps to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-applications/migrating-applications-to-different-environments/)

        *   - [x]  Manage Rate Limiting Policies   Manage Rate Limiting Policies  
            *   [Manage Rate Limiting Policies](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-rate-limiting-policies/throttle-policy-import-export/)
            *   [Migrate Rate Limiting Policies to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-rate-limiting-policies/migrating-rate-limiting-policies-to-different-environments/)

        *   - [x]  Manage Common API Policies   Manage Common API Policies  
            *   [Manage Common API Policies](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-common-api-policies/managing-common-api-policies/)
            *   [Migrate Common API Policies to Different Environments](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/managing-common-api-policies/migrating-common-api-policies-to-different-environments/)

        *   [Encrypt Secrets with apictl](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/encrypting-secrets-with-ctl/)
        *   [Enable Correlation Logs with apictl](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/enabling-correlation-logs-with-apictl/)
        *   [AI Related Operations with apictl](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/ai-related-operations-with-apictl/)
        *   - [x]  Advanced Topics   Advanced Topics  
            *   [Create Custom Users to Perform apictl Operations](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/creating-custom-users-to-perform-api-controller-operations/)
            *   [Configure Environment Specific Parameters](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/configuring-environment-specific-parameters/)
            *   [Use Dynamic Data in apictl Projects](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/using-dynamic-data-in-api-controller-projects/)
            *   [Configure Different Endpoint Types](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/configuring-different-endpoint-types/)
            *   [Configuring Different Endpoint Security Types](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/configuring-different-endpoint-security-types/)
            *   [Format the Outputs of Get Commands](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/formatting-the-output-of-get-command/)
            *   [Configure Git Integration](https://apim.docs.wso2.com/en/4.6.0/apiops/cli/advanced-topics/configuring-git-integration/)

* * *

*   - [x] Reference   Reference  
    *   - [x]  Product REST APIs   Product REST APIs  
        *   [Overview](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/overview/)
        *   - [x]  Publisher APIs   Publisher APIs  
            *   [Publisher API v4](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/publisher-apis/publisher-v4/publisher-v4/)

        *   - [x]  Developer Portal APIs   Developer Portal APIs  
            *   [Developer Portal API v3](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/devportal-apis/devportal-v3/devportal-v3/)

        *   - [x]  Admin APIs   Admin APIs  
            *   [Admin API v4](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/admin-apis/admin-v4/admin-v4/)

        *   - [x]  Gateway APIs   Gateway APIs  
            *   [Gateway API v2](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/gateway-apis/gateway-v2/gateway-v2/)

        *   - [x]  Service Catalog APIs   Service Catalog APIs  
            *   [Service Catalog API v1](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/service-catalog-apis/service-catalog-v1/service-catalog-v1/)

        *   - [x]  DevOps APIs   DevOps APIs  
            *   [DevOps API v0](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/devops-apis/devops-v0/devops-v0/)

        *   - [x]  Governance APIs   Governance APIs  
            *   [Governance API v1](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/governance-apis/governance-v1/governance-v1/)

        *   [Advanced Configurations](https://apim.docs.wso2.com/en/4.6.0/reference/product-apis/advanced-configurations/)

    *   - [x]  Product Configurations   Product Configurations  
        *   [Understand the New Configuration Model](https://apim.docs.wso2.com/en/4.6.0/reference/understanding-the-new-configuration-model/)
        *   [API-M Config Catalog](https://apim.docs.wso2.com/en/4.6.0/reference/config-catalog/)

    *   [API Controller (APICTL)](https://apim.docs.wso2.com/en/4.6.0/reference/apictl/wso2-api-controller/)
    *   - [x]  Governance   Governance  
        *   [Rule Validator](https://apim.docs.wso2.com/en/4.6.0/reference/governance/rule-validator/rule-validator/)
        *   - [x]  Ruleset Catalog   Ruleset Catalog  
            *   [WSO2 API Management Guidelines](https://apim.docs.wso2.com/en/4.6.0/reference/governance/wso2-api-management-guidelines/)
            *   [WSO2 REST API Design Guidelines](https://apim.docs.wso2.com/en/4.6.0/reference/governance/wso2-rest-api-design-guidelines/)
            *   [OWASP Top 10](https://apim.docs.wso2.com/en/4.6.0/reference/governance/owasp-top-10/)

        *   [API YAML Representation](https://apim.docs.wso2.com/en/4.6.0/reference/governance/api-yaml-representation/)
        *   [API Documentation YAML Representation](https://apim.docs.wso2.com/en/4.6.0/reference/governance/api-doc-yaml-representation/)

    *   - [x]  Customizations   Customizations  
        *   [Vendor Specific Extensions](https://apim.docs.wso2.com/en/4.6.0/reference/vendor-extensions-catalog/)
        *   - [x]  Extend WSO2 API Manager   Extend WSO2 API Manager  
            *   - [x]  Extend Key Management   Extend Key Management  
                *   [Extend Key Validation](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-key-management/extending-key-validation/)
                *   [Extend Scope Validation](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-key-management/extending-scope-validation/)
                *   [Extend Key Manager](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-key-management/extending-the-key-manager-interface/)
                *   [Write Custom Grant Types](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-key-management/writing-custom-grant-types/)

            *   - [x]  Extend API Gateway   Extend API Gateway  
                *   [Customize API Template](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-gateway/customizing-api-template-for-gateway/)
                *   [Write Custom Handlers](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-gateway/writing-custom-handlers/)

            *   - [x]  Extend Workflows   Extend Workflows  
                *   [Invoke the API Manager from the BPEL Engine](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/invoking-the-api-manager-from-the-bpel-engine/)
                *   [Customize a Workflow Extension](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/customizing-a-workflow-extension/)
                *   [Configure HTTP Redirection for Workflows](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/configuring-http-redirection-for-workflows/)
                *   [Configure Workflows for Tenants](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/configuring-workflows-for-tenants/)
                *   [Configure Workflows in a Cluster](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/configuring-workflows-in-a-cluster/)
                *   [Change the Default User Role in Workflows](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/changing-the-default-user-role-in-workflows/)
                *   [Clean Up Workflow Tasks](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/extending-workflows/cleaning-up-workflow-tasks/)

            *   - [x]  SAML2 SSO   SAML2 SSO  
                *   [Configure Single Sign On with SAML2](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/saml2-sso/configuring-single-sign-on-with-saml2/)
                *   [Configure External IDP Through Identity Server for SSO](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/saml2-sso/configuring-external-idp-through-identity-server-for-sso/)
                *   [Configure Identity Server as IDP for SSO](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/saml2-sso/configuring-identity-server-as-idp-for-sso/)
                *   [Multi Factor Authentication for Publisher and Developer Portals](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/extending-api-manager/saml2-sso/multi-factor-authentication-mfa-for-publisher-and-developer-portals/)

        *   - [x]  Customizations   Customizations  
            *   - [x]  Customize the Developer Portal   Customize the Developer Portal  
                *   [Override the Developer Portal Theme](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/overriding-developer-portal-theme/)
                *   - [x]  Customize API Listing   Customize API Listing  
                    *   [API Category based Grouping](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/customize-api-listing/api-category-based-grouping/)
                    *   [Change Default View](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/customize-api-listing/change-default-view/)

                *   [Enable or Disable API Detail Tabs](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enabling-or-disabling-api-detail-tabs/)
                *   [Override API Overview Page per API](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/override-api-overview-page-per-api/)
                *   [Enable or Disable Rating](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enable-or-disable-rating/)
                *   [Enable or Disable Home Page](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enable-or-disable-home-page/)
                *   [Enable or Disable Tag Cloud](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enable-or-disable-tag-cloud/)
                *   [Enable or Disable Footer](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enable-or-disable-footer/)
                *   [Enable or Disable Banner](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enable-or-disable-banner/)
                *   [Styling API Details Left Menu](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/styling-api-details-left-menu/)
                *   [Styling the Logo and Header](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/styling-the-logo-and-header/)
                *   [Enable or Disabling Self Signup](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/enabling-or-disabling-self-signup/)
                *   [Configure reCaptcha for Self-SignUp](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-the-developer-portal/configuring-recaptcha-for-self-signup/)

            *   [Override the Publisher Portal Theme](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/overriding-the-publisher-portal-theme/)
            *   [Log in to the Developer Portal Using Social Media](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/log-in-to-the-dev-portal-using-social-media/)
            *   [Directing the Root Context to the Developer Portal](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/directing-the-root-context-to-the-developer-portal/)
            *   [Customize User Signup in Developer Portal](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-user-signup-in-developer-portal/)
            *   [Customize Login Pages for Developer Portal and Publisher](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customizing-login-pages-for-dev-portal-and-publisher/)
            *   [Customize the Developer Portal and Gateway URLs for Tenants](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/customize-the-api-store-and-gateway-urls-for-tenants/)
            *   [Add a User Signup Workflow](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/adding-a-user-signup-workflow/)
            *   [Add internationalization](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/adding-internationalization/)
            *   [Define Custom Linter Rules](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/define-custom-linters/)
            *   [Advanced UI Customization](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/advanced-ui-customization/)
            *   [Modify Workflow Approval Task Limit](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/modify-workflow-approval-task-limit/)
            *   [Implementing a Custom Validation Engine](https://apim.docs.wso2.com/en/4.6.0/reference/customize-product/customizations/implementing-a-custom-validation-engine/)

        *   [Admin Services](https://apim.docs.wso2.com/en/4.6.0/reference/wso2-admin-services/)
        *   [Work with the Source Code](https://apim.docs.wso2.com/en/4.6.0/reference/working-with-the-source-code/)
        *   [Java Documentation](https://apim.docs.wso2.com/en/4.6.0/reference/java-documentation/)

    *   - [x]  Best Practices   Best Practices  
        *   [WSO2 API-M Best Practices](https://apim.docs.wso2.com/en/4.6.0/reference/wso2-api-manager-best-practices/)
        *   [Best Practices for Working with Endpoints](https://apim.docs.wso2.com/en/4.6.0/reference/best-practices-endpoints/)

    *   [Accessibility Compliance](https://apim.docs.wso2.com/en/4.6.0/reference/accessibility-compliance/)
    *   - [x]  Guides   Guides  
        *   [Message Flow in the API Manager Gateway](https://apim.docs.wso2.com/en/4.6.0/reference/guides/message-flow-in-the-api-manager-gateway/)
        *   [Accessing API Manager by Multiple Devices Simultaneously](https://apim.docs.wso2.com/en/4.6.0/reference/guides/accessing-api-manager-by-multiple-devices-simultaneously/)
        *   [admin_Directory Structure of WSO2 Products](https://apim.docs.wso2.com/en/4.6.0/reference/guides/directory-structure-of-wso2-products/)

    *   [Common Runtime and Configuration Artifacts](https://apim.docs.wso2.com/en/4.6.0/reference/common-runtime-and-configuration-artifacts/)
    *   [Default Product Ports](https://apim.docs.wso2.com/en/4.6.0/reference/default-product-ports/)
    *   [Product Compatibility](https://apim.docs.wso2.com/en/4.6.0/reference/product-compatibility/)
    *   - [x]  Performance Test Results   Performance Test Results  
        *   [API Manager](https://apim.docs.wso2.com/en/4.6.0/reference/performance-tests-results/)
        *   [Token Persistence](https://apim.docs.wso2.com/en/4.6.0/reference/performance-test-results-token-persistence/)

    *   [Supported Cipher Suites](https://apim.docs.wso2.com/en/4.6.0/reference/supported-cipher-suites/)
    *   - [x]  Troubleshooting   Troubleshooting  
        *   [Error Handling](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/error-handling/)
        *   [Capturing System Data in Error Situations](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/capturing-system-data-in-error-situations/)
        *   [Troubleshooting in Production Environments](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/admin-troubleshooting-in-production-environments/)
        *   [Utilizing Runtime Diagnostic Tool](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/utilizing-runtime-diagnostic-tool/)
        *   [Cleaning Up Partially Created Keys](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/cleaning-up-partially-created-keys/)
        *   [Configure XSLT Mediation with Xalan](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/configuring-xslt-mediation-with-xalan/)
        *   [Troubleshooting 'Registered callback does not match with the provided url' error](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/troubleshooting-invalid-callback-error/)
        *   [Troubleshooting JMS](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/troubleshooting-jms/)
        *   [Troubleshooting WebSocket APIs](https://apim.docs.wso2.com/en/4.6.0/reference/troubleshooting/troubleshooting-websocket-api/)

    *   [FAQ](https://apim.docs.wso2.com/en/4.6.0/reference/faq/)

 Table of contents  
*   [Contents](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#contents)
*   [Prerequisites](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#prerequisites)
    *   [Set Up Basic Configurations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#set-up-basic-configurations)
    *   [Build WSO2 Identity Server Docker Image](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#build-wso2-identity-server-docker-image)
    *   [Configure WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configure-wso2-identity-server-as-key-manager)

*   [Minimal Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#minimal-configuration)
*   [Further IS Customizations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#further-is-customizations)
*   [Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configuration)
    *   [1. General Configuration of Helm Charts](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#1-general-configuration-of-helm-charts)
    *   [2. Add WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#2-add-wso2-identity-server-as-key-manager)
    *   [3. Add a DNS record mapping the hostnames and the external IP](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#3-add-a-dns-record-mapping-the-hostnames-and-the-external-ip)
    *   [4. Access Management Consoles](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#4-access-management-consoles)

[](https://github.com/wso2/docs-apim/edit/4.6.0/en/docs/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km.md "Edit this page")[](https://github.com/wso2/docs-apim/raw/4.6.0/en/docs/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km.md "View source of this page")
Pattern 6: API-M Deployment with IS as Key Manager[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#pattern-6-api-m-deployment-with-is-as-key-manager "Permanent link")
========================================================================================================================================================================================================================================================

This deployment consists of a single API-M node with a single API-M runtime with IS configured as a third party key manager.

Contents[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#contents "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Pattern 6: API-M Deployment with IS as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#pattern-6-api-m-deployment-with-is-as-key-manager)
*   [Contents](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#contents)
*   [Prerequisites](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#prerequisites)
    *   [Set Up Basic Configurations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#set-up-basic-configurations)
    *   [Build WSO2 Identity Server Docker Image](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#build-wso2-identity-server-docker-image)
    *   [Configure WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configure-wso2-identity-server-as-key-manager)

*   [Minimal Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#minimal-configuration)
*   [Further IS Customizations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#further-is-customizations)
*   [Configuration](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configuration)
    *   [1. General Configuration of Helm Charts](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#1-general-configuration-of-helm-charts)
        *   [1.1 Add Ingress Controller](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#11-add-ingress-controller)
        *   [1.2 Mount Keystore and Truststore](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#12-mount-keystore-and-truststore)
        *   [1.3 Encrypting Secrets](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#13-encrypting-secrets)
        *   [1.4 Configure Docker Image and Databases](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#14-configure-docker-image-and-databases)
        *   [1.5 Configure SSL in Service Exposure](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#15-configure-ssl-in-service-exposure)

    *   [2. Add WSO2 Identity Server as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#2-add-wso2-identity-server-as-key-manager)
    *   [3. Add a DNS Record Mapping the Hostnames and the External IP](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#3-add-a-dns-record-mapping-the-hostnames-and-the-external-ip)
    *   [4. Access Management Consoles](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#4-access-management-consoles)

Prerequisites[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#prerequisites "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Before you begin, ensure you have the following prerequisites in place:

### Set Up Basic Configurations[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#set-up-basic-configurations "Permanent link")

Info

The following tools and configurations are necessary for deploying WSO2 API-M in a Kubernetes environment.

1.   Install the required tools:
2.   [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3.   [Helm](https://helm.sh/docs/intro/install/)
4.   [Kubernetes client](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

5.   Ensure you have a running [Kubernetes cluster](https://kubernetes.io/docs/setup/).

6.   Install the [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/).

7.   Add the WSO2 Helm chart repository:

```
helm repo add wso2 https://helm.wso2.com && helm repo update
``` 

### Build WSO2 Identity Server Docker Image[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#build-wso2-identity-server-docker-image "Permanent link")

*   This deployment pattern uses WSO2 Identity Server 7.x as a third-party Key Manager.
*   Download the WSO2 Identity Server Docker image from [DockerHub](https://hub.docker.com/r/wso2/wso2is) or use the [WSO2 Private Docker Registry](https://docker.wso2.com/) if you have an active WSO2 subscription.
*   Since WSO2 IS 7.x needs to be configured as a Key Manager for WSO2 API Manager, you need to create a custom Docker image with the necessary configurations and extensions.
*   Below is a sample Dockerfile to build a custom WSO2 IS image for use as a Key Manager:

```
FROM docker.wso2.com/wso2is:7.0.0.0

ARG USER=wso2carbon
ARG USER_HOME=/home/${USER}
ARG WSO2_SERVER_NAME=wso2is
ARG WSO2_SERVER_VERSION=7.0.0
ARG WSO2_SERVER=${WSO2_SERVER_NAME}-${WSO2_SERVER_VERSION}
ARG WSO2_SERVER_HOME=${USER_HOME}/${WSO2_SERVER}

# Add notification event handler JAR for API Manager integration
ADD --chown=wso2carbon:wso2 https://maven.wso2.org/nexus/content/repositories/releases/org/wso2/km/ext/wso2is/wso2is.notification.event.handlers/2.0.5/wso2is.notification.event.handlers-2.0.5.jar ${WSO2_SERVER_HOME}/repository/components/dropins
```

*   After building your custom Docker image, push it to your container registry so it can be accessed by your Kubernetes cluster: ```
docker build -t CONTAINER_REGISTRY/wso2is-km:7.0.0.0 .
docker push CONTAINER_REGISTRY/wso2is-km:7.0.0.0
``` 

### Configure WSO2 Identity Server as Key Manager[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configure-wso2-identity-server-as-key-manager "Permanent link")

This section explains how to configure WSO2 Identity Server 7.x as a Key Manager for WSO2 API Manager. In this deployment pattern, both API Manager and Identity Server run as separate containerized applications in the Kubernetes cluster.

Info

Before you begin: You need to import the public certificate of the WSO2 Identity Server 7.x to the truststore of the WSO2 API Manager, and vice-versa. For information on importing the certificates, see the [Importing certificates to the truststore](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/keystore-basics/creating-new-keystores/#step-3-importing-certificates-to-the-truststore) guide.

To configure WSO2 Identity Server 7.x to work as a Key Manager with WSO2 API Manager, you need to apply the following configurations:

1.   Configure WSO2 Identity Server using the Helm chart's values.yaml file:

```
deploymentToml:
      extraConfigs: |
        [oauth]
        authorize_all_scopes = true

        [[resource.access_control]]
        context="(.*)/scim2/Me"
        secure=true
        http_method="GET"
        cross_tenant=true
        permissions=[]
        scopes=[]

        [[event_listener]]
        id = "token_revocation"
        type = "org.wso2.carbon.identity.core.handler.AbstractIdentityHandler"
        name = "org.wso2.is.notification.ApimOauthEventInterceptor"
        order = 1
        [event_listener.properties]
        notification_endpoint = "https://<APIM_HOST>:<APIM_PORT>/internal/data/v1/notify"
        username = "${admin.username}"
        password = "${admin.password}"
        'header.X-WSO2-KEY-MANAGER' = "WSO2-IS"
```

Minimal Configuration[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#minimal-configuration "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to quickly try out WSO2 API Manager with WSO2 Identity Server 7.x as a Key Manager on Kubernetes with minimal configuration, you can use the default values provided in the `default_values.yaml` file.

Quick Start Configuration

This minimal configuration includes:

*   H2 database (embedded)
*   Default keystore and truststore
*   Basic settings for testing purposes

**Note:** This configuration is ideal for development environments or quick evaluation but is not recommended for production use.

Before you begin

You need to import the public certificate of the WSO2 Identity Server 7.x to the truststore of the WSO2 API Manager, and vice-versa. For information on importing the certificates, see the Importing certificates to the truststore guide.

Follow the steps in the [1.2 Mount Keystore and Truststore](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#12-mount-keystore-and-truststore) section to create a Kubernetes secret containing the keystore and truststore files. Here you will need two keystores: one for the API Manager and one for the Identity Server. The truststore should contain the public certificate of the Identity Server.

*   To add external keystores and truststores to IS, you can enable `externalJKS` and define the `secretName`
*   To add external keystores and truststores to API Manager, you can specify `jksSecretName`

*   First download the IS values.yaml

```
helm show values wso2/identity-server --version next > default_values.yaml
``` 
*   Update the IS `default_values.yaml` file with the above configurations.

*   Deploy IS with minimal configuration using the following command:

```
helm install is wso2/identity-server --version next \
-f default_values.yaml
```

*   Deploy API Manager with minimal configuration using the following command:

```
helm install apim wso2/wso2am-all-in-one --version 4.6.0-1 -f https://raw.githubusercontent.com/wso2/helm-apim/4.6.x/docs/am-pattern-0-all-in-one/default_values.yaml
```

Once the service is up and running, make sure you have the NGINX Ingress Controller deployed by following the steps outlined in the [Add Ingress Controller](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#11-add-ingress-controller) section.

For this pattern, you will need to deploy both API Manager and Identity Server in your Kubernetes cluster. Configure the values files for both API Manager and Identity Server with the necessary settings and deploy them using Helm.

Further IS Customizations[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#further-is-customizations "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For advanced deployment scenarios and further customizations of WSO2 Identity Server on Kubernetes, refer to the [official WSO2 Identity Server Kubernetes deployment documentation](https://is.docs.wso2.com/en/next/deploy/deploy-is-on-kubernetes/). This guide covers topics such as:

*   Customizing Helm chart values for production
*   Enabling persistence and external databases
*   Integrating with external identity providers
*   Configuring monitoring and logging
*   Scaling and high availability options

Review these resources to tailor your deployment to your specific requirements and production standards.

Configuration[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#configuration "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. General Configuration of Helm Charts[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#1-general-configuration-of-helm-charts "Permanent link")

The Helm charts for the API Manager deployment are available in the [WSO2 Helm Chart Repository](https://github.com/wso2/helm-apim/tree/4.6.x). You can either use the charts from the repository or clone the repository and use the charts from the local copy.

Resource Naming Convention

The helm naming convention for APIM follows a simple pattern:

```
<RELEASE_NAME>-<CHART_NAME>-<RESOURCE_NAME>
```

#### 1.1 Add Ingress Controller

The recommendation is to use [**NGINX Ingress Controller**](https://kubernetes.github.io/ingress-nginx/deploy/) suitable for your cloud environment or local deployment. Some sample annotations that could be used with the ingress resources are as follows.

*   The ingress class should be set to nginx in the ingress resource if you are using the NGINX Ingress Controller.
*   Following are some of the recommended annotations to include in the helm charts for ingresses. These may vary depending on the requirements. Please refer to the [documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/) for more information about the annotations.

```
ingressClass: "nginx"
ingress:
  tlsSecret: ""
  ratelimit:
    enabled: false
    zoneName: ""
    burstLimit: ""
  controlPlane:
    hostname: "am.wso2.com"
    annotations:
      nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
      nginx.ingress.kubernetes.io/affinity: "cookie"
      nginx.ingress.kubernetes.io/session-cookie-name: "route"
      nginx.ingress.kubernetes.io/session-cookie-hash: "sha1"
```  - You need to create a kubernetes secret including the certificate and the private key and include the name of the secret in the helm charts. This will be used for TLS termination in load balancer level by the ingress controller. Please refer to the [documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/#tls) for more information. ```
kubectl create secret tls my-tls-secret --key <private key filename> --cert <certificate filename>
``` 

#### 1.2 Mount Keystore and Truststore

*   If you are not including the keystore and truststore into the docker image, you can mount them using a Kubernetes secret. Following steps shows how to mount the keystore and truststore using a Kubernetes secret.
*   Create a Kubernetes secret with the keystore and truststore files. The secret should contain the primary keystore file, secondary keystore file, internal keystore file, and the truststore file. Note that the secret should be created in the same namespace in which you will be setting up the deployment.
*   Make sure to use the same secret name when creating the secret and when configuring the helm chart.
*   If you are using a different keystore file name and alias, make sure to update the helm chart configurations accordingly. In addition to the primary, internal keystores and truststore files, you can also include the keystores for HTTPS transport as well.
*   Refer the following sample command to create the secret and use it in the APIM.

```
kubectl create secret generic apim-keystore-secret --from-file=wso2carbon.jks --from-file=client-truststore.jks --from-file=wso2internal.jks -n <namespace>
```

> By default, this deployment uses the default keystores and truststores provided by the relevant WSO2 product. For advanced details with regards to managing custom Java keystores and truststores in a container based WSO2 product deployment please refer to the [official WSO2 container guide](https://github.com/wso2/container-guide/blob/master/deploy/Managing_Keystores_And_Truststores.md).

#### 1.3 Encrypting Secrets

*   If you need to use cipher tool to encrypt the passwords in the secret, first you need to encrypt the passwords using the cipher tool. The cipher tool can be found in the bin directory of the product pack. The following command can be used to encrypt the password. ```
sh cipher-tool.sh -Dconfigure
``` 
*   Also the apictl can be used to encrypt password as well. Reference can be found in [following](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/api-controller/encrypting-secrets-with-ctl/).
*   Then the encrypted values should be filled in the relevant fields of values.yaml.
*   Since internal keystore password is required to resolve the encrypted value in runtime, we need to store the value in the cloud provider's secret manager. You can use the cloud provider's secret store to store the password of the internal keystore. The following section can be used to add the cloud provider's credentials to fetch the internal keystore password. Configuration for aws can be at as below. ```
internalKeystorePassword:
  # -- AWS Secrets Manager secret name
  secretName: ""
  # -- AWS Secrets Manager secret key
  secretKey: ""
``` 
> Please note that currently AWS, Azure and GCP Secrets Managers are only supported for this.

#### 1.4 Configure Docker Image and Databases

*   Add the following configurations to reflect the docker image created previously in the helm chart.

```
wso2:
  deployment:
    image:
      imagePullSecrets:
        enabled: false
        username: ""
        password: ""        
      registry: ""
      repository: ""
      digest: ""
``` 
> If you are using a **private Docker registry**, you must enable `imagePullSecrets.enabled` and provide the username and password. - Provide the database configurations under the following section.

```
wso2:
  apim:
    configurations:
      databases:
        apim_db:
          url: ""
          username: ""
          password: ""
        shared_db:
          url: ""
          username: ""
          password: ""
```  - If you need to change the hostnames, update them under the Kubernetes ingress section. - Update the keystore passwords in the security section of the `values.yaml` file. - Review the descriptions of other configurations and modify them as needed to meet your requirements. A simple deployment can be achieved using the basic configurations provided in the `values.yaml` file. All configuration options for each Helm chart are documented in their respective component guides: - [All-in-one](https://github.com/wso2/helm-apim/blob/main/all-in-one/README.md) - [Universal Gateway](https://github.com/wso2/helm-apim/blob/main/distributed/gateway/README.md) - Update the admin credentials in the configuration directory. ```
# -- Super admin username
  adminUsername: ""
  # -- Super admin password
  adminPassword: ""
``` 

#### 1.5 Configure SSL in Service Exposure

SSL Configuration Best Practices

For WSO2 recommended best practices in configuring SSL when exposing internal services to outside of the Kubernetes cluster, refer to the [official WSO2 container guide](https://github.com/wso2/container-guide/blob/master/route/Routing.md#configuring-ssl).

Proper SSL configuration is critical for securing API traffic and maintaining compliance with security standards.

### 2. Add WSO2 Identity Server as Key Manager[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#2-add-wso2-identity-server-as-key-manager "Permanent link")

After setting up WSO2 Identity Server 7.x, you need to configure API Manager to use it as a Key Manager:

1.   Access the API Manager Admin Portal: `https://<API-M-HOSTNAME>:9443/admin`

2.   Navigate to **Key Managers** and click **Add Key Manager**.

3.   Configure the Key Manager with the following settings:

| Field | Value |
| --- | --- |
| Name | WSO2IS7 |
| Display Name | WSO2 Identity Server 7 |
| Key Manager Type | WSO2 Identity Server 7 |
| Well-known URL | https://wso2is.km:9443/oauth2/token/.well-known/openid-configuration |
| Issuer | https://wso2is.km:9443/oauth2/token |
| Client Registration Endpoint | https://wso2is.km:9443/api/identity/oauth2/dcr/v1.1/register |
| Introspection Endpoint | https://wso2is.km:9443/oauth2/introspect |
| Token Endpoint | https://wso2is.km:9443/oauth2/token |
| Display Token Endpoint | https://wso2is.km:9443/oauth2/token |
| Revoke Endpoint | https://wso2is.km:9443/oauth2/revoke |
| Display Revoke Endpoint | https://wso2is.km:9443/oauth2/revoke |
| UserInfo Endpoint | https://wso2is.km:9443/scim2/Me |
| Authorize Endpoint | https://wso2is.km:9443/oauth2/authorize |
| Scope Management Endpoint | https://wso2is.km:9443/api/identity/oauth2/v1.0/scopes |
| Certificate Type | JWKS |
| JWKS URL | https://wso2is.km:9443/oauth2/jwks |
| Username (connector config) | admin |
| Password (connector config) | admin |
| WSO2 Identity Server 7 API Resource Management Endpoint | https://wso2is.km:9443/api/server/v1/api-resources |
| WSO2 Identity Server 7 Roles Endpoint | https://wso2is.km:9443/scim2/v2/Roles |
| Create roles in WSO2 Identity Server 7 | Enable if needed |

1.   For all these configurations to work correctly in Kubernetes, you must ensure proper service discovery between API Manager and Identity Server pods. Configure the necessary Kubernetes services and ingresses to enable communication between these components.

2.   Update your Helm chart values to include the Identity Server deployment and services along with API Manager.

Note

When using WSO2 IS 7.x as a Key Manager, note the following limitations: - Tenancy is not supported. - WSO2 IS 7.x cannot be set up as a Resident Key Manager. It can only be set up as a Third-party Key Manager. - Role creation in WSO2 Identity Server 7.x is supported from WSO2 API Manager 4.4.0.5 update level onwards.

### 3. Add a DNS record mapping the hostnames and the external IP[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#3-add-a-dns-record-mapping-the-hostnames-and-the-external-ip "Permanent link")

Obtain the external IP (EXTERNAL-IP) of the API Manager Ingress resources, by listing down the Kubernetes Ingresses.

```
kubectl get ing -n <NAMESPACE>
```

If the defined hostnames (in the previous step) are backed by a DNS service, add a DNS record mapping the hostnames and the external IP (`EXTERNAL-IP`) in the relevant DNS service.

If the defined hostnames are not backed by a DNS service, for the purpose of evaluation you may add an entry mapping the hostnames and the external IP in the `/etc/hosts` file at the client-side.

```
<EXTERNAL-IP> <kubernetes.ingress.management.hostname> <kubernetes.ingress.gateway.hostname> <kubernetes.ingress.websub.hostname> <kubernetes.ingress.websocket.hostname>
```

### 4. Access Management Consoles[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#4-access-management-consoles "Permanent link")

*   API Manager Publisher: `https://<kubernetes.ingress.management.hostname>/publisher`

*   API Manager DevPortal: `https://<kubernetes.ingress.management.hostname>/devportal`

*   API Manager Carbon Console: `https://<kubernetes.ingress.management.hostname>/carbon`

*   Universal Gateway: `https://<kubernetes.ingress.gateway.hostname>`

*   Identity Server Management Console: `https://<kubernetes.ingress.is.hostname>/carbon`

*   Universal Gateway: `https://<kubernetes.ingress.gateway.hostname>`

*   Identity Server Management Console: `https://<kubernetes.ingress.is.hostname>/carbon`

[Back to top](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/#)

### Join our Discord

Connect with our community on our official Discord server. Share ideas, get help, and be a part of the awesome conversations!

[Join Discord](https://discord.com/invite/wso2)

Got a tough question? [Ask on Stackoverflow](https://stackoverflow.com/questions/tagged/wso2-apim?tab=Newest)

Want to contribute? [Head over to GitHub](https://github.com/wso2/docs-apim)

Like to stay updated? [Follow us on X (Formerly Twitter)](https://twitter.com/intent/follow?screen_name=wso2)

Prefer video tutorials? [Subscribe to our YouTube Channel](https://www.youtube.com/user/WSO2TechFlicks)

 © 2024-2026 [WSO2](https://wso2.com/) LLC. | Content licensed under [CC By 4.0](https://creativecommons.org/licenses/by/4.0). | Sample code licensed under [Apache 2.0](http://www.apache.org/licenses/).
