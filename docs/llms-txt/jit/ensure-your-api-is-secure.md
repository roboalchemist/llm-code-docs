# Source: https://docs.jit.io/docs/ensure-your-api-is-secure.md

# Scan Your API for Vulnerabilities (DAST)

## Jit Dynamic Application Security Testing (DAST) for APIs: Key things to know

* **Brief description:** Jit DAST detects an extensive list of weaknesses, misconfigurations, and security vulnerabilities to ensure your APIs are secure before, during, and after production.
* **Scanning process:** Automated API scanning takes place daily or whenever a new change is deployed to a specific web application. Multiple APIs can be scanned with a single Jit account.
* **Vulnerability detection types**: SQL injection, cross-site scripting, clickjacking or path traversal that may not be visible in the source code.
* **How to get started:** Simply add inputs into Jit's ZAP Configuration Wizard – which can be found by navigating to **Security Plans** --> **Dynamic Application Security Testing** --> scroll down to **Scan your API for vulnerabilities** – to point Jit toward the relevant API and run automated scans.
  * After a scan, all security findings are recorded in the [Findings page](https://docs.jit.io/v5.0/docs/jit-findings).
  * Multiple APIs can be scanned with a single Jit account – each API will require its own DAST configuration.
  * For detailed onboarding instructions, see the section below.
* **Based on ZAP:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For DAST, we use [Zed Attack Proxy](https://www.jit.io/resources/owasp-zap) to run the analyses, which is used by thousands of security teams.
* **Test Jit DAST:** Test Jit DAST with our suggested [test targets](https://docs.jit.io/docs/code-samples#run-a-web-application-scanner--ensure-your-apis-are-secure-zap-based-security-requirements).

***

## Getting started with Jit DAST for API Scanning

See Jit DAST onboarding instructions [here](https://docs.jit.io/v5.0/docs/scan-your-web-application-for-vulnerabilities-dast-copy).

***

## Jit DAST Rules

Jit DAST is based on ZAP, which supports the following rules – each of which are designed to detect specific application vulnerabilities:

* [Active rules](https://www.zaproxy.org/docs/desktop/start/features/ascan/), identify potential vulnerabilities by using known attacks against selected targets in web applications.
* [Passive rules](https://www.zaproxy.org/docs/desktop/start/features/pscan/), scan all HTTP request and response messages sent to the API or web application being tested. Passive scans do not make any changes to messages.

For more information about scans and their rules see [ZAP Rules for Detecting Vulnerabilities](https://dash.readme.com/project/jitsecurity/v4.5.0/docs/vulnerabilities-detected-using-zap).

***

## Authenticated vs unauthenticated mode

In Unauthenticated Mode, Jit DAST can reach the parts of an application that an unauthenticated user could reach, while Authenticated Mode allows Jit DAST to reach any part of an application that an authenticated user could reach.

For this reason, we suggest Authenticated Mode, which provides deeper insight into the security of your web application. Authenticated Mode requires a bit of additional configuration and supports multiple authentication methods. This requires some specialized configuration, which is why we ask that you meet with us for a free onboarding session if you want to enable Authenticated Mode.

***

> 🔒 Whitelisting Jit DAST scanners
>
> To perform API scans, Zap requires access to your APIs. If your APIs are secured with a whitelist, please ensure the following IP addresses are included:
>
> For Jit - 🇺🇸 US site (<https://platform.jit.io>)
>
> * 3.220.250.224/32
> * 52.45.232.22/32
>
> For Jit - 🇪🇺 Europe site (<https://platform.eu.jit.io>)
>
> * 18.198.245.94/32
> * 18.157.204.182/32
>
> Adding these IP addresses to your whitelist will enable Zap to conduct its scans without interruption.