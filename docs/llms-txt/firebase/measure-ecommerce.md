# Source: https://firebase.google.com/docs/analytics/measure-ecommerce.md.txt

[Ecommerce](https://support.google.com/analytics/answer/9786881)allows measurement of user interactions with products across your users' shopping experiences, including interactions such as product (item) list views, product list clicks, viewing product details, adding a product to a shopping cart, initiating the checkout process, purchases, and refunds.

For details on implementing ecommerce web apps, see[Google Analytics Ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce).

## Before you begin

Make sure that you've set up your project and can access Analytics as described in[Get Started with Analytics](https://firebase.google.com/docs/analytics/get-started). Ecommerce measurement requires you to link your Firebase project to anAnalyticsaccount and to have the Android SDK v17.3.0 or iOS v6.20.0 and up in your app.

## Implementation

A typical ecommerce implementation measures any of the following actions:

- [Select a product from a list](https://firebase.google.com/docs/analytics/measure-ecommerce#select_product)
- [View product details](https://firebase.google.com/docs/analytics/measure-ecommerce#view_product)
- [Add/remove a product from a shopping cart](https://firebase.google.com/docs/analytics/measure-ecommerce#add_remove_product)
- [Initiate the checkout process](https://firebase.google.com/docs/analytics/measure-ecommerce#initiate_checkout)
- [Make purchases or refunds](https://firebase.google.com/docs/analytics/measure-ecommerce#make_purchase_refund)
- [Apply promotions](https://firebase.google.com/docs/analytics/measure-ecommerce#apply_promotions)

At the heart of these actions are products. Products can be instrumented as an array of items that can be added to prescribed ecommerce events.

Note the following limits:

- An array of items can include up to 27[custom parameters](https://firebase.google.com/docs/analytics/measure-ecommerce#item_custom_parameters), in addition to the prescribed parameters.

- A single ecommerce event can include up to 200 items. If you try to send more than 200 items, any items beyond this limit will be dropped and not included in the event data.

The following example demonstrates how to create an array of items that is referenced throughout this guide.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// A pair of jeggings
var jeggings: [String: Any] = [
  AnalyticsParameterItemID: "SKU_123",
  AnalyticsParameterItemName: "jeggings",
  AnalyticsParameterItemCategory: "pants",
  AnalyticsParameterItemVariant: "black",
  AnalyticsParameterItemBrand: "Google",
  AnalyticsParameterPrice: 9.99,
]

// A pair of boots
var boots: [String: Any] = [
  AnalyticsParameterItemID: "SKU_456",
  AnalyticsParameterItemName: "boots",
  AnalyticsParameterItemCategory: "shoes",
  AnalyticsParameterItemVariant: "brown",
  AnalyticsParameterItemBrand: "Google",
  AnalyticsParameterPrice: 24.99,
]

// A pair of socks
var socks: [String: Any] = [
  AnalyticsParameterItemID: "SKU_789",
  AnalyticsParameterItemName: "ankle_socks",
  AnalyticsParameterItemCategory: "socks",
  AnalyticsParameterItemVariant: "red",
  AnalyticsParameterItemBrand: "Google",
  AnalyticsParameterPrice: 5.99,
]https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L47-L75
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// A pair of jeggings
NSMutableDictionary *jeggings = [@{
  kFIRParameterItemID: @"SKU_123",
  kFIRParameterItemName: @"jeggings",
  kFIRParameterItemCategory: @"pants",
  kFIRParameterItemVariant: @"black",
  kFIRParameterItemBrand: @"Google",
  kFIRParameterPrice: @9.99,
} mutableCopy];

// A pair of boots
NSMutableDictionary *boots = [@{
  kFIRParameterItemID: @"SKU_456",
  kFIRParameterItemName: @"boots",
  kFIRParameterItemCategory: @"shoes",
  kFIRParameterItemVariant: @"brown",
  kFIRParameterItemBrand: @"Google",
  kFIRParameterPrice: @24.99,
} mutableCopy];

// A pair of socks
NSMutableDictionary *socks = [@{
  kFIRParameterItemID: @"SKU_789",
  kFIRParameterItemName: @"ankle_socks",
  kFIRParameterItemCategory: @"socks",
  kFIRParameterItemVariant: @"red",
  kFIRParameterItemBrand: @"Google",
  kFIRParameterPrice: @5.99,
} mutableCopy];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L44-L72
```

### Kotlin

```kotlin
val itemJeggings = Bundle().apply {
    putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_123")
    putString(FirebaseAnalytics.Param.ITEM_NAME, "jeggings")
    putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "pants")
    putString(FirebaseAnalytics.Param.ITEM_VARIANT, "black")
    putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google")
    putDouble(FirebaseAnalytics.Param.PRICE, 9.99)
}

val itemBoots = Bundle().apply {
    putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_456")
    putString(FirebaseAnalytics.Param.ITEM_NAME, "boots")
    putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "shoes")
    putString(FirebaseAnalytics.Param.ITEM_VARIANT, "brown")
    putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google")
    putDouble(FirebaseAnalytics.Param.PRICE, 24.99)
}

val itemSocks = Bundle().apply {
    putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_789")
    putString(FirebaseAnalytics.Param.ITEM_NAME, "ankle_socks")
    putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "socks")
    putString(FirebaseAnalytics.Param.ITEM_VARIANT, "red")
    putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google")
    putDouble(FirebaseAnalytics.Param.PRICE, 5.99)
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L51-L76
```

### Java

```java
Bundle itemJeggings = new Bundle();
itemJeggings.putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_123");
itemJeggings.putString(FirebaseAnalytics.Param.ITEM_NAME, "jeggings");
itemJeggings.putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "pants");
itemJeggings.putString(FirebaseAnalytics.Param.ITEM_VARIANT, "black");
itemJeggings.putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google");
itemJeggings.putDouble(FirebaseAnalytics.Param.PRICE, 9.99);

Bundle itemBoots = new Bundle();
itemBoots.putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_456");
itemBoots.putString(FirebaseAnalytics.Param.ITEM_NAME, "boots");
itemBoots.putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "shoes");
itemBoots.putString(FirebaseAnalytics.Param.ITEM_VARIANT, "brown");
itemBoots.putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google");
itemBoots.putDouble(FirebaseAnalytics.Param.PRICE, 24.99);

Bundle itemSocks = new Bundle();
itemSocks.putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_789");
itemSocks.putString(FirebaseAnalytics.Param.ITEM_NAME, "ankle_socks");
itemSocks.putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "socks");
itemSocks.putString(FirebaseAnalytics.Param.ITEM_VARIANT, "red");
itemSocks.putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google");
itemSocks.putDouble(FirebaseAnalytics.Param.PRICE, 5.99);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L67-L89
```

### Web

```javascript
// A pair of jeggings
const item_jeggings = {
  item_id: 'SKU_123',
  item_name: 'jeggings',
  item_category: 'pants',
  item_variant: 'black',
  item_brand: 'Google',
  price: 9.99
};

// A pair of boots
const item_boots = {
  item_id: 'SKU_456',
  item_name: 'boots',
  item_category: 'shoes',
  item_variant: 'brown',
  item_brand: 'Google',
  price: 24.99
};

// A pair of socks
const item_socks = {
  item_id: 'SKU_789',
  item_name: 'ankle_socks',
  item_category: 'socks',
  item_variant: 'red',
  item_brand: 'Google',
  price: 5.99
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_items.js#L8-L36
```

### Web

```javascript
// A pair of jeggings
const item_jeggings = {
  item_id: 'SKU_123',
  item_name: 'jeggings',
  item_category: 'pants',
  item_variant: 'black',
  item_brand: 'Google',
  price: 9.99
};

// A pair of boots
const item_boots = {
  item_id: 'SKU_456',
  item_name: 'boots',
  item_category: 'shoes',
  item_variant: 'brown',
  item_brand: 'Google',
  price: 24.99
};

// A pair of socks
const item_socks = {
  item_id: 'SKU_789',
  item_name: 'ankle_socks',
  item_category: 'socks',
  item_variant: 'red',
  item_brand: 'Google',
  price: 5.99
};https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L5-L33
```

### Dart

    // A pair of jeggings
    final jeggings = AnalyticsEventItem(
        itemId: "SKU_123",
        itemName: "jeggings",
        itemCategory: "pants",
        itemVariant: "black",
        itemBrand: "Google",
        price: 9.99,
    );

    // A pair of boots
    final boots = AnalyticsEventItem(
        itemId: "SKU_456",
        itemName: "boots",
        itemCategory: "shoes",
        itemVariant: "brown",
        itemBrand: "Google",
        price: 24.99,
    );

    // A pair of socks
    final socks = AnalyticsEventItem(
        itemId: "SKU_789",
        itemName: "ankle_socks",
        itemCategory: "socks",
        itemVariant: "red",
        itemBrand: "Google",
        price: 5.99,
    );

### Select a product from a list

When a user is presented with a list of results, log a`view_item_list`event including an`items`array parameter containing the displayed products.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Add item indexes
jeggings[AnalyticsParameterIndex] = 1
boots[AnalyticsParameterIndex] = 2
socks[AnalyticsParameterIndex] = 3

// Prepare ecommerce parameters
var itemList: [String: Any] = [
  AnalyticsParameterItemListID: "L001",
  AnalyticsParameterItemListName: "Related products",
]

// Add items array
itemList[AnalyticsParameterItems] = [jeggings, boots, socks]

// Log view item list event
Analytics.logEvent(AnalyticsEventViewItemList, parameters: itemList)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L81-L96
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Add item indexes
jeggings[kFIRParameterIndex] = @1;
boots[kFIRParameterIndex] = @2;
socks[kFIRParameterIndex] = @3;

// Prepare ecommerce parameters
NSMutableDictionary *itemList = [@{
  kFIRParameterItemListID: @"L001",
  kFIRParameterItemListName: @"Related products",
} mutableCopy];

// Add items array
itemList[kFIRParameterItems] = @[jeggings, boots, socks];

// Log view item list event
[FIRAnalytics logEventWithName:kFIREventViewItemList parameters:itemList];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L78-L93
```

### Kotlin

```kotlin
val itemJeggingsWithIndex = Bundle(itemJeggings).apply {
    putLong(FirebaseAnalytics.Param.INDEX, 1)
}
val itemBootsWithIndex = Bundle(itemBoots).apply {
    putLong(FirebaseAnalytics.Param.INDEX, 2)
}
val itemSocksWithIndex = Bundle(itemSocks).apply {
    putLong(FirebaseAnalytics.Param.INDEX, 3)
}

firebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_ITEM_LIST) {
    param(FirebaseAnalytics.Param.ITEM_LIST_ID, "L001")
    param(FirebaseAnalytics.Param.ITEM_LIST_NAME, "Related products")
    param(
        FirebaseAnalytics.Param.ITEMS,
        arrayOf(itemJeggingsWithIndex, itemBootsWithIndex, itemSocksWithIndex),
    )
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L80-L97
```

### Java

```java
Bundle itemJeggingsWithIndex = new Bundle(itemJeggings);
itemJeggingsWithIndex.putLong(FirebaseAnalytics.Param.INDEX, 1);

Bundle itemBootsWithIndex = new Bundle(itemBoots);
itemBootsWithIndex.putLong(FirebaseAnalytics.Param.INDEX, 2);

Bundle itemSocksWithIndex = new Bundle(itemSocks);
itemSocksWithIndex.putLong(FirebaseAnalytics.Param.INDEX, 3);

Bundle viewItemListParams = new Bundle();
viewItemListParams.putString(FirebaseAnalytics.Param.ITEM_LIST_ID, "L001");
viewItemListParams.putString(FirebaseAnalytics.Param.ITEM_LIST_NAME, "Related products");
viewItemListParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsWithIndex, itemBootsWithIndex, itemSocksWithIndex});
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_ITEM_LIST, viewItemListParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L93-L107
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params1 = {
  item_list_id: 'L001',
  item_list_name: 'Related products',
  items: [item_jeggings, item_boots, item_socks]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'view_item_list', params1);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_view_item_list.js#L8-L19
```

### Web

```javascript
// Prepare ecommerce params
const params1 = {
  item_list_id: 'L001',
  item_list_name: 'Related products',
  items: [item_jeggings, item_boots, item_socks]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.VIEW_ITEM_LIST, params1);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L38-L46
```

### Dart

    await FirebaseAnalytics.instance.logViewItemList(
        itemListId: "L001",
        itemListName: "Related products",
        items: [jeggings, boots, socks],
    );

Once a user selects a particular product from the list, log a`select_item`event with the chosen product in an`items`array parameter.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare ecommerce parameters
var selectedItem: [String: Any] = [
  AnalyticsParameterItemListID: "L001",
  AnalyticsParameterItemListName: "Related products",
]

// Add items array
selectedItem[AnalyticsParameterItems] = [jeggings]

// Log select item event
Analytics.logEvent(AnalyticsEventSelectItem, parameters: selectedItem)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L100-L110
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare ecommerce parameters
NSMutableDictionary *selectedItem = [@{
  kFIRParameterItemListID: @"L001",
  kFIRParameterItemListName: @"Related products",
} mutableCopy];

// Add items array
selectedItem[kFIRParameterItems] = @[jeggings];

// Log select item event
[FIRAnalytics logEventWithName:kFIREventSelectItem parameters:selectedItem];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L97-L107
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_ITEM) {
    param(FirebaseAnalytics.Param.ITEM_LIST_ID, "L001")
    param(FirebaseAnalytics.Param.ITEM_LIST_NAME, "Related products")
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggings))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L101-L105
```

### Java

```java
Bundle selectItemParams = new Bundle();
selectItemParams.putString(FirebaseAnalytics.Param.ITEM_LIST_ID, "L001");
selectItemParams.putString(FirebaseAnalytics.Param.ITEM_LIST_NAME, "Related products");
selectItemParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggings});
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_ITEM, selectItemParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L111-L116
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce event params
const params2 = {
  item_list_id: 'L001',
  item_list_name: 'Related products',
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'select_item', params2);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_select_item.js#L8-L19
```

### Web

```javascript
// Prepare ecommerce event params
const params2 = {
  item_list_id: 'L001',
  item_list_name: 'Related products',
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.SELECT_ITEM, params2);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L52-L60
```

### Dart

    await FirebaseAnalytics.instance.logSelectItem(
        itemListId: "L001",
        itemListName: "Related products",
        items: [jeggings],
    );

### View product details

To measure how many times product details are viewed, log a`view_item`event whenever a user views a product's details screen.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare ecommerce parameters
var productDetails: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 9.99
]

// Add items array
productDetails[AnalyticsParameterItems] = [jeggings]

// Log view item event
Analytics.logEvent(AnalyticsEventViewItem, parameters: productDetails)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L116-L126
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare ecommerce parameters
NSMutableDictionary *productDetails = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @9.99
} mutableCopy];

// Add items array
productDetails[kFIRParameterItems] = @[jeggings];

// Log view item event
[FIRAnalytics logEventWithName:kFIREventViewItem parameters:productDetails];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L113-L123
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_ITEM) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 9.99)
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggings))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L109-L113
```

### Java

```java
Bundle viewItemParams = new Bundle();
viewItemParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
viewItemParams.putDouble(FirebaseAnalytics.Param.VALUE, 9.99);
viewItemParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggings});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_ITEM, viewItemParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L120-L126
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce event params
const params3 = {
  currency: 'USD',
  value: 9.99,
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'view_item', params3);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_view_item_details.js#L8-L19
```

### Web

```javascript
  // Prepare ecommerce event params
  const params3 = {
    currency: 'USD',
    value: 9.99,
    items: [item_jeggings]
  };

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.VIEW_ITEM, params3);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L66-L74
```

### Dart

    await FirebaseAnalytics.instance.logViewItem(
        currency: 'USD',
        value: 9.99,
        items: [jeggings],
    );

### Add or remove a product from a shopping cart

Measure a product being added to a wishlist or cart by logging an`add_to_wishlist`or`add_to_cart`event, respectively, with the relevant products in an`items`array parameter.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Specify order quantity
jeggings[AnalyticsParameterQuantity] = 2

// Prepare item detail params
var itemDetails: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 19.98
]

// Add items
itemDetails[AnalyticsParameterItems] = [jeggings]

// Log an event when product is added to wishlist
Analytics.logEvent(AnalyticsEventAddToWishlist, parameters: itemDetails)

// Log an event when product is added to cart
Analytics.logEvent(AnalyticsEventAddToCart, parameters: itemDetails)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L132-L148
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Specify order quantity
jeggings[kFIRParameterQuantity] = @2;

// Prepare item detail params
NSMutableDictionary *itemDetails = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @19.98
} mutableCopy];

// Add items
itemDetails[kFIRParameterItems] = @[jeggings];

// Log an event when product is added to wishlist
[FIRAnalytics logEventWithName:kFIREventAddToWishlist parameters:itemDetails];

// Log an event when product is added to cart
[FIRAnalytics logEventWithName:kFIREventAddToCart parameters:itemDetails];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L129-L145
```

### Kotlin

```kotlin
val itemJeggingsWishlist = Bundle(itemJeggings).apply {
    putLong(FirebaseAnalytics.Param.QUANTITY, 2)
}

firebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_TO_WISHLIST) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 2 * 9.99)
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsWishlist))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L117-L125
```

### Java

```java
Bundle itemJeggingsWishlist = new Bundle(itemJeggings);
itemJeggingsWishlist.putLong(FirebaseAnalytics.Param.QUANTITY, 2);

Bundle addToWishlistParams = new Bundle();
addToWishlistParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
addToWishlistParams.putDouble(FirebaseAnalytics.Param.VALUE, 2 * 9.99);
addToWishlistParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsWishlist});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_TO_WISHLIST, addToWishlistParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L130-L139
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Specify order quantity
const item_jeggings_quantity = {
  ...item_jeggings,
  quantity: 2
};

// Prepare ecommerce bundle
const params4 = {
  currency: 'USD',
  value: 19.98,
  items: [item_jeggings_quantity]
};

// Log event when a product is added to a wishlist
const analytics = getAnalytics();
logEvent(analytics, 'add_to_wishlist', params4);

// Log event when a product is added to the cart
logEvent(analytics, 'add_to_cart', params4);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_add_cart.js#L8-L28
```

### Web

```javascript
// Specify order quantity
const item_jeggings_quantity = {
  ...item_jeggings,
  quantity: 2
};

// Prepare ecommerce bundle
const params4 = {
  currency: 'USD',
  value: 19.98,
  items: [item_jeggings_quantity]
};

// Log event when a product is added to a wishlist
firebase.analytics().logEvent(firebase.analytics.EventName.ADD_TO_WISHLIST, params4);

// Log event when a product is added to the cart
firebase.analytics().logEvent(firebase.analytics.EventName.ADD_TO_CART, params4);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L80-L97
```

### Dart

    final jeggingsWithQuantity = AnalyticsEventItem(
        itemId: jeggings.itemId,
        itemName: jeggings.itemName,
        itemCategory: jeggings.itemCategory,
        itemVariant: jeggings.itemVariant,
        itemBrand: jeggings.itemBrand,
        price: jeggings.price,
        quantity: 2,
    );
    await FirebaseAnalytics.instance.logAddToWishlist(
        currency: 'USD',
        value: 19.98,
        items: [jeggingsWithQuantity],
    );
    await FirebaseAnalytics.instance.logAddToCart(
        currency: 'USD',
        value: 19.98,
        items: [jeggingsWithQuantity],
    );

When a user subsequently views the cart, log the`view_cart`event with all`items`in the cart.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Specify order quantity
jeggings[AnalyticsParameterQuantity] = 2
boots[AnalyticsParameterQuantity] = 1

// Prepare order parameters
var orderParameters: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 44.97
]

// Add items array
orderParameters[AnalyticsParameterItems] = [jeggings, boots]

// Log event when cart is viewed
Analytics.logEvent(AnalyticsEventViewCart, parameters: orderParameters)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L152-L166
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Specify order quantity
jeggings[kFIRParameterQuantity] = @2;
boots[kFIRParameterQuantity] = @1;

// Prepare order parameters
NSMutableDictionary *orderParameters = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @44.97
} mutableCopy];

// Add items array
orderParameters[kFIRParameterItems] = @[jeggings, boots];

// Log event when cart is viewed
[FIRAnalytics logEventWithName:kFIREventViewCart parameters:orderParameters];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L149-L163
```

### Kotlin

```kotlin
val itemJeggingsCart = Bundle(itemJeggings).apply {
    putLong(FirebaseAnalytics.Param.QUANTITY, 2)
}
val itemBootsCart = Bundle(itemBoots).apply {
    putLong(FirebaseAnalytics.Param.QUANTITY, 1)
}

firebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_CART) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 2 * 9.99 + 1 * 24.99)
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsCart, itemBootsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L129-L140
```

### Java

```java
Bundle itemJeggingsCart = new Bundle(itemJeggings);
itemJeggingsCart.putLong(FirebaseAnalytics.Param.QUANTITY, 2);

Bundle itemBootsCart = new Bundle(itemBoots);
itemBootsCart.putLong(FirebaseAnalytics.Param.QUANTITY, 1);

Bundle viewCartParams = new Bundle();
viewCartParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
viewCartParams.putDouble(FirebaseAnalytics.Param.VALUE, (2 * 9.99) + (1 * 24.99));
viewCartParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsCart, itemBootsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_CART, viewCartParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L143-L155
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Specify order quantity
const item_jeggings_quantity = {
  ...item_jeggings,
  quantity: 2
};

const item_boots_quantity = {
  ...item_boots,
  quantity: 1
};

// Prepare ecommerce params
const params5 = {
  currency: 'USD',
  value: 44.97,
  items: [item_jeggings_quantity, item_boots_quantity]
};

// Log event when the cart is viewed
const analytics = getAnalytics();
logEvent(analytics, 'view_cart', params5);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_view_cart.js#L8-L30
```

### Web

```javascript
// Specify order quantity
const item_jeggings_quantity = {
  ...item_jeggings,
  quantity: 2
};

const item_boots_quantity = {
  ...item_boots,
  quantity: 1
};

// Prepare ecommerce params
const params5 = {
  currency: 'USD',
  value: 44.97,
  items: [item_jeggings_quantity, item_boots_quantity]
};

// Log event when the cart is viewed
firebase.analytics().logEvent(firebase.analytics.EventName.VIEW_CART, params5);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L103-L122
```

### Dart

    await FirebaseAnalytics.instance.logViewCart(
        currency: 'USD',
        value: 19.98,
        items: [jeggingsWithQuantity],
    );

To measure when a user removes a product from a cart, log the`remove_from_cart`event.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Specify removal quantity
boots[AnalyticsParameterQuantity] = 1

// Prepare params
var removeParams: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 24.99
]

// Add items
removeParams[AnalyticsParameterItems] = [boots]

// Log removal event
Analytics.logEvent(AnalyticsEventRemoveFromCart, parameters: removeParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L170-L183
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Specify removal quantity
boots[kFIRParameterQuantity] = @1;

// Prepare params
NSMutableDictionary *removeParams = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @24.99
} mutableCopy];

// Add items
removeParams[kFIRParameterItems] = @[boots];

// Log removal event
[FIRAnalytics logEventWithName:kFIREventRemoveFromCart parameters:removeParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L167-L180
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.REMOVE_FROM_CART) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 1 * 24.99)
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemBootsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L144-L148
```

### Java

```java
Bundle removeCartParams = new Bundle();
removeCartParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
removeCartParams.putDouble(FirebaseAnalytics.Param.VALUE, (1 * 24.99));
removeCartParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemBootsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.REMOVE_FROM_CART, removeCartParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L159-L165
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params6 = {
  currency: 'USD',
  value: 24.99,
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'remove_from_cart', params6);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_remove_cart.js#L8-L19
```

### Web

```javascript
// Prepare ecommerce params
const params6 = {
  currency: 'USD',
  value: 24.99,
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.REMOVE_FROM_CART, params6);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L128-L136
```

### Dart

    final jeggingsWithQuantity = AnalyticsEventItem(
        itemId: jeggings.itemId,
        itemName: jeggings.itemName,
        itemCategory: jeggings.itemCategory,
        itemVariant: jeggings.itemVariant,
        itemBrand: jeggings.itemBrand,
        price: jeggings.price,
        quantity: 1,
    );
    await FirebaseAnalytics.instance.logRemoveFromCart(
        currency: 'USD',
        value: 9.99,
        items: [jeggingsWithQuantity],
    );

### Initiate the checkout process

Measure the first step in a checkout process by logging a`begin_checkout`event with one or more`items`defined with the relevant fields. A coupon can also be added at this stage to the entire order by adding it to the event or applied to a particular item by adding it to specific elements in the`items`array.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare checkout params
var checkoutParams: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 14.98,
  AnalyticsParameterCoupon: "SUMMER_FUN"
];

// Add items
checkoutParams[AnalyticsParameterItems] = [jeggings]

// Log checkout event
Analytics.logEvent(AnalyticsEventBeginCheckout, parameters: checkoutParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L189-L200
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare checkout params
NSMutableDictionary *checkoutParams = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @14.98,
  kFIRParameterCoupon: @"SUMMER_FUN"
} mutableCopy];

// Add items
checkoutParams[kFIRParameterItems] = @[jeggings];

// Log checkout event
[FIRAnalytics logEventWithName:kFIREventBeginCheckout parameters:checkoutParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L186-L197
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.BEGIN_CHECKOUT) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 14.98)
    param(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN")
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L152-L157
```

### Java

```java
Bundle beginCheckoutParams = new Bundle();
beginCheckoutParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
beginCheckoutParams.putDouble(FirebaseAnalytics.Param.VALUE, 14.98);
beginCheckoutParams.putString(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN");
beginCheckoutParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.BEGIN_CHECKOUT, beginCheckoutParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L169-L176
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params7 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'begin_checkout', params7);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_checkout.js#L8-L20
```

### Web

```javascript
// Prepare ecommerce params
const params7 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.BEGIN_CHECKOUT, params7);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L142-L151
```

### Dart

    await FirebaseAnalytics.instance.logBeginCheckout(
        currency: 'USD',
        value: 15.98,  // Discount applied.
        coupon: "SUMMER_FUN",
        items: [jeggingsWithQuantity],
    );

When a user proceeds to the next step in the checkout process and adds shipping information, log an`add_shipping_info`event. Use the parameter`shipping_tier`to specify the user's delivery option, such as "Ground", "Air", or "Next-day".  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare shipping params
var shippingParams: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 14.98,
  AnalyticsParameterCoupon: "SUMMER_FUN",
  AnalyticsParameterShippingTier: "Ground"
]

// Add items
shippingParams[AnalyticsParameterItems] = [jeggings]

// Log added shipping info event
Analytics.logEvent(AnalyticsEventAddShippingInfo, parameters: shippingParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L204-L216
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare shipping params
NSMutableDictionary *shippingParams = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @14.98,
  kFIRParameterCoupon: @"SUMMER_FUN",
  kFIRParameterShippingTier: @"Ground"
} mutableCopy];

// Add items
shippingParams[kFIRParameterItems] = @[jeggings];

// Log added shipping info event
[FIRAnalytics logEventWithName:kFIREventAddShippingInfo parameters:shippingParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L201-L213
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_SHIPPING_INFO) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 14.98)
    param(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN")
    param(FirebaseAnalytics.Param.SHIPPING_TIER, "Ground")
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L161-L167
```

### Java

```java
Bundle addShippingParams = new Bundle();
addShippingParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
addShippingParams.putDouble(FirebaseAnalytics.Param.VALUE, 14.98);
addShippingParams.putString(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN");
addShippingParams.putString(FirebaseAnalytics.Param.SHIPPING_TIER, "Ground");
addShippingParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_SHIPPING_INFO, addShippingParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L180-L188
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params8 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  shipping_tier: 'Ground',
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'add_shipping_info', params8);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_shipping_info.js#L8-L21
```

### Web

```javascript
// Prepare ecommerce params
const params8 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  shipping_tier: 'Ground',
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.ADD_SHIPPING_INFO, params8);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L157-L167
```

### Dart

    await FirebaseAnalytics.instance.logAddShippingInfo(
        currency: 'USD',
        value: 15.98,
        coupon: "SUMMER_FUN",
        shippingTier: "Ground",
        items: [jeggingsWithQuantity],
    );

Log`add_payment_info`when a user submits their payment information. If applicable, include`payment_type`with this event for the chosen method of payment.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare payment params
var paymentParams: [String: Any] = [
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 14.98,
  AnalyticsParameterCoupon: "SUMMER_FUN",
  AnalyticsParameterPaymentType: "Visa"
]

// Add items
paymentParams[AnalyticsParameterItems] = [jeggings]

// Log added payment info event
Analytics.logEvent(AnalyticsEventAddPaymentInfo, parameters: paymentParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L220-L232
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare payment params
NSMutableDictionary *paymentParams = [@{
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @14.98,
  kFIRParameterCoupon: @"SUMMER_FUN",
  kFIRParameterPaymentType: @"Visa"
} mutableCopy];

// Add items
paymentParams[kFIRParameterItems] = @[jeggings];

// Log added payment info event
[FIRAnalytics logEventWithName:kFIREventAddPaymentInfo parameters:paymentParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L217-L229
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_PAYMENT_INFO) {
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 14.98)
    param(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN")
    param(FirebaseAnalytics.Param.PAYMENT_TYPE, "Visa")
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L171-L177
```

### Java

```java
Bundle addPaymentParams = new Bundle();
addPaymentParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
addPaymentParams.putDouble(FirebaseAnalytics.Param.VALUE, 14.98);
addPaymentParams.putString(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN");
addPaymentParams.putString(FirebaseAnalytics.Param.PAYMENT_TYPE, "Visa");
addPaymentParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.ADD_PAYMENT_INFO, addPaymentParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L192-L200
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params9 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  payment_type: 'Visa',
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'add_payment_info', params9);  https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_payment_info.js#L8-L21
```

### Web

```javascript
// Prepare ecommerce params
const params9 = {
  currency: 'USD',
  value: 14.98, // Total Revenue
  coupon: 'SUMMER_FUN',
  payment_type: 'Visa',
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.ADD_PAYMENT_INFO, params9);  https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L173-L183
```

### Dart

    await FirebaseAnalytics.instance.logAddPaymentInfo(
        currency: 'USD',
        value: 15.98,
        coupon: "SUMMER_FUN",
        paymentType: "Visa",
        items: [jeggingsWithQuantity],
    );

### Make a purchase or issue a refund

Measure a purchase by logging a`purchase`event with one or more`items`defined with the relevant fields.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare purchase params
var purchaseParams: [String: Any] = [
  AnalyticsParameterTransactionID: "T12345",
  AnalyticsParameterAffiliation: "Google Store",
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 14.98,
  AnalyticsParameterTax: 2.58,
  AnalyticsParameterShipping: 5.34,
  AnalyticsParameterCoupon: "SUMMER_FUN"
]

// Add items
purchaseParams[AnalyticsParameterItems] = [jeggings]

// Log purchase event
Analytics.logEvent(AnalyticsEventPurchase, parameters: purchaseParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L238-L253
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare purchase params
NSMutableDictionary *purchaseParams = [@{
  kFIRParameterTransactionID: @"T12345",
  kFIRParameterAffiliation: @"Google Store",
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @14.98,
  kFIRParameterTax: @2.58,
  kFIRParameterShipping: @5.34,
  kFIRParameterCoupon: @"SUMMER_FUN"
} mutableCopy];

// Add items
purchaseParams[kFIRParameterItems] = @[jeggings];

// Log purchase event
[FIRAnalytics logEventWithName:kFIREventPurchase parameters:purchaseParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L235-L250
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.PURCHASE) {
    param(FirebaseAnalytics.Param.TRANSACTION_ID, "T12345")
    param(FirebaseAnalytics.Param.AFFILIATION, "Google Store")
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 14.98)
    param(FirebaseAnalytics.Param.TAX, 2.58)
    param(FirebaseAnalytics.Param.SHIPPING, 5.34)
    param(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN")
    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggingsCart))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L181-L190
```

### Java

```java
Bundle purchaseParams = new Bundle();
purchaseParams.putString(FirebaseAnalytics.Param.TRANSACTION_ID, "T12345");
purchaseParams.putString(FirebaseAnalytics.Param.AFFILIATION, "Google Store");
purchaseParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
purchaseParams.putDouble(FirebaseAnalytics.Param.VALUE, 14.98);
purchaseParams.putDouble(FirebaseAnalytics.Param.TAX, 2.58);
purchaseParams.putDouble(FirebaseAnalytics.Param.SHIPPING, 5.34);
purchaseParams.putString(FirebaseAnalytics.Param.COUPON, "SUMMER_FUN");
purchaseParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggingsCart});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.PURCHASE, purchaseParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L204-L215
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce bundle
const params10 = {
  transaction_id: 'T12345',
  affiliation: 'Google Store',
  currency: 'USD',
  value: 14.98, // Total Revenue
  tax: 2.85,
  shipping: 5.34,
  coupon: 'SUMMER_FUN',
  items: [item_jeggings]
};

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'purchase', params10);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_purchase.js#L8-L24
```

### Web

```javascript
// Prepare ecommerce bundle
const params10 = {
  transaction_id: 'T12345',
  affiliation: 'Google Store',
  currency: 'USD',
  value: 14.98, // Total Revenue
  tax: 2.85,
  shipping: 5.34,
  coupon: 'SUMMER_FUN',
  items: [item_jeggings]
};

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.PURCHASE, params10);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L189-L202
```

### Dart

    await FirebaseAnalytics.instance.logPurchase(
        transactionId: "12345",
        affiliation: "Google Store",
        currency: 'USD',
        value: 15.98,
        shipping: 2.00,
        tax: 1.66,
        coupon: "SUMMER_FUN",
        items: [jeggingsWithQuantity],
    );

| **Note:** The purchase event replaces`ecommerce_purchase`and is different from the`in_app_purchase`event, which is reported automatically.

Measure refunds by logging a`refund`event with the relevant`transaction_id`specified and optionally one or more`items`defined with`item_id`and`quantity`. We recommend that you include item information in your`refund`event to see item-level refund metrics in Analytics.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare refund params
var refundParams: [String: Any] = [
  AnalyticsParameterTransactionID: "T12345",
  AnalyticsParameterCurrency: "USD",
  AnalyticsParameterValue: 9.99,
]

// (Optional) for partial refunds, define the item ID and quantity of refunded items
let refundedProduct: [String: Any] = [
  AnalyticsParameterItemID: "SKU_123",
  AnalyticsParameterQuantity: 1,
];

// Add items
refundParams[AnalyticsParameterItems] = [refundedProduct]

// Log refund event
Analytics.logEvent(AnalyticsEventRefund, parameters: refundParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L257-L274
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare refund params
NSMutableDictionary *refundParams = [@{
  kFIRParameterTransactionID: @"T12345",
  kFIRParameterCurrency: @"USD",
  kFIRParameterValue: @9.99,
} mutableCopy];

// (Optional) for partial refunds, define the item ID and quantity of refunded items
NSDictionary *refundedProduct = @{
  kFIRParameterItemID: @"SKU_123",
  kFIRParameterQuantity: @1,
};

// Add items
refundParams[kFIRParameterItems] = @[refundedProduct];

// Log refund event
[FIRAnalytics logEventWithName:kFIREventRefund parameters:refundParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L254-L271
```

### Kotlin

```kotlin
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.REFUND) {
    param(FirebaseAnalytics.Param.TRANSACTION_ID, "T12345")
    param(FirebaseAnalytics.Param.AFFILIATION, "Google Store")
    param(FirebaseAnalytics.Param.CURRENCY, "USD")
    param(FirebaseAnalytics.Param.VALUE, 9.99)

    // (Optional) for partial refunds, define the item ID and quantity of refunded items
    param(FirebaseAnalytics.Param.ITEM_ID, "SKU_123")
    param(FirebaseAnalytics.Param.QUANTITY, 1)

    param(FirebaseAnalytics.Param.ITEMS, arrayOf(itemJeggings))
}https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L194-L205
```

### Java

```java
Bundle refundParams = new Bundle();
refundParams.putString(FirebaseAnalytics.Param.TRANSACTION_ID, "T12345");
refundParams.putString(FirebaseAnalytics.Param.AFFILIATION, "Google Store");
refundParams.putString(FirebaseAnalytics.Param.CURRENCY, "USD");
refundParams.putDouble(FirebaseAnalytics.Param.VALUE, 9.99);

// (Optional) for partial refunds, define the item ID and quantity of refunded items
refundParams.putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_123");
refundParams.putLong(FirebaseAnalytics.Param.QUANTITY, 1);

refundParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggings});

mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.REFUND, refundParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L219-L232
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params11 = {
  transaction_id: 'T12345', // Required
  affiliation: 'Google Store',
  currency: 'USD',
  value: 9.99,
  items: []
};

// (Optional) For partial refunds, define the item_id and quantity of refunded items
const refundedProduct = {
  item_id: 'SKU_123', // Required
  quantity: 1 // Required
};

params11.items.push(refundedProduct);

// Log event
const analytics = getAnalytics();
logEvent(analytics, 'refund', params11);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_refund.js#L8-L29
```

### Web

```javascript
// Prepare ecommerce params
const params11 = {
  transaction_id: 'T12345', // Required
  affiliation: 'Google Store',
  currency: 'USD',
  value: 9.99,
  items: []
};

// (Optional) For partial refunds, define the item_id and quantity of refunded items
const refundedProduct = {
  item_id: 'SKU_123', // Required
  quantity: 1 // Required
};

params11.items.push(refundedProduct);

// Log event
firebase.analytics().logEvent(firebase.analytics.EventName.REFUND, params11);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L208-L226
```

### Dart

    await FirebaseAnalytics.instance.logRefund(
        transactionId: "12345",
        affiliation: "Google Store",
        currency: 'USD',
        value: 15.98,
        items: [jeggingsWithQuantity],
    );

| **Note:** The`refund`event replaces`ecommerce_refund`.

### Apply promotions

Ecommerce includes support for measuring impressions and clicks of internal promotions, such as banners displayed to promote a sale.

Promotion impressions are typically measured with the initial screen view by logging the`view_promotion`event with an`items`parameter to specify the promoted product. To indicate a user clicked on a promotion, log a`select_promotion`event with that product as an`item`parameter.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

```swift
// Prepare promotion parameters
var promoParams: [String: Any] = [
  AnalyticsParameterPromotionID: "T12345",
  AnalyticsParameterPromotionName:"Summer Sale",
  AnalyticsParameterCreativeName: "summer2020_promo.jpg",
  AnalyticsParameterCreativeSlot: "featured_app_1",
  AnalyticsParameterLocationID: "HERO_BANNER",
]

// Add items
promoParams[AnalyticsParameterItems] = [jeggings]

// Log event when promotion is displayed
Analytics.logEvent(AnalyticsEventViewPromotion, parameters: promoParams)

// Log event when promotion is selected
Analytics.logEvent(AnalyticsEventSelectPromotion, parameters: promoParams)https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/ViewController.swift#L280-L296
```

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

```objective-c
// Prepare promotion parameters
NSMutableDictionary *promoParams = [@{
  kFIRParameterPromotionID: @"T12345",
  kFIRParameterPromotionName: @"Summer Sale",
  kFIRParameterCreativeName: @"summer2020_promo.jpg",
  kFIRParameterCreativeSlot: @"featured_app_1",
  kFIRParameterLocationID: @"HERO_BANNER",
} mutableCopy];

// Add items
promoParams[kFIRParameterItems] = @[jeggings];

// Log event when promotion is displayed
[FIRAnalytics logEventWithName:kFIREventViewPromotion parameters:promoParams];

// Log event when promotion is selected
[FIRAnalytics logEventWithName:kFIREventSelectPromotion parameters:promoParams];https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/firoptions/FiroptionConfiguration/AnalyticsHelper.m#L277-L293
```

### Kotlin

```kotlin
val promoParams = Bundle().apply {
    putString(FirebaseAnalytics.Param.PROMOTION_ID, "SUMMER_FUN")
    putString(FirebaseAnalytics.Param.PROMOTION_NAME, "Summer Sale")
    putString(FirebaseAnalytics.Param.CREATIVE_NAME, "summer2020_promo.jpg")
    putString(FirebaseAnalytics.Param.CREATIVE_SLOT, "featured_app_1")
    putString(FirebaseAnalytics.Param.LOCATION_ID, "HERO_BANNER")
    putParcelableArray(FirebaseAnalytics.Param.ITEMS, arrayOf<Parcelable>(itemJeggings))
}

// Promotion displayed
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_PROMOTION, promoParams)

// Promotion selected
firebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_PROMOTION, promoParams)https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/kotlin/MainActivity.kt#L209-L222
```

### Java

```java
Bundle promoParams = new Bundle();
promoParams.putString(FirebaseAnalytics.Param.PROMOTION_ID, "SUMMER_FUN");
promoParams.putString(FirebaseAnalytics.Param.PROMOTION_NAME, "Summer Sale");
promoParams.putString(FirebaseAnalytics.Param.CREATIVE_NAME, "summer2020_promo.jpg");
promoParams.putString(FirebaseAnalytics.Param.CREATIVE_SLOT, "featured_app_1");
promoParams.putString(FirebaseAnalytics.Param.LOCATION_ID, "HERO_BANNER");
promoParams.putParcelableArray(FirebaseAnalytics.Param.ITEMS,
        new Parcelable[]{itemJeggings});

// Promotion displayed
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.VIEW_PROMOTION, promoParams);

// Promotion selected
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SELECT_PROMOTION, promoParams);https://github.com/firebase/snippets-android/blob/13e06772027dc34151efbb8e17dc793b04702ec4/analytics/app/src/main/java/com/google/firebase/example/analytics/MainActivity.java#L236-L249
```

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

// Prepare ecommerce params
const params12 = {
  promotion_id: 'ABC123',
  promotion_name: 'Summer Sale',
  creative_name: 'summer2020_promo.jpg',
  creative_slot: 'featured_app_1',
  location_id: 'HERO_BANNER',
  items: [item_jeggings]
};

// Log event when a promotion is displayed
const analytics = getAnalytics();
logEvent(analytics, 'view_promotion', params12);

// Log event when a promotion is selected
logEvent(analytics, 'select_promotion', params12);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/snippets/analytics-next/ecommerce/analytics_ecommerce_promotions.js#L8-L25
```

### Web

```javascript
// Prepare ecommerce params
const params12 = {
  promotion_id: 'ABC123',
  promotion_name: 'Summer Sale',
  creative_name: 'summer2020_promo.jpg',
  creative_slot: 'featured_app_1',
  location_id: 'HERO_BANNER',
  items: [item_jeggings]
};

// Log event when a promotion is displayed
firebase.analytics().logEvent(firebase.analytics.EventName.VIEW_PROMOTION, params12);

// Log event when a promotion is selected
firebase.analytics().logEvent(firebase.analytics.EventName.SELECT_PROMOTION, params12);https://github.com/firebase/snippets-web/blob/95c8c159ff4d90af442352f058406f1aeb8adcbb/analytics/ecommerce.js#L232-L246
```

### Dart

    await FirebaseAnalytics.instance.logViewPromotion(
        promotionId: "SUMMER_FUN",
        promotionName: "Summer Sale",
        creativeName: "summer2020_promo.jpg",
        creativeSlot: "featured_app_1",
        locationId: "HERO_BANNER",
    );

    await FirebaseAnalytics.instance.logSelectPromotion(
        promotionId: "SUMMER_FUN",
        promotionName: "Summer Sale",
        creativeName: "summer2020_promo.jpg",
        creativeSlot: "featured_app_1",
        locationId: "HERO_BANNER",
    );

### Send item-scoped custom parameters

An item-scoped custom parameter is a parameter that isn't one of the parameters that Google includes in the list of required or optional parameters for an ecommerce item. The custom parameter lets you collect information about an item that's useful to your specific business.

From your app, you can send up to 27 item-scoped custom parameters in the array of items, of which you can configure 10[item-scoped custom dimensions](https://support.google.com/analytics/answer/10075209)for standard properties and 25 for Analytics 360 properties. This gives you the flexibility to choose from a larger pool of parameters without having to retag your app.  

### Swift

<br />

**Note:**This Firebase product is not available on the macOS target.  

    // A pair of jeggings
    var jeggings: [String: Any] = [
      AnalyticsParameterItemID: "SKU_123",
      AnalyticsParameterItemName: "jeggings",
      AnalyticsParameterItemCategory: "pants",
      AnalyticsParameterItemVariant: "black",
      AnalyticsParameterItemBrand: "Google",
      AnalyticsParameterPrice: 9.99,
      AnalyticsParameterItemColor: "blue", // The item-scoped custom parameter
    ]

### Objective-C

<br />

**Note:**This Firebase product is not available on the macOS target.  

    // A pair of jeggings
    NSMutableDictionary *jeggings = [@{
      kFIRParameterItemID: @"SKU_123",
      kFIRParameterItemName: @"jeggings",
      kFIRParameterItemCategory: @"pants",
      kFIRParameterItemVariant: @"black",
      kFIRParameterItemBrand: @"Google",
      kFIRParameterPrice: @9.99,
      kFIRParameterItemColor: @"blue", // The item-scoped custom parameter
    } mutableCopy];

### Kotlin

    val itemJeggings = Bundle().apply {
      putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_123")
      putString(FirebaseAnalytics.Param.ITEM_NAME, "jeggings")
      putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "pants")
      putString(FirebaseAnalytics.Param.ITEM_VARIANT, "black")
      putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google")
      putDouble(FirebaseAnalytics.Param.PRICE, 9.99)
      putString(FirebaseAnalytics.Param.ITEM_COLOR, "blue") // The item-scoped custom parameter
    }

### Java

    Bundle itemJeggings = new Bundle();
    itemJeggings.putString(FirebaseAnalytics.Param.ITEM_ID, "SKU_123");
    itemJeggings.putString(FirebaseAnalytics.Param.ITEM_NAME, "jeggings");
    itemJeggings.putString(FirebaseAnalytics.Param.ITEM_CATEGORY, "pants");
    itemJeggings.putString(FirebaseAnalytics.Param.ITEM_VARIANT, "black");
    itemJeggings.putString(FirebaseAnalytics.Param.ITEM_BRAND, "Google");
    itemJeggings.putDouble(FirebaseAnalytics.Param.PRICE, 9.99);
    itemJeggings.putDouble(FirebaseAnalytics.Param.ITEM_COLOR, 9.99); // The item-scoped custom parameter

### Web

    // A pair of jeggings
    const item_jeggings = {
      item_id: 'SKU_123',
      item_name: 'jeggings',
      item_category: 'pants',
      item_variant: 'black',
      item_brand: 'Google',
      price: 9.99,
      item_color: 'blue' // The item-scoped custom parameter
    };

### Web

    // A pair of jeggings
    const item_jeggings = {
      item_id: 'SKU_123',
      item_name: 'jeggings',
      item_category: 'pants',
      item_variant: 'black',
      item_brand: 'Google',
      price: 9.99,
      item_color: 'blue' // The item-scoped custom parameter
    };

### Dart

    // A pair of jeggings
    final jeggings = AnalyticsEventItem(
        itemId: "SKU_123",
        itemName: "jeggings",
        itemCategory: "pants",
        itemVariant: "black",
        itemBrand: "Google",
        price: 9.99,
        itemColor: "blue", // The item-scoped custom parameter
    );