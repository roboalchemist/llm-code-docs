# Source: https://docs.curator.interworks.com/server_management/system_administration/server_hardening_procedures.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Server Hardening Procedures

> Security best practices and procedures for hardening Curator server installations to protect your data and infrastructure.

## Introduction

Securing your data is vitally important. Curator uses many
[checks and procedures](https://curator.interworks.com/data-and-security)
to ensure the safety of your system.

Many security settings are already set up for your site "out of the box", however, additional steps can be
taken by your system administrators to further harden the setup upon installation.

## Hardening Steps

1. **SSL Certificates:** Make sure SSL certificates are added to your website! Secure transportation of data
   between the users and the server is very important. Click
   [here to follow the instructions for SSL certificate installation](/setup/ssl/linux_ssl).
   Both Tableau Server and Curator should utilize SSL for user traffic.

2. **Force SSL Traffic:** You will also want to force users to use this new SSL route. Curator has a simple
   toggle to force users over HTTPS instead of HTTP. Simply enable this setting in
   [Settings->Curator->Portal Settings](/setup/ssl/force_ssl) \
   to ensure users use this route.

3. While you are in “Portal Settings” for Step #2, also set the “Forced Curator Domain” option to prevent
   [Host Header Injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection).

4. After enabling SSL, make sure your SSL Ciphers are up to date. You can update these values using the
   [SSL Protocols / Ciphers](/setup/ssl/linux_ssl)
   steps on the Linux SSL installation page.

5. In addition to setting SSL Ciphers in your `curator.conf`, you may wish to adjust the default values for
   `Strict-Transport-Security` and `Expect-CT`. There are four lines to set these values toward the bottom of
   the file. These are commented out by default. Simply uncomment these lines and restart Curator to utilize them.

6. Other than that, Curator should pass most security scans “out of the box”. If you do run into any issues,
   though, please let us know! We’d love to help you resolve them: either through core Curator changes, or (more
   likely) configuration adjustments.

7. If your website is public available, you may wish to utilize
   [SSLLabs.com](https://www.ssllabs.com/ssltest/analyze.html)
   and [SecurityHeaders.com](https://securityheaders.com/) to further test your configuration.

## Additional Information

**!Important! Tableau Server:** Your Tableau Server must also be available to end users for them to be able to access
dashboards.

For example, if Tableau Server is on-prem and behind the firewall, the end users won’t be able to access the
dashboards unless they are using the VPN. Because of this, you will want to place Tableau Server on the open
internet as well, following [their hardening instructions](https://help.tableau.com/current/server/en-gb/security_harden.htm).
If you are using Tableau Cloud, then you do not need to worry about this, as it is already accessible.

**WAF Systems:** If you’d like an extra layer of protection, many of our customers utilize WAF systems in
front of both Tableau Server and Curator. To configure Curator for a WAF, use
[these instructions](/setup/proxy_configuration/reverse_proxy). To configure Tableau Server,
[use Tableau’s reverse proxy instructions](https://help.tableau.com/current/server/en-us/proxy.htm#configure-the-reverse-proxy-server)
,as well as Curator’s
[“alternative URL routing”](/creating_integrations/tableau_connection/alternative_url_routing)
instructions.
