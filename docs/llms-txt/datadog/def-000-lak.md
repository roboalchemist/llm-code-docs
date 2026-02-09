# Source: https://docs.datadoghq.com/security/default_rules/def-000-lak.md

---
title: Incoming client certificates should be required to be 'On'
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Incoming client certificates should be
  required to be 'On'
---

# Incoming client certificates should be required to be 'On'
 
## Description{% #description %}

Client certificates allow for an app to request a certificate for incoming requests. Only clients that have a valid certificate can reach the app. The TLS mutual authentication technique in enterprise environments ensures the authenticity of clients to the server. If incoming client certificates are enabled, only an authenticated client who has valid certificates can access the app.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Log in to Azure Portal using [https://portal.azure.com](https://portal.azure.com).
1. Go to **App Services**.
1. Click on each App.
1. Under **Settings** section, Click on **Configuration**.
1. Under **Incoming client certificates**, set the **Client Certificate Mode** option to **Require**.
