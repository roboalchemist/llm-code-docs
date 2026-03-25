# Source: https://plivo.com/docs/numbers/number-porting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Number Porting

> Learn how to port phone numbers to and from Plivo, including timelines, requirements, and troubleshooting.

Porting transfers a phone number from one service provider to another. Number porting lets you retain the same phone number while switching service providers, avoiding service interruptions and maintaining your existing user base.

<Note>
  Number porting is available for **US and Canada only**. Port-in is free of charge.
</Note>

## Porting timeline

| Number Type                    | Timeline                                                    |
| ------------------------------ | ----------------------------------------------------------- |
| Local numbers                  | Up to 4 weeks                                               |
| Toll-free numbers              | Similar timeline                                            |
| Project porting (100+ numbers) | May take longer; requires numbers from same carrier account |

## What numbers can be ported to Plivo?

* Local numbers (US and Canada)
* Toll-free numbers (US and Canada)

## Required documents

You must have a Plivo Standard account to initiate a port-in request. See [Account Management FAQ](/faq/account/account-management) for account requirements. Before you send the porting request, make sure you have the following documents:

| Document                          | Description                                                                                                                                                                                 | Required                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Letter of Authorization (LOA)** | Signed by the authorized user/owner of the number(s). Use our [LOA template](https://cdn.prod.website-files.com/6565737286e587567248583f/686fba5cfad3ae244a7aeb39_Plivo-LOA-Template.docx). | Mandatory for toll-free; optional for fixed numbers |
| **PIN**                           | Depending on coverage, may be required for US numbers. Include if you have one.                                                                                                             | Optional                                            |
| **Recent Invoice**                | Copy of your most recent phone bill (within 30-60 days) showing account name, authorized username, and billing details.                                                                     | Optional but recommended                            |

<Warning>
  The name and address on your LOA must match exactly what your current carrier has on file. Contact your carrier to verify this information or request a Customer Service Record (CSR).
</Warning>

## How to port your phone number to Plivo

### Overview of the process

1. Submit porting request documentation to Plivo
2. Plivo submits the porting request to the gaining carrier
3. The gaining carrier submits the porting request to the losing carrier
4. The losing carrier approves or rejects the request
5. If approved, Plivo notifies you of the Firm Order Commitment (FOC), or porting date
6. On the FOC date, Plivo activates the number, tests all capabilities, and notifies you that the process is complete

### Submit your port request

1. Log in to the Plivo console and go to **Phone Numbers > Port-In > [New Port-In Order](https://cx.plivo.com/phone-numbers)**
2. Fill in your business details on the **User Details** screen, then click **Continue**

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screenshot-2024-02-22-at-7-07-07-pm.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=d62a4815a849553650502b0832cc655d" alt="" width="1204" height="648" data-path="images/screenshot-2024-02-22-at-7-07-07-pm.png" />
</Frame>

3. On the **Port-In Details** screen:
   * Select the phone number type
   * Select your preferred port-in date (at least 2 business days away)
   * Add the numbers you want to port in
   * Enter the current carrier's account number and PIN (if applicable)
   * Click **Continue**

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screenshot-2024-02-22-at-7-06-25-pm.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fec8e082c1c1ecedabf0306a140a0ea8" alt="" width="1348" height="816" data-path="images/screenshot-2024-02-22-at-7-06-25-pm.png" />
</Frame>

4. On the **Numbers Configure** screen:
   * Select capabilities (Voice or Voice + SMS)
   * Enter an alias for identification
   * Select a subaccount (optional)
   * Enter a CNAM for caller ID branding (optional)
   * Select the [XML](/voice/xml/overview), [PHLO](/phlo/getting-started/getting-started), or Zentrunk application to associate with the numbers

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screenshot-2024-02-22-at-7-05-32-pm.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fdb7b3d4d39c9c32ae8ffd7b6ddbe458" alt="" width="1062" height="632" data-path="images/screenshot-2024-02-22-at-7-05-32-pm.png" />
</Frame>

5. Upload supporting documents (LOA, invoice) and click **Submit**

<Frame>
    <img src="https://mintcdn.com/plivo/7-odxN9fJG_Dg1dt/images/screenshot-2024-02-22-at-7-04-19-pm.png?fit=max&auto=format&n=7-odxN9fJG_Dg1dt&q=85&s=fbece4a237dfbc11f98cc78e3d8a55a7" alt="" width="1654" height="1112" data-path="images/screenshot-2024-02-22-at-7-04-19-pm.png" />
</Frame>

<Note>
  Don't close your account with your old carrier until the porting process is complete. Keep your numbers active to avoid downtime.
</Note>

## Port request statuses

| Status          | Description                  | Action                            |
| --------------- | ---------------------------- | --------------------------------- |
| Submitted       | Request received             | Wait for carrier processing       |
| Approved        | Carrier accepted             | Wait for FOC date                 |
| Completed       | Successfully ported          | Number is active on Plivo         |
| Rejected        | Request denied               | Review rejection reason, resubmit |
| Update Required | Information needs correction | Plivo will contact you            |

## What happens after submission

If all details and documents are acceptable, Plivo submits the porting request to the gaining carrier. This takes about a day.

The gaining carrier verifies the request and forwards it to the losing carrier. The request shows as pending while the losing carrier processes it (5-20 business days).

Once processed, you'll receive a status update:

* **Approved**: Plivo receives a Firm Order Commitment (FOC) with the porting date
* **Update Required**: Plivo contacts you to re-submit corrected information
* **Rejected**: Plivo explains the rejection so you can resubmit with correct details

## FOC/porting date

Plivo sends you an email with your porting date and adds the numbers to your account two days before the FOC.

Have your application set up and ready before the FOC date to avoid service interruption. You can configure numbers at **Phone Numbers > Port-In > Configure Number**.

## Handling rejected requests

### Common rejection reasons

| Reason                                   | Solution                                    |
| ---------------------------------------- | ------------------------------------------- |
| **Data mismatch**                        | Update LOA to match carrier records exactly |
| **Name mismatch**                        | Verify name with current carrier            |
| **Address mismatch**                     | Use address from carrier's CSR              |
| **Unsatisfactory business relationship** | Pay outstanding balance to current carrier  |
| **Number not portable**                  | Contact Plivo support                       |

### How to fix and resubmit

1. Review the rejection reason in the console or email
2. Correct the issue (usually LOA information mismatch)
3. Submit a new port request with corrected information

For more details on rejection reasons, see [this guide](https://support.plivo.com/hc/en-us/articles/360041880011).

### Escalating port-in issues

If your port request is stuck or you're experiencing issues that require carrier intervention:

1. **Contact Plivo Support** at [support.plivo.com](https://support.plivo.com) with:
   * Your port request ID
   * Phone number(s) affected
   * Description of the issue
   * Any error messages received

2. **Plivo's porting team** will:
   * Review your request status with the carrier
   * Escalate to the carrier's porting department if needed
   * Provide updates on resolution timeline

<Note>
  Plivo cannot directly contact carriers on your behalf for account-specific issues (like outstanding balances). You may need to resolve these with your current carrier before resubmitting.
</Note>

## Cancel a port request

Before carrier acceptance:

1. Navigate to Port-In orders in console
2. Select the order
3. Click **Cancel**

No cancellation fee applies before carrier acceptance.

<Note>
  Plivo cannot expedite the porting process as it involves multiple carriers. You can request your current carrier to release the number, which may help speed things up.
</Note>

## Porting numbers out of Plivo

To transfer numbers from Plivo to another carrier:

1. Contact your new carrier and submit a port-in request with your Plivo number(s)
2. New carrier validates and submits port-out request to Plivo's carriers
3. Plivo emails you to confirm the request
4. You authorize or stop the transfer
5. Number transfers on the FOC date

### How to stop or delay a port-out

If you receive a port-out notification and want to stop or delay it:

**To stop a port-out:**

1. Reply to the port-out confirmation email from Plivo
2. Clearly state you want to **reject** the port-out request
3. Include the phone number(s) and reason for rejection

**To delay a port-out:**

1. Contact [Plivo Support](https://support.plivo.com) immediately
2. Provide:
   * Phone number(s) involved
   * Current FOC (porting) date
   * Requested new completion date
   * Reason for delay
3. Plivo will work with the gaining carrier to reschedule

<Warning>
  **Time-sensitive:** Port-out stop/delay requests must be submitted **before the FOC date**. Once the FOC date passes, the port-out cannot be reversed.
</Warning>

### After port-out

* Number loses service with Plivo on FOC date
* Number is removed from your Plivo account
* If you don't respond to the confirmation email, Plivo automatically processes the port-out

## Unauthorized port-out disputes

If a number was ported away without your authorization, contact [Plivo Support](https://support.plivo.com) immediately with:

* Affected phone number(s)
* Reason for dispute
* Signed and dated LOA from the end user confirming intent to retain service

### Dispute timeline

* Disputes must be filed within **30 days**
* Plivo works with carriers to retrieve the number
* Resolution time varies by carrier
