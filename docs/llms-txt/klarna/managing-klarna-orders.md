# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/vtex/payments/managing-klarna-orders.md

# Managing Klarna orders with Vtex

## This section explains how to capture payments, process refunds, cancel transactions, and release uncaptured amounts for Klarna orders through the VTEX back office.

## Available order management actions

Once Klarna has authorized a payment, you can manage the order through VTEX. The following actions are supported:

- **Capture:**
  - Finalizes the payment and charges the customer.
  - The Klarna app for VTEX only supports **full capture** or **one partial capture**, multiple partial captures are not currently supported.
- **Refund:**
  - Issues a refund for an order.
  - VTEX **only refunds the value of the products**. To refund tax, shipping, or additional charges, these must be specified as an additional amount in the refund request.
- **Cancel:**
  - Cancels an order before it is captured.
  - If an order is authorized but not yet captured, cancellation releases the authorized funds back to the customer.
- **Release uncaptured amount:**
  - If an order is modified (lower amount than the amount authorized) **before capture**, the Klarna Payments App automatically adjusts the captured amount to the new order total and releases any uncaptured funds.

## Klarna and VTEX order status mapping

VTEX order actions trigger specific status updates in Klarna. The table below outlines how these actions map between VTEX and Klarna:

| **Order action on VTEX** | **What happens on Klarna** |
|----|----|
| Return/Refund | Klarna refunds the order. |
| Invoice/Capture | Klarna captures the full amount specified by VTEX. If less than the authorized amount, Klarna releases the remaining funds automatically. |
| Cancel | Klarna cancels the order. |
| Partially Captured | Klarna refunds the reminder of the order. |
| Expired | No action is possible. |
| Closed | No action is possible. |