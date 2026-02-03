# Source: https://loops.so/docs/smtp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send with SMTP

> Send Loops emails over SMTP.

You can send transactional emails over SMTP, meaning you can use Loops to power emails in platforms like Supabase and development tools and frameworks like Laravel, Rails, Django and Nodemailer.

## How it works

The Loops way of sending emails over SMTP is a bit different from other services.

<Steps>
  <Step title="Create emails in Loops">
    First, you create transactional email templates in [the Loops editor](/creating-emails/editor) for the emails you want to send.

    Our rich editor helps you create beautiful, client-compatible *and* easy-to-update emails rather than hand-coding them.
  </Step>

  <Step title="Send emails from your application">
    Use these SMTP settings in your application:

    | Field       | Value                                                                                      |
    | ----------- | ------------------------------------------------------------------------------------------ |
    | Host        | `smtp.loops.so`                                                                            |
    | Port number | `587`                                                                                      |
    | Username    | `loops`                                                                                    |
    | Password    | An API key copied from your [API settings](http://app.loops.so/settings?page=api) in Loops |

    Then, when it comes to sending emails, instead of the content of an email, you send an API-like request body like this:

    ```json  theme={"dark"}
    {
      "transactionalId": "clomzp89u035xl50px7wrl0ri",
      "email": "dan@loops.so",
      "dataVariables": {
        "confirmationUrl": "https://myapp.com/confirm/12345/"
      }
    }
    ```

    This content **needs to be converted to a string** and then sent as the email body.

    Loops takes the provided data and compiles an email using the template you specify in the `transactionalId` value plus the provided `dataVariables`, then sends the email to `email`.
  </Step>
</Steps>

<Warning>
  Every email sent using Loops' SMTP service requires a transactional email to be set up in your Loops account. Note the `transactionalId` value in the email payload.
</Warning>

## SMTP Integrations

Learn how to set up SMTP in platforms and developer tools.

### Integrations

<CardGroup>
  <Card
    title="Auth0"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 256 285"><path fill="#FF4A00" d="M220.412 0h-92.415l28.562 89.006h92.416l-74.77 53.077 28.57 89.511c48.128-35.06 63.854-88.12 46.208-142.588L220.413 0ZM7.018 89.006h92.416L127.997 0H35.589L7.019 89.006c-17.655 54.468-1.92 107.529 46.207 142.588l28.563-89.51-74.77-53.078Zm46.208 142.588 74.77 52.97 74.77-52.97-74.77-53.847-74.77 53.847Z"/></svg>
  }
    href="/integrations/auth0"
  >
    Send Auth0 authentication emails with Loops.
  </Card>

  <Card
    title="Novu"
    icon={
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" class="h-6" viewBox="0 0 102 32"><path fill="#FF4A00" fill-rule="evenodd" d="M24.64 12.826c0 .86-1.044 1.286-1.646.671L10.676.907A16 16 0 0 1 16 0c3.183 0 6.148.93 8.64 2.531zm4.48-5.986v5.986c0 4.875-5.919 7.289-9.328 3.804L6.545 3.091C2.576 6.003 0 10.701 0 16c0 3.407 1.065 6.565 2.88 9.16v-5.954c0-4.875 5.919-7.289 9.328-3.804l13.229 13.52A15.976 15.976 0 0 0 32 16c0-3.407-1.065-6.565-2.88-9.16M9.006 18.535 21.301 31.1c-1.659.583-3.443.9-5.301.9-3.182 0-6.148-.93-8.64-2.531V19.206c0-.86 1.045-1.286 1.646-.671" clip-rule="evenodd"/><path fill="#FF4A00" fill-rule="evenodd" d="M24.64 12.826c0 .86-1.044 1.286-1.646.671L10.676.907A16 16 0 0 1 16 0c3.183 0 6.148.93 8.64 2.531zm4.48-5.986v5.986c0 4.875-5.919 7.289-9.328 3.804L6.545 3.091C2.576 6.003 0 10.701 0 16c0 3.407 1.065 6.565 2.88 9.16v-5.954c0-4.875 5.919-7.289 9.328-3.804l13.229 13.52A15.976 15.976 0 0 0 32 16c0-3.407-1.065-6.565-2.88-9.16M9.006 18.535 21.301 31.1c-1.659.583-3.443.9-5.301.9-3.182 0-6.148-.93-8.64-2.531V19.206c0-.86 1.045-1.286 1.646-.671" clip-rule="evenodd"/><path fill="#FF4A00" fill-rule="evenodd" d="M24.64 12.826c0 .86-1.044 1.286-1.646.671L10.676.907A16 16 0 0 1 16 0c3.183 0 6.148.93 8.64 2.531zm4.48-5.986v5.986c0 4.875-5.919 7.289-9.328 3.804L6.545 3.091C2.576 6.003 0 10.701 0 16c0 3.407 1.065 6.565 2.88 9.16v-5.954c0-4.875 5.919-7.289 9.328-3.804l13.229 13.52A15.976 15.976 0 0 0 32 16c0-3.407-1.065-6.565-2.88-9.16M9.006 18.535 21.301 31.1c-1.659.583-3.443.9-5.301.9-3.182 0-6.148-.93-8.64-2.531V19.206c0-.86 1.045-1.286 1.646-.671" clip-rule="evenodd"/></svg>
  }
    href="/integrations/novu"
  >
    Send Novu notification emails with Loops.
  </Card>

  <Card
    title="Supabase"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      fill="none"
      viewBox="0 0 109 113"
    >
      <path
        fill="url(#a)"
        d="M63.708 110.284c-2.86 3.601-8.658 1.628-8.727-2.97l-1.007-67.251h45.22c8.19 0 12.758 9.46 7.665 15.874l-43.151 54.347Z"
      />
      <path
        fill="url(#b)"
        fillOpacity=".2"
        d="M63.708 110.284c-2.86 3.601-8.658 1.628-8.727-2.97l-1.007-67.251h45.22c8.19 0 12.758 9.46 7.665 15.874l-43.151 54.347Z"
      />
      <path
        fill="#ffbca6"
        d="M45.317 2.071c2.86-3.601 8.657-1.628 8.726 2.97l.442 67.251H9.83c-8.19 0-12.759-9.46-7.665-15.875L45.317 2.072Z"
      />
      <defs>
        <linearGradient
          id="a"
          x1="53.974"
          x2="94.163"
          y1="54.974"
          y2="71.829"
          gradientUnits="userSpaceOnUse"
        >
          <stop stopColor="#FF4A00" />
          <stop offset="1" stopColor="#ffbca6" />
        </linearGradient>
        <linearGradient
          id="b"
          x1="36.156"
          x2="54.484"
          y1="30.578"
          y2="65.081"
          gradientUnits="userSpaceOnUse"
        >
          <stop />
          <stop offset="1" stopOpacity="0" />
        </linearGradient>
      </defs>
    </svg>
  }
    href="/smtp/supabase"
  >
    Send Supabase authentication emails with Loops.
  </Card>
</CardGroup>

### Frameworks

<CardGroup>
  <Card title="Django" icon={<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path fill="#FF4A00" d="M14.859 0h5.234v24.219c-2.682.51-4.656.714-6.797.714-6.385 0-9.714-2.885-9.714-8.427 0-5.333 3.531-8.797 9-8.797.849 0 1.495.068 2.276.271zm0 12.193a5.225 5.225 0 0 0-1.766-.276c-2.651 0-4.177 1.63-4.177 4.49 0 2.786 1.458 4.313 4.146 4.313.578 0 1.052-.031 1.797-.135v-8.396zm13.558-4.115v12.13c0 4.177-.302 6.188-1.219 7.917-.849 1.667-1.974 2.719-4.281 3.875l-4.859-2.313c2.307-1.089 3.432-2.036 4.146-3.5.745-1.495.984-3.229.984-7.781V8.078zM23.188.026h5.229v5.37h-5.229z"/></svg>} href="/smtp/django">
    Send transactional emails from your Django project.
  </Card>

  <Card title="Laravel" icon="laravel" href="/smtp/laravel">
    Send transactional emails from your Laravel project.
  </Card>

  <Card title="Ruby on Rails" icon={<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 200 122.179"><g fill="#FF4A00" fill-rule="evenodd"><path d="M6.226 122.179h69.646s-13.312-61.028 30.767-85.74c9.61-4.695 40.2-22.233 90.275 14.968 1.587-1.328 3.086-2.391 3.086-2.391s-45.843-45.97-96.887-40.833c-25.655 2.303-57.216 25.775-75.73 56.776C8.87 95.961 6.227 122.18 6.227 122.18Z"/><path d="M6.226 122.179h69.646s-13.312-61.028 30.767-85.74c9.61-4.695 40.2-22.233 90.275 14.968 1.587-1.328 3.086-2.391 3.086-2.391s-45.843-45.97-96.887-40.833c-25.655 2.303-57.216 25.775-75.73 56.776C8.87 95.961 6.227 122.18 6.227 122.18Z"/><path d="M6.226 122.179h69.646S62.56 61.441 106.639 36.846c9.61-4.673 40.2-22.127 90.275 14.898a54.832 54.832 0 0 1 3.086-2.38S154.157 3.61 103.113 8.724C77.37 11.016 45.809 34.377 27.296 65.231 8.782 96.085 6.226 122.18 6.226 122.18Zm145.11-108.518.353-5.906c-.794-.441-2.998-1.499-8.552-3.086l-.352 5.818c2.909.97 5.73 2.028 8.551 3.174Z"/><path d="m143.016 32.845-.352 5.547a49.29 49.29 0 0 1 8.734 1.057l.353-5.46c-3-.616-5.911-.968-8.735-1.144ZM110.372 5.37h.883L109.49 0c-2.735 0-5.558.176-8.47.528l1.677 5.196c2.558-.265 5.117-.353 7.675-.353Zm4.235 32.405 2.03 6.076c2.558-1.233 5.117-2.29 7.675-3.082l-1.94-5.812c-3 .88-5.559 1.85-7.765 2.818ZM74.552 14.617l-3.97-6.076c-2.206 1.145-4.5 2.378-6.882 3.787l4.059 6.164c2.293-1.41 4.5-2.73 6.793-3.875ZM92.64 54.243l4.235 6.34c1.5-2.202 3.264-4.227 5.205-6.252l-3.97-5.988a48.751 48.751 0 0 0-5.47 5.9ZM79.846 82.597l7.146 5.635a70.2 70.2 0 0 1 1.853-10.302l-6.352-5.02c-1.147 3.259-1.941 6.517-2.647 9.687ZM41.202 40.77l-6.264-5.46c-2.294 2.202-4.5 4.403-6.529 6.605l6.794 5.811a89.226 89.226 0 0 1 6-6.956ZM14.558 80.131 4.41 76.433C2.735 80.219.882 84.622 0 86.999l10.146 3.699c1.147-2.994 3-7.309 4.412-10.567Zm63.964 24.832c.177 4.667.618 8.453 1.059 11.095l10.587 3.786c-.794-3.434-1.588-7.308-2.117-11.447l-9.529-3.434Z"/></g></svg>} href="/smtp/rails">
    Send transactional emails from your Rails project.
  </Card>
</CardGroup>
