# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/osm-customise-merchant-portal.md

# Customize placements through Merchant portal

## If you're not familiar with CSS or don't have access to your website's source code, use Klarna's Merchant portal to customize placements to better suit your website's design.

For most elements, you're given a variety of customization options. The content specific to the Klarna brand, for example our logo, is less customizable. You can modify the look and feel at the placement level in the Merchant portal. Changes you make there are live immediately after you publish them.

## Step 1. Open the Custom design menu

In the [Merchant portal](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/conversion-boosters/), go to **Conversion Boosters**\&gt; **On-site messaging**\&gt; **Placements**. Pick a placement you want to customize, then click **Custom design**.


![klarna docs image](caefc8c8-8613-44cf-9afc-9bb6b08da93a_Screenshot+2024-03-06+at+14.53.10.jpeg)image

## Step 2. Customize the placement.

Modify the placement's font, layout, and choose which Klarna logo you want to display. Preview the changes as you're editing to make sure everything looks OK.


![ Customizing a placement](cbf940e0-d772-4f04-bca0-ab67747fd885_Screenshot+2024-03-06+at+14.55.11.jpeg)
*Customizing a placement*

All customizations go through an accessibility check to ensure that the placements are readable and meet the accessibility criteria. If a custom placement doesn't pass the accessibility check, the **Publish** button is grayed out and hints are displayed. You have to edit the style until the button becomes active again. You can reset a custom placement to its default design at any time by clicking **Reset to default**.

## Step 3. Publish changes

Once you're happy with the design changes, click **Publish**, then **Confirm**. Your changes will be live immediately. 
![ Publishing a custom placement](0d74a13d-4385-4485-a980-a76296e3c159_Screenshot+2024-03-06+at+14.56.13.jpeg " Publishing a custom placement")

## Placement sizes

Placements labeled with *(auto)x(auto)* adjust to 100% of the width and height of the container element. All placements are responsive.

## Themes

The On-site messaging placements come in different themes you can switch between:

- Light theme
- Dark theme
- Custom theme, created when you save a custom design in Merchant portal

When you switch between themes in the Merchant portal, the data-theme attribute in the code snippet changes accordingly. If you're not using a custom design, the light theme is the default. When you select it, data-theme isn't included in the code. If you then switch to the dark mode, data-theme="dark" is added to the placement tag. If you're using a placement with a custom design, the custom theme is the default and the placement tag doesn't include the data-theme attribute. In that case, when you switch to the light theme, data-theme is set to default. When you then switch to the dark theme, data-theme is set to dark. When the placement tag contains data-theme, all customisations are overridden.