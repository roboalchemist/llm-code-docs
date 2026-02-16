# Squarespace Developer Documentation
# Source: https://developers.squarespace.com/changes/upcoming-changes

Upcoming changes — Squarespace Developers

-

[

](/)

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

[Custom Code](/custom-code/about)

[Upcoming Changes](/changes/upcoming-changes)

[Get Started](/quick-start)

[

](/)

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

[Custom Code](/custom-code/about)

[Upcoming Changes](/changes/upcoming-changes)

[Get Started](/quick-start)

Changes

[Upcoming changes](/changes/upcoming-changes)

# Products V2 Update: Required Action

## Required Action

If your site uses custom code that targets product pages, you must migrate to Products V2 before **August 30** to avoid disruption.

## Summary

This article outlines important changes to the markup of product-related pages on Squarespace, including the Product Detail Page (PDP) and Product List Page (PLP), also known as the Store Page. These changes are part of a broader initiative to optimize the underlying DOM structure, improve load performance, and increase consistency across layouts and features.

If your site relies on custom CSS, JavaScript, or injected HTML that targets specific classes or attributes in product pages, you will need to update your code during the **60 day migration window** outlined below.

## Migration Timeline

**June 30** – Migration opt-in period begins

You can begin updating your site using the new markup structure. A migration tool will be available from your Squarespace dashboard under Settings > Selling > Product Settings.

**August 30** – Migration opt-in period ends.

**Starting in September** – Automatic migration

Sites that have not been manually updated will be migrated automatically. Any unsupported or outdated custom code may stop working, potentially affecting how your product pages appear or function.

## Overview of Changes

The updates apply to all PDP layout types (Simple, Full, Half, Wrap), the Product List Page (PLP)/Store Page, and shared elements used across both page types.

### Key Themes

Top-level layout elements are now identified by a single data-product-detail-layout attribute.

-

Legacy class names (e.g., `.ProductItem-*`) have been replaced by a new standardized prefix (`.product-*`).

-

Deprecated `data-*` attributes have been removed.

-

Structural wrappers for titles, prices, variants, and buttons have been unified across layouts.

-

Related Products has the same HTML structure as the new PLP changes

## Updates

### August 22nd, 2025

#### Product Detail Page

- Added `data-product-id` attribute to the level of `.product-detail` for all layouts

#### Product List Page

- Added `data-product-id` attribute to the same level of each `.product-list-item` element

- New header `.product-list-header` element was added that wraps the header elements like breadcrumbs, title, and categories

- New header element `.product-list-header` now exists above the `data-product-list-layout` attribute element,

rather than as the first child inside that element

## Detailed Changes by Page and Layout

### Product Detail Page

#### All Layouts

- Tag (i.e. `.tag-<tagName>`), `.on-sale`, and `.sold-out` classes now exist on the top-level `.product-item` element

- Product Price

`.product-price-value` wrapper element added around price text

- Product Payment Method Messaging

`[data-afterpay]` element replaced by a [Stripe component](https://docs.stripe.com/elements/payment-method-messaging) rendered within a new `.product-payment-method-messaging`

Also moved within `.product-price` element

wrapper element

- Product Status

`.product-status` wrapper element added

#### Simple Layout

- `.ProductItem` element replaced by `data-product-detail-layout="simple"` element

`data-item-id` attribute removed

- `.ProductItem-summary` element replaced by `.product-content-wrapper` element

- `.product-details.ProductItem-details` element replaced by `.product-meta` element

- `data-test` attribute removed

- `data-current-context` attribute removed

- `.ProductItem-details-checkout` wrapper element removed

- `.ProductItem-product-price` wrapper element removed

- `.ProductItem-quantity-add-to-cart` wrapper element removed

- Elements

Gallery

All classes with the prefix `ProductItem` have been changed to use the prefix `product`

- Removed various attributes on the `.ProductItem-gallery-slides-item` element

`data-slide-index`

- `data-image-id`

- `data-slide-url`

- `data-test`

- Product Title

`.ProductItem-details-title` element replaced by `.product-title`

`data-content-field` attribute removed

- `data-test` attribute removed

- Product Description

`.ProductItem-details-excerpt` element replaced by `.product-description` element

Removed `data-content-field` attribute

- Removed various classes that were previously set based on element position

`.ProductItem-details-excerpt-below-price`

- `.ProductItem-details-excerpt-below-add-to-cart`

- `.ProductItem-details-excerpt-below-add-ons`

#### Full Layout

- `.ProductItem` element replaced by `data-product-detail-layout="full"` element

`data-item-id attribute` removed

- `data-layout` removed and replaced with `data-product-detail-layout`

- `.pdp-layout pdp-layout-full-width-carousel` element removed

- Removed various attributes on the `.ProductItem-gallery-slides-item` element

`data-slide-index`

- `data-image-id`

- `data-slide-url`

- `data-test`

- All classes with the prefix `ProductItem` have been changed to use the prefix `product`

- `.product-details.pdp-details` replaced with `.product-meta`

`data-current-context` removed

- `.ProductItem-nav` replaced by `.product-nav`

- `.ProductItem-nav-breadcrumb` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.ProductItem-nav-breadcrumb-separator` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.product-details.pdp-details` replaced with `.product-meta

`data-current-context` removed

- `.product-meta-section` added

- Product Title

`.pdp-details-title` replaced with `.product-title`

- `data-content-field` removed

- `data-test` removed

- `.pdp-details-price` replaced with `.product-price`

`.product-price` replaced with `.product-price-value`

- `.product-scarcity` is moved out from `.product-price` and is a sibling

- `.pdp-details-excerpt` replaced with  `.product-description.hidden-md-down` and `.product-description.hidden-md-up` depending on description placement

- `.product-variant data-item-id` and `data-variants` attributes removed

- `.variant-select-wrapper` or `.variant-radiobtn-wrapper` removed depending on which Variant Display option is selected

- `.product-quantity-input` and `data-item-id` attribute removed `.product-quantity-input-wrapper` placed inside `.product-add-to-cart` > `.product-add-to-cart-layout-wrapper.add-to-cart-inline-md-up` (desktop - inline) `.add-to-cart-inline-md-down` (mobile - inline)

#### Half Layout

- `#pdp.pdp-layout.pdp-layout-full-bleed` element replaced by `data-product-detail-layout="half"` element

`data-item-id` attribute removed

- `data-layout` removed and replaced with `data-product-detail-layout`

- `pdp-gallery-images` replaced with `pdp-gallery-wrapper`

- `class="pdp-gallery-images"` and `data-product-gallery="slideshow"` wraps all `.pdp-gallery-slides`

- `.pdp-form-wrapper.hidden-sm-down` replaced by

`.product-content-wrapper`

- `.ProductItem-nav` replaced by `.product-nav`

- `.ProductItem-nav-breadcrumb` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.ProductItem-nav-breadcrumb-separator` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.product-details.pdp-details` replaced with `.product-meta`

- `data-current-context` removed

- Product Meta

Product Title

`.pdp-details-title` replaced with `.product-title`

- `data-content-field` attribute removed

- `data-test` attribute removed

- `.pdp-details-price` replaced with `.product-price`

`.product-price` replaced with `.product-price-value`

- `.product-scarcity` is moved out from `.product-price` and is a sibling

- `.pdp-details-excerpt` replaced with `.product-description.hidden-md-down` and `.product-description.hidden-md-up` depending on description placement

- `.product-variant data-item-id` and `data-variants` attributes removed

`.variant-select-wrapper` or `.variant-radiobtn-wrapper` removed depending on which Variant Display option is selected

- `.product-quantity-input` and `data-item-id` attribute removed `.product-quantity-input-wrapper` placed inside `.product-add-to-cart` > `.product-add-to-cart-layout-wrapper.add-to-cart-inline-md-up` (desktop - inline) `.add-to-cart-inline-md-down` (mobile - inline)

#### Wrap Layout

- `#pdp.pdp-layout.pdp-layout-wrap-around` element replaced by `data-product-detail-layout="wrap"` element

`data-item-id` attribute removed

- `data-layout` removed and replaced with `data-product-detail-layout`

- `pdp-gallery-images` replaced with `pdp-gallery-wrapper`

- `class="pdp-gallery-images"` and `data-product-gallery="slideshow"` wraps all `.pdp-gallery-slides`

- `.pdp-form-wrapper.hidden-sm-down` replaced by

`.product-content-wrapper`

- `.ProductItem-nav` replaced by `.product-nav`

- `.ProductItem-nav-breadcrumb` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.ProductItem-nav-breadcrumb-separator` removed

- `.ProductItem-nav-breadcrumb-link` replaced by `.product-nav-breadcrumb-link`

- `.product-details.pdp-details` replaced with `.product-meta`

- `data-current-context` removed

- Product Meta

Product Title

`.pdp-details-title` replaced with `.product-title`

- `data-content-field` attribute removed

- `data-test` attribute removed

- `.pdp-details-price` replaced with `.product-price`

`.product-price` replaced with `.product-price-value`

- `.product-scarcity` is moved out from `.product-price` and is a sibling

- `.pdp-details-excerpt` replaced with `.product-description.hidden-md-down` and `.product-description.hidden-md-up` depending on description placement

- `.product-variant data-item-id` and `data-variants` attributes removed

`.variant-select-wrapper` or `.variant-radiobtn-wrapper` removed depending on which Variant Display option is selected

- `.product-quantity-input` and `data-item-id` attribute removed `.product-quantity-input-wrapper` placed inside `.product-add-to-cart` > `.product-add-to-cart-layout-wrapper.add-to-cart-inline-md-up` (desktop - inline) `.add-to-cart-inline-md-down` (mobile - inline)

### Product List Page and Related Products on the Product Detail Page

- All tweak related class names and styles have been removed and replaced with `.product-list`

- `.products.collection-content-wrapper.products-list` replaced with several attributes

`data-product-list-layout`

- `data-section-width`

- `data-header-text-alignment`

- `data-meta-text-alignment`

- `data-category-display-type`

- `style`

- `.products-flex-container` replaced with `.product-list-container`

- `.grid-item` replaced with `.product-list-item`

Tag (i.e. `.tag-<tagName>`), `.on-sale`, and `.sold-out` classes still exist on the `.product-list-item` element

- Following classes and attributes removed from `.product-list-item`

`.hentry`

- `.author-your-name`

- `.post-type-store-item`

- `.article-index`

- `.sqs-product-quick-view-button-hover-area`

- `id`

- `data-item-id`

- `data-current-context`

- `.grid-item-link.product-lists-item` replaced by `.product-list-item-link`

- `.grid-image` replaced by `.product-list-image-wrapper`

- `.grid-meta-wrapper` replaced by `.product-list-item-meta`

`data-num-columns` attribute removed

- `.grid-title` replaced by `.product-list-item-title`

- `.grid-prices` replaced by `.product-list-item-price`

- `.product-price` nested element removed

- `.product-list-title-price` wraps `.product-list-item-title` and `.product-list-item-price`

- `.product-scarcity` `data-variant-attributes` removed

- `.grid-meta-status` wraps `.product-scarcity`, `.product-mark.sold-out`, and `.product-mark.sale`

- `.product-list-item-status` wraps `.grid-meta-status`

- `.product-variant` element all attributes removed

### Shared Elements between Product Detail Page and Product List Page

- Product Scarcity

Only one `.product-scarcity` element now, rather than one for each variant

`data-variant-attributes` attribute removed

- Product Variant Select

Removed various attributes from the `.product-variants element`

`data-item-id`

- `data-variants`

- `data-is-subscribable`

- `data-subscription-plan`

- `data-selected-variant`

- `data-unselected-options`

- `data-variant-in-stock`

- Moved `data-variant-option-name` attribute to the `.variant-option wrapper` element

- Restock Notification (Waitlist)

Only one `.product-restock-notification` element now, rather than one for each variant

- Removed various attributes from the `.product-restock-notification` element

`data-product-id`

- `data-variant-id`

- `.product-restock-mailing-list` checkbox name changed from `isJoinMailingList` to `join-mailing-list-checkbox`

- Add to Cart

Add `.product-add-to-cart` wrapper element containing subscription/one-time-payment select, quantity input, and add to cart button

- Subscription/One-Time-Payment Select

`.ProductItem-Subs-Otp` element replaced with `.product-subs-otp` element

- Removed `data-variants` attribute from `.pdp-subscriptions-and-otp` element

- `#one-time-purchase-radio` and `#one-time-purchase-radio-button` value changed from `one-time-purchase-radio` to `ONE_TIME_PURCHASE`

- `#subscription-radio` and `#subscription-radio-button` value changed from `subscription-radio` to `SUBSCRIPTION`

- Quantity Input

`.product-quantity-input` element replaced with `.product-quantity-input-wrapper` element

Removed `data-item-id` attribute

- Add to Cart Button

Changes on the `.sqs-add-to-cart-button` element

Removed `.use-form` class

- Removed various attributes

`data-collection-id`

- `data-item-id`

- `data-product-type`

- `data-use-custom-label`

- `data-is-subscription`

- `data-original-label`

- `data-form`

- `Data-subscription-option-id`

- Added extra `.add-to-cart-text wrapper` element around the text within the `.sqs-add-to-cart-button-inner` element

- Product Add-Ons

Replaced `.pdp-product-add-ons` element with `.product-add-ons` element

- Removed various attributes from the `.add-on-add-to-cart-wrapper` element

`data-is-product-add-on`

- `data-current-context`

- Changes on the `.sqs-add-to-cart-button` element

Removed `use-form` class

- Removed various attributes

`data-item-id`

- `data-collection-id`

- `data-product-type`

- `data-form`

- `Data-original-label`

- Classes within the `.icons-container` element have changed

`.plus-icon` → `.add-icon`

- `.add-on-add-to-cart-loading` → `.loading-icon`

- `.checkmark-icon` → `.complete-icon`

- Product Reviews

`.reviewSummary` element replaced with `.product-review-summary` element

## Layout Examples

Please see some of these example layouts pre and post DOM changes below so you can use a tool like [Diffchecker](https://www.diffchecker.com/) to compare the differences.

- Simple Layout

[Pre DOM Changes Simple Layout](https://forum.squarespace.com/pdpplp-before-after/pdp-simple-layout-before-dom)

- [Post DOM Changes Simple Layout](https://forum.squarespace.com/pdpplp-before-after/pdp-simple-layout-after-dom/)

- Wrap Layout

[Pre DOM Changes Wrap Layout](https://forum.squarespace.com/pdpplp-before-after/pre-dom-changes-wrap-layout)

- [Post DOM Changes Wrap Layout](https://forum.squarespace.com/pdpplp-before-after/post-dom-changes-wrap-layout/)

## Next Steps

- **Audit** your site for any custom code targeting product pages and familiarize yourself with changes described in this article.

- **Migrate** your site to Products V2 by going to your Site Settings > Selling > Products and follow the prompts. Complete this step between June 30 and August 30 to avoid automatic changes.

After this step there is no option to return to the earlier version.

- **Update** your code that references the old selectors, classnames, and data-* attributes to match the new structure.

- **Test** your updates thoroughly in production and make adjustments as needed.

If you don’t opt in by the **August 30, 2025 deadline**, your site will be migrated automatically. Any unsupported or outdated custom code may stop working, potentially affecting how your product pages appear or behave. This update is not optional and there is no way to opt-out of making these changes.

## FAQs

#### What exactly is changing?

We’re updating the DOM structure and changing the class and data attributes on Squarespace’s  Store Page (aka Product List Page or PLP) or Product Detail Pages (PDP). These changes are foundational for enabling future improvements to commerce design and functionality.

#### Will I be able to preview changes before publishing?

No, the opt-in is a one-way migration and cannot be undone after you go through the process. We suggest familiarizing yourself with the changes ahead of time and setting aside time outside of peak business hours to make the update.

#### Is there downtime?

No, there is no site downtime.

#### Will shoppers still be able to checkout while I make changes?

Yes. There are no changes to checkout.

#### Will this only affect product pages, or other parts of my site too?

Only Product Detail Pages (PDPs) and Store Page will be affected. No other page types are impacted.

#### How do I know if I have custom code that’s affected?

If you’ve manually edited the custom code of your PDP or Store Page, or use custom code that targets class names on those pages, it’s likely to be affected. You’ll need to cross-check your custom code with our list of structural changes described above.

#### What’s the timeline for these changes?

- **June 30**: Ability to migrate begins. Starting June 30, you can access a migration mechanism from your Squarespace site; instructions will be provided.

- **June 30 - August 30**: Code migration period. Whether you signed up for the Circle migration service or you’re doing it on your own, the migration from the current to the new system must be completed within this time.

- **September**: All remaining sites that have not been manually updated will be migrated automatically.

#### It’s after June 30, 2025 and I don’t see the option to migrate. What’s going on?

Your site was automatically migrated because it had no custom code. You don’t need to take further action.

#### I have a 7.0 site, what does this mean for me?

7.0 sites will not be impacted by the migration, however they will not benefit from any updates or new releases we have planned for later this year. We highly recommend updating all sites from 7.0 to 7.1. [You can read more about that here.](https://support.squarespace.com/hc/en-us/articles/360038270572-Moving-from-Squarespace-version-7-0-to-version-7-1)

#### What happens if I don’t opt in by August 30?

If you don’t opt in by the deadline, your site will be migrated automatically. Any outdated custom code may stop working, potentially affecting how your site product pages appear or behave.

#### What’s the deadline to take action?

If you want to control the timing of your site’s migration, act before August 30.

#### What happens if I do nothing?

Your site will be automatically migrated after August 30. If your product pages rely on custom code for updated class names or data attributes, you may see visual issues or layout changes that require manual int.

#### Will my site break?

Not necessarily, but visual issues are possible if your custom code depends on classes or elements that are changing. That’s why we strongly recommend proactive updates.

#### Will my custom styles disappear?

Only if they target class names or structural elements that have changed or no longer exist. With proper updates, your site will look and function as expected.

# Squarespace

[Main Site](https://www.squarespace.com)

[Careers](https://www.squarespace.com/about/careers)

# Developers

[Home](/)

[Developer Terms of Use](https://www.squarespace.com/developer-terms)

[Privacy Policy](https://www.squarespace.com/privacy)

[Security Measures](https://www.squarespace.com/measures)

# Documentation

[Template Docs](/quick-start)

[Commerce APIs](/commerce-apis/overview)

[Webhooks](/webhooks/overview)

# Community

[Circle](https://circle.squarespace.com)

[Specialists](https://specialists.squarespace.com)

[Forum](https://forum.squarespace.com)

# Follow

[Engineering Blog](https://engineering.squarespace.com)

[Github](https://github.com/squarespace)

[NPM](https://www.npmjs.com/org/squarespace)