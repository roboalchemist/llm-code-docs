# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/sap-commerce-cloud/payments/use-cases.md

# Use Cases on SAP Commerce Cloud

## This section outlines the capabilities of Klarna Payments, covering pre-purchase messaging, flexible order placement, efficient order management, and secure settlement options like Virtual Card Numbers, enhancing both customer experience and operational workflows.

Klarna Payments integration with SAP Commerce streamlines payment processes with features like On-site Messaging, dynamic payment options, and robust order management. Whether enhancing the pre-purchase experience, managing pending orders, or leveraging Virtual Card Numbers for secure settlements, Klarna offers tailored solutions to meet diverse business needs. This ensures a smooth checkout experience for your customers and operational efficiency for your business.

### Pre-purchase experience

#### **Use Case: Display Klarna Upstream on the Website Before Payment**

The Klarna integration supports configuring and displaying On-site Messaging (OSM) placements on product display pages and the cart page. This includes back-office configuration to enable default themes or customized themes set up by the merchant in the Klarna Merchant Portal. For detailed instructions, refer to the "*Klarna On-site messaging installation*" section.

### Order placement via Klarna Payments

The Klarna extension can be configured by the storefront to enable specific payment methods by Klarna market. The relevant Klarna configuration is stored by a specific payment config ID, which can be attached to the respective Base-store configuration for the relevant storefront. For detailed instructions, refer to the "*Activating Klarna Payments*" section.

#### **Use Case: Billing Address Collection from Address Forms**

The Klarna extension integration uses the standard form and extends it for data entered by the end-user during the SAP Commerce checkout process. The form data updates support both billing and shipping addresses. The address forms are customized to align with the required information for respective Klarna markets. Any person identifiable data is sent to Klarna once the customer authorizes and pays with a Klarna payment method. Additional data may be requested in a widget (Klarna modal) as part of the payment method authorization, depending on the market and Klarna product.

#### **Use Case: Update Basket**

The Klarna extension integration ensures that updates made to the cart are applied to the Klarna payment session. Updates to the cart that trigger a Klarna session update will lead to re-authorization when the customer checks out with a Klarna payment method. Any additional authorization will return an updated authorization token for the new cart amount.

#### **Use Case: Management of Klarna Decline - Recoverable**

The extension handles Klarna authorization declines gracefully. If a payment method is declined with a recoverable error, the payment methods are displayed again, and the customer is redirected to the payment method selection step. The customer has the option to update their details and re-select Klarna payment methods (e.g., Response: `show_form: false`, `approve: true`).

#### **Use Case: Order Creation**

Upon submission from the payment page, an authorization token is received from Klarna using a client-side authorization call. Using this authorization token, an order is created at Klarna by calling the create order API from SAP Commerce. The Klarna order is created just before the order creation in SAP Commerce and after authorization. Payment transaction entries are created for Klarna Authorization (`PaymentTransactionType AUTHORIZATION`) and Klarna Order Creation (`PaymentTransactionType KLARNA_ORDER_PLACED`).

#### **Use Case: Pending Orders**

The extension supports processing pending order statuses when the functionality is enabled. Pending order statuses are returned to the configured merchant notification URL, such as `FRAUD_RISK_ACCEPTED`, `FRAUD_RISK_ACCEPTED`, and `FRAUD_RISK_REJECTED`. The order fraud status is verified using the Order Management API. The order process is suspended until the application receives a pending order update from Klarna. For example, if the notification URL receives an update with the status `FRAUD_RISK_ACCEPTED`, then order processing will resume.

#### **Use Case: Confirmation Email**

The extension enables the sending of order confirmation emails with a “*Paid by Klarna*” message in the email body. Additional information regarding the Klarna App and customer support links are included for customers to find more information about the payment process and status. For more details, refer to the "*Modifying the Order Confirmation Email*" section.

### Order Management

#### **Use Case: Post Purchase Update - Shipment of Goods / “Capture” / “Card Settlement”**

The extension does not support capture, cancellation, or other post-order placement use cases out of the box. These use cases can be enabled or extended using the `klarnapaymentapi` extension, which includes support for the Klarna Payment and Order Management API. For reference, a sample capture implementation is provided as part of the accelerator fulfillment under the `TakePaymentAction`.

#### Card Settlement Using Virtual Card Number (VCN)

If standard order management is not feasible for a Klarna integration, Klarna’s merchant card service-based virtual card solution may be utilized. When an order is settled via the Virtual Card-based settlement approach, the merchant must work with their Payment Service Provider (PSP) in collaboration with the Klarna Merchant Success team to ensure proper handling of VCN-based settlement post-purchase use cases. This option can be enabled via the backoffice Klarna configuration attribute “*VCNEnabled*.” By default, this option is disabled. When a customer places an order that is created and accepted by Klarna, the add-on integration creates a virtual card-based settlement using the Merchant Card Services (MCSv3) API and creates an order in SAP Commerce. Once a settlement has been created (virtual card returned), the merchant platform can authorize the virtual card until the Klarna order is valid. Once the order has been fulfilled, the card funds should be captured. For delays in capture or other special use cases, please consult with the Klarna Key Account Manager in advance. While Klarna is the original payment method for the order, the order amount will be settled with a virtual card instead of a direct bank account transfer. A virtual card settlement request is triggered for new orders or those with a pending status resolved to `FRAUD_RISK_ACCEPTED`*.* An order placed with VCN settlement will have VCN-specific data persisted in payment info. If a Klarna order has a `fraud_status` of `PENDING`, no actions will be taken on the order until Klarna sends a push notification to update the fraud_status to `FRAUD_RISK_ACCEPTED`. Once updated, the virtual card issued for the order can only be authorized successfully once for a given merchant ID, ensuring secure transaction processing. This mechanism provides enhanced protection and compliance during order settlement.