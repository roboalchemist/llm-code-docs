# Source: https://docs.intelligems.io/checkout/testing-checkout-experiences.md

# Testing Checkout Experiences

Intelligems enables your org to run real-time split tests on different Checkout Experiences. This article will walk you through how to run a Checkout Experience Test with Intelligems and some best practices.

### Understanding Checkout Experience Tests

There are two main ways to test blocks in your checkout:

1. **Location Testing:** Test the same block in different positions on your checkout page (e.g., top of the page vs. below the order total)
2. **Content Testing:** Test different block designs or messaging in the same location

The setup process in Shopify differs slightly depending on which type of test you're running (see Steps 4 and 5).

### Step 1: Create a New Test

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click **Create New Test** above the experiments table. Select **Checkout Experience Test** and then **Create Test**.

### Step 2: Enter the Test Details

Fill in the **Test Name** and **Test Description** for the experiment you are creating. This information is all internal; the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

**Example test names:**

* "Header vs. Below Total Location Test"
* "Green vs. Blue vs. Red Transformation Badge"
* "Warranty Badge Content Test Q4"

You will also select your **primary goal**. This will not affect what data is tracked or available to view, but will allow Intelligems to display analytics so that the most important information is surfaced first.

**Common goals for Checkout Experience tests:**

* Checkout conversion rate
* Order completion rate
* Revenue per visitor
* Average order value

### Step 3: Create Your Test Groups

Create between two and five groups to include in the test by clicking on the '+' button. Name the groups for the experiment and use the slider at the bottom of the page to allocate what percentage of traffic will go to each group.

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

### Step 4: Configure Checkout Experiences for Each Group

Once you've created your groups, go to the **Modifications** step. Here's where the setup differs based on your test type.

#### For Location Tests

When testing the same block in different locations, each test group needs:

* The same block design, colors, text, and icons
* A **different Location ID** for each position

**Example:** Testing a "High Quality Guarantee" badge in two locations:

* **Main Group:** Create a block with Location ID `badge-main`
* **Below Total Group:** Create the same block design with Location ID `badge-below-total`

The content looks identical, but the different Location IDs allow you to place them in different positions on your checkout.

#### For Content Tests

When testing different content in the same location, each test group needs:

* Different block designs, colors, text, or icons
* The **same Location ID** across both blocks

**Example:** Testing three color variations of a guarantee badge:

* **Green Group:** Green badge with Location ID `guarantee-badge`
* **Blue Group:** Blue badge with Location ID `guarantee-badge`
* **Red Group:** Red badge with Location ID `guarantee-badge`

Since all groups share the same Location ID, you only need to add one block to your Shopify checkout.

#### Creating Experiences for Each Group

For each test group:

1. Click into the group's modifications
2. Add a Checkout Experience modification
3. Configure the block content and styling
4. Set the appropriate Location ID based on your test type
5. Save the group

**Optional:** You can also leave one group as a control with no modifications to measure the impact of having any block at all.

### Step 5: Add Blocks to Shopify Checkout

This is where the setup differs significantly based on your test type.

#### For Location Tests: Add Multiple Blocks

Since you're testing different positions, you need to add a separate Intelligems block for each location you're testing.

**Setup process:**

1. In Shopify, go to **Customize** → **Checkout**
2. For the first location (e.g., main):
   * Navigate to that position in the checkout editor
   * Click **Add block** and select **Intelligems A/B Testing**
   * Copy the Location ID from your first test group (e.g., `badge-main`)
   * Paste it into the **Location ID** field in the block settings
   * Toggle on **Include block in Shop Pay** (recommended)
   * Position the block exactly where you want it (you can drag to reorder)
3. For the second location (e.g., below total):
   * Navigate to that position in the checkout editor
   * Click **Add block** and select **Intelligems A/B Testing**
   * Copy the Location ID from your second test group (e.g., `badge-below-total`)
   * Paste it into the **Location ID** field in the block settings
   * Toggle on **Include block in Shop Pay** (recommended)
   * Position the block exactly where you want it (you can drag to reorder)
4. Save your checkout customization

**Important:** Add all test location blocks before starting your test. Each position needs its own Intelligems block with the corresponding Location ID.

#### For Content Tests: Add One Block

Since all variations use the same Location ID and appear in the same position, you only need to add one Intelligems block.

**Setup process:**

1. In Shopify, go to **Customize** → **Checkout**
2. Navigate to where you want the block to appear
3. Click **Add block** and select **Intelligems**
4. Copy the shared Location ID from any of your test groups (they're all the same)
5. Paste it into the **Location ID** field in the block settings
6. Toggle on **Include block in Shop Pay** (recommended)
7. Position the block where you want it
8. Save your checkout customization

That's it! Intelligems will automatically show the correct variation to each visitor based on their test group assignment.

#### Why This Is Safe

A key advantage of Intelligems Checkout Experiences: **Adding blocks to your Shopify checkout doesn't make them immediately visible to customers.**

Unlike typical Shopify checkout changes that go live immediately, Intelligems blocks only appear when:

* The test is started in Intelligems, OR
* An Experience containing that block is activated

This means you can safely add all your test blocks to Shopify checkout, configure them, and preview them without any risk of customers seeing them before you're ready.

If a Location ID isn't associated with an active test or Experience, it simply won't appear on the checkout page.

### Step 6: Set Up Targeting If Needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using Intelligems' random split-test mechanism. This assignment is determined at the first visit and is stored via a first-party cookie, ensuring that the visitor remains in the same group on subsequent visits during the test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* **Audience Targeting:** Limit your users based on their device, country, UTM parameters, landing page URL, new/returning status, cookies, and much more.
* **Currency Targeting:** Limit your test to a single currency and/or a list of specific countries.
* **Mutual Exclusion:** Prevent users from being targeted by related experiments to reduce undesired interactions under the [Mutually Exclusive Tests](https://docs.intelligems.io/general-features/targeting/mutually-exclusive-experiments) option.

You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting).

{% hint style="warning" %}
**A note on targeting: If you had any targeting options set on the Offer Experiences you used to define your test groups, these will be ignored in lieu of test-level targeting.**

* Experience-level audience targeting is ignored. The audience targeting used on the test (or lack thereof) is used in its place.
* Experience-level currency targeting is ignored. The currency targeting used on the test (or lack thereof) is used in its place.
* Experience-level page targeting is ignored. The page targeting used on the test (or lack thereof) is used in its place.
  {% endhint %}

### Step 8: Start Your Test

Once you have completed all the steps, you'll be able to save your test with the button in the bottom right. You can then start it whenever you're ready.

### Common Test Scenarios

#### Scenario 1: Location Test (Same Content, Different Positions)

**Goal:** Determine which checkout position drives better conversion

**Setup:**

* 2 test groups: "Header" and "Below Total"
* Both groups have identical block design
* Different Location IDs: `badge-main` and `badge-below-total`
* Add 2 Intelligems blocks to Shopify checkout (one in each position)

**Example:** Test whether a "High Quality Guarantee" badge performs better above the contact information or below the order total.

#### Scenario 2: Content Test (Different Designs, Same Position)

**Goal:** Determine which design or messaging performs best

**Setup:**

* 3+ test groups: "Green Badge", "Blue Badge", "Red Badge"
* Different block designs with varied colors, text, or icons
* Same Location ID across all groups: `guarantee-badge`
* Add 1 Intelligems block to Shopify checkout

**Example:** Test which color variation of a "Quality Guarantee" drives the most conversions.

#### Scenario 3: Presence Test (Block vs. No Block)

**Goal:** Measure whether having a block improves conversion

**Setup:**

* 2 test groups: "Control" (no block) and "Trust Badge"
* Control group has no modifications
* Test group has a Checkout Experience with Location ID `trust-badge`
* Add 1 Intelligems block to Shopify checkout

**Example:** Test whether adding a warranty badge increases conversion compared to having no badge at all.

#### Scenario 4: Multi-Block Test

**Goal:** Test complete checkout layouts with multiple blocks

**Setup:**

* 2 test groups: "Single Badge" and "Triple Badge"
* First group has one block
* Second group has three blocks (each with unique Location IDs)
* Add appropriate number of blocks to Shopify for each variation

**Example:** Test whether one prominent badge performs better than three smaller badges distributed across checkout.
