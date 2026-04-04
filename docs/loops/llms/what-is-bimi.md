# Source: https://loops.so/docs/guides/what-is-bimi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What is BIMI?

> And why does it matter?

As an email marketer, ensuring that your emails actually get seen and read is priority #1. Adding an avatar to your emails can increase your open rates by up to 21%. The familiarity and trust that this little avatar brings has a great impact on your email campaigns.

Outside of manually adding your brand’s logo as an avatar to each individual email client, there may actually be another way to ensure your emails have the same visual aid with additional layer of trust built in.

How? BIMI.

## What is BIMI?

BIMI, or Brand Indicators for Message Identification is a relatively new email standard that allows you to add your brand’s logo to your authenticated emails.

Adopting BIMI will allow your brand’s logo to appear next to your emails in your recipient’s inbox without manually needing to add and maintain it on a provider by provider level. As long as the email client supports BIMI, your logo will appear.

## Which email providers support BIMI?

A growing number of email provider’s are currently supporting BIMI with many more currently considering it. The current list of supported providers are:

* Gmail
* Google Workspace
* Apple Mail ([macOS Ventura 13, iOS 16, and iPadOS 16, or later](https://developer.apple.com/support/bimi/))
* AOL
* Netscape
* Fastmail
* Yahoo (Yahoo Japan is not currently supported but is under considering for future adoption)
* Pobox

Here is the full breakdown of who does and doesn’t support BIMI as of right now:

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=ce6f070e7111e6c31d2eba8077b35a10" alt="" data-og-width="565" width="565" data-og-height="640" height="640" data-path="images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=0770acdc87b225241979a4b81abacce8 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=790f1207ccac0d33e4ca0c189a46101b 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=e7a2a5aee17203c9fe489088f2500c47 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=b50f4bd3beace8980cb2ba6c24fd5010 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=a4dce68690f624187957398d0d5e6ff4 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/R3P9DzvgnutHbbSomXep6ZOEOQ.webp?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=cf406126f482910d9f874aa30d2858a3 2500w" />
<small>Image via [BIMI Group](https://bimigroup.org/bimi-infographic/)</small>

## How does BIMI actually work?

Setting up BIMI will take a bit more work than simply uploading your brand’s logo and hitting save.

Technically speaking, BIMI is a text file that lives on your sending servers and works hand in hand with DKIM, SPF, and DMARC protocols.

At a broad level, after you send an email, your recipient’s email provider will look up your BIMI text file and attempt to verify the legitimacy of it. Once verified, your BIMI text file points the email provider to where they can find your logo and they will then attach it to your email.

To start, the sender (you) will need to ensure that you are DMARC compliant. DMARC (domain-based Message Authentication, Reporting, & Conformance) is an [email authentication policy and reporting protocol](https://bimigroup.org/faqs-for-senders-esps/) that defends against unauthorized use of domains.

Basically, DMARC helps protect your brand by detecting emails that aren’t coming from your domain – preventing spoofing and phishing attempts.

The email provider will also run through the Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) protocols to ensure that the sender’s email address was sent from the correct domain.

Next, you will need to create the logo that will actually be used. The current recommendation is a [square SVG file](https://bimigroup.org/creating-bimi-svg-logo-files/).

The naming convention of this file should be:

`https://yourservername.com/logo.svg`

Next is an optional but recommended step. To fully embrace BIMI, your brand should acquire a VMC, or a Verified Mark Certificate. This will help validate the true ownership of the logo being used. More on this in the section below.

Finally, you will need to create a TXT record for BIMI in your DNS records. This record will contain a URL to your logo for the email provider to grab and display.

The full implementation guide from BIMI can be located [here](https://bimigroup.org/implementation-guide/).

## How much does BIMI cost?

Along with taking some technical chops to get BIMI fully set up, it’s also not free.

Getting the Verified Mark Certificate mentioned above currently [costs \$1,500](https://www.digicert.com/tls-ssl/verified-mark-certificates).

On top of this cost, to qualify for the certificate your brand logo also needs to be a registered trademark, which will also come with additional costs and possible legal fees.

## Checking your BIMI record

Now that you’ve gone through the work of setting up your BIMI records, it’s time to confirm that everything is working as expected.

The BIMI group provides a [BIMI inspector](https://bimigroup.org/bimi-generator/) where you can enter your domain to ensure everything is set.

## Implement BIMI, build trust

As you can see, fully embracing BIMI is a lengthy and potentially expensive process that may test your patience.

However, leaning into this new email standard positions your brand to gain your reader’s trust while limiting the manual labor and upkeep on your end to ensure that your brand’s logo is always at the forefront of their inboxes.

As the inbox becomes a more and more competitive landscape with each passing day, anything that you can do to stand out should be done.

BIMI just might give your brand the edge it needs to capture those sought after eyeballs.
