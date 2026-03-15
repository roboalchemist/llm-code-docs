# Source: https://docs.jit.io/docs/different-dast-plans.md

# Different DAST plans

## Dynamic Application Security Plan

The [Dynamic Application Security Plan]() aims to identify and mitigate security vulnerabilities in web applications and APIs using ZAP DAST (Dynamic Application Security Testing). This plan consists of two primary scanning strategies:

1. ZAP Web Scan
2. ZAP API Scan

These scans are also included in the[ Jit MVS Plan](https://docs.jit.io/docs/jit-mvs-for-appsec-plan)

Additionally, there is a specialized scanning plan targeting the most critical vulnerabilities outlined in the [OWASP Top 10](https://docs.jit.io/docs/owasp-top-10-plan).

## OWASP Top 10 Plan

The OWASP Top 10 Plan is designed to address the most critical web application security risks as identified by the Open Web Application Security Project (OWASP). This plan provides comprehensive coverage of both passive and active security tests, ensuring robust detection and mitigation of the most severe vulnerabilities.

## Differences Between The Plans

| **Aspect**            | **ZAP Web Scan**                                                                                      | **ZAP API Scan**                                                                 | **OWASP Top 10 Plan**                             |
| --------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Passive Tests**     | 12 tests                                                                                              | 6 tests                                                                          | 74 tests                                          |
|                       | - Application error disclosure                                                                        | - API rate limiting                                                              | - Insufficient transport layer protection         |
|                       | - HTTP parameter pollution                                                                            | - Application error disclosure                                                   | - Clickjacking                                    |
|                       | - Secure pages with mixed content                                                                     | - Missing cookie attributes                                                      | - Insecure HTTP methods                           |
|                       | - Missing cookie attributes                                                                           | - Information disclosure                                                         | - CSRF (Cross-Site Request Forgery)               |
|                       | - Information disclosure                                                                              | - HTTP response splitting                                                        | - SSL certificate validation                      |
|                       | - HTTP response splitting                                                                             | - Remote file inclusion                                                          | - Additional SQL injection checks                 |
|                       | - Anti-CSRF tokens                                                                                    |                                                                                  | - XML injection                                   |
|                       | - Cross-domain misconfigurations                                                                      |                                                                                  | - Information leakage                             |
|                       | - Remote file inclusion                                                                               |                                                                                  | - Directory browsing                              |
|                       | - Directory browsing                                                                                  |                                                                                  | - Insecure deserialization                        |
| **Active Tests**      | 18 tests                                                                                              | 18 tests                                                                         | 62 tests                                          |
|                       | - SQL injection                                                                                       | - SQL injection                                                                  | - Various SQL injection techniques                |
|                       | - Cross-site scripting (XSS) - reflected and stored                                                   | - Local file inclusion                                                           | - OS command injection                            |
|                       | - Local file inclusion                                                                                | - Remote code execution (PHP)                                                    | - Path traversal                                  |
|                       | - Remote code execution (PHP)                                                                         | - Open redirect                                                                  | - Remote and local file inclusion                 |
|                       | - Open redirect                                                                                       | - Path traversal                                                                 | - HTTP parameter pollution                        |
|                       | - Path traversal                                                                                      | - OS command injection                                                           | - Cross-site scripting (XSS) - multiple types     |
|                       | - OS command injection                                                                                | - Server-side code injection                                                     | - Insecure direct object references               |
|                       | - Server-side code injection                                                                          | - XXE (XML External Entity) injection                                            | - Insecure deserialization                        |
|                       | - XXE (XML External Entity) injection                                                                 | - XPath injection                                                                | - API rate limiting                               |
|                       | - XPath injection                                                                                     | - JSON injection                                                                 | - Command injection                               |
|                       | - JSON injection                                                                                      | - LDAP injection                                                                 | - Remote code execution                           |
|                       | - LDAP injection                                                                                      | - Insecure deserialization                                                       | - Server-side template injection                  |
| **Comprehensiveness** | Moderate                                                                                              | Moderate                                                                         | High                                              |
| **Target**            | General web application security                                                                      | API-specific security                                                            | Broad range of vulnerabilities aligned with OWASP |
| **Recommendations**   | Suitable for general web application security testing with a broad range of passive and active tests. | Best for API-specific security testing with a comprehensive set of active tests. | Ideal for comprehensive security assurance.       |