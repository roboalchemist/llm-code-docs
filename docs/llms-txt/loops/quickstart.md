# Source: https://loops.so/docs/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Welcome to Loops, the platform for SaaS email.

This is your guide to getting started with Loops. If you're new to setting up email for your SaaS company, this is the guide you should start with.

## What is Loops?

Loops is an email platform, that helps you send marketing and transactional emails from our app, API and integrations.

With Loops, you can track events and contact properties and then use that information to send emails to increase revenue, engagement or just generally improve your user's experience of your app.

**Let's get started ✨**

What we'll be covering...

1. [Set up your domain records](#1-set-up-your-domain-records)
2. [Import contacts](#2-import-contacts)
3. [Collect signups with a form](#3-collect-signups-with-a-form)
4. [Create your first email](#4-create-your-first-email)
5. [Send transactional email](#5-send-transactional-email)

## 1. Set up your domain records

The first step is to set up your domain, so you can send emails through Loops. You need to do this before you can send any emails.

We send from your domain so your emails appear as if they are coming from you.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=3f6707e1d720d43e2f6b321f795fa220" alt="" data-og-width="2280" width="2280" data-og-height="1418" height="1418" data-path="images/set-up-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f0e7d42771f9e752c7348e6e0aa4368f 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=49b5fbc49a52b27388961637be9c019e 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=d44e4171e9bfd66f95c4b66ac52e2920 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=1629ff8c5e124f2a12129dab4dbc1534 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=52d49abe36641c9b608e18bec622ce59 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-domain.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=eb0a59150c18d9073e43b459eb6b89c0 2500w" />

We choose to send from a `mail.loops.so` subdomain but you can send from your root domain if you'd prefer.

To set up your domain in Loops, you need to add some MX, TXT and CNAME records to your domain's DNS settings so that we can verify that you own the domain you want to send emails from.

Once you've set up your domain records, you'll be able to start sending emails!

You can always send the records to a developer to help you integrate them. Read how to [add a member to your team](/account/team-members).

<CardGroup cols={2}>
  <Card title="Setting up your domain" icon="globe" href="/sending-domain" />

  <Card title="Subdomains vs root domains" icon="sitemap" href="/deliverability/sending-from-subdomain" />
</CardGroup>

## 2. Import contacts

To send marketing and product emails to your contacts, you will need to import those contacts into Loops.

Note: this isn't required if you only plan to use transactional email, as those contacts can be emailed directly via the API.

If you have any existing contacts, i.e from a waitlist, your early access users, a database or your audience on a different platform, you can get started by importing them via CSV.

You can import contacts via [CSV upload](/add-users/csv-upload), [API](/api-reference) or through one of our [integrations](/integrations).

<Tip>
  The most popular path is to import a CSV of existing contacts, then going
  forward automatically add contacts using our API, a form or an integration.
</Tip>

### Contacts

Contacts are unique users in your Loop's audience. We use email and a unique identifier to distinguish contacts. The only required field a contact must have is an email.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f49de0824fea0b232756877d12270bb6" alt="" data-og-width="2280" width="2280" data-og-height="921" height="921" data-path="images/contacts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c476765e03c1ada48640fcf17b5f36dc 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f1fec69b8bf586ed51f765919026207f 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=65a7caf3f506a7d5a2d9454f5138e641 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5ea476efc07966484fc319cf5aac423c 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a5ce533a83220e59fb8c783cdd4ddf01 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contacts.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=56d23b9842c475c7d757f9210feec488 2500w" />

### Contact properties

Contact properties are additional pieces of information you can associate with a contact. They can include things like name, location, job title, and more.

We provide [default properties](/contacts/properties#default-contact-properties) like name, user group and source, but you are free to add any number of [custom properties](/contacts/properties#custom-contact-properties) to your contacts, too.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=467aae52673b379ca2ef950125062d85" alt="" data-og-width="2280" width="2280" data-og-height="504" height="504" data-path="images/contact-properties.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7fd6cf66f211cd36f6f7e5c84567c605 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1e720a1de143ebf90dd3074abc2bae20 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=10a25f094dfebecf6468d848747a8cb8 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=33e07092a45850f5d8e5cd5b471b5088 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0293fe254532a1d2e54ab1999e14d7bd 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/contact-properties.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7d9ac4476954a61439e689db28a53fbf 2500w" />

You can use contact properties to [segment your audience](/contacts/filters-segments) and send more targeted emails to specific groups.

For example, you could send a promotional email only to contacts with a certain job title or to those in a specific user group.

<CardGroup cols={2}>
  <Card title="Add with CSV Upload" icon="plus" href="/add-users/csv-upload" />

  <Card title="Add via integrations" icon="arrows-turn-right" href="/add-users/integrations" />

  <Card title="Add with the API" icon="rectangle-terminal" href="/add-users/loops-api" />

  <Card title="Filters and Segments" icon="filter-list" href="/contacts/filters-segments" />
</CardGroup>

## 3. Collect signups with a form

Adding a form to your site is one (popular) way to automatically add new contacts to your Audience.

Even if you're adding contacts programmatically via API or integration, in most cases you'll also want to have an input form on your page to collect emails for newsletters or product updates.

To add a form to your site, head over to the [Forms page](https://app.loops.so/forms).

You will see a handful of customization options including the form style, placeholder text, success message, font, font color, button color, and more.

Make as many changes as you need to create a form that matches your brand.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8f834516f33153454989d49f5110f2dd" alt="Simple form" data-og-width="3040" width="3040" data-og-height="2026" height="2026" data-path="images/simple-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=cb6fd923a4d7689f5b370d7e9b10b44d 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=a557be73c99d0ca7d57ee5804c3e9474 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=2bb003becb3bd1eafbd69f8f8f04f093 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ba5cd04c08493b8036ce1e83565e896a 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f74597e7911cc5876830f523e69d3cde 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/simple-form.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=274b07701a3af14be93ca31f2a7d8329 2500w" />

When you have finished customizing your form, simply copy the HTML or JSX that is automatically generated and paste it into your site.

For more flexibility, you can create custom HTML forms that work with Loops. [Read our full guide about custom forms](/forms/custom-form) or check out our [form-based integrations](/integrations#manage-contacts).

<CardGroup cols={2}>
  <Card title="Simple form" icon="input-pipe" href="/forms/simple-form" />

  <Card title="Custom form" icon="table-list" href="/forms/custom-form" />

  <Card
    title="Add a form to Framer"
    icon={
    <svg
      xmlns="http://www.w3.org/2000/svg"
      xmlnsXlink="http://www.w3.org/1999/xlink"
      width="24"
      height="24"
      viewBox="0 0 98 148"
    >
      <path
        d="M 93.852 94.49 C 95.387 96.036 94.292 98.667 92.113 98.667 L 51.45 98.667 C 50.097 98.667 49 99.764 49 101.117 L 49 142.057 C 49 144.243 46.353 145.335 44.812 143.783 L 0.949 99.622 C 0.341 99.01 0 98.183 0 97.32 L 0 51.783 C 0 50.43 1.097 49.333 2.45 49.333 L 49 49.333 Z"
        fill="#FF4A00"
      ></path>
      <path
        d="M 49 49.333 L 4.148 4.177 C 2.613 2.631 3.708 0 5.887 0 L 95.55 0 C 96.903 0 98 1.097 98 2.45 L 98 46.883 C 98 48.236 96.903 49.333 95.55 49.333 Z"
        fill="#FF4A00"
      ></path>
    </svg>
  }
    href="/integrations/framer"
  />

  <Card
    title="Add a form to Webflow"
    icon={
    <svg
      width="24"
      height="24"
      viewBox="0 0 16 16"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        fillRule="evenodd"
        clipRule="evenodd"
        d="M15.3334 4L11.2916 12H7.49528L9.18675 8.68446H9.11086C7.7154 10.5186 5.63335 11.726 2.66675 12V8.73034C2.66675 8.73034 4.56456 8.61685 5.68023 7.42922H2.66675V4.00006H6.05357V6.8205L6.12959 6.82018L7.51356 4.00006H10.0749V6.80261L10.151 6.80249L11.5869 4H15.3334Z"
        fill="#FF4A00"
      ></path>
    </svg>
  }
    href="/integrations/webflow"
  />
</CardGroup>

## 4. Create your first email

To create your first email, first select the type of content you'll be sending. You can send email as a campaign, loop or transactional email. You can also choose to start with a [Template](https://app.loops.so/templates) instead of starting from scratch.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=daa962aaa3dd795ed89021acc341a7a6" alt="" data-og-width="2280" width="2280" data-og-height="1134" height="1134" data-path="images/create-first-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=995db60712ac648e3d14e8fbb7e651e0 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e8d3056be93980f525bb84acc8484820 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=44eb7ade0e2da35e08cd7c968cfe575c 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=557b3af625d764ecfff8d3fa6cd6cb56 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=265f7518e2ac38d3ceb42fa3d4863fe5 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/create-first-email.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e7546ba6f5bc0275d3c6444fb6878d3d 2500w" />

**Campaigns** are single marketing emails sent to a group (e.g. newsletters, product updates, announcements, investor updates), **Loops** are automated emails sent based on specific triggers or conditions (e.g. onboarding sequences) and **Transactional** emails are one-off emails sent to a single person (e.g. forgot password, two-factor authorization codes, receipts). [Read more](/types-of-emails)

In this example, we will build a product update (a campaign), which could be sent to your users if you're building a SaaS. They should be sent monthly or at a faster cadence depending on shipping speed and contain a high-level overview of what you shipped over the last 30 days.

To get started, click the **Create** button on the Home screen, followed by **Campaign**.

Then we’re going to personalize by adding [dynamic content](/creating-emails/personalizing-emails) and [style it](/creating-emails/editor) to match our brand.

<img src="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=50f73381c384e4ff6ed919d81630cbe9" alt="Adding personalization" data-og-width="2280" width="2280" data-og-height="1035" height="1035" data-path="images/basic-merge.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=280&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=18814146da18de5f13e391fa12a20c0e 280w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=560&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=11778fb9f17dcc74d2d8cc3862188dd0 560w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=840&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=1d9873614099f8e8a8bf03a6737d6784 840w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=1100&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=2edecb2194d57f86bc98b4f265381631 1100w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=1650&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=f516cbbf3856e25d5583034ff6b9319c 1650w, https://mintcdn.com/loops/EgyPhKkeXp9wCnWY/images/basic-merge.png?w=2500&fit=max&auto=format&n=EgyPhKkeXp9wCnWY&q=85&s=1e7b6b3fcaf7193246b46cbfe703f4d2 2500w" />

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e2c7088ffd4d20ac66b5fee7a1756010" alt="Adding styling" data-og-width="2280" width="2280" data-og-height="1953" height="1953" data-path="images/message-visual.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=1566d2f25ff94cd77ce02190627153c6 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=b97a0e4251a474a7649518819d87364b 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=a81c6e2c9f6ac29e31329ada927e038a 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=adb055873f4fd4c0e917faac0c927983 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=5e6346334f27792ff4fab4450fe9c3a9 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/message-visual.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=738b8ddf5342b807bcfddc6fa07e61c7 2500w" />

<Tip>
  You can preview your email any time by hitting the paper airplane icon in the
  top right of the editor window.
</Tip>

Once you're finished with the email content, click **Next** in the top right to choose your audience.

Now we'll select the audience segment to whom we'll be sending the update.

Since we're sending a product update, we want to send it to our entire audience so we won't be adding any audience filters.

If you'd like to segment your audience, just click **Add filter**, which will open the filtering options.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9672bd5756789f880f53626fe58da5b9" alt="Filter campaign audience" data-og-width="2280" width="2280" data-og-height="1277" height="1277" data-path="images/campaign-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8352866be9413370786a56d39c3d8732 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=75573cf48c2b6e31f4395e017cd906ba 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=555a7902a81557f6fc2fa706790ef64b 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ae762e120ee3cc9365eaee7d0be4112a 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=023e7b715eb7a8fda39b6e72d1cde341 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-filter.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4f3fe7c700966c8d12b5552886f3efef 2500w" />

Click the **Next** button top right and you'll see options to send the email immediately or to schedule it for a time in the future.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=889f1c27cb43082d324a4b097e8f903e" alt="Schedule a campaign" data-og-width="2280" width="2280" data-og-height="1803" height="1803" data-path="images/campaign-schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=899ac6f02919d54d2a83499abd10c6e9 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=75fca2a38e1b120cadea94b93fb346fc 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=bf767884784702eb3a1d8cf60a56e8c5 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=990d75b55db048e1295c6b224d188b49 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d21b907539f15b0b01658fde80097c54 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/campaign-schedule.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d6cf4917eea337e6abce1ced52752f48 2500w" />

Click **Next** one last time to see a review of your email and settings (you can also see a preview of your email, too). If you're happy with how everything looks, click **Schedule send** on the last page and we're done!

The email is now scheduled to go out.

By the way, you can cancel the scheduled send at any time between the send time and now to update it, or you can just send it right away.

<CardGroup cols={2}>
  <Card title="Types of emails" icon="envelopes-bulk" href="/types-of-emails" />

  <Card title="Sending your first email" icon="mailbox" href="/sending-first-email" />

  <Card title="Editing emails in our editor" icon="keyboard" href="/creating-emails/editor" />

  <Card title="Custom emails with Emailify, Email Love or MJML" icon="upload" href="/creating-emails/uploading-custom-email" />
</CardGroup>

## 6. Set up an automated mail sequence

We suggest that new Loops users warm up their new sending domain with a welcome email sequence. A slow ramp up of emails sent to highly-engaged recipients will help prepare your domain for larger campaigns later on ([read more](/deliverability/sending-to-large-audience)).

You can create an onboarding or welcome sequence using what we call "loops".

A loop looks like this:

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=19c5e3492b267d7ba217776daecfb363" alt="" data-og-width="2280" width="2280" data-og-height="2084" height="2084" data-path="images/building-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c9222854fb36db1e3538aa1a6965f500 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=4eb8c5584a138580ce104c7a7aaea3e4 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=54afadd407e9e095ee995e0d106e50f3 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0b7ba983960b33cd4de013a2675fd40b 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5a834e73735d5b265dca815bf8bbcc4b 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/building-loop.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7aed70f56f4fa1cd67b81258c21ea3a7 2500w" />

Go to the [Loops page](https://app.loops.so/loops) and click **New**.

We'll start with the "Introduce yourself" template. This will create a loop with a "Contact added" trigger (meaning every new contact will be added to the loop), with an already-written introduction email ready for you.

Edit the email and when you're ready to make it live, click **Start**.

You can use [branches](/loop-builder/branching-loops) to create more complex workflows, sending contacts down different branches depending on contact properties or even whether they've interacted with campaigns you've sent from Loops.

<img src="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=f28b3a021d8215d32331cb9e6fd35066" alt="Branches in a loop" data-og-width="2280" width="2280" data-og-height="1479" height="1479" data-path="images/loop-builder-branching.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=280&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=ff9789af355e784e7c69aa548dea8bac 280w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=560&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=376818c45ff13412f6af850d670a9af8 560w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=840&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=f9f8543329ad6424e702a0ce860fd31d 840w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=1100&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=47edac897c29edb4f90005d0420f590f 1100w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=1650&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=a53133c2587d35c445348aea4c7d5d60 1650w, https://mintcdn.com/loops/YzXNyAoWJH6Zxv4S/images/loop-builder-branching.png?w=2500&fit=max&auto=format&n=YzXNyAoWJH6Zxv4S&q=85&s=d748e070abf937973fd04e041639a819 2500w" />

<CardGroup cols={2}>
  <Card title="Loop builder" icon="arrows-rotate" href="/loop-builder" />

  <Card title="Triggering Loops" icon="circle-play" href="/loop-builder/loop-triggers" />

  <Card title="Branching Loops" icon="code-branch" href="/loop-builder/branching-loops" />
</CardGroup>

## 7. Send transactional email

You'll likely need to send a password reset, login or other automatic email that confirms a user action.

These non-promotional emails are considered **Transactional emails** and are the 1:1 emails that are sent to a single contact via API or integration.

They're included in all paid Loops plans, and also included within the 4,000 monthly sends available in the [Free plan](/account/free-plan).

To get started, click the **Create** button on the Home screen, followed by **Transactional**.

Next, it’s time to write and style your email.

We recommend following a similar style across all of your Transactional emails. You can do this by using [themes](/creating-emails/styles#themes).

Let’s create a Password Reset email together.

Add copy and styling, and then to add dynamic content click the **Insert data variables** icon and specify a data variable name.

These data variables will be populated with real content when you send the email using the API.

<img src="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=d124653cd87536765f40e4de3102c15a" alt="Add data variables" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/terminal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=280&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=1c1834773261e5a0c8be7a0e1b4191a5 280w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=560&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=5e9e0bae89a5aded6a9d7448926ff5a8 560w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=840&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=40030ce29b5df99adb0c950877a84baa 840w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1100&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=7712e06a02cfeedd04e43aef5024c6eb 1100w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=1650&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=cbcbd72414a41dc5717a61b867789fbe 1650w, https://mintcdn.com/loops/SqldyWKxvGS7UNL4/images/terminal.png?w=2500&fit=max&auto=format&n=SqldyWKxvGS7UNL4&q=85&s=3a8450a5d3357e016e9b562574bd68fe 2500w" />

Click the **Next** button top right to view the data needed in your API call.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=553cf454d657a3049b9566e2851d1b0b" alt="View the paylod" data-og-width="2280" width="2280" data-og-height="1682" height="1682" data-path="images/next.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=60b1e92d098c794c93b8cfb01310586c 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=c8f8c7d1c2918340532861bb8bd52c4c 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=e9569fd50c07b058708c7447fcf4cacf 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=695b04041f9dfe709a25a3ad36345426 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=ea4ba40f8634d64c2905b0cc375c0c43 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/next.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2083f0ff2fc32596387a81dcf6e07f17 2500w" />

Hit **Publish** to finalize the email. Copy the payload details and the ID; you'll need these to send the email using the API.

Make an [API request](/api-reference/send-transactional-email) to the transactional endpoint (or use an [SDK](/sdks)).

```
POST https://app.loops.so/api/v1/transactional
```

You will need the payload copied from before. Make sure to include values for all of the data variables you added to the email.

```json  theme={"dark"}
{
  "transactionalId": "clfq6dinn000yl70fgwwyp82l",
  "email": "favorite@example.com",
  "dataVariables": {
    "name": "Chris",
    "passwordResetLink": "https://example.com/reset-password"
  }
}
```

<Tip>
  To test sending transactional emails you can use an API tool like
  [Postman](https://www.postman.com), [Httpie](https://httpie.io) or
  [Insomnia](https://insomnia.rest) to make API requests.
</Tip>

<CardGroup cols={2}>
  <Card title="About transactional email" icon="envelope" href="/transactional" />

  <Card title="Transactional guide" icon="file-code" href="/transactional" />
</CardGroup>

## 8. Integrate with other platforms

Loops integrates with thousands of other platforms, making it easy to send email to your audience, users or customers, regardless of where they originate.

<img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=48a4e1fc1c670610372a3f2185864824" alt="Create an action in Make" data-og-width="2307" width="2307" data-og-height="1538" height="1538" data-path="images/make-add-module.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=00b7f2310a7113b4dc87349263c7e049 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=7250533ada99744f86d1496b170c0753 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4ce0277161be6809bcc1c7e669a1812b 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=12db09b3e66b8c74f9336d5224f421e2 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=fd0811855132f0dddeb25614e32bf2aa 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/make-add-module.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=3971b446549cd1405821e27118498661 2500w" />

Set up connections to different apps using a tool like [Zapier](/integrations/zapier) or [Make](/integrations/make), or create contacts using events from [Segment](/integrations/segment).

Our [webhook integration for Stripe](/integrations/stripe) lets you easily sync customers and send automated emails based on payment events.

## Get support from the team

Whether you’re sending your very first emails for your business or are switching over from another service, we’re always here to help!

Every page of Loops has a small `?` widget in the bottom right-hand corner. Click it to receive instant support.

💬 Do you prefer live chat? Click and chat!

💌 Do you prefer email? [Send away](mailto:chris@loops.so)

🧑‍💻 Do you prefer a video call? [Book it](https://calendly.com/chris-loops/loops-in-app-support)
