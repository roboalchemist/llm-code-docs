# Source: https://directus.io/docs/raw/configuration/email.md

# Email

> Configuration for email settings and templates.

<partial content="config-env-vars">



</partial>

## Email Transport

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_VERIFY_SETUP
      </code>
    </td>
    
    <td>
      Check if email setup is properly configured.
    </td>
    
    <td>
      <code>
        true
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_TRANSPORT
      </code>
    </td>
    
    <td>
      What to use to send emails. One of <code>
        sendmail
      </code>
      
      , <code>
        smtp
      </code>
      
      , <code>
        mailgun
      </code>
      
      , <code>
        ses
      </code>
      
      .
    </td>
    
    <td>
      <code>
        sendmail
      </code>
    </td>
  </tr>
</tbody>
</table>

Based on the `EMAIL_TRANSPORT` used, you must also provide additional variables.

### Sendmail

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_SENDMAIL_NEW_LINE
      </code>
    </td>
    
    <td>
      What new line style to use in sendmail.
    </td>
    
    <td>
      <code>
        unix
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SENDMAIL_PATH
      </code>
    </td>
    
    <td>
      Path to your sendmail executable.
    </td>
    
    <td>
      <code>
        /usr/sbin/sendmail
      </code>
    </td>
  </tr>
</tbody>
</table>

### SMTP

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_SMTP_HOST
      </code>
    </td>
    
    <td>
      SMTP server host.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_PORT
      </code>
    </td>
    
    <td>
      SMTP server port.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_USER
      </code>
    </td>
    
    <td>
      SMTP user.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_PASSWORD
      </code>
    </td>
    
    <td>
      SMTP password.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_POOL
      </code>
    </td>
    
    <td>
      Use SMTP pooling.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_SECURE
      </code>
    </td>
    
    <td>
      Enable TLS.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_IGNORE_TLS
      </code>
    </td>
    
    <td>
      Ignore TLS.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SMTP_NAME
      </code>
    </td>
    
    <td>
      SMTP client hostname.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

### Mailgun

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_MAILGUN_API_KEY
      </code>
    </td>
    
    <td>
      Your Mailgun API key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_MAILGUN_DOMAIN
      </code>
    </td>
    
    <td>
      A domain from <a href="https://app.mailgun.com/app/sending/domains" rel="nofollow">
        your Mailgun account
      </a>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_MAILGUN_HOST
      </code>
    </td>
    
    <td>
      Specify a custom host.
    </td>
    
    <td>
      <code>
        api.mailgun.net
      </code>
    </td>
  </tr>
</tbody>
</table>

### AWS SES

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_SES_CREDENTIALS__ACCESS_KEY_ID
      </code>
    </td>
    
    <td>
      Your AWS SES access key ID.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SES_CREDENTIALS__SECRET_ACCESS_KEY
      </code>
    </td>
    
    <td>
      Your AWS SES secret key.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_SES_REGION
      </code>
    </td>
    
    <td>
      Your AWS SES region.
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

## Email Templates

Templates can be used to add custom templates for your emails, or to override the system emails used for things like resetting a password or inviting a user.

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EMAIL_FROM
      </code>
    </td>
    
    <td>
      Email address from which emails are sent.
    </td>
    
    <td>
      <code>
        no-reply@example.com
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EMAIL_TEMPLATES_PATH
      </code>
    </td>
    
    <td>
      Where custom templates are located
    </td>
    
    <td>
      <code>
        ./templates
      </code>
    </td>
  </tr>
</tbody>
</table>

In the `EMAIL_TEMPLATES_PATH`, you can create templates for your emails by adding [`.liquid`](https://liquidjs.com) files.

### Overriding System Emails

There are a number of templates provided by Directus that can be overridden with a custom template:

<table>
<thead>
  <tr>
    <th>
      Template
    </th>
    
    <th>
      File
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Password Reset
    </td>
    
    <td>
      <code>
        password-reset.liquid
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      User Invitation
    </td>
    
    <td>
      <code>
        user-invitation.liquid
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      User Registration
    </td>
    
    <td>
      <code>
        user-registration.liquid
      </code>
    </td>
  </tr>
</tbody>
</table>

When overriding the default email templates, make sure to include the provided `url` somewhere to ensure the email is functional.

## Email Rate Limiting

Emails can be rate limited by opting in to our [email rate limiters](/configuration/security-limits#email-rate-limiting)
