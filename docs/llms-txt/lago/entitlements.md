# Source: https://getlago.com/docs/guide/entitlements.md

# Entitlements

> Unify entitlements and billing in one streamlined platform with Lago.

In a billing system, entitlements define what a customer can access and how much they can use, based on their subscription or contract.
This includes feature gates, which control whether a feature is enabled or disabled for a given customer; feature privileges, which determine the level of access within a feature, such as basic or advanced functionality; allowances, which represent the included usage in a plan, like 100 API calls per month; and quotas, which are the maximum usage limits that may trigger overage charges or access restrictions. Together, these components help enforce product limits, manage access, and support accurate usage-based billing.

In addition to the usage-based engine for allowances and quotas, Lago lets you define Features and Entitlements.

## Set up your features

<Tabs>
  <Tab title="Dashboard">
    Lago supports the creation of any type of feature to tailor your billing logic. To create a new feature:

    1. Navigate to the **Features** section in the sidebar;
    2. Click on **Add a Feature** to start a new entry;
    3. Give it a unique `code` (used for programmatic actions) and a `name`;
    4. Assign one or more **privileges** to the feature (optional); and
    5. Click **Create feature** to finalize and save the feature to your instance.

    A feature in Lago represents a capability that can be gated behind a plan. It's not necessarily something you bill for directly, but rather something a customer gains access to based on their subscription.

    <Frame caption="Features section with the list of features">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=5bb1b1fe6a101386fd890bddbdb03558" data-og-width="2880" width="2880" data-og-height="1600" height="1600" data-path="guide/images/features-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=46bb49f400207daa4207423fd676de6f 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7f4ef0875b9da6dfeca1395d65280660 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=7d9d03621d54d8b5317609282b5b4940 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=ce23934d18e7d8cae0550f0308365df0 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=bae7f349959f86a671bf84aa2b367f66 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/features-list.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3d71903d76f1125ead796a0a0d2a0498 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Create a feature theme={"dark"}
      curl --request POST \
      --url https://api.getlago.com/api/v1/features \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "code": "seats",
      "name": "Number of seats",
      "description": "Number of users that can be added to the account"
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Define feature privileges

<Tabs>
  <Tab title="Dashboard">
    Additionally, you can define privileges for a specific feature. Privileges allow you to configure more granular access controls across different plans. For example, the invite\_member feature might allow inviting 1 member on the *Free plan*, while offering unlimited invites on the *Pro plan*.

    Feature privileges can be associated with the following types:

    * **`boolean`** – The privilege value is either `true` or `false`.
    * **`integer`** – The privilege value is a numeric limit (e.g., `10 GPUs`).
    * **`string`** – The privilege value is freeform text.
    * **`select`** – The privilege value is chosen from a predefined list of options.

    At this stage, you're only defining the **type** of each privilege. The actual values will be set later, when the feature is entitled to a specific plan or subscription.

    <Info>
      You can add an unlimited number of privileges to a feature.
    </Info>

    <Frame caption="Add feature privileges">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=90917e748e97a8d349bca79f17c68406" data-og-width="2880" width="2880" data-og-height="2360" height="2360" data-path="guide/images/add-feature-privileges.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=e58360b2ad7d68aeab4d44c863c771ba 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=df98fc4d50205b8bf3062279f715b733 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=f3883a05fa2eaa080d2775f0722c0e34 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9a2e5471d40ea60bef1caef5de75bc0e 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b6dc9298246d5f3070b53fa432cd952e 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/add-feature-privileges.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=456930046eac925e0292325c30ccafee 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Create feature with privileges theme={"dark"}
      curl --request POST \
      --url https://api.getlago.com/api/v1/features \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "code": "seats",
      "name": "Number of seats",
      "description": "Number of users that can be added to the account",
      "privileges": [
        {
          "code": "max_",
          "name": "Maximum seats",
          "value_type": "integer"
        },
        {
          "code": "min",
          "name": "Minimum seats",
          "value_type": "integer"
        },
        {
          "code": "allow_admin_user",
          "name": "Allow admin user",
          "value_type": "boolean"
        }
      ]
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Map entitled features to your plans

<Tabs>
  <Tab title="Dashboard">
    Once your features have been created, they can be added to your plans through a process called **Entitlements**.
    This is where you define features that are unlocked for a specific plan and the limits, values or privileges for each feature.

    Entitlements define which features a customer is allowed to use based on the plan they are subscribed to. By assigning features to specific plans, you control access to functionality across your pricing tiers.

    <Frame caption="Subscription and entitlement workflow">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b906f7138c976545d714910b360be93c" data-og-width="3728" width="3728" data-og-height="2340" height="2340" data-path="guide/images/entitlements-subscription-workflow.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=01fc08d60ec7d805d755d735edc88a82 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=9d17b6183a15c0825f1cfe8ee20be0e3 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=c619803431146925c7e27d4bdccc3821 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b2ec86f36a74b668ed7ad33ad535ad9b 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=1f1e743b0ec308b8392722eb33ccaf68 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/entitlements-subscription-workflow.jpg?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=8821cdfc63433811dc10dcf080cbe456 2500w" />
    </Frame>

    To assign features to a plan:

    1. Create a new plan or edit an existing one;
    2. Navigate to the **Advanced Settings** section;
    3. Select the features you want to entitle for that plan; and
    4. Configure the values for each feature's privileges according to the plan's rules.

    <Frame caption="Entitle features to a plan">
      <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=5115a301b7794f3d96fd2526f57921e7" data-og-width="2720" width="2720" data-og-height="3058" height="3058" data-path="guide/images/plans-entitlements.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=16387592ca1060920352d8c4a252108c 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=172c661d5bcff41f36606856206ccbc6 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=b2ee1b604b285a8f36829665b962d844 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=4de192ad166fbd3887461b4ce107c321 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=2ed5d58b97a67f7fa26387be437bbc33 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/images/plans-entitlements.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c52fa10de5fd5bcc9cada50071a38665 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Create plan entitlements theme={"dark"}
      curl --request POST \
      --url https://api.getlago.com/api/v1/plans/{code}/entitlements \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "seats": {
        "max": 20,
        "min": 10,
        "allow_admin_user": false
      },
      "sso": {
        "provider": "okta"
      }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Override entitlements for a subscription

<Tabs>
  <Tab title="Dashboard">
    Some customers may subscribe to a standard plan but negotiate custom entitlements as part of their contract.

    Just like charges, **you can override any entitlement value** for a specific subscription.
    This creates an **overridden subscription**, where the custom entitlements apply **only** to that particular customer, without affecting the base plan or other subscribers.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Create subscription entitlements theme={"dark"}
      curl --request PATCH \
      --url https://api.getlago.com/api/v1/subscriptions/{external_id}/entitlements \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: application/json' \
      --data '{
      "seats": {
        "max": 30,
        "min": 20,
        "allow_admin_user": true
      },
      "sso": {
        "provider": "okta"
      }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Get entitlements for a subscription

You can retrieve the current list of entitled features for a subscription by calling the following endpoint:

```bash  theme={"dark"}
curl --request GET \
  --url https://api.getlago.com/api/v1/subscriptions/{external_id}/entitlements \
  --header 'Authorization: Bearer <token>'
```

You can also track entitlement changes through the `subscription.updated` webhook.
