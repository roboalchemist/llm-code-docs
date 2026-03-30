# Source: https://www.ory.com/docs/kratos/emails-sms/custom-email-templates

Title: Customize message templates for Ory Identity emails | Ory

URL Source: https://www.ory.com/docs/kratos/emails-sms/custom-email-templates

Markdown Content:
Email templates
---------------

Ory Identities comes with built-in templates for all messages sent by the system. You can replace the default templates with custom ones that can carry your own branding, visual elements, and communication tone.

Built-in templates[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#built-in-templates "Direct link to Built-in templates")
-----------------------------------------------------------------------------------------------------------------------------------------------

*   Account recovery
*   Address verification
*   Login code
*   Registration code

When you set the account verification method to `code`, the system uses the `recovery_code.valid` template to send the recovery code to the user.

If you enabled sending attempted recovery notifications to unregistered addresses, the system uses the `recovery_code.invalid` template.

If you set the account recovery method to `link`, the system uses these templates instead:

*   `recovery.valid`
*   `recovery.invalid`

To learn more about the recovery flow, read [Account recovery and password reset](https://www.ory.com/docs/kratos/self-service/flows/account-recovery-password-reset).

Using custom message templates[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#using-custom-message-templates "Direct link to Using custom message templates")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Templates can be customized to fit your own branding and requirements. If you don't customize a specific template, the system automatically uses the built-in template.

A custom email server is required to use custom templates. Read more about [custom SMTP and HTTP servers](https://www.ory.com/docs/kratos/emails-sms/sending-emails-smtp).

*   Ory Console
*   Ory CLI

1.   Go to **Branding** → **Email templates** in the [Ory Console](https://console.ory.sh/projects/current/email-templates)
2.   Select the email template you want to customize.

The recovery & verification templates only show the versions for the method (**one-time code** or **link**) you have selected in the flow configuration.

*   **Authentication** → **Account recovery** in the [Ory Console](https://console.ory.sh/projects/current/authentication/recovery)
*   **Authentication** → **Account verification** in the [Ory Console](https://console.ory.sh/projects/current/authentication/verification)

Creating templates[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#creating-templates "Direct link to Creating templates")
-----------------------------------------------------------------------------------------------------------------------------------------------

Templates use the Go template engine in the `text/template` package for rendering the `email.subject.gotmpl` and `email.body.plaintext.gotmpl` templates, and the `html/template` package for rendering the `email.body.gotmpl` template.

Learn more:

*   [https://pkg.go.dev/text/template](https://pkg.go.dev/text/template)
*   [https://pkg.go.dev/html/template](https://pkg.go.dev/html/template)

tip

danger

For security reasons, these Sprig functions are disabled in the Ory Network:

*   Date functions: `date`,`date_in_zone`,`date_modify`, `now`, `htmlDate`, `htmlDateInZone`, `dateInZone`, `dateModify`
*   Strings: `randAlphaNum`, `randAlpha`, `randAscii`, `randNumeric`, `uuidv4`
*   OS: `env`, `expandenv`
*   Network: `getHostByName`

### Available variables[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#available-variables "Direct link to Available variables")

The variables available for use in email templates change depending on the flow and the selected method:

*   Recovery (via code)
*   Verification (via code)
*   Recovery (via magic link)
*   Verification (via magic link)
*   Login (via code)
*   Registration (via code)

For the `recovery_code.valid` template, the following variables are available:

| Variable | Description |
| --- | --- |
| `To` | The email address the email will be sent to |
| `RecoveryCode` | The recovery code |
| `Identity` | The identity to be recovered |
| `ExpiresInMinutes` | the expiration time of the code in minutes |

note

The `recovery_code.invalid` template does not allow to send a direct link to the user, as the recovery flow enforces anti-CSRF measures, which would lead to the flow failing, in case the user opens the link in a different browser.

For the `recovery_code.invalid` template, the following variables are available:

| Variable | Description |
| --- | --- |
| `To` | the email address the email will be sent to |

### Mandatory template formats[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#mandatory-template-formats "Direct link to Mandatory template formats")

Each template must have two versions: `html` and `plaintext`.

*   `html` version uses the HTML syntax to achieve the desired look and functionality (such as clickable buttons) of the email message.
*   `plaintext` version can't contain any HTML. Must contain only plain text content and any necessary `gotmpl` logic. This version is used as a fallback when the `html` version cannot be delivered, for example when the user's mail server blocks HTML in all incoming messages.

*   HTML
*   Plain text

courier/template/templates/verification/valid/email.body.gotmpl

`Hi, please verify your account by clicking the following link:<a href="{{ .VerificationURL }}">{{ .VerificationURL }}</a>`

Customizing template content for specific users[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#customizing-template-content-for-specific-users "Direct link to Customizing template content for specific users")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To enable customizing the content of templates based on the identity of the recipient of the email, the `Identity` object is available inside the templates. This object is a map containing all the attributes of an identity defined in the identity schema, such as `id`, `state`, `recovery_addresses`, `verifiable_addresses` and `traits`.

tip

Read [this document](https://www.ory.com/docs/kratos/manage-identities/overview) to learn more about the Ory Identity and the identity schema.

### Translated templates (i18n)[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#translated-templates-i18n "Direct link to Translated templates (i18n)")

You can use nested templates to render `email.subject.gotmpl`, `email.body.gotmpl` and `email.body.plaintext.gotmpl` templates based on user settings, for example based on their chosen language.

To enable i18n customization of templates, customize the identity schema to include the user's preferred communication language. For example:

Sample custom Identity Schema with user language

`{  // ...  "properties": {    "traits": {      "type": "object",      "properties": {        // ...        "lang": {          "type": "string",          "title": "Your preferred language"      },      "required": [        "email"      ],      "additionalProperties": false,    }  }}`

This identity trait can then be used inside the template to render a section conditionally.

The following example defines various templates for the `recovery_code.valid` template and renders the respective template depending on the language set in the `lang` identity traits, that was defined above:

recovery_code/valid/email.body.gotmpl

`{{define "en"}}Hi,Please enter the following code to recover your account:{{ .RecoveryCode }}{{end}}{{define "fr"}}Bonjour,Veuillez entrer le code suivant pour récupérer votre compte:{{ .RecoveryCode }}{{end}}{{define "de"}}Hallo,Bitte geben Sie den folgenden Code ein, um Ihr Konto wiederherzustellen:{{ .RecoveryURL }}{{end}}{{- else if eq .Identity.traits.lang "fr" -}}{{ template "fr" . }}{{- else if eq .Identity.traits.lang "de" -}}{{ template "de" . }}{{- else -}}{{ template "en" . }}{{- end -}}`

tip

You can use Sprig functions in the nested templates. For security reasons, some functions are disabled in the Ory Network. [See the list of disabled functions here.](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#creating-templates)

### Metadata in templates[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#metadata-in-templates "Direct link to Metadata in templates")

As an administrator, you can set identity metadata, such as the user's language, in your application code using Identity metadata property. Read [this document](https://www.ory.com/docs/kratos/manage-identities/managing-users-identities-metadata#metadata) to learn more.

You can access `metadata_public` through `.Identity.metadata_public` in email templates.

The following example requires that the field `lang` is set in the public metadata. Your application could set this value after user completes registration.

recovery_code/valid/email.body.gotmpl

`{{define "en"}}Hi,Please enter the following code to recover your account:{{ .RecoveryCode }}{{end}}{{define "fr"}}Bonjour,Veuillez entrer le code suivant pour récupérer votre compte:{{ .RecoveryCode }}{{end}}{{define "de"}}Hallo,Bitte geben Sie den folgenden Code ein, um Ihr Konto wiederherzustellen:{{ .RecoveryURL }}{{end}}{{- if eq .Identity.metadata_public.lang "fr" -}}{{ template "fr" . }}{{- else if eq .Identity.metadata_public.lang "de" -}}{{ template "de" . }}{{- else -}}{{ template "en" . }}{{- end -}}`

danger

Since metadata is not validated by Ory Identities, missing entries or unexpected values can cause errors in the template rendering process. If the system encounters errors in the rendering process, Ory Identities uses the default templates.

### Transient payload in templates[​](https://www.ory.com/docs/kratos/emails-sms/custom-email-templates#transient-payload-in-templates "Direct link to Transient payload in templates")

The transient payload allows you to pass additional data along with certain self-service flows. Transient payloads can be used for passing temporary information to your email template without storing it permanently.

The following `example_key` transient payload

`...    traits: {      email: "user@example.com",    },    transient_payload: {      example_key: "This is an example value"    },...`

can be accessed in the email template using `{{index .TransientPayload "example_key"}}`

`<h1>Recovery Details</h1><p>To: {{.To}}</p><p>Recovery URL: {{.RecoveryURL}}</p><p>Transient Payload: {{index .TransientPayload "example_key"}}</p><p>  {{- if eq (index .TransientPayload "lang") "foo" -}}  FOO  {{- else -}}  BAR  {{- end -}}</p>`

This results into the following email to be sent to the user.

`<h1>Recovery Details</h1><p>To: user@example.com</p><p>Recovery URL: https://example.com/recover</p><p>Transient Payload: This is an example value</p><p>  BAR</p>`
