# Source: https://docs.klarna.com/payments/mobile-payments/additional-resources/flows-and-error-handling.md

# Payment Flows and Error Handling

​This page outlines the steps and flows integrators may need to understand when integrating the SDK. It will additionally provide some code snippets and try to expand on how error handling and potential custom flows may work.

## Klarna Payment View Integration

### Overview

End to end integration of the Klarna Payment View integrationconsists of 4 steps;

1.  Creating a session (Server-side)
2.  Rendering the payment view (Client-side)
3.  Authorizing the session (Client-side)
4.  Creating an order (Server-side)

### Server-side Operations

#### <span>Creating a session</span>

When the user is ready to check out, your app will want to render Klarna’s payment views. These views provide customers with information about Klarna as a payment option. Before rendering these views, your backend will need to create what we call a “Payment Session” with Klarna. This payment session contains details about your prospective order and customer. A session also contains a Client Token that identifies the session to the SDK. This step is identical to how you do it when integrating Klarna Payments on the web. You can read more about it [here](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-1-initiate-a-payment.md).

#### <span>Creating an order</span>

Once the authorization is done, you will be handed an authorization token from the SDK, with this token you backend will be able to create an order via the Klarna Payments APIs. This stage is performed in your backend. As with session creation, we offer more details about this in our documentation about Klarna Payments [here](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order.md).

##### <span>Purchase confirmation</span>

After a successful authorization and order creation, you can render your native mobile confirmation screen inside you app as desired and let the customers know that their purchase has been completed.

### Client-side Operations

The integration on client side can be broken down into roughly two parts:

- When the user enters checkout and Klarna appears as a payment option.
- When the user logs into their user account in an emerging window and selects a Klarna payment method there, Klarna needs to evaluate if the user is eligible to pay with the selected payment method.

### Init & Load Flow

When a user enters a checkout view or a view that should show Klarna as a payment option.

#### Diagram

{{#mermaid:
sequenceDiagram
    autonumber
    participant U as User
    participant M as Merchant's App
    participant SDK as In-App SDK
    U->>M: Arrives to checkout view
    M->>M: Creates payment view
    M->>SDK: Calls initialize()
    alt Fatal initialization error
        SDK->>M: Calls error callback (fatal)
        M->>M: Hides/Removes payment view
    else Non-fatal initialization error
        SDK->>M: Calls error callback (non-fatal)
        M->>M: Corrects the error. May call initialize() again
    end
    alt Successful initialization
        SDK->>M: Calls initialize callback
        M->>SDK: Calls load()
        alt Fatal load error
            SDK->>M: Calls error callback (fatal)
            M->>M: Hides/Removes payment view
        else Non-fatal load error
            SDK->>M: Calls error callback (non-fatal)
            M->>M: Corrects the error. May call initialize() again
        else Successful load
            SDK->>M: Calls load callback. Payment view is visible.
        end
    end
}}

- Common errors include using an invalid session token. \*\* Common errors include sending in invalid order information or billing information. Error callback has an error object with an invalidFields parameter.

#### Some Notes

When receiving an error message, you may check the isFatal parameter to determine whether the error is “final”, and Klarna shouldn’t be made available to customers.

### Authorization Flow

When a user confirms they want to pay with Klarna.

#### Diagram

{{#mermaid:
sequenceDiagram
autonumber
participant U as User
participant M as Merchant's App
participant SDK as In-App SDK
U->>M: Taps buy/checkout
M->>SDK: Calls Authorize()
SDK->>SDK: Renders authorization dialog (if necessary)
alt Success flow
U->>SDK: Completes authorization flow successfully
SDK->>M: Calls authorization callback with authorization token
M->>M: Submits authorization token to Klarna
end
alt Cancel flow
U->>SDK: Cancels authorization flow (taps x). Payments method is still available
SDK->>M: Calls authorization callback without authorization token
M->>M: Stays in the checkout view
end
alt Reject flow
U->>SDK: User is rejected in authorization flow. Payment method is not available.
SDK->>M: Calls error callback with show_form=false
M->>M: Hides the payment method
end
}}

#### Some Notes

Authorization is successful when:

1.  You have an authorization token *and*
2.  You have approved == true

#### Code Example



### Android


``` kotlin
    override fun onAuthorized(view: KlarnaPaymentView, approved: Boolean, authToken: String?,
       finalizedRequired: Boolean?) {
       val success = !authToken.isNullOrBlank() && approved
       if (success) {
           // User successfully completed the auth. flow.
           // Send the auth token to Klarna.
       } else {
           // User closed the payment window (tap x).
           // Merchant may keep payment view in checkout view.
       }
    }
    override fun onErrorOccurred(view: KlarnaPaymentView, error: KlarnaPaymentsSDKError) {
       if(error.name == "ShowFormFalseError"){
           // User is rejected in auth flow or payment method is not available.
           // Merchant may hide Klarna as payment option, as it's not available to the user.
       }
    }
```



### iOS


``` swift
    func klarnaAuthorized(paymentView: KlarnaPaymentView, approved: Bool, authToken: String?, finalizeRequired: Bool) {
        if let token = authToken, approved == true {
            // Authorization approved! Send token to backend and create an order.
        } else {
            // User tapped close button, or maybe merchant may need to call finalize().
        }
    }
    func klarnaFailed(inPaymentView paymentView: KlarnaPaymentView, withError error: KlarnaPaymentError) {
        if error.name == "ShowFormFalseError" {
            // Klarna has determined that the customer is not eligible for this
            // payment method.
            //
            // This is final. Merchant may hide/remove this payment view. Should
            // not call authorize() again.
        }
    }
```

## Error Handling

following errors might occur during the payment flow:

## Invalid Client Token

### Description:

This error happens when the client token used to initialize the SDK is invalid for any reason. Merchant should make sure that the client token value is not expired or tampered with.

### Report:

When this error occurs, merchant’s app will receive an error in the onErrorOccurred callback method that contains this information:

- action: Initialize
- name: InvalidClientTokenError
- message: Error performing Klarna.Payments.init().

### Handling:

Merchant can fix this error by getting a valid client token and calling the init method again. 

### Android


``` kotlin
    override fun onErrorOccurred(view: KlarnaPaymentView, error: KlarnaPaymentsSDKError) {
       if(error.name == "InvalidClientTokenError"){
           // Client token used to initialize the SDK is invalid.
           // Merchant should get a valid client token and use it to initialize the SDK again.
       }
    }
```



### iOS


``` swift
    func klarnaFailed(inPaymentView paymentView: KlarnaPaymentView, withError error: KlarnaPaymentError) {
        if error.name == "InvalidClientTokenError" {
          // Client token used to initialize the SDK is invalid.
           // Merchant should get a valid client token and use it to initialize the SDK again.
        }
    }
```

## Invalid Payment Method

### Description:

This error happens when the payment method is invalid and is not available for this session. You must ensure that the payment method is the same value as in the `payment_method_categories` parameter that is inside the response object when\[ initiating a payment\]. The most common value is `KlarnaPaymentCategory(“klarna”),`but there might be cases when you encounter one of these other values:

- `KlarnaPaymentCategory.PAY_NOW (“pay_now”)`
- `KlarnaPaymentCategory.PAY_LATER (“pay_later”)`
- `KlarnaPaymentCategory.SLICE_IT (“pay_over_time”)`

### Report:

When this error occurs, the merchant’s app will receive an error in the onErrorOccurred callback method after calling the load function. The error contains this information:

- action: Load
- name: ShowFormFalseError
- message: Error performing Klarna.Payments.load().

### Handling:

This error is fatal, meaning that the merchant cannot fix it and call the load function again. Merchant should hide the payment view, set a valid payment method and start the SDK again by calling the init function. 

### Android


``` kotlin
    override fun onErrorOccurred(view: KlarnaPaymentView, error: KlarnaPaymentsSDKError) {
       if(error.action == "Load" && error.name == "ShowFormFalseError"){
           // The selected payment method is invalid.
           // Merchant should set a valid payment method for SDK and initialize the SDK again.
       }
    }
```



### iOS


``` swift
    func klarnaFailed(inPaymentView paymentView: KlarnaPaymentView, withError error: KlarnaPaymentError) {
        if error.action == "Load" && error.name == "ShowFormFalseError" {
          // The selected payment method is invalid.
           // Merchant should set a valid payment method for SDK and initialize the SDK again.
        }
    }
```

## Invalid Card Information

### Description:

This error happens when the user sets invalid card information when authorizing the payment.

### Report:

When this error occurs, merchant’s app will receive the onAuthorized callback method with these parameters:

- approved: false
- authToken: null

### Handling:

Merchant can keep the payment view. User will see error messages on the card information field(s) and have to review the submitted information and try again. 

### Android


``` kotlin
    override fun onAuthorized(view: KlarnaPaymentView, approved: Boolean, authToken: String?,
       finalizedRequired: Boolean?
    ) {
       val success = !authToken.isNullOrBlank() && approved
       if (success) {
           // User successfully completed the auth. flow.
           // Send the auth token to Klarna.
       } else {
           // User provided invalid card information.
           // Merchant may keep the payment view in checkout view.
       }
    }
```



### iOS


``` swift
    func klarnaAuthorized(paymentView: KlarnaPaymentView, approved: Bool, authToken: String?, finalizeRequired: Bool) {
        if let token = authToken, approved == true {
            // Authorization approved! Send token to backend and create an order.
        } else {
          // User provided invalid card information.
           // Merchant may keep the payment view in checkout view.
        }
    }
```

## User Cancels The Authorization

### Description:

This error happens when the user closes the authorization window.

### Report:

When this error occurs, merchant’s app will receive the onAuthorized callback method with these parameters:

- approved: false
- authToken: null

### Handling:

Merchant keeps the payment view and the user can continue with the payment again. 

### Android


``` kotlin
    override fun onAuthorized(view: KlarnaPaymentView, approved: Boolean, authToken: String?,
       finalizedRequired: Boolean?
    ) {
       val success = !authToken.isNullOrBlank() && approved
       if (success) {
           // User successfully completed the auth. flow.
           // Send the auth token to Klarna.
       } else {
           // User closed the authorization window.
           // Merchant may keep the payment view in checkout view.
       }
    }
```



### iOS


``` swift
    func klarnaAuthorized(paymentView: KlarnaPaymentView, approved: Bool, authToken: String?, finalizeRequired: Bool) {
        if let token = authToken, approved == true {
            // Authorization approved! Send token to backend and create an order.
        } else {
            // User closed the authorization window.
           // Merchant may keep the payment view in checkout view.
        }
    }
```

## Missing or Invalid Fields in Authorize Data

### Description:

This error happens when the merchant doesn’t send some of the required billing or shipping information fields or sends invalid data when calling the authorize function on SDK.

### Report:

If this error occurs, Klarna will show an error message to the user saying that some of the information is missing and might ask for the missing information then. In this case the user can fill the information and proceed. Otherwise, the user will acknowledge the error and close the payment view. In the latter case, this error is treated exactly like the user cancel the authorization flow and the merchant’s app will receive the onAuthorized callback method with these parameters:

- approved: false
- authToken: null

### Handling:

Merchant should fix the error by sending all the required information to the authorize method and continue. 

### Android


``` kotlin
    override fun onAuthorized(view: KlarnaPaymentView, approved: Boolean, authToken: String?,
       finalizedRequired: Boolean?
    ) {
       val success = !authToken.isNullOrBlank() && approved
       if (success) {
           // User successfully completed the auth. flow.
           // Send the auth token to Klarna.
       } else {
           // Authorize information is missing some of the required fields.
           // Merchant may keep the payment view in checkout view and call the
           // authorize function with valid information.
       }
    }
```



### iOS


``` swift
    func klarnaAuthorized(paymentView: KlarnaPaymentView, approved: Bool, authToken: String?, finalizeRequired: Bool) {
        if let token = authToken, approved == true {
            // Authorization approved! Send token to backend and create an order.
        } else {
           // Authorize information is missing some of the required fields.
           // Merchant may keep the payment view in checkout view and call the
           // authorize function with valid information.
        }
    }
```

## User Getting Rejected on Authorize

### Description:

This error happens when a user gets rejected by Klarna. This error is fatal and can’t be fixed by the merchant.

### Report:

When this error occurs, merchant’s app will receive an error in the onErrorOccurred callback method containing this information:

- action: Authorize
- name: ShowFormFalseError
- message: Error performing Klarna.Payments.authorize().

### Handling:

Since this is a fatal error, merchant should remove the Klarna view and stop the payment process. 

### Android


``` kotlin
    override fun onErrorOccurred(view: KlarnaPaymentView, error: KlarnaPaymentsSDKError) {
       if(error.action == "Authorize" && error.name == "ShowFormFalseError"){
           // user is rejected when authorizing the payment.
           // Merchant should remove the Klarna view and stop the payment process.
       }
    }
```



### iOS


``` swift
    func klarnaFailed(inPaymentView paymentView: KlarnaPaymentView, withError error: KlarnaPaymentError) {
        if error.action == "Authorize" && error.name == "ShowFormFalseError" {
           // user is rejected when authorizing the payment.
           // Merchant should remove the Klarna view and stop the payment process.
        }
    }
```

## FAQ About Standalone Integration

**Q**: What is the finalizeRequired parameter in the callback? **A**: Some payment methods’ authorize() processes consist of two steps. By default, Klarna does both at once. When you call authorize() with autoFinalize = false, the aforementioned two steps are split into individual calls (authorize() and finalize()). In that case, if you receive finalizeRequired == true, you need to call finalize() to receive an authorization token. **Q**: Can I set the return URL in the application to <some extended="" path="">? **A**: Anything that triggers a return to the application to the same view works. Ideally, don’t trigger a navigation and let the SDK evaluate whether the authorization flow is complete. It’ll close any dialogs it was presenting and call either your authorized or error callbacks. **Q**: (iOS) I created a Payment View and added my event listener but nothing is happening when I call init(), etc. **A**: The Payment View contains a web view which actually shows Klarna as a payment option. On some versions of iOS, the web view needs to be added to the view hierarchy for it to function. Make sure you’ve also added the PaymentView to one of your app’s view’s before you call init().

## General Mobile SDK Errors

In the process of integrating the Mobile SDK, you may encounter various general errors, irrespective of the specific integration you are working on. To identify the error, you can refer to the **error.name** field. Below is a comprehensive list of general error names, which are predefined in the Mobile SDK's generic error class known as **KlarnaMobileSDKError**. Each error is accompanied by an explanation of its meaning and guidance on how to appropriately respond to it:

- **KlarnaMobileSDKError.SDK_NOT_AVAILABLE:** This error indicates that, for various reasons such as the specific integration, device model, or OS version, the Mobile SDK is currently unavailable. Consider this error as critical, and refrain from proceeding with the use of Klarna Mobile SDK at this point. Instead, switch to an alternative solution. If you encounter this error unexpectedly, please reach out to us for further assistance.</some>