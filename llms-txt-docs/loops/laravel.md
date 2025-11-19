# Source: https://loops.so/docs/smtp/laravel.md

# Laravel

> Send transactional emails from your Laravel project using Loops' SMTP service.

Transactional emails with Loops simplifies your code. With our WYSIWYG editor and API-like payloads, you can design and manage email templates outside of your codebase, ensuring cleaner code and easier template maintenance.

<Note>
  Unlike older SMTP services, Loops requires the body of emails sent via SMTP to
  be formatted as an [API-like payload](/smtp#how-it-works). This approach
  allows you to use Loops' [powerful email editor](/creating-emails/editor) to
  craft your emails and keep email templating outside of your application code.
</Note>

<Warning>
  Every email sent over Loops SMTP requires a transactional email to be set up
  in your Loops account. Note the `transactionalId` value in the email payload.
</Warning>

Here's how you can set up transactional emails with Loops SMTP in Laravel:

<Steps>
  <Step title="Create emails in Loops">
    Create transactional emails in Loops using the [editor](/creating-emails/editor).

    Add [data variables](/transactional#add-data-variables) to your emails for any dynamic content you want to send from your Laravel application.

        <img src="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=d124653cd87536765f40e4de3102c15a" alt="Add a data variable" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=280&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=1c1834773261e5a0c8be7a0e1b4191a5 280w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=560&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=5e9e0bae89a5aded6a9d7448926ff5a8 560w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=840&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=40030ce29b5df99adb0c950877a84baa 840w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1100&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=7712e06a02cfeedd04e43aef5024c6eb 1100w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1650&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=cbcbd72414a41dc5717a61b867789fbe 1650w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=2500&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=3a8450a5d3357e016e9b562574bd68fe 2500w" />
  </Step>

  <Step title="Add SMTP variables">
    To configure Loops SMTP in your Laravel project, add the following values to your `.env` file.

    <Tip>
      `MAIL_PASSWORD` should be an API key from your [API Settings](http://app.loops.so/settings?page=api) page.
    </Tip>

    ```bash .env theme={"dark"}
    MAIL_MAILER=smtp
    MAIL_HOST=smtp.loops.so
    MAIL_PORT=587
    MAIL_USERNAME=loops
    MAIL_PASSWORD=<API_KEY>
    MAIL_ENCRYPTION=tls
    ```
  </Step>

  <Step title="Send emails from Laravel">
    Now you can send emails from your application.

    If you haven't already, create a mailable class, for example `AuthEmail`:

    ```bash  theme={"dark"}
    php artisan make:mail AuthEmail
    ```

    Loops' SMTP system doesn't send full HTML emails directly. Instead, you should provide a structured API-like payload, which Loops will then use to render an HTML email.

    Create a view for your email, like below.

    You can copy an example payload from the **Publish** page of your transactional email in Loops.

    ```json resources/views/mail/auth-email-text.blade.php theme={"dark"}
    {
      "transactionalId": "clomzp89u635xl30px7wrl0ri",
      "email": "{{ $email }}", /* recipient */
      "dataVariables": {
        "loginUrl": "https://myapp.com/login?code={{ $auth_code }}"
      }
    }
    ```

    Then add a reference to your template in the `Content` definition using the `text` key.

    You also need to pass the values for the recipient email address and any data variables in your email. In this case we are using a `$user` property added to the constructor.

    ```php app/Mail/AuthEmail.php theme={"dark"}
    use App\Models\User;

    class AuthEmail extends Mailable
    {
      /**
       * Create a new message instance.
       */
      public function __construct(
          private User $user,
      ) {}

      /**
       * Get the message content definition.
       */
      public function content(): Content
      {
          return new Content(
              text: 'mail.auth-email-text',
              with: [
                'email' => $this->user->email,
                'auth_code' => $this->user->auth_code,
              ]
          );
      }
    }
    ```

    <Tip>You can omit the `view` option typically required for HTML emails in Laravel. Loops handles HTML rendering using the provided payload.</Tip>

    You can skip adding values to the `Envelope` because the "from" address and subject are all defined within Loops on your transactional email.

    Now you can send transactional emails.

    ```php  theme={"dark"}
    use \App\Mail\AuthEmail;

    Mail::to('anything.here@mail.com')->send(new AuthEmail($user));
    ```

    Note that the email address defined in `to()` will not be used for sending the email even though it's a required parameter. **You have to provide the recipient's email to the template itself**.

    You can read more about sending emails from Laravel [in their docs](https://laravel.com/docs/11.x/mail#writing-mailables).
  </Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Send transactional email" icon="rectangle-terminal" href="/api-reference/send-transactional-email">
    Read how to send transactional email with our API.
  </Card>

  <Card title="Transactional email guide" icon="code" href="/transactional">
    Learn how to send transactional email with Loops.
  </Card>
</CardGroup>
