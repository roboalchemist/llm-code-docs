# Source: https://docs.intelligems.io/checkout/getting-started-with-checkout.md

# Getting Started with Checkout Experiences

{% hint style="success" %}
**Shopify Plus Required**

Checkout Experiences require a Shopify Plus account. This is a Shopify limitation - adding app blocks on the checkout page are only available to Shopify Plus merchants. If you're not on Shopify Plus, you'll see a message in the Intelligems app letting you know this feature isn't available.
{% endhint %}

## What are Checkout Experiences?

Checkout Experiences help you add custom content blocks to your Shopify checkout page to build trust, reduce cart abandonment, and improve conversion rates. These blocks appear directly on the checkout page where customers complete their purchase.

With Checkout Experiences, you can:

* Add trust badges to build customer confidence
* Display security guarantees and certifications
* Show warranty information
* Highlight shipping and return policies
* Add custom callouts and messaging
* Test different checkout content to see what converts best

## How to Access Checkout Experiences

You can find the Checkout Experiences feature in your Intelligems dashboard:

1. Log into your Intelligems account
2. Navigate to the Checkout Experiences section
3. Click "Create New Checkout Experience" to get started

## Types of Blocks

Intelligems currently supports static blocks with image and text content. These are perfect for content that doesn't need to change based on cart contents or customer behavior.

### 1. Trust Badge Layout

Trust badges display icons with text to highlight key selling points, guarantees, or security features.

**When to use it:**

* You want to highlight security, warranties, or guarantees
* You need to build customer confidence at checkout
* You want to reduce checkout abandonment

**How it works:**

* Add multiple badges with icons and text
* Customize colors, spacing, and layout
* Arrange badges in rows or columns

**Example:** Display badges for "Lifetime Warranty," "Secure Checkout," and "Free Returns"

### 2. Callout Layout

Callouts create focused messaging blocks with optional headings, body text, and icons.

**When to use it:**

* You want to highlight a single important message
* You need to communicate shipping information
* You want to promote a special offer or guarantee

**How it works:**

* Add a heading and body text
* Include icons for visual interest
* Customize colors and spacing

**Example:** "Free Shipping on Orders Over $50" with a shipping icon

### 3. Static Image

Static images allow you to add custom graphics to your checkout.

**When to use it:**

* You have custom-designed graphics
* You want complete control over the visual design
* You need to display logos or certifications

**How it works:**

* Upload your image
* Position it on the checkout page
* Set sizing and spacing

**Example:** Payment security badges or industry certifications

## Setting Up Your First Checkout Experience

Follow these steps to create and activate a block:

### Step 1: Choose Your Block Type and Name It

1. Go to Checkout Experiences in your dashboard
2. Click "Create New Checkout Experience"
3. Select a layout type (Trust Badge, Callout, or Static Image)
4. Give your experience a clear, descriptive name (like "Lifetime Warranty Badge" or "Security Trust Badges")

### Step 2: Understanding Block Structure

Before diving into configuration, it's helpful to understand what makes up a block.

#### **What's in a Badge?**

Each badge in your block contains three elements:

1. **Icon/Image** - A visual element (icon from the library or custom image)
2. **Title** - The main text for the badge (e.g., "Lifetime Warranty")
3. **Subtitle** - Optional supporting text below the title (e.g., "Yes, it's real")

#### Block Composition

* A single block can contain **1 to 15 badges**
* Each badge can be customized individually (different icons, text, colors)
* Badges are arranged in a grid layout that you control (rows and columns)
* The entire block can optionally include a heading above all badges

Now let's configure your block.

\[Screenshot with labels for each area of the layout]

### Step 3: Configure Block Structure and Layout

#### General Settings

**Block Name**

* Internal name for your reference in Intelligems (e.g., "Trust Badge 1")
* Not visible to customers

**Location ID**

* A unique identifier used to connect this block to Shopify checkout
* Must be unique across all your blocks
* Use lowercase letters, numbers, and hyphens (e.g., "trust-badge-1", "warranty-callout")
* You'll need this exact ID when adding the block to Shopify

**Heading (Optional)**

* Add a main heading above your badges (e.g., "CHECKOUT NOW!" or "Why Shop With Us")
* Leave the heading text field blank to hide the heading entirely
* The heading appears centered above all badges

#### Badge Layout Controls

**Body Alignment** Controls how the entire block of badges aligns on the checkout page:

* **Left:** Badges align to the left side
* **Center:** Badges center on the page
* **Right:** Badges align to the right side

**Rows and Columns** Define the grid layout for your badges:

* **Rows:** Number of stacked rows (maximum 5)
* **Columns:** Number of badges per row (maximum 3)

The total badges displayed = rows × columns. If you have more badges configured than your grid allows, only the first badges up to the grid limit will show.

**Layout Examples:**

* 1 row, 3 columns = Three badges in a horizontal line
* 2 rows, 1 column = Two badges stacked vertically
* 2 rows, 2 columns = Four badges in a 2×2 grid
* 3 rows, 1 column = Three badges stacked vertically

**Image Position** Determines where the icon or image appears relative to the badge text:

* **Top:** Icon above text
* **Left:** Icon to the left of text (most common)
* **Right:** Icon to the right of text
* **Bottom:** Icon below text

This applies uniformly to all badges in the block.

### Step 4: Design Your Block - Typography and Visual Style

#### Typography Controls

Typography settings apply to all badges uniformly and use [preset options from your theme’s checkout settings](#common-questions).

* **Font Size:** Choose from available preset sizes (small, medium, large, additional sizes [based on your checkout theme](https://docs.intelligems.io/personalizations/getting-started-with-checkout#common-questions))
* **Font Style:** Controls text emphasis (bold, normal, italic)
* **Text Alignment:** How the text aligns (left, center, right)

#### Color Settings

All color options come directly from your Shopify checkout brand settings. These are not custom color pickers - you're selecting from [preset colors defined in your checkout theme](https://docs.intelligems.io/personalizations/getting-started-with-checkout#common-questions).

* **Title Color:** Sets the color for badge title text.
* **Subtitle Color:** Sets the color for badge subtitle text. Uses the same color palette as title colors.
* **Background Color:** Sets the background color for the entire block
  * Base (usually white or your checkout background)
  * Subdued (more subtle version of Base, calculated by Shopify)
  * Transparent (no background)
  * Other colors from your checkout theme
* **Border Color:** Sets the color for the border around your block (if border thickness is above 0)

#### Appearance and Spacing

* **Border Style:** Choose the style of border around your entire block:
* **Border Thickness:** Controls the width of the border in pixels. Set to Base with Border Style "None" for no border
* **Corner Radius:** Controls how rounded the corners of your block are:
* **Padding:** Controls the internal spacing inside your block (space between the border and your badges)
* **Body Spacing:** Controls the gap between individual badges and the heading when you have multiple badges

### Step 5: Configure Individual Badges

Now configure the content for each badge. You can add up to 15 badges per block using the "+ Add badge" button.

Each badge has the following settings:

#### Icon/Image Selection

* **Icon or Image Toggle:** Choose whether to use a Shopify icon, or upload a custom image file
* **Icon Selection (if using Icon)**: Choose from available Shopify icons
* **Image Upload (if using Image)**: Upload a custom image file to use instead of an icon

#### Icon/Image Styling

* **Icon Color:** Override the global icon color for this specific badge
* **Icon/Image Size:** Control the size of the icon or image

#### Badge Content

**Title:** The main text for this badge, located above the subtitle text

**Subtitle:** Supporting text below the title

#### **Configuring Multiple Badges:**

Use the "+ Add badge" button at the bottom of the badges section to add more badges (up to 15 total). Each badge is configured independently with its own icon, colors, title, and subtitle.

You can also:

* Reorder badges by dragging them
* Delete badges using the trash icon
* Collapse/expand badge sections using the arrow icon

### Step 6: Block-Level Styling

These settings affect the entire block container (the box that holds all your badges).

* **Background Color:** Sets the background color for the entire block:
* **Block Outer Padding:** Controls spacing between the block border and the content inside (heading and badges)
* **Border Style:** The line style for the block border
* **Border Thickness:** Width of the border around the entire block
* **Corner Radius:** How rounded the block corners are

### Step 7: Preview Your Block

As you make changes, the preview pane updates in real-time to show how your block will appear on checkout:

* Review the overall layout and spacing
* Check that colors match your brand
* Verify text is readable and properly sized
* Ensure icons are positioned correctly

**Note:** The preview shows your block in the Intelligems interface. The final appearance on your Shopify checkout may have slight variations based on your checkout theme settings.

### Step 8: Save and Create Experience

1. Click "Next" when you're satisfied with your block design
2. Choose whether to create a single Experience or a Test:
   * **Create Experience:** Activate this block on your checkout
   * **Create Test:** Test multiple variations against each other
3. Your Checkout Experience is now created and ready for Shopify configuration

### Step 9: Add Block to Shopify Checkout

This is a required step - you must configure the block in Shopify for it to appear:

1. Copy the Block ID from Intelligems (shown in the configuration instructions)
2. In Shopify, go to **Settings** → **Checkout**
3. Click **Customize**
4. In the left panel, click **Apps**
5. Navigate to **Intelligems**, click (+)
6. Click **Add block** in that location
7. Select **Intelligems A/B Testing** from the app blocks list
8. Paste your Block ID into the block settings field
9. Toggle on **Include block in Shop Pay** (recommended)
10. Adjust the block's position by dragging it to where you want it to appear.
11. Click **Save** in the top right corner
12. Use **Preview** to see your block on a live checkout page and in a **Shop Pay** checkout

**Important:** Each Checkout Experience needs to be added to your Shopify checkout separately using its unique Block ID. Without this step, the block won't appear on your checkout page.

### Step 10: Activate Your Experience

Once your block is configured in Shopify:

1. Return to your Intelligems Experience
2. Set up any targeting (optional) - see Targeting section below
3. Review your Experience settings
4. Click "Activate" to make it live

Your block will now appear for customers based on your targeting settings.

## Targeting Your Checkout Experiences

You can control who sees your Checkout Experiences using targeting rules:

**Audience Targeting:**

* Device type (mobile, desktop, tablet)
* Country or region
* New vs. returning customers
* UTM parameters from marketing campaigns
* Custom cookie values

**Currency Targeting:**

* Limit to specific currencies
* Target specific countries for multi-currency stores

**When to use targeting:**

* Test blocks with specific customer segments first
* Show different messages to different regions
* Display country-specific guarantees or policies
* Limit to specific marketing campaigns

## Adding Multiple Blocks to One Experience

You can add multiple blocks to a single Experience. All blocks in the Experience will activate together.

**To add multiple blocks:**

1. Create your first block and save it
2. In your Experience, click "Add another block"
3. Configure your second block with a different Location ID
4. Repeat for additional blocks
5. Save the updated Experience
6. Add each block to your Shopify checkout using its unique Block ID

## FAQs <a href="#common-questions" id="common-questions"></a>

* **Do I need to be on Shopify Plus?**

  Yes, Shopify checkout extensibility and using blocks are only available to Shopify Plus merchants. This is a Shopify limitation, not an Intelligems one.
* **Do Checkout Experiences have any impact on my Checkout page's load time?**\
  Intelligems blocks have no impact on your core checkout performance. Intelligems doesn’t interfere with the loading of payment details, shipping forms, or any other critical elements needed for customers to complete their purchase. Blocks load only after the checkout page has been fully initialized, and their load time is driven mostly by the user’s internet connection. Average load time is 248 milliseconds.
* **Can I use dynamic content in my blocks?**

  Not yet. Currently, Checkout Experiences only support static text and images. Additional blocks like countdown timers, upsells, recommendations, and reviews are coming soon.
* **How many blocks can I add to my checkout?**

  You can add as many blocks as you want to a single Experience, and create multiple Experiences. However, we recommend keeping your checkout clean with only the most important messages.
* **Can I test these blocks?**

  Yes! If you're on a Plus or Blue plan, you can create tests with different Checkout Experiences to see which performs best. Testing blocks is not available on Core plans.
* **What if I change my block in Intelligems?**

  Changes to your block design will automatically update on your checkout. You don't need to reconfigure anything in Shopify unless you're changing the Block ID.
* **Can blocks appear conditionally?**

  Yes, you can use Intelligems targeting to show blocks only to specific audiences, countries, devices, or based on other conditions.
* **Will this work with checkout extensions?** Yes, Intelligems Checkout Experiences work alongside other Shopify checkout extensions and apps.
* **Where do the color and typography options come from?**

  All colors come from your Shopify checkout brand settings.

  **To modify available options:**

  1. Go to your Shopify admin
  2. Navigate to **Online Store** → **Themes**
  3. Click **Customize** → **Checkout**
  4. Go to **Settings**
  5. Update your checkout brand colors (Primary, Accent, etc.) and typography settings
  6. These options will then be available in Intelligems

## Getting Help

If you need assistance with setting up Checkout Experiences:

* Check the technical integration guides for detailed setup instructions
* Contact Intelligems support for help with complex configurations
* Work with your Shopify team if you need help accessing checkout customization

For more details about testing different checkout experiences, see Testing Checkout Experiences.

***

*Last updated: October 2025*

*Was this helpful?*
