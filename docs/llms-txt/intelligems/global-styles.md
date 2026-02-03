# Source: https://docs.intelligems.io/general-features/global-styles.md

# Global Styles

### Overview

Global Styles is your centralized design system for managing component defaults across all Tests and Experiences. Create consistent, branded components with the flexibility to override them per offer when needed.

{% hint style="warning" %}
**Important:** To add these components to your site, please follow [these installation instructions](https://docs.intelligems.io/offer-personalizations/offers-integrating-widgets)
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f377382f83589d954c2d795ad5eac4bcb5efe98c%2FGlobal%20styles%20-%20Quantity%20buttons.png?alt=media" alt=""><figcaption></figcaption></figure>

### Key Features

* **Centralized Design Management**: Manage styling defaults for all component types in one location
* **Brand Consistency**: Ensure components maintain consistent styling across all offers
* **Time-Saving Workflow**: Set up styles once and automatically apply to new offers
* **Flexible Override System**: Customize individual components without affecting global defaults

### How It Works

Global Styles serve as templates for each component type:

1. **Default Application**: New components automatically use Global Styles
2. **Inheritance**: Styling, content templates, and layouts transfer to new components
3. **Override Capability**: Modify styles in specific offers without affecting globals
4. **Consistency**: Global changes update all linked components

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-33f257db8705aced497a3f6b9d61f5a828d6eeba%2FQuantity%20buttons%20-%20Classic%20list%20-%20Default2.png?alt=media" alt=""><figcaption></figcaption></figure>

### Component Types

Global Styles can be configured for each component style type:

* [**Quantity Buttons**](https://docs.intelligems.io/offer-personalizations/quantity-buttons)
* [**Progress Bars**](https://docs.intelligems.io/offer-personalizations/progress-bars)
* [**Shipping Progress Bars**](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)
* [**Offer Messages**](https://docs.intelligems.io/offer-personalizations/offer-modifications)

Each component type allows you to set default styling, content templates, and layout preferences that will automatically apply to new components.

{% hint style="warning" %}
Note: In order to use Quantity Buttons, Progress Bars, and Shipping Progress Bars in an Offer, you need to [complete the installation](https://docs.intelligems.io/offer-personalizations/offers-integrating-widgets) by adding a snippet to your Theme code.
{% endhint %}

{% hint style="info" %}
No theme installation is required to use Slideout / Pop Up Messages in Offers. The component is automatically available.
{% endhint %}

### Setting Up Global Styles

1. **Access Global Styles** from your dashboard
2. **Choose Component Type** to configure
3. **Configure Base Styling**: Colors, typography, spacing
4. **Save and Apply** to make available for new offers

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8906eeacb82d2d4801c20b12bff1ba36058e5ad5%2FGlobal%20styles%20-%20Quantity%20buttons3.png?alt=media" alt=""><figcaption></figcaption></figure>

### Advanced Features

#### Color Theme System

* **Primary Color Selection**: Choose a color and it automatically filters down to all elements in different opacities
* **Manual Swatch Override**: Manually change specific color swatches for individual elements when needed

### Using in Offers

#### Automatic Application

Once Global Styles is set up and the components are installed via adding snippets to your theme, new offer components inherit Global Styles automatically.

#### Customizing Components

Override global settings for specific campaigns:

* **Linked**: Follows global updates
* **Unlinked**: Independent custom styling

{% hint style="success" %}
**Tips**

* **Start with Brand Guidelines**: Use official colors and typography
* **Think Mobile-First**: Design for touch interactions and small screens
* **Plan for Flexibility**: Create styles that work across campaign types
* **Regular Reviews**: Update based on performance and brand evolution
  {% endhint %}

### Troubleshooting

**Components Not Using Global Styles**: Verify styles are saved and components aren't individually customized

Last updated: 7/29/25
