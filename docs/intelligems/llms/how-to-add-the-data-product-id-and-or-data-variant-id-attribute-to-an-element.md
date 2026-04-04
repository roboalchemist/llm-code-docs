# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element.md

# How to Add the data-product-id and/or data-variant-id Attribute to an Element

### Background

One of the most common issues we see when completing the Intelligems Price Testing integration is that a price on your website that is included in your test is not updating in preview mode, or is highlighted in blue when it should be highlighted in green. This help guide will walk you through what theme change needs to be made to resolve this issue.

### **Step 1: Inspect the price that is not working**

On the price that is not updating, right click and select 'Inspect' from the menu. This will open up the developer tools in the same window.

### **Step 2: Find a unique combination of classes, IDs, and/or attributes**

In the developer tools, the element you are inspecting should be highlighted. In one of the **parent** elements for the price that is not updating, find a unique combination of classes, IDs, and/or attributes. In the screenshot below, `intelli-price intelli-span_USD_37.04`would be a good spot to start. However, you're not looking for this intelli-price class; you're looking for the `price-container__price` class in this case.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-28f080c7f4bd088552cc27482ddb45e0df88fd70%2FScreenshot%202024-03-01%20at%203.07.23%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>

### **Step 3: Download the 'Shopify Theme File Search by EZFY' Chrome extension**

If you don't already have it, this Chrome extension will be extremely helpful! You can download it [here](https://chrome.google.com/webstore/detail/shopify-theme-file-search/mhchmhfecfdpaifljcfebnlaiaphfkmb).

### **Step 4: Open the code editor in Shopify**

In another window, got to your Shopify admin account and select 'Sales Channels' > 'Online Store' > the three dots next to the theme you are integrating with > ' Edit code'.

### **Step 5: Search the files**

Once in the theme file of your choice navigate to the `edit code` option of the themes dropdown. \\

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d7828af81e713f8e58659794d46243ae72706bf0%2FScreenshot%202023-08-24%20at%2011.09.38%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

The Chrome extension you just downloaded should render a search box at the top of your screen like the one in the screenshot below once you are in the code editor. If you don't see it, you may need to refresh, or exit the code editor and come back by repeating the step above.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1966cd25c6e279ddf8de4b9a682ab501dadaef90%2FScreenshot%202023-08-24%20at%2011.12.07%20AM.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

In that search box, enter the unique combination of classes, IDs, and/or attributes that you found while inspecting your price in step 2. (It was `price-container__price` in the example above; yours will vary.) This will search all of your files, and any files that contains a match will be highlighted in blue.

{% hint style="danger" %}
If no matches are found, search for a smaller portion of the text.
{% endhint %}

### **Step 6: Search each .liquid file to find the text**

For each highlighted file with a .liquid extension, open the file and use keys Cmd + F to search the file for the text.

### **Step 7: Find the closest HTML open tag to the text.**

An opening tag begins a section of page content. To find the closest one to the text,

1\. Start from the highlighted text that you searched for.

2\. Keep moving left until you see an open tag.

3\. If there is no open tag directly to the left of the text, move one line up and start from the right end.

### **Step 8: Insert a data-product-id and/or data-variant-id snippet.**

Once you have found the closest HTML open tag, making sure there are spaces before and after, insert a data-product-id or data-variant-id snippet after the open tag using the below guidelines. Replace `product` with `variant` where necessary. With proper space, it should look similar to this:

```html
<span data-product-id="{{ product.id }}" class="{{ … }}"
```

1\. If there's code nearby where 'product' is being used (e.g. `{{ product.title }}`), insert `data-product-id="{{ product.id }}"`. If you don't see anything about 'product', go to number two.

2\. If you see a value that is being used like `product` but is named something else, replace `product.id` with `<whatever custom name>.title` in the data-product-id snippet. If you don't see any usage of 'product' or something similar in the file, go to number three.

3\. Try adding `data-product-id="{{ product.id }}"`. Save the file and go back to the window with your site open. Refresh and see if the price is now working. If not, please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help.
