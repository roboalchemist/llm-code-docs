# Source: https://docs.base44.com/Integrations/Resend-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Resend Integration 

> Connect your Base44 app with Resend to send emails like confirmations, updates, and newsletters from your own domain with minimal setup.

<Info>
  <u>Note</u>: Resend integration is available on Builder tier and above. If you're on the Free tier, you'll need to upgrade your app to use backend functions.
</Info>

## **Step-by-step setup**

### **Part 1: The Resend side**

If you already have your Resend API keys, you can skip ahead to "[Part 2 - The Base44 side](https://docs.base44.com/Integrations/Resend-integration#part-2%3A-the-base44-side)" setup

<Steps>
  <Step title="Create a Resend account">
        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Resendsetupaccount1-verifydomain.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=ec6940b8eaaa1f688cb4a4e80251fea4" alt="Resendsetupaccount1 Verifydomain Pn" width="1024" height="495" data-path="images/Resendsetupaccount1-verifydomain.png" />

    If you don’t already have one:

    1. Go to [<u>Resend domains</u>](https://resend.com/domains)
    2. Sign up and add your domain
  </Step>

  <Step title="Verify your domain">
    After adding your domain

    1. Follow the DNS instructions provided by Resend to complete domain verification. You’ll be given DNS records (TXT, MX) to add via your own DNS provider. 
    2. These will help prevent your emails from being flagged as spam. 

    <Tip>
      Tip: You can use a subdomain like [updates.yourdomain.com](http://updates.yourdomain.com) or [mail.yourdomain.com](http://mail.yourdomain.com) instead of your main domain. This helps isolate your email sending reputation and can reduce the chance of deliverability issues affecting your primary domain.
    </Tip>
  </Step>

  <Step title="Create your Resend API key">
        <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Resendsetupaccount-APIkey.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=5b2a8a35b153694f586f45dcdbe2608c" alt="Resendsetupaccount AP Ikey Pn" width="1024" height="494" data-path="images/Resendsetupaccount-APIkey.png" />

    1. Go to the [<u>API Keys page</u>](https://resend.com/api-keys) 
    2. Click on “**Generate API key**”
    3. Copy and save the key somewhere secure, but also keep it handy. You’ll need to paste it into Base44 in the next step.
  </Step>
</Steps>

### Part 2: **The Base44 side**

Once you have your Resend API keys, there are two ways to use this integration in Base44. Click the option below to expand and view the instructions.

<Accordion defaultOpen icon="sparkles" title="Option 1: Creating an app from scratch (preferred)">
  1. Head over to the [integrations catalog page](https://app.base44.com/integrations-catalog)

     <Info>
       Make sure you're logged into Base44 to view this page
     </Info>

     <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Integrations.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=16ac71b185167177ef260be7c92b0339" alt="Integrations Pn" width="1570" height="652" data-path="images/Integrations.png" />
  2. Find Resend and click “**Use this integration**”

     <img src="https://mintcdn.com/base44/oUaRpzSyJvMVshj9/images/Resend-useintegration.png?fit=max&auto=format&n=oUaRpzSyJvMVshj9&q=85&s=3287824e497c3f8bc88041e822804063" alt="Resend Useintegration Pn" width="1566" height="815" data-path="images/Resend-useintegration.png" />
  3. When prompted, paste your API key from Step 3. Your app is now connected to Resend.

     <img src="https://mintcdn.com/base44/-Vklow6W-uVvNnvR/images/resend-apikeys.png?fit=max&auto=format&n=-Vklow6W-uVvNnvR&q=85&s=3f5a6facbb160e59a40c13604579d5b6" alt="Resend Apikeys Pn" width="1572" height="815" data-path="images/resend-apikeys.png" />
  4. Type out your idea / prompt into the AI chat box to build your app

     > *“Build me an app to create and send welcome emails when someone signs up.”* 

     Base44s AI will walk you through setting it up.
</Accordion>

<Accordion defaultOpen icon="browser" title="Option 2: Working with an existing app">
  If you're working in an existing app, you can use the chat to ask:

  > *“Add the Resend integration to my app. Prompt me for the API key and send a welcome email when someone subscribes."*

  The AI chat will then walk you through the steps to set up this integration and will prompt you for your API keys.
</Accordion>

## **Common use cases for the Base44 x Resend integration**

Here are some examples of how Resend can be used in your Base44 app:

* Welcome emails when someone signs up 
* Password reset links or account recovery emails 
* Order confirmations or status updates 
* Internal team alerts when forms are submitted 
* Reminder emails for actions left incomplete 
* Newsletter campaigns for subscribers or users
* Survey or feedback requests after key actions 
* Trigger-based updates to users or admins

## **FAQ**

<AccordionGroup>
  <Accordion title="What is Resend?">
    Resend is a modern email API platform. It helps developers send transactional and marketing emails easily, with a focus on deliverability and ease of use.
  </Accordion>

  <Accordion title="Do I need a paid Resend plan?">
    No. The free tier lets you send emails from a verified domain and supports up to 3,000 contacts.
  </Accordion>

  <Accordion title="How do I manage newsletter subscribers?">
    Use Resend's Audiences to: 

    * Add contacts via CSV, manually, or via the API. 
    * Automatically manage unsubscribes with Resend's built-in link.
  </Accordion>

  <Accordion title="How does Resend handle unsubscribes?">
    Unsubscribes are processed automatically: 

    * You must include an unsubscribe link in all broadcast emails. 
    * Resend will remove users who unsubscribe from.
    * This ensures compliance with laws like CAN-SPAM and GDPR.
  </Accordion>

  <Accordion title="Can I set up double opt-in?">
    Yes, manually: 

    1. Send a confirmation email after form submission. 
    2. Include a link for users to click.
    3. Only add users to your audience after they confirm.
  </Accordion>

  <Accordion title="Why are my emails going to spam?">
    A few common reasons: 

    * Your domain isn't verified 
    * Missing plain-text version 
    * Using a generic sender (e.g., [onboarding@resend.dev](mailto:onboarding@resend.dev)) 
    * No unsubscribe link in marketing emails 

    <Tip>
      Use Resend’s [<u>Deliverability Insights</u>](https://resend.com/docs/dashboard/emails/deliverability-insights)  to get suggestions based on your email setup.
    </Tip>
  </Accordion>

  <Accordion title="Can I customize how my emails look?">
    Yes, you can use tools like [<u>React Email</u>](https://react.email/), which is an open-source library for building styled emails with React components.
  </Accordion>

  <Accordion title="Does Resend support transactional and marketing emails?">
    Yes, Resend supports both types of emails: 

    * Transactional emails - like account confirmations, password resets, and real-time notifications

    Marketing emails - such as newsletters and promotional campaigns, sent using the [<u>Broadcast tool</u>](https://resend.com/docs/dashboard/broadcasts/introduction) and [<u>Audiences</u>](https://resend.com/docs/dashboard/audiences/introduction)
  </Accordion>

  <Accordion title="Can I send emails to people who are not signed up with my app?">
    If you want to send emails to people who are not signed up to your app, you can use an external email service such as Resend. Resend lets you email any recipient, whether they have registered with your app or not.

    The built-in email function can only send emails to users who have signed up with your app. 
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).