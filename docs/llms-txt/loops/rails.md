# Source: https://loops.so/docs/smtp/rails.md

# Ruby on Rails

> Send transactional emails from your Rails project using Loops' SMTP service.

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

Here's how you can set up transactional emails with Loops SMTP in Rails:

<Steps>
  <Step title="Create emails in Loops">
    Create transactional emails in Loops using the [editor](/creating-emails/editor).

    Add [data variables](/transactional#add-data-variables) to your emails for any dynamic content you want to send from your Rails application.

        <img src="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=d124653cd87536765f40e4de3102c15a" alt="Add a data variable" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=280&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=1c1834773261e5a0c8be7a0e1b4191a5 280w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=560&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=5e9e0bae89a5aded6a9d7448926ff5a8 560w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=840&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=40030ce29b5df99adb0c950877a84baa 840w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1100&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=7712e06a02cfeedd04e43aef5024c6eb 1100w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1650&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=cbcbd72414a41dc5717a61b867789fbe 1650w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=2500&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=3a8450a5d3357e016e9b562574bd68fe 2500w" />
  </Step>

  <Step title="Configure Action Mailer">
    To use Loops SMTP, configure Action Mailer using the following settings.

    <Tip>
      The `password` value should be an API key from your [API Settings](http://app.loops.so/settings?page=api) page.
    </Tip>

    ```ruby config/environments/production.rb theme={"dark"}
    config.action_mailer.delivery_method = :smtp
    config.action_mailer.smtp_settings = {
      address:         'smtp.loops.so',
      port:            587,
      user_name:       'loops',
      password:        '<API_KEY>',
      authentication:  'plain',
      enable_starttls: true
    }
    ```
  </Step>

  <Step title="Send emails from Rails">
    Now you can send emails from your application.

    Here's an example Mailer:

    ```ruby app/mailers/user_mailer.rb theme={"dark"}
    class UserMailer < ApplicationMailer

      def login_email
        @user = params[:user]
        # Note: the "to" address is required by Action Mailer
        #  but is overwritten by the email provided in the view
        #  (see below). Likewise, a subject is not required here
        #  because Loops will use the subject provided in the editor.
        mail(to: @user.email)
      end

    end
    ```

    Loops' SMTP system doesn't send full HTML emails directly. Instead, you should provide a structured API-like payload, which Loops will then use to render an HTML email.

    Create a text view for your email, like below.

    You can copy an example payload from the **Publish** page of your transactional email in Loops.

    ```json app/views/user_mailer/login_email.text.erb theme={"dark"}
    {
      "transactionalId": "clomzp89u635xl30px7wrl0ri",
      "email": "<%= @user.email %>", /* recipient */
      "dataVariables": {
        "loginUrl": "https://myapp.com/login?code=<%= @user.auth_code %>"
      }
    }
    ```

    <Tip>You do not need to provide an HTML view for your emails when using Loops SMTP (i.e.: `login_email.html.erb` is not required).</Tip>
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
