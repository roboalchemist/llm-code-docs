# Source: https://docs.intelligems.io/general-features/css-and-javascript-injection.md

# CSS Styles and JavaScript Injection

This feature enables you to test custom CSS styles and JavaScript for specific test groups. You'll find it in the Modifications tab for Pricing, Shipping, Offer, Checkout, and Onsite Edits tests. For all other content tests, access it through the onsite widget.

To use the onsite widget's edit mode, first preview your test. When the preview appears, click the edit button in the bottom right corner of the widget. Then, click the `</>` button to enter edit mode.

<div data-full-width="false"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-665552e4dccaf0ae33faafda677f5481847d9005%2FScreenshot%202025-11-18%20at%202.12.32%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure></div>

## Editing the CSS of an Element

**Adding CSS in the Intelligems App:** Navigate to your test's Modifications tab and scroll to the Styles & Javascript accordion. Click to expand it.

**Adding CSS from the Onsite Widget:** Click the `</>` button on the widget to open a modal. You'll automatically start on the CSS tab.

**Styling Page Elements:** Select the test group you want to edit using the dropdown at the top of the accordion or modal. To add CSS to any element, locate its classname using the dev tools inspector. Need help finding classnames? Check out [this video](https://www.youtube.com/watch?v=rjWUzxMjCAU). Once you have the classname, you can modify that element's styles. See the example below.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9d0d779b8b8932f7964d7558ef6ce4d73b5a2f37%2FScreenshot%202023-09-20%20at%209.13.24%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Not comfortable writing CSS? Describe what change you want to make to have it AI generated!
{% endhint %}

## Editing the JavaScript

**Adding JavaScript in the Intelligems App:** Navigate to your test's Modifications tab and scroll to the Styles & Javascript accordion. Click to expand it, and select the JavaScript tab.

**Adding JavaScript from the Onsite Widget:** Click the `</>` button on the widget to open a modal and select the JavaScript tab.

**Adding JavaScript:** Select the test group you want to edit using the dropdown at the top of the accordion or modal. Enter the Javascript that you'd like to inject for the selected test group into the editor. You can also control when your custom JavaScript is injected into the page using the JavaScript Injection Timing dropdown.

The three injection timing mode options are:

* **Immediately**: Injected as soon as possible and loads at the same time as the rest of your content. Ideal for critical code that needs to run without delay.
* **After Page Load**: Injects when the page's content has fully loaded and is ready to use (after the DOM is loaded). Great for scripts that rely on the page’s structure.
* **Delay**: Delays injection by a set time (e.g., 1-2 seconds). A delay of 1-2 seconds is recommended for most users to improve page load speed for non-essential scripts.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-70acfbe64488f7c566f985b7b2d8eb2e90ba672c%2FScreenshot%202023-09-20%20at%209.25.33%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

### Interacting with the DOM

Injected JavaScript will execute according to the JavaScript Injection Timing that you've set up, which may be before the page has rendered. If you want to interact with the DOM with injected JavaScript, we recommend adding a listener, for example:

```javascript
function myDOMChanges() {
    document.body.setAttribute("data-my-change", "true");
}

if (document.readyState !== "loading") {
    // if the page is already ready, execute now
    myDOMChanges()
} else {
    // otherwise, add a listener
    document.addEventListener('DOMContentLoaded', () => {
        myDOMChanges();
    })
}
```

Our JavaScript only runs once per page, and often very early into the page lifecycle, so you may need to handle that situation as well (i.e., wrap the code in a `setInterval` or `setTimeout`).
