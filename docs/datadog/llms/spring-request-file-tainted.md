# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/spring-request-file-tainted.md

---
title: Avoid user-input file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid user-input file
---

# Avoid user-input file

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/spring-request-file-tainted`

**Language:** Java

**Severity:** Notice

**Category:** Security

**CWE**: [23](https://cwe.mitre.org/data/definitions/23.html)

## Description{% #description %}

An attacker could try to pass a filename of content that could traverse the server path and control system files. Make sure all user-inputs is checked and sanitized before use.

#### Learn More{% #learn-more %}

- [CWE-23 - Relative Path Traversal](https://cwe.mitre.org/data/definitions/23.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Test {
  @PostMapping(value = "/fileupload")
  public ModelAndView importFile(@RequestParam("file") MultipartFile myFile) throws IOException {
    var user = (WebGoatUser) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
    var destinationDir = new File(fileLocation, user.getUsername());
    destinationDir.mkdirs();
    myFile.transferTo(new File(destinationDir, myFile.getOriginalFilename()));
    log.debug("File saved to {}", new File(destinationDir, myFile.getOriginalFilename()));

    return new ModelAndView(
        new RedirectView("files", true),
        new ModelMap().addAttribute("uploadSuccess", "File uploaded successful"));
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
