# Source: https://docs.hypermode.com/agents/connections/stripe.md

# Using Stripe with Hypermode

> Connect your Hypermode agent to Stripe for automated payment processing and financial operations

<div className="flex items-center gap-3 mb-6">
  <img src="https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=e5e6ec503157ec14d5ef36949be1898b" alt="Stripe" width={48} height={48} width="512" height="512" data-path="images/agents/connections/icons/stripe.png" srcset="https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=280&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=6f57b22a9b8be5d29c1a81bd5357ad36 280w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=560&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=14c7ad70b866b9bb2e0c7b2532362e1d 560w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=840&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=d3ab23a582a21eda8c7b7f125b49d506 840w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=1100&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=d2551d88535468553105396ec71f41ff 1100w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=1650&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=793c1ecd2851c79b60368bd27107343b 1650w, https://mintcdn.com/hypermode/168JkHD55lMGo3-U/images/agents/connections/icons/stripe.png?w=2500&fit=max&auto=format&n=168JkHD55lMGo3-U&q=85&s=3b557f9e0df6b65021765760dd391651 2500w" data-optimize="true" data-opv="2" />

  <div>
    <h2 className="text-2xl font-bold m-0">Stripe</h2>

    <p className="text-gray-600 m-0">
      Stripe powers online and in-person payment processing and financial
      solutions for businesses of all sizes.
    </p>
  </div>
</div>

## Overview

Stripe is a comprehensive payments platform that handles everything from payment
processing to financial reporting. This guide will walk you through connecting
your Hypermode agent to Stripe, enabling automated payment operations, customer
management, and financial data analysis.

## Prerequisites

Before connecting Stripe to Hypermode, you'll need:

1. A [Stripe account](https://stripe.com/) (individual or business)
2. Stripe API credentials (publishable and secret keys)
3. A [Hypermode workspace](https://hypermode.com/)

## Setting up Stripe

### Create your Stripe account

If you haven't already, sign up for a Stripe account. You can start with a test
account to experiment safely.

### Access your API keys

Navigate to your Stripe dashboard to find your API credentials:

1. Go to **Developers** → **API keys** in your Stripe dashboard
2. You'll see both test and live API keys
3. Start with test keys for development

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8e779b9dbc58be3e8e04428888aea9b7" alt="Stripe API keys" width="2058" height="1390" data-path="images/connections/stripe/stripe-api-keys-dashboard.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=bde042ce9c305d94a5578509e8731778 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6755138a23f065fc2b96255f01fdc2d6 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e66dfee53d22bbd17894855335e6da5b 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=13f24202ad7d285a8590080bd1f319ee 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=7da50eb54e5fabdab41e76d330a998ff 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-api-keys-dashboard.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=47add9e50c9b53118b6cc23f6ba4e6e0 2500w" data-optimize="true" data-opv="2" />

<Note>
  Stripe provides separate test and live environments. Always start with test
  keys during development to avoid processing real payments accidentally.
</Note>

### Create a restricted API token (Recommended)

For enhanced security, create a restricted API token with only the permissions
your agent needs:

1. Go to **Developers** → **API keys**
2. Click **Create restricted key**
3. Select specific permissions based on your use case

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c47e3b0faaccedbf0eaf0f133ade8d38" alt="Create restricted key" width="2036" height="1640" data-path="images/connections/stripe/stripe-restricted-key.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=97a4ba59436d4e8c3dfc7977b0ce9a68 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=066a27555afedf7ca4303e4cd6ee7da5 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3c70c3f99d1ae06ea2a08080adbd4052 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=efd2daded5e9f8ceb543b4d4f29e78ac 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=b59a837a24a630e75b9b0c282bd95ea4 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-restricted-key.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d0571517ebdd670e70ed771d02be47a8 2500w" data-optimize="true" data-opv="2" />

**Recommended permissions for most agents:**

* **Customers**: Read and Write
* **Payment Intents**: Read and Write
* **Charges**: Read
* **Invoices**: Read and Write
* **Products**: Read and Write
* **Subscriptions**: Read and Write

<Warning>
  Only grant the minimum permissions your agent actually needs. This follows the
  principle of least privilege and enhances security.
</Warning>

## Creating your Stripe agent

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e0b26e31c95c2e089ebeb644601f5a82" alt="Create new agent" width="2190" height="638" data-path="images/connections/stripe/create-new-agent-button.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9b405a826d40adacad14d37fa6dff24e 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8b38eaf36e0ab5a03b4db03e1c0f3b22 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=7fe2b8e0d957eb088b9a51a7ac4dcac4 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=869930e27300c997065d5725793fa0dd 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=77fde702e48c9ec29bcca70d537b1b2b 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6d6c4aee6183791de8658a92175424ef 2500w" data-optimize="true" data-opv="2" />

### Create a new agent

From the Hypermode Agents console, create a new agent:

1. Click the **Create new Agent** button from the agents view or select *Create
   new >> Create new agent* from the threads view.
2. Enter a name for your agent.
3. Click the **Create Agent** button.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=28bb47bfddaba8942c7f9aa787c2eeb5" alt="Create new agent modal" width="1878" height="1154" data-path="images/connections/stripe/create-new-agent-description.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fdb5d00b6e7a0dffb84d9e575a1e4f21 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d5951a8b801b97a81c42bd0899ea0689 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c154545eff47ad99f3b9e8f68d684d35 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6c395ba70d08f0e71cee690e6992cb77 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=151c815859b946e47dd41cfeb2dc6bd4 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-description.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3e2d740c049f3cd5dc8f9f7217444fbd 2500w" data-optimize="true" data-opv="2" />

### Agent profile

You can view and edit agent details in the agent profile. The agent profile
includes the agent name, description, and instructions. You can also view your
threads with this agent as well as manage the agent's tasks and knowledge.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1c8ab3f58e5748b18c8d77d60098e578" alt="Agent profile" width="3378" height="2834" data-path="images/connections/stripe/agent-profile-view.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a05a5e3d4a95350841b9235b46c3d9a1 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=662d94edc2d72e64d7a3669a17172e55 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=57a720764fa60f5de0d0d6128aa89b84 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c3300be63ff960f95763cca46acba1ed 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3b5e96495535d78c05cf0e331660bd9d 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-profile-view.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fe9ad3e2038019c5072bc6eb7c1e719e 2500w" data-optimize="true" data-opv="2" />

### Agent instructions

You can edit the agent instructions in the agent profile. Editing the agent's
instructions is useful for personalizing your agent and customizing how your
agent will work with you and your team.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3891f7e69b470695fef1272d9bb53f72" alt="Create agent modal" width="1908" height="1084" data-path="images/connections/stripe/edit-agent-instructions.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=92205f90f4ce2f11847fae4dec1efedf 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1598fccd86e42ed704cf5a36ef2e09ca 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=af48be46643f7c305c309a7c1d817bd5 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=30d2ba47f50dd7d68a401885fe0d2c78 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=99ac0f48d294f5a8792cee4d1030a467 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/edit-agent-instructions.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=eacfa0788d25705ac334dae52b155c84 2500w" data-optimize="true" data-opv="2" />

## Connecting to Stripe

### Add the Stripe connection

Select the Agents tab in the left navigation bar, then click your StripeSleuth
agent. Select the "Connections" tab.

1. Select the Connection tab
2. Select "Connect" next to Stripe in the list of available connections

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1f6f1389f153d6e965d535ef724dfd2d" alt="Add Stripe connection" width="3072" height="1626" data-path="images/connections/stripe/stripe-add-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=379e1c1625f213821d19131c18c6b330 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6902842943c238210eeec4db09403136 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=243dbc502b005e80af4fe22e3d3d2868 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=380f7e451d38d0e24b17582224319c96 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8ed1d7ca7c71ee5770a9e09992a1fecc 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6ce1655b88780e3c483565933752b735 2500w" data-optimize="true" data-opv="2" />

### Configure credentials

Enter your Stripe credentials:

* **API Key**: Your Stripe secret key (starts with `sk_test_` for test mode or
  `sk_live_` for live mode)

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=66a6149f19f1f5c87b38e2c49ad1f380" alt="Stripe connection modal" width="1586" height="788" data-path="images/connections/stripe/stripe-configure-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a70522b7df7ea0a0d9e4e22c7f8d872a 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3d7ad42bbb0340e41c2c240f59a3bb5a 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9e9505750c57e3a533c8a6367ea268e5 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=23f2c30183d0c0db5db0dbed8be5bd72 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=23d1dd7b0098d7e56b01e62d728faf09 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e58c695d26ffd0f78138ddcaf317fb5a 2500w" data-optimize="true" data-opv="2" />

<Warning>
  Keep your secret API key secure! This key provides full access to your Stripe
  account and should never be exposed in client-side code or shared publicly.

  We recommend using a Stripe Sandbox environment for development and testing.
</Warning>

## Create a new thread with your agent

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=903fb5b81e9c6fcf5da6097ae8376b46" alt="Create agent thread" width="1796" height="586" data-path="images/connections/stripe/agent-new-thread.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0dabce23a69a0624778b7bb5d72bf35c 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ef496a61e47e83f56fcd5f1ac4aca3a8 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1907b98d862e686b8cf3de479175cb29 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=cb17ee9cc151a0690dbea31deda31c1a 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=67b786ee47903419de483238bb11f45d 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/agent-new-thread.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e0355c26ba58b7488319e1a00bef7a4d 2500w" data-optimize="true" data-opv="2" />

From the threads view, select "Create new" then select your "Stripe Sleuth"
agent from the list of agents.

### Test basic connectivity

Start a new thread and test the connection with a simple query:

```text
Can you check my Stripe account balance?
```

You should see a Stripe tool call in the chat history, confirming the connection
works:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=254d60ea730808e0a91d9d04cee4f551" alt="Test connection" width="2308" height="938" data-path="images/connections/stripe/stripe-test-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=cd13c973d12b67d287cd64d46a524aee 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=13a3c2efe781a47b0951b56712552635 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c62d2ca3e0f1f54e44f12064bfcc4911 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=507078e8b5dcc8000efd701bfb3c8487 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a8c8bfc46d9ddb806c261a8324086090 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a3d35fe8d78dd06b972c2058d40c1257 2500w" data-optimize="true" data-opv="2" />

### Test permissions

Verify your API key has the necessary permissions:

```text
Can you list my recent customers and products?
```

If you see permission errors, you may need to update your API key permissions or
use a different key.

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=96473e9169e44bac36e0a074b63f8698" alt="Test permissions" width="1634" height="1656" data-path="images/connections/stripe/stripe-test-permissions.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=67f8eb36e5093a7c70c7b09e7f34eb5d 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a84134469c1e4dee38d5d966ca6a1cf0 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=40d857921fbc049fbb61639f7cba4457 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3cb32e476728b79e228871f5873f158c 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d68e8469170d2eafcda627110f267316 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-permissions.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=bd0854f9f00514645f0c8f63c645308c 2500w" data-optimize="true" data-opv="2" />

## Setting up your Stripe environment

<Note>
  Unlike databases, Stripe doesn't require schema setup. However, you'll want to
  configure products, pricing, and webhook endpoints for a complete integration.
</Note>

### Create test products

Set up some test products to work with:

```text
Can you create a test product called "Premium Subscription" with a monthly price of $29.99?
```

### Update agent instructions

Enhance your agent's understanding by updating its instructions with your
business context:

```text
You are connected to a Stripe account for [Your Business Name]. Our main products include:

1. **Premium Subscription** - $29.99/month recurring
2. **Basic Plan** - $9.99/month recurring
3. **One-time Setup** - $99 one-time payment

When processing payments, always:
- Verify customer information
- Use appropriate product IDs
- Handle errors gracefully
- Provide clear confirmation messages

For subscription management, monitor for failed payments and proactively communicate with customers about billing issues.
```

## Testing payment operations

### Test 1: Create a customer

Test customer creation capability:

```text
Can you create a new customer with email bob.loblaw@example.com and name "Bob Loblaw"?
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9863b5930c3349055c6f49b97248b6b6" alt="Create customer" width="1622" height="478" data-path="images/connections/stripe/stripe-create-customer.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d5e0a69304bf7fcbca2c1ee76a06e56b 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=fad34d1b3ce589f7d61146b32a760afa 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6e4a57d043be08a3d890b567326e15a1 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=67c0c8f96f1672675796d5ab668de1ae 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=2445c45dd89b466d82817c0ef5dfd47e 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-customer.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6c3aae7ad87ff8715865a67eae69d4aa 2500w" data-optimize="true" data-opv="2" />

### Test 2: Process a test payment

Try processing a payment using Stripe's test card numbers:

```text
Can you create a payment intent for $50 for customer bob.loblaw@example.com?
```

<Note>
  In test mode, use Stripe's test card numbers like `4242424242424242` for
  successful payments or `4000000000000002` for declined cards.
</Note>

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=08b2d4f6b77a640771a9c63af1b6586d" alt="Process payment" width="1634" height="616" data-path="images/connections/stripe/stripe-process-payment.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6125accd29c25e433a27c62254f7a278 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=dfeb02eadba19aad04edb75ea8e15dce 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3b12206d998b24c5db55de89eef08f6c 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=ecb806f32e53875275a2feac4b356f00 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=0d9f6a9146aecc2ac395692db156b752 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-process-payment.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9c8b370687928f3d00b17fce65bfe39f 2500w" data-optimize="true" data-opv="2" />

### Test 3: Handle subscriptions

Test subscription management:

```text
Can you create a monthly subscription for Bob Loblaw using the Premium Subscription product?
```

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3e6f0f6d2102cdb014351bccd98140e8" alt="Create subscription" width="1608" height="606" data-path="images/connections/stripe/stripe-create-subscription.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3cfdc3e229c73495b06b5bd19ecc6dde 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=4d95db181e23a2e8b3f3f06f4cffb593 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=cd4a042cb894612399bbb0d15260a122 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3d1194530f3edd14c3d7ddab71d38d39 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1ac0a1cd39e82c2f7f6326c4e0f41606 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-create-subscription.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=d7710d4d41d2899af71af72acd57c880 2500w" data-optimize="true" data-opv="2" />

## What you can do

With your Stripe connection established, your agent can:

* **Process payments** with various payment methods
* **Manage customers** and their payment information
* **Handle subscriptions** including creation, updates, and cancellations
* **Process refunds** and handle disputes
* **Generate invoices** and manage billing
* **Analyze financial data** and generate reports
* **Manage products and pricing** dynamically
* **Integrate with other tools** like CRM systems, email marketing, and
  accounting software

## Best practices

1. **Security first**: Always use restricted API keys with minimal required
   permissions
2. **Test thoroughly**: Use Stripe's test environment before going live
3. **Error handling**: Implement robust error handling for payment failures
4. **Compliance**: Ensure PCI compliance and follow data protection regulations
5. **Monitoring**: Set up alerts for failed payments and unusual activity

## Advanced operations

### Payment processing workflows

Your agent can handle complex payment scenarios:

```text
Process a payment for a customer, and if it fails, try their backup payment method, then send them an email notification
```

### Subscription management

Automate subscription lifecycle management:

```text
Check for subscriptions that failed payment in the last 24 hours and send dunning emails to those customers
```

### Financial reporting

Generate comprehensive financial reports:

```text
Create a monthly revenue report showing breakdown by product, including refunds and net revenue
```

### Dispute handling

Manage chargebacks and disputes:

```text
List all open disputes and provide evidence suggestions for each case
```

## Integration examples

### E-commerce automation

```text
When a customer places an order, create a payment intent, and if successful, fulfill the order and send a confirmation email
```

### SaaS billing management

```text
Monitor subscription statuses and automatically downgrade accounts when payments fail after the grace period
```

## Troubleshooting

### Common connection issues

1. **Invalid API key**: Verify your key is correct and has proper permissions
2. **Test vs Live mode**: Ensure your API key matches the intended environment
3. **Rate limiting**: Stripe has rate limits; your agent will handle these
   automatically
4. **Insufficient permissions**: Update your restricted key permissions as
   needed

### Payment failures

1. **Declined cards**: Use appropriate test card numbers in test mode
2. **Authentication required**: Handle 3D Secure authentication flows
3. **Insufficient funds**: Test with appropriate test card numbers
4. **Invalid parameters**: Verify all required fields are provided correctly

### Webhook issues

1. **Endpoint verification**: Ensure your webhook endpoint is accessible
2. **Event handling**: Verify you're listening for the correct event types
3. **Signature verification**: Implement proper webhook signature verification

## Security considerations

<Warning>
  Never expose your Stripe secret keys in client-side code, logs, or public
  repositories. Always use environment variables or secure key management
  systems.
</Warning>

1. **API key rotation**: Regularly rotate your API keys
2. **Webhook signatures**: Always verify webhook signatures to ensure
   authenticity
3. **PCI compliance**: Follow PCI requirements when handling card data
4. **Audit logs**: Monitor your Stripe dashboard for unusual activity
5. **Two-factor authentication**: Enable 2FA on your Stripe account

## Learn more

* [Stripe Documentation](https://stripe.com/docs)
* [Stripe API Reference](https://stripe.com/docs/api)
* [Payment Intents Guide](https://stripe.com/docs/payments/payment-intents)
* [Testing Guide](https://stripe.com/docs/testing)

<Tip>
  Combine Stripe with other Hypermode connections to create powerful business
  workflows. For example, use Slack to notify your team of large payments,
  GitHub to track payment-related code changes, or your CRM to update customer
  information after successful payments.
</Tip>

## Compliance and regulations

### PCI compliance

When handling payment card data:

* Use Stripe's secure payment forms
* Never store card details directly
* Implement proper access controls
* Regularly monitor for vulnerabilities

### Data protection

* Follow GDPR requirements for customer data
* Implement proper data retention policies
* Provide mechanisms for data deletion
* Ensure proper consent management

### Financial regulations

* Comply with local financial regulations
* Implement proper record keeping
* Ensure accurate tax reporting
* Handle dispute resolution appropriately
