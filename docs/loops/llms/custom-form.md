# Source: https://loops.so/docs/forms/custom-form.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom form

> Integrate with Loops via a form endpoint, which will work with any type of custom form solution you have set up.

Our form endpoint lets you add new contacts to your audience from an HTML form or using JavaScript.

## Find the form endpoint

To submit data to Loops you will need to retrieve the form endpoint URL that's linked to your Loops account.

1. Go to the [Forms page](https://app.loops.so/forms) in your Loops account.
2. Click on the **Settings** tab.
3. Copy the URL shown in the **Form Endpoint** field.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c44978586df98ffbb59edc5208d5fc39" alt="" data-og-width="2280" width="2280" data-og-height="1389" height="1389" data-path="images/form-endpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=fa3193dddf8fc5f6fbb03097e90c28ee 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=97d23f7cf388dd355a93a3cdf4629320 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=48384da872ccdafe15fef4fa521a4748 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=badc4b16efe927447068e6e3610baab6 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=81888b8b2c46441883d70dbc0f662b25 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/form-endpoint.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c04bebe574485c7fef2c7ad5e4b573a8 2500w" />

## Create a form

In a form, add `input` elements for each of the contact properties you want to collect.

The following contact properties can be added to a new contact via a Loops form endpoint:

* Email `email`
* First name `firstName`
* Last name `lastName`
* User group `userGroup`
* Source `source` (default value is "Form" if omitted)
* Notes `notes`
* Mailing list subscriptions ([read more](/forms/custom-form#subscribe-to-mailing-lists))

<Note>
  The only contact property that can be updated on an existing contact via a form endpoint is `userGroup`.\
  Existing contacts can be added to new mailing lists via a form, but not unsubscribed.
</Note>

You can also use any [custom contact properties](/contacts/properties) from your [API settings page](https://app.loops.so/settings?page=api) in your form.

### Add contact properties

For each form field use the "API Name" value found from your [API settings page](https://app.loops.so/settings?page=api) as the `name` attribute.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7a6b9e7ac436c4165e27627b5dffebe4" alt="" data-og-width="3040" width="3040" data-og-height="2026" height="2026" data-path="images/contact-properties-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=320cc5040458c0ac638d1040914d547b 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f50762bb3508c4f86a827e069900078f 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c411dc27f070328066d8c22a42298333 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ae0a96a477d8bd95486f8bc4db3c9022 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=93f4694ddddc419147e67b0ab378217f 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties-table.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cf9358d984a9ccc2d59882912a038532 2500w" />

Here's a simple example form that collects name, email address and assigns a custom user group:

```HTML  theme={"dark"}
<form
  method="post"
  action="https://app.loops.so/api/newsletter-form/<YOUR_FORM_ID>"
>
  <input type="text" name="firstName" required>
  <input type="email" name="email" required>
  <input type="hidden" name="userGroup" value="Website signups">
  <button type="submit">Sign up</button>
</form>
```

### Subscribe to mailing lists

To add subscribers to mailing lists via a form endpoint, include a hidden field called `mailingLists`. You can use a single mailing list ID or to add subscribers to multiple lists, use a comma-separated list of mailing list IDs.

<Warning>
  Make sure that any mailing list you add to a form is
  [Public](/contacts/mailing-lists#list-types). You cannot subscribe contacts to
  private mailing lists from the form endpoint.
</Warning>

```HTML {6} theme={"dark"}
<form
  method="post"
  action="https://app.loops.so/api/newsletter-form/<YOUR_FORM_ID>"
>
  <input type="email" name="email" required>
  <input type="hidden" name="mailingLists" value="cly2xnjbn002z0mme68uog1wk, cly4xnjbn002x0mme28uog1wk">
  <button type="submit">Sign up</button>
</form>
```

<Tip>
  If you need a hand integrating with your custom form, just shoot [help@loops.so](mailto:help@loops.so)
  an email and we'll help you integrate with anything your specific setup ✌️
</Tip>

## Submit with JavaScript

We recommend submitting forms using JavaScript because the endpoint responds with JSON.

To do this, make a `POST` request to your form endpoint. Make sure to set the `Content-Type` header to `application/x-www-form-urlencoded` and to submit the form body with encoded values.

<CodeGroup>
  ```javascript Simple example theme={"dark"}
  function handleSubmit() {
    const formBody = `firstName=${encodeURIComponent(firstName)}&email=${encodeURIComponent(email)}&mailingLists=${encodeURIComponent(mailingListIds)}`;

    // Change this URL to your own endpoint URL
    fetch("https://app.loops.so/api/newsletter-form/<YOUR_FORM_ID>", {
      method: "POST",
      body: formBody,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  }
  ```

  ```javascript Detailed example theme={"dark"}
  function handleSubmit() {
    const formBody = `firstName=${encodeURIComponent(firstName)}&email=${encodeURIComponent(email)}&mailingLists=${encodeURIComponent(mailingListIds)}`;

    try {
      // Change this URL to your own endpoint URL
      const response = await fetch("https://app.loops.so/api/newsletter-form/<YOUR_FORM_ID>", {
        method: "POST",
        body: formBody,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

      if (response.status === 429) {
        // Handle rate limit error
        return {
          success: false,
          message: "Too many signups, please try again in a little while"
        };
      }

      // Returns `success=true` or `success=false`, plus an error message if false
      const data = await response.json();
      return data;

    } catch (error) {
      return {
        success: false,
        message: "An error occurred. Please try again."
      };
    }
  }
  ```
</CodeGroup>

Responses from this form endpoint will be one of the following:

```json  theme={"dark"}
HTTP 200

{
  success: true
}
```

```json  theme={"dark"}
HTTP 400 or 500

{
  success: false,
  message: "A descriptive error message."
}
```

## Troubleshooting

Submissions to form endpoints are rate limited to a low number of requests per minute from each IP address. The endpoint will return a `HTTP 429` response if requests exceed the rate limit. You should try to handle these responses gracefully in your form as shown in the example above.
