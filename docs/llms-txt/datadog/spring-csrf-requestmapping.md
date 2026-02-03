# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/spring-csrf-requestmapping.md

---
title: Spring CSRF unrestricted RequestMapping
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Spring CSRF unrestricted RequestMapping
---

# Spring CSRF unrestricted RequestMapping

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/spring-csrf-requestmapping`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [352](https://cwe.mitre.org/data/definitions/352.html)

## Description{% #description %}

Classes that contain methods annotated with `RequestMapping` are by default mapped to all the HTTP request methods.

Spring Security's CSRF protection is not enabled by default for the HTTP request methods `GET`, `HEAD`, `TRACE`, and `OPTIONS`.

For this reason, requests or routes with `RequestMapping`, and not narrowing the mapping to the HTTP request methods `POST`, `PUT`, `DELETE`, or `PATCH`, makes them vulnerable to CSRF attacks.

#### Learn More{% #learn-more %}

- [Spring CSRF unrestricted RequestMapping](https://find-sec-bugs.github.io/bugs.htm#SPRING_CSRF_UNRESTRICTED_REQUEST_MAPPING)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
@Controller
public class ApplicationService extends BaseService {
    @RequestMapping(value = "/application.mvc", produces = "application/json")
    public @ResponseBody
    Application showApplication(HttpSession session) {
        Application app = Application.getInstance();
        return app;
    }

}
```

```java
@Controller
public class UnsafeController {

    @RequestMapping("/path")
    public void writeData() {
        // State-changing operations performed within this method.
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
@Controller
public class SafeController {

    /**
     * For methods without side-effects use @GetMapping.
     */
    @GetMapping("/path")
    public String readData() {
        // No state-changing operations performed within this method.
        return "";
    }

    /**
     * For state-changing methods use either @PostMapping, @PutMapping, @DeleteMapping, or @PatchMapping.
     */
    @PostMapping("/path")
    public void writeData() {
        // State-changing operations performed within this method.
    }

    /**
     * You can also use @RequestMapping if you specify a method
     */
    @RequestMapping(value = "/path2", method = RequestMethod.GET)
    public String readData2() {
        return "";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 