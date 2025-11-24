# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/before-you-start/user-guide.md

# User guide for Salesforce Commerce Cloud

## Cartridge Upgrade

Regular updates to our cartridge code include bug fixes, performance enhancements, security patches, and new features. Staying up to date with these changes is essential for maintaining compatibility, security, and optimal functionality of your integration. Follow these steps to upgrade your custom code with the latest version of our cartridge: **Review Release Notes** Start by reviewing the [release notes](https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/before-you-start/changelog.md) for the latest version of the cartridge. The release notes outline changes, improvements, and any potential compatibility considerations associated with the upgrade. **Assess Custom Code Changes** Identify any customizations or modifications you have made to the SFCC cartridge code in your custom files. These may include storefront customizations, controller adjustments, or custom business logic built on top of our cartridge. **Backup Custom Files** Before proceeding with the upgrade, ensure that you have a backup of your custom files, including any modifications made to the SFCC cartridge code. This backup will serve as a safety net in case any issues arise during the upgrade process. **Compare Code Differences** Use a version control system or a file comparison tool to compare the differences between your custom code and the latest version of the SFCC cartridge code. Pay close attention to areas where changes have been made to ensure compatibility and maintain functionality. **Update Integration Code** Integrate the latest version of the SFCC cartridge code into your custom files, replacing any outdated or deprecated code with the new implementations. Follow the migration guides and best practices provided to ensure a smooth transition. **Test and Validate** After updating your custom code, thoroughly test the integration to ensure that all functionality works as expected. Test various scenarios, including user interactions, data processing, and third-party integrations, to identify any potential issues or regressions. **Address Compatibility Issues** If you encounter any compatibility issues or conflicts with your existing custom code, troubleshoot and resolve them accordingly. Consult our support resources or reach out to our team for assistance in addressing compatibility concerns. **Deploy Changes** Once you are satisfied with the upgrade and have validated its functionality, deploy the changes to your production environment. Monitor the integration closely following deployment to ensure ongoing stability and performance.

## Roles and Responsibilities

There are no recurring tasks required by the merchant. Once configurations are set up, the functionality runs on demand.

## Storefront Functionality

When Klarna is set up, Klarna Payment options and iframe widgets will be shown on the billing step. All SFCC out-of-the-box (OOTB) checkout functionality remains in place, such as:

- Cart updates during checkout
- Checkout with applied coupon(s) code(s)
- Checkout with applied product-level promotion
- Checkout with applied order-level promotion
- Checkout with applied shipping-level promotion
- Checkout with applied order-level promotion with a bonus product

To use Klarna's payment options on the billing step of the checkout process: 1. Select one of Klarna's payment options as the payment method. 2. Click the “Next: Place Order” button.


![ Payment Options on Checkout](Zwe6lIF3NbkBXKKT_sfcc-PaymentOptionsonCheckout.jpeg)
*Payment Options on Checkout*

3\. The Klarna authorization process begins and the pop up is triggered.


![The Klarna popup](Zwe6woF3NbkBXKLs_sfcc-KlarnaPopUpScreen.jpeg)
*The Klarna popup*

4\. On the Review step click on “Place Order” button.


![Place order button in SFCC](Zwfc_4F3NbkBXMVr_sfcc-PaymentReviewScreen.jpeg)
*Place order button in SFCC*

5\. The customer’s browser is sent to the `redirect_url` and immediately thereafter shown the Commerce Cloud Order Confirmation page.


![SFCC confirmation page.](ZwfdSYF3NbkBXMV6_sfcc-OrderConfirmationPage.jpeg)
*SFCC confirmation page.*

6\. The newly created order can be inspected in Business Manager.


![SFCC business manager](ZwfdeIF3NbkBXMWF_sfcc-OrdersListinBM.jpeg)
*SFCC business manager*

- The Klarna Payments order ID can be inspected in the attributes tab of the order.


![Order attributes in SFCC](Zwfd_4F3NbkBXMWf_sfcc-OrderAttributes.jpeg)
*Order attributes in SFCC*

- The payment method details can be inspected on the Payment tab of the order, and it should be `KLARNA_PAYMENTS`.


![ Order payment details](Zwfj5YF3NbkBXMmX_sfcc-OrderPaymentDetail.jpeg)
*Order payment details*

- The order can be further inspected in Klarna Merchant Portal.

## SFRA 6 users

To continue using the Klarna plugin with SFRA version 6, please update the following files and build as usual: **`package.json`**

``` json
{
  "init": [],
  "name": "klarna",
  "version": "24.4.0",
  "description": "Salesforce Commerce Cloud | Klarna Payment Integration",
  "main": "Gruntfile.js",
  "dependencies": {
    "css-loader": "^0.28.11",
    "eslint": "^3.2.2",
    "eslint-config-airbnb-base": "^5.0.1",
    "eslint-plugin-import": "^1.12.0",
    "eslint-plugin-sitegenesis": "~1.0.0",
    "node-sass": "^4.11.0",
    "postcss-loader": "^2.1.5",
    "proxyquire": "1.7.4",
    "sass-loader": "^7.1.0",
    "sgmf-scripts": "^2.3.0",
    "stylelint": "^7.1.0",
    "stylelint-config-standard": "^12.0.0",
    "stylelint-scss": "^1.3.4",
    "mocha": "^5.2.0",
    "chai": "^3.5.0",
    "chai-subset": "^1.5.0",
    "request-promise": "^4.2.2"
  },
  "scripts": {
    "test": "sgmf-scripts --test test/unit/**/*.js",
    "test:integration": "sgmf-scripts --integration 'test/integration/**/*.js'",
    "compile:scss": "sgmf-scripts --compile css",
    "compile:js": "sgmf-scripts --compile js",
    "build": "npm run compile:js && npm run compile:scss",
    "lint": "npm run lint:css && npm run lint:js",
    "lint:css": "sgmf-scripts --lint css",
    "lint:js": "sgmf-scripts --lint js",
    "upload": "sgmf-scripts --upload",
    "uploadSG": "sgmf-scripts --uploadCartridge int_klarna_payments && sgmf-scripts --uploadCartridge int_klarna_payments_controllers && sgmf-scripts --uploadCartridge int_klarna_payments_pipelines",
    "uploadSFRA": "sgmf-scripts --uploadCartridge int_klarna_payments_sfra",
    "uploadCartridge": "npm run uploadSG && npm run uploadSFRA",
    "watch": "sgmf-scripts --watch",
    "watch:static": "sgmf-scripts --watch static"
  },
  "author": "Alexander Gaydardzhiev",
  "contributors": [
    {
      "name": "Ivan Zanev",
      "email": "Ivan.Zanev@tryzens.com"
    },
    {
      "name": "Nikolay Kunev",
      "email": "Nikolay.Kynev@tryzens.com"
    },
    {
      "name": "Antonia Dimitrova",
      "email": "Antonia.Dimitrova@tryzens.com"
    },
    {
      "name": "Tihomir Ivanov",
      "email": "Tihomir.Ivanov@tryzens.com"
    },
    {
      "name": "Rumyana Topalska",
      "email": "Rumyana.Topalska@tryzens.com"
    }
  ],
  "license": "",
  "packageName": "int_klarna_payments_sfra",
  "paths": {
    "base": "../storefront-reference-architecture/cartridges/app_storefront_base/"
  }
}
```

**`webpack.config.js`**

``` javascript
/* globals cat, cd, cp, echo, exec, exit, find, ls, mkdir, rm, target, test */
'use strict';
require( 'shelljs/make' );
var path = require( 'path' );
var ExtractTextPlugin = require( 'sgmf-scripts' )['extract-text-webpack-plugin'];
var cartridgePath = './cartridges/int_klarna_payments_sfra/cartridge/';
module.exports = [{
    mode: 'production',
    name: 'js',
    entry: {
        'klarnaPayments': path.join( __dirname, cartridgePath + '/client/default/js/klarnaPayments.js' ),
        'klarnaOsm': path.join( __dirname, cartridgePath + '/client/default/js/klarnaOsm.js' ),
        'klarnaExpressButton': path.join( __dirname, cartridgePath + '/client/default/js/klarnaExpressButton.js' ),
        'klarnaMiniCart': path.join( __dirname, cartridgePath + '/client/default/js/klarnaMiniCart.js' ),
        'klarnaSubscriptions': path.join(__dirname, cartridgePath + '/client/default/js/klarnaSubscriptions.js'),
        'klarnaExpressCheckout': path.join(__dirname, cartridgePath + '/client/default/js/klarnaExpressCheckout.js'),
        'klarnaExpressMiniCart': path.join(__dirname, cartridgePath + '/client/default/js/klarnaExpressMiniCart.js'),
        'klarnaSignIn': path.join(__dirname, cartridgePath + '/client/default/js/klarnaSignIn.js')
    },
    output: {
        path: path.resolve( cartridgePath + './static/default/js/' ),
        filename: '[name].js'
    },
    optimization: {
        // We no not want to minimize our code.
        minimize: true
    }
}, {
    mode: 'production',
    name: 'scss',
    entry: {
        'klarnaPayments': path.join( __dirname, cartridgePath + '/client/default/scss/klarnaPayments.scss' ),
        'klarnaExpress': path.join( __dirname, cartridgePath + '/client/default/scss/klarnaExpress.scss' ),
        'klarnaSignIn': path.join( __dirname, cartridgePath + '/client/default/scss/klarnaSignIn.scss' )
    },
    output: {
        path: path.resolve( cartridgePath + './static/default/css/' ),
        filename: '[name].css'
    },
    module: {
        rules: [{
            test: /\.scss$/,
            use: ExtractTextPlugin.extract( {
                use: [{
                    loader: 'css-loader',
                    options: {
                        url: false,
                        minimize: true
                    }
                }, {
                    loader: 'postcss-loader',
                    options: {
                        plugins: [
                            require( 'autoprefixer' )()
                        ]
                    }
                }, {
                    loader: 'sass-loader',
                    options: {
                        includePaths: [
                            path.resolve( 'node_modules' ),
                            path.resolve( 'node_modules/flag-icon-css/sass' )
                        ]
                    }
                }]
            } )
        }]
    },
    plugins: [
        new ExtractTextPlugin( { filename: '[name].css' } )
    ]
}];
```