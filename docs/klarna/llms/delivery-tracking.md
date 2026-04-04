# Source: https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking.md

# Delivery tracking

## Read this article to learn how to offer delivery tracking information to your customers.

If you bought something using Klarna and have questions about your delivery, please contact **`support@klarna.com`**. This section only contains technical details for partners integrating Klarna into an online store. When your customers want to see the delivery status of the goods they paid with Klarna, they can check our [Klarna app](https://www.klarna.com/us/klarna-app/) to track the delivery. The Klarna app offers a smooth and intuitive way for your customers to track the entire shipping lifecycle and get notifications throughout the different stages (for example, when the goods are in transit or ready to pick up).


![ Tracking information in the Klarna app.](f4c44cc5-c7ba-42d2-9fbf-27c796434b0a_Delivery+tracking_order+management.jpeg)
*Tracking information in the Klarna app.*

## Benefits

Some benefits of enabling delivery tracking are:

- Offering a smooth post-purchase experience to your customers
- Increasing customer satisfaction and loyalty
- Increasing the successful delivery rate
- Reducing customer service workload

## Enabling delivery tracking

To enable delivery tracking, you have to send us the shipping information, including details of the carrier that manages your deliveries. This way, we communicate to your customers the delivery updates through the Klarna app. We integrate with hundreds of [carriers](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list/) to provide your customers with the best possible post-purchase experience. To share tracking information with us, you have to:

1.  [Identify your carrier partner](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking/#enabling-delivery-tracking-identifying-your-carrier-partner).
2.  [Send us the information through the Order management API.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking/#enabling-delivery-tracking-sending-the-information)
3.  [Validate your integration](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking/#enabling-delivery-tracking-validating-your-integration).

### Identifying your carrier partner

The first step is identifying the carrier partner (logistic company) that manages your deliveries. We integrate with global companies such as \*\*DHL\*\*, \*\*UPS\*\*, \*\*FedEx\*\*, \*\*DPD\*\* \*\*DHL\*\*, \*\*UPS\*\*, \*\*FedEx\*\*, \*\*DPD\*\* and nationwide carriers such as \*\*OnTrac\*\*, \*\*Australia Post\*\*, \*\*Canada Post\*\*, \*\*La Poste\*\*, and \*\*Correos\*\*. To see a complete list of our partners, check the [carriers section.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list/) If you have any questions about Klarna carrier partners, contact **`logistics+integration@klarna.com`** While some carriers are recognized globally by their corporate entity brand (for example, DHL or DPD), some others use subsidiaries. If you have questions about your carrier's services, contact your carrier directly.

### Sending the information

Once you've identified the carrier that manages your deliveries, you're ready to go with the implementation. You can send us details for one or multiple deliveries using the following endpoints of the Order management API:

- [Capture an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders/)
  - (`POST {apiUrl}/ordermanagement/v1/orders/{order_id}/captures`[{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/captureOrder)/ordermanagement/v1/orders/{order_id}/captures)
- [Add shipping information](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking/)
  - (`POST `[`{apiUrl}`](https://docs.klarna.com/api/ordermanagement/#operation/appendShippingInfo)`/ordermanagement/v1/orders/{order_id}/captures/{capture_id}/shipping-info)`

Include the `shipping_info` parameter in your request. It's an array containing two attributes:

- **`shipping_company`**(required): The carrier (logistics company) managing the delivery. You can find the list of `shipping_company` values in the second column of the [carrier partner list](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list/).
- **`tracking_number`**(required): The identifier that the carrier provided to fetch further delivery updates.

The following is an example of a request with the information you have to send us.

``` json
"shipping_info": [
    {
    "shipping_company": "dhl-express",
    "tracking_number": "JJII1234567890234234234",
    }
]
```

Sample of a request to send the shipping information. You can add details for more than one delivery. For example, suppose a single order contains two packages with two different tracking numbers. In that case, you have to send us the information for each package. The following is an example of a request including two deliveries.

``` json
"shipping_info": [
    {
    "shipping_company": "fedex",
    "tracking_number": "941741365856",
    },
    {
    "shipping_company": "ups",
    "tracking_number": "1Z83V552YW00095703",
    }
]
```

Sample of a request to send the shipping information for two different deliveries.

#### Special cases

There are special cases when delivery tracking is not possible. You don't have to send us shipping information in your API call in the following cases:

- **Non-trackable deliveries:**The products might be shipped using a non-trackable postal product (for example, a regular letter).
- **Non-physical products:**For non-physical products, there are no physical deliveries.
- **Own delivery infrastructure:**We can't track your deliveries if you deliver the goods via your own delivery infrastructure or couriers.
- **Picking up products at a store:**For **Click and collect** or other In-store purchases, you don't need to include any shipping information in your API call. When a shipping company delivers the goods to the store and the shipment is trackable, you need to send the shipping information as usual.

Want to go further? The APIs enable you to send us more information such as shipping method and tracking URI, which can improve your customer's post-purchase experience. For more details, see our [API documentation](https://docs.klarna.com/api/ordermanagement/).

### Validating your integration

We don't perform any data validation at the moment of the API call. The data processing we run happens asynchronously in the background. This means that, for example, the call won't fail if the tracking number we receive is invalid. For this reason, you need to contact us to validate your integration after sending us the shipping information. Read the following section to learn about our contact and support channels.

#### Contact and support

If you want to validate your integration or have any questions about it, our Klarna Logistics team is ready to help you. Contact **`logistics+integration@klarna.com`** and include the following information in your email:

- As a subject, use *Delivery tracking integration: {merchant name}\*\*Delivery tracking integration: {merchant name}*'.
- As an email body, disclose your online store's URL and your Klarna's eStore ID/merchant ID.
- Include the order number to validate the integration.

You can also contact [Merchant support](https://www.klarna.com/merchant-support/) for any other questions regarding your integration.