# Source: https://resend.com/docs/send-with-customer-io-smtp.md

# Send emails using Customer.io with SMTP

> Learn how to integrate Customer.io with Resend SMTP.

### Prerequisites

To get the most out of this guide, you'll need to:

* [Create an API key](https://resend.com/api-keys)
* [Verify your domain](https://resend.com/domains)

## 1. Get the Resend SMTP credentials

When configuring your SMTP integration, you'll need to use the following credentials:

* **Host**: `smtp.resend.com`
* **Port**: `465`
* **Username**: `resend`
* **Password**: `YOUR_API_KEY`

## 2. Integrate with Customer.io SMTP

After logging into your [Customer.io](https://customer.io) account, you'll need to enable the SMTP integration.

1. Go to **Settings** > **Workspace Settings**.

<img alt="Customer.io SMTP - Workspace Settings" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=97d3402e7acb7c66e5d54ff2886dd4e3" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/customer-io-smtp-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5b4635f750141488e068de1bf5140e05 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=4e656440fb0ff1afbd61a0d7ca275da2 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b008e95e151cceefc61d59cb50aa75d1 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=fce421ab414cdce4b2cf5390caf8ee33 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=2253c58f47a395826a3b7886838a6009 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-1.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=b7b18c99ca7c6e92fc5ab460e9a401ae 2500w" />

2. Go to the Messaging tab and select **Email**.

<img alt="Customer.io SMTP - Email" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=af35d8a9c99681e1a508694f02157943" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/customer-io-smtp-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=d6e2a6cfd4f3ad9618a98067e27801b9 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=6b41245943a57c055e7eaec6f84abc9f 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=3cdda8dce7097c4a86ae3b1100786b61 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=6e362e3c8d92ad027ef58d69462cc03b 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7c77742324264b5be8c550a2193b59b4 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-2.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=80076cea4c6b508491a4c4c79102afab 2500w" />

3. Select the **Custom SMTP** tab and click **Add Custom SMTP Server**.

<img alt="Customer.io SMTP - Add Custom SMTP Server" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=1d18082018463dc5989fb91d8f881b39" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/customer-io-smtp-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=66704ff0ca38c530b6f19801d021414e 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=0d75ab03f8555f83ae6b88467a8ba4cc 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=52c959b9b7bb5e4e374ff0a923cbb269 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=cfc6ac8025e122da1b554cecbcafd877 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a99d2c1bf62ef8858e08f495b38c222b 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-3.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=0829001dadb1d1198692e407dce2b25f 2500w" />

4. Select **Other SMTP** and click **Continue to set up**.

<img alt="Customer.io SMTP - Other SMTP" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=acc404b8b5b7fc11db0279d84453cb11" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/customer-io-smtp-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=7c40495f7483f2894f864ec5565ef481 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a71ddd0a726fe8559032ef5cee6e7da6 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=328829343fba2ccd7baa6403219b6960 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=92fd0a866aa4aa6caa9507821b4aecc8 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=36d7b59d088e39300e385f66770cea92 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-4.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=cf18f0846dce50c6e77300a32a255bed 2500w" />

5. Copy-and-paste the SMTP credentials from Resend to Customer.io.

<img alt="Customer.io SMTP integration" src="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=519742fc4d97d06646fdd52de4f373fd" data-og-width="3414" width="3414" data-og-height="1886" height="1886" data-path="images/customer-io-smtp-5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=280&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=df9d92806579bad07df23eca1bd2ab5d 280w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=560&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=a6044b5b5d6c76d59da01c768e6a37d5 560w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=840&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=3880624e319f52746eb77b4ef0e55e68 840w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=1100&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=23a7d220764020c7e5f280a3d12494df 1100w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=1650&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=ed453e0aa17c6b72d4504d31105e4942 1650w, https://mintcdn.com/resend/ABWmVTZIHGIFNTFD/images/customer-io-smtp-5.png?w=2500&fit=max&auto=format&n=ABWmVTZIHGIFNTFD&q=85&s=5b3c4fc8021d5014c17933304db43021 2500w" />
