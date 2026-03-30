# Source: https://plivo.com/docs/aiagent/deploy/whatsapp/waba.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WhatsApp Business Account

> Onboard and link your WhatsApp Business Account to Plivo

### What is WABA?

**WhatsApp Business API (WABA)** is an official Meta (WhatsApp) solution designed to help businesses communicate with customers via WhatsApp. The setup involves creating a WABA under **Meta Business Suite**, where each WABA can have several **WhatsApp profiles**.

Each profile is associated with:

* A unique **phone number**,
* A **business-approved name** visible to customers,
* **Template messages** that are shared across all channels within the same WABA.

It’s important to note that each WABA can only be linked to a **single Meta Business Partner**. You also need to review and comply with [**WhatsApp’s Business Policy**](https://business.whatsapp.com/policy)**.**

Once you have completed these prerequisites, you can use Whatsapp channel to deploy your AI Agents.

### WABA Onboarding Process

You can onboard your WhatsApp Business Account (WABA) to Plivo via an [**Embedded Sign-Up**](https://developers.facebook.com/docs/whatsapp/embedded-signup/#the-new-embedded-signup-flow)\*\* Model\*\*. This process allows Plivo to link or create a customer's WABA, simplifying the connection.

#### Step-by-Step Onboarding

1. **Go to WhatsApp Configuration**:\
   Navigate to your **Plivo Console** and head to the **WhatsApp Configuration** section.
2. **Link Your WhatsApp Number**:\
   You will be given two options for linking your WhatsApp Business account (WABA):
   * **Connect an Existing WhatsApp Business App**
   * **Start with a New WhatsApp Business Number**

#### 1. Connecting an Existing WhatsApp Business App

**When to Use:**\
If you already have a WhatsApp Business App and want a shared messaging experience (i.e., messages sent through Plivo’s linked WABA also appear in your WhatsApp Business App) or wish to respond to users replying back to messages sent by WABA.

**Steps:**

* Select **"Connect Existing WhatsApp Business App"**.
* An embedded sign-up popup will appear.
* Enter the **registered WhatsApp Business number**.
* A QR code will display.
* You will receive a **WhatsApp message** with a button to scan the QR code.
* Scan the QR code and **agree to share chats**.
* For more details, refer to [Meta’s Embedded Signup Documentation](https://developers.facebook.com/docs/whatsapp/embedded-signup/custom-flows/onboarding-business-app-users).

#### 2. Starting with a New WhatsApp Business Number

**Option 1: Using Your Own Number**

* If you want to use your own number, enter your **number**, **Display name (**[as per WhatsApp Business Display Name Guidelines)](https://www.facebook.com/business/help/757569725593362), and **category**.
* Validate the **OTP** received on your WhatsApp Business number.
* Meta’s Embedded Sign-Up modal will appear.
* **Log in to Facebook** and click **Continue**.
* Select your **business** and either:
  * Select an **existing WABA** (Note: It will be delinked from any previously connected BSP).
  * Or **create a new WABA**.
* **Complete the process** to successfully link your WhatsApp number.

**Option 2: Using a Plivo Number**

* Rent a **Plivo number** for WhatsApp.
* Select the rented number while linking WhatsApp. Enter your **Display name (**[as per WhatsApp Business Display Name Guidelines)](https://www.facebook.com/business/help/757569725593362) and **category**.
* Enter a Number for Receiving Forwarded OTP Call from Meta.
  <Info>
    Plivo uses **Voice OTP** to verify the number with Meta.
  </Info>
* Ensure the number is available to receive Meta's OTP call.
* Enter and validate the **OTP** received on the voice call.
* Meta’s Embedded Sign-Up modal will appear.
* **Log in to Facebook** and click **Continue**.
* Select your **business** and either:
  * Select an **existing WABA** (Note: It will be delinked from any previously connected BSP).
  * Or **create a new WABA**.
* **Complete the flow** to finish the setup.

Once your WABA is linked and the profile is added, it will appear in the console under WhatsApp page in settings.
<Note>You will be able to send and receive messages on a number only when the status of the profile is **Connected**</Note>
