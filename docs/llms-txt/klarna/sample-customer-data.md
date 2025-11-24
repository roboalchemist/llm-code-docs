# Source: https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data.md

# Sample customer data

## This page contains sample data you can use for testing your integration in the Klarna playground environment.

Use the sample customer data in this page to test the standard approved and denied payment flows in Klarna payments.

If you want to test non-standard flows, such as pending payments or presenting only pre-paid payment options, see the Other test scenarios section in this page.

If you want to test different payment methods, direct debit, credit card, and bank transfer, use the [data in our sample data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data/).

### About user account

To make a purchase new users in most countries go through an account creation wizard, provide their personal data, and enter a verification code to create their Klarna user account.

To test a new Klarna user account, select a combination of a random phone number and an email matching the required pattern. If the combination was used during sign-up before, you'll be logged into an existing account after providing a one-time password (OTP). In the playground environment, you can use any valid 6-digit number other than *999999* as the OTP.

One user account is only valid in a single market. For example, you can't use the same email address or phone number to test purchases in a playground store in Germany and Sweden.

User account is available in all countries included in the sample customer data list, except for Switzerland and Finland.

If you choose to create a new account rather than using one of the provided sample customer accounts on this page, any Personally Identifiable Information (PII) will be substituted with synthetically generated data. Consequently, you may notice different account values from those you provided. This helps us prevent data leaks in our playground environment.

### Sample customer data

Use the sample data for private persons to test B2C transactions. The company test data can be used for testing B2B transactions.

If you're testing a B2B transaction with Billie, please refer to [Billie’s sample data](https://docs.billie.io/docs/international-test-buyer-accounts) for guidance.

The B2C sample data in this article s split into two sub-categories:

- Standard flows shows the data for testing standard responses approved and denied transactions.
- Custom flows shows the data for testing flows other than the standard approved and denied transactions, for example, launching a dispute.

Below is a list of email addresses associated with standard and custom test flows. When testing, replace the final two asterisks with a 2-letter country code of a Klarna market. For example, to test an approved transaction flow for Sweden, use *customer@email.se*.

#### Standard flows

| Email address pattern | Description |
|----|----|
| customer@email.\*\* | Accept purchase. **Message:**"None, auth_token (valid 60 minutes) is returned for use in create_order" |
| customer+denied@email.\*\* | Hard decline. **Message:**"Your purchase can not be accepted Unfortunately your purchase can not be accepted at this moment. Please choose a different payment method to complete your purchase." |

#### Custom flows

| Email address pattern | Description |
|----|----|
| customer+new_user@email.\*\* | New user sign up flow. Payment method specific details (e.g. cards) are stored to the user. |
| customer+disputed-return@email.\*\* | Creates a dispute on each capture of the order with the reason return and one open dispute request |
| customer+disputed-goods_not_received@email.\*\* | Creates a dispute on each capture of the order with the reason goods not received and one open dispute request |
| customer+disputed-already_paid@email.\*\* | Creates a dispute on each capture of the order with the reason already paid and one open dispute request |
| customer+disputed-faulty_goods@email.\*\* | Creates a dispute on each capture of the order with the reason faulty goods and one open dispute request |
| customer+disputed-incorrect_invoice@email.\*\* | Creates a dispute on each capture of the order with the reason incorrect invoice and one open dispute request |
| customer+disputed-high_risk_order@email.\*\* | Creates a high-risk order (formerly known as stop request) on order level. |
| customer+disputed-non_compliance@email.\*\* | Creates a non compliance type of dispute. |
| customer+disputed-non_guaranteed_payment_program@email.\*\* | Creates a non guaranteed payment program type of dispute |
| customer+disputed-unauthorized_purchase@email.\*\* | Creates a dispute on each capture of the order with the reason unauthorized_purchase and one open dispute request |
| customer+disputed-return_not_possible@email.\*\* | Creates a return not possible type of dispute |

As we're constantly improving the testing experience, you may not able to test the denied payment flow in some markets, for example, Sweden and Norway. Please contact Klarna merchant support for more information.

## All Countries

Select a country to view the sample data you can use to test Klarna.

|  |  |  |  |
|----|----|----|----|
| **[Australia 🇦🇺](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#asia-and-oceania-australia)** | **[Austria 🇦🇹](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-austria)** | **[Belgium 🇧🇪](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-belgium)** | **[Canada 🇨🇦](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#americas-canada)** |
| **[Czech Republic 🇨🇿](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-czech-republic)** | **[Denmark 🇩🇰](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-denmark)** | **[Finland 🇫🇮](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-finland)** | **[France 🇫🇷](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-france)** |
| **[Germany 🇩🇪](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-germany)** | **[Greece 🇬🇷](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-greece)** | **[Hungary 🇭🇺](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-hungary)** | **[Ireland 🇮🇪](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-ireland)** |
| **[Italy 🇮🇹](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-italy)** | **[Mexico 🇲🇽](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#americas-mexico)** | **[Netherlands 🇳🇱](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-netherlands)** | **[New Zealand 🇳🇿](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#asia-and-oceania-new-zealand)** |
| **[Norway 🇳🇴](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-norway)** | **[Poland 🇵🇱](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-poland)** | **[Portugal 🇵🇹](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-portugal)** | **[Romania 🇷🇴](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-romania)** |
| **[Slovakia 🇸🇰](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-slovakia)** | **[Spain 🇪🇸](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-spain)** | **[Sweden 🇸🇪](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-sweden)** | **[Switzerland🇨🇭](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-switzerland)** |
| **[United Kingdom 🇬🇧](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#europe-united-kingdom)** | **[United States of America 🇺🇸](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/#americas-united-states-of-america)** |  |  |

## Europe

### Austria

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.at | +4306762600456 |
| Denied | customer+denied@email.at | +4306762600745 |
| New user sign up | customer+new_user@email.at | +4306762600721 |
| Dispute: return | customer+disputed-return@email.at | +4306762600762 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.at | +4306762600763 |
| Dispute: order already paid | customer+disputed-already_paid@email.at | +4306762600764 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.at | +4306762600765 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.at | +4306762600766 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.at | +4306762600767 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.at | +4306762600768 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.at | +4306762600770 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.at | +4306762600771 |
| Dispute: return not possible | customer+return_not_possible@email.at | +4306762600771 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person AT |
| Last name | Person-at | Person-at | Test |
| Address | Mariahilfer Straße 47 | Mariahilfer Straße 47 | E Opernring 2 |
| Zip code | 1060 | 1060 | 1010 |
| City | Wien | Wien | Wien |
| Country | AT | AT | AT |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Belgium

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.be | +32485121291 |
| Denied | customer+denied@email.be | +32485212123 |
| New user sign up | customer+new_user@email.be | +32485212101 |
| Dispute: return | customer+disputed-return@email.be | +32485212140 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.be | +32485212141 |
| Dispute: order already paid | customer+disputed-already_paid@email.be | +32485212142 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.be | +32485212143 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.be | +32485212144 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.be | +32485212145 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.be | +32485212146 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.be | +32485212150 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.be | +32485212151 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.be | +32485212152 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person BE |
| Last name | Person-be | Person-be | Test |
| Address | Grote Markt 1 | Grote Markt 1 | Parc du Cinquantenaire 10 |
| Zip code | 1000 | 1000 | 1000 |
| City | Brussel | Brussel | Bruxelles |
| Country | BE | BE | BE |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Czech Republic

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.cz | +420771613715 |
| Denied | customer+denied@email.cz | +420771623691 |
| New user sign up | customer+new_user@email.cz | +420771623765 |
| Dispute: return | customer+disputed-return@email.cz | +420771623708 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.cz | +420771623709 |
| Dispute: order already paid | customer+disputed-already_paid@email.cz | +420771623710 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.cz | +420771623711 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.cz | +420771623712 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.cz | +420771623713 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.cz | +420771623714 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.cz | +420771623720 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.cz | +420771623721 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.cz | +420771623722 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person CZ |
| Last name | Person-cz | Person-cz | Test |
| Address | Zazvorkova 1480/11 | Zázvorkova 1480/11 | Panská 7 |
| Zip code | 155 00 | 155 00 | 110 00 |
| City | Praha | PRAHA 13 | Praha |
| Country | CZ | CZ | CZ |
| Date of birth (DD-MM-YYYY) | 01-01-1970 | 27-06-1992 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Denmark

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.dk | +4542555628 |
| Denied | customer+denied@email.dk | +4552555348 |
| New user sign up | customer+new_user@email.dk | +4561555920 |
| Dispute: return | customer+disputed-return@email.dk | +4561555921 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.dk | +4531555956 |
| Dispute: order already paid | customer+disputed-already_paid@email.dk | +4571555576 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.dk | +4561555601 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.dk | +4571555705 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.dk | +4541555404 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.dk | +4525558959 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.dk | +4561555930 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.dk | +4561555931 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.dk | +4561555932 |
| Bank Authentication | customer+denied+auth_monthio@email.dk | +4561555922 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person DK |
| Last name | Person-dk | Person-dk | Test |
| Address | Dantes Plads 7 | Nygårdsvej 65 | Dantes Plads 7 |
| Zip code | 1556 | 2100 | 1556 |
| City | København Ø | København Ø | København Ø |
| Country | DK | DK | DK |
| Date of birth (DD-MM-YYYY) | 01-01-1980 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

#### Company

| Field                       | Approved            | Denied                     |
|-----------------------------|---------------------|----------------------------|
| Company registration number | 27968880            | 99999993                   |
| Company name                | Testcompany-dk      | Testcompany-dk             |
| Street                      | Nygårdsvej 65       | Nygårdsvej 65              |
| Zip code                    | 2100                | 2100                       |
| City                        | København Ø         | København Ø                |
| Phone number                | 20123456            | 20123456                   |
| Email                       | youremail@email.com | youremail+denied@email.com |

### Finland

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.fi | +358401234567 |
| Denied | customer+denied@email.fi | +358401234568 |
| New user sign up | customer+new_user@email.fi | +358401234584 |
| Dispute: return | customer+disputed-return@email.fi | +358401234585 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.fi | +358401234586 |
| Dispute: order already paid | customer+disputed-already_paid@email.fi | +358401234587 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.fi | +358401234588 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.fi | +358401234589 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.fi | +358401234590 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.fi | +358401234591 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.fi | +358401234600 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.fi | +358401234601 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.fi | +358401234602 |
| Bank Authentication | customer+denied+auth_bank_id_fi@email.fi Use Nordea with DEMOUSER4 for approved authentication. | +358401234596 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Person FI | Person FI |
| Last name | Person-fi | Test | Test |
| Address | Mannerheimintie 34 | Mannerheimintie 34 | Mannerheimintie 34 |
| Zip code | 00100 | 00100 | 00100 |
| City | Helsinki | Helsinki | Helsinki |
| Country | FI | FI | FI |
| Date of birth (DD-MM-YYYY) | 01-01-1999 | 01-01-1999 | 01-01-2000 |
| Personal number | 190122-829F |  |  |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

#### Company

| Approved                    | Denied              |
|-----------------------------|---------------------|
| Company registration number | 10891871            |
| Company name                | Testcompany-fi      |
| Street                      | Kiväärikatu 10      |
| Zip code                    | 28100               |
| City                        | Pori                |
| Phone number                | 0401234567          |
| Email                       | youremail@email.com |

### France

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.fr | +33689854321 |
| Denied | customer+denied@email.fr | +33687984322 |
| New user sign up | customer+new_user@email.fr | +33656194338 |
| Dispute: return | customer+disputed-return@email.fr | +33656194339 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.fr | +33656194340 |
| Dispute: order already paid | customer+disputed-already_paid@email.fr | +33656194341 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.fr | +33656194342 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.fr | +33656194343 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.fr | +33656194344 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.fr | +33656194345 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.fr | +33656194360 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.fr | +33656194361 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.fr | +33656194362 |
| ID Scan | customer+denied+auth_id_scan@email.fr | +33644974346 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person FR |
| Last name | Person-fr | Person-fr | Test |
| Address | 33 rue la Fayette | 33 rue la Fayette | 57 Rue Cuvier |
| Zip code | 75009 | 75009 | 75005 |
| City | Paris | Paris | Paris |
| Country | FR | FR | FR |
| Date of birth (DD-MM-YYYY) | 10-07-1990 | 10-07-1990 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Germany

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.de | +49017614284340 |
| Denied | customer+denied@email.de | +49017610927312 |
| New user sign up | customer+new_user@email.de | +491713920066 |
| Dispute: return | customer+disputed-return@email.de | +491713920016 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.de | +491713920017 |
| Dispute: order already paid | customer+disputed-already_paid@email.de | +491713920018 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.de | +491713920019 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.de | +491713920020 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.de | +491713920021 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.de | +491713920022 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.de | +491713920030 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.de | +491713920031 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.de | +491713920032 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Mock | Test | Person DE |
| Last name | Mock | Person-de | Test |
| Address | Neue Schönhauser Str. 2 | Neue Schönhauser Str. 2 | Bodestr. 1-3 |
| Zip code | 10178 | 10178 | 10178 |
| City | Berlin | Berlin | Berlin |
| Country | DE | DE | DE |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Greece

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.gr | +306945553624 |
| Denied | customer+denied@email.gr | +306945553625 |
| New user sign up | customer+new_user@email.gr | +306945553654 |
| Dispute: return | customer+disputed-return@email.gr | +306945553642 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.gr | +306945553643 |
| Dispute: order already paid | customer+disputed-already_paid@email.gr | +306945553644 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.gr | +306945553645 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.gr | +306945553646 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.gr | +306945553647 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.gr | +306945553648 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.gr | +306945553650 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.gr | +306945553651 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.gr | +306945553652 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person GR |
| Last name | Person-gr | Test-gr | Test |
| Address | Kephisias 37 | Baralo 56 | Dionysiou Areopagitou 15 |
| Zip code | 151 23 | 123 67 | 117 42 |
| City | Athina | Athina | Athens |
| Country | GR | GR | GR |
| Date of birth (DD-MM-YYYY) | 01-01-1960 | 11-11-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |
| Tax number | 090000045 | 090000045 | 090000045 |

### Hungary

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.hu | +36300102692 |
| Denied | customer+denied@email.hu | +36705553575 |
| New user sign up | customer+new_user@email.hu | +36505557327 |
| Dispute: return | customer+disputed-return@email.hu | +36505557326 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.hu | +36701308232 |
| Dispute: order already paid | customer+disputed-already_paid@email.hu | +36705553902 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.hu | +36201093784 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.hu | +36315555600 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.hu | +36385393517 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.hu | +36705550064 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.hu | +36505557330 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.hu | +36505557331 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.hu | +36505557332 |

| Field                      | Approved       | Denied         | Other flows    |
|----------------------------|----------------|----------------|----------------|
| First name                 | Test           | Person HU      | Person HU      |
| Last name                  | Person-hu      | Test           | Test           |
| Address                    | Ludovika tér 2 | Ludovika tér 2 | Ludovika tér 2 |
| Zip code                   | 1083           | 1083           | 1083           |
| City                       | Budapest       | Budapest       | Budapest       |
| Country                    | HU             | HU             | HU             |
| Date of birth (DD-MM-YYYY) | 01-01-2000     | 01-01-2000     | 01-01-2000     |

### Ireland

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.ie | +353855351400 |
| Denied | customer+denied@email.ie | +353855351401 |
| New user sign up | customer+new_user@email.ie | +353855351432 |
| Dispute: return | customer+disputed-return@email.ie | +353855351418 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.ie | +353855351419 |
| Dispute: order already paid | customer+disputed-already_paid@email.ie | +353855351420 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.ie | +353855351421 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.ie | +353855351422 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.ie | +353855351423 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.ie | +353855351424 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.ie | +353855351430 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.ie | +353855351431 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.ie | +353855351433 |
| ID Scan | customer+denied+auth_id_scan@email.ie | +353855351425 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person IE |
| Last name | Person-ie | Person-ie | Test |
| Address | 30 King Street South | 30 King Street South | 25 Merrion Street Upper |
| Zip code | D02 C838 | D02 C838 | D02 AW74 |
| City | Dublin | Dublin | Dublin |
| Country | IE | IE | IE |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Italy

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.it | +393339741231 |
| Denied | customer+denied@email.it | +393312232389 |
| New user sign up | customer+new_user@email.it | +393312232432 |
| Dispute: return | customer+disputed-return@email.it | +393312232406 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.it | +393312232407 |
| Dispute: order already paid | customer+disputed-already_paid@email.it | +393312232408 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.it | +393312232409 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.it | +393312232410 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.it | +393312232411 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.it | +393312232412 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.it | +393312232420 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.it | +393312232421 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.it | +393312232422 |
| ID Scan | customer+denied+auth_id_scan@email.it | +393312232413 |

| Field | Approved | Denied | Other flows |
|-----|--------|------|-----------|
| First name | Test | Test | Person IT |
| Last name | Person-it | Person-it | Test |
| Address | Via Enrico Fermi 150 | Via Enrico Fermi 150 | Piazza del Popolo 12 |
| Zip code | 00146 | 00146 | 00187 |
| City | Roma | Roma | Roma |
| Country | IT | IT | IT |
| Fiscal code (Codice fiscale) | RSS BNC 80A41 H501B | RSS BNC 80A41 H501B | <ul><li>Dispute - return:PRS CST 00A41 H501N</li><li>Dispute - goods not received:PRS VST 00A41 H501G</li><li>Dispute - order already paid:PRS BST 00A41 H501M</li><li>Dispute - faulty goods:PRS NST 00A41 H501Y</li><li>Dispute - incorrect invoice:PRS MST 00A41 H501X</li><li>Dispute - high-risk order:PRS QST 00A41 H501B</li><li>Dispute - unauthorized purchase:PRS QTS 00A41 H501C</li></ul> |
| Date of birth (DD-MM-YYYY) | 01-01-1980 | 01-01-1980 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Netherlands

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.nl | +31689124321 |
| Denied | customer+denied@email.nl | +31632167678 |
| New user sign up | customer+new_user@email.nl | +31632167655 |
| Dispute: return | customer+disputed-return@email.nl | +31632167695 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.nl | +31632167696 |
| Dispute: order already paid | customer+disputed-already_paid@email.nl | +31632167697 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.nl | +31632167698 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.nl | +31632167699 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.nl | +31632167700 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.nl | +31632167701 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.nl | +31632167710 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.nl | +31632167711 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.nl | +31632167712 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person NL |
| Last name | Person-nl | Person-nl | Test |
| Address | Osdorpplein 137 | Osdorpplein 137 | Museumstraat 1 |
| Zip code | 1068 SR | 1068 SR | 1071 XX |
| City | Amsterdam | Amsterdam | Amsterdam |
| Country | NL | NL | NL |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Norway

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.no | +4740123456 |
| Denied | customer+denied@email.no | +4740123457 |
| New user sign up | customer+new_user@email.no | +4740123485 |
| Dispute: return | customer+disputed-return@email.no | +4740123474 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.no | +4740123475 |
| Dispute: order already paid | customer+disputed-already_paid@email.no | +4740123476 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.no | +4740123477 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.no | +4740123478 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.no | +4740123479 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.no | +4740123480 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.no | +4740123490 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.no | +4740123491 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.no | +4740123492 |

| Field | Approved | Denied | Other flows |
|-----|--------|------|-----------|
| First name | Jane | Test | Person NO |
| Last name | Test | Person-no | Test |
| Address | Edvard Munchs Plass 1 | Sæffleberggate 56 | Edvard Munchs Plass 1 |
| Zip code | 0194 | 0563 | 0194 |
| City | Oslo | Oslo | Oslo |
| Country | NO | NO | NO |
| Date of birth (DD-MM-YYYY) | 01-08-1970 | 01-08-1970 | 01-01-2000 |
| Personal number | NO01087000571 | NO01087000148 | <ul><li>Dispute - return:NO30062449205</li><li>Dispute - goods not received:NO27083206670</li><li>Dispute - order already paid:NO14040845144</li><li>Dispute - faulty goods:NO16089639496</li><li>Dispute - incorrect invoice:NO19046731789</li><li>Dispute - high-risk order:NO27115906319</li><li>Dispute - unauthorized purchase:NO25064127953</li></ul> |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

#### Company

| Approved                    | Denied              |
|-----------------------------|---------------------|
| Company registration number | 999999999           |
| Company name                | Testcompany-no      |
| Street                      | Sæffleberggate 56   |
| Zip code                    | 0563                |
| City                        | Oslo                |
| Email                       | youremail@email.com |

### Poland

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.pl | +48795222223 |
| Denied | customer+denied@email.pl | +48795223325 |
| New user sign up | customer+new_user@email.pl | +48795223355 |
| Dispute: return | customer+disputed-return@email.pl | +48795223342 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.pl | +48795223343 |
| Dispute: order already paid | customer+disputed-already_paid@email.pl | +48795223344 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.pl | +48795223345 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.pl | +48795223346 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.pl | +48795223347 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.pl | +48795223348 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.pl | +48795223350 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.pl | +48795223351 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.pl | +48795223352 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person PL |
| Last name | Person-pl | Person-pl | Test |
| Address | Ul. Górczewska 124 | Ul. Górczewska 124 | Rynek Starego Miasta 28 |
| Zip code | 01-460 | 01-460 | 00-272 |
| City | Warszawa | Warszawa | Warszawa |
| Country | PL | PL | PL |
| Date of birth (DD-MM-YYYY) | 05-05-1967 | 05-05-1967 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Portugal

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.pt | +351935556731 |
| Denied | customer+denied@email.pt | +351915593837 |
| New user sign up | customer+new_user@email.pt | +351808151176 |
| Dispute: return | customer+disputed-return@email.pt | +351808151188 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.pt | +351760715143 |
| Dispute: order already paid | customer+disputed-already_paid@email.pt | +351762748941 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.pt | +351302066842 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.pt | +351926839015 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.pt | +351301381736 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.pt | +351937416657 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.pt | +351808151190 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.pt | +351808151191 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.pt | +351808151192 |
| ID Scan | customer+denied+auth_id_scan@email.pt | +351912341112 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person PT |
| Last name | Person-pt | Person-pt | Test |
| Address | Avenida Dom João II 40 | Avenida Dom João II 40 | Praça do Comércio 78 |
| Zip code | 1990-094 | 1990-094 | 1100-148 |
| City | Lisboa | Lisboa | Lisboa |
| Country | PT | PT | PT |
| Date of birth (DD-MM-YYYY) | 10-07-1990 | 10-07-1990 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Romania

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.ro | +40741209876 |
| Denied | customer+denied@email.ro | +40707127444 |
| New user sign up | customer+new_user@email.ro | +40707129334 |
| Dispute: return | customer+disputed-return@email.ro | +40707129331 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.ro | +40707129442 |
| Dispute: order already paid | customer+disputed-already_paid@email.ro | +40707129553 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.ro | +40707129664 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.ro | +40707129775 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.ro | +40707129886 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.ro | +40707129997 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.ro | +40707129340 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.ro | +40707129341 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.ro | +40707129342 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person RO |
| Last name | Person-ro | Person-ro | Test |
| Address | Drumul Taberei 35 | Drumul Taberei 35 | Calea Victoriei 12 |
| Zip code | 061357 | 061357 | 030026 |
| City | București | București | București |
| Sector | Sectorul 6 | Sectorul 6 | Sectorul 3 |
| Country | RO | RO | RO |
| Date of birth (DD-MM-YYYY) | 25-12-1970 | 25-12-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |
| Personal Identification Number (CNP) | 1701225193558 |  |  |

### Slovakia

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.sk | +421905123456 |
| Denied | customer+denied@email.sk | +421905123457 |
| New user sign up | customer+new_user@email.sk | +421905123432 |
| Dispute: return | customer+disputed-return@email.sk | +421905123474 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.sk | +421905123475 |
| Dispute: order already paid | customer+disputed-already_paid@email.sk | +421905123476 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.sk | +421905123477 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.sk | +421905123478 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.sk | +421905123479 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.sk | +421905123480 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.sk | +421905123490 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.sk | +421905123491 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.sk | +421905123492 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Person Sk | Person Sk |
| Last name | Person-sk | Test | Test |
| Address | Vajanského nábrežie 2 | Vajanského nábrežie 2 | Vajanského nábrežie 2 |
| Zip Code | 810 06 | 810 06 | 810 06 |
| City | Bratislava | Bratislava | Bratislava |
| Country | SK | SK | SK |
| Date of birth (DD-MM-YYYY) | 01-01-2000 | 01-01-2000 | 07-10-1997 |
| Personal Identification Number (Rodné Číslo) | 000101/0009 | 000101/0020 | 971007/0249 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Spain

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.es | +34672563009 |
| Denied | customer+denied@email.es | +34682425101 |
| New user sign up | customer+new_user@email.es | +34670097139 |
| Dispute: return | customer+disputed-return@email.es | +34670097138 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.es | +34680859660 |
| Dispute: order already paid | customer+disputed-already_paid@email.es | +34735215817 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.es | +34782234072 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.es | +34699002829 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.es | +34782153382 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.es | +34670369667 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.es | +34670097140 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.es | +34670097141 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.es | +34670097142 |
| ID Scan | customer+denied+auth_id_scan@email.es | +34670097113 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person ES |
| Last name | Person-es | Person-es | Test |
| DNI | 99999999R | 99999999R | 99999999R |
| Address | C. de Atocha, 27 | C. de Atocha, 27 | Calle de Santa Isabel 52 DCHA |
| Zip code | 28012 | 28012 | 28012 |
| City | Madrid | Madrid | Madrid |
| Country | ES | ES | ES |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Sweden

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.se | +46701740615 |
| Denied | customer+denied@email.se | +46701740620 |
| New user sign up | customer+new_user@email.se | +46701740656 |
| Dispute: return | customer+disputed-return@email.se | +46701740637 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.se | +46701740638 |
| Dispute: order already paid | customer+disputed-already_paid@email.se | +46701740639 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.se | +46701740640 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.se | +46701740641 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.se | +46701740642 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.se | +46701740643 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.se | +46701740660 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.se | +46701740661 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.se | +46701740662 |

| Field | Approved | Denied | Other flows |
|-----|--------|------|-----------|
| First name | Alice | Test | Person SE |
| Last name | Test | Person-se | Test |
| Address | Södra Blasieholmshamnen 2 | Karlaplan 3 | Södra Blasieholmshamnen 2 |
| Zip code | 11 148 | 11 460 | 11 148 |
| City | Stockholm | Stockholm | Stockholm |
| Country | SE | SE | SE |
| Date of birth (DD-MM-YYYY) | 21-03-1941 | 28-10-1941 | 01-01-2000 |
| Personal number | SE194103219202 | SE194110288083 | <ul><li>Dispute - return:SE200001011287</li><li>Dispute - goods not received:SE200001011493</li><li>Dispute - order already paid:SE200001015270</li><li>Dispute - faulty goods:SE200001019744</li><li>Dispute - incorrect invoice:SE200001011485</li><li>Dispute - high-risk order:SE200001015726</li><li>Dispute - unauthorized purchase:SE200001015973</li></ul> |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

#### Company

| Approved                    | Denied              |
|-----------------------------|---------------------|
| Company registration number | 002031-0132         |
| Company name                | Testcompany-se      |
| Street \#1                  | Stårgatan 1         |
| Zip code \#1                | 12345               |
| City \#1                    | Ankeborg            |
| Street \#2                  | Lillegatan 1        |
| Zip code \#2                | 12334               |
| City \#2                    | Ankeborg            |
| Phone number                | 0765260000          |
| Email                       | youremail@email.com |

### Switzerland

**The use of provided sample data is strongly recommended.** When using your own sample data, your test orders might get rejected:

- Avoid using *test* or the plus sign *+* in either First name or Last name if you want to get your order approved.

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.ch | +41758680000 |
| Denied | customer+denied@email.ch | +41758680001 |
| New user sign up | customer+new_user@email.ch | +41758680028 |
| Dispute: return | customer+disputed-return@email.ch | +41758680018 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.ch | +41618680019 |
| Dispute: order already paid | customer+disputed-already_paid@email.ch | +41618680020 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.ch | +41618680021 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.ch | +41618680022 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.ch | +41618680023 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.ch | +41618680024 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.ch | +41758680030 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.ch | +41758680031 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.ch | +41758680032 |
| ID Scan | customer+denied+auth_id_scan@email.ch | +41758680025 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Accepted | Customer | Accepted |
| Last name | Person-ch | Person-ch | Person-ch |
| Address | Augustinergasse 2 | Bahnhofstrasse 77 | Augustinergasse 2 |
| Zip code | 4051 | 8001 | 4051 |
| City | Basel | Zürich | Basel |
| Date of birth (DD-MM-YYYY) | 01-01-1990 | 01-01-2000 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### United Kingdom

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.uk | +447755564318 |
| Denied | customer+denied@email.uk | +447355505530 |
| New user sign up | customer+new_user@email.gb | +445674519812 |
| Dispute: return | customer+disputed-return@email.uk | +445674519807 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.uk | +447455511475 |
| Dispute: order already paid | customer+disputed-already_paid@email.uk | +447755535234 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.uk | +443794116227 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.uk | +443012348266 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.uk | +447555529984 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.uk | +447555595216 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.uk | +445674519810 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.uk | +445674519811 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.uk | +445674519814 |
| ID Scan | customer+denied+auth_id_scan@email.co.uk | +445674519822 |
| Bank Authentication | customer+denied+auth_bank_login@email.gb | +445674519815 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | Person GB |
| Last name | Person-uk | Person-uk | Test |
| Address | 10 New Burlington Street Apt. 214 | 10 New Burlington Street Apt. 214 | 150 London Wall |
| Zip code | W1S 3BE | W1S 3BE | EC2Y 5HN |
| City | London | London | London |
| Country | GB | GB | GB |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

#### Term loan financing

When testing term loan financing in playground, enter the following billing address details:

| Field            | Value                      |
|------------------|----------------------------|
| `city`           | Test Town                  |
| `country`        | GB                         |
| `email`          | termloanfinancing@email.uk |
| `family_name`    | Cameroon                   |
| `given_name`     | Campbell                   |
| `phone`          | 07744225533                |
| `postal_code`    | X9 9LG                     |
| `street_address` | 34 Global Avenue           |

You'll be asked to provide additional information, for example, about income and dependants. In this step, you're free to provide any details.

In the next step, enter the following bank details:

| Field               | Value                |
|---------------------|----------------------|
| Account holder name | Mr Campbell Cameroon |
| Sort code           | 20-00-00             |
| Account number      | 55779911             |

## Americas

### Canada

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.ca | +15197438620 |
| Denied | customer+denied@email.ca | +15197308624 |
| New user sign up | customer+new_user@email.ca | +15195550145 |
| Dispute: return | customer+disputed-return@email.ca | +15195550116 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.ca | +15195550117 |
| Dispute: order already paid | customer+disputed-already_paid@email.ca | +15195550118 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.ca | +15195550119 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.ca | +15195550120 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.ca | +15195550121 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.ca | +15195550122 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.ca | +15195550140 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.ca | +15195550141 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.ca | +15195550142 |
| ID Scan | customer+denied+auth_id_scan@email.ca | +15195550145 |
|  | email+reject_reason_OTHER@email.com |  |
|  | email+reject_reason_COULD_NOT_ESTABLISH_IDENTITY@email.com |  |
|  | email+reject_reason_CREDIT_LIMIT_EXCEEDED@email.com |  |
|  | email+reject_reason_CUSTOMER_NOT_FULFILLING_PREVIOUS_ENGAGEMENTS@email.com |  |
|  | email+reject_reason_EXTERNAL_HARD_REJECT@email.com |  |
|  | email+reject_reason_HIGH_RISK@email.com |  |
|  | email+reject_reason_LEGAL_RESTRAINTS@email.com |  |
|  | email+reject_reason_TECHNICAL_ERROR@email.com |  |
|  | email+reject_reason_INTERNAL_BLOCK@email.com |  |
|  | email+reject_reason_LOW_CREDIT_RATING@email.com |  |
|  | email+reject_reason_UNDER_AGE@email.com |  |
|  | email+reject_reason_DENIED@email.com |  |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | John |
| Last name | Person-ca | Person-ca | Test |
| Address | 2693 Byron Rd | 2693 Byron Rd | 380 Sussex Dr |
| Zip code | V7H 1L9 | V7H 1L9 | K1N 9N4 |
| City | North Vancouver | North Vancouver | Ottawa |
| Province | BC | BC | ON |
| Country | CA | CA | CA |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### Mexico

#### Private person

| Flow Mexico | Email address | Phone number |
|----|----|----|
| Approved | customer@email.mx | +525593747739 |
| Denied | customer+denied@email.mx | +525593747740 |
| New user sign up | customer+new_user@email.mx | +525593747767 |
| Dispute: return | customer+disputed-return@email.mx | +525593747757 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.mx | +525593747758 |
| Dispute: order already paid | customer+disputed-already_paid@email.mx | +525593747759 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.mx | +525593747760 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.mx | +525593747761 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.mx | +525593747762 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.mx | +525593747763 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.mx | +525593747770 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.mx | +525593747771 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.mx | +525593747772 |

| Field Mexico | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Person-mx | John |
| Last name | Person-mx | Test | Test |
| Address | Av Cuauhtémoc 462 Col Piedad Narvarte | Av Cuauhtémoc 462 Col Piedad Narvarte | Revillagigedo 11 Col Centro |
| Zip code | 03000 | 03000 | 06000 |
| City | Benito Juárez | Benito Juárez | Ciudad de México |
| State | CDMX | CDMX | CMX |
| Country | MX | MX | MX |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### United States of America

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.us | +13106683312 |
| Denied | customer+denied@email.us | +13106354386 |
| New user sign up | customer+new_user@email.us | +13105550134 |
| Dispute: return | customer+disputed-return@email.us | +13105550116 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.us | +13105550117 |
| Dispute: order already paid | customer+disputed-already_paid@email.us | +13105550118 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.us | +13105550119 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.us | +13105550120 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.us | +13105550121 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.us | +13105550122 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.us | +13105550130 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.us | +13105550131 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.us | +13105550132 |
| ID Scan | customer+denied+auth_id_scan@email.us | +13105550124 |
| Bank Authentication | customer+denied+auth_bank_login@email.us | +13105558963 |
| Email Verification | customer+denied+auth_otp_email@email.us | +13105558632 |
| Phone Verification | customer+denied+auth_otp_phone@email.us | +13105558633 |
| Card Security Code Verification | customer+denied+auth_cvv_entry@email.us | +13105558634 |
| Rejection | customer+reject_reason_other@email.us | +13105558637 |
| Rejection | customer+reject_reason_could_not_establish_identity@email.us | +13105558636 |
| Rejection | customer+reject_reason_credit_limit_exceeded@email.us | +13105558638 |
| Rejection | cust+reject_reason_customer_not_fulfilling_previous_engagements@email.us | +13105558639 |
| Rejection | customer+reject_reason_external_hard_reject@email.us | +13105558640 |
| Rejection | customer+reject_reason_high_risk@email.us | +13105558641 |
| Rejection | customer+reject_reason_legal_restraints@email.us | +13105558642 |
| Rejection | customer+reject_reason_technical_error@email.us | +13105558643 |
| Rejection | customer+reject_reason_internal_block@email.us | +13105558644 |
| Rejection | customer+reject_reason_low_credit_rating@email.us | +13105558645 |
| Rejection | customer+reject_reason_under_age@email.us | +13105558646 |
| Rejection | customer+reject_reason_denied@email.us | +13105558647 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | John |
| Last name | Person-us | Person-us | Test |
| Address | 509 Amsterdam Ave | 509 Amsterdam Ave | 1300 Constitution Ave |
| Zip code | 10024-3941 | 10024-3941 | 20002-6452 |
| City | New York | New York | Washington |
| State | NY | NY | DC |
| Date of birth (DD-MM-YYYY) | 07-10-1970 | 07-10-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

## Asia & Oceania

### Australia

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.au | +61473752244 |
| Denied | customer+denied@email.au | +61473763254 |
| New user sign up | customer+new_user@email.au | +61491574119 |
| Dispute: return | customer+disputed-return@email.au | +61491574118 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.au | +61491574632 |
| Dispute: order already paid | customer+disputed-already_paid@email.au | +61491575254 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.au | +61491575789 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.au | +61491575789 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.au | +61491576801 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.au | +61491577426 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.au | +61491574120 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.au | +61491574121 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.au | +61491574122 |
| ID Scan | customer+denied+auth_id_scan@email.au | +61491574127 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | John | John |
| Last name | Person-au | snow | Test |
| Address | 4 Wharf St | 1-5 Silverwater Rd | 1 Bennelong Point |
| Zip code | 4877 | 2128 | 2000 |
| City | Port Douglas | Silverwater | Sydney |
| State | QLD | NSW | NSW |
| Country | AU | AU | AU |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 03-05-1994 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

### New Zealand

#### Private person

| Flow | Email address | Phone number |
|----|----|----|
| Approved | customer@email.nz | +6427555290 |
| Denied | customer+denied@email.nz | +642993007712 |
| New user sign up | customer+new_user@email.nz | +642862276121 |
| Dispute: return | customer+disputed-return@email.nz | +642862276120 |
| Dispute: goods not received | customer+disputed-goods_not_received@email.nz | +648596357854 |
| Dispute: order already paid | customer+disputed-already_paid@email.nz | +642838916248 |
| Dispute: faulty goods | customer+disputed-faulty_goods@email.nz | +64265615253 |
| Dispute: incorrect invoice | customer+disputed-incorrect_invoice@email.nz | +648597431043 |
| Dispute: high-risk order | customer+disputed-high_risk_order@email.nz | +64217249819 |
| Dispute: unauthorized purchase | customer+disputed-unauthorized_purchase@email.nz | +642293258935 |
| Dispute: non-guaranteed payment program | customer+disputed-non_guaranteed_payment_program@email.nz | +642862276130 |
| Dispute: non-compliance | customer+disputed-non_compliance@email.nz | +642862276131 |
| Dispute: return not possible | customer+disputed-return_not_possible@email.nz | +642862276132 |
| ID Scan | customer+denied+auth_id_scan@email.nz | +642862276142 |

| Field | Approved | Denied | Other flows |
|----|----|----|----|
| First name | Test | Test | John |
| Last name | Person-nz | Person-nz | Test |
| Address | 286 Mount Wellington Highway | 286 Mount Wellington Highway | Te Papa Tongarewa Museum Of Nz |
| Zip code | 6011 | 6011 | 6011 |
| City | Auckland | Wellington | Wellington |
| Country | NZ | NZ | NZ |
| Date of birth (DD-MM-YYYY) | 10-07-1970 | 10-07-1970 | 01-01-2000 |
| OTP (Random 6 digits different from 999999) | 123456 | 123456 | 123456 |

## Other test scenarios

The sample customer data lets you test the basic approve and deny transaction flows. However, you can also test some other Payments scenarios by adding suffixes to sample usernames.

In the examples below, the email address reflects sample customer data for the United States. Make sure to adjust the address to match the country in which your store operates.

To launch a Payments widget, include a sample email address in your API call. You can modify the address to display the sign-up widget or delay the payment.

To launch a Checkout widget, include a sample email address in your API call.

| Scenario | Customer email address pattern | Example | Applies to Payments |
|--------|------------------------------|-------|-------------------|
| New customer signup | username+require_signup@domain.com | customer+require_signup@email.us | Payments |
| Returning customer | username@domain.com | customer@email.us | Payments |
| Don't show form (only when pre-screen is enabled) | username+red@domain.com | customer+red@email.us | Payments |
| Pending payment <ul><li>{status} is the expected status after the time delay, either accept to accept a payment or reject to reject a payment.</li></ul> * {time delay} is the time delay, in minutes, before the decision is made and the status is confirmed. The value must be a two-digit number in the range of 00–99. Note: Only works for US and UK. | username+pend-{status}-{time delay}@domain.com | customer+pend-accept-05@email.us | Payments |
| Only present pre-paid options | example-email+red@example.com | customer+red@email.us | Checkout |