# Source: https://docs.api7.ai/apisix/enterprise-feature/compliance.md

# Compliance

Data security and privacy are paramount for enterprises in the data-driven business environment. API gateways, which handle large volumes of sensitive data, must adhere to strict compliance standards to protect data during transmission and processing.

Global and regional regulations such as GDPR, FIPS 140-2, and SOC 2 set rigorous data management requirements to safeguard sensitive information. These regulations help mitigate the risks of data misuse or leakage, ensuring that business operations align with international security and privacy standards.

API7.ai prioritizes security and continuously maintains compliance across its products and services. API7.ai ensures robust data protection by adhering to industry-leading [compliance standards](https://api7.ai/compliance), including SOC 2 Type II, ISO/IEC 27001:2022, HIPAA, and GDPR. These compliance standards collectively address data protection and security's technical, operational, and regulatory aspects, making API7.ai a secure, compliant choice for organizations across sectors.

## Compliance Solutions of API7 Enterprise[â](#compliance-solutions-of-api7-enterprise "Direct link to Compliance Solutions of API7 Enterprise")

### 1. FIPS 140-2[â](#1-fips-140-2 "Direct link to 1. FIPS 140-2")

[FIPS 140-2](https://en.wikipedia.org/wiki/FIPS_140-2) (Federal Information Processing Standard 140-2) is a US government security standard specifying cryptographic module requirements. Industries such as finance and healthcare often impose specific compliance requirements for data security.

API7 Enterprise integrates FIPS 140-2 compliance to ensure that its cryptographic modules meet the rigorous security requirements for handling sensitive data. API7 Enterprise fulfills the rigorous FIPS 140-2 (Level 1) requirements by supporting the FIPS 140-2 validated OpenSSL 3.0, fortifying the encryption and decryption of SSL/TLS encrypted network traffic.

### 2. Secure Data Transmission[â](#2-secure-data-transmission "Direct link to 2. Secure Data Transmission")

API7 Enterprise employs robust transmission protocols including TLS and mTLS, forming a comprehensive multi-layered security framework. TLS secures communication channels by encrypting data between clients and servers while mTLS secures mutual authentication between them.

It also supports access control based on IP addresses by configurable IP blacklisting and whitelisting. The [`ip-restriction`](https://docs.api7.ai/hub/ip-restriction) plugin can be used to restrict access to upstream resources by IP addresses. In addition, API7 Enterprise provides a variety of authentication methods such as [`key-auth`](https://docs.api7.ai/hub/key-auth), [`basic-auth`](https://docs.api7.ai/hub/basic-auth), [`jwt-auth`](https://docs.api7.ai/hub/jwt-auth), and [`hmac-auth`](https://docs.api7.ai/hub/hmac-auth), allowing businesses to tailor their security policies to meet specific requirements. These features help fortify API7 Enterprise against a wide range of cyber threats, ensuring that modern enterprise environments remain protected from evolving risks.

### 3. Secret Management[â](#3-secret-management "Direct link to 3. Secret Management")

Enterprises can store sensitive data like secrets, tokens, and SSL certificates securely within API7 Enterprise, aligning with industry standards such as FIPS. Alternatively, sensitive information can be stored in trusted secret management solutions like HashiCorp Vault and AWS Secrets Manager. As API7 Enterprise has integrated with these mainstream secret management solutions, companies can securely retrieve and reference this data as variables, minimizing the risk of exposure.

By integrating with these external secret managers, API7 Enterprise helps organizations enforce strong security policies. Additionally, API7 Enterprise provides fine-grained access control, further reducing the risk of unauthorized access or modifications.

### 4. Data Privacy Protection[â](#4-data-privacy-protection "Direct link to 4. Data Privacy Protection")

To further protect sensitive data, API7 Enterprise offers a set of robust data security plugins. The [`data-mask`](https://docs.api7.ai/hub/data-mask) plugin can be used to remove or replace sensitive information in request headers, request bodies, and URL queries. Therefore, sensitive data like secrets and passwords can be masked in logs, preventing the exposure of sensitive information.

API7 Enterprise enhances its data privacy protection with robust Web Application Firewalls (WAFs), including [`chaitin-waf`](https://github.com/chaitin/SafeLine), [`coraza-proxy-wasm`](https://github.com/corazawaf/coraza-proxy-wasm), and [`open-appsec`](https://github.com/openappsec). They help to detect and block malicious requests like SQL injection and cross-site scripting (XSS) to protect the security of applications and user data.
