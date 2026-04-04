# Source: https://docs.intelligems.io/developer-resources/external-api/automations-and-guides/automated-test-alerting-for-slack.md

# Automated Test Alerting for Slack

## Overview:

This guide walks you through creating a daily automation that checks running tests for traffic or data issues (low visitors, SRM failures, large conversion drops, minimum orders per variant) and posts a Slack alert when a test fails health thresholds.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fr0hbHUsEkCWdvUtEBIFP%2FScreenshot%202026-02-02%20at%201.37.48%E2%80%AFPM.png?alt=media&#x26;token=a1bbde81-69c1-404c-9e30-6042a76429aa" alt=""><figcaption></figcaption></figure>

### Softwares Used <a href="#softwares-used" id="softwares-used"></a>

To build this automated reporting pipeline, you will need the following tools:

* [n8n](https://n8n.io/): The primary workflow automation platform used to connect APIs and schedule tasks.
* [Slack](https://api.slack.com/apps): The final destination where the AI-generated health checks and reports will be posted.

## How to Create Your Automated Test Alerts <a href="#how-to-create-your-scheduled-test-analysis" id="how-to-create-your-scheduled-test-analysis"></a>

### Step 1: Get Your Intelligems API Keys <a href="#step-1-get-your-api-keys" id="step-1-get-your-api-keys"></a>

To request access and receive your API key, [contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

### Step 2: Create the Workflow in n8n <a href="#how-to-create-an-automated-test-monitoring-integration-for-slack" id="how-to-create-an-automated-test-monitoring-integration-for-slack"></a>

#### **Node 1: Schedule Trigger**

1. Click the **"+"** button to add a node
2. Search for **"Schedule Trigger"**
3. Configure it:
   * **Trigger Interval**: "Hours"
   * **Hours Between Triggers**: 8 (runs 3x daily: morning, afternoon, evening)
   * Or set to **12** for 2x daily

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FEKUTSgvHv5A8wqxSWhFV%2FScreenshot%202026-02-02%20at%2012.59.14%E2%80%AFPM.png?alt=media&#x26;token=c5105d5c-94d5-4bcf-bc8a-b9cc1f66818e" alt=""><figcaption></figcaption></figure>

#### **Node 2: Create Organization List**

* Add **"Code"** node
* Select **"Code in JavaScript"**
* Select **"Run Once for All Items"**
* Paste this code. Update it with a display name for your client & their API key:

```
// Define all your Intelligems organizations
const organizations = [
  {
    name: "Client 1",
    apiKey: "YOUR_API_KEY_1"
  },
  {
    name: "Client 2", 
    apiKey: "YOUR_API_KEY_2"
  },
  {
    name: "Client 3",
    apiKey: "YOUR_API_KEY_3"
  }
];

// Return each org as a separate item for n8n to process
return organizations.map(org => ({ json: org }));
```

<figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FDRBeDys0ClEIoItfUdsH%252FScreenshot%25202026-01-30%2520at%252010.58.08%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Dfdc79f48-af06-4251-809a-3fd2a5864bc9&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=b4f3eeab&#x26;sv=2" alt=""><figcaption></figcaption></figure>

#### **Node 3: Get All Running Tests**

1. Click **"+"** after the Schedule node
2. Search for **"HTTP Request"**
3. Configure:
   * **Method**: GET
   * **URL**: `https://api.intelligems.io/v25-10-beta/experiences-list`
   * **Authentication**: None
   * Enable **Send Headers**
     * **Name**: `intelligems-access-token`
     * **Value**: `{{ $json.apiKey }}`
4. Click "Execute step" to verify it works

<figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252F4VQawiu8Aj6jmzn9W7Tt%252FScreenshot%25202026-01-30%2520at%252010.59.12%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3Dc21a9cec-3937-429a-8eb7-ca459dedb53a&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=c1bd2f9&#x26;sv=2" alt=""><figcaption></figcaption></figure>

#### **Node 4: Filter Tests by Status = "started"**

* \
  Add **"Code"** node
* Select **"Code in JavaScript"**
* Select **"Run Once for All Items"**
* Update the below code so that `InsertOrgId` maps to match the Intelligems organization IDs of your clients (you can find these in Intelligems under Settings > General > Organization Settings), the `name` value is display name for your clients, and the `apiKey` value is the Intelligems API Key for those clients. Then paste this code into the Code section in n8n.

```
// Filter for running tests with status = started
const items = $input.all();
const today = new Date();
const filteredTests = [];

// Static mapping of organization IDs to client names AND API keys
const clientMapping = {
  "InsertOrgId": {
    name: "Client 1",
    apiKey: "ig_live_11111"
  },
  "InsertOrgId": {
    name: "Client 2",
    apiKey: "ig_live_22222"
  }
};

for (const item of items) {
  // Get organization ID from the API response
  const orgId = item.json.organizationId || item.json.organization?.id || (item.json.experiencesList && item.json.experiencesList[0]?.organizationId);
  const clientData = clientMapping[orgId] || { name: "Unknown Client", apiKey: "" };
  
  // Access the experiencesList array
  const experiencesList = item.json.experiencesList;
  
  // Iterate through each test in the experiencesList
  if (experiencesList) {
    for (const test of experiencesList) {
      // Only check if status is "started"
      if (test.status === "started") {
        // Calculate days running for reporting purposes
        const startDate = new Date(test.startedAtTs);
        const daysRunning = Math.floor((today - startDate) / (1000 * 60 * 60 * 24));
        
        filteredTests.push({
          json: {
            clientName: clientData.name,
            apiKey: clientData.apiKey,
            experienceId: test.id,
            testName: test.name,
            daysRunning: daysRunning,
            weekNumber: Math.ceil(daysRunning / 7),
            startDate: startDate.toISOString().split('T')[0],  
            startDateReadable: startDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
            endDate: today.toISOString().split('T')[0],
            endDateReadable: today.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
          }
        });
      }
    }
  }
}

return filteredTests;
```

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FB7agCS54lGZrleqNsj6W%2Fimage.png?alt=media&#x26;token=74010bd5-6b77-4aaa-a47d-e7e91fb184fd" alt=""><figcaption></figcaption></figure>

#### **Node 5: Get Test Analytics Data (Loop)**

1. Add **"HTTP Request"** node
2. Configure:
   * **Method**: GET
   * **URL**: `https://api.intelligems.io/v25-10-beta/analytics/resource/{{ $json.experienceId }}`
   * **Authentication**: None
   * Enable **Send Headers**
     * **Name**: `intelligems-access-token`
     * **Value**: `{{ $json.apiKey }}`
3. Click "Execute step" to verify it works

<figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FumtLe94pm7cFpWZXsahT%252FScreenshot%25202026-01-30%2520at%252011.00.26%25E2%2580%25AFAM.png%3Falt%3Dmedia%26token%3D5770d8fb-e58a-45a0-abdc-09f759505b42&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=5ff81b64&#x26;sv=2" alt=""><figcaption></figcaption></figure>

#### Node 6: Check if below threshold

* Add **"Code"** node
* Select **"Code in JavaScript"**
* Select **"Run Once for All Items"**
* Update the below code so that the `minTotalVisitors`, `minOrdersPerVariant`, `srmPValueThreshold`, and `conversionDropThreshold` values match your threshold requirements. Then paste this code into the Code section in n8n.

```
const analytics = $input.item.json;
const filterData = $('Code in JavaScript1').item.json;
const testName = filterData.testName || "Unknown Test";
const clientName = filterData.clientName || "Unknown Client";
const experienceId = filterData.experienceId;

const THRESHOLDS = {
  minTotalVisitors: 1000,
  minOrdersPerVariant: 50,
  srmPValueThreshold: 0.01,
  conversionDropThreshold: 0.20
};

const overview = analytics.overview || analytics;
const variations = overview.variations || [];

if (!variations || variations.length === 0) {
  return [];
}

let totalVisitors = 0;
let controlVariation = null;
const variantData = [];

for (let i = 0; i < variations.length; i++) {
  const variant = variations[i];
  const sessions = variant.sessions || 0;
  const orders = variant.orders || 0;
  const cvr = sessions > 0 ? orders / sessions : 0;
  
  totalVisitors = totalVisitors + sessions;
  
  const isControl = variant.isControl || variant.name === "Control" || variant.label === "Control";
  
  const variantInfo = {
    name: variant.name || variant.label || "Variant " + i,
    sessions: sessions,
    orders: orders,
    cvr: cvr,
    isControl: isControl
  };
  
  variantData.push(variantInfo);
  
  if (isControl) {
    controlVariation = variantInfo;
  }
}

const failedThresholds = [];
const details = {};

if (totalVisitors < THRESHOLDS.minTotalVisitors) {
  failedThresholds.push("min_total_visitors");
  details.minTotalVisitors = {
    current: totalVisitors,
    required: THRESHOLDS.minTotalVisitors,
    message: "Only " + totalVisitors + " visitors (need " + THRESHOLDS.minTotalVisitors + ")"
  };
}

for (let i = 0; i < variantData.length; i++) {
  const variant = variantData[i];
  if (variant.orders < THRESHOLDS.minOrdersPerVariant) {
    if (!details.minOrdersPerVariant) {
      failedThresholds.push("min_orders_per_variant");
      details.minOrdersPerVariant = [];
    }
    details.minOrdersPerVariant.push({
      variant: variant.name,
      current: variant.orders,
      required: THRESHOLDS.minOrdersPerVariant,
      message: variant.name + ": Only " + variant.orders + " orders"
    });
  }
}

if (variantData.length >= 2 && totalVisitors > 0) {
  const expectedPerVariant = totalVisitors / variantData.length;
  let chiSquare = 0;
  
  for (let i = 0; i < variantData.length; i++) {
    const observed = variantData[i].sessions;
    const expected = expectedPerVariant;
    chiSquare = chiSquare + Math.pow(observed - expected, 2) / expected;
  }
  
  const df = variantData.length - 1;
  let isSRM = false;
  
  if (df === 1 && chiSquare > 6.635) {
    isSRM = true;
  } else if (df === 2 && chiSquare > 9.210) {
    isSRM = true;
  } else if (df >= 3 && chiSquare > 11.345) {
    isSRM = true;
  }
  
  if (isSRM) {
    failedThresholds.push("sample_ratio_mismatch");
    const distribution = [];
    for (let i = 0; i < variantData.length; i++) {
      const v = variantData[i];
      distribution.push({
        variant: v.name,
        sessions: v.sessions,
        percentage: ((v.sessions / totalVisitors) * 100).toFixed(1) + "%"
      });
    }
    details.sampleRatioMismatch = {
      chiSquare: chiSquare.toFixed(2),
      trafficDistribution: distribution,
      message: "Traffic split is uneven"
    };
  }
}

if (controlVariation && controlVariation.cvr > 0) {
  for (let i = 0; i < variantData.length; i++) {
    const variant = variantData[i];
    if (!variant.isControl) {
      const cvrChange = (variant.cvr - controlVariation.cvr) / controlVariation.cvr;
      
      if (cvrChange < -THRESHOLDS.conversionDropThreshold) {
        if (!details.conversionRateDrop) {
          failedThresholds.push("conversion_rate_drop");
          details.conversionRateDrop = [];
        }
        const dropPercent = Math.abs(cvrChange * 100).toFixed(1);
        details.conversionRateDrop.push({
          variant: variant.name,
          change: cvrChange,
          message: variant.name + ": CVR down " + dropPercent + "% vs control"
        });
      }
    }
  }
}

if (failedThresholds.length > 0) {
  return [{
    json: {
      hasIssues: true,
      testName: testName,
      clientName: clientName,
      experienceId: experienceId,
      failedThresholds: failedThresholds,
      details: details,
      totalVisitors: totalVisitors,
      variantCount: variantData.length
    }
  }];
}

return [];
```

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FK1SSLFtLRtcgZTyifXaf%2FScreenshot%202026-02-02%20at%201.38.58%E2%80%AFPM.png?alt=media&#x26;token=c7685bda-f031-4a79-afa7-ea2efebbf704" alt=""><figcaption></figcaption></figure>

#### **Node 7: If hasIssues = True**

1. Add an **"If"** node
2. Set the condition as `{{ $json.hasIssues }}` is euqal to `true`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FDsJDcykGeUXw3qbVthsj%2FScreenshot%202026-02-02%20at%201.47.41%E2%80%AFPM.png?alt=media&#x26;token=40756257-0b8f-403f-8b85-39b598c0a77c" alt=""><figcaption></figcaption></figure>

#### **Node 8: Send to Slack**&#x20;

1. For the **"true"** response only, add a **"Slack"** node where the action is **"Send a message"**

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FEcMap4i2SH1MH0s57SYW%2FScreenshot%202026-02-02%20at%201.48.20%E2%80%AFPM.png?alt=media&#x26;token=4101b8c2-9472-441e-9cb7-45d5178edb11" alt=""><figcaption></figcaption></figure>

2. **Authentication**:

* Click "Create New Credential"
* Click "Connect my account" and follow the prompts

3. **Channel/Use**:

* Under "Send Message To" configure where you want this slack message to appear

4. **Message**:

* in "Message Text" input:

```
🔴 *TEST HEALTH ALERT*

*Client:* {{ $json.clientName }}
*Test:* <https://app.intelligems.io/experiment/{{ $json.experienceId }}|{{ $json.testName }}>
*Failed Threshold(s):* {{ $json.failedThresholds }}

*Action Required:* Review test setup and consider pausing if issues persist.
```

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FFzAQ4nV9AtH8Fc653VME%2FScreenshot%202026-02-02%20at%201.36.45%E2%80%AFPM.png?alt=media&#x26;token=6d904284-fcd4-4080-bce3-1d19513e0a72" alt=""><figcaption></figcaption></figure>

### Step 3: Activate the Workflow <a href="#step-4-activate-the-workflow" id="step-4-activate-the-workflow"></a>

1. Once everything works, click **"publish"** at the top to make this workflow go live!
2. Your workflow will now run 3 times a day and notify you if an active test does not meet your threshold.
