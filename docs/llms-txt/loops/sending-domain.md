# Source: https://loops.so/docs/sending-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up your domain

> Steps for adding a sending domain to your account.

When you set up your account for the first time, you need to set up your domain records in order to start sending email. We'll be sending email on your behalf, so we need to verify that you own the domain you're sending from.

Here's how to set it up in just a few steps.

## Step 1: Add your sending domain

During the sign up flow, you are asked to specify your desired sending domain. You can enter any domain here that you can set up DNS records for, and if you choose a subdomain, it doesn't need to exist yet.

We [recommend using a subdomain for this](/deliverability/sending-from-subdomain), e.g. `mail.yourcompany.com`, rather than sending from your root domain `yourcompany.com`.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=488ba76f344c60b0c9b5dd6bd7c21ff3" alt="Adding a domain during sign up" data-og-width="2280" width="2280" data-og-height="1967" height="1967" data-path="images/signup-domain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ec2a74c5ff0f86afeda25d375ab5c26d 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=51fd95cde921614cbe67fed194f36560 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=371346266dff06d4663f932c7467036b 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=ca82607d060c86ca0f15a121c8fa64bb 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=f17618833a8261e2d1dd8dc0d65dc221 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/signup-domain.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=4e49608a5096314ece1bbf4de301b588 2500w" />

If you have already signed up and want to edit your sending domain, you can do so from **Settings -> Domain**.

<Note>
  You do not need to create this subdomain with an A or CNAME record. Loops will
  provide all DNS records you need to set up.
</Note>

## Step 2: Set up your records

From the **Settings -> Domain** page, click **View records** (or [click this link](https://app.loops.so/sending-domain) to go directly).

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=269363c1164a7eea0dc5b7dcd8bc23e2" alt="" data-og-width="2280" width="2280" data-og-height="876" height="876" data-path="images/domain-records.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=58eb22e5d8cd7677b4b2d0170ade0b91 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=7b834c498e1adb519bdc0a9aefd30ba9 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=e7d21d43f6dd8f0ba425536cc977e462 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=8395da22c44ea3b8db4a2a7330f4a2c9 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=45b16de765aeb19b10daca6900bf7ed5 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/domain-records.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=08c700ae39f476592f6ba9024191ab22 2500w" />

On this page, you'll see a few things.

**Your records**

These are SPF, DKIM and MX records that need to be set up in your domain zone editor inside of your domain registrar like Namecheap, Google Domains, AWS, Godaddy or elsewhere.

Next to each record is a clipboard icon. You can use this to copy the records to your clipboard and easily paste them into your domain registrar.

**Your sending domain**

This is indicated below by “yourcompany.com”. This will have your domain listed. If you'd like to change domains, you can do so in the [account settings](https://app.loops.so/settings).

**A verify records button**

Once you have copied your records to your registrar, click this button to verify they have been set up correctly.

<img src="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=8e6ea3307b22861a150399f7b99c95e3" alt="" data-og-width="2280" width="2280" data-og-height="2630" height="2630" data-path="images/set-up-records.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=280&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=be2f8fc7aafc84731138097965f3ecd1 280w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=560&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=872cdb55a8dbeb9571f1a81179719539 560w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=840&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=c45acf4fff2aaaccb7a9fcb6ca6c3e15 840w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=1100&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=375547f4561f366b95099c01eb14551c 1100w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=1650&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=798db9a9094a02926b68e4bbd6de8a78 1650w, https://mintcdn.com/loops/Z7viZoAUCPxaqCl2/images/set-up-records.png?w=2500&fit=max&auto=format&n=Z7viZoAUCPxaqCl2&q=85&s=9587b503245626056828eaf9befc62a0 2500w" />

## Step 3: Add your domain records

Copy and paste the records one by one into your registrar.

You want to use the **Type** (indicated as TXT, CNAME and MX) in setting up your records, ***not*** the title of the record e.g. SPF, DKIM, MX.

<Tip>
  Loops' records for SPF are at envelope.sendingdomain.com, meaning they won't
  collide with any other SPF records you have set up. We specify a DMARC record
  so that you have one, but you can also just have a single DMARC at the root
  domain level.
</Tip>

<AccordionGroup>
  <Accordion title="Cloudflare">
    DNS records can be added from the "DNS" page within a website.

    Click **Add record** to open the form. Select a "Type" (TXT, MX or CNAME), then paste the "Name" and "Value" information.

    [Read the guide](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records)

    Be sure to set the proxy to “DNS Only” for the CNAME records:

        <img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=fdb8807679ab016c001fa0e7ba3df89e" alt="" data-og-width="480" width="480" data-og-height="226" height="226" data-path="images/cloudflare.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f71643e0d4f176c9c263464a35dd4f19 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d6d53ce5eb1dd296a9936273004bc409 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=21e37599fae71f362985000fe1b1a301 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d4689ecdc46a6096f69ecb81dcc27fd4 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ce7311d2341bd89de4423380eb92dea2 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/cloudflare.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d57bdf58d22f921a8d856b7e1f9b687e 2500w" />
  </Accordion>

  <Accordion title="Dreamhost">
    Dreamhost is currently unsupported in full because you cannot add custom MX records.
  </Accordion>

  <Accordion title="GoDaddy">
    For GoDaddy, [read this guide](https://www.godaddy.com/help/manage-dns-records-680).
  </Accordion>

  <Accordion title="Google Domains">
    Google Domains (and potentially other providers) combine the mail server and
    priority inputs into a single line. So if you receive an error like this when
    setting up the domain, make sure to instead type out the input like this: `10
                feedback-smtp.us-east-1.amazonses.com`

        <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=4c026c03bb8213d98399ed9fef9cc098" alt="" data-og-width="1440" width="1440" data-og-height="207" height="207" data-path="images/google-domains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=7103684505d4a140c787b2a5cd06a18b 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=8650abcf15881535281400cc12b431ae 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=f4767f4ba664e892a45c58c120c9dc32 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=5d782ce442ccc9ceb1bda8117fb6e153 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0f1c425ef717bbadd5e9b18dc93d5523 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-domains.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=fbe6c4af7b7dd81043c6bbb4a4070d1c 2500w" />

    Google domains will also include quotes “ “ around some record names. This is
    expected and will not impact anything.
  </Accordion>

  <Accordion title="Namecheap">
    Go to the **Advanced DNS** page for your domain.

    If you are using the automatic Gmail/Gsuite integration with Namecheap, you
    will need to disable the automatic integration and switch to **Custom MX** in the **Mail Settings** dropdown. You then need to [add an MX record](https://support.google.com/a/answer/174125#current\&legacy\&zippy=%2Cgoogle-workspace-current-version-later) to set up Gmail on your domain again.

    Then you can add Loops' MX records by clicking **Add new record** in the "Mail Settings" section and pasting in the values provided in Loops. Click the `✓` icon to save each record.

        <img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=eeff1ebe96df42d3b1386182f01d831a" alt="" data-og-width="1440" width="1440" data-og-height="457" height="457" data-path="images/namecheap-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=9a5cdb351c9a3450b7fb2231b93aad81 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=2185ffb63af5699ad9361c5b8ec8d17e 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=64097f30a55cb969715ce64a91b2c4a5 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=4c056c259ae37d0443acab3645799337 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=0985a9b93027af2db8f0a6cf362483c0 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-1.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=651279fd135081cb6edf584e75705fc4 2500w" />

    Add the TXT and CNAME records by clicking **Add new record** in the "Host Records" section.

        <img src="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=225bf3773e28b2a1165afaa095bfbd4f" alt="" data-og-width="860" width="860" data-og-height="381" height="381" data-path="images/namecheap-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=280&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=87715c9c078fa62ff3f3dd4101953d3b 280w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=560&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f8daa8a2c45add070eb5630280d8ca14 560w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=840&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f67291e77d8bb01b4457e285373a61c4 840w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=1100&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=cf4d3f3fc762888d0834137c8243d156 1100w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=1650&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=6ffb063011bd4fe6fd5624b8f22159ac 1650w, https://mintcdn.com/loops/W7EWSDUW0GR-XWrp/images/namecheap-2.png?w=2500&fit=max&auto=format&n=W7EWSDUW0GR-XWrp&q=85&s=f546ee50685a12d588a01ae1a993c1d5 2500w" />
  </Accordion>

  <Accordion title="Route 53">
    For Route 53, [read this guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html).
  </Accordion>

  <Accordion title="Squarespace">
    For adding your records to Squarespace, [read this guide](https://support.squarespace.com/hc/en-us/articles/31120985010957-DNS-records-for-email#toc-option-2---add-custom-records-manually).

    Note that you might need to trim a trailing period from the record values.
  </Accordion>

  <Accordion title="Wix">
    Unfortunately, Wix DNS [does not support subdomains](https://support.wix.com/en/article/request-connecting-a-mailbox-to-a-subdomain) for MX records when your nameservers are pointed at Wix.

    If you purchased a domain outside of Wix, you should use the ["Pointing" method](https://support.wix.com/en/article/connecting-a-domain-to-wix-using-the-pointing-method) for your domain, which will let you set up DNS records externally a domain registrar. Then you can add records using [this guide](https://support.wix.com/en/article/managing-dns-records-in-your-wix-account).
  </Accordion>
</AccordionGroup>

<Tip>
  Make sure you enter the “Priority” while setting up your MX record. In most
  registrars this is done by formatting it like “10 pastedrecordname”.
  Occasionally you will be asked to place it on a separate line. Just make sure
  to read the instructions on the page as you set up your MX record and if you
  have any questions, just ping [help@loops.so](mailto:help@loops.so)
</Tip>

## Step 4: Verify your records are set up correctly

After you have copied and pasted your records into your domain registrar, click **Verify Records** at the bottom of the page to check your configuration is correct.

<Tip>
  Sometimes records can take up to an hour to propagate across all the servers.
  During that time you may see different records validate. This is totally
  normal, just check back later.
</Tip>

If the domain is set up correctly, you should see a page like the one below. If not, check back soon; sometimes records can take some time to propagate.

Notice the "Records present" in green next to each record section.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=50400ef754d6398f725ccbbcfecdec3c" alt="" data-og-width="2280" width="2280" data-og-height="2475" height="2475" data-path="images/verified.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a32bef575528c365a08441405bf40441 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=c92a51db6015047e0020acb44762117e 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=b204efdc894ae929dfd3ae8c18cc0584 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=880774ed221780820237a45078cd2805 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=69d0812d40a255614b57b072e9c47950 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/verified.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=80efa3690c3a6724c213f93223dacb00 2500w" />

## Domain already in use

If you're getting a "domain already in use" error when trying to set up your domain, this typically means someone on your team has already registered an account with Loops using your domain.

Here are the steps you can take to resolve this:

<AccordionGroup>
  <Accordion title="Signing in with another account">
    Go to the [Loops login page](https://app.loops.so/) and request a login link using your email address.
  </Accordion>

  <Accordion title="Search your inbox">
    Search for `loopsbot@mail.loops.so` in your email inbox(es) to see if you have received other registration or login emails from Loops.
  </Accordion>

  <Accordion title="Check with your team">
    Ask your teammates if someone has already set up a Loops account for your organization. If so, ask them to invite you to the existing account.
  </Accordion>
</AccordionGroup>

If you've tried all these steps and still can't access your domain, [contact our support team](mailto:help@loops.so) for manual assistance.

<Tip>
  Confused or have questions? Just shoot us an [email](mailto:help@loops.so) 🙂
</Tip>
