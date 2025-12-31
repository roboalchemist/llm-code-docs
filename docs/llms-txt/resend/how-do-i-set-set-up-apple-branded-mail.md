# Source: https://resend.com/docs/knowledge-base/how-do-i-set-set-up-apple-branded-mail.md

# How do I set up Apple Branded Mail?

> Learn how to implement Apple Branded Mail to display your logo in Apple Mail clients.

export const YouTube = ({id}) => {
  return <iframe className="w-full aspect-video rounded-xl" src={`https://www.youtube.com/embed/${id}`} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe>;
};

## Prerequisites

To get the most out of this guide, you will need to:

* [Create an Apple Business Connect account](https://www.apple.com/business/connect/)
* [Setup DMARC on your domain](/dashboard/domains/dmarc)
* A company identification number for Apple to verify your company

Prefer watching a video? Check out our video walkthrough below.

<YouTube id="zLDRvWVPqxk" />

## What is Apple Branded Mail?

Apple Branded Mail is a proprietary Apple format that displays your logo as an avatar in the inbox of Apple Mail. Displaying your logo can increase brand recognition and trust and improve engagement.

There are a few benefits of Apple Branded mail over BIMI:

* Since it's an Apple format, it does not require a certificate like [BIMI does](/dashboard/domains/bimi).
* The image support is broader, supporting `.png`, `.heif`, and `.jpg` logos.

Since Apple Branded Mail works only with Apple Mail on new iOS, iPadOS, and macOS versions, your logo will not show in other mail clients or older versions of Apple Mail.

For this reason, we recommend following all possible methods for adding your logo to your emails, including Apple Branded Mail, [our general guide](/knowledge-base/how-do-i-send-with-an-avatar), and [BIMI](/dashboard/domains/bimi) if it fits your needs.

## Implementing Apple Branded Mail

### 1. Configure DMARC

<Note>
  If you haven't set up DMARC yet, follow our [DMARC Setup
  Guide](/dashboard/domains/dmarc).
</Note>

To ensure your logo appears with Apple Branded Mail, set your DMARC policy to either `p=quarantine;` or `p=reject;`. This policy guarantees that your emails are authenticated and prevents others from spoofing your domain and sending emails with your logo.

Here's an overview of the required parameters:

| Parameter | Purpose    | Required Value                 |
| --------- | ---------- | ------------------------------ |
| `p`       | Policy     | `p=quarantine;` or `p=reject;` |
| `pct`     | Percentage | `pct=100;`                     |

Here is an example of an adequate DMARC record:

```
"v=DMARC1; p=quarantine; pct=100; rua=mailto:dmarcreports@example.com"
```

As we mention in our [DMARC Setup Guide](/dashboard/domains/dmarc), be sure to test your emails to make sure they are passing DMARC before changing your DMARC policy to `p=quarantine;` or `p=reject;`.

### 2. Create an Apple Business Connect account

Apple displays the logo you set in your Business Connect account. [Create an account](https://www.apple.com/business/connect/) if your company does not already have one. Make sure to use your company details when signing up.

### 3. Add your company details

Apple will prompt you to provide details like your company address and name.

### 4. Add your brand details

Once your company account is created, in Apple Business Connect, select the **Branded Mail** option in the left sidebar and provide details on your brand. Add details like the brand name and your brand website.

<img src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8348f2b44a70bfb6c4e065046a7443dd" alt="Add your brand details" data-og-width="3412" width="3412" data-og-height="1884" height="1884" data-path="images/abm-step-4-add-brand-details-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8f128d72a6c163a6b6b2af632cec92f6 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7dd0a8dc2e6135595270f4a19f0b370f 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5fbf82fed28982b58428a4b961c727f7 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=df7d16dcfdc469fdae4405ee44b90512 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=354cb4793cbec4dc66eae73d53426714 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-1.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=51987608cca6dfb16dec5509c623f506 2500w" />

<img src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=8ae25d711442f1f38620bd0aa1996fee" alt="Add your brand details" data-og-width="3412" width="3412" data-og-height="1884" height="1884" data-path="images/abm-step-4-add-brand-details-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=272097166b079d7617786cfd5f272b4b 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=6c902c656546c0368bec47ee9ed2eece 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=23057844522b36426468d1f9b4aae83b 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=07b2438027f3c17dba6ef4d0f7c7aecb 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=761ee931793dbf2567d9484bc66acc60 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-4-add-brand-details-2.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ee469b8134f2b471edbbcd469297e4f1 2500w" />

### 5. Add your logo

Once you fill out the brand details, upload your logo. Apple requires the logo to be at least 1024 x 1024 px in a `.png`, `.heif`, or `.jpeg` format.

<img src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=325d6466f5c237cd8c478eba3ac746d5" alt="Add your logo" data-og-width="3412" width="3412" data-og-height="1884" height="1884" data-path="images/abm-step-5-add-your-logo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2bc479f38855f2bed9a87652f3a16786 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=92a18a3ff5cf66aa50abfd6a3b8e70ef 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=9570d8fd257e807cf0ca3b96b4cf87ed 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=80d628ba93763f56b006bd79012c974f 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=e41fc8c5477df3ace2eddb5fe589c72a 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-5-add-your-logo.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=805b9a1cccba9b37bfdb745a32a79c25 2500w" />

### 6. Add your domain

Confirm the domains or email addresses where you want your brand logo to appear.

You can register your logo for your root domain or a subdomain. If you don't set a specific logo for a subdomain, the root domain logo will automatically display for any email sent from your subdomains.

### 7. Verify your company

Apple requires details to confirm your company identity.

If you're in the United States, provide a Federal Taxpayer Identification Number. Other countries will use a local equivalent for this step. Apple also asks that you add a DNS record to verify DNS access.

### 8. Verify with Apple

After you submit all your information, Apple will verify your details. This process may take up to seven business days.

Once the logo is verified, Apple will send an email notification and note the verified status in Branded Mail. Your logo will start to display in compatible Apple Mail versions.

<img src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=be541896283e84398a893013095e7f40" alt="Verified logo" data-og-width="3412" width="3412" data-og-height="1884" height="1884" data-path="images/abm-step-8-verify-with-apple.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=f7a889139327b05a41d28a7f3ca0fd42 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c526f7ef1f4bbd65cf21622d007061ca 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5a147c360b73dd6b15b1698e29aa0306 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=c86ee74b7178690e4c5b22a5ddb9dbc1 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7decb3aa50b7fe8821eaef783e6e1bb2 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/abm-step-8-verify-with-apple.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=42bbe9553e4577991c8c9e550abd127b 2500w" />

<Tip>
  See Apple's documentation on [Apple Branded
  Mail](https://support.apple.com/en-au/guide/apple-business-connect/abcb761b19d2/web)
  for any detailed questions on adding your logo.
</Tip>
