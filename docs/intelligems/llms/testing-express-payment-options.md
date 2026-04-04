# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-express-payment-options.md

# Testing Express Payment Options

### Introduction

Testing whether to offer express payment options (like PayPal, Klarna, Afterpay, etc.) on your checkout page can be done using Intelligems with [Shopify Checkout Blocks](https://apps.shopify.com/checkout-blocks). Because the Shopify Checkout Block app is only available for brands on the Shopify Plus plan, this type of test is only possible for brands on Shopify Plus.

### Setup Instructions

#### Step 1: Create an Onsite Edits Test

In Intelligems, create a Content Test using the 'Onsite Edits' test type with two test groups (or more if you are hoping to test multiple variations). For this example, we'll stick with two groups and name the groups "Express Payment On" and 'Express Payment Off". You'll save the test without creating any onsite edits - this test essentially gives you the ability to split your traffic into two test groups and track the results.

#### Step 2: Copy your Test Group's Test ID

You can find this information by clicking on the three dots in the top right of your test > Show Info > clicking on the 12 digit ID next to the line that says "Express Payment Off For Google Analytics:".

#### Step 3: Configure your Checkout Block

1. Head to the Checkout Block app in Shopify and select the "Functions" option from the left hand nav
2. Click "Create Function" in the top right, followed by "Hide" under "Payment"
3. Choose "Create from blank template"
4. Give your Function a title, and choose "Cart rules" under "Type"
5. Click "Add method", select which payment method(s) you'd like to hide from the dropdown, and click "Add rule"
6. Select "Cart attributes", set the "Key" as "igTestGroups" and paste the ID you copied from the Intelligems app in the Value field
7. Save your new Function and set the status to "Active" - it will only hide the payment method(s) when it finds the test group ID associated with your test group in the cart, which will not happen until you preview or start your test

{% embed url="<https://www.loom.com/share/f765433e1b2447f7b671b5f38d54d00d?sid=84698a8c-cf66-4312-b5b6-e11f5590d274>" %}

#### Step 4: Preview your Test

Preview your test like any other Content Test. Open the test preview, add a product to cart, and go to checkout. When switching test groups in the preview widget, empty your cart to ensure the correct Cart Attribute controls express payment display.

### Best Practices

* **Test one item on the checkout page at a time** to isolate the impact of each element
* **Monitor key metrics** like conversion rate and cart abandonment
* **Use sufficient sample sizes** for statistically significant results
* **Set appropriate test duration** based on your traffic volume

### Measuring Success

Track these key performance indicators:

* Checkout conversion rate
* Express payment usage
* Cart abandonment rate
* Average order value
