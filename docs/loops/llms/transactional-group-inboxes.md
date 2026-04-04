# Source: https://loops.so/docs/deliverability/transactional-group-inboxes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sending transactional emails to group inboxes

> Learn how to ensure transactional emails can be delivered to your group inbox.

When sending [transactional emails](/transactional) to a group address, you may occasionally encounter issues with email delivery due to settings within your Google Workspace Admin. This guide explains how to handle these situations and prevent them in the future.

Group inboxes are intended as a catch-all email address that receives email and relays it on to many recipients. Transactional email however is intended as a one-to-one communication method and is generally not appropriate for group inboxes. As a result, group inboxes may have additional filtering in place, often by default, which impedes your ability to receive emails like 2FA, click to login and others.

These emails include transactional emails sent to your customers and users from Loops and other services, but also the emails sent by us when you log in.

Here are some steps to help you troubleshoot and prevent these issues.

## Google Workspace

### Checking for blocked emails

If you're not receiving expected emails to a group inbox, check these locations:

#### Google Groups Pending Conversations

* Go to [groups.google.com](https://groups.google.com)
* Go to **Pending** conversations in the left sidebar.
  <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=a948d6ee1539a9baa95a45170cbc0f7b" alt="Pending conversations" data-og-width="2280" width="2280" data-og-height="1079" height="1079" data-path="images/google-group-conversations.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0234b8e3101a5743aced7676b52cc730 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d856cbb3be54e46a897f218b0f0bd36b 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6dce0fb77b89a38bbc6934d5a2e6b91f 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0f691cea170d0567f74fec7a0bf42398 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=bbb04b46c344c7ee75e5cf6c530fc716 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-conversations.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=50b07d4530f98668cd52339884de2100 2500w" />
* Click the checkmark icon on the right to approve individual messages.
  <img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=0431daaaef0208ede828d2d5368f21ac" alt="Approve message" data-og-width="2280" width="2280" data-og-height="1196" height="1196" data-path="images/google-group-approve.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d2d6f7f6681687d4e08e283c79baf7a2 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=9fcc8321d66f2cc5d3d2415cab371c9c 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=91995fd06af587639b663568c85a337c 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1ccf33a63ccd298751559c0a529f324c 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b62f338afe5318a401cabd5f1ab56b23 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-approve.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=82e940bdeb912ca3e887a226ed226833 2500w" />

#### Email logs

* Check the email logs at [admin.google.com/ac/emaillogsearch](https://admin.google.com/ac/emaillogsearch)
* Search for specific emails to see their status. Look for emails labeled with "Sent for moderation".

#### Google Admin Moderation queue

* Go to [admin.google.com/moderation](https://admin.google.com/moderation) to view all quarantined email messages.
* Check the queue for emails to group inboxes.

### Preventing future issues

To prevent important emails from being blocked, you can change a setting in Google Groups.

Go to the Group settings in Google Workspace. In the **Posting policies** section, change the **Spam message handling** selection to "Post suspicious messages to the group".

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c3bd5f337d4bc3d641496b09a5f34b01" alt="Spam setting" data-og-width="2280" width="2280" data-og-height="1271" height="1271" data-path="images/google-group-setting.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=82d5a91053baa01a1f76e6c9d8425c25 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b071da7918908fcd8745be5895a76901 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=82830cf57ad837efbfd14427d1918354 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=17ff0438c1cf128201ef9afda4ad383a 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=5d424e488c3faf64764325d587063640 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/google-group-setting.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6279d43eeae4900bbcee1875b1069cfe 2500w" />

## Other troubleshooting steps

If you're still having issues:

1. Verify the email is being sent successfully. For example, in Loops you can check the **Metrics** page of your transactional email to see if the email was sent, delivered and bounced.
2. Check if the email is being received by other group members.
3. Contact your workspace administrator for assistance with group settings.

## Read more

<CardGroup>
  <Card title="About transactional email" icon="envelope" href="/transactional" />

  <Card title="Transactional guide" icon="file-code" href="/transactional" />

  <Card title="Improve your inbox placement" icon="inbox" href="/deliverability/improving-inbox-placement" />
</CardGroup>
