# Source: https://help.aikido.dev/dast-surface-monitoring/front-end-scanning/http-websites-are-not-supported-by-front-end-scanning.md

# HTTP websites are not supported by Front-End Scanning

Aikido Front-End Scanning is designed to evaluate real world web security conditions. For that reason, **scanning websites served over plain HTTP is intentionally not supported**.

## Modern web security assumes HTTPS

Most front end security controls only make sense when HTTPS is in place. This includes:

* Secure cookies and SameSite attributes
* HSTS enforcement
* TLS certificate validation
* Protection against man in the middle attacks
* Browser enforced security guarantees

Without HTTPS, these controls either cannot be applied or are irrelevant. Scanning an HTTP website would produce results that are misleading at best and meaningless at worst.

## Browsers already treat HTTP as unsafe

Modern browsers actively warn users when visiting HTTP websites and block or restrict many security sensitive behaviors. Testing advanced front end security on top of an insecure transport layer is comparable to testing seatbelts in a car without brakes. The foundation is missing.

## Front end scanners are built around TLS guarantees

Aikido Front-End Scanning validates correct usage of HTTPS related mechanisms. When a site does not use HTTPS, the scanner cannot reliably:

* Assess cookie security settings
* Validate transport level protections
* Detect misconfigurations related to certificates or encryption

Supporting HTTP would require ignoring large parts of what the scanner is meant to verify, which goes against its purpose.

## This is not a limitation of testing, but of usefulness

HTTP applications can still be tested using other approaches such as [AI pentesting](https://help.aikido.dev/pentests) or controlled environments. However, a front end scanner that focuses on real browser behavior and modern security standards must assume HTTPS.

If HTTPS is required for testing, you can:

* Connect a domain with TLS enabled
* Use a reverse proxy or broker that terminates TLS
* Test a staging or production like environment

## Focus on real security outcomes

Aikido prioritizes accurate, actionable security findings over check the box scans. Enforcing HTTPS ensures that results reflect how applications are actually used and attacked in production today.

Scanning HTTP websites would not improve security posture and would only create noise. **This is why it is intentionally not supported.**
