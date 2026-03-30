# Source: https://plivo.com/docs/voice/concepts/whatsapp-calling.md

# Source: https://plivo.com/docs/messaging/concepts/whatsapp/whatsapp-calling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up WhatsApp Calling via Plivo

> Enable inbound and outbound voice calls on WhatsApp Business numbers

Enable voice calling on your WhatsApp Business numbers to connect with customers directly through WhatsApp.

**Time to complete:** \~15 minutes

## Quick Start

**What you’ll build**

* Inbound calling: Receive calls from users through your WhatsApp Business number
* Outbound calling (Business Initiated Calling): Initiate calls to users (with proper permissions)

**Prerequisites**

* Plivo account - [Request Trial](https://www.plivo.com/request-trial/)
* WhatsApp Business Account linked to Plivo. [Follow these steps](https://www.plivo.com/docs/messaging/concepts/whatsapp/waba-onboarding)
* A WhatsApp-enabled phone number
* A server endpoint to handle webhooks (for testing, use[ ngrok](https://ngrok.com/) or similar)

### Part 1: Receiving Inbound Calls (User-initiated Calls)

**Step 1: Create a Plivo XML Application**

1. Navigate to [Voice -> Applications -> XML](https://cx.plivo.com/xml-applications) -> Add New Application
2. Configure the application

* ***Application Name: WhatsApp Calling Application***
* ***Primary URL: [https://yourdomain.com/receive\_call/](https://yourdomain.com/receive_call/) (Replace this with your actual call URL)***
  * *This endpoint receives call events*
  * *Must return a valid Plivo XML*
* Hangup URL(Optional): URL called when the call ends
* Fallback URL(Optional): Backup URL if Primary fails

3. Click **Create Application**

**Step 2: Enable Calling on Your WhatsApp Number**

1. Go to [WhatsApp > WhatsApp Business Account](https://cx.plivo.com/whatsapp/numbers)
2. Click Enable Calling next to your phone number

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa1.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=e35fa2b798c2ba92e7d57375c360f243" alt="" width="911" height="117" data-path="images/wa1.png" />
</Frame>

3. Select the XML application you created: `WhatsApp Calling Application`

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa2.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=fd585a74da527824077649af39ebbc12" alt="" width="597" height="367" data-path="images/wa2.png" />
</Frame>

4. Click **Save Configuration**
5. Once calling is enabled:
   1. ✅ You should now see a call button next to your WhatsApp number on WhatsApp

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa3.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=6924def568f03ec7b11f6d8ac7dfc188" alt="" width="745" height="193" data-path="images/wa3.png" />
</Frame>

**Step 3: Configure Calling Hours**

Set when users can call your business number:

1. Open **Meta Business Manager → WhatsApp Manager → Phone Numbers**
2. Select your number → **More → Calls → Available call hours**
3. Configure your business hours

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa4.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=6ef993254d6a6e1a4b7f8efdea9f9d95" alt="" width="1186" height="675" data-path="images/wa4.png" />
</Frame>

**Step 4: Test Inbound Calls**

1. Call your WhatsApp Business number from any WhatsApp account:
2. Verify:

* Call connects successfully
* Audio is routed to your configured endpoint
* Two-way audio works

**Troubleshooting:** Check **Voice → Call Logs** in the Plivo console if issues occur.

### Part 2: Making outbound calls (Business Initiated Calls)

**Understanding Callback permissions**

**Important:** As per Meta guideline, you must obtain explicit permission before calling a WhatsApp user.

#### **Permission Methods**

**Method 1: Request Permission via Message**

Send a permission request using a WhatsApp template message / free-form message (see Step 1 below).

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa5.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=099548cd154e992dc8a1b3b9013014e1" alt="" width="1228" height="816" data-path="images/wa5.png" />
</Frame>

\*\*Create a callback request permission template: \*\*

1. Go to your Meta Business Profile > WhatsApp Manager > Manage Templates > Create Template

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa6.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=1b275fb96116f6947cf31b92de3ce9f3" alt="" width="1031" height="246" data-path="images/wa6.png" />
</Frame>

2. Select the Calling permissions request under Marketing or Utility

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa7.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=f177cf16175f19b170764d742523eed2" alt="" width="1102" height="601" data-path="images/wa7.png" />
</Frame>

3. Configure the template and submit for approval.

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa8.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=ada710c9cc0f3261d9fa45a475454a2d" alt="" width="1599" height="887" data-path="images/wa8.png" />
</Frame>

**Method 2: Automatic Callback Permission**

When a user calls your business first, they automatically grant temporary callback permission (if enabled on your number in Meta Business Manager).

<Frame>
    <img src="https://mintcdn.com/plivo/9TcugqK5W7G3A-xp/images/wa9.png?fit=max&auto=format&n=9TcugqK5W7G3A-xp&q=85&s=a86e7e3cc227a8953a53585d337957c8" alt="" width="1638" height="816" data-path="images/wa9.png" />
</Frame>

**Placing a call:**

Refer to the [Plivo XML Dial element](https://www.plivo.com/docs/voice/xml/dial) to configure and place an outbound call

Use [Plivo's XML \<Dial> element](https://www.plivo.com/docs/voice/xml/dial) to initiate calls:

#### **Required Parameters**

| **Parameter** | **Description**                                          | **Example**                 |
| ------------- | -------------------------------------------------------- | --------------------------- |
| `callerId`    | Your WhatsApp Business number (must be WhatsApp-enabled) | `"918035737458"`            |
| `callType`    | **Must be** `whatsapp` for WhatsApp calls                | `"whatsapp"`                |
| `<User>`      | Recipient's WhatsApp phone number (E.164 format)         | `<User>919412341234</User>` |

## **Limitations & Restrictions**

### **Meta Restrictions**

#### **Geographic Restrictions**

**Outbound calls are NOT available** from business numbers in:

* 🇺🇸 United States
* 🇨🇦 Canada
* 🇹🇷 Turkey
* 🇪🇬 Egypt
* 🇳🇬 Nigeria
* 🇻🇳 Vietnam

⚠️ **Important:** This restriction applies to your **business phone number's country code** only. Users can call from any country where the WhatsApp Cloud API is available.

#### **Call Routing**

* Calls **cannot** be forwarded to PSTN (traditional phone) numbers
* Calls **must** be answered via a Cloud platform
* WhatsApp-to-WhatsApp call forwarding is not supported

#### **Capacity Limits**

* **Maximum concurrent calls:** 1,000 simultaneous calls per WhatsApp Business number
  * Other than this, your Plivo account's [CPS (Calls Per Second)](https://support.plivo.com/hc/en-us/articles/22640156915609-Calls-per-Second-CPS) limits apply to all calls combined (including WhatsApp calls). Check your CPS limits [here](https://cx.plivo.com/home).

#### **Permission Rules**

| **Rule**                | **Limit**            | **Details**                  |
| ----------------------- | -------------------- | ---------------------------- |
| **Request frequency**   | Once per 24 hours    | Maximum 2 requests in 7 days |
| **Calls allowed**       | 5 calls per 24 hours | After permission granted     |
| **Permission duration** | 7 days               | From approval date           |
| **Auto-revocation**     | After 4 missed calls | Consecutive missed calls     |

**Permission expires in these scenarios:**

1. **Time-based expiration**
   * 7 days after approval, rejection, or no response
2. **New permission granted**
   * When a new call permission request is approved
3. **Missed call warnings**
   * After 2 consecutive missed calls → User prompted to reconsider permission
   * After 4 consecutive missed calls → Permission automatically revoked
