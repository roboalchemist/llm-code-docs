# Source: https://docs.bugbug.io/preventing-failed-tests/smart-scroll.md

# Smart scroll

BugBug simulates [real user clicks and mouse movements](https://docs.bugbug.io/preventing-failed-tests/smart-click), so the element needs to be visible in the viewport to actually click it.

BugBug will try to behave like a human: we will automatically attempt to scroll the page to see the element and interact with it.

**So you don't need to maintain the scroll actions!** :tada:

Your tests <mark style="color:green;">**will not fail**</mark> if:

* some content on the page changed and pushed the clickable element down outside of the browser viewport
* some fixed popup or an ad covered the element completely, but it is still reachable if you scroll more

{% hint style="info" %}
You can still [manually add scroll steps](https://docs.bugbug.io/editing-tests/manually-creating-the-test), for handling more complex scrolling and items with their own overflow scroll.&#x20;
{% endhint %}
