# Source: https://resend.com/docs/knowledge-base/replit-integration.md

# Send emails with Replit and Resend

> Learn how to add the Resend integration to your Replit project.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

[Replit](https://replit.com/) is a platform for building sites and apps with AI. You can add Resend in a Replit project by asking the chat to add email sending with Resend.

**Example prompt**

```
When someone fills out the contact form, send an email using Resend.
```

Prefer watching a video? Check out our video walkthrough below.

<YouTube id="gXwFWFMcnnY" />

## 1. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in Replit (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/dashboard/domains/introduction).

## 2. Add your Resend API key and from address

To use Resend with Replit, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys). Do not share your API key with others or expose it in the browser or other client-side code.

The from address is the email address that will be used to send emails. Use your custom domain you added in step 1 here (e.g., `hello@yourdomain.com`).

<img src="https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=7c6dee645c882748990a7973150b252f" alt="adding the Resend integration to a Replit chat" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/replit-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=280&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=6ceb79a381e2410a78d588d3372b855b 280w, https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=560&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=f12638b6db44015b3984fe99cda57e23 560w, https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=840&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=418a2cea8140f612a47dbe1b04e25491 840w, https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=1100&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=31da7dcb80ebb985c0e685e469987569 1100w, https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=1650&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=5fa3c8956cb7e4599162da358762dfbb 1650w, https://mintcdn.com/resend/873NN72QQCCHs00J/images/replit-integration.png?w=2500&fit=max&auto=format&n=873NN72QQCCHs00J&q=85&s=2a108ec2f5bb1b0aeb5eb3629f4a79f6 2500w" />

<Note>
  Replit tracks the details of your Resend integration in the [Integrations
  page](https://replit.com/integrations).
</Note>
