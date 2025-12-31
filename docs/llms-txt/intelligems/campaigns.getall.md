# Source: https://docs.intelligems.io/developer-resources/javascript-api/campaigns-object/campaigns.getall.md

# campaigns.getAll()

{% hint style="success" %}
Gets all eligible campaigns and returns a list of campaigns with all nested data.
{% endhint %}

**Example**

```javascript
console.log(igData.campaigns.getAll())
```

**Return**

```json
[
    {
        "id": "b95ee9e7-34c7-4612-ad9e-fc75195551fc",
        "campaignId": "b95ee9e7-34c7-4612-ad9e-fc75195551fc",
        "name": "My first Campaign",
        "description": "This is a test Campaign so I can see what the Campaign object looks like",
        "discountId": "0d0ce9d7-652c-4adb-827b-62d8eb87b836",
        "discount": {
            "id": "0d0ce9d7-652c-4adb-827b-62d8eb87b836",
            "enabled": true,
            "combinesWithIntelligems": true,
            "combinesWithShopify": true,
            "name": "Discount",
            "isTest": false,
            "unitType": "unit",
            "discountType": "percentage",
            "discountApplicationType": "tieredDiscount",
            "discountApplicationMethod": "perOrder",
            "tiers": [
                {
                    "id": "1944f444-d85d-45fc-9da5-bbd7566416f9",
                    "minimumUnits": 5,
                    "maximumUnits": 6,
                    "unitDiscount": 10,
                    "discountTitle": "5 units gets you 10% off",
                    "isFreeShipping": false,
                    "isGiftWithPurchase": false,
                    "giftWithPurchaseProductId": null,
                    "giftWithPurchaseVariantId": null,
                    "autoAddGiftWithPurchase": true,
                    "giftWithPurchaseHandle": null
                },
                {
                    "id": "2ca983ee-7e49-432f-9b4a-5b02db4c13c2",
                    "minimumUnits": 7,
                    "maximumUnits": 9,
                    "unitDiscount": 15,
                    "discountTitle": "7 units gets you 15% off",
                    "isFreeShipping": false,
                    "isGiftWithPurchase": false,
                    "giftWithPurchaseProductId": null,
                    "giftWithPurchaseVariantId": null,
                    "autoAddGiftWithPurchase": true,
                    "giftWithPurchaseHandle": null
                },
                {
                    "id": "9ef6de6c-b48f-4d57-8aa1-195f6be2527a",
                    "minimumUnits": 10,
                    "maximumUnits": 1000000000,
                    "unitDiscount": 20,
                    "discountTitle": "10 units gets you 20% off",
                    "isFreeShipping": false,
                    "isGiftWithPurchase": false,
                    "giftWithPurchaseProductId": null,
                    "giftWithPurchaseVariantId": null,
                    "autoAddGiftWithPurchase": true,
                    "giftWithPurchaseHandle": null
                }
            ],
            "testProducts": [
                {
                    "id": "8467185303848",
                    "title": "Ceramic Risotto Plate",
                    "variants": [
                        {
                            "id": "46008284643624",
                            "title": "Lapis / Large",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284676392",
                            "title": "Lapis / XL",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284184872",
                            "title": "Cream / Small",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284807464",
                            "title": "Marigold / XL",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284348712",
                            "title": "Gainsboro / Medium",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284545320",
                            "title": "Volcanic / XL",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284447016",
                            "title": "Volcanic / Small",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284774696",
                            "title": "Marigold / Large",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284610856",
                            "title": "Lapis / Medium",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284709160",
                            "title": "Marigold / Small",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284512552",
                            "title": "Volcanic / Large",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284217640",
                            "title": "Cream / Medium",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284479784",
                            "title": "Volcanic / Medium",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284578088",
                            "title": "Lapis / Small",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284315944",
                            "title": "Gainsboro / Small",
                            "price": 25,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284283176",
                            "title": "Cream / XL",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284414248",
                            "title": "Gainsboro / XL",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284741928",
                            "title": "Marigold / Medium",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284381480",
                            "title": "Gainsboro / Large",
                            "price": 35,
                            "compareAtPrice": null
                        },
                        {
                            "id": "46008284250408",
                            "title": "Cream / Large",
                            "price": 35,
                            "compareAtPrice": null
                        }
                    ]
                }
            ],
            "isArchived": false
        },
        "findReplaces": [],
        "requiresLink": false,
        "linkBaseUrl": null,
        "enabledAtTs": null,
        "disabledAtTs": null,
        "isArchived": false,
        "isPreview": true,
        "createdAtTs": 1692908710645
    }
]
```
