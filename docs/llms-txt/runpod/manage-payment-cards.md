# Source: https://docs.runpod.io/references/troubleshooting/manage-payment-cards.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage payment card declines

> Learn how to troubleshoot declined payment cards and prevent service interruptions on Runpod.

Payment card declines can occur when adding funds to your Runpod account. Credit card processors apply stringent fraud detection standards, particularly for international transactions. This document provides guidance to help you troubleshoot payment issues.

## Keep your balance topped up

To prevent service interruptions, refresh your balance at least a few days before it runs out. This gives you time to address any payment delays.

You can enable automatic balance refresh from the [Billing page](https://www.console.runpod.io/user/billing):

<Frame caption="">
  <img src="https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=6d8aab60eb54137d723a0fba8d107f70" data-og-width="874" width="874" data-og-height="262" height="262" data-path="images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=280&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=a1cb67032cf9022f35c70f12213313b4 280w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=560&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=63b8ec6dd18b0a99b5ca8ca47b37b064 560w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=840&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=26baae30aa56cc86fb9ae73435bba21c 840w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=1100&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=19575d64115fbeea18e6ec11ee73ea81 1100w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=1650&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=057290213e2a5591f8dff70cd815df6f 1650w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/a3d8a093-739337f-image-0c08fb3431d388762ce79a8769ef4ca0.png?w=2500&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=7572b12805e253d4ecaa0f2fb08e34b1 2500w" />
</Frame>

## Contact your card issuer

If your card is declined, contact your issuing bank to determine the reason. Due to privacy standards, payment processors only indicate that a transaction was not processed without providing specific details. Your bank can tell you why the payment was declined.

Card declines often occur for routine reasons, such as anti-fraud protection. Your bank can resolve blocks they have placed on your card.

<Warning>
  Contact your bank about the initial decline before trying a different card. The payment processor may block all funding attempts from your account if it detects multiple card declines, even if those cards would otherwise work. These account blocks typically clear after 24 hours.
</Warning>

## Other reasons for card blocks

The payment processor may block cards based on user risk profiles. Using several different cards within a short period or having disputed transactions in the past may trigger card declines.

For a list of supported card brands, see [Stripe's supported cards documentation](https://stripe.com/docs/payments/cards/supported-card-brands).

## Contact support

If you're still having trouble after checking with your bank, contact [Runpod support](https://www.runpod.io/contact) for assistance.
