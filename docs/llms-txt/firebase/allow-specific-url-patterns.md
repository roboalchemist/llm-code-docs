# Source: https://firebase.google.com/docs/dynamic-links/allow-specific-url-patterns.md.txt

<br />

| **Note:** Firebase Dynamic Links is*deprecated* and should not be used in new projects. The service will be shutting down soon. Follow the[migration guide](https://firebase.google.com/support/dynamic-links-faq#how_should_i_migrate_from_the_service)and see the[Dynamic Links Deprecation FAQ](https://firebase.google.com/support/dynamic-links-faq)for more information.

To prevent unauthorized parties from using your API key to createDynamic Linksthat redirect from your domain to sites you don't own, you should specify the URLs yourDynamic Linkscan redirect to.

To specify the allowed URLs, clickmore_vert**\> Allowlist URL pattern** from theDynamic Linkspage of theFirebaseconsole, and then specify up to 10 regular expressions using[RE2 syntax](https://github.com/google/re2/wiki/Syntax). Only URLs that match one of these regular expressions can be successfully used as a deep link (`link`) or fallback link (`afl`,`ifl`,`ipfl`,`ofl`) for aDynamic Links. If you specify URL patterns, any URL that doesn't match one of the patterns will cause yourDynamic Linksto return HTTP error 400.

You should make your URL patterns as restrictive as possible. For example:

|                                 Too permissive                                 |                                                                Better                                                                 |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| `^https://.*.com/.*$` Can redirect to any page on any site ending with`.com`.  | `^https://mybrand\.com/.*$` Can redirect only to pages at`mybrand.com`.                                                               |
| `^https://play.google.com/.*$` Can redirect to any app'sGoogle PlayStorepage.  | `^https://play\.google\.com/.*id=myapp\.com$` Can redirect only toGoogle PlayStorepages for the app with the package name`myapp.com`. |
| `^https://itunes.apple.com/.*$` Can redirect to any page on`itunes.apple.com`. | `^https://itunes\.apple\.com/.*id123$` Can redirect only to the App Store page for the app with the ID`id123`.                        |

You can make sure a deep link and fallback links for aDynamic Linksmatch one of your URL patterns by viewing the debug page forDynamic Linksand verifying there are no warnings:  

```
https://example.page.link/WXYZ?d=1
```