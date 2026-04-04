# Source: https://docs.jit.io/docs/owasp-top-10-plan.md

# OWASP Top 10 Plan

### Overview

The [OWASP Top 10](https://owasp.org/Top10/) is a globally recognized standard for web application security. It identifies the most critical security risks faced by web applications today. Our product integrates OWASP Top 10 coverage to ensure comprehensive security assessments and mitigation strategies.

### Plan Description

The OWASP Top 10 plan aims to address the critical security risks outlined by the Open Web Application Security Project. By leveraging [OWASP Zed Attack Proxy (ZAP)](https://www.zaproxy.org/), our Dynamic Application Security Testing (DAST) plan thoroughly evaluates web applications and APIs for vulnerabilities and potential security weaknesses.

### Key Features

* **Comprehensive Vulnerability Detection**: ZAP simulates real-world attack scenarios to identify a wide range of security vulnerabilities and misconfigurations.
* **API Security Assessment**: Ensures APIs are secure by detecting weaknesses and vulnerabilities before, during, and after production.
* **Web Application Security Assessment**: Identifies vulnerabilities like SQL injection, cross-site scripting, clickjacking, and path traversal, even if they are not apparent in the source code.

## Configuration

### Plan Items

| ID       | Method | OWASP Top 10 Item                          | Security Tool |
| -------- | ------ | ------------------------------------------ | ------------- |
| A01-2021 | Auto   | Broken Access Control                      | ZAP           |
| A02-2021 | Auto   | Cryptographic Failures                     | ZAP           |
| A03-2021 | Auto   | Injection                                  | ZAP           |
| A04-2021 | Auto   | Insecure Design                            | ZAP           |
| A05-2021 | Auto   | Security Misconfiguration                  | ZAP           |
| A06-2021 | Auto   | Vulnerable and Outdated Components         | ZAP           |
| A07-2021 | Manual | Identification and Authentication Failures |               |
| A08-2021 | Auto   | Software and Data Integrity Failures       | ZAP           |
| A09-2021 | Manual | Security Logging and Monitoring Failures   |               |
| A10-2021 | Manual | Server-Side Request Forgery                |               |

### Configuration Guides

* [OWASP Top 10 Assessment Configuration](#): Detailed configurations for setting up OWASP Top 10 assessment within the DAST framework.