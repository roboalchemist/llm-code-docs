# Source: https://firebase.google.com/docs/reference/js/analytics.eventparams.md.txt

# EventParams interface

Standard `gtag.js` event parameters. For more information, see [the GA4 reference documentation](https://developers.google.com/gtagjs/reference/ga4-events).

**Signature:**  

    export interface EventParams 

## Properties

|                                                             Property                                                             |                                                   Type                                                    |                              Description                              |
|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [affiliation](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsaffiliation)                     | string                                                                                                    |                                                                       |
| [checkout_option](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamscheckout_option)             | string                                                                                                    |                                                                       |
| [checkout_step](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamscheckout_step)                 | number                                                                                                    |                                                                       |
| [content_type](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamscontent_type)                   | string                                                                                                    |                                                                       |
| [coupon](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamscoupon)                               | string                                                                                                    |                                                                       |
| [currency](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamscurrency)                           | string                                                                                                    |                                                                       |
| [description](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsdescription)                     | string                                                                                                    |                                                                       |
| [event_category](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsevent_category)               | string                                                                                                    |                                                                       |
| [event_label](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsevent_label)                     | string                                                                                                    |                                                                       |
| [fatal](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsfatal)                                 | boolean                                                                                                   |                                                                       |
| [firebase_screen_class](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsfirebase_screen_class) | string                                                                                                    | Firebase-specific. Use to log a `screen_class` to Firebase Analytics. |
| [firebase_screen](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsfirebase_screen)             | string                                                                                                    | Firebase-specific. Use to log a `screen_name` to Firebase Analytics.  |
| [item_id](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsitem_id)                             | string                                                                                                    |                                                                       |
| [item_list_id](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsitem_list_id)                   | string                                                                                                    |                                                                       |
| [item_list_name](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsitem_list_name)               | string                                                                                                    |                                                                       |
| [items](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsitems)                                 | [Item](https://firebase.google.com/docs/reference/js/analytics.item.md#item_interface)\[\]                |                                                                       |
| [method](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsmethod)                               | string                                                                                                    |                                                                       |
| [number](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsnumber)                               | string                                                                                                    |                                                                       |
| [page_location](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspage_location)                 | string                                                                                                    |                                                                       |
| [page_path](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspage_path)                         | string                                                                                                    |                                                                       |
| [page_title](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspage_title)                       | string                                                                                                    |                                                                       |
| [payment_type](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspayment_type)                   | string                                                                                                    |                                                                       |
| [promotion_id](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspromotion_id)                   | string                                                                                                    |                                                                       |
| [promotion_name](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspromotion_name)               | string                                                                                                    |                                                                       |
| [promotions](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamspromotions)                       | [Promotion](https://firebase.google.com/docs/reference/js/analytics.promotion.md#promotion_interface)\[\] |                                                                       |
| [screen_name](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsscreen_name)                     | string                                                                                                    |                                                                       |
| [search_term](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamssearch_term)                     | string                                                                                                    |                                                                       |
| [shipping_tier](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsshipping_tier)                 | string                                                                                                    |                                                                       |
| [shipping](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsshipping)                           | [Currency](https://firebase.google.com/docs/reference/js/analytics.md#currency)                           |                                                                       |
| [tax](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamstax)                                     | [Currency](https://firebase.google.com/docs/reference/js/analytics.md#currency)                           |                                                                       |
| [transaction_id](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamstransaction_id)               | string                                                                                                    |                                                                       |
| [value](https://firebase.google.com/docs/reference/js/analytics.eventparams.md#eventparamsvalue)                                 | number                                                                                                    |                                                                       |

## EventParams.affiliation

**Signature:**  

    affiliation?: string;

## EventParams.checkout_option

**Signature:**  

    checkout_option?: string;

## EventParams.checkout_step

**Signature:**  

    checkout_step?: number;

## EventParams.content_type

**Signature:**  

    content_type?: string;

## EventParams.coupon

**Signature:**  

    coupon?: string;

## EventParams.currency

**Signature:**  

    currency?: string;

## EventParams.description

**Signature:**  

    description?: string;

## EventParams.event_category

**Signature:**  

    event_category?: string;

## EventParams.event_label

**Signature:**  

    event_label?: string;

## EventParams.fatal

**Signature:**  

    fatal?: boolean;

## EventParams.firebase_screen_class

Firebase-specific. Use to log a `screen_class` to Firebase Analytics.

**Signature:**  

    firebase_screen_class?: string;

## EventParams.firebase_screen

Firebase-specific. Use to log a `screen_name` to Firebase Analytics.

**Signature:**  

    firebase_screen?: string;

## EventParams.item_id

**Signature:**  

    item_id?: string;

## EventParams.item_list_id

**Signature:**  

    item_list_id?: string;

## EventParams.item_list_name

**Signature:**  

    item_list_name?: string;

## EventParams.items

**Signature:**  

    items?: Item[];

## EventParams.method

**Signature:**  

    method?: string;

## EventParams.number

**Signature:**  

    number?: string;

## EventParams.page_location

**Signature:**  

    page_location?: string;

## EventParams.page_path

**Signature:**  

    page_path?: string;

## EventParams.page_title

**Signature:**  

    page_title?: string;

## EventParams.payment_type

**Signature:**  

    payment_type?: string;

## EventParams.promotion_id

**Signature:**  

    promotion_id?: string;

## EventParams.promotion_name

**Signature:**  

    promotion_name?: string;

## EventParams.promotions

**Signature:**  

    promotions?: Promotion[];

## EventParams.screen_name

**Signature:**  

    screen_name?: string;

## EventParams.search_term

**Signature:**  

    search_term?: string;

## EventParams.shipping_tier

**Signature:**  

    shipping_tier?: string;

## EventParams.shipping

**Signature:**  

    shipping?: Currency;

## EventParams.tax

**Signature:**  

    tax?: Currency;

## EventParams.transaction_id

**Signature:**  

    transaction_id?: string;

## EventParams.value

**Signature:**  

    value?: number;