# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-checkout-blocks.md

# Testing Shopify Checkout Blocks

{% hint style="info" %}
You can now use Intelligems to power and test Checkout Experiences like trust badges, guarantees, and custom content in your checkout. Learn more about [testing-checkout-experiences](https://docs.intelligems.io/checkout/testing-checkout-experiences "mention")
{% endhint %}

### Introduction

Testing elements on the Checkout page is a functionality that many stores have been longing for. While Shopify still doesn't allow changes to their native components by 3rd party apps, stores on the Shopify Plus plan have access to the [Shopify Checkout Blocks app](https://apps.shopify.com/checkout-blocks), through which you can add custom blocks to checkout that can be controlled through an A/B Test in Intelligems.

### How It Works

The concept is straightforward: create blocks conditioned by a **cart attribute**, then use Intelligems' [JavaScript injection](https://docs.intelligems.io/general-features/css-and-javascript-injection) capability to set up a Content Test that controls the display of the checkout block for each test group.

See the example below for how you can test a block that **allows your customers to edit their items on Checkout**.

### Setup Instructions

#### Step 1: Create a Checkout Block

In the [Checkout Blocks app](https://apps.shopify.com/checkout-blocks), click on 'Blocks', then 'Create block'. In this example, we'll be selecting the 'Line item edit' block:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-746bbb95770f0113ec86758f4cc9f7d03e928bce%2F01%20-%20create%20block.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Step 2: Set up a Display Rule

The block will be conditioned to a cart attribute set through the test on Intelligems. Under 'Display Rules' click on 'Add display rule' and select 'Cart attributes'. Next, set 'Key' as '\_igShowBlock' and 'Value' as 'true':

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b79ba31f299d827e2dfb887eda43853a829f0b50%2F02%20-%20set%20attribute.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The key/value pair configured at this step is arbitrary. You can set a different attribute key and value if you like, as long as that matches the key and value you'll be setting up through your test.
{% endhint %}

#### Step 3: Activate your block and add it to Checkout

Follow the instructions on the Shopify Checkout Blocks app to activate your newly created block and add it to Checkout. Once the block is active, you'll open the Checkout editor, click the '+' icon next to 'Line item edit', and add it to the 'Information' section. Make sure to 'Save' your changes:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-52ff1fd2c8e664e7d0ad99c8a90a698780a8bee2%2F03%20-%20add%20to%20checkout.gif?alt=media" alt=""><figcaption></figcaption></figure>

When viewing your Checkout sections, you'll locate the block under 'Order summary > Items in cart'.

{% hint style="info" %}
In the editor, if you click on your newly added block, you'll see a few customization options, such as the button's styles and label.
{% endhint %}

You may now close the editor and go back to the Checkout Blocks app, where you'll close the popup where the editor steps are listed, and mark that step as done. Your block is now active, and you can proceed with the next steps on Intelligems:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-847c8e8281b34b2af82d379af4983a7c5821805a%2F04%20-%20mark%20as%20done.gif?alt=media" alt=""><figcaption></figcaption></figure>

#### Step 4: Create an Onsite Edits Test with a Javascript injection

On Intelligems, create a Content Test of the type 'Onsite Edits Test' (you may refer to the steps [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)), with two test groups - in this example, we will call the groups 'Block OFF' and 'Block ON':

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-dd1be8674d666d94a7358eb8c8c596661a3dfdd4%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Move on to the 'Modifications' tab, and expand the section 'Styles & Javascript'. Within it, switch to the 'Javascript' tab, and paste the following code for the group 'Block OFF':

```
const res = fetch("/cart/update.js", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    attributes: {
      '_igShowBlock': "false"
    },
  }),
})
```

Additionally, switch the setting 'Javascript Injection Timing' to 'Delay', with a value of '2500 ms'. This will ensure that the Javascript runs correctly across different devices and browsers, as we noticed some devices and browsers require this extra delay.

Here's a quick video on the steps you'll be taking:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b4b1b3a877c511f28a65d470c3329d2a95569e69%2Fcb-update-01.gif?alt=media" alt=""><figcaption></figcaption></figure>

Next, switch over to the group 'Block ON', and add the same code, but this time change the attribute's value from 'false' to 'true'. Also remember to set the 'Delay' to '2500 ms'. You may now 'Save' the test:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ba02f19b7b4a25aee4286ae0eed99004bbf5ed0a%2Fcb-update-02.gif?alt=media" alt=""><figcaption></figcaption></figure>

The code above will run for each test group, and add the '\_igShowBlock' attribute to the cart. In the group 'Block OFF', having the attribute's value set to 'false' will ensure that it is not displayed for visitors in that group. For the group 'Block ON', the attribute's value will be set to 'true', ensuring its display rule is met, so visitors in that group see the 'edit' option on Checkout.

#### Step 5: Preview your test

You can now preview your test the same way you preview any other Content Tests. Simply open the test's preview, add a product to the cart, and proceed to the Checkout page. As you switch test groups in the preview widget, the Javascript injected for the group will run, updating the value of the '\_igShowBlock' attribute in the cart and determining whether or not the block on Checkout will be displayed:

{% embed url="<https://www.loom.com/share/0b532524682c4b769aeeae2f6a1d7152>" %}

***

### Other Block types

The Shopify Checkout Blocks app offers various block types you can test:

* **Product Upsells**: Test additional product recommendations
* **Dynamic Content**: Test personalized checkout messaging
* **Custom Fields**: Test additional information collection
* **Promotional Blocks**: Test discount or shipping messaging
* As long as you set a **Display Rule** on your block, as done in Step 2 in this guide, you can test any checkout block type using the same methodology described above!

### Best Practices

* **Test one block at a time** to isolate the impact of each element
* **Monitor key metrics** like conversion rate and cart abandonment
* **Use sufficient sample sizes** for statistically significant results
* **Consider mobile experience** when testing checkout blocks
* **Set appropriate test duration** based on your traffic volume

### Measuring Success

Track these key performance indicators:

* Checkout conversion rate
* Cart abandonment rate
* Average order value
* Time spent on checkout page
* Customer satisfaction scores
