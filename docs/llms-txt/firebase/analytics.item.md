# Source: https://firebase.google.com/docs/reference/js/analytics.item.md.txt

# Item interface

Standard Google Analytics `Item` type.

**Signature:**  

    export interface Item 

## Properties

|                                               Property                                               |                                      Type                                       | Description |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------|
| [affiliation](https://firebase.google.com/docs/reference/js/analytics.item.md#itemaffiliation)       | string                                                                          |             |
| [brand](https://firebase.google.com/docs/reference/js/analytics.item.md#itembrand)                   | string                                                                          |             |
| [category](https://firebase.google.com/docs/reference/js/analytics.item.md#itemcategory)             | string                                                                          |             |
| [coupon](https://firebase.google.com/docs/reference/js/analytics.item.md#itemcoupon)                 | string                                                                          |             |
| [creative_name](https://firebase.google.com/docs/reference/js/analytics.item.md#itemcreative_name)   | string                                                                          |             |
| [creative_slot](https://firebase.google.com/docs/reference/js/analytics.item.md#itemcreative_slot)   | string                                                                          |             |
| [discount](https://firebase.google.com/docs/reference/js/analytics.item.md#itemdiscount)             | [Currency](https://firebase.google.com/docs/reference/js/analytics.md#currency) |             |
| [id](https://firebase.google.com/docs/reference/js/analytics.item.md#itemid)                         | string                                                                          |             |
| [index](https://firebase.google.com/docs/reference/js/analytics.item.md#itemindex)                   | number                                                                          |             |
| [item_brand](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_brand)         | string                                                                          |             |
| [item_category](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_category)   | string                                                                          |             |
| [item_category2](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_category2) | string                                                                          |             |
| [item_category3](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_category3) | string                                                                          |             |
| [item_category4](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_category4) | string                                                                          |             |
| [item_category5](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_category5) | string                                                                          |             |
| [item_id](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_id)               | string                                                                          |             |
| [item_list_id](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_list_id)     | string                                                                          |             |
| [item_list_name](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_list_name) | string                                                                          |             |
| [item_name](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_name)           | string                                                                          |             |
| [item_variant](https://firebase.google.com/docs/reference/js/analytics.item.md#itemitem_variant)     | string                                                                          |             |
| [location_id](https://firebase.google.com/docs/reference/js/analytics.item.md#itemlocation_id)       | string                                                                          |             |
| [name](https://firebase.google.com/docs/reference/js/analytics.item.md#itemname)                     | string                                                                          |             |
| [price](https://firebase.google.com/docs/reference/js/analytics.item.md#itemprice)                   | [Currency](https://firebase.google.com/docs/reference/js/analytics.md#currency) |             |
| [promotion_id](https://firebase.google.com/docs/reference/js/analytics.item.md#itempromotion_id)     | string                                                                          |             |
| [promotion_name](https://firebase.google.com/docs/reference/js/analytics.item.md#itempromotion_name) | string                                                                          |             |
| [quantity](https://firebase.google.com/docs/reference/js/analytics.item.md#itemquantity)             | number                                                                          |             |

## Item.affiliation

**Signature:**  

    affiliation?: string;

## Item.brand

> | **Warning:** This API is now obsolete.
>
> Use item_brand instead.

**Signature:**  

    brand?: string;

## Item.category

> | **Warning:** This API is now obsolete.
>
> Use item_category instead.

**Signature:**  

    category?: string;

## Item.coupon

**Signature:**  

    coupon?: string;

## Item.creative_name

**Signature:**  

    creative_name?: string;

## Item.creative_slot

**Signature:**  

    creative_slot?: string;

## Item.discount

**Signature:**  

    discount?: Currency;

## Item.id

> | **Warning:** This API is now obsolete.
>
> Use item_id instead.

**Signature:**  

    id?: string;

## Item.index

**Signature:**  

    index?: number;

## Item.item_brand

**Signature:**  

    item_brand?: string;

## Item.item_category

**Signature:**  

    item_category?: string;

## Item.item_category2

**Signature:**  

    item_category2?: string;

## Item.item_category3

**Signature:**  

    item_category3?: string;

## Item.item_category4

**Signature:**  

    item_category4?: string;

## Item.item_category5

**Signature:**  

    item_category5?: string;

## Item.item_id

**Signature:**  

    item_id?: string;

## Item.item_list_id

**Signature:**  

    item_list_id?: string;

## Item.item_list_name

**Signature:**  

    item_list_name?: string;

## Item.item_name

**Signature:**  

    item_name?: string;

## Item.item_variant

**Signature:**  

    item_variant?: string;

## Item.location_id

**Signature:**  

    location_id?: string;

## Item.name

> | **Warning:** This API is now obsolete.
>
> Use item_name instead.

**Signature:**  

    name?: string;

## Item.price

**Signature:**  

    price?: Currency;

## Item.promotion_id

**Signature:**  

    promotion_id?: string;

## Item.promotion_name

**Signature:**  

    promotion_name?: string;

## Item.quantity

**Signature:**  

    quantity?: number;