# Source: https://docs.intelligems.io/developer-resources/external-api/automations-and-guides/scheduled-analysis-building-7-and-14-day-post-launch-test-reports.md

# Scheduled Analysis: Building 7 & 14-Day Post-Launch Test Reports

## Overview

This guide shows you how to build a fully automated reporting engine that keeps both your team and your clients informed without manual effort.

Every day, the workflow checks for tests that are either 7 or 14 days old, pulls fresh Intelligems results, leverages AI to generate an in-depth Internal CRO Strategist Report, and crafts a concise, client-ready summary—all delivered directly into a threaded Slack message for easy discussion.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F0iTNotQCUI7QZxDCng9Z%2FScreenshot%202026-01-30%20at%2011.23.00%E2%80%AFAM.png?alt=media&#x26;token=ceacb297-b044-49b0-89f3-371d7a298f1b" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
AI can make mistakes. Always check it's work before sharing with a client.
{% endhint %}

### Softwares Used

To build this automated reporting pipeline, you will need the following tools:

* [n8n](https://n8n.io/): The primary workflow automation platform used to connect APIs and schedule tasks.
* [Groq](https://console.groq.com): A high-speed AI inference engine used to process test data and generate natural language reports.
  * *Note: You can swap this for OpenAI or Anthropic if preferred, but this guide uses Groq for its free API tier*.
* [Slack](https://api.slack.com/apps): The final destination where the AI-generated health checks and reports will be posted.

## How to Create Your Scheduled Test Analysis

### Step 1: Get Your API Keys

#### Groq API Key (Or your AI of Choice)

* Go to <https://console.groq.com>
* Sign up for free (no credit card needed)
* Click "API Keys" on the top nav
* Click "Create API Key"
* Name the key & press submit
* Copy and save the key (starts with `gsk_`)

#### Intelligems API Key(s)

To request access and receive your API key, [contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

### Step 2: Create the Workflow in n8n <a href="#how-to-create-an-automated-test-monitoring-integration-for-slack" id="how-to-create-an-automated-test-monitoring-integration-for-slack"></a>

#### Node 1: Schedule Trigger

1. Click the **"+"** button to add a node
2. Search for **"Schedule Trigger"**
3. Configure it:
   * **Trigger Interval**: "Days"
   * **Days Between Triggers**: 1 (runs daily)
   * **Trigger at Hour**: Pick a time (e.g., 9am)
   * **Trigger at Minute**: 0

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FXpShJzNcRzbDbCt3408k%2FScreenshot%202026-01-29%20at%208.37.47%E2%80%AFAM.png?alt=media&#x26;token=798b9c09-8001-45b9-8e40-d70a236861a3" alt="" width="375"><figcaption></figcaption></figure>

#### Node 2: Create Organization List

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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FDRBeDys0ClEIoItfUdsH%2FScreenshot%202026-01-30%20at%2010.58.08%E2%80%AFAM.png?alt=media&#x26;token=fdc79f48-af06-4251-809a-3fd2a5864bc9" alt=""><figcaption></figcaption></figure>

#### Node 3: Get All Running Tests

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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2F4VQawiu8Aj6jmzn9W7Tt%2FScreenshot%202026-01-30%20at%2010.59.12%E2%80%AFAM.png?alt=media&#x26;token=c21a9cec-3937-429a-8eb7-ca459dedb53a" alt=""><figcaption></figcaption></figure>

#### Node 4: Filter Tests by Status = "started" AND Duration

Now we need to filter for both `status = "started"` AND tests at 7 or 14 days:

* Add **"Code"** node
* Select **"Code in JavaScript"**
* Select **"Run Once for All Items"**
* Update the below code so that `InsertOrgId` maps to match the Intelligems organization IDs of your clients (you can find these in Intelligems under Settings > General > Organization Settings), the `name` value is display name for your clients, and the `apiKey` value is the Intelligems API Key for those clients. Then paste this code into the Code section in n8n.

```javascript
// Filter for running tests that are at 7 or 14 days old
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
      // First check if status is "started"
      if (test.status !== "started") {
        continue;
      }
      
      // Then check if it's been 7 or 14 days
      const startDate = new Date(test.startedAtTs);
      const daysRunning = Math.floor((today - startDate) / (1000 * 60 * 60 * 24));
      
      // Check if test is at 7 or 14 days
      if (daysRunning === 7 || daysRunning === 14) {
        filteredTests.push({
          json: {
            clientName: clientData.name,
            apiKey: clientData.apiKey,
            experienceId: test.id,
            testName: test.name,
            daysRunning: daysRunning,
            weekNumber: daysRunning === 7 ? 1 : 2,
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

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fyj954QfON4RqprZbK2hG%2FScreenshot%202026-01-30%20at%2010.59.53%E2%80%AFAM.png?alt=media&#x26;token=442d49c2-60a2-4eda-905b-8896addba785" alt=""><figcaption></figcaption></figure>

#### Node 5: Get Test Analytics Data (Loop)

1. Add **"HTTP Request"** node
2. Configure:
   * **Method**: GET
   * **URL**: `https://api.intelligems.io/v25-10-beta/analytics/resource/{{ $json.experienceId }}`
   * **Authentication**: None
   * Enable **Send Headers**
     * **Name**: `intelligems-access-token`
     * **Value**: `{{ $json.apiKey }}`
3. Click "Execute step" to verify it works

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FumtLe94pm7cFpWZXsahT%2FScreenshot%202026-01-30%20at%2011.00.26%E2%80%AFAM.png?alt=media&#x26;token=5770d8fb-e58a-45a0-abdc-09f759505b42" alt=""><figcaption></figcaption></figure>

#### Node 6: Send to AI Agent (Internal Report)

1. Click the **"+"** button after your analytics HTTP Request node
2. Search for **"AI Agent"** or look under "AI Nodes"
3. Click **"AI Agent"**

**Configure the AI Agent:**

1. **Under "Chat Model"** section:
   * Click "Select model"
   * Choose **"Groq"** from the list (Or swap in your AI of choice)
   * Click "Create New Credential"
   * Paste your Groq API key (the one starting with `gsk_`)
   * Select Model: **"llama-3.3-70b-versatile"** (best free model) or **"mixtral-8x7b-32768"**
2. Back under the main AI Agent Screen:
   * **Under "Source for Prompt"** set it to Define below
   * **Under "Prompt"** section:
     * In the text area, paste the below prompt. You can customize this prompt to meet your specific needs.

```
Analyze the A/B test data below and create a Slack-formatted report that matches this EXACT structure:

*A/B TEST RESULTS: [Test Name]*

📊 *Test Overview*
• Run Period: {{ $('Code in JavaScript1').item.json.startDateReadable }} to {{ $('Code in JavaScript1').item.json.endDateReadable }} ({{ $('Code in JavaScript1').item.json.daysRunning }} days)
• Traffic Split: [X] sessions per variant
• Conversions: [Variant 1] ([X] orders) | [Variant 2] ([X] orders)

💰 *Performance Comparison*

For each variant, display results in this order:

*[Use actual variant name from data, e.g., $Off or %Off]:*
Revenue Per Visitor: [+/- X.XX%] (confidence: [XX%])
Conversion Rate: [+/- X.XX%] (confidence: [XX%])
Average Order Value: [+/- X.XX%] (confidence: [XX%])
Profit Per Visitor: [+/- X.XX%] (confidence: [XX%]) // include only if COGS data exists
Projected Monthly Impact: [+/- $X,XXX]
Sample: [X] orders from [X] sessions

🔍 *Key Insights*

*Signal Strength:* [Strong / Moderate / Weak / Insufficient]
- Explain what the data pattern shows
- Identify which metrics are aligned vs. conflicting
- Note any segments or patterns worth investigating

*DECISION FRAMEWORK*

*Sample Adequacy:* [Met / Not Met]
✓ Minimum 7-day runtime including weekend
✓ Minimum 350 conversions per variant
✓ Minimum 8,000 sessions per variant

✅ *Decision:* [IMPLEMENT / ITERATE / ABANDON / EXTEND]

IMPLEMENT if:
- Sample adequacy met
- Primary metric shows ≥4% improvement
- Confidence level ≥85%
- Downside risk is acceptable (lower bound of credible interval ≥-2%)

ABANDON if:
- Sample adequacy met
- Primary metric shows ≤-4% decline
- Confidence that variant is worse ≥85%
- Upside potential is negligible (upper bound ≤+2%)

ITERATE if:
- Sample adequacy met
- Mixed signals (one key metric up, another down)
- OR improvement exists but confidence <85% and test passed planned end date
- Recommendation: [specific iteration to test next]

EXTEND if:
- Sample adequacy not met
- OR confidence between 70-85% with meaningful trend (≥3% change)
- Estimated runway: [X] additional days needed

*Rationale:* [1-2 sentences explaining the decision]

🔗 *View Full Results*
https://app.intelligems.io/experiment/{{ $('Code in JavaScript1').item.json.experienceId }}

Formatting Rules
- Use one asterisks * for bold text (e.g., *Variant A*)
- Round percentages to 2 decimal places (e.g., +3.47%, -2.03%)
- Round confidence scores to whole numbers (e.g., 87%, 92%)
- Format revenue with commas, no decimals (e.g., +$8,450, -$3,200)
- Use proper em dashes (—) for breaks in text
- Keep spacing consistent
- For confidence, use the p2bc value: if p2bc = 0.87, display as "87%"
- Include emojis exactly as shown: 📊 💰 🔍 📋 ✅ 🔗
- Use bullet points with - symbol
- DO NOT include the word "text:" or any JSON formatting in your output
- Output only the formatted message content, no JSON wrapper

Decision Calculation Guidelines
Determining Confidence: Use p2bc (probability to beat control) directly as the confidence percentage

Estimating Extension Time:
- Calculate average daily session volume: total sessions ÷ days run
- Determine sessions needed for 8,000 minimum per variant
- For confidence building: if confidence is 70-75%, assume need 80% more data; if 75-85%, assume need 40% more data
- Convert to days and cap at 14 additional days maximum
- If >14 days needed, classify as ITERATE instead

Signal Strength Classification:
- Strong: confidence ≥85% and absolute change ≥4%
- Moderate: confidence 70-85% OR absolute change 3-4%
- Weak: confidence 50-70% OR absolute change 1-3%
- Insufficient: confidence <50% OR duration <7 days

Handling Multiple Variants:
- Report all variants separately
- In decision section, identify best-performing variant
- If multiple variants show promise, note this in rationale
- IMPORTANT: Use the actual variant names from the data (like "$Off", "%Off", "Variant A", etc.), do NOT use placeholder text like "[Variant Name]"

Test Name: {{ $('Code in JavaScript1').item.json.testName }}
Days Running: {{ $('Code in JavaScript1').item.json.daysRunning }}

Input Data
{{ JSON.stringify($json, null, 2) }}
```

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FGtliDvrDq3FAcsYQyD0H%2FScreenshot%202026-01-30%20at%2011.01.07%E2%80%AFAM.png?alt=media&#x26;token=dcbf835f-3ba5-4319-ba7f-4088ae94e674" alt=""><figcaption></figcaption></figure>

#### Node 7: Send to AI Agent (Client Overview)

Set up another AI Agent node identical to the one you set up above in Node 6. But for this agent, have the prompt be:

```
Transform this in-depth test analysis into a concise client update following the format below. 
Use straightforward, conversational language—skip the industry lingo and statistical terminology. 
The goal is for clients to instantly grasp the results without having to figure out what anything means.
# Required Structure

Hi CLIENT NAME, quick update on the insert test name test:

*Current Results*: The test has been running for [X days/weeks] with [X,XXX] visitors per variant. [Variant A/B/C/D] is currently leading with a [X%] lift in [primary metric]. We're at [XX%] statistical confidence, so [we're close to calling a winner / we need another week or two of data / we can confidently move forward].

*Key Metrics:*
• Conversion Rate: [Variant A: X%] vs [Variant B: X%]
• Revenue per Visitor: [Variant A: X%] vs [Variant B: X%]
• Average Order Value: [Variant A: X%] vs [Variant B: X%]
• Est. Monthly Rev Change for winning variant: *+/-$[number]*

*Intelligems Link:* <https://app.intelligems.io/experiment/{{ $('Code in JavaScript1').item.json.experienceId }}|HERE>

*What's next:* [e.g., "Planning to let this run until end of week to hit 95% confidence, then we'll implement the winner" / "Results are clear - I'll prepare a rollout plan for the winning variant" / "Considering a follow-up test based on what we're seeing"]

Happy to discuss in more detail if you have questions!

# Rules
Keep it more concise and easier to digest than internal reporting.
Focus on the most important numbers—skip the rest.
Format percentages with one decimal place (+2.1%, -15.7%), except drop the decimal when it's zero (+2% not +2.0%).
Format estimated monthly revenue changes as whole numbers with comma separators (+$12,395 or -$7,123).
Write in a relaxed, assured tone that sounds natural.
Stick to only the specified section headers.
Bold text by wrapping it in single asterisks (*like this*).
Begin each line in the Key Metrics section with a bullet point (•). DO NOT use dashes, use the bullet character.


# Internal CRO test report:

{{ $json.output }}
```

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fep8ENBZ8QeBrqpl37rAJ%2FScreenshot%202026-01-30%20at%2011.01.34%E2%80%AFAM.png?alt=media&#x26;token=7c93d254-9c84-4153-b086-3b349a46a474" alt=""><figcaption></figcaption></figure>

#### Node 8: Send to Slack (Notification)

1. Add **"Slack"** node where the action is **"Send a message"**
2. **Authentication**:
   * Click "Create New Credential"
   * Click "Connect my account" and follow the prompts
3. **Channel/Use**:
   * Under "Send Message To" configure where you want this slack message to appear
4. **Message**:
   * in "Message Text" input:

```
Client: {{ $('Code in JavaScript1').item.json.clientName }}
Test: <https://app.intelligems.io/experiment/{{ $('Code in JavaScript1').item.json.experienceId }}|{{ $('Code in JavaScript1').item.json.testName }}> - reached {{ $('Code in JavaScript1').item.json.daysRunning === 7 ? '7 days' : '14 days' }}
```

5. Click **"Execute node"** to test

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FG3oglwkCU2EtMEZBkbfk%2FScreenshot%202026-01-30%20at%2011.01.59%E2%80%AFAM.png?alt=media&#x26;token=acd76cf6-9bb9-4055-8ddd-6d352d7f27b6" alt=""><figcaption></figcaption></figure>

#### Node 9: Send to Slack (Report)

1. Add **"Slack"** node where the action is **"Send a message"**
2. Set the same channel as your 8th Node.
3. In "Message Text" input:

```
{{ $('AI Agent').item.json.output }}



*Slack Update for Client*

{{ $('AI Agent1').item.json.output }}
```

4. Under Options, add a "Reply to a message" option.
5. For "Message Timestamp to Reply To" input `{{ $json.message_timestamp }}`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2FWfdin0kC9U8sEQgg4sL0%2FScreenshot%202026-01-30%20at%2011.02.25%E2%80%AFAM.png?alt=media&#x26;token=c163afa9-f9f2-4b6c-bf48-bca12e79abb9" alt=""><figcaption></figcaption></figure>

### Step 3: Test Your Workflow

1. Click the **"Test workflow"** button at the bottom
2. Watch each node execute
3. Check your Slack channel for the message
4. If anything fails, click on the red node to see the error

### Step 4: Activate the Workflow

1. Once everything works, click **"publish"** at the top to make this workflow go live!
2. Your workflow will now run daily and check for tests at 7 or 14 days, analyze them, and give you a notification in slack with the analysis!

<br>
