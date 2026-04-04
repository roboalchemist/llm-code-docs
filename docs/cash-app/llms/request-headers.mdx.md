# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/introduction/request-headers.mdx

***

## stoplight-id: d7jb37p4lo5rq

# Request headers

Merchants must send appropriate headers with all requests.

## HTTP headers

| Field Name    | Requirement | Description                                                                                   |
| ------------- | ----------- | --------------------------------------------------------------------------------------------- |
| Authorization | required    | See [Authentication](/cash-app-afterpay/api-reference/reference/introduction/authentication). |
| Content-Type  | required    | All POST and PUT requests must declare the content-type as `application/json`.                |
| User-Agent    | required    | See below.                                                                                    |
| Accept        | recommended | All requests must accept `application/json` or `*/*`.                                         |

## User-Agent header

User-Agent headers are used by the Cash App Afterpay team to identify API requests. A User-Agent header must be supplied with all Merchant API requests prior to placing any live transactions.

For example: `MyAfterpayModule/1.0.0 (E-Commerce Platform Name/1.0.0; PHP/7.0.0; Merchantname/600032000) https://merchant.example.com`

| Description          | Example Data Above                                           | Other Merchant Examples                                                                           |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Afterpay Plugin      | MyAfterpayModule/1.0.0                                       | Custom Plugin/1.0<br />Shopify Plugin/3.5.1<br />AfterpayCartridge/1.0<br />AfterpayExtension/2.9 |
| Platform             | E-Commerce Platform Name/1.0.0                               | Websphere Commerce/8.1<br />Commerce Cloud/1.1<br />Adobe Commerce (Magento)/2.3.0                |
| System Information   | PHP/7.0.0                                                    | PHP/7.2.18<br /> Ruby/2.5.3<br /> Java/8.3                                                        |
| Merchant ID          | Merchantname/600032000                                       | Merchantname/101113200<br />Merchantname/101931210                                                |
| Merchant Website URL | [https://merchant.example.com](https://merchant.example.com) | [http://www.merchantwebsite.com](http://www.merchantwebsite.com)                                  |

<Note>
  In this case the Merchant ID is your company name or organisation name followed by an eight-digit number.
</Note>
