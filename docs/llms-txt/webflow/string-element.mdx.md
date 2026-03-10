# Source: https://developers.webflow.com/designer/reference/string-element.mdx

***

title: String Element
slug: designer/reference/string-element
description: The String element represents a string value within the Webflow Designer
hidden: false
'og:title': 'Webflow Designer API: String Element'
'og:description': The String element represents a string value within the Webflow Designer
------------------------------------------------------------------------------------------

The String element represents text content of an element within the Webflow Designer.

String elements can't be created directly, and are only created when adding elements that contain text content.

## Methods

You can get and set the text value of a string element using the following methods:

<CardGroup>
  <Card title="Get Text" href="/designer/reference/string-element/getText">
    Retrieves the text value from a String element.
  </Card>

  <Card title="Set Text" href="/designer/reference/string-element/setText">
    Sets the text value on a String element, overwriting any prior text value.
  </Card>
</CardGroup>

{" "}

## Properties

| Property           | Description                                                                                       | Type      | Example                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------ | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`. | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                | `string`  | 'String'                                                |
| `children`         | Indicates whether an element can contain child elements.                                          | `boolean` | `false`                                                 |
| `styles`           | Indicates if the element can be styled.                                                           | `boolean` | `false`                                                 |
| `textContent`      | Indicates if the element can contain text content                                                 | `boolean` | `false`                                                 |
| `customAttributes` | Indicates whether an element can have custom attributes                                           | `boolean` | `false`                                                 |

## Supported Elements

The following elements contain string elements as children, which can be accessed using the String element methods.

* `DOMElement`
* `BlockquoteElement`
* `EmphasizedElement`
* `HeadingElement`
* `LinkElement`
* `ParagraphElement`
* `SpanElement`
* `StrongElement`
* `SuperscriptElement`
* `SubscriptElement`
* `InlineCodeElement`
* `CommerceBuyNowButtonElement`
* `CommerceCartOpenLinkElement`
* `CommerceCartCheckoutButtonElement`
* `CommerceCartCloseLinkElement`
* `CommerceCartRemoveLinkElement`
* `CommerceCartOptionListItemLabelElement`
* `CommerceCartOptionListItemValueElement`
* `CommerceCartQuickCheckoutButtonElement`
* `CommerceCartApplePayButtonElement`
* `CommerceCheckoutLabelElement`
* `CommerceLabelElement`
* `CommerceCheckoutPlaceOrderButtonElement`
* `CommerceCheckoutBillingAddressToggleLabelElement`
* `CommerceCheckoutOrderItemOptionListItemLabelElement`
* `CommerceCheckoutOrderItemOptionListItemValueElement`
* `CommerceCheckoutSummaryLabelElement`
* `CommerceCheckoutDiscountsButtonElement`
* `CommerceCheckoutDiscountsLabelElement`
* `DropdownLinkElement`
* `LightboxWrapperElement`
* `FormBlockLabelElement`
* `FormInlineLabelElement`
* `NavbarLinkElement`
* `TabsLinkElement`
* `UserFormBlockLabelElement`
