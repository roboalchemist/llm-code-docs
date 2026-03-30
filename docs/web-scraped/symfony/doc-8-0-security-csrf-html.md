# Source: https://symfony.com/doc/8.0/security/csrf.html

Title: How to Implement CSRF Protection (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/security/csrf.html

Markdown Content:
CSRF, or [Cross-site request forgery](https://en.wikipedia.org/wiki/Cross-site_request_forgery), is a type of attack where a malicious actor tricks a user into performing actions on a web application without their knowledge or consent.

The attack is based on the trust that a web application has in a user's browser (e.g. on session cookies). Here's a real example of a CSRF attack: a malicious actor could create the following website:

If you visit this website (e.g. by clicking on some email link or some social network post) and you were already logged in on the `https://example.com` site, the malicious actor could change the email address associated to your account (effectively taking over your account) without you even being aware of it.

An effective way of preventing CSRF attacks is to use anti-CSRF tokens. These are unique tokens added to forms as hidden fields. The legit server validates them to ensure that the request originated from the expected source and not some other malicious website.

Anti-CSRF tokens can be managed in two ways: using a **stateful** approach, where tokens are stored in the session and are unique per user and action; or a **stateless** approach, where tokens are generated on the client side.

[Installation](https://symfony.com/doc/8.0/security/csrf.html#installation "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

Symfony provides all the needed features to generate and validate the anti-CSRF tokens. Before using them, install this package in your project:

Then, enable/disable the CSRF protection with the `csrf_protection` option (see the [CSRF configuration reference](https://symfony.com/doc/current/reference/configuration/framework.html#reference-framework-csrf-protection) for more information):

By default, the tokens used for CSRF protection are stored in the session. That's why a session is started automatically as soon as you render a form with CSRF protection.

This leads to many strategies to help with caching pages that include CSRF protected forms, among them:

* Embed the form inside an uncached [ESI fragment](https://symfony.com/doc/current/http_cache/esi.html) and cache the rest of the page contents;
* Cache the entire page and load the form via an uncached AJAX request;
* Cache the entire page and use [hinclude.js](https://symfony.com/doc/current/templates.html#templates-hinclude) to load the CSRF token with an uncached AJAX request and replace the form field value with it.

The most effective way to cache pages that need CSRF protected forms is to use [stateless CSRF tokens](https://symfony.com/doc/current/security/csrf.html#csrf-stateless-tokens), as explained below.

[CSRF Protection in Symfony Forms](https://symfony.com/doc/8.0/security/csrf.html#csrf-protection-in-symfony-forms "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------

[Symfony Forms](https://symfony.com/doc/current/forms.html) include CSRF tokens by default and Symfony also checks them automatically for you. So, when using Symfony Forms, you don't have to do anything to be protected against CSRF attacks.

Note

According to [OWASP best practices](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html), CSRF protection is only required for **state-changing operations**, which must not use `GET` requests (as per the HTTP specification). Moreover, including CSRF tokens in `GET` request parameters can cause them to leak through browser history, log files, network utilities, and Referer headers.

If one of your forms uses GET (for example, a read-only search form), you can [configure the form to disable CSRF protection](https://symfony.com/doc/current/security/csrf.html#form-csrf-configuration).

By default Symfony adds the CSRF token in a hidden field called `_token`, but this can be customized (1) globally for all forms and (2) on a form-by-form basis. Globally, you can configure it under the `framework.form` option:

On a form-by-form basis, you can configure the CSRF protection in the `setDefaults()` method of each form:

You can also customize the rendering of the CSRF form field by creating a custom [form theme](https://symfony.com/doc/current/form/form_themes.html) and using `csrf_token` as the prefix of the field (e.g. define `{% block csrf_token_widget %} ... {% endblock %}` to customize the entire form field contents).

[Generating and Checking CSRF Tokens Manually](https://symfony.com/doc/8.0/security/csrf.html#generating-and-checking-csrf-tokens-manually "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Although Symfony Forms provide automatic CSRF protection by default, you may need to generate and check CSRF tokens manually for example when using regular HTML forms not managed by the Symfony Form component.

Consider a HTML form created to allow deleting items. First, use the [csrf_token() Twig function](https://symfony.com/doc/current/reference/twig_reference.html#reference-twig-function-csrf-token) to generate a CSRF token in the template and store it as a hidden form field:

Then, get the value of the CSRF token in the controller action and use the [isCsrfTokenValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php#:~:text=function%20isCsrfTokenValid "Symfony\Bundle\FrameworkBundle\Controller\AbstractController::isCsrfTokenValid()") method to check its validity, passing the same token ID used in the template:

Alternatively you can use the [IsCsrfTokenValid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Security/Http/Attribute/IsCsrfTokenValid.php "Symfony\Component\Security\Http\Attribute\IsCsrfTokenValid") attribute on the controller action:

Suppose you want a CSRF token per item, so in the template you have something like the following:

This attribute can also be applied to a controller class. When used this way, the CSRF token validation will be applied to **all actions** defined in that controller:

The [IsCsrfTokenValid](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Security/Http/Attribute/IsCsrfTokenValid.php "Symfony\Component\Security\Http\Attribute\IsCsrfTokenValid") attribute also accepts an [Expression](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/Expression.php "Symfony\Component\ExpressionLanguage\Expression") object evaluated to the id:

By default, the `IsCsrfTokenValid` attribute performs the CSRF token check for all HTTP methods. You can restrict this validation to specific methods using the `methods` parameter. If the request uses a method not listed in the `methods` array, the attribute is ignored for that request, and no CSRF validation occurs:

You can also choose where the CSRF token is read from using the `tokenSource` parameter. This is a bitfield that allows you to combine different sources:

* `IsCsrfTokenValid::SOURCE_PAYLOAD` (default): request payload (POST body / json)
* `IsCsrfTokenValid::SOURCE_QUERY`: query string
* `IsCsrfTokenValid::SOURCE_HEADER`: request header

Example:

The token is checked against each selected source, and validation fails if none match.

[CSRF Tokens and Compression Side-Channel Attacks](https://symfony.com/doc/8.0/security/csrf.html#csrf-tokens-and-compression-side-channel-attacks "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[BREACH](https://en.wikipedia.org/wiki/BREACH) and [CRIME](https://en.wikipedia.org/wiki/CRIME) are security exploits against HTTPS when using HTTP compression. Attackers can leverage information leaked by compression to recover targeted parts of the plaintext. To mitigate these attacks, and prevent an attacker from guessing the CSRF tokens, a random mask is prepended to the token and used to scramble it.

[Stateless CSRF Tokens](https://symfony.com/doc/8.0/security/csrf.html#stateless-csrf-tokens "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

Traditionally, CSRF tokens are stateful, meaning they're stored in the session. However, some token IDs can be declared as stateless using the `stateless_token_ids` option. Stateless CSRF tokens are enabled by default in applications using [Symfony Flex](https://symfony.com/doc/current/setup.html#symfony-flex).

Stateless CSRF tokens provide protection without relying on the session. This allows you to fully cache pages while still protecting against CSRF attacks.

When validating a stateless CSRF token, Symfony checks the `Origin` and `Referer` headers of the incoming HTTP request. If either header matches the application's target origin (i.e. its domain), the token is considered valid.

This mechanism relies on the application being able to determine its own origin. If you're behind a reverse proxy, make sure it's properly configured. See [How to Configure Symfony to Work behind a Load Balancer or a Reverse Proxy](https://symfony.com/doc/current/deployment/proxies.html).

### [Using a Default Token ID](https://symfony.com/doc/8.0/security/csrf.html#using-a-default-token-id "Permalink to this headline")

Stateful CSRF tokens are typically scoped per form or action, while stateless tokens don't require many identifiers.

In the example above, the `authenticate` and `logout` identifiers are listed because they are used by default in the Symfony Security component. The `submit` identifier is included so that form types defined by the application can also use CSRF protection by default.

The following configuration applies only to form types registered via [autoconfiguration](https://symfony.com/doc/current/service_container.html#services-autoconfigure) (which is the default for your own services), and it sets `submit` as their default token identifier:

Forms configured with a token identifier listed in the above `stateless_token_ids` option will use the stateless CSRF protection.

### [Generating CSRF Token Using Javascript](https://symfony.com/doc/8.0/security/csrf.html#generating-csrf-token-using-javascript "Permalink to this headline")

In addition to the `Origin` and `Referer` HTTP headers, stateless CSRF protection can also validate tokens using a cookie and a header (named `csrf-token` by default; see the [CSRF configuration reference](https://symfony.com/doc/current/reference/configuration/framework.html#reference-framework-csrf-protection)).

These additional checks are part of the **defense-in-depth** strategy provided by stateless CSRF protection. They are optional and require [some JavaScript](https://github.com/symfony/recipes/blob/main/symfony/stimulus-bundle/2.20/assets/controllers/csrf_protection_controller.js) to be enabled. This JavaScript generates a cryptographically secure random token when a form is submitted. It then inserts the token into the form's hidden CSRF field and sends it in both a cookie and a request header.

On the server side, CSRF token validation compares the values in the cookie and the header. This "double-submit" protection relies on the browser's same-origin policy and is further hardened by:

* generating a new token for each submission (to prevent cookie fixation);
* using `samesite=strict` and `__Host-` cookie attributes (to enforce HTTPS and limit the cookie to the current domain).

By default, the Symfony JavaScript snippet expects the hidden CSRF field to be named `_csrf_token` or to include the `data-controller="csrf-protection"` attribute. You can adapt this logic to your needs as long as the same protocol is followed.

To prevent validation from being downgraded, an extra behavioral check is performed: if (and only if) a session already exists, successful "double-submit" is remembered and becomes required for future requests. This ensures that once the optional cookie/header validation has been proven effective, it remains enforced for that session.

Note

Enforcing "double-submit" validation on all requests is not recommended, as it may lead to a broken user experience. The opportunistic approach described above is preferred, allowing the application to gracefully fall back to `Origin` / `Referer` checks when JavaScript is unavailable.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
