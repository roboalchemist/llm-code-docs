# Source: https://docs.bugbug.io/troubleshooting/prohibited-behaviors.md

# Prohibited behaviors

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

## You cannot minimalize the test window&#x20;

If there is a test in progress, you cannot minimize the window that is running the local test. **Minimizing** the browser window has some limitations from the Chrome browser, which puts the minimized tab into standby mode. In this case, the JS code is not executed, so the **test stops** automatically.\
\
If you want to run tests without disrupting your work, you can run tests in the cloud.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fg6ozQFnZjNaceU72ujfi%2FProjekt%20bez%20tytu%C5%82u.png?alt=media&#x26;token=831ea469-6935-4a9e-9843-44efe24f54bc" alt=""><figcaption></figcaption></figure>

## BugBug doesn't support multiple windows

BugBug does not support multiple windows for recording and running tests. You are able to record tests with multiple tabs, but if your app use for example *window\.open()* or 3rd party popups BugBug will not handle them. We have that on our roadmap.&#x20;

## LastPass extension modifies DOM&#x20;

If you use the LastPass extension during recording, you may have some problems with element selectors. As we know, LastPass changes the DOM of your page, so also selectors can be different. This can cause a failed test if you run it in cloud mode or another person will perform a local test on a different browser. Please disable the LastPass extension for incognito mode before recording or editing a test.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FofOak3Rce90kDiahRVUZ%2FLastPassLogoShadow.png?alt=media&#x26;token=6c7a6695-528c-42cb-96f3-4a3ef7840b5a" alt=""><figcaption></figcaption></figure>
