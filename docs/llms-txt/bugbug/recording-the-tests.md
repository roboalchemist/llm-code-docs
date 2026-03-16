# Source: https://docs.bugbug.io/creating-tests/recording-the-tests.md

# Your first test

## Learn the basics

If you're new to test automation, see our "[**how to" guide -->**](https://docs.bugbug.io/in-depth-guides/beginners-tutorial-to-automation-testing)

{% hint style="success" %}
[Read how to prepare your app for automated testing and avoid common pitfalls.](https://docs.bugbug.io/best-practices#how-to-prepare-your-app-for-testing)
{% endhint %}

## Create your first test

1. Think upfront of what do you want to test - choose a one simple use case
2. Create a new test
3. Enter the URL of the web app or website that you want to test
4. Click "Record" - if you [installed the extension](https://docs.bugbug.io/quick-start/install-chrome-extension), the incognito Chrome browser window should appear
5. Carefully click the elements to navigate - each click will be recorded automatically
6. Don't forget that [hovers are not automatically recorded](https://docs.bugbug.io/recording-tests-steps/recording-hover)
7. When you are ready with the test case click the `Finish and close` button in the [overlay menu](https://docs.bugbug.io/recording-tests-steps/bugbug-test-recorder) on the right
8. Now run the test to see if everything was correctly recorded

{% hint style="danger" %}
**Hovers are not automatically recorded!** You need to [record in hover mode](https://docs.bugbug.io/recording-tests-steps/recording-hover) by activating it in the [recording overlay](https://docs.bugbug.io/recording-tests-steps/bugbug-test-recorder).
{% endhint %}

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FSVabXzKBYBD13XBpARXb%2FZrzut%20ekranu%202023-03-15%20111506.png?alt=media&#x26;token=666c3f5f-1460-4356-ab3a-876d472f812b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FBqslGIjETFsBom7hUYzM%2Fbugbug-guide-03.png?alt=media&#x26;token=615cce9b-0b80-4f8b-a8a8-e45408e80b50" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FDeGHovPyw9Qrv7z34cpS%2Fbugbug-guide-05.png?alt=media&#x26;token=41721452-19c2-4783-899e-a7df658e1871" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fa5JQwTklQleOtHB4KEy0%2Fbugbug-guide-11.png?alt=media&#x26;token=60d8e1cb-5be5-4e95-acdb-498ec187f837" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
BugBug recording does not support multiple browser window testing. You can only record in one window, but we support multiple tabs and user movement between them.
{% endhint %}

## Manually reviewing and adding steps after the recording

You don't need to use recording, you can also create your tests step by step by adding particular actions and their parameters. This is however much slower!&#x20;

You can [manually edit steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test) anywhere in your test by clicking the plus symbol between the rows.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FhCzAvhQrc6DallYjtFxs%2FScreenshot%202022-04-07%20at%2016.41.49.png?alt=media\&token=90844dd1-fe78-47a6-b6d2-b1239234ec97)

You can modify the particular step when some element is not correctly caught by the BugBug's recording. Edit, run the test again, and check if it is working!&#x20;
