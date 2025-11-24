# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/customization.md

# Customization

When creating an HPP Session you have some optional parameters that will let you modify the look and feel of Klarna’s Hosted Payment Page in order to better match your own branding.

## Overview

### Standard version


![klarna docs image](30d325c0-7bcc-4b5d-a601-61f04acba131_HPP_desktop_no_custom.jpeg)image

![klarna docs image](6a7717be-29a8-4a3a-b3ad-c812285cb013_HPP_mobile_no_custom.jpeg)image

### Customized


![klarna docs image](647d82c9-3596-463a-b60d-48de620c585e_HPP_desktop_custom.jpeg)image

![klarna docs image](d7eba885-4658-4728-9898-0acabf1a1fdb_HPP_mobile_custom.jpeg)image

## Generic confirmation pages

When creating an HPP Session you can define the URL that you want the Consumer to be redirected to after making an action on the payment page. These URLs are in the merchant_urls block, but they are also optional. When you don’t put any value in there, generic pages are displayed to the Consumer.

### Success


![klarna docs image](063f9280-e7fd-4b88-b188-4548e75fe120_HPP_pages_payment.jpeg)image

Failure


![klarna docs image](94877411-a8df-4377-9f93-6871e2193208_HPP_pages_failure.jpeg)image

Cancellation


![klarna docs image](18dcc8bf-1bb7-4005-8a2d-bbc363002b65_HPP_pages_cancellation.jpeg)image

## Parameters

A description of the options that can be passed to HPP. All of these are optional, some default to a sensible value if omitted in the call.


![klarna docs image](34fcc3f0-f511-47b1-bd44-d4c369908f03_HPP_customization.jpeg)image

## Logo and Feature image

When provided your logo and feature image will appear on the Hosted Payment Page, their positions will depend on the Consumer’s browser capacities as HPP as different responsive designs. Both can be configured through the merchant portal. Merchants can try their setup in playground as well as production environment. It may take sometime for the changes to reflect on HPP. Logo configuration is documented at Merchant Branding Configuration Page

### Background Images

Use this parameter to send a list of images to use as backgrounds on the payment page. HPP will use the image that fits the better to the Consumer’s browser capacities using the width parameter given. Images have to be served over HTTPS to avoid all kind of security warning on the Consumer’s browser.

| Key         | background_images                                     |
|-------------|-------------------------------------------------------|
| Description | A list of images to be used as the background for HPP |
| Type        | Array                                                 |
| Default     | none                                                  |

| **Parameter** | Type   | Usage                                       |
|---------------|--------|---------------------------------------------|
| url           | String | Url of the image, must be served over HTTPS |
| width         | Int    | Width of the screen the image works best on |

### Example Code: Background Images

``` json
{
    "options": {
        "background_images": [
            {
                "url": "https://example.com/background.jpg",
                "width": 1280
            },
            {
                "url": "https://example.com/background_small.jpg",
                "width": 480
            }
        ]
    }
}
```

### Page Title

Use this parameter to modify the title of the Hosted Payment Page. This title is shown in the page and as header of the Consumer’s browser. As it is defined by you, you are responsible of its localization to the Locale of the Consumer.

| **Key**     | **page_title**                          |
|-------------|-----------------------------------------|
| Description | Title on top of the Hosted Payment Page |
| Type        | String                                  |
| Default     | Complete your purchase                  |

### Example Code: Page

``` json
{
    "options": {
        "page_title": "Complete your purchase"
    }
}
```

### Complete purchase button labeling

Depending on the kind of goods you are selling, use this parameter to change the label of the button on which the Consumer will click to finalize the purchase. Label is localized in the locale of the Session.

| **Key** | **purchase_type** |
|----|----|
| Description | Purchase type, reflected in the complete purchase button on the bottom of HPP |
| Type | Enum |
| Accepted values | BOOK,BUY,CONTINUE,DOWNLOAD,ORDER,RENT,SUBSCRIBE,PAY |
| Default | BUY |

| Value     | Button label in English |
|-----------|-------------------------|
| BOOK      | Book                    |
| BUY       | Buy                     |
| CONTINUE  | Continue                |
| DOWNLOAD  | Download                |
| ORDER     | Order                   |
| RENT      | Rent                    |
| SUBSCRIBE | Subscribe               |
| PAY       | Pay                     |

### Example Code: Purchase type

``` json
{
    "options": {
        "purchase_type": "buy"
    }
}
```

### Back Button Labeling

Use this parameter to enable the user to go back to purchase page while providing the flexibility to you to end or keep alive the purchase session. When provided, a “Go Back” button will be displayed on the page instead of a “Cancel” button and the consumer will get redirected to this url on clicking on the go back button. See back button versus cancel button chapter for more information.

| Key | back |
|----|----|
| Description | Redirection url on back button click |
| Type | String |
| Default | There is no back button by default. If this parameter is not provided, a cancel button will be displayed. |

### Example Code: Back URL

``` json
{
    "merchant_urls": {
        "back": "https://example.com/back?token=<random_uuid>&sid={{session_id}}"
    }
}
```

### Styling of payment methods

Documented in the KP docs</random_uuid>