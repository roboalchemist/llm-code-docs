# Source: https://documentation.onesignal.com/docs/en/google-postmaster-tools.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Postmaster Tools

> Set up Google Postmaster Tools to monitor Gmail spam rates and domain reputation — data Gmail does not share directly with email senders.

Google Postmaster Tools is the only way to see your spam rate and domain reputation with Gmail. Unlike other inbox providers, Gmail does not report per-user spam complaints or bounces back to email senders like OneSignal. Instead, Google Postmaster Tools provides aggregate data you can use to monitor and improve your [email deliverability](./email-deliverability).

Gmail is the largest inbox provider in the world, making this data essential for understanding how your emails perform.

## How to connect Google Postmaster Tools

<Steps>
  <Step>
    Go to [https://gmail.com/postmaster/](https://gmail.com/postmaster/) and **click "Get Started"**.
  </Step>

  <Step>
    **Input the *subdomain*** that you have set up with OneSignal.

    <Frame caption="mail.domain.com (subdomain) vs domain.com (root domain)">
      <img src="https://mintcdn.com/onesignal/MUgio66t0sYhGEvj/images/docs/6eaddd7cd7359d13da9938ca83bb4894875cf0a8c0554fce8c7cf4ccd3bb2b93-Domain_input_GPT_2.png?fit=max&auto=format&n=MUgio66t0sYhGEvj&q=85&s=6a68deebd2a01c99ffa80f7dc34ea0d9" alt="Google Postmaster Tools domain input showing subdomain vs root domain" width="600" height="560" data-path="images/docs/6eaddd7cd7359d13da9938ca83bb4894875cf0a8c0554fce8c7cf4ccd3bb2b93-Domain_input_GPT_2.png" />
    </Frame>
  </Step>

  <Step>
    **Click "Next"** and Google will provide a TXT record for you to create in your DNS records.

    * Create this record in your DNS registrar to verify ownership of the domain.
  </Step>

  <Step>
    Once you have created the provided TXT record in your DNS records, **click "Verify"**.
  </Step>

  <Step>
    Lastly, add `mailmonitor@onesignal.com` as a **"managed user"**.

    * This gives OneSignal view-only access to help monitor your reputation on your behalf.

    <Frame caption="Click &#x22;Managed Users&#x22;">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a4e3c41a18a8c0ecb80af1f2550a661a5212fded4b727b9c1ea4bd9c4a9fc554-Spam_Rate_GPT_1.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=40cdcf5fb5c4e9a38cc692ec10396552" alt="Google Postmaster Tools interface showing the Managed Users option" width="1024" height="313" data-path="images/docs/a4e3c41a18a8c0ecb80af1f2550a661a5212fded4b727b9c1ea4bd9c4a9fc554-Spam_Rate_GPT_1.png" />
    </Frame>

    <Frame caption="Add mailmonitor@onesignal.com as a managed user">
      <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a6c96f16ac36fd33714a40e457cea95c18bbfafcbb3463938661947d304b4cce-Spam_Rate_GPT_2.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=1947f848af539f36e74412f7df528a65" alt="Adding mailmonitor@onesignal.com as a managed user in Google Postmaster Tools" width="601" height="584" data-path="images/docs/a6c96f16ac36fd33714a40e457cea95c18bbfafcbb3463938661947d304b4cce-Spam_Rate_GPT_2.png" />
    </Frame>
  </Step>
</Steps>

***

## Monitor spam rate

This Gmail spam rate is separate from the spam metrics shown in your OneSignal dashboard.

If your emails are landing in Gmail spam folders, Google Postmaster Tools may offer insight.

The spam rate represents the percentage of your mail volume that Gmail recipients actively reported as spam on a given day.

This data is aggregated by Google and does not identify individual recipients who reported spam.

Google states: *"Keep spam rates reported in Postmaster Tools below 0.10% and avoid ever reaching a spam rate of 0.30% or higher."* — [Email Sender Guidelines](https://support.google.com/a/answer/81126?hl=en#spam-rate)

<Frame caption="Gmail spam rate">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/63568bcc52035527c85dc47ddd5bf62fadffe6025a8205978ef51b52696e8efb-Spam_Rate_GPT.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=1e984d7ef1dfe5ca88400672a391323e" alt="Google Postmaster Tools chart showing a healthy Gmail spam rate" width="2110" height="1128" data-path="images/docs/63568bcc52035527c85dc47ddd5bf62fadffe6025a8205978ef51b52696e8efb-Spam_Rate_GPT.png" />
</Frame>

The following example shows a consistently high spam rate, with peaks regularly exceeding Google's recommended thresholds.

<Frame caption="Very high Gmail spam rate">
  <img src="https://mintcdn.com/onesignal/9_Q1FZLh6C0BFLq-/images/docs/c8c3b2c44f82c68918737abb644be32fc7343b66406a9434cce68577be223454-Poor_Spam_Rate.png?fit=max&auto=format&n=9_Q1FZLh6C0BFLq-&q=85&s=d16ebc54ab43e2bc3b1f503f74c94336" alt="Google Postmaster Tools chart showing a dangerously high Gmail spam rate" width="6808" height="1796" data-path="images/docs/c8c3b2c44f82c68918737abb644be32fc7343b66406a9434cce68577be223454-Poor_Spam_Rate.png" />
</Frame>

<Card title="Email reputation best practices" icon="shield-check" href="./email-reputation-best-practices">
  Follow these best practices to lower spam complaint rates and improve deliverability.
</Card>

***

## FAQ

### Why does Google Postmaster Tools show 0% or no data for my domain?

Google Postmaster Tools requires a minimum daily email volume to Gmail before it displays data. If you're sending low volumes, you may not see any metrics.

If you do have sufficient volume, check that you added the correct domain. Data appears for the domain used in the visible "From" address header of your email, not necessarily your return-path or SMTP sending domain. Although you send from your "sending domain," the *from* address in the header may be different, causing the sending domain to show 0%.

<Frame caption="Authentication Dashboard details from Google Postmaster for reference">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/475485b2871a3bcfe5a5812d5474813a09144e952c628708f212710b9916c021-Screenshot_2024-12-13_at_10.01.07_AM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=bfdaf6f92512ffdb0cffa08d932b0edb" alt="Google Postmaster Tools Authentication Dashboard showing domain details" width="720" height="748" data-path="images/docs/475485b2871a3bcfe5a5812d5474813a09144e952c628708f212710b9916c021-Screenshot_2024-12-13_at_10.01.07_AM.png" />
</Frame>

### How often is Google Postmaster Tools data updated?

Google Postmaster Tools updates data daily, typically with a 1–2 day delay. You will not see same-day data.

### What do the domain reputation levels mean?

Google Postmaster Tools rates your domain as **High**, **Medium**, **Low**, or **Bad** based on your sending history and spam rates:

* **High** — Good sending history with a very low spam rate.
* **Medium** — Good sending history, but has occasionally generated spam.
* **Low** — Known to send a considerable volume of spam regularly.
* **Bad** — History of sending a high volume of spam. Emails from this domain will almost always be rejected or filtered to spam.

If your reputation drops to Low or Bad, review the [email reputation best practices](./email-reputation-best-practices) to identify the cause. See [Google's domain reputation documentation](https://support.google.com/a/answer/9981691) for more details.

### What should I do if my spam rate is above 0.10%?

Review the [email reputation best practices](./email-reputation-best-practices) to identify and fix the cause. Common steps include verifying your [opt-in process](./email-reputation-best-practices#set-up-a-clear-opt-in-process), [sunsetting unengaged recipients](./email-reputation-best-practices#exclude-or-sunset-unengaged-recipients), and [controlling send frequency](./email-reputation-best-practices#control-send-frequency).

***

Built with [Mintlify](https://mintlify.com).
