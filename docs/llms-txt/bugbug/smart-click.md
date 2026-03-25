# Source: https://docs.bugbug.io/preventing-failed-tests/smart-click.md

# Smart click

## Simulating real cursor clicks

BugBug simulates real clicks as if the user was moving a mouse. So if the element is not visible or covered by something else, it is not possible to click it.&#x20;

BugBug will not fake-click the elements with JavaScript events.&#x20;

## Smart preventing incorrect clicks

BugBug prevents randomly failed tests by being smart about clicking elements.

**1) BugBug will retry the click if the right element was suddenly covered**

After clicking an element, BugBug will check if the right item was clicked. This prevents a situation when the click event was received by a different element, for example, you wanted to click a button but it was covered by a cookie popup overlay or scrolled outside of the viewport.&#x20;

**2) BugBug will click the element even if it's partially covered**

Your test will not fail if the button is partially covered. BugBug will click the remaining visible button area.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FVNoXB6U1dc8WTNkxnlNv%2FScreenshot%202022-04-11%20at%2018.50.08.png?alt=media\&token=99d9f554-5666-4300-8054-4e2037ac945c)

## Smart position detection&#x20;

BugBug will first try to click the element in the center, but if this will not work, BugBug will automatically find different coordinates for clicking an element, that is not covered by anything else and is visible on the screen.&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F1tGZQKG3XgqKjjAymLSp%2FScreenshot%202022-04-11%20at%2018.40.32.png?alt=media\&token=5967df3b-26a4-47a5-8046-17c148eed278)
