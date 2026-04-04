# Source: https://docs.bugbug.io/quick-start/install-chrome-extension.md

# Install Chrome extension

### Why do you need the extension?

To run and record the tests, BugBug requires you to install a BugBug Chrome Extension and enable it in Incognito mode.

### Why does the extension require incognito mode?

All your tests should be independent of each other. Every test should begin with a **clean session, without any cookies, cache, localStorage, etc.** To achieve this BugBug runs the tests in incognito mode. Every time you run the test, the previous incognito session is closed and a new incognito window opens, with a completely clean session.

### Install the extension

Go to [BugBug Extension on the Chrome Webstore](https://chrome.google.com/webstore/detail/bugbug-no-code-test-autom/oiedehaafceacbnnmindilfblafincjb/related) and install it.

![If you try to run or record the test without the extension you will see a prompt](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fkwl3iaM0fzv5Ji7v1QrA%2FScreenshot%202022-04-07%20at%2014.48.24.png?alt=media\&token=3072bb20-8367-4d44-aeb4-61cb7fbabcdb)

![https://chrome.google.com/webstore/detail/bugbug-no-code-test-autom/oiedehaafceacbnnmindilfblafincjb/related](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FALDLrppRVkKuaNoMXf9g%2FScreenshot%202022-04-07%20at%2014.48.34.png?alt=media\&token=7a5e071b-b25f-4ea0-9844-25ba46b385ed)

### Enable the extension in incognito mode

![If you don't enable the extension in incognito mode, you will ba asked to do so before running a test](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F6eLSsZYC9RKvB0NlhN7r%2FScreenshot%202022-04-07%20at%2014.49.06.png?alt=media\&token=019b459b-b55f-49f3-960d-4b93e5aab030)

1. Go to extension settings by clicking the "Go to extension settings" button or use the link below

`chrome://extensions/?id=oiedehaafceacbnnmindilfblafincjb`

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDTMw0qB0RKMgqGjqJEz9%2FScreenshot%202022-04-07%20at%2014.57.41.png?alt=media\&token=f09bfd21-70d9-4715-aac6-039905eb1315)

2\. Scroll down, then enable the switch near "Allow in Incognito"

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FZKqLbTNOhoxAyEdhJ8KL%2Fimage.png?alt=media\&token=b8baca1f-2fbb-4e56-adcf-219e5cc1d02a)

**That's it! You're ready to run and record the tests now.**

***

#### \[Opera Only] Allow access to search page results

The BugBug extension requires the 'Allow access to search page results' permission to function properly in Opera. When this option is disabled, Opera blocks access to sandboxed iframes, such as reCAPTCHA. Therefore, attaching to tabs containing these types of frames is not allowed.

{% hint style="info" %}
We take your privacy seriously. This permission is used solely for recording and running tests.\
We never collect, store, or share your search queries or personal data.
{% endhint %}

1. Go to extension settings by clicking the "Go to extension settings" button or use the link below

   `chrome://extensions/?id=oiedehaafceacbnnmindilfblafincjb`&#x20;
2. Scroll down, then enable the switch near "Allow access to search page results"

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FbYjT9lCWPJTdlEHbIypj%2Fbugbug-incognito-enable-screen%20-%20opera%2004.11.2025.png?alt=media&#x26;token=3090b95e-d8be-4c19-877d-465ac58f94ed" alt=""><figcaption></figcaption></figure>
