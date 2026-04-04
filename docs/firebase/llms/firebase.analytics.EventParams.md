# Source: https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams.md.txt

# EventParams | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [analytics](https://firebase.google.com/docs/reference/js/v8/firebase.analytics).
- EventParams

Standard gtag.js event parameters.
For more information, see
[the gtag.js documentation on parameters](https://developers.google.com/gtagjs/reference/parameter).

## Index

### Properties

- [affiliation](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#affiliation)
- [checkout_option](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#checkout_option)
- [checkout_step](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#checkout_step)
- [content_type](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#content_type)
- [coupon](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#coupon)
- [currency](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#currency)
- [description](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#description)
- [event_category](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#event_category)
- [event_label](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#event_label)
- [fatal](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#fatal)
- [firebase_screen](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#firebase_screen)
- [firebase_screen_class](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#firebase_screen_class)
- [item_id](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#item_id)
- [item_list_id](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#item_list_id)
- [item_list_name](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#item_list_name)
- [items](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#items)
- [method](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#method)
- [number](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#number)
- [payment_type](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#payment_type)
- [promotion_id](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#promotion_id)
- [promotion_name](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#promotion_name)
- [promotions](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#promotions)
- [screen_name](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#screen_name)
- [search_term](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#search_term)
- [shipping](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#shipping)
- [shipping_tier](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#shipping_tier)
- [tax](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#tax)
- [transaction_id](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#transaction_id)
- [value](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.EventParams#value)

## Properties

### Optional affiliation

affiliation: string

### Optional checkout_option

checkout_option: string

### Optional checkout_step

checkout_step: number

### Optional content_type

content_type: string

### Optional coupon

coupon: string

### Optional currency

currency: string

### Optional description

description: string

### event_category

event_category: string

### Optional event_label

event_label: string

### Optional fatal

fatal: boolean

### Optional firebase_screen

firebase_screen: string  
Firebase-specific. Use to log a `screen_name` to Firebase Analytics.

### Optional firebase_screen_class

firebase_screen_class: string  
Firebase-specific. Use to log a `screen_class` to Firebase Analytics.

### Optional item_id

item_id: string

### Optional item_list_id

item_list_id: string

### Optional item_list_name

item_list_name: string

### Optional items

items: [Item](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Item)\[\]

### Optional method

method: string

### Optional number

number: string

### Optional payment_type

payment_type: string

### Optional promotion_id

promotion_id: string

### Optional promotion_name

promotion_name: string

### Optional promotions

promotions: [Promotion](https://firebase.google.com/docs/reference/js/v8/firebase.analytics.Promotion)\[\]

### Optional screen_name

screen_name: string

### Optional search_term

search_term: string

### Optional shipping

shipping: [Currency](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#currency)

### Optional shipping_tier

shipping_tier: string

### Optional tax

tax: [Currency](https://firebase.google.com/docs/reference/js/v8/firebase.analytics#currency)

### Optional transaction_id

transaction_id: string

### Optional value

value: number