# Source: https://plivo.com/docs/numbers/cnam-lookup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CNAM Lookup

> Learn about CNAM (Caller ID Name) lookup for US phone numbers on Plivo.

CNAM (Caller ID Name) is a feature in the US public telephone network that associates phone numbers with registered names. When someone receives a call, their carrier queries the Line Information Database (LIDB) and displays the caller's registered name.

## Where is CNAM lookup available?

CNAM lookup on Plivo works for:

* Inbound Voice API calls on US phone numbers
* Inbound Zentrunk (SIP trunking) calls on US phone numbers

<Note>
  CNAM is only available for US numbers and inbound calls only.
</Note>

## How does CNAM lookup work?

1. Caller dials your Plivo US number
2. Plivo queries the LIDB for the caller's registered name
3. CNAM data is included in the call callback payload
4. Your application can display or use the caller name

## Configure CNAM settings

### Set account-level default

1. Navigate to **Phone Numbers > Settings**
2. Enable or disable CNAM lookup as the default
3. This setting applies to numbers rented after the change

### Configure during number purchase

1. Go to **Phone Numbers > Buy Numbers**
2. Search for US numbers
3. During purchase, select CNAM lookup configuration
4. If you skip configuration, the account default applies

### Update CNAM on existing numbers

**Single number:**

1. Go to **Phone Numbers > Active**
2. Click on the US phone number
3. Update CNAM lookup setting
4. Save

**Multiple numbers:**

1. Go to **Phone Numbers > Active**
2. Select numbers using checkboxes
3. Click **Choose Action > Update CNAM**
4. Apply changes

## View CNAM status

### Via Console

1. Navigate to **Phone Numbers > Active**
2. View CNAM lookup status column for US numbers
3. Use filters to show only CNAM-enabled or disabled numbers

### Via API

Use the `cnam_lookup` parameter of the [Account Phone Numbers API](/numbers/account-phone-numbers):

```
GET /v1/Account/{auth_id}/Number/{number}/
```

Response includes:

```json  theme={null}
{
  "number": "14151234567",
  "cnam_lookup": true
}
```

### Filter numbers by CNAM status

Use the `cnam_lookup` parameter in the [List Account Phone Numbers API](/numbers/account-phone-numbers#list-all-numbers):

```
GET /v1/Account/{auth_id}/Number/?cnam_lookup=true
```

## Callback data

When CNAM lookup is enabled, inbound call callbacks include:

| Parameter            | Description                             |
| -------------------- | --------------------------------------- |
| `cnam_lookup_result` | The caller's registered name (if found) |

<Note>
  CNAM data may not be available for all callers. Mobile numbers and some VoIP services may not have CNAM records.
</Note>

## Pricing

CNAM lookup is charged **per inbound call** when enabled on a number.

* Charged regardless of whether a name is found
* See [Voice Pricing](https://cx.plivo.com/billing/plans-and-pricing) for current rates

## When to enable CNAM

Enable CNAM selectively on numbers where caller identification provides business value:

* Customer service lines
* Sales hotlines
* Support numbers

### Managing costs

* Disable CNAM on high-volume numbers if caller name isn't needed
* Monitor CNAM charges in your monthly invoice
* Use account-level defaults to control costs

## Handling missing results

Your application should gracefully handle cases where:

* CNAM lookup returns no result
* Caller has no registered name
* Database timeout occurs

## Limitations

| Limitation        | Details                                            |
| ----------------- | -------------------------------------------------- |
| US only           | CNAM lookup is only available for US phone numbers |
| Inbound only      | Only works for incoming calls, not outbound        |
| Database coverage | Not all phone numbers have CNAM records            |
| Accuracy          | CNAM data may be outdated or incorrect             |
