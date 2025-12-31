# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel/facebook-channel-manual-configuration.md

# Facebook Channel Manual Configuration

The agent developed on the Avaamo platform can be deployed on different channels. Facebook is a popular social media platform. You can deploy your agent on Facebook by clicking on the **Channels** tab on the Visual Editor.

{% hint style="info" %}
**Note**: You can also configure the Facebook channel without creating a new application. [Read more](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/facebook-channel).
{% endhint %}

Here, let us configure the Facebook Channel manually to add your application.

* Open a browser and go to [developer.facebook.com](https://developers.facebook.com/)
* Login with your Facebook login credentials.
* Click on **My Apps** and select your product.
* Click on **Create a New App**.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3ErcR_sn1nAY1kJU8%2F-Ly3FKRUA2S13G4PWkFM%2Fagent-deploy-fb-manual-1.png?alt=media&#x26;token=08f40407-ee6f-43a1-be32-24b8c5222bfc" alt=""></div>

* Enter a **Display Name**.
* Click on **Create App ID**.&#x20;
* In the **Settings -> Basic** page, select the checkbox for **Get Started with the Pages API** and click on Confirm.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3ErcR_sn1nAY1kJU8%2F-Ly3FXwo1x5DjtvUYY2H%2Fagent-deploy-fb-manual-3.png?alt=media&#x26;token=05ff9c9e-7ece-4726-bc62-8ebe3b4dc9a9" alt=""></div>

* Now, you can add an App Icon, Enter the Avaamo URL for Terms of Service URL and Privacy Policy URL. You can also choose a category, and make the required changes. And click on **Save Changes**.

### **Page Access Token**

The manual configuration of the Facebook Messenger as a channel on the Avaamo platform requires a Page Access Token. To generate a token on [developers.facebook.com](https://developers.facebook.com/) and configure the same on Avaamo UI follow the steps below:

* Click on **Dashboard** on the left pane and go to **My Products**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3ErcR_sn1nAY1kJU8%2F-Ly3FoLdk_zEZMzRaf-P%2Fagent-deploy-fb-manual-4.png?alt=media\&token=e48659cf-4817-440b-bbfa-05034f9abf14)

* Click on **Settings** under Messenger. Under **Token Generation** select the page you want to create the token for (from the drop-down list) and the **Page Access Token** is generated.

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3ErcR_sn1nAY1kJU8%2F-Ly3FufKuN0uWqv9fEHO%2Fagent-deploy-fb-manual-5.png?alt=media&#x26;token=90c1850b-a6f0-4eea-aa07-6979c8142128" alt=""></div>

Now, on the Avaamo UI, go to the Visual Editor and click on Channels. Click on Connect under Facebook Messenger.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3ErcR_sn1nAY1kJU8%2F-Ly3G2kH2HpmS7Tn7h08%2Fagent-deploy-fb-manual-6.png?alt=media\&token=f5be1453-be2a-4fd5-839a-bb7cbbc26d2c)

\
On the popup window, select the slider for Yes to enable **Manual Configuration**.

* Enter the Page Name of the Facebook page.
* Enter the App ID of the Facebook page.
* Enter the Page Access Token, and click on Save. The Channel Settings are saved and the Webhook URL is generated.

### **Webhook**

The Webhook setup requires the Callback URL from the Avaamo platform. So, on the Channels page click on **View** under Facebook Messenger. The Channel Settings popup window has the Webhook URL details required to set up Webhook on [developers.facebook.com](https://developers.facebook.com/).

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3G9sQoX7QR6pxLs16%2F-Ly3GKH8dAo0Pz7or_s9%2Fagent-deploy-fb-manual-7.png?alt=media&#x26;token=27a00200-71df-4476-891f-90783dd64f26" alt=""></div>

To set up the Webhook URL, click on **Dashboard** on the left pane and go to **My Products**. Click on Settings under Messenger.

Under Webhooks, click on **Setup Webhooks**.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3G9sQoX7QR6pxLs16%2F-Ly3GT5ApNuT5YOThZNx%2Fagent-deploy-fb-manual-8.png?alt=media\&token=8d1cdca1-5fc2-448b-8034-3c02fd2d2e05)

On the New page Subscription popup window,

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-Ly3G9sQoX7QR6pxLs16%2F-Ly3G_pDZ-mY4Ac3oAF9%2Fagent-deploy-fb-manual-9.png?alt=media\&token=5fa4550b-7c94-4ad3-9bf3-897e62b2eed6)

* Enter the Callback URL and Verify Token from Channels page on Avaamo UI.
* Select the checkboxes under **Subscription Fields**, and click on **Verify and Save**.

Subscribe to the page under Webhooks and you are ready to use your agent on Facebook Messenger.
