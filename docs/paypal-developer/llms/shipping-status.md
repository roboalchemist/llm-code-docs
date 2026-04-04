# Add Tracking API Shipping Statuses

When a merchant adds a tracking number, the Add Tracking API expects one of the following shipping statuses.

**Note:** A merchant is not required to update the shipping status each time the shipment status changes. Update the status only once when you update the tracking number.

| Status | Description | Use status when |
| --- | --- | --- |
| **SHIPPED** | The item was shipped and is on the way. | The recommended status. |
| **ON_HOLD** | The item is on hold. | The item might be held up in customs or is on hold for another reason. |
| **DELIVERED** | When the tracking number was uploaded, the item had already been delivered. |  |
| **CANCELLED** | The shipment was cancelled and the tracking number no longer applies. | The user wants to indicate that a tracking number is no longer valid. |

---

If you accept cookies, we’ll use them to improve and customize your experience and enable our partners to show you personalized PayPal ads when you visit other sites. [Manage cookies and learn more](https://www.paypal.com/myaccount/privacy/cookiePrefs?locale=en_US)