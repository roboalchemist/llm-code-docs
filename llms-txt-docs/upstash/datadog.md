# Source: https://upstash.com/docs/workflow/integrations/datadog.md

# Source: https://upstash.com/docs/redis/howto/datadog.md

# Source: https://upstash.com/docs/qstash/integrations/datadog.md

# Source: https://upstash.com/docs/workflow/integrations/datadog.md

# Datadog - Upstash QStash Integration

This guide walks you through connecting your Datadog account with Upstash QStash for monitoring and analytics of your message delivery, retries, DLQ, and schedules.

<Check>
  **Integration Scope**

  Upstash Datadog Integration covers Prod Pack.
</Check>

## **Step 1: Log in to Your Datadog Account**

1. Go to [Datadog](https://www.datadoghq.com/) and sign in.

## **Step 2: Install Upstash Application**

1. In Datadog, open the Integrations page.
2. Search for "Upstash" and open the integration.

<img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=1d4018e79c0fedb23a2c8d21bc3b6a43" alt="integration-tab.png" data-og-width="2880" width="2880" data-og-height="1028" height="1028" data-path="img/datadog/integration-tab.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=e20319650673fc0c2ddb267c8c521d59 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=5eceb4e5af82406788781e8098229cf3 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=1e0ba16abd0046c3e8a65815eaa3fc19 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=5ade8ad371aaf59d811824c6310887a2 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=80c8644a9d8d417d9138d13143afaba0 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/integration-tab.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=eda063436df126a626dd96a87f22a050 2500w" />

Click "Install" to add Upstash to your Datadog account.

<img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=add4288783757921f62353223fbf39b5" alt="installation.png" data-og-width="2802" width="2802" data-og-height="1384" height="1384" data-path="img/datadog/installation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=142c3fcc921b90a0abc94bbeb8a7bae3 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=b7a6aae307da8f8b9757e84cff0db8d3 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=413d45cfe27a64e38c4e422c97984c8e 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=ba35ec57c2be78e999358a701e533812 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=52b29977b08a6500f380adea36c6881c 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/installation.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=811d297b670fc274b74322f932c80475 2500w" />

## **Step 3: Connect Accounts**

After installing Upstash, click "Connect Accounts". Datadog will redirect you to Upstash to complete account linking.

<img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=64d0abd76d3037f01a3811cd531c46d4" alt="connect-acc.png" data-og-width="1756" width="1756" data-og-height="936" height="936" data-path="img/datadog/connect-acc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=085212af402a08e0f7e89ba644529d48 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=f379315b18a9f213fa92aa119ca32f81 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=3a7dadd01cdd15abded31929223a534e 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=6b2fa6785253ca09d38a1c24cc081e4e 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=f6630bbfe1b49efa9f4b6fc4f4cc3a22 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/connect-acc.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=80054d3b9fa019a5bf1c1ee60334b116 2500w" />

## **Step 4: Select Account to Integrate**

1. On Upstash, select the Datadog account to integrate.
2. Personal and team accounts are supported.

**Caveats**

* The integration can be established once at a time. To change the account scope (e.g., add/remove teams), re-establish the integration from scratch.

<img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=7d332ed4228eaba275329f458d1dbd2f" alt="personal.png" data-og-width="886" width="886" data-og-height="1026" height="1026" data-path="img/datadog/personal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=f665cc6a4bbcf6d9d639c0b2b953fa0d 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=a1f4954abf4877df690e05633d0e0142 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=be4a2b8f7e038b224d48dada4132866c 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=4b18d7807fa6df65216f98ed0d3526f5 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=4791a82eeec9a917746a8684751e99f0 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/personal.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=d5cc8d1e39f3ab8058127a7bfc5a4f84 2500w" />

<img src="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=91af03309be7ba54f5c1e605052fe3cd" alt="team.png" data-og-width="950" width="950" data-og-height="1104" height="1104" data-path="img/datadog/team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=280&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=e0bcf3f87626d2f35dad5e349d8d530a 280w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=560&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=e5a7d1921331a83c3b2b6d0485b418df 560w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=840&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=575a5ad465eaa4e5ff17a202f0dce775 840w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=1100&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=67232bca77ab58e0be7a9ea6788caab9 1100w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=1650&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=71654ac0f72319d20778dacd0c9c2c3d 1650w, https://mintcdn.com/upstash/eu0laKPu7u_-Kw04/img/datadog/team.png?w=2500&fit=max&auto=format&n=eu0laKPu7u_-Kw04&q=85&s=6326dfc48f62069c3cb19a0f6b96a7ed 2500w" />

## **Step 5: Wait for Metrics Availability**

Once the integration is completed, metrics from QStash (publish counts, success/error rates, retries, DLQ, schedule executions) will start appearing in Datadog dashboards shortly.

<img src="https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=e4dbab20b620a015f5978e1ebce6ef18" alt="upstash-dashboard.png" data-og-width="2728" width="2728" data-og-height="1508" height="1508" data-path="img/datadog/upstash-qstash-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=280&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=2d5604424145437d8c65bf1f29961276 280w, https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=560&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=50b7cabece58a0ca711f1109a9ebee7a 560w, https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=840&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=60f1c33f2de64434705dc452a0f43c1e 840w, https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=1100&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=a69c642498a7621fcad8a236bd925534 1100w, https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=1650&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=a6e1d7ebfa95dc9f58e05c49eadb3868 1650w, https://mintcdn.com/upstash/dlfw7EZCyeFSjFPX/img/datadog/upstash-qstash-dashboard.png?w=2500&fit=max&auto=format&n=dlfw7EZCyeFSjFPX&q=85&s=d910a6cc1be7ac4d7a3f813694484808 2500w" />

## **Step 6: Datadog Integration Removal Process**

From Datadog → Integrations → Upstash, press "Remove" to break the connection.

### Confirm Removal

Upstash will stop publishing metrics after removal. Ensure any Datadog API keys/configurations for this integration are also removed on the Datadog side.

## **Conclusion**

You’ve connected Datadog with Upstash QStash. Explore Datadog dashboards to monitor message delivery performance and reliability.

If you need help, contact support.
