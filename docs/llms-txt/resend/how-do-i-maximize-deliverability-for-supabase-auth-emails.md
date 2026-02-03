# Source: https://resend.com/docs/knowledge-base/how-do-i-maximize-deliverability-for-supabase-auth-emails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How do I maximize deliverability for Supabase Auth emails?

> Everything you should do before you start sending authentication emails with Resend and Supabase.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

<Note>
  If you haven't yet, [configure your own Supabase
  integration](https://resend.com/settings/integrations)!
</Note>

Below are **five steps to improve the deliverability of your authentication emails**.

Prefer watching a video? Check out our video walkthrough below.

<YouTube id="51vzcGEmjRI" />

## 1. Setup a custom domain on Supabase

By default, Supabase generates a `supabase.co` domain for your project, and uses that domain for the links in your authentication emails (e.g., verify email, reset password).

Once you are ready to go live, though, it is important to setup a custom domain. The key benefit here is to align the domains used in your `from` address and the links in your emails. Especially for something as sensitive as email verification and magic links, **giving confidence to the inbox providers that the origin of the email and the links in the body are the same** can be very impactful.

This changes your links from:

```
https://039357829384.supabase.co/auth/v1/{code}
```

To something like this:

```
https://auth.yourdomain.com/auth/v1/{code}
```

Supabase has a helpful guide for [Setting up a custom domain](https://supabase.com/docs/guides/platform/custom-domains).

## 2. Setup a dedicated subdomain

There are many benefits to using a subdomain vs your root domain for sending, one being that you can isolate the reputation of the subdomain from your root domain.

For authentication emails, using a subdomain is particularly helpful because it is a way to **signal your intention to the inbox provider**. For example, if you use `auth.yourdomain.com` for your authentication emails, you are communicating to the inbox provider that all emails from this subdomain are related to sending authentication emails.

This clarity is essential because it helps the inbox provider understand that this subdomain is not used for sending marketing emails, which are more likely to be marked as spam.

<Note>
  If you don't want a subdomain just for auth, you can also achieve this by
  establishing one subdomain for all your transactional emails (e.g.,
  `notifications.yourdomain.com`).
</Note>

To add a subdomain to Resend, you can [add it as a domain on the dashboard](https://resend.com/domains).

<img alt="Create auth subdomain" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=3d0629c74757298069867f0019e69a90" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/kb-create-auth-subdomain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=0cf05912a6970427692bd9ed030d98cb 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1c9e26479ea82534a819897044b40f45 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=3da6b1d836979372ae4f2b9b39ec3c5b 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=c147e739d844cc20c2fc9a1ca8f599f8 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=43daf8479539ec7776173ec98c3f72fe 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-create-auth-subdomain.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=79408b7562dbc19b18508f6590cb990b 2500w" />

## 3. Disable link and open tracking

Link and open tracking can be great for marketing emails but not for transactional emails. This kind of **tracking can actually hurt your deliverability**. Open tracking embeds a 1x1 pixel image in the email, and link tracking rewrites the links in the email to point to Resend's servers first. Both types can be seen as suspicious by the inbox provider and hurt your deliverability.

Also, Supabase has noted that link tracking is [known for corrupting verification links](https://supabase.com/docs/guides/platform/going-into-prod), making them unusable for your users.

You can disable link and open tracking by clicking on your domain and disabling at the bottom.

<img alt="Disable link and open tracking" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1deeae548895ad4047ca7283faad95c6" data-og-width="3024" width="3024" data-og-height="1888" height="1888" data-path="images/kb-disable-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=720f858d9a4b8fd9f5ecb36d85542d66 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=172505a2c9bcd1857b655c2f07e817b6 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ccb950b486157629a0fd1d28e7f44ea3 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=440a144d6c75a566251d75e28d8083f6 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=ac51dd92caa9b79c8f0c805a7335511a 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-disable-tracking.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=29d1ec433ae73b2b6f46f609764dbf55 2500w" />

## 4. Prepare for link scanners

Some inbox providers or enterprise systems have email scanners that run a `GET` request on all links in the body of the email. This type of scan can be problematic since Supabase Auth links are single-use.

To get around this problem, consider altering the email template to replace the original magic link with a link to a domain you control. The domain can present the user with a "Sign-in" button, which redirects the user to the original magic link URL when clicked.

## 5. Setup DMARC

Like our human relationships, email deliverability is built on trust. The more inboxes can trust your emails, your domain, and your sending, the more likely your emails will be delivered to the inbox. This makes [Email Authentication a critical pillar](https://resend.com/blog/email-authentication-a-developers-guide) in the journey to excellent deliverability.

That is where DMARC comes in. As the industry standard for email authentication, **DMARC is a way to tell the inbox provider that you are who you say you are**. It is a way to signal to the inbox provider that you are a legitimate sender and that your emails should be delivered to the inbox.

Following security best practices like DMARC will show your validity and authenticity.

<img alt="DMARC policy details" src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=2b853e7501c2863ddd2ded6de271e0b6" data-og-width="2980" width="2980" data-og-height="2040" height="2040" data-path="images/kb-dmarc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=1617ba218838af4146c39f0b3e488933 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6f531ccebea71e50dac30a6d13f4dc1b 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=6056e9bf254033b63ec550915412c94a 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=4dccca9f083cd3d550772fb52244e3e4 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=40aaf8a282ddca464ebd302ed86e6441 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/kb-dmarc.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=14788176851801b3b558ab8e8d260640 2500w" />

You can use our [DMARC setup guide to get started](/dashboard/domains/dmarc).
