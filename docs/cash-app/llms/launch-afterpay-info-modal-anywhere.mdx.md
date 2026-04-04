# Source: https://developers.cash.app/cash-app-afterpay/guides/afterpay-messaging/launch-afterpay-info-modal-anywhere.mdx

***

## stoplight-id: 0e2vphqvolz9i

# Launch Cash App Afterpay Info Modal Anywhere

This page is a short guide on how to use JavaScript to enable any element to open the Cash App Afterpay information modal.

For the customer, it should be a single click operation; click on any element and the Cash App Afterpay information modal opens.

## Instructions

Do the following:

1. Open your existing messaging script with an HTML editor.

2. Load `square-marketplace.js` script in the HTML, see the example below:

   ```html
   <script src="https://js.squarecdn.com/square-marketplace.js" async></script>
   ```

3. Add `data-afterpay-modal` attribute to any element. When a customer clicks that element, it now opens the Cash App Afterpay information modal. Here's an example code snippet that opens when a customer clicks the icon symbol:

   ```html
   <div>
     Or 4 interest-free payments with 
     <strong>[Cash App Afterpay Logo] <span data-afterpay-modal>ⓘ</span></strong>
   </div>
   ```

### Regional Modal Themes

| Region        | Accepted Values                |
| ------------- | ------------------------------ |
| United States | "en\_US", "en\_US-theme-white" |

For example:

`<strong>[Cash App Afterpay Logo] <span data-afterpay-modal="en_US">ⓘ</span></strong>`

Results in a modal suitable for US merchants.
