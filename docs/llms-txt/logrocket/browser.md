# Source: https://docs.logrocket.com/reference/browser.md

# Sanitize URLs

Scrub data from captured browser URLs

## Use the URL Sanitizer Function

`urlSanitizer`\
optional - *function*

Use urlSanitizer to scrub sensitive data from browser URLs.

You can redact from the URL and the query string, or remove the URL completely.   The modified URL will then be used for all dashboard searches and metrics. Make sure that you return the modified url from the function:

```javascript
LogRocket.init(YOUR_APP_ID, {
  browser: {
    urlSanitizer: url => {
      let sanitizedUrl = url;

      // redact the path following /ssn/ from the URL
      sanitizedUrl = sanitizedUrl.replace(/\/ssn\/([^\/]*)/i, '/ssn/REDACTED');

      // redact the value of the query parameter secret_key
      sanitizedUrl = sanitizedUrl.replace(/secret_key=([^&]*)/, 'secret_key=REDACTED');

      // make sure you return the sanitized URL string
      return sanitizedUrl;
    },
  },
})
```