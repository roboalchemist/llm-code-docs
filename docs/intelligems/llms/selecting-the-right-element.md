# Source: https://docs.intelligems.io/general-features/onsite-editor/selecting-the-right-element.md

# Selecting the Right Element

## Introduction

One of the most powerful abilities of Intelligems is the possibility to make simple, low-code edits to your site based on on-page elements that are already there through our Onsite Editor. These edits are built using a CSS selector, which is a pattern or rule used to identify and target specific HTML elements on a webpage for styling or manipulation.

{% hint style="warning" %}
**Ask Your Developer to Help:** Element selection can be tricky! A developer can help by adding IDs or attributes to make your Onsite Edit more reliable.
{% endhint %}

CSS selectors act like addresses that tell the browser exactly which elements to select from the HTML document. They can target elements based on:

* **Element type** (e.g., `div`, `p`, `h1`)
* **Class names** (e.g., `.header`, `.button`)
* **IDs** (e.g., `#navigation`, `#main-content`)
* **Attributes** (e.g., `[type="email"]`, `[data-id="123"]`)
* **Relationships** (e.g., parent-child, siblings)
* **States** (e.g., `:hover`, `:active`, `:first-child`)

**Common Examples:**

* `h1` - selects all heading 1 elements
* `.product-card` - selects all elements with class "product-card"
* `#hero-banner` - selects the element with ID "hero-banner"
* `button:hover` - selects buttons when hovered over
* `.container > .item` - selects direct child elements with class "item" inside elements with class "container"

Intelligems automatically generates CSS selectors through our point-and-click flow to help you target page elements quickly. However, since every website has a unique structure and specific targeting requirements, you may need to fine-tune these selectors to ensure your Onsite Edits display exactly where intended.

**Why selector adjustments might be needed:**

* Your site has a custom layout or unique element structure
* The automatically generated selector is too broad or too narrow for your goals
* Dynamic content requires more specific selectors

**Two ways to optimize your selectors:**

1. **Edit the selector directly** in the Intelligems interface by modifying the CSS selector string
2. **Update your site code** by having your developer add unique IDs or attributes to target elements

This guide will show you both approaches so you can choose the method that works best for your setup and ensure your Tests and Experiences trigger reliably across your site.

## How to Select an Element in Intelligems

When setting up a new Onsite Edit, you have several options for defining which CSS selector you'd like to target:

1. **Select an element:** This option will enable a point-and-click flow. Hover your mouse over your page to identify the element you want to edit. The available elements will have a blue highlighting appear around them and you can simply click to select one. Select which action you'd like to take from the dropdown that opens up to finish making your edit. You will see the CSS selector that was automatically created based on what you clicked on in the "Targeting selector" text box. If you find that your element isn't correctly identified, you can adjust it further to fit the exact one you want to target. Read more about selecting and adjusting your elements below under "How to Adjust Which CSS Selector is Used".
2. **Paste a selector:** This option will provide you with a text box where you can paste or type the CSS selector you'd like to target. Once you hit submit, you will be notified if this CSS selector matches more than one element, and if so, given the option to target all elements in the list or choose a specific one before setting up the necessary edits.
3. **Describe element to AI:** This option will provide you with a text box where you can describe the element you'd like to target. Once you hit submit, the AI will work to find the correct element and then you can set up the necessary edits.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-fcc24efcc30866a6ef811332f2a81f91663ae3cf%2Fchrome-capture-2025-9-22%20(2).gif?alt=media" alt=""><figcaption></figcaption></figure>

## How to Adjust Which CSS Selector is Used <a href="#h_41c38ccba2" id="h_41c38ccba2"></a>

In some cases, when you use the "Select an element" option, you may not see the correct element highlighted (with the blue or green outline). For example, you may be trying to edit the product title on one of your product pages, but see the product title on all pages highlighted, or vice versa. Our tool aims to pick the best possible CSS selector, but because we may not have all the necessary context, it might be necessary to manually adjust the CSS selector to accurately match the intended one.

You can adjust the CSS selector by editing the text found in the Targeting selector text box found in red below:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0e27178bb2d8e671b565ef45362838422c35c419%2FScreenshot%202025-09-22%20at%202.58.07%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

As you adjust the CSS selectors, the matching will be updated once you click out of the Targeting selector text box and the matching element(s) will show the green outline.

If you're having difficulty getting the correct CSS selector for your element through our point-and-click flow, you can use your browser's built-in developer tools to identify and copy it directly. Here are the steps to do that:

1. **Navigate to your target page** in a new browser tab where you want to add your Onsite Edit - you should not have the Intelligems Onsite Editor open in this tab.
2. **Open Developer Tools** using the keyboard shortcut:
   * Mac: `Command + Option + C`
   * PC: `Control + Shift + I`
3. **Activate the element picker** by clicking the "Select Element" icon (cursor arrow) in the top-left corner of the developer tools panel.
4. **Hover and select** your target element—you'll see elements highlight in blue as you move your cursor around the page. Click on the element you want to target.
5. **Fine-tune your selection** in the Inspector panel by hovering over nearby HTML elements until the correct element is highlighted on the page.
6. **Copy the selector** by right-clicking (or Ctrl+click) on the highlighted element in the Inspector and choosing "Copy > Copy selector".
7. **Paste into Intelligems** by returning to your tab with the Onsite Editor and pasting the selector into the targeting field, or use the "Paste a selector" option.

**Common adjustments needed:**

* **Too specific?** If no elements are found, or you are looking to target multiple similar elements, gradually remove parts from the beginning of the selector (delete up to the first space, repeat as needed) until it matches your target element(s).
* **Too broad?** If multiple unwanted elements are selected, look for unique identifying attributes like alt text, data attributes, or more specific class names to narrow it down. This is also a great opportunity to have your developer help by adding IDs or attributes to create a unique selector for you to target.

This method gives you a reliable starting point that you can then refine for your specific targeting needs.
