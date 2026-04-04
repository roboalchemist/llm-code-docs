# Source: https://getlago.com/docs/guide/invoicing/export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Export invoices

> Lago enables you to filter invoices and export them as a simple or advanced CSV file, tailored to your needs.

## Invoice filtering options

With Lago, filtering your invoice list is straightforward and customizable. To filter invoices effectively, follow these steps:

1. Go to the **Invoices** section;
2. **Use quick filters** for fast, predefined filtering;
3. Select the **Filters options** for more advanced filtering criteria; and
4. Click **Reset filters** to remove all active filters when needed.

<Frame caption="Invoices filtering options">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=ff67baaca7861289030ad5d3c3351e11" data-og-width="2884" width="2884" data-og-height="1274" height="1274" data-path="guide/invoicing/images/filters-and-quick-filters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=5cf0347d55f84143ffcdd59488c914c0 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=e673537557afe234c785b75c2944b0c2 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=efdac7be4cdc82c2022fb368675c34c6 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=8905edc546861ddd7532f757d80f0195 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9e51355b7e1768ae53652860c3afab92 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/filters-and-quick-filters.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=58b3b40d328cb28cf9dd0ebc18cbd540 2500w" />
</Frame>

Here is the list of filter options you will encounter in Lago:

* **Amount:** Filter invoices by amount;
* **Currency:** Filter invoices based on the currency in which they are issued;
* **Customer:** Filter by the customer associated with the invoices;
* **Disputed:** Filter invoices to show only those that are disputed or undisputed;
* **Issuing Dates:** Filter invoices by their issuing dates;
* **Overdue:** Filter to display only overdue invoices;
* **Payment Status:** Filter invoices by their payment status;
* **Status:** Filter invoices by their status;
* **Type:** Filter invoices by their type;
* **Billing entity:** Filter invoice by their billing entity; and
* **Metadata:** Filter invoices by their metadata (API option only).

## Basic invoices export

The first option is a basic invoice export. This process generates a CSV file containing one row per invoice, based on the filters you have previously applied.
The exported CSV includes relevant invoice details and is sent to the email address of the user who requested the export.
The download link for the CSV file remains valid for 7 days.

<Frame caption="Basic invoices export in CSV">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=6f3dcad44d362255649459cec8df155c" data-og-width="2890" width="2890" data-og-height="1452" height="1452" data-path="guide/invoicing/images/invoices-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0eea915cadcaee0c4fbff5ad0a2c9b3f 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=ee15e9b570896caa9f87c0ee561f14cb 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c8b72ac4f3661ed68d2c54ff748c15b3 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9b436cb103655993128d723dbebd1b44 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=ced2cea2fd67c5b55e943de6bdb6bff7 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/invoices-export.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=77c62f75e90ba426390eb92f08a54aa3 2500w" />
</Frame>

## Detailed invoice fees export

The second option is an advanced invoice export. This process generates a CSV file containing one row per fee (line item of your invoices),
based on the filters you have previously applied. The exported CSV includes detailed information on each fee and line item of your invoices, and is
sent to the email address of the user who requested the export. The download link for the CSV file is valid for 7 days.

<Frame caption="Advanced invoice fees export in CSV">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=17666e52179aa39408bc5fb75759efc1" data-og-width="2898" width="2898" data-og-height="1550" height="1550" data-path="guide/invoicing/images/fees-export.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=bb93569d052b4fc5073338533bd809bc 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=f4bf3f8d268fcf645fb273c56e7e4268 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=16cad2cbf9c8fb89776c551eea92abc8 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=8ab265c4405f6cd0154622ac98df859f 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=3cbef1ebef8a7901ee27f4c343c9f8d0 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/fees-export.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=28f2929512082ba305a92d507bee09c5 2500w" />
</Frame>

## Filter and export Credit notes[](#filter-and-export-credit-notes "Direct link to heading")

Please note that the `Credit Notes` list can be filtered and exported. The behavior aligns with the functionality defined above based on the credit note fields.
