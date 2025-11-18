# Source: https://docs.klarna.com/payments/after-payments/settlements/settlement-files.md

# Settlement reports

## Reconcile Klarna payments easily with detailed Settlement Reports available in CSV, PDF, or JSON formats via the Merchant Portal, Settlements API, or Klarna-SFTP.

Settlement Reports explain in detail all payments made by Klarna to you and help you to reconcile your accounts. Each Settlement Report can be linked to a payout by using the unique payment reference, which appears on your bank account statement. Settlement Reports are available in CSV, PDF or JSON format and can be accessed in three different ways - using Klarna’s Merchant Portal, using the Settlements API or by using the [Klarna-SFTP](https://docs.klarna.com/payments/after-payments/settlements/additional-resources/how-to-get-settlement-reports-via-sftp/).

## Merchant Portal

Using the Merchant Portal to access your Settlement Reports is the simplest method of managing them, as no technical setup or configuration is needed. The Merchant Portal allows for filtering by dates and currency and simple downloads of Settlement Reports for desired transactions. For each payout, a settlement report is created and shown in the table at the bottom. You'll find the options to download the CSV and PDF report from the table or to click on the payment reference for the transactional details.


![klarna docs image](29e3d23c-df8b-4f06-9e9e-ecf6429b4aa8_FIRE-settlements-app-overview.jpeg)image

## CSV settlement report

{{CardList|
id=Resend_Email_API_Technical_Documentation
|cardListType=downloadable_assets
|showAssetsGroupedHorizontally=false
|bannerBackgroundColor=white
|cards=
{{Card
|image=CSV settlement report example1.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=20496
}}
{{Card
|image=CSV settlement report example2.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=12311
}}
{{Card
|image=CSV settlement report example3.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=8968617
}}
{{Card
|image=CSV settlement report example4.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=2072133
}}
{{Card
|image=CSV settlement report example5.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=1308
}}
{{Card
|image=CSV settlement report example6.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=10892
}}
{{Card
|image=CSV settlement report example7.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=48577
}}
{{Card
|image=CSV settlement report example8.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=6831
}}
{{Card
|image=CSV settlement report example9.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=20738
}}
{{Card
|image=CSV settlement report example10.csv
|downloadBehaviour=OpenNewWindow
|contentType=CSV settlement report example
|assetSize=815943
}}
}}

## Settlements API

The Settlements API allows for managing and gathering Settlement Reports using our predefined API. It requires technical configuration but is a preferred method to manage larger volumes of Settlement Reports. Click [here](https://docs.klarna.com/api/settlements/) for detailed information about the Settlements API.


![ Available endpoints for the Settlements API](b20b8140-ea4e-4b0a-a812-dfb459aa332d_FIRE-settlements_api_overview.jpeg)
*Available endpoints for the Settlements API*

## Fields description

### Calculation of settlement amount

| Total amount | Transaction Type |
|----|----|
| \+ total_sale_amount | \+ sale |
| − total_return_amount | − return |
| − total_reversal_amount | − reversal + reversal_merchant_protection |
| − total_fee_amount | − fee |
| \+ total_fee_correction_amount | N/A |
| \+ total_commission_amount | \+ commission |
| \- total_tax_amount |  Not available as a separate transaction type. However, the amount can be included as a separate column “vat_amount” with the Report Configurator |
| − total_charge_amount | − charge |
| \+ total_credit_amount | \+ credit |
| − total_repay_amount | N/A |
| − total_holdback_amount | − holdback |
| \+ total_release_amount | \+ release |
| \+ total_fee_refund_amount | \+ fee_refund |

## total_settlement_amount

### Summary section fields

| Field | Type | Description |
|----|----|----|
| total_sale_amount | Decimal | Total of all “sale” events. These are all captured orders that have been shipped to the customers. |
| total_fee_amount | Decimal | Total of all “fee” events. These are service fees charged by Klarna for the related sale transactions. |
| total_fee_correction_amount | String | Total of refunded fees in a given settlement or period. |
| total_tax_amount | Decimal | Total tax (VAT, GST) amount on Klarna fees. Reflects the total of all vat_amount values per transaction, which are described further down |
| total_return_amount | Decimal | Total of all “return” events. These are refund transaction, registered by the merchant and indicating that the goods/services have been returned by the customer. |
| total_reversal_amount | Decimal | Total of all “reversal” events. These are refund transactions, registered by Klarna in disputed orders in favour of the customer. This contains fraudulent cases seen as merchant loss eg. due to missing tracking data. |
| total_commission_amount | Decimal | Total of all “commission” events. These are paid by Klarna to the merchant based on the contractual agreement regarding commissions. |
| total_credit_amount | Decimal | Total of all “credit” transactions. |
| total_charge_amount | Decimal | Total of all “charge” transactions. |
| total_holdback_amount | Decimal | The amount is used as a (rolling) reserve, which covers for future refunds or other security reasons. |
| total_release_amount | Decimal | The amount reduces the rolling reserve (the opposite of a holdback). The credit that Klarna had set apart for a merchant, gets released and paid back to the merchant. |
| opening_debt_balance | Decimal | Your negative balance with Klarna from previous settlements, if your returns, fees, and other charges exceeded your sales. This amount equals the closing_debt_balance of your last settlement unless Klarna has invoiced you separately for the amount. |
| total_deposit_amount | Decimal | Increase of your debt balance with Klarna if your returns, fees, and other charges exceed your sales within this settlement period. This debt will be deducted from your next settlements as a total_repayment_amount. This field deposit amount describes the amount that is increasing your debt balance, to be seen in the closing_debt_balance. For the calculation refer to the chapter "Calculation of settlement amount". |
| total_repay_amount | Decimal | Assuming you have an opening_debt_balance with Klarna because your previous settlement was negative, this amount states the reduction of your debt balance, to be seen in a lower closing_debt_balance. The amount is simply deducted from your current settlement and you don't need to do anything further. |
| closing_debt_balance | Decimal | Your debt balance after the settlement. This amount will be the opening debt balance of your next settlement and helps you understand which amounts will be deducted from your next settlements. The amount is calculated as: opening_debt_balance - total_repay_amount + total_deposit_amount |
| total_fee_refund_amount | Decimal | Credit entries in the settlement report where Klarna has identified that the fee was incorrectly charged. |
| total_settlement_amount | Decimal | Total amount of this payout (sales + release - fees - tax - returns - holdback - reversals - repay = total_settlement_amount) |
| payment_reference | String | Unique identifier of this payout, which is stated in the transfer note in your bank statement |
| settlement_currency | ISO 4217 | Settlement Currency. We settle you like for like in your transacting currency. Example **EUR, USD, GBP** |
| payout_date | ISO 8601 | Indicates when Klarna initiated the payout (Coordinated Universal Time, UTC). Please note that it usually takes one banking day until the funds are credited to your bank account. Example:**2018-08-10T07:45:00Z** |
| merchant_id | String | Unique Merchant Identification Number Example:**"K123456"** |
| merchant_settlement_type | String | Settlement type: **NET** Klarna service fees are deducted from the payout. **GROSS** Klarna service fees are invoiced separately. **GROSS_FEE** Invoice for Klarna service fees. |
| submerchant_id | String | unique identifier for a sub merchant |

### Transaction fields

| Field | Type | Description |
|----|----|----|
| type | String | Type of this event: **SALE** (+) captured order that has been shipped to the customer. **FEE** (-) Service fee charged by Klarna for the related sale transaction. Please note that according to your contract multiple fee transactions can be applied to one sale transaction, eg. fixed fees and percentage fees. **RETURN** (-) refund transaction, registered by the merchant and indicating that the goods/services have been returned by the customer. **REVERSAL** (-) refund transaction, registered by Klarna in disputed orders in favour of the customer. This contains fraudulent cases seen as merchant loss eg. due to missing tracking data. **REVERSAL_MERCHANT_PROTECTION** (+) net-amount of the order value (without tax), credited by Klarna to the merchant due to Klarna’s merchant protection eg. in case of fraud. The amount is reducing the total_reversal_amount. **COMMISSION** (+) Paid by Klarna to the merchant based on the contractual agreement regarding commissions. **CORRECTION** (+/-) Certain corrections that are booked against specific orders according to a mutual agreement between the merchant and Klarna. **HOLDBACK** (-) The amount is used as a rolling reserve, which covers for future refunds or other security reasons. **RELEASE** (+) The amount reduces the rolling reserve (the opposite of a holdback). The credit that Klarna had set apart for a merchant, gets released and paid back to the merchant. **CREDIT** (+) Miscellaneous credit towards you, which is described in the field detailed_type. **CHARGE** (-) Miscellaneous charge towards you, which is described in the field detailed_type. **FEE_REFUND** (+) Credit entries in the settlement report where Klarna has identified that the fee was incorrectly charged. |
| capture_date | ISO 8601 | Date when the event was registered in Klarna’s system (Coordinated Universal Time, UTC). In case of a SALE transaction it refers to the moment when you shipped the goods to the customer and captured/activated the order. Example:**2018-08-10T07:45:00Z** |
| sale_date | ISO 8601 | Date of the order creation (Coordinated Universal Time, UTC). Example:**2018-08-10T07:45:00Z** |
| order_id | UUID | Unique identifier of the order. All related transactions in the life-span of an order are associated with this ID. eg. fees or refunds. It is therefore the recommended identifier for reconciling the report lines with your system. Example: **c504a9bb-1948-46d5** |
| short_order_id | String | Customer-facing order ID. Example:**9875QW2** |
| capture_id | String | Each capture on an order is assigned a unique identifier, referred to as the **capture_ID**, which is provided exclusively for sale and fee transactions. In instances of partial shipments, an order may undergo multiple captures, each of which is reflected as a separate sale transaction with its own unique **capture_id**. It's important to note that for certain transaction types such as RETURNS and REVERSALS, where captures do not exist, the API will return empty strings for the **capture_id** field. Example:**8e93b66-6ab1-4d3d-b60d-1cc4e24f4a99** |
| merchant_reference1 | String | Your internal reference to the order, that has been submitted during order creation. |
| merchant_reference2 | String | Your internal reference to the order, that has been submitted during order creation. |
| amount | Decimal | Amount of the related transaction. Example:**100.00** |
| posting_currency | ISO 4217 | Currency in which the order has been placed. The following currencies are currently available:**DKK, EUR, GBP, NOK, SEK, USD, CHF, CAD, AUD** |
| refund_id | String | Unique identifier for Return and Reversal transactions. In case of partial returns, each return transaction is associated with a unique refund_ID.*Note*: By default, these are not included in the reports on SFTP. They can be included by using the Report Configurator. Example:**8e93b66-6ab1-4d3d-b60d-1cc4e24f4a99** |
| purchase_country | ISO 3166-alpha-2 | Purchase country, as provided by the merchant.*Note*: By default, these are not included in the reports on SFTP. They can be included by using the Report Configurator. Example:**US, GB, DE, SE** |
| tax_rate | Decimal | VAT (Value added tax in Europe) or GST (goods and services tax in Australia) rate on Klarna fees. |
| tax_amount | Decimal | VAT (Value added tax in Europe) or GST (goods and services tax in Australia) amount on Klarna fees. |
| shipping_country | ISO 3166-alpha-2 | As provided by you. |
| initial_payment_method_type | String | Payment method the consumer chose during checkout. |
| initial_number_of_installments | Decimal | Number of installments the consumer chose during checkout in case of installment payments. |
| initial_payment_method_monthly_downpayments | Decimal | Number of monthly downpayments that were chosen during the checkout in case of installment payments. |
| merchant_capture_reference | String | Your internal reference to the capture, that has been submitted during capturing an order via API. |
| merchant_refund_reference | String | Your internal reference to the refund, that has been submitted during refunding an order via API. |
| detailed_type | String | Detailed description of the transaction type. See section “Detailed type” for further information. |
| tax_rate_1-4 | String | Consumer VAT (value added tax) rates on your products/services. The rate needs to be submitted by you for every order-line when capturing or refunding an order, because an order can consist of items with different VAT rates |
| tax_amount_1-4 | Decimal | Consumer VAT (value added tax) amounts on your products/services. The amount needs to be submitted by you for every order-line when capturing or refunding an order, because an order can consist of items with different VAT rates. |
| reversal_reference | String | Unique internal identifier, known as DisputeKRN, assigned to each dispute by Klarna. This identifier includes a dispute category and a numeric code, enabling efficient tracking and management of the dispute's status. |

### Detailed Type

| Transaction type | Detailed type | Description |
|----|----|----|
| CHARGE | CASH_ADVANCE_AMORTISATION | Merchant Lending loan amortisation |
| CHARGE | TRANSFER_FROM_LEGACY_INTEGRATION | Transfer of debt from the legacy KPM integration towards a KP integration. This mechanism is used instead of issuing an invoice. |
| CHARGE | LIABILITY_TRANSFER | Represents the movement of financial obligations (liabilities) from one entity to another, i.e. reassigns the responsibility for the debt or obligation from the original holder to a new party. For instance, liabilities can be moved between different MIDs belonging to the same organisation. |
| CHARGE | PAYMENT_REMINDER | Represents the amount of outstanding debt owed by the merchant, created when the merchant’s balance remains negative for a consecutive period. |
| COMMISSION | COMMISSION | Commission |
| COMMISSION | PURCHASE_COMMISSION_PERCENTAGE | Percentage Commission Paid by Klarna to the merchant based on the contractual agreement regarding percentage commissions |
| CORRECTION | CREDITED_CORRECTION | Manual corrections |
| CREDIT | CASH_ADVANCE_FEES | Merchant Lending fees charges |
| CREDIT | CASH_ADVANCE_PAYOUT | Merchant Lending loan payout |
| CREDIT | CORRECTION_DISPUTE | Credit entries in the settlement report where Klarna has identified that the customer refund was incorrectly charged. |
| FEE | EXPIRY_FEE_GROSS | Fee for extending the due date for a consumer invoice. |
| FEE | LATE_RETURN_FEE | Added when an order is returned by the consumer after a reminder is sent. |
| FEE | PURCHASE_FEE_FIXED | Fixed Fee on captured order |
| FEE | PURCHASE_FEE_PERCENTAGE | Percentage Fee on captured order |
| FEE | SERVICING_FEE | Fee on captured order if a consumer pays with Klarna account. |
| FEE | EXTEND_DUE_DATE_FEE | Fee for extending the due date for a consumer invoice |
| FEE | DISPUTE_FEE | Dispute fee on a captured order |
| FEE_REFUND | DISPUTE_FEE_REFUND | Fee refund on disputes in favour of the merchant |
| FEE_REFUND | PURCHASE_FEE_FIXED | A refund issued for a previously charged purchase fee. This action is performed manually as part of a fee correction process in the event of an error or other issue. |
| FEE_REFUND | PURCHASE_FEE_PERCENTAGE_REFUND | A refund for the percentage component of a previously applied purchase fee. This action is performed manually as part of a fee correction process in the event of an error or other issue. |
| HOLDBACK/RELEASE | INSUFFICIENT_BANK_ACCOUNT_DETAILS | A holdback for the sum amount that would have been released if correct bank details were present. These can be updated in Merchant portal under settings\> Bank account details. Once updated the withheld amount(s) will be paid out together either in a new settlement the following business day if you are settled weekly, or in your next settlement if you are settled daily. |
| HOLDBACK/RELEASE | ROLLING_RESERVE | Security measure that works well for both you as a merchant and Klarna since we do not hold funds or delay payment of funds, but rather hold only a portion of it as collateral, which will automatically be released after the time agreed upon. |
| HOLDBACK/RELEASE | UNDER_REVIEW | Security measure that will allow Klarna to place a hold on payouts either in part of full while we review the financial holding of a merchant and the underlying transactions |
| RETURN | PURCHASE_RETURN | Refund, registered by the merchant and indicating that the goods/services have been returned by the customer. |
| RETURN | PAYMENT_DEFAULT | Refund registered by Klarna and indicating the customer fails to pay. This is to distinguish this refund from others. |
| REVERSAL | COMMISSION_RETURN | Return of commission |
| REVERSAL | REVERSAL | Refund, registered by Klarna on disputed orders in favour of the customer. This contains fraudulent cases seen as merchant loss eg. due to missing tracking data. |
| REVERSAL | FRAUD_POLICY_CHARGE | Gross amount of the order value (incl. consumer VAT), debited by Klarna due to Klarna’s merchant protection. The net order value (excl. consumer VAT) is credited in the same settlement with the detailed type FRAUD_POLICY_CREDIT_NET. |
| REVERSAL_MERCHANT_PROTECTION | FRAUD_POLICY_CREDIT_NET | Net-amount of the order value (incl. consumer VAT), credited by Klarna to the merchant due to Klarna’s merchant protection eg. in case of fraud. The amount is reducing the total_reversal_amount. |
| SALE | PURCHASE | Captured order |