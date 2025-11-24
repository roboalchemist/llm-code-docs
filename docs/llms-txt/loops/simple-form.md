# Source: https://loops.so/docs/forms/simple-form.md

# Simple form

> Collect signups from any web page with a customizable form.

<Tip>
  Check out our specific documentation for adding forms to
  [Framer](/integrations/framer) and [Webflow](/integrations/webflow).
</Tip>

You may want to collect signups from your website directly into Loops.

## Generate the form

Easily generate an HTML or JSX form for collecting new signups for your mailing list from inside Loops.

Go to the [Forms page](https://app.loops.so/forms) and customize your form.

Here you will see settings to manage features of your form:

* add contacts to [mailing lists](/contacts/mailing-lists) (make sure your lists are marked as **Public** first)
* add a "User group" value to each contact
* change the layout
* edit the button color
* edit the success message

When you're happy with your form, copy the HTML into your website.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8f834516f33153454989d49f5110f2dd" alt="" data-og-width="3040" width="3040" data-og-height="2026" height="2026" data-path="images/simple-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=cb6fd923a4d7689f5b370d7e9b10b44d 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a557be73c99d0ca7d57ee5804c3e9474 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2bb003becb3bd1eafbd69f8f8f04f093 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ba5cd04c08493b8036ce1e83565e896a 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f74597e7911cc5876830f523e69d3cde 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=274b07701a3af14be93ca31f2a7d8329 2500w" />

## Add more fields to the form

It's possible to add other fields to your form if you want to collect more than just email addresses.

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

When adding fields to a form, use the "API Name" value found from your [API settings page](https://app.loops.so/settings?page=api) as the `name` attribute for each field. See the above list for examples.

For example, this code would collect a First Name and add the contact to a mailing list (using a hidden field input that doesn't appear in the web page):

```html  theme={"dark"}
<input type="text" name="firstName" />
<input type="hidden" name="mailingLists" value="cly2xnjbn002z0mme68uog1wk" />
```

If you want more flexibility when creating signup forms, [read about creating custom forms](/forms/custom-form).

## Troubleshooting

Submissions to form endpoints are rate limited to a low number of requests per minute from each IP address. If you see the message "Too many signups, please try again in a little while" when submitting a form, you have hit the rate limit. Please wait and try again.

Additionally, the form JavaScript does not allow duplicates of the same email address per pageload.
