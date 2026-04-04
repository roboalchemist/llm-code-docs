# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/inner-outer-html.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/inner-outer-html.md

---
title: Do not modify innerHTML or outerHTML
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not modify innerHTML or outerHTML
---

# Do not modify innerHTML or outerHTML

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/inner-outer-html`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Properties like `innerHTML` and `outerHTML` should not be modified directly unless such modifications are clearly reviewed. Modifying `innerHTML` or `outerHTML` using user inputs that has not been validated can lead to XSS injection.

#### Learn More{% #learn-more %}

- [Why InnerHTML Is a Bad Idea and How to Avoid It?](https://www.dhairyashah.dev/posts/why-innerhtml-is-a-bad-idea-and-how-to-avoid-it/)
- [CWE-79 - Improper Neutralization of Input During Web Page Generation](https://cwe.mitre.org/data/definitions/79.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function display(text) {
    const mealPlanDiv = document.getElementById("meal-plan");
    const defaultMessage = document.getElementById("default-message");
    defaultMessage.style.display = 'none';
    something.innerHTML = `

        ${something}

        <div style="background:white; padding:15px; border-radius:10px;">
        </div>
    `;


    somethingElse.innerHTML = `
        <div style="background:white; padding:15px; border-radius:10px;">
            ${DOMPurify.sanitize(marked(text))}
        </div>
    `;

    somethingElseElse.innerHTML = `

        ${something}

        <div style="background:white; padding:15px; border-radius:10px;">
            ${DOMPurify.sanitize(marked(text))}
        </div>
    `;
}
```

```javascript
// Set content
if (typeof HTMLElement === 'object' ? this.message instanceof HTMLElement : this.message && typeof this.message === 'object' && this.message !== null && this.message.nodeType === 1 && typeof this.message.nodeName === 'string') {
    toast.appendChild(this.message);

    // Check if it is jQuery object
} else if (this.message instanceof jQuery) {
    $(toast).append(this.message);

    // Insert as text;
} else {
    toast.innerHTML = this.message;
}

// Append toasft
Toast._container.appendChild(toast);
return toast;
}
```

```javascript
function nonCompliant(argument) {
  const content = '<div>' + argument + '</div>';
  document.write(content);
}
```

```javascript
function nonCompliant(myArgument) {
  document.body.outerHTML = myArgument;
}
```

```javascript
if (typeof(SERVER_DOMAIN) === 'undefined') {
   window.location.replace("/unconfigured.html");
}

const RECEIVE_URL = SERVER_DOMAIN + "/challenge_scoreboard.html" + "?origin=" + get_domain();

var window_ref = null;

document.getElementById("username").focus();

function store_username() {
   var username;
   var username_obj;

   username_obj = document.getElementById("username");
   username = username_obj.value

   var welcome;
   welcome = document.getElementById("welcome");
   welcome.innerHTML = "Welcome " + html_encode (username);

   var set_username;
   set_username = document.getElementById("set_username");
   set_username.style.display="none";

   var game;
   game = document.getElementById("game");
   game.style.display="inline";

   start_game();
   // have to do time out so the window can open
   setTimeout (function () {send_username(username);}, 1000);

   return false;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
import { xss, xssStrip, xssEscapeHtml } from '@/utils/xss';

function sanitizeHtml(el, something) {
    if (Array.isArray(something.value)) {
      el.innerHTML = xss(something.value);
    } else if (something.strip) {
      el.innerHTML = xssStrip(something.value);
    } else if (something.escape) {
      el.innerHTML = xssEscapeHtml(something.value);
    } else if (something.strip) {
      el.innerHTML = "hello"
    } else if (something.escape) {
      el.innerHTML += "hello"
    } else if (something.escape) {
      el.innerHTML += 'hello
      world'
    } else {
      el.innerHTML = xss(binding.value);
    }
  }
}

export default sanitizeHtml;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
