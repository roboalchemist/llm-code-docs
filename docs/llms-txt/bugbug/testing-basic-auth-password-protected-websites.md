# Source: https://docs.bugbug.io/troubleshooting/testing-basic-auth-password-protected-websites.md

# Testing basic auth password protected websites

## Websites with basic authentication

BugBug allows you to test websites that require a *basic authentication* password.

Basic authentication or "basic auth" is a simple way to protect a website from being viewed before you publish it. Developers often use it to hide the testing environment from the external world. That means that when you enter an URL you need to provide a username and password.

{% hint style="info" %}
**Important!** BugBug will not automatically record this step. You need to manually add "basic auth" to the "Go to URL" step. See below.
{% endhint %}

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FM71m8oVozyT9IPWRedz7%2Fbasic-auth-example.png?alt=media\&token=909b6725-c343-4fc9-9c9c-4642e2b332d0)

## Add basic auth to "Go to URL" step

1. &#x20;[Manually add](https://docs.bugbug.io/editing-tests/manually-creating-the-test) a "Go to URL" action
2. Click it to see the details on the right-hand side
3. Click "Password protected"
4. Enter the username and password here
5. Save the step
6. [Run the test](https://docs.bugbug.io/running-tests) to see if the page is loaded correctly

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fl0zHX8hGNJaAMXHCnrsF%2Fimage.png?alt=media&#x26;token=494189e1-0104-4b35-9cb1-1f6cab89b804" alt=""><figcaption></figcaption></figure>
