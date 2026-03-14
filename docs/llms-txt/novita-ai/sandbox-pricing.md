# Source: https://novita.ai/docs/guides/sandbox-pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing

Agent Sandbox supports independent billing for CPU and RAM (memory) by the second, with on-demand usage and flexible billing.

## Billing Items

<table class="table table-big">
  <thead>
    <tr>
      <th style={{ minWidth: '80px' }}>Billing Item</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>CPU</td>
      <td>Billed based on the number of vCPU cores used and usage duration (accurate to the second). Current pricing can be found on the [here](https://novita.ai/pricing?sandbox=1). No billing occurs after the Sandbox is stopped.</td>
    </tr>

    <tr>
      <td>RAM (memory)</td>
      <td>Billed based on allocated memory capacity and usage duration (accurate to the second). Current pricing can be found on the [here](https://novita.ai/pricing?sandbox=1). No billing occurs after the Sandbox is stopped.</td>
    </tr>

    <tr>
      <td><Link href="/guides/sandbox-filesystem" target="_blank">Storage</Link></td>
      <td>Current pricing can be found on the [here](https://novita.ai/pricing?sandbox=1).</td>
    </tr>

    <tr>
      <td><Link href="/guides/sandbox-template" target="_blank">Templates</Link></td>
      <td>Currently free.</td>
    </tr>
  </tbody>
</table>

## Pricing

* **CPU**

<table class="table table-big">
  <thead>
    <tr>
      <th>vCPUs (cores)</th>
      <th>Unit Price</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>1</td>
      <td>\$0.0000098/s</td>
    </tr>

    <tr>
      <td>2</td>
      <td>\$0.0000196/s</td>
    </tr>

    <tr>
      <td>3</td>
      <td>\$0.0000294/s</td>
    </tr>

    <tr>
      <td>4</td>
      <td>\$0.0000392/s</td>
    </tr>

    <tr>
      <td>5</td>
      <td>\$0.000049/s</td>
    </tr>

    <tr>
      <td>6</td>
      <td>\$0.0000588/s</td>
    </tr>

    <tr>
      <td>7</td>
      <td>\$0.0000686/s</td>
    </tr>

    <tr>
      <td>8</td>
      <td>\$0.0000784/s</td>
    </tr>
  </tbody>
</table>

* **RAM (memory)**

<table class="table table-big">
  <thead>
    <tr>
      <th>Memory (MiB)</th>
      <th>Unit Price</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Valid values: multiples of 512 MiB, from 512 MiB to 8192 MiB</td>
      <td>\$0.0000032/GiB/s</td>
    </tr>

    <tr>
      <td>512 MiB</td>
      <td>\$0.0000016/s</td>
    </tr>

    <tr>
      <td>1 GiB</td>
      <td>\$0.0000032/s</td>
    </tr>

    <tr>
      <td>2 GiB</td>
      <td>\$0.0000064/s</td>
    </tr>
  </tbody>
</table>

* **Storage**

<table class="table table-big">
  <thead>
    <tr>
      <th>Memory (MiB)</th>
      <th>Unit Price</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Each account includes 60 GB of free storage. Usage beyond this limit is billed on a pay-as-you-go basis.</td>
      <td>\$0.00009/GB/h</td>
    </tr>
  </tbody>
</table>

## Get Bills

You can view and export Agent Sandbox bills in <u>"Billing - Billing Details - Usage-based Billing"</u>.

* Go to the <Link href="https://novita.ai/billing/details" target="_blank">billing details page</Link>;
* Select the "Usage-based Billing" tab on the right, then click the "Agent Sandbox" secondary tab below;
* You can set the "Time Range" and "Group By" filters;
* You can click "Export" button after querying to export bill data as an .xlsx file.

## Overdue Payment Notice

If the account's available balance (including available balance and voucher balance) is less than the bill to be paid, the account is considered overdue. Overdue payments will result in sandboxes being terminated and data loss, affecting your service. During usage, please ensure sufficient account balance. After overdue, the system will send relevant notification emails, please recharge promptly.

You can confirm account balance and vouchers on the <Link href="https://novita.ai/billing" target="_blank">payments</Link> page, recharge as needed.

<Warning>
  To avoid overdue payments affecting your service, it is recommended that you set up <Link href="https://novita.ai/billing/balance-warning" target="_blank">low balance alerts</Link>. When your account balance is less than the alert threshold you set, an notification email will be sent.
</Warning>

The specific **overdue payment impacts** are as follows:

* Unable to start new sandboxes.
* Running sandboxes will be terminated.


Built with [Mintlify](https://mintlify.com).