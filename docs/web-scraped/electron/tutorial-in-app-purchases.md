# Source: https://www.electronjs.org/docs/latest/tutorial/in-app-purchases

On this page

# In-App Purchases

## Preparing[â€‹](#preparing "Direct link to Preparing") 

### Paid Applications Agreement[â€‹](#paid-applications-agreement "Direct link to Paid Applications Agreement") 

If you haven\'t already, youâ€™ll need to sign the Paid Applications Agreement and set up your banking and tax information in iTunes Connect.

[iTunes Connect Developer Help: Agreements, tax, and banking overview](https://help.apple.com/itunes-connect/developer/#/devb6df5ee51)

### Create Your In-App Purchases[â€‹](#create-your-in-app-purchases "Direct link to Create Your In-App Purchases") 

Then, you\'ll need to configure your in-app purchases in iTunes Connect, and include details such as name, pricing, and description that highlights the features and functionality of your in-app purchase.

[iTunes Connect Developer Help: Create an in-app purchase](https://help.apple.com/itunes-connect/developer/#/devae49fb316)

### Change the CFBundleIdentifier[â€‹](#change-the-cfbundleidentifier "Direct link to Change the CFBundleIdentifier") 

To test In-App Purchase in development with Electron you\'ll have to change the `CFBundleIdentifier` in `node_modules/electron/dist/Electron.app/Contents/Info.plist`. You have to replace `com.github.electron` by the bundle identifier of the application you created with iTunes Connect.

``` 
<key>CFBundleIdentifier</key>
<string>com.example.app</string>
```

## Code example[â€‹](#code-example "Direct link to Code example") 

Here is an example that shows how to use In-App Purchases in Electron. You\'ll have to replace the product ids by the identifiers of the products created with iTunes Connect (the identifier of `com.example.app.product1` is `product1`). Note that you have to listen to the `transactions-updated` event as soon as possible in your app.

``` 
// Main process
const  = require('electron')

const PRODUCT_IDS = ['id1', 'id2']

// Listen for transactions as soon as possible.
inAppPurchase.on('transactions-updated', (event, transactions) => 

  // Check each transaction.
  for (const transaction of transactions) ...`)
        break

      case 'purchased':  purchased.`)

        // Get the receipt url.
        const receiptURL = inAppPurchase.getReceiptURL()

        console.log(`Receipt URL: $`)

        // Submit the receipt file to the server and check if it is valid.
        // @see https://developer.apple.com/library/content/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateRemotely.html
        // ...
        // If the receipt is valid, the product is purchased
        // ...

        // Finish the transaction.
        inAppPurchase.finishTransactionByDate(transaction.transactionDate)

        break
      }

      case 'failed':

        console.log(`Failed to purchase $.`)

        // Finish the transaction.
        inAppPurchase.finishTransactionByDate(transaction.transactionDate)

        break
      case 'restored':

        console.log(`The purchase of $ has been restored.`)

        break
      case 'deferred':

        console.log(`The purchase of $ has been deferred.`)

        break
      default:
        break
    }
  }
})

// Check if the user is allowed to make in-app purchase.
if (!inAppPurchase.canMakePayments()) 

// Retrieve and display the product descriptions.
inAppPurchase.getProducts(PRODUCT_IDS).then(products => 

  // Display the name and price of each product.
  for (const product of products)  is $.`)
  }

  // Ask the user which product they want to purchase.
  const selectedProduct = products[0]
  const selectedQuantity = 1

  // Purchase the selected product.
  inAppPurchase.purchaseProduct(selectedProduct.productIdentifier, selectedQuantity).then(isProductValid => 

    console.log('The payment has been added to the payment queue.')
  })
})
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/in-app-purchases.md)