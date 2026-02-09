# Source: https://docs.klarna.com/resources/business-tools/merchant-portal-guide/payments.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/payments.md

# Klarna Payments in Salesforce Commerce Cloud

## Klarna Payments enables merchants to integrate flexible payment options like Pay Now, Pay Later, and Financing. It supports easy configuration through the Business Manager, enhancing the checkout experience and boosting conversion rates. Advanced features include virtual card settlements and streamlined fraud management for secure and efficient transactions.

## Key features

**Integrate Klarna Payments using Best Practices**

- Available for international markets including North America, Europe, and Oceania.
- Klarna Payments on SFRA can be configured independently on each site by region.
- Supports multiple Klarna payment methods: Pay Now, Pay Later, and Pay Over Time.
- Quick integration with a virtual card-based approach for settlement.
- Compliant with GDPR (EU) standards for checkout flow.
- Supports multi-shipping addresses.  

**Payment and Notification Handling**

- Handles notifications for pending status updates (`reject`/`accept`) for suspected orders after review.
- Supports Klarna authorization with finalization for bank transfer methods (Pay Now).
- Supports Auto-Capture of payments.

**Advanced Features**

- BOPIS (Buy Online, Pickup in Store) support, including additional merchant data.
- Supports Klarna payment method-based promotions.
- Supports adjusted price promotions under the Gross Tax Policy.

## Klarna Payments cartridge integration

The Klarna cartridge utilizes the Klarna Payments JSON REST API and JavaScript SDK for storefront integration. This integration displays various payment options via the Klarna widget. **Customer Interaction** Customers select Klarna as their payment method, review the payment terms, and authorize payment by clicking the "Place Order" button. **Order Creation** Upon authorization, a Klarna order is created, and the customer is redirected to the confirmation page. **Fraud Status Management**

- Orders with a fraud status of `ACCEPTED` proceed with standard order creation in the SCC.


![ Klarna Payment Details in Business Manager](ZuBY_RoQrfVKl7I9_SFCC-KlarnaPaymentDetailsinBM.jpeg)
*Klarna Payment Details in Business Manager*

- Orders with a `PENDING` status undergo further review. If later accepted as `FRAUD_RISK_ACCEPTED`, the SCC order status updates accordingly.


![ Klarna Payment Details in Business Manager](ZuBZaxoQrfVKl7Jp_SFCC-KlarnaPaymentDetailsinBM2.jpeg)
*Klarna Payment Details in Business Manager*

### Key Attributes and Business Manager Details

- **Custom Attribute for Payment Status:** The fraud status of Klarna Payments is stored in a custom attribute `kpFraudStatus` within the PaymentTransaction system object.
- **Business Manager View:**This status is visible in the Business Manager on the order details Payment tab.

## Locales

The Klarna Payments cartridge supports multiple locales, ensuring a seamless experience for a global customer base. Supported locales include:

- English
- Danish
- Dutch
- Finnish
- French
- German
- Italian
- Polish
- Spanish
- Swedish

For a comprehensive list of the 25+ supported locales, please check [here](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md).