# Source: https://www.zaproxy.org/docs/guides/zapping-the-top-10-2021

Title: ZAPping the OWASP Top 10 (2021)

URL Source: https://www.zaproxy.org/docs/guides/zapping-the-top-10-2021

Published Time: 2021-12-01T00:00:00+00:00

Markdown Content:
This document gives an overview of the automatic and manual components provided by OWASP Zed Attack Proxy (ZAP) that are recommended for testing each of the OWASP Top Ten Project 2021 risks.

For the previous Top Ten see [ZAPping the OWASP Top 10 (2017)](https://www.zaproxy.org/docs/guides/zapping-the-top-10-2017)

Note that the [OWASP Top Ten Project](https://owasp.org/www-project-top-ten/) risks cover a wide range of underlying vulnerabilities, some of which are not really possible to test for in a completely automated way. If a completely automated tool claims to protect you against the full OWASP Top Ten then you can be sure they are being ‘economical with the truth’!

The component links take you to the relevant places in an online version of the ZAP User Guide from which you can learn more.

|  |  |  |
| --- | --- | --- |
| ##### Common Components |  | The ‘common components’ can be used for pretty much everything, so can be used to help detect all of the Top 10 |
|  | Manual | [Manipulator-in-the-middle proxy](https://www.zaproxy.org/docs/desktop/start/features/intercept/) |
|  | Manual | [Manual request](https://www.zaproxy.org/docs/desktop/addons/requester/dialogs/) / resend |
|  | Manual | [Scripts](https://www.zaproxy.org/docs/desktop/addons/script-console/) |
|  | Manual | [Community Scripts](https://www.zaproxy.org/docs/desktop/addons/community-scripts/) |
|  | Manual | [Search](https://www.zaproxy.org/docs/desktop/ui/tabs/search/) |
| [##### A1 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A01](https://www.zaproxy.org/alerttags/owasp_2021_a01/) |
|  | Automated | [Access Control Testing*](https://www.zaproxy.org/docs/desktop/addons/access-control-testing/) |
|  | Manual | [Port Scanner*](https://www.zaproxy.org/docs/desktop/addons/port-scan/) |
|  | Manual | [Wappalyzer - Technology detection*](https://www.zaproxy.org/docs/desktop/addons/technology-detection/) |
| [##### A2 Cryptographic Failures](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A02](https://www.zaproxy.org/alerttags/owasp_2021_a02/) |
| [##### A3 Injection](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2021/Top_10-2021_A3-Injection) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A03](https://www.zaproxy.org/alerttags/owasp_2021_a03/) |
|  | Manual | [Fuzzer](https://www.zaproxy.org/docs/desktop/addons/fuzzer/), combined with the [FuzzDb*](https://www.zaproxy.org/docs/desktop/addons/fuzzdb-files/) and [SVN Digger*](https://www.zaproxy.org/docs/desktop/addons/svn-digger-files/) files |
|  | Manual | [Eval Villain](https://www.zaproxy.org/docs/desktop/addons/eval-villain/) |
| [##### A4 Insecure Design](https://owasp.org/Top10/A04_2021-Insecure_Design/) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A04](https://www.zaproxy.org/alerttags/owasp_2021_a04/) |
| [##### A5 Security Misconfiguration](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2021/Top_10-2021_A5-Security_Misconfiguration) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A05](https://www.zaproxy.org/alerttags/owasp_2021_a05/) |
|  | Manual | [Spider](https://www.zaproxy.org/docs/desktop/addons/spider/) |
|  | Manual | [Ajax Spider](https://www.zaproxy.org/docs/desktop/addons/ajax-spider/) |
|  | Manual | [Session comparison](https://www.zaproxy.org/docs/desktop/ui/tlmenu/report/#compare-with-another-session) |
|  | Manual | [Access Control Testing*](https://www.zaproxy.org/docs/desktop/addons/access-control-testing/) |
| [##### A6 Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A06](https://www.zaproxy.org/alerttags/owasp_2021_a06/) |
|  | Manual | [Wappalyzer - Technology detection*](https://www.zaproxy.org/docs/desktop/addons/technology-detection/) |
| [##### A7 Identification and Authentication Failure](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/) |  |  |
|  | Manual | [HTTP Sessions](https://www.zaproxy.org/docs/desktop/start/features/httpsessions/) |
|  | Manual | [Spider](https://www.zaproxy.org/docs/desktop/addons/spider/) |
|  | Manual | [Forced Browse](https://www.zaproxy.org/docs/desktop/addons/forced-browse/) |
|  | Manual | [Token Generator*](https://www.zaproxy.org/docs/desktop/addons/token-generator/) |
|  | Automated | [Access Control Testing*](https://www.zaproxy.org/docs/desktop/addons/access-control-testing/) |
| [##### A8 Software and Data Integrity Failures](https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/) |  |  |
|  | Automated | Scan Rules tagged with: [OWASP_2021_A08](https://www.zaproxy.org/alerttags/owasp_2021_a08/) |
| [##### A9 Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) |  |  |
|  | Automated / Manual | The Spider(s), Active Scanner, Fuzzer, and Access Control addon can all be used to generate traffic and “attacks” which are potential sources/causes for logging and alerting. |
| [##### A10 Server-Side Request Forgery](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/) |  |  |
|  | Automated | [OAST Support](https://www.zaproxy.org/docs/desktop/addons/oast-support/) |
|  |  |  |

* The stared add-ons (and Beta and Alpha scan rules) are not included by default in the full ZAP release but can be downloaded from the ZAP Marketplace via the ‘Manage add-ons’ button on the ZAP main toolbar.

![Image 1: ZAP Toolbar - Marketplace Button](https://www.zaproxy.org/img/zap-screenshot-browse-addons.png)
