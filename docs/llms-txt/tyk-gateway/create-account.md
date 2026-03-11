# Source: https://tyk.io/docs/getting-started/create-account.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Tyk Account

> Create your account on Tyk Cloud

Welcome to Tyk! This guide will walk you through the process of creating your account and getting started with our powerful API management platform.

## Choosing Your Tyk Solution

Tyk offers multiple deployment options to suit your needs:

* **Tyk Cloud**: A fully managed service for easy API management at any scale.

* **Tyk Self-Managed**: Install the full lifecycle API management solution in your own infrastructure.

  > This page focuses on getting started with Tyk Cloud, If you are looking for information on Tyk Self-Managed, please refer to the [Getting Started with Tyk Self-Managed Guide](/getting-started/quick-start).

* **Tyk Open Source**: The core API Gateway, freely available and open source.

For this guide, we'll focus on creating an account for Tyk Cloud, which offers a free 48 hour trial.

## Creating Your Tyk Cloud Account

### Step 1: Visit the Sign-Up Page

Navigate to the Tyk sign-up page at [https://tyk.io/sign-up/](https://tyk.io/sign-up/).

### Step 2: Choose "Start Your 48-hour Free Trial"

On the sign-up page, select the "Start your 48-hour free trial" option to begin your Tyk Cloud experience.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-start-trial.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=231bec85c63802cb5c18912659e93a37" alt="Start Trial" width="2624" height="1318" data-path="img/getting-started/create-account-start-trial.png" />

### Step 3: Complete the Account Creation Form

Fill out the account creation form with your details:

* First Name
* Last Name
* Email Address
* Password
* Company Name (if applicable)
* Work Role and How We Can Help

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-free-trial-info.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=3cadb429a53e75e89bc419f6088ecd4b" alt="Create Account Free Trial" width="2550" height="1636" data-path="img/getting-started/create-account-free-trial-info.png" />

### Step 4: Check Your Email

Check your email inbox for a verification message from Tyk. Click the verification link to confirm your email address.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-resend-email.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=de08b4626691884ec025088178e0f0d8" alt="Create Account Resend Email" width="2678" height="1088" data-path="img/getting-started/create-account-resend-email.png" />

In your inbox, you should find this email (press "Log in"):

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-view-email.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=cbb6d0344e340d8356ce8433d06c9086" alt="Create Account View Email" width="2096" height="1360" data-path="img/getting-started/create-account-view-email.png" />

### Step 5: Create Password

After finding the email and logging in, set your password, organization name (any name which you want to represent your environment), and control plane region (select the control plane which is closest to your location).

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-set-password.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=8ba4df40c6d969257e5f816669887c23" alt="Create Account Set Password" width="2620" height="1498" data-path="img/getting-started/create-account-set-password.png" />

### Step 6: Deploy and Take Tutorial

Once your password, organization, and control plane are setup, continue to the next page where your environment will be deployed. This may take 2-5 minutes, you can peruse the tutorial to learn how to use the dashboard while you wait.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-deploy-tutorial.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=a9d80f7247b11b1c2d19481ea96ec236" alt="Create Account Deploy Tutorial" width="2378" height="1380" data-path="img/getting-started/create-account-deploy-tutorial.png" />

After a few minutes, the "Add API" button should appear. Select it and you will be taken to the dashboard.

<img src="https://mintcdn.com/tyk/zB4143fn76CY8N8G/img/getting-started/create-account-add-api.png?fit=max&auto=format&n=zB4143fn76CY8N8G&q=85&s=fa0b2a1f98dcd4dff08ec79de67c4439" alt="Create Account Add API" width="2646" height="588" data-path="img/getting-started/create-account-add-api.png" />

### Step 7: Start Creating APIs

Finally, you will be taken to the Tyk Dashboard. Select "Design From Scratch" and continue on to [our tutorial](/getting-started/configure-first-api) to learn how to setup and secure your APIs.

<img src="https://mintcdn.com/tyk/GWakR0LnkXjsKcah/img/getting-started/create-account-design-from-scratch.png?fit=max&auto=format&n=GWakR0LnkXjsKcah&q=85&s=59e30dfd6088c21e2fbbf6a6c66488e0" alt="Create Account Design From Scratch" width="2940" height="1652" data-path="img/getting-started/create-account-design-from-scratch.png" />

## What Happens Next?

Once you've created your account, Tyk will automatically:

* **Assigns Billing Admin Role**: You are designated as the Billing Admin for your organization, granting you full access to manage billing details and subscription plans.

* **Activates 48-Hour Free Trial**: Your account is enrolled in a 48-hour free trial of Tyk Cloud, allowing you to explore its features and capabilities without immediate commitment.

* **Creates Initial Organization**: An organization is automatically established, serving as the primary entity for managing your environments, APIs, and users.

* **Establishes Default Team**: A default team is set up within your organization, providing a collaborative space for managing APIs and related resources.

* **Deploys Control Plane**: A control plane is deployed in your selected home region, centralizing the management of your APIs, policies, and configurations.

* **Deploys Gateway**: A Tyk Gateway is deployed to manage and route incoming API traffic, handling authentication, rate limiting, and analytics to ensure secure, reliable access.

For certain Tyk Cloud configurations, you may also get an Edge Gateway deployment option, allowing gateways to be positioned closer to users for lower latency and optimized routing. This is ideal for multi-region or global API setups but may require additional configuration or regional deployment options through Tyk’s Multi Data Centre Bridge (MDCB) if set up manually.

<Note>
  After the 48-hour free trial of Tyk Cloud ends, your infrastructure (control plane, gateway, and organization settings) will be deactivated unless you upgrade to a paid plan. Here’s what happens:

* Limited Access: Control plane access and API traffic routing through the gateway will be suspended.
* Data Retention: Your configurations (APIs, policies, user settings) are temporarily retained, allowing you to pick up where you left off if you upgrade within a grace period.
* Billing Admin Role: You’ll still be able to manage billing and subscription options.

  Upgrading restores full functionality, letting you continue from where you paused. To avoid disruption, consider exploring paid plans before your trial ends.
</Note>

## Next Steps

Now that you have your Tyk account set up, here are some recommended next steps:

* **Create Your First API**: Follow our guide on [setting up and securing your first API](/getting-started/configure-first-api).
* **Explore the Dashboard**: Familiarize yourself with the [Tyk Cloud interface](/api-management/dashboard-configuration).

## Need Help?

If you encounter any issues or have questions during the setup process, don't hesitate to reach out to our support team at [support@tyk.io](mailto:support@tyk.io).

Remember, Tyk offers powerful features for API management, security, and performance. Take advantage of your trial period to explore all that Tyk has to offer!

Built with [Mintlify](https://mintlify.com).
