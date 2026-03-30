# Source: https://docs.bugbug.io/editing-tests/tabs-and-iframes.md

# Tabs & iframes

BugBug <mark style="color:green;">**fully supports testing in iframes or multiple tabs**</mark>. This is handled automatically during the recording but can also be controlled manually. You will notice the `Switch context` action if you work with iframes or multiple tabs.&#x20;

### What is the "Switch context" action?

When you record something in a different tab or iframe, an additional step will be recorded before the actual action for switching the context to this new frame or tab.

This defines the context for all the following test steps until you switch the context again to a different frame or a tab.

### Locating the right frame

The first tab you visit during the test is `Tab number` **0** and `context` identified as **`Top`**. This is the **default text execution context**, and if you don't interact in your test with iframes or other tabs, you don't need to add the `Switch context` step.

{% hint style="info" %}
The **default** test execution context is `Tab number` **0** and `context` **Top,** and adding this at the beginning of the test is unnecessary.
{% endhint %}

If you navigate to different tabs or iframes during the test, they will be identified by:

* Tab number \[`number`]
* Context \[`Top`|`Iframe`]
* Frame element (if the context is `Iframe`)

Tabs are numerated from 0, so each frame you open during the recording session will have incremented numbers.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FHp8H9t7lmc42B4eFDViQ%2Fimage.png?alt=media&#x26;token=d76d29bc-932d-4a70-a918-6e23f8c041ff" alt=""><figcaption><p>Tab numbers starting from 0</p></figcaption></figure>

If the interaction **is not** in an `Iframe`, the context should be set to your default tab context: `Top`.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkI261Tzem4B3JxaUzRtU%2Fimage.png?alt=media&#x26;token=6b4b0b06-b8da-4852-9eff-c2b50e183fe2" alt=""><figcaption><p>Default tab context - Top</p></figcaption></figure>

If the interaction **is inside** an `iframe`, the context should be set to `Iframe` and the correct iframe selector is needed:

&#x20;

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FQxYKEMDDRDQhJMdlmSzv%2Fimage.png?alt=media&#x26;token=b6e95a58-d1fb-4dd0-a080-7abaaaa3f9c6" alt=""><figcaption><p>Switch to the iframe identified by XPath //IFRAME[id="frame1"] in the first browser tab (tab 0)</p></figcaption></figure>

BugBug also supports nested iframes during a regular recording session. You can read more about [nested selectors](https://docs.bugbug.io/preventing-failed-tests/selectors#nested-selectors) here.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FH2UElyfso2hgJytxmjiB%2Fimage.png?alt=media&#x26;token=9521698e-d222-450e-b1ce-ec7a799489a9" alt=""><figcaption><p>Switch test execution context to nested iframe</p></figcaption></figure>

A test scenario when you operate in your first tab, then in an iframe, in the nested iframe, and then again in the first tab looks like the below:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FyjjJ6gMBBGuk6dNYxf5F%2Fimage.png?alt=media&#x26;token=12914416-f901-424d-b5c5-7f5fd4bc64d9" alt=""><figcaption><p>Mixed test contexts</p></figcaption></figure>

If you have mixed contexts in your tests, it's important to remember which context you're in to make sure the test works correctly.
