# Card decline errors

To understand why a card payment was declined, the Orders v2 API processor_response object includes values returned for card transactions.

The following tables list possible AVS and CVV error response decline values and descriptions.

## Error response codes

Visa, Mastercard, Discover, and American Express use the same alphabetical AVS and CVV error codes. Maestro uses numeric AVS and CVV error codes.

Choose a payment process method from the dropdown menu below:

### Visa, Mastercard, Discover, American Express

#### AVS Error

| AVS Code | Meaning | Matched details |
| --- | --- | --- |
| A | Address | Address only (no ZIP code) |
| B | International "A" | Address only (no ZIP code) |
| C | International "N" | None. The transaction is declined. |
| D | International "X" | Address and Postal Code |
| E | Not allowed for MOTO (Internet/Phone) transactions | Not applicable. The transaction is declined. |
| F | UK-specific "X" | Address and Postal Code |
| G | Global Unavailable | Not applicable |
| I | International Unavailable | Not applicable |
| M | Address | Address and Postal Code |
| N | No | None. The transaction is declined. |
| P | Postal (International "Z") | Postal Code only (no Address) |
| R | Retry | Not applicable |
| S | Service not Supported | Not applicable |
| U | Unknown - Issuer is not certified | Not applicable |
| X | No response | Not applicable |
| All others | Error | Not applicable |

### CVV Error

| CVV2 Code | Meaning | Matched details |
| --- | --- | --- |
| E | Error - Unrecognized or Unknown response | Not applicable |
| I | Invalid or Null | Not applicable |
| M | Match | or CSC |
| N | No match | None |
| P | Not processed | Not applicable |
| S | Service not supported | Not applicable |
| U | Unknown - Issuer is not certified | Not applicable |
| X | No response | Not applicable |
| All others | Error | Not applicable |

## See Also

- [Orders response object](/docs/api/orders/v2/#definition-processor_response)
- [Orders errors](/api/rest/reference/orders/v2/errors/)