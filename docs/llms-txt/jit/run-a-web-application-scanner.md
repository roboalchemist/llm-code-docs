# Source: https://docs.jit.io/docs/run-a-web-application-scanner.md

# Scan your Web Application for Vulnerabilities (DAST)

## Jit Dynamic Application Security Testing (DAST) for Web Apps: Key things to know

* **Brief description:** Jit DAST scans your web applications in runtime to detect application vulnerabilities with an exceptionally high true positive rate.
* **Scanning process**: Automated scanning takes place daily or whenever a new change is deployed to a specific web application.
* **Vulnerability detection types**: SQL injection, cross-site scripting, clickjacking or path traversal that may not be visible in the source code.
* **How to get started:** Simply add inputs into Jit's ZAP Configuration Wizard – which can be found by navigating to **Security Plans** --> **Dynamic Application Security Testing** --> scroll down to **Scan your web application for vulnerabilities** – to point Jit toward the relevant web app and run automated scans.
  * After a scan, all security findings are recorded in the [Findings page](https://docs.jit.io/v5.0/docs/jit-findings).
  * Multiple web apps can be scanned with a single Jit account – each web application will require its own DAST configuration.
  * For detailed onboarding instructions, see the section below.
* **Based on ZAP:** Jit unifies and enhances the leading open source scanners for all product security scanning technologies. For DAST, we use [Zed Attack Proxy](https://www.jit.io/resources/owasp-zap) to run the analyses, which is used by thousands of security teams.
* **Test Jit DAST:** Test Jit DAST with our suggested [test targets](https://docs.jit.io/docs/code-samples#run-a-web-application-scanner--ensure-your-apis-are-secure-zap-based-security-requirements).

***

## Getting started with Jit DAST

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

> 🔒 Whitelisting Jit DAST scanners
>
> To perform web application scans, Zap requires access to your applications. If your web applications are secured with a whitelist, please ensure the following IP addresses are included:
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