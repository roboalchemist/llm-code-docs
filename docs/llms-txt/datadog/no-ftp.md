# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/no-ftp.md

---
title: Avoid FTP connections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid FTP connections
---

# Avoid FTP connections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/no-ftp`

**Language:** Ruby

**Severity:** Info

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

The rule "Avoid FTP connections" is a security best practice that discourages the use of the File Transfer Protocol (FTP) for transferring files in your Ruby applications. FTP is a protocol that lacks modern security features such as encryption and is susceptible to numerous types of attacks, including packet capture, spoofing, and brute force attacks.

This rule is important because the use of insecure protocols like FTP can lead to the exposure of sensitive data, such as user credentials or confidential file contents. The lack of encryption means that data transferred via FTP can be easily intercepted and read by unauthorized parties. This can lead to serious security breaches and data loss.

To adhere to this rule and avoid the associated security risks, use secure alternatives to FTP. For instance, you could use SFTP (SSH File Transfer Protocol) or FTPS (FTP Secure) which provide the necessary encryption for data transfers. In Ruby, you can use libraries such as `Net::SFTP` or `Net::FTPS` for secure file transfers. Using these alternatives will ensure that your file transfers are securely encrypted and less vulnerable to attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
Net::FTP.open('example.com') do |ftp|
    ftp.login
    files = ftp.chdir('pub/lang/ruby/contrib')
    files = ftp.list('n*')
    ftp.getbinaryfile('nif.rb-0.91.gz', 'nif.gz', 1024)
end

ftp = Net::FTP.new('example.com')
ftp.login
files = ftp.chdir('pub/lang/ruby/contrib')
files = ftp.list('n*')
ftp.getbinaryfile('nif.rb-0.91.gz', 'nif.gz', 1024)
ftp.close
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
