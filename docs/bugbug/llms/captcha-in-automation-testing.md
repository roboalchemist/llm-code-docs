# Source: https://docs.bugbug.io/troubleshooting/captcha-in-automation-testing.md

# CAPTCHA in automation testing

## What is CAPTCHA?

[CAPTCHA](https://en.wikipedia.org/wiki/CAPTCHA) makes test automation more difficult, as it was specifically designed to prevent automated bots from using your web app.&#x20;

For example, if you have a registration form, it might be protected by [reCAPTCHA](https://en.wikipedia.org/wiki/ReCAPTCHA) to prevent fake account registrations.&#x20;

<img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0BWcufBQr1bKceIB1aP7%2FScreenshot%202022-08-18%20at%2012.29.42.png?alt=media&#x26;token=a2e84b4a-e610-4cdd-9f9f-34834a698796" alt="" data-size="original">

## Disable the captcha on test environments

There are multiple captcha providers and each has a different way to disable it. For example, if you use reCAPTCHA you need to set a [special "site key"](https://developers.google.com/recaptcha/docs/faq#id-like-to-run-automated-tests-with-recaptcha.-what-should-i-do).

![Excerpt from the reCAPTCHA documentation](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkV5I3kFNTADKQiZc9RmQ%2Frecaptcha%20screenshot.png?alt=media\&token=c0638e49-aa0b-4abf-ab7a-1b5fe2303ed7)

## Allow BugBug to skip CAPTCHA during the automation testing

You can implement a special secret flag in your backend code to allow BugBug to skip the captcha.&#x20;

1. Add a custom header in your project settings with a secret string of your choice
2. On your backend code, add a condition, that the captcha is not required if the request header contains this secret string

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FsjHu2vHLkKdw6eVhkZjL%2Fcustom-headers%20\(1\).png?alt=media\&token=04d3550d-e540-4a2c-9234-d32815579f0e)
