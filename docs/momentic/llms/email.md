# Source: https://momentic.ai/docs/email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Email

<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Momentic supports sending and receiving emails to and from allocated
`@usemomentic.com` or `@gomomentic.com` addresses.

Email functionality is surfaced through the [JavaScript](/steps/javascript)
step. Within Momentic's JavaScript sandbox, your code can access the `email`
object. This object contains the following utility functions:

## Sending emails

The `send` utility function allows you to send an email to an inbox. The inbox
provided in the `from` argument must be issued by Momentic.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
      async function send(params: {
        subject: string;
        body: string;
        to: string;
        from: string;
      }): Promise<void>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
      await email.send({
        subject: "Hello",
        body: "Hello world!",
        to: "momentic+test@gomomentic.com",
        from: "momentic"
      });
    ```
  </Tab>
</Tabs>

## Fetching the latest email

<Info>
  Make sure the function timeout is shorter than the JavaScript lambda timeout.
  The default timeout for both is 10 seconds.
</Info>

The `fetchLatest` utility function retrieves the most recent email received.
Optionally, you can filter for emails sent after a particular date. This can be
useful for ensuring that you are not reading stale emails that were received
before the test began.

This function will automatically retry until a matching email is found or the
timeout is exhausted. If no email is received within the timeout, an error is
thrown.

If an email is received, the text content of the email will be available in the
`text` field of the result. When `trimWhitespace` is true, which is the default
behavior, adjacent whitespace characters will be combined to make the text
easier to read and parse in future steps. If the email contains HTML content,
the raw HTML will be provided in the `html` field.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
    async function fetchLatest(params: {
      inbox: string, // inbox name allocated by momentic
      afterDate?: Date,
      timeout?: number,
      trimWhitespace: boolean = true,
    }): Promise<Email>;

    type Email = {
      subject: string; // subject line
      from: string; // sender's name and email
      fromEmail: string; // sender's email address
      to: string; // recipient's name and email address (the email address allocated to your organization)
      time: number; // unix timestamp for when the email was received
      secondsAgo: number; // how many seconds ago the email was received
      size: number | undefined; // size of the email in bytes

      text: string; // the text content of the email. if trimWhitespace is true, adjacent whitespace characters will be combined
      html: string | undefined; // if the email has HTML content, this field will contain the raw HTML
    };
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
    const msg = await email.fetchLatest({
      inbox: "jeff+test",
      afterDate: new Date(),
      timeout: 20_000,
    });

    return msg.text;
    ```
  </Tab>
</Tabs>

## Fetching all emails

The `fetchAll` utility function retrieves all recently received emails. You can
filter for emails received after a certain date and set a limit on the number of
emails returned. By default, these parameters are set to 15 minutes ago and 3
emails; the maximum allowed values are 24 hours and 10 emails.

This function runs instantaneously and does not retry or poll until an email
exists. As such, it is the responsibility of the caller to ensure that the email
they are interested in is already delivered by the time this function is
invoked. If no emails exist in the inbox, the function will throw an error.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
    async function fetchAll(params: {
      inbox: string, // inbox name allocated by momentic
      afterDate?: Date,
      limit?: number,
      trimWhitespace: boolean = true,
    }): Promise<Email[]>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
    const msgs = await email.fetchAll({
      inbox: "jeff+test",
      afterDate: new Date(Date.now() - 60 * 1000),
      limit: 5,
    });

    return msgs.filter((msg) => msg.text.includes("verification code"))
    ```
  </Tab>
</Tabs>

## Creating isolated inboxes

Once you are allocated unique username from Momentic, you can create unlimited,
isolated inboxes accessible from your organization by appending a suffix to the
username. For example, if your unique username is `momentic`, you can also send
emails to `momentic+test@usemomentic.com` and fetch results using the
`momentic+test` inbox name.

We recommend using this strategy with a randomized suffix such as `Date.now()`
when running multiple tests in parallel that require email access to prevent
race conditions.


Built with [Mintlify](https://mintlify.com).