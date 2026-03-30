# Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/

Title: Security Guidelines for a Production Deployment

URL Source: https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/

Markdown Content:
Security Guidelines for a Production Deployment - WSO2 API Manager Documentation
===============
- [x] - [x] 

[Skip to content](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#security-guidelines-for-production-deployment)

[![Image 1: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo.svg)![Image 2: logo](https://apim.docs.wso2.com/en/4.6.0/assets/images/logo-for-light.svg)](https://apim.docs.wso2.com/en/4.6.0/ "WSO2 API Manager Documentation")

 API Manager Documentation 

 Security Guidelines for a Production Deployment 

[4.6.0](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#!)
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

[](https://apim.docs.wso2.com/en/latest/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/?q= "Share")

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
                    *   [Configure IS as Key Manager](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/kubernetes/am-pattern-6-all-in-one-is-as-km/)

            *   [API-M on Openshift](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/openshift/openshift-deployment-overview/)
            *   [API-M on EKS](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/kubernetes-deployment/aws/deploying-wso2-api-m-on-eks/)

        *   - [x]  Deployment Best Practices   Deployment Best Practices  
            *   [Deployment Checklist](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/production-deployment-guidelines/)
            *   - [x]  Security Guidelines for a Production Deployment  [Security Guidelines for a Production Deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/) Table of contents  
                *   [Runtime-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#runtime-level-security)
                    *   [API-M runtime security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#api-m-runtime-security)

                *   [OS-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#os-level-security)
                *   [Network-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#network-level-security)
                *   [Configure client authentication](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#configure-client-authentication)
                    *   [Enable HTTP Strict Transport Security (HSTS) Headers](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#enable-http-strict-transport-security-hsts-headers)

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
*   [Runtime-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#runtime-level-security)
    *   [API-M runtime security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#api-m-runtime-security)

*   [OS-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#os-level-security)
*   [Network-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#network-level-security)
*   [Configure client authentication](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#configure-client-authentication)
    *   [Enable HTTP Strict Transport Security (HSTS) Headers](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#enable-http-strict-transport-security-hsts-headers)

[](https://github.com/wso2/docs-apim/edit/4.6.0/en/docs/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment.md "Edit this page")[](https://github.com/wso2/docs-apim/raw/4.6.0/en/docs/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment.md "View source of this page")
Security Guidelines for Production Deployment[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#security-guidelines-for-production-deployment "Permanent link")
=====================================================================================================================================================================================================================================================

Given below are the common security guidelines for deploying a WSO2 API Manager in a **production environment**.

In addition, see the [production deployment checklist](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/production-deployment-guidelines) and any other product-specific guidelines in the respective product's documentation.

*   [Runtime-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#runtime-level-security)
*   [OS-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#os-level-security)
*   [Network-level security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#network-level-security)

Runtime-level security[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#runtime-level-security "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Given below are the security guidelines for the API-M runtime.

### API-M runtime security[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#api-m-runtime-security "Permanent link")

Given below are the security guidelines for the API-M runtime.

| **Guideline** | **Details** |
| --- | --- |
| Apply security updates | Apply all the security patches relevant to your product version. Use WSO2 Updates to get the latest security patches. * See [WSO2 Updates](https://updates.docs.wso2.com/en/latest/updates/overview/) for details. **Note the following:** * WSO2 releases security patch notifications monthly via the Support Portal. However, WSO2 issues patches immediately to customers if there are highly critical issues. * WSO2 does not issue patches publicly for older product versions. Community users are encouraged to use the latest product version to receive all the security issues resolved until that particular product release. |
| Change default keystores | Change the default key stores and create new keys for all the cryptographic operations.WSO2 products, by default, come with a self-signed SSL key. As these keys are public, it is recommended to configure your own keys for security purposes. Consider the following guidelines when creating the keystores: * Select a key size of at least 2048 bits. * Use an SHA256 certificate. * Make sure that WSO2 default certificates do not exist in any of the keystores in your production environment. For example, be sure to delete the default public certificate in the default trust store that is shipped with the product. For more information on recommendations for using keystores in WSO2 products, see [About Asymmetric Cryptography](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/keystore-basics/about-asymetric-cryptography/). For information on how to create and configure your own keys and keystores, see [Creating New Keystores](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-keystores/configuring-keystores-in-wso2-api-manager/). |
| Encrypt passwords in configuration files | WSO2 products use a tool called **Secure Vault** to encrypt the plain-text passwords in configuration files. See [Encrypting Passwords in Configuration Files](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/working-with-encrypted-passwords/) for instructions. |
| Change default ports | For information on all the default ports used by WSO2 API Manager, see [Default Product Ports](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/reference/default-product-ports/). For example, the default HTTPS port is 9443 and the HTTP port is 9763. In addition, Axis2 services are exposed over the following ports: 8243 and 8280. For information on changing a default port, see [Changing the Default Ports with Offset](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/changing-the-default-ports-with-offset). |
| Enable **read-only access** to external user stores (LDAPs etc.) | If your product runtimes are connecting to an external user store, such as Microsoft Active Directory for the purpose of reading and retrieving user information, be sure to enable read-only access to that user store. See [Configuring a Read-Only LDAP User Store](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-stores/configure-primary-user-store/configuring-a-read-only-ldap-user-store/) for the API-M runtime. |
| Always communicate (with external user stores) over TLS | All connections from your WSO2 API Manager to external databases, userstores(LDAP), or other services, should be over TLS to ensure adequate network-level protection. Therefore, be sure to use external systems (user stores, databases) that are TLS-enabled. |
| Connect to data stores using a less privileged user | When connecting the server to external databases or user stores (LDAP), be sure to go through a user who does not have permission to change the data store's schema. Be sure not to use the root user of the data store because all permissions are generally granted to the root user. |
| Configure strong HTTP(S) security | To have strong transport-level security, disable SSL protocol versions and enable only TLS protocol versions: TLS 1, TLS 1.1, and TLS 1.2. This can be done by replacing the `sslProtocol = "TLS"` property with `protocols="+TLSv1, +TLSv1.1, +TLSv1.2, +TLSv1.3"` under `[transport.https.sslHostConfig.properties]` in the `deployment.toml` file. You can configure multiple TLS versions or a single TLS version according to your preference. To achieve high security, use the latest TLS version by removing `+TLSv1`, `+TLSv1.1`, and `+TLSv1.2` from the protocols `property` of the configuration. In addition, configure strong ciphers for `ThriftAuthenticationService`, Tomcat transport, and PassThrough transport in the `deployment.toml` file. See the following links for instructions: * [Configuring Transport Level Security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-transport-level-security/) * [Supported Cipher Suites](https://apim.docs.wso2.com/en/4.6.0/reference/supported-cipher-suites/) **Note :** * When deciding on the TLS protocol and the ciphers, consider the compatibility with existing client applications. Imposing maximum security might cause functional problems with client applications. * Apply ciphers with 256 bit key length if you have applied the "Unlimited" strength policy. Note that an unlimited strength policy is recommended. * Also, consider the following factors when deciding on the ciphers: * DES/3DES are deprecated and should not be used. * MD5 should not be used due to known collision attacks. * RC4 should not be used due to analytical cryptographic attacks. * DSS is limited to a small 1024 bit key size. * Cipher-suites that do not provide Perfect Forward Secrecy/ Forward Secrecy (PFS/FS). * GCM based ciphers are recommended over CBC ciphers. |
| Remove weak ciphers for PassThrough transport | Remove any weak ciphers from the PassThrough transport and ensure that the server does not accept connections using those weak ciphers. For this, `PreferredCiphers` should be configured for the PassThrough transport in the `deployment.toml`file (stored in the `<PRODUCT_HOME>/repository/conf/` directory). For more information, see [Configuring Transport Level Security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-transport-level-security/). |
| Update the HTTP Response header "Server" value | By default, all WSO2 products pass "WSO2 Carbon Server" as the server value in HTTP headers when sending HTTP responses. This means that information about the WSO2 product stack is exposed through HTTP responses. It is recommended to change this by configuring the server name for relevant connectors via `deployment.toml`. For more information, see [Configuring Transport Level Security](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/configuring-transport-level-security/). |
| Enabling HTTP Strict Transport Security Headers (HSTS) | Be sure that HTTP Strict Transport Security (HSTS) is enabled for all the applications deployed in your server. This includes the management console, and any other web applications and/or Jaggery applications. Note that (for WSO2 products based on Carbon 4.4.11 or later versions, which implies API-M 2.1.0 and newer) HSTS is disabled for the applications with which the product is shipped by default. This is because HSTS validation can interrupt the development processes by validating signatures of self-signed certificates. To enable HSTS please follow the instructions [Enable HTTP Strict Transport Security (HSTS) Headers](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#enable-http-strict-transport-security-hsts-headers). |
| Preventing browser caching | If there are dynamic pages in your application with sensitive information, you need to prevent browser caching. This can be done by making sure that the applications deployed in your server return the relevant HTTP response headers. Note that cache prevention headers are enabled for the applications with which the product is shipped by default. Therefore, you need to manually enable cache prevention headers only for all the new applications that you deploy in your server. |
| Increase Ephemeral Diffie-Hellman Key size | Before starting the server, open the product startup script (`api-manager.sh` in Linux and `api-manager.bat` in Windows) and enter the following with the other Java properties: `-Djdk.tls.ephemeralDHKeySize=2048 \` |
| Disable client-initiated renegotiation | Before starting the server, open the product startup script (`api-manager.sh` in Linux and `api-manager.bat` in Windows) and enter the following with the other Java properties: `-Djdk.tls.rejectClientInitiatedRenegotiation=true \` |
| Enable HostName Verification | If your product is using Carbon Kernel 4.4.17 or a later version (which implies API-M 2.2.0 and newer), make sure that hostname verification is enabled in the product startup script(`api-manager.sh` in Linux and `api-manager.bat` in Windows)with the **Strict** mode. If it is not, you need to enable it as below: `-Dhttpclient.hostnameVerifier=Strict \` In Carbon versions prior to 4.4.17, be sure that hostname verification is enabled by setting the following property to `false`. `-Dorg.wso2.ignoreHostnameVerification=false \` For instructions, see [Enabling HostName Verification](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/enabling-hostname-verification/). |
| Increase JSESSIONID length | If required, increase the session ID length by changing the `sessionIDLength` attribute of the session manager in the `context.xml` file(stored in the `<PRODUCT_HOME>/repository/conf/tomcat/context.xml` directory) as shown below. The default value is 16 bytes. `<Manager className="org.wso2.carbon.webapp.mgt.CarbonTomcatSessionManager" sessionIdLength="16"></Manager>` |
| Change default admin credentials | The Administrator account is configured by default. The default user name and password of the administrator account is "admin". To change the administrator credentials, you need to first sign in to the management console of the API-M server as "admin", and then use the **Change Password** option under **Home->Configure->User Management->Users** in the navigator. For more information on how to change the password of the administrator in the API-M server, see [Changing the super admin credentials](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/security/logins-and-passwords/maintaining-logins-and-passwords/#change-the-super-admin-credentials). |
| Restrict access to the management console | Make sure that the permission for signing into the management console is granted only to the users that need to use the management console.For example, the majority of users only need to login to the connected service providers via the WSO2 product. Therefore, such users should not have permission to log into the management console. You need to make sure that only administrative users have access to the product's management console. Further, instead of granting all permission to one administrator, you can distribute the responsibilities among administrators by assigning different permissions for conducting various tasks. For instructions, see [Managing User Roles](https://apim.docs.wso2.com/en/4.6.0/administer/managing-users-and-roles/managing-user-roles/). |
| Enable log rotation and monitoring | Ensure that you have a relevant log rotation scheme to manage logs. Log4J properties for WSO2 products can be configured in the `<PRODUCT_HOME>/repository/conf/log4j2.properties` file. Rollover based on a time period can be configured by changing the below configuration (Default value is 1 day). `appender.CARBON_LOGFILE.policies.time.interval = 1` You can also configure rollover based on log file size, and also it is possible to limit the number of backup files. For details on how to configure log rotation and manage log growth details in the API-M runtime, see [Managing log growth](https://apim.docs.wso2.com/en/4.6.0/administer/logging-and-monitoring/logging/managing-log-growth/). |
| Prevent log forging | Log forging can be identified by appending a UUID to the log message. The conversion character '%u' can be used in the pattern layout to log a UUID. For example, the log pattern can be set as following for `AUDIT` logs so that the UUID is printed at the beginning of each log record. `appender.AUDIT_LOGFILE.layout.pattern = [%u] TID: [%tenantId] [%d] %5p {%c} - %m%ex%n` For more information on configuring logging, see [Setting up logging in API Manage](https://apim.docs.wso2.com/en/4.6.0/administer/logging-and-monitoring/logging/configuring-logging/). |
| Set appropriate JVM parameters | The recommended JDK version is JDK 8 or 11. For more information, see [Tested Operating Systems and JDKs](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/reference/product-compatibility/#tested-operating-systems-and-jdks). You do not need to set the Heap and Permgen values for the JVM from JDK 1.8 onwards as the `MaxPermSize` value has been removed from Hotspot JVM. |
| Restrict outbound connections of Publisher node | In an API-M deployment, it is recommended to restrict outbound connections of the Control Plane node (which contains the Publisher) and only allow access to the internal nodes (only to the nodes that the Publisher portal is intended to communicate with) of the deployment. Therefore, even if a situation arises where privileged user credentials are exposed to a user with malicious intent, such users will not be able to exploit and perform any unintended network interactions. See the [API-M deployment](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-overview) documentation for details. |
| Use a separate admin user account to login into the system | WSO2 recommends that you use two separate admin user accounts in production - one account for logging into the system and the other one as the system user doing configurations (for internal service communications). For more information regarding admin user accounts, see [super admin configurations](https://apim.docs.wso2.com/en/4.6.0/reference/config-catalog/#super-admin-configurations). |
| Defining callback URL regular expression | For password recovery, you can define a regular expression to validate the callback URL. The default configuration allows any callback URL. Note that if you are using the recovery option, it is highly recommended to define the regular expression that validates and only allows access to specific callback URLs. See the [Callback URL Regular Expressions](https://is.docs.wso2.com/en/6.1.0/deploy/security/product-level-security-guidelines/#callback-url-regular-expressions) documentation for details. |
| Configure client authentication | Client authentication is used to identify the application or client making a request to the WSO2 API Manager REST APIs. By default, web applications provided with WSO2 API Manager use a set of default credentials for authentication. However, it is recommended to change these default credentials to enhance security. For more details see, [Configure client authentication](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#configure-client-authentication) |
| Disable Try-It Tool | This feature enables users to invoke external web services through API-M. However, in a production environment, it is strongly recommended to disable this functionality to mitigate potential security risks. To do so, add the following configuration to the `deployment.toml` file: ``` [system.parameter] tryItFunctionalityDisabled = true ``` |
| Restrict Access to Java classes and Java Methods/Native Objects in Scripts | JS scripts can be used inside script mediators (eg: in Mock Endpoints) to access Java classes, methods and native objects. By default, all the classes are visible to these scripts. However, it is recommended to restrict access to these. **Limiting Access to Java Classes** Access to Java Classes can be restricted by providing the following configurations in `deployment.toml`. ``` [synapse_properties] 'limit_java_class_access_in_scripts.enable'=true 'limit_java_class_access_in_scripts.list_type' = "ALLOW_LIST" # or BLOCK_LIST 'limit_java_class_access_in_scripts.class_prefixes' = "java.util" ``` Only the Java classes having names starting with any of the values given under `limit_java_class_access_in_scripts.class_prefixes` will be allowed, when `limit_java_class_access_in_scripts.list_type` is `ALLOW_LIST` (all other classes will not be allowed). Likewise, when `limit_java_class_access_in_scripts.list_type` is `BLOCK_LIST`, classes with matching names will be selectively blocked. **Limiting Access to Java Methods/Native Objects** Access to Java Methods/Native Objects can be restricted by providing the following configurations in `deployment.toml`. ``` [synapse_properties] 'limit_java_native_object_access_in_scripts.enable'=true 'limit_java_native_object_access_in_scripts.list_type' = "BLOCK_LIST" # Or "ALLOW_LIST" 'limit_java_native_object_access_in_scripts.object_names' = "getClassLoader" ``` Java methods/native objects having names equal to any of the values given under `limit_java_native_object_access_in_scripts.object_names`, will be selectively blocked when `limit_java_native_object_access_in_scripts.list_type` is `BLOCK_LIST` (all other classes will be allowed). Likewise, when `limit_java_native_object_access_in_scripts.list_type` is `ALLOW_LIST`, classes with matching names will be selectively allowed. **Recommended Approach for Restricting Access** It is recommended to use an Allow List approach for both class and method access restrictions, as it provides a more secure method of permitting only the required classes and methods to be used in the script, while blocking all others by default. The following `ALLOW_LIST` configuration is the recommended baseline to enable the API mocking feature. If you have any script mediator-related use cases with classes included in the prefixes list, adjust it according to your requirements. ``` [synapse_properties] 'limit_java_class_access_in_scripts.enable' = true 'limit_java_class_access_in_scripts.list_type' = "ALLOW_LIST" 'limit_java_class_access_in_scripts.class_prefixes' = "org.apache.synapse.mediators.bsf.CommonScriptMessageContext,java.lang.String" ``` |
| Configuring Case-Sensitive User Stores | If you are using a **case-sensitive** user store, it is important to configure the Developer Portal to handle usernames in a case-sensitive manner. This ensures consistent username handling across components and prevents potential cross-user data sharing. Add the following configuration to the `deployment.toml` file: ``` [apim.devportal] login_username_case_insensitive = false ``` |

OS-level security[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#os-level-security "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section provides the list of OS-level security guidelines for your production environment.

| Guideline | Details |
| --- | --- |
| Run WSO2 processes with a specific OS-level user | Use a separate OS-level user to run WSO2 products. Make sure that the user is only granted the permissions required for running the product for that particular user. Do not use the root/administrator user of your OS because the root/administrator is granted all privileges by default. |
| Minimize software to avoid vulnerability | Make sure that you only install the software/packages that are relevant to your WSO2 product's deployment. Also, continuously monitor the software that you install. For information on the minimum software that your WSO2 product will need, see [Installation Prerequisites](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/install/installation-prerequisites/#system-requirements). |
| Enable the Firewall | Enable a firewall at the OS level (for example, [iptables](https://help.ubuntu.com/community/IptablesHowTo)). This will provide protection for inbound and outbound connections of your WSO2 product. Make sure that you only open the required outbound and inbound ports from the OS-level firewall. |
| Restrict access to TCP ports used for clustering | Apply a firewall at the host-level to disallow access to TCP ports used for clustering (port 4000, 4001, … by default) from unrecognized hosts. These ports should be accessible only from other members of the WSO2 product cluster. |
| Use Secure Shell(SSH) | Use Secure Shell (SSH) when interacting with servers and executing commands. Adhere to the following best practices when you configure SSH: * Change the default SSH port to a higher value. * Disable the root or administrator. * Enable login with user keys. * Display a legal banner or a security banner with security warnings before SSH authentication. |
| Keep the system up-to-date | If there are security updates available for the packages installed in your OS (including the Java runtime), be sure to perform the necessary testing in a staging environment, and then proceed to install them for your OS. |
| Monitor user activities | Monitor the activities of your OS users. You can do this by enabling OS-level logs and by reviewing them regularly. You can also set up a centralized log monitoring system for this purpose. |
| Session Data Cleanup | **Note:** This security guideline is only applicable to WSO2 API Manager. In a production environment, there is a possibility for a deadlock or a database lock to occur when running a session data cleanup task in high load scenarios. To mitigate this, configure the following property to clean data in chunks. Configure this property in the file under `session_data` with the required chunk size. This value is in the number of records and depends on the database type and server capacity. It also depends on the amount of load generated by single sign-on (SSO).A higher value increases the chances of deadlocks and a lower value increases the time it takes for a cleanup. ``` [session_data] cleanup.clean_expired_session_data_in_chunks_of = 8192 ``` For more information on configuring sessions in production, see [Authentication Session Persistence](https://is.docs.wso2.com/en/5.10.0/learn/authentication-session-persistence/) in the WSO2 API Manager documentation. |
| Make regular backups | Make sure to back up important files and archive them continuously. For more information, see [Backup and Recovery Recommendations](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/backup-recovery). |

Network-level security[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#network-level-security "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section provides a list of security guidelines for configuring the network.

| **Guideline** | **Details** |
| --- | --- |
| Create a failover setup | In the cloud native deployment, high-availability should be achieved via the container orchestration system (e.g., Kubernetes ). In a VM deployment, there should be at least two nodes with the failover configuration. When your servers are clustered, you need to regularly monitor the health of your server instances. For example, you need to monitor resource-level factors such as the server's resource utilization, response time anomalies, and the number of incoming network connections.Server monitoring will help you identify when additional server instances (failover instances) are required. You can also make decisions about network routing changes that you need to do in order to avoid server downtime. |
| Maintain network-level logging | Be sure to maintain and monitor logs for your proxy servers, load balancers, and other network devices. |
| Check open ports and services | Periodically check for open ports using port scanning tools and make sure that only the necessary ports are open to both internal and external networks. Be sure that only the ports relevant to your WSO2 products are open for communication. If there are other ports started, be sure to monitor them. For the full list of ports in all WSO2 products, see [Default Product Ports](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/reference/default-product-ports/). |
| Configure device-level security | All your network devices should be periodically checked for anomalies. For example, you need to verify routing tables and firewall rules. Also, make sure that the default credentials are changed before the first use of those devices. |
| Apply firmware updates | Firmware updates for your network devices should be applied regularly. |
| **Note:**This security guideline is applicable to the API-M runtime. Block the `/services` and `/carbon` contexts from the DMZ | Access to the "/services" and "/carbon" contexts should be blocked from the DMZ level (i.e., from the proxy server, load balancer and/or firewall). * The "/services" context is used in WSO2 products to expose admin services. These admin services are used for performing administrative operations using SOAP requests. * The "/carbon" context is used in WSO2 products to expose the management console (administration console) of the product. The management console is a user interface for performing some of the administrative operations of a product. * In addition to the "/services" and "/carbon" contexts, be sure to expose only the required applications in your product to users beyond the DMZ level in your network. **Note:** It is recommended to use an allowlisting approach when allowing access to resources in your product from the DMZ level. For the API-M Developer Portal, exposing the following paths would be sufficient: * https://<host>:<port>/devportal * https://<host>:<port>/devportal/* * https://<host>:<port>/api/am/devportal/v3/* * https://<host>:<port>/oauth2/* * https://<host>:<port>/oidc/* * https://<host>:<port>/authenticationendpoint/* * https://<host>:<port>/logincontext * https://<host>:<port>/oauth2/authorize * https://<host>:<port>/commonauth * https://<host>:<port>/accountrecoveryendpoint/* |

Configure client authentication[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#configure-client-authentication "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Client authentication is used to identify the application or the client that is making the request. The web applications provided out of the box use a set of default credentials to authenticate with WSO2 API Manager REST APIs that are marked as **secure** under the `ResourceAccessControl` tag of the `<APIM_HOME>/repository/conf/identity/identity.xml` file.

Follow the steps below to change the default credentials.

1.   Shut the server down in case you have already started it.

2.   Add the following configuration changes to the `<APIM_HOME>/repository/conf/deployment.toml` file.

    *   Add the `app_password` property and enter a preferred password as the value.

```
[identity.auth_framework.endpoint] 
app_password="<value of preferred password>"
``` 
    *   Add the `hash` property and enter the SHA-256 hash value of the `app_password` as the property value.

```
[account_recovery.endpoint.auth]
hash="<SHA-256 hash of the newly added app_password property value>"
``` 
    *   If the `authenticationendpoint` web app is hosted externally, follow the instructions given below.

a. Open the `EndpointConfig.properties` file found in the root of the `authenticationendpoint` folder.

b. Change the `app.password` property value to the value added as `app_password` in the `deployment.toml` file.

c. Do the same changes to the `EndpointConfig.properties` file located in the `<APIM_HOME>/repository/deployment/server/webapps/authenticationendpoint/WEB-INF/classes` directory.

    *   If the `accountrecoveryendpoint` web app is hosted externally, follow the instructions given below.

a. Open the `RecoveryEndpointConfig.properties` file found in the root of the `accountrecoveryendpoint` folder.

b. Change the `app.password` property value to the value added as `app_password` in the `deployment.toml` file.

c. Do the same changes to the `RecoveryEndpointConfig.properties` file located in the `<APIM_HOME>/repository/deployment/server/webapps/accountrecoveryendpoint/WEB-INF/classes` directory.

3.   Once these changes are configured, restart the server.

    *   Linux/Unix : sh api-manager.sh
    *   Windows : api-manager.bat

### Enable HTTP Strict Transport Security (HSTS) Headers[¶](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#enable-http-strict-transport-security-hsts-headers "Permanent link")

To enable HSTS for all the Tomcat deployed webapps including Management console, Publisher, Developer and Admin portals, please add the below config to the `deployment.toml` file.

```
[[tomcat.filter]]
name = "httpHeaderSecurity"
class = "org.apache.catalina.filters.HttpHeaderSecurityFilter"
async_supported = true

[tomcat.filter.init_params]
hstsEnabled = true
hstsMaxAgeSeconds = 31536000
hstsIncludeSubDomains = true

[[tomcat.filter_mapping]]
name = "httpHeaderSecurity"
url_pattern = "/*"
dispatchers = "REQUEST"
```

To enable HSTS only to selected web applications, check whether the HttpHeaderSecurityFilter stored in the `<APIM_HOME>/repository/deployment/server/webapps/` directory is available in the `web.xml` file of that particular web application. If the filter is available, enable HSTS as shown below.

```
<filter>
    <filter-name>HttpHeaderSecurityFilter</filter-name>        
    <filter-class>org.apache.catalina.filters.HttpHeaderSecurityFilter</filter-class>
</filter>
<filter-mapping>     
    <filter-name>HttpHeaderSecurityFilter</filter-name>     
    <url-pattern>*</url-pattern>
</filter-mapping>
```

[Back to top](https://apim.docs.wso2.com/en/4.6.0/install-and-setup/setup/deployment-best-practices/security-guidelines-for-production-deployment/#)

### Join our Discord

Connect with our community on our official Discord server. Share ideas, get help, and be a part of the awesome conversations!

[Join Discord](https://discord.com/invite/wso2)

Got a tough question? [Ask on Stackoverflow](https://stackoverflow.com/questions/tagged/wso2-apim?tab=Newest)

Want to contribute? [Head over to GitHub](https://github.com/wso2/docs-apim)

Like to stay updated? [Follow us on X (Formerly Twitter)](https://twitter.com/intent/follow?screen_name=wso2)

Prefer video tutorials? [Subscribe to our YouTube Channel](https://www.youtube.com/user/WSO2TechFlicks)

 © 2024-2026 [WSO2](https://wso2.com/) LLC. | Content licensed under [CC By 4.0](https://creativecommons.org/licenses/by/4.0). | Sample code licensed under [Apache 2.0](http://www.apache.org/licenses/).
