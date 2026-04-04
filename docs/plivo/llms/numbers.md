# Source: https://plivo.com/docs/numbers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Learn about phone number types, availability, rental, and compliance on Plivo.

Phone numbers are carrier-recognized identifiers that enable applications to send and receive calls and messages over the public telephone network (PSTN). They provide reachability to global mobile and landline networks, trust through verified caller identity, and support for voice, SMS, and MMS capabilities.

You can learn more about searching and buying numbers in the [Phone Numbers API documentation](/numbers/phone-numbers), and learn more about accessing the numbers already added to your account in the [Account Phone Numbers API documentation](/numbers/account-phone-numbers).

## Phone number types

Plivo offers different phone number types depending on the country. Availability varies by region—see the [Country availability](#country-availability) table below.

### Fixed (Local) numbers

Fixed numbers are assigned to a specific region—a city, area, or country. Callers from within the region are charged local rates. Fixed numbers support voice, and in some countries (like the US and Canada) also support SMS.

### Toll-free numbers

Toll-free numbers (prefixes like 1800 or 800) are free for callers—charges are billed to the number owner. Businesses use them for customer service lines and SMS messaging.

### Mobile numbers

Mobile numbers support SMS and voice. Plivo offers mobile numbers in select countries only (UK, Australia).

## Country availability

Plivo offers phone numbers across multiple regions:

| Country              | Number Types                                                                |
| -------------------- | --------------------------------------------------------------------------- |
| United States        | Local, Toll-free                                                            |
| Canada               | Local, Toll-free                                                            |
| India                | Local ([calling guidelines](/faq/voice-api-and-SIP-trunking/india-calling)) |
| United Kingdom       | Local, Mobile                                                               |
| Australia            | Local, Mobile, Toll-free                                                    |
| New Zealand          | Local, Toll-free                                                            |
| Singapore            | Local                                                                       |
| Brazil               | Local, Toll-free                                                            |
| United Arab Emirates | Local                                                                       |

<Note>
  US and India numbers are available on the Pay As You Go plan. Other countries require the Enterprise plan (\$1,000/month commit). See [Plivo Pricing](https://www.plivo.com/pricing/) for details.
</Note>

## Renting phone numbers

### Via Console

1. Navigate to **Phone Numbers > Buy Numbers**
2. Filter by country, capabilities (Voice, SMS, MMS), and number type
3. Click **Buy Number**

### Via API

Use the [Phone Number API](/numbers/phone-numbers#buy-a-phone-number) to rent numbers programmatically.

There is no limit on the number of phone numbers you can rent, as long as you have sufficient credits.

## Charges

| Charge             | Description                                                |
| ------------------ | ---------------------------------------------------------- |
| **Monthly Rental** | Recurring fee, billed from rental date                     |
| **Setup Fee**      | One-time fee when renting (applicable in select countries) |

See [Phone Number Pricing](https://www.plivo.com/virtual-phone-numbers/pricing/) for details.

## Compliance requirements

Many countries require regulatory documentation before numbers can be activated. Requirements vary by country, number type, and end-user type (business or individual).

Compliance applications bundle end-user information and regulatory documents for country-specific compliance requirements. Assign them during number rental or via **Phone Numbers > Compliance Applications** in the Console.

See [Regulatory Compliance](/numbers/regulatory-compliance) for details.

## Caller ID and CNAM

### Branded Caller ID (CNAM)

CNAM (Caller Name) displays your business name instead of just the phone number on outgoing calls.

| Country           | CNAM Support                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **United States** | Supported. See [CNAM Lookup](/numbers/cnam-lookup) for details.                                                                                                          |
| **India**         | Not yet available. Indian carriers are gradually rolling out CNAM support. Plivo is working with carriers and will notify customers when this feature becomes available. |

### Verified Caller ID

Verified Caller ID lets you use your own non-Plivo number as a caller ID for outbound calls:

1. Go to [Verified Caller IDs](https://cx.plivo.com/home)
2. Add your phone number
3. Complete verification via SMS or voice call
4. Use the verified number as the `from` parameter in API calls

<Warning>
  **India:** Verified Caller ID is not supported. All outbound calls from India must use a Plivo-rented Indian number as the caller ID.
</Warning>

## Bulk Operations

### Bulk Number Purchase

Use the API to search and rent multiple numbers:

```python  theme={null}
# Search for available numbers
numbers = client.numbers.search(country_iso='US', type='local', limit=10)

# Rent each number
for number in numbers:
    client.numbers.buy(number.number)
```

### Bulk Unrent

```python  theme={null}
# List your numbers
my_numbers = client.numbers.list()

# Unrent specific numbers
for number in numbers_to_unrent:
    client.numbers.delete(number)
```

<Note>
  API rate limits apply. For bulk operations exceeding 100 numbers, spread requests over time or contact support for higher limits.
</Note>

### Get Available Countries

List countries where numbers are available:

```bash  theme={null}
curl -i --user AUTH_ID:AUTH_TOKEN \
  https://api.plivo.com/v1/Account/{auth_id}/PhoneNumber/
```

## Related concepts

### Subaccounts

Subaccounts let you link numbers to isolate traffic across departments, customers, or use cases. Each subaccount has its own Auth ID and Token; charges deduct from the main account.

See [Subaccount API](/account/api/subaccount) for details.

### Plivo Applications

A Plivo Application is assigned to numbers to define how incoming calls and messages are handled using XML instructions.

See [Application API](/account/api/application) and [Voice XML](/voice/xml/overview) for details.
