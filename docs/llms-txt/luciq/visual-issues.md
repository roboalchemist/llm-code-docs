# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/ai-features/detect-agent/visual-issues.md

# Visual Issues

### Overview

**AI Visual Issues** is a feature built on top of Session Replay. Once enabled, it uses AI to scan screenshots captured during user sessions and flag visual defects such as:

* Misaligned elements or overlapping UI
* Color variations that don’t match design spec
* Unexpected layout shifts or gaps
* Text overflow, clipping, or truncation
* Visual artifacts, noise, or anomalies

These issues get surfaced as **Visual Issue events**, which you can filter and inspect alongside normal session data.

### How to Use

You need to have the **Session Replay** product enabled to be able to enable the AI Visual Issues feature. Once the feature is enabled, you follow these steps:

#### Step-by-Step

1. On the Session Replay list, use the new “AI Issues” filter to only show sessions flagged with AI issues including visual issues.

   <div align="left"><figure><img src="https://files.readme.io/e5631b68409cf7f0e1d02e5b35c2dbc7febec9cefffd16b551c23ed2ec1f6de4-image.png" alt="" width="563"><figcaption></figcaption></figure></div>
2. Open a session with flagged issues. Two ways to navigate:
   * Scroll through the event timeline to find the visual issue event.
   * Click the purple dot on the timeline to jump directly to the issue’s screenshot view.
   * Use the new AI issues filter, you can select “Visual Issues”
3. Viewing a Visual Issue event shows:
   * The exact screenshot where the issue was detected
   * A descriptive summary of the issue (e.g. “element misaligned by 4px”)

### How It Works

* No instrumentation changes required - once enabled, existing session screenshots are routed to the visual analysis pipeline.
* Screenshots are passed through an AI model for analysis.
* When anomalies are detected, a Visual Issue event is emitted in the timeline at the same timestamp as the screenshot.
* The event payload includes descriptive text of the anomaly
* On the front end, UI surfaces let you filter and inspect these events alongside other session data.

### Compatibility & Requirements

* Supported Platforms: All mobile platforms currently supported by Luciq (iOS, Android, React Native, etc.)
* Prerequisite: Session Replay must be enabled
* No SDK version upgrade needed (feature is server-side)

### Limits & Quotas

* Per-account monthly cap: Up to **1,000 analyzed sessions**
* Maximum visual issues generated per month: 1,000

### Getting Access

* Beta / Invite-only: At present, the feature is available by invitation only.
* To request access:
  * Submit a request via Intercom / support chat
  * If you're an Enterprise customer, reach out to your customer success manager to be added to the waitlist.
* Once approved, the feature will be toggled on from the backend - no SDK changes are needed.
