# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/cookies-secure-flag.md

---
title: Ensure cookies have the secure flag
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure cookies have the secure flag
---

# Ensure cookies have the secure flag

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/cookies-secure-flag`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

Ensure cookies use the `secure` flag or attribute. If not set, it could cause the user agent to send those cookies in plaintext over an HTTP session.

#### Learn More{% #learn-more %}

- [CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute](https://cwe.mitre.org/data/definitions/614.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
@Controller
@RequestMapping(value = "/transfer")
public class TransferController {

    private static final String PENDING_TRANSFER = "PENDING_TRANSFER";

    public static Process toTraces(Runtime runtime, String command) throws IOException {
        return runtime.exec(command);
    }

    @Autowired
    CashAccountDao cashaccountDao;

    @Autowired
    AccountDao accountDao;

    @Autowired
    TransfersFacade transfersFacade;

    @RequestMapping
    public String newTransferForm(final Model model, final Principal principal, final HttpServletResponse response) {
        List<CashAccount> cashAccounts = cashaccountDao.findCashAccountsByUsername(principal.getName());

        Account account = accountDao.findUsersByUsername(principal.getName()).get(0);

        Transfer newTransfer = new Transfer();
        newTransfer.setFee(5.00);

        if (!model.containsAttribute("transfer")) {
            model.addAttribute("transfer", newTransfer);
        }
        model.addAttribute("cashAccounts", cashAccounts);
        model.addAttribute("account", account);

        response.addCookie(new Cookie("accountType", AccountType.PERSONAL));

        return "newTransfer";
    }
}
```

```java
class Test{
    public void eatCookies() {
        Cookie[] cookies = request.getCookies();

        for (int loop = 0; loop < cookies.length; loop++) {
            if (!cookies[loop].getName().startsWith("JS")) {
                cookies[loop].setMaxAge(0);
                response.addCookie(cookies[loop]);
            }
        }
    }
}
```

```java
class Compliant {
    @Override
    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");

        String queryString = request.getQueryString();
        String paramval = "BenchmarkTest01683" + "=";
        int paramLoc = -1;
        if (queryString != null) paramLoc = queryString.indexOf(paramval);
        if (paramLoc == -1) {
            response.getWriter()
                    .println(
                            "getQueryString() couldn't find expected parameter '"
                                    + "BenchmarkTest01683"
                                    + "' in query string.");
            return;
        }

        String param =
                queryString.substring(
                        paramLoc
                                + paramval
                                        .length()); // 1st assume "BenchmarkTest01683" param is last
        // parameter in query string.
        // And then check to see if its in the middle of the query string and if so, trim off what
        // comes after.
        int ampersandLoc = queryString.indexOf("&", paramLoc);
        if (ampersandLoc != -1) {
            param = queryString.substring(paramLoc + paramval.length(), ampersandLoc);
        }
        param = java.net.URLDecoder.decode(param, "UTF-8");

        String bar = new Test().doSomething(request, param);

        byte[] input = new byte[1000];
        String str = "?";
        Object inputParam = param;
        if (inputParam instanceof String) str = ((String) inputParam);
        if (inputParam instanceof java.io.InputStream) {
            int i = ((java.io.InputStream) inputParam).read(input);
            if (i == -1) {
                response.getWriter()
                        .println(
                                "This input source requires a POST, not a GET. Incompatible UI for the InputStream source.");
                return;
            }
            str = new String(input, 0, i);
        }
        if ("".equals(str)) str = "No cookie value supplied";
        javax.servlet.http.Cookie cookie = new javax.servlet.http.Cookie("SomeCookie", str);

        cookie.setSecure(false);
        cookie.setHttpOnly(true);
        cookie.setPath(request.getRequestURI()); // i.e., set path to JUST this servlet
        // e.g., /benchmark/sql-01/BenchmarkTest01001
        response.addCookie(cookie);

        response.getWriter()
                .println(
                        "Created cookie: 'SomeCookie': with value: '"
                                + org.owasp.esapi.ESAPI.encoder().encodeForHTML(str)
                                + "' and secure flag set to: false");
    }
}
```

```java
class NotCompliant {
    public void setCookie(String field, String value) {
        Cookie cookie = new Cookie(field, value);
        response.addCookie(cookie);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class NotCompliant {
    public void setCookie(String field, String value) {
        // cookie not added, all good
        Cookie cookie = new Cookie(field, value);
    }
}
```

```java
class Test{
    public void eatCookies() {
        Cookie[] cookies = request.getCookies();

        for (int loop = 0; loop < cookies.length; loop++) {
            cookies[loop].setSecure(true);
            if (!cookies[loop].getName().startsWith("JS")) {
                cookies[loop].setMaxAge(0);
                response.addCookie(cookies[loop]);
            }
        }
    }
}
```

```java
class Compliant {
    public void setCookie(String field, String value) {
        Cookie cookie = new Cookie(field, value);
        cookie.setSecure(true);
        cookie.setHttpOnly(true);
        response.addCookie(cookie);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
