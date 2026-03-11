# Source: https://docs.xano.com/xano-features/instance-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Instance Settings

## Custom Domain

Xano has support for users on any of our paid plans to set up a custom domain for their Xano backend.

#### How to set up your custom domain in Xano:

1. Navigate to your Instances page.

2. Open the menu on your instance and select Custom Domain, a panel on the right will open like below.

3. Carefully read and follow the instructions to update your DNS records: Create a CNAME record to the address provided, set the TTL to 5 minutes, and depending on your provider allow time for your DNS to propagate properly.

4. Enter your custom domain name at the bottom and click submit.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/22762cd4-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=bc58bceabc7f1fed289da85f6c844760" width="960" height="540" data-path="images/22762cd4-image.jpeg" />
</Frame>

To use your custom domain, navigate to your Instances page and follow the given instructions.

Once completed, you can use your custom domain on your API endpoints.

### Connect via Xano Domain

In some cases, you may still want to connect to your Xano instance via the original Xano domain. To connect through your Xano domain, head to your instance selection screen. Click the three dots when hovering over your instance, and choose "Connect Via Xano Domain".

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f4daac94-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=9cce0c0968fece15b10439a6182dd1b6" width="1093" height="533" data-path="images/f4daac94-image.jpeg" />
</Frame>

## Database Connector

<Info>
  Database Connector is included in our Essential and Pro plans. If you're on a grandfathered plan, please visit your [Billing page](https://app.xano.com/billing?mode=master) for more information.
</Info>

You have the option to connect your Xano instance's PostgreSQL database directly with an external application or service. This can be useful if there is a platform for manipulating your database that you prefer to use over the Xano interface, creating custom backup and restore solutions, or even performing data analytics.

<Warning>
  Use care when accessing your database directly. This type of connection removes a significant portion of normal checks and balances for data validity that using Xano directly provides.

  **Proceed with caution.**
</Warning>

#### How to Access the Database Connector

On your instance selection screen, click the⚙️ icon, and in the panel that opens, choose Database Connector.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/64629eeb-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=2a96eda17e833a3bf199e3267bb21370" width="1257" height="328" data-path="images/64629eeb-image.jpeg" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/713e2585-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=7c9f94307027c89ad7f8da0dc551817c" width="439" height="996" data-path="images/713e2585-image.jpeg" />
</Frame>

The panel that opens is split into two sections, Details and Settings.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/abcda124-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=8a9e48ce8f356d045638f3fba369a36d" width="881" height="553" data-path="images/abcda124-image.jpeg" />
</Frame>

Details allows you to retrieve the access information for a direct database connection.

Settings allows you to enable and use an allow list, to limit direct database connections to specific IP addresses.

1. Get your database's public IP

2. Get your database credentials

3. Settings Panel

4. Add an IP address to your allow list

Clicking both of the "Get" buttons will provide us with the database IP and two sets of credentials, full-access and read-only.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/bdc55291-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=1f739c1eaa589eb8bf37ecc978da0dd0" width="427" height="812" data-path="images/bdc55291-image.jpeg" />
</Frame>

From this panel, you can also **revoke and re-generate** your database credentials, should the need arise.

####

You can use any application you'd like that is capable of connecting to a PostgreSQL database. In this example, we'll be using Navicat.

Select 'Connection' in the top-left, and fill in your credentials and the IP recieved from Xano.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5a4c1f19-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=d9876d44d76ffcf74a008513c0bf03c5" width="1236" height="878" data-path="images/5a4c1f19-image.jpeg" />
</Frame>

Click 'Save' to save the connection. We can now navigate the PostgreSQL database from Xano using Navicat. We can even add / update data, run queries, etc...

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/39940ccf-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=70e1970724a10f3f9b87c157016d831e" width="800" height="564" data-path="images/39940ccf-image.jpeg" />
</Frame>

## Upgrading an Instance

**Why should you upgrade?** Free accounts come with **one workspace that shares resources with other Xano customers**. It also is limited on capabilities such as storage, database records, and processing power. You'll easily be able to prototype most of your application in this type of account, but upgrading to a paid plan will give you a more powerful instance that can scale with your needs. [View plan pricing and details](http://www.xano.com/pricing).

**What can I upgrade to?** If you are on our Essential plan, your next step would be Pro. Upgrades from Essential to Pro are able to make use of a 48 hour no questions asked refund policy -- if you find that Pro is not solving the requirement that prompted the upgrade, reach out to support within 48 hours and we'll roll you back and refund the difference.

**What does upgrading your instance actually do?** Upgrading your instance migrates your data and business logic to a brand new, faster instance. If you upgrade to the Essential or Pro plan, you'll be put on your own dedicated instance for maximum performance and scalability.

**How long does upgrading take?** Upgrading an instance takes seconds to complete.

### **Does upgrading happen automatically once I pay?**

**You will need to update your API URL ORIGIN if:**

* You are adding certain features to your plan, such as Static IP

* You are upgrading from **free** to **paid**

* You are changing your server region

**You do not need to update your API URL ORIGIN if:** - You are upgrading from a PAID to PAID instance and not changing your server location.

## **How to upgrade an instance**

### **Step 1 - Go to the Billing page**

Go to the Billing section within Xano. You can get there by clicking "Billing" in the side menu on the instances page. You can also click your initials when you're in your workspace and clicking the "Billing" link.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d53aa135-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=2fc34240edd471c122266cd808a0df77" width="943" height="589" data-path="images/d53aa135-image.jpeg" />
</Frame>

### **Step 2 - Select a plan**

Click the **Change Plan** button on the instance you want to upgrade.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3da6024d-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=5fc924d06daa33187c842d36ebd52d10" width="2256" height="972" data-path="images/3da6024d-image.jpeg" />
</Frame>

On the next screen, you'll be able to change your current plan, modify your billing schedule, add additional upgrades, or change your region.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b5f7fbed-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=fd0bd5c6a5d7ca75b70640e33a320dd1" width="2257" height="3176" data-path="images/b5f7fbed-image.jpeg" />
</Frame>

Once you've made your selections, click the green button at the bottom to proceed to checkout.

### **If your base API URL is changing...**

### **THIS IS THE MOST IMPORTANT STEP**

**To ensure a seamless transition for your users, please read this section carefully.**

#### **Click the "Start Upgrade" button...**

Don't worry, this doesn't start the upgrade right away. This will bring up a dialog telling you what you need to be aware of before continuing.

#### Write down your new API URL Origin

<Info>
  **What is an API URL ORIGIN anyway?** It's the first part of any API endpoint you have hooked up to the front-end. See below for an example

  ```
  YOUR API URL ORIGIN (example)
  https://xd6b-cfde-62f6.dev.xano.io/

  YOUR FULL API ENDPOINT URL FOR 'GET USERS' (example)
  https://xd6b-cfde-62f6.dev.xano.io/api:4qSkfrOl/user
  ```
</Info>

### Step 4 - Update your Front-end with the new API URL ORIGIN if you are upgrading from the FREE plan or changing your server region.

### Step 5 - Complete your upgrade

Once you follow the steps above, type **I UNDERSTAND** into the box and click the button "Start upgrade now".


Built with [Mintlify](https://mintlify.com).