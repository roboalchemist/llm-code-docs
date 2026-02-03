# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/spring-csrf-disable.md

---
title: Do not disable CSRF
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not disable CSRF
---

# Do not disable CSRF

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/spring-csrf-disable`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [352](https://cwe.mitre.org/data/definitions/352.html)

## Description{% #description %}

Disabling CSRF leads to security issues as the server may not be able to accurately identify a request.

#### Learn More{% #learn-more %}

- [CWE-352](https://cwe.mitre.org/data/definitions/352.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Test {
  @Bean
  public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http.authorizeHttpRequests(
        auth ->
            auth.requestMatchers(
                    "/css/**",
                    "/images/**",
                    "/js/**",
                    "fonts/**",
                    "/plugins/**",
                    "/registration",
                    "/register.mvc",
                    "/actuator/**")
                .permitAll()
                .anyRequest()
                .authenticated());
    http.formLogin()
        .loginPage("/login")
        .defaultSuccessUrl("/welcome.mvc", true)
        .usernameParameter("username")
        .passwordParameter("password")
        .permitAll();
    http.logout().deleteCookies("JSESSIONID").invalidateHttpSession(true);
    http.csrf().disable();

    http.headers().cacheControl().disable();
    http.exceptionHandling().authenticationEntryPoint(new AjaxAuthenticationEntryPoint("/login"));
    return http.build();
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 