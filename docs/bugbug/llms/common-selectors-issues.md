# Source: https://docs.bugbug.io/troubleshooting/common-selectors-issues.md

# Common selectors issues

### How to create good selectors for apps with tables and interactive lists? <a href="#how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists" id="how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists"></a>

Here's a typical problem to solve: you have an app with list of orders in a table. Each row has a checkbox in it. You want to create a test automation that clicks the checkbox in the second row.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F2bOPxr5oz0IdoMLvfbfw%2Fimage.png?alt=media&#x26;token=fddc3962-377d-41d9-ac65-60bfe78d3b44" alt=""><figcaption><p>The above example comes from an <a href="https://marmelab.com/react-admin-demo/#/commands">open-source demo app</a></p></figcaption></figure>

The problem is that there is no way to write a unique selector directly to this checkbox. There are more checkboxes on the list and we don't want to rely on the order of elements. We don't want the second checkbox, we want a *specific* checkbox.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkyW2Ic5RtzXSwWcXSSGs%2Fimage.png?alt=media&#x26;token=c57d0b25-5218-4749-9f56-5593330b7481" alt=""><figcaption></figcaption></figure>

There is nothing unique in the HTML element itself. Wait, is that class attribute unique? It is, but it's not good for test automation selectors. It's a random string that changes with every app deployment.&#x20;

**‍XPath traversing comes to the rescue!**\
We will guide you step by step how to create a reliable selector, that first identifies the right row in the table and then finds the checkbox inside. The result selector will "traverse" the parents and children in 3 steps.

1. Find a specific text in the table

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FJo9gLsyLr1bsRajPkDqH%2Fimage.png?alt=media&#x26;token=abed7b48-2a7a-417a-aab3-d68a019c66ff" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FG0Nz2SAvuwV80BMXivO3%2Fimage.png?alt=media&#x26;token=c6b89c04-5e01-4251-a566-a201bae5741a" alt=""><figcaption></figcaption></figure>

2. Find the parent table row by searching ancestors of the element from step 1

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FjyUxk28BK9g5A8yRnnP4%2Fimage.png?alt=media&#x26;token=e94cb47c-9759-4b16-ac7a-ab716c55093f" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F7fcduEHDCGlxpK3bNDZ8%2Fimage.png?alt=media&#x26;token=396c244a-48df-43cb-8e0a-ceb26c22dfff" alt=""><figcaption></figcaption></figure>

3. Find the checkbox inside the row

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FiMru6svHlAGBKttMELn9%2Fimage.png?alt=media&#x26;token=2321bb6f-39c5-4623-9dc8-d204e62cce8d" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FkBJ0NUCavGSuTWDDpbBm%2Fimage.png?alt=media&#x26;token=1788810f-fc03-4723-b2f6-008f950fc681" alt=""><figcaption></figcaption></figure>

Here's how to do this with our no-code tool. You need to use "Then find..." button and connect these 3 steps into one sophisticated and powerful XPath selector:

{% code overflow="wrap" %}

```
//*[contains(text(), "KYDGHM") ]/ancestor::tr/descendant::input[​@type="checkbox"]
```

{% endcode %}

You can apply the same technique to multiple other test cases.

### Capitalization of selectors values matters <a href="#capitalisation-matters" id="capitalisation-matters"></a>

Make sure your selector uses the same capitalisation of characters as in the page. Pay attention to uppercase and lowercase letters! Ideally copy-paste the text from HTML via Chrome developer tools.

### My selector works on desktop but doesn't work on mobile. Why? <a href="#my-selector-works-on-desktop-but-doesn-t-work-on-mobile.-why" id="my-selector-works-on-desktop-but-doesn-t-work-on-mobile.-why"></a>

Your app may have 2 different button "duplicates", one dedicated for desktop and one for mobile. One is always hidden, depending on the window width.

In such situation, the best solution is to create 2 separate tests for mobile and desktop with 2 different selectors.

Or try refactoring the code so that there is only one button present at a time - not hiding, but removing the button from the document.

You can also try to write a clunky selector that matches the 2 buttons, but somehow remove the hidden button with the `not` operator, for example:

{% code overflow="wrap" %}

```markup
//button[contains(text(), "Example") and not(ancestor::div[contains(@style, 'display:none')]) and not(ancestor::div[contains(@style, 'display:none')])]
```

{% endcode %}

### How to check if your selector works in Chrome? <a href="#how-to-check-if-your-selector-works-in-chrome" id="how-to-check-if-your-selector-works-in-chrome"></a>

In the [above example](#how-to-create-good-selectors-for-apps-with-tables-and-interactive-lists) we created a selector, now we should check if it works.

1. Open this [demo app](https://marmelab.com/react-admin-demo/#/commands) and login with "demo / demo", then go to "Orders" tab
2. Open Chrome developer tools
3. Click Ctrl+F to open the "Find" box (Cmd+F on Mac)
4. Paste the selector
5. Click enter
6. The matching element will be highlighted
7. Click enter several times to make sure that this is the only element that has a match

Here's a quick video that shows the whole XPath selector verification process in Chrome:

{% embed url="<https://www.youtube.com/watch?v=GiZGk7LYjaA>" %}
