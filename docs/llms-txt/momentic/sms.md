# Source: https://momentic.ai/docs/sms.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS

<Info>**Prerequisites**: A SMS number must be provisioned by Momentic.</Info>

SMS functionality is surfaced through the [JavaScript](/steps/javascript) step.
Within Momentic's JavaScript sandbox, your code can access the `sms` object.
This object contains the following utility functions:

### Sending SMS

The `send` utility function allows you to send an SMS message to a phone number.
The phone number provided in the `from` argument must be issued by Momentic.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
    async function send(params: {
      body: string;
      to: string;
      from: string;
    }): Promise<void>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
    await sms.send({
      body: "Hello world!",
      to: "+14151234567",
      from: "+14159876543"
    });
    ```
  </Tab>
</Tabs>

### Fetching the latest SMS message

<Info>
  Make sure the function timeout is shorter than the JavaScript lambda timeout.
  The default timeout for both is 10 seconds.
</Info>

The `fetchLatest` utility function retrieves the most recent SMS message sent to
your phone number. You can filter messages based on the sender as well as the
receipt date. This function will automatically retry until a matching message is
found or the timeout is exhausted.

If multiple new SMS messages are received, only the most recently received
message will be returned. To avoid race conditions, we recommend structuring
your tests so that only a single SMS flow is active at any given time for each
phone number allocated.

If you do not filter by receipt date, `fetchLatest` can return messages that
were received before your test started (i.e. data generated from previous test
runs).

`fetchLatest` will throw an error if no matching SMS message is received within
the timeout.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
    async function fetchLatest(params: {
      to: string;
      from?: string;
      beforeDate?: Date;
      afterDate?: Date;
      timeout?: number; // milliseconds
    }): Promise<{ body: string }>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
    const { body } = await sms.fetchLatest({
      to: "+14151234567",
      from: "+14159876543"
      afterDate: new Date(), // only fetch messages received after this call starts
      timeout: 30000, // 30 seconds
    });
    // use regex to extract link from message body
    const link = body.match(/https?:\/\/[^\s]+/)[0];
    return link;
    ```
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).