# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/whatsapp.md

# WhatsApp

WhatsApp Messenger is a freeware and cross-platform messaging with Voice over IP (VoIP) service. The application runs from a mobile device but is also accessible from desktop computers; the service requires its users to provide a standard cellular mobile number.

{% hint style="info" %}
**Note**: You can connect to a channel only if it is enabled for your account or company. If you wish to enable a channel, then contact Avaamo Support for further assistance. Note that only the web channel is enabled by default.&#x20;
{% endhint %}

The agents built on the Avaamo Platform can be deployed on WhatsApp. In this article, the following steps are detailed:

1. [Before you begin](#before-you-begin)
2. [WhatsApp Registration](#whatsapp-registration)
3. [Deploy your agent to WhatsApp channel](#deploy-your-agent-to-whatsapp-channel)
4. [WhatsApp Business API Configuration](#whatsapp-business-api-configuration)
5. [Manage channel settings](#manage-channel-settings)

## Before you begin

The process to integrate WhatsApp with the Avaamo platform requires the prerequisites of the **WhatsApp Setup** (business and technical) and **Avaamo Integration**.

### **WhatsApp Business Setup**

* [Set up your WhatsApp Account on the Facebook Business Manager](#set-up-your-whatsapp-account).
* [Add a Phone Number to your WhatsApp Account](#phone-number).
* [Add a Verified Name to your WhatsApp Account](#add-verified-name).

#### **Set up your WhatsApp Account**

Login into your **Facebook Business Manager** account to set up the WhatsApp account.

{% hint style="info" %}
**Note**: See [Create a WhatsApp Account](https://www.facebook.com/business/help/2087193751603668?id=2129163877102343), for detailed information on setting up the WhatsApp account.
{% endhint %}

#### **Phone Number**

Every WhatsApp account must have a phone number. The phone number that you intend to use with WhatsApp must have no previous registration or affiliation with WhatsApp. There are three types of phone numbers you can use for this product:

* Landlines - The landline numbers can be used if the developers have access to them and can answer a phone call if required during the setup process.
* Cellular - The cellular numbers can be used only if the number has not been used on WhatsApp in the last 6 months.
* 1-800 or toll-free numbers - The toll-free numbers can be used only if the number is capable of receiving SMS or voice calls directly. You cannot use numbers that are behind an IVR. (If you have a phone number already registered using a manual code before, then it continues to work normally.)

{% hint style="info" %}
**Note**: See [Connect your phone number to your WhatsApp Business API account](https://www.facebook.com/business/help/456220311516626?helpref=faq_content), for detailed information on adding a phone number to the WhatsApp account.
{% endhint %}

#### **Add Verified Name**

The WhatsApp account must have a verified name added to it. The verified name can be a maximum of 256 characters and must not contain an emoticon or any variation of the word "WhatsApp".

{% hint style="info" %}
**Note**: See [Verified Name Guide](https://developers.facebook.com/docs/whatsapp/guides/vname#set-up), for detailed information on adding a verified name to the WhatsApp account,&#x20;
{% endhint %}

### **WhatsApp Technical Setup**

The successful integration of WhatsApp as a channel with the bot developed on the Avaamo platform is the deployment of the **WhatsApp Business API Client** software. This software can be deployed on the customer premise, within a docker container or in an instance within AWS (Amazon Web Services). This is evaluated based on the restrictions imposed by your network security requirements.

{% hint style="info" %}
**Note**: See [network requirements](https://developers.facebook.com/docs/whatsapp/guides/network-requirements) to consider your deployment option.
{% endhint %}

#### **Environment Setup**

The WhatsApp Client Software needs to run on a **Container** platform that helps create a channel connected to the **Avaamo** platform. For example:

* Docker EE or Docker CE, or
* Containers-as-a-Service (CaaS) such as Amazon Elastic Container Service (ECS) and the WhatsApp Client Docker image, or
* Deploy WhatsApp Client on an AWS instance.

**Docker**

The WhatsApp Client Image requires a [Docker,](https://www.docker.com/) a container platform that lets you run the WhatsApp Business API Client. A [Docker Compose](https://docs.docker.com/compose/) is also required. Docker Compose is bundled with Docker for macOS and Windows but it requires a separate installation on Linux.

{% hint style="info" %}
**Note**: See [Installation and Upgrading](https://developers.facebook.com/docs/whatsapp/guides/installation), for detailed information on installing the WhatsApp Business API Client using Docker Compose,
{% endhint %}

**AWS**

For the customers who wish to deploy the WhatsApp Business API Client using Amazon Web Services(AWS) must set up a valid AWS account and be familiar with working on AWS.

{% hint style="info" %}
**Note**: See [Deploying the WhatsApp Business API with Amazon Web Services](https://developers.facebook.com/docs/whatsapp/aws), for detailed information on deploying the WhatsApp Business API Client using AWS
{% endhint %}

## WhatsApp Registration

The WhatsApp Registration requires a Phone Number and Verified Name Certificate. Details on creating the Verified Name Certificate is found in the section [Phone Number and Name Certificate](https://developers.facebook.com/docs/whatsapp/api/account). The phone number and verified name certificate are then used to complete the registration with the WhatsApp Business API Client.

WhatsApp Business API Client provides a REST interface to perform the registration. The end-point is where you either have the Docker image running or AWS Instance IP address.

Follow the steps below to register WhatsApp for the Avaamo platform:

1. Initial login to change the admin password
2. Login using new admin password
3. Create a non-admin user for use by the Avaamo platform
4. Request registration code
5. Register account with registration code

For the example (using cURL) that follow assume the following credentials:\
Admin User => admin\
Admin Password => conversation123\
User => channel\
User Password => channel123\
End-Point => myhost.com:9090

#### **Initial Login and Setting Password**

The initial login and password setup requires the admin password to be changed, prior to performing any of the registration steps. This is performed by:

```bash
curl -k -X POST https://myhost.com:9090/v1/users/login \
  -H 'Authorization: Basic Y2hhbm5lbDpjaGFubmVsMTIz' \
  -H 'Content-Type: application/json' \
  -d '{ "new_password": "conversation123"}'
```

Here, the Basic Authentication is used as given by the header:

```bash
Authorization: Basic Y2hhbm5lbDpjaGFubmVsMTIz
```

Where the authentication string is formed by base64 encoding of “admin:secret” that are the credentials by default. Base64 encoding is easily performed by [base64encode](https://www.base64encode.org/).

#### **Login Using New Password**

Login to your account with the new password to access the bearer token:

```bash
curl -k -X POST https://myhost.com:9090/v1/users/login \
  -H 'Authorization: Basic Y2hhbm5lbDpjaGFubmVsMTIz' \
  -H 'Content-Type: application/json' \
  -d ''
```

This returns the following output that contains the bearer token:

```
{"users":[{"token":"<bearer token>":"2018-10-10 21:08:57+00:00"}],"meta":{"version":"v2.19.7","api_status":"stable"}}
```

#### **Create User**

You can create a new user on WhatsApp by using the following code:

```bash
curl -k -X POST https://myhost.com:9090/v1/users \
  -H 'Authorization: Bearer <bearer token>' \
  -H 'Content-Type: application/json' \
  -d '{"username": "channel", "password": "channel123"}'
```

The bearer token value is from the previous call that logged in the admin user.

#### **Requesting a Registration Code**

The Registration code is returned by submitting the phone number and verified name on WhatsApp. The code is sent via voice or SMS (depending on your request). The example below is the call request of the registration code via voice:

```bash
curl -k -X POST https://myhost.com:9090/v1/account \
  -H 'Authorization: Bearer <bearer token>' \
  -H 'Content-Type: application/json' \
  -d '{ "cc": "US", "phone_number": "555555555", "method": "voice", "cert": "Zm9vOmJhcg==", "pin": ""}'
```

#### Account Registration

The final step is to perform the actual account registration:

```bash
curl -k -X POST https://myhost.com:9090/v1/account/verify \
  -H 'Authorization: Bearer <bearer token' \
  -H 'Content-Type: application/json' \
  -d '{ "code": "<code from sms/voice>"}'
```

## Deploy your agent to WhatsApp channel

The WhatsApp account is set up and registered. Now, let us integrate the WhatsApp channel with the Avaamo platform.

{% hint style="info" %}

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can deploy the agent to a channel after creating and building an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](applewebdata://9AE47367-043D-436A-BAB1-053A8B89E2A1/@avaamo/s/avaamo/~/edit/drafts/-Lsoojy2kKRX1KXPWAZ2/how-to/build-agents/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the **Agent** page, navigate to the **Configure -> Channels** option in the left navigation menu.

* On the Channels page, click **Connect** in the WhatsApp channel.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M-Q91f93zoxIBR-6DFO%2F-M-QAEpPirRqcIGm_bso%2Fagent-deploy-whatsapp-1.png?alt=media\&token=fff1afd0-38a8-459d-b2ba-331c746f9c28)

* Specify the following details:
  * The **Channel Name** is the phone number registered with the WhatsApp account.
  * The **Webhook URL** is the end-point of the WhatsApp Business API client.
  * The **Connection Credentials** are the base64 encoding of the user-created within the WhatsApp Business API client.
  * Click **Save**.

Now, click view under WhatsApp to open the Configuration window to get the WhatsApp Webhook URL. Make a note of the URL. This is the URL you must specify in the WhatsApp Business API Configuration:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M2WmQgHaymBUeYP7wLL%2F-M2WqffZBRpfFV1Fgtw1%2Fagent-deploy-whatsapp-3.png?alt=media\&token=0542bb47-d625-4f0b-81f6-6e1ce295c093)

## WhatsApp Business API Configuration

Login into the WhatsApp Business API Client account using the admin credentials to add the WhatsApp Webhook URL.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LxzGoX982gnpgqw1LSl%2F-LxzIi-UZVlETffwLjPI%2Fagent-deploy-whatsapp-4.png?alt=media\&token=12cedb38-e21a-45d6-a4c7-d13fbd04dc16)

## Manage channel settings

After you configure the channel settings, you can view, edit, disconnect and delete the channel settings as per your requirements. See [Manage channel settings](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/manage-channel-settings), for more information.
