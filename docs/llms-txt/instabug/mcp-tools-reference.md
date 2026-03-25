# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/ai-features/luciq-mcp-server/mcp-tools-reference.md

# MCP Tools Reference

Luciq’s MCP Server provides 10 tools grouped by problem areas

| **Area**                                 | **Tools**                                           | **What they cover**                         |
| ---------------------------------------- | --------------------------------------------------- | ------------------------------------------- |
| **App Context**                          | `list_applications`                                 | Which apps you can work with                |
| **Crash-Level Debugging**                | `list_crashes`, `crash_details`, `crash_patterns`   | Crash groups & their details                |
| **Occurrences Deep-dive**                | `list_occurrences_tokens`, `get_occurrence_details` | Single crash instances (per device/session) |
| **Stability Beyond Crashes (App Hangs)** | `list_app_hangs`                                    | App freezes / UI hangs                      |
| **User Reported Issues (Bugs)**          | `list_application_bugs`, `get_bug_details`          | User-reported issues via Luciq SDK          |
| **User Sentiment & Store Ratings**       | `list_reviews`                                      | User reviews and ratings                    |

The details and context for each tool are detailed below.

### **1. App Context**

***

### `1.1 list_applications`

#### What it does

Returns all applications accessible to your account.

#### Use this when

* Setting up your MCP config and not sure which `slug` / `mode` to use.
* You work across multiple apps and want a quick list in the IDE.

#### Parameters

**None required.**

Optional:

* `platform`: `ios`, `android`, `react_native`, `flutter`
* `limit`, `offset`

#### Key Fields

* **slug** — Identifier used in most tools
* **name** — Display name
* **token** — Needed for the Reviews tool
* **platform** — App platform
* **mode** — App environment
* **created\_at** — Timestamp

#### Usage Examples

* “List all my applications.”
* “Show only iOS applications.”
* “Which apps do I have access to?”

### **2. Crash-Level Debugging**

***

### `2.1 list_crashes`

#### What it does

Shows crash groups for an app: how often they happen, how many users they affect, and basic cause.

#### Use this when

* You want to know “what should we fix first?”
* You’re scanning production for new, recent, or high-impact crashes.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development

#### Useful Filters

* `date_ms` (time window)
* `status_id` (open, closed, in progress)
* `devices`, `os_versions`
* `app_versions`
* `current_views`, `teams`, `platform`

#### Key Fields

* **number** — Crash ID
* **exception** — Main exception message
* **crash\_cause** — File/function of failure
* **crash\_type** — Fatal or non-fatal
* **occurrences\_counter** — Total occurrences
* **affected\_users\_counter** — Unique users affected
* **app\_version** — Version where it occurred
* **last\_occurred\_at** — Latest timestamp
* **severity / level** — Severity indicators

#### Usage Examples

* “Show production crashes for the last 7 days.”
* “List crashes for version 3.0.1.”
* “Show open crashes only.”
* “What are the top Android crashes?”

### `2.2 crash_details`

#### What it does

Shows everything we know about a single crash (stack, versions, status, severity).

#### Use this when

You need to investigate or reproduce the crash.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development
* `number` crash number

#### Key Fields

* **exception** — Full exception
* **exception\_name** — Exception class/type
* **crash\_cause** — Main file/line
* **stack\_frames\[]** — Parsed stack trace
* **min\_app\_version**, **max\_app\_version** — Affected versions
* **crash\_type** — Fatal/non-fatal
* **status\_id** — Current status
* **team** — Assigned team
* **sdk\_version** — SDK version
* **package / ndk\_info / path** — Platform extra fields

#### Usage Examples

* “Show details for crash #12.”
* “Explain the stack trace for crash 45.”
* “Which file caused crash #17?”
* “What versions are affected by crash 5?”

### `2.3 crash_patterns`

#### What it does

Groups a crash’s occurrences by **device**, **app version**, **OS**, **view**, etc. to show where it clusters.

#### Use this when

* You want to understand where a crash is concentrated.
* You want to answer: “Is this crash mostly on Pixel 8? On Android 14? On version 3.0.4?”

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development
* `number` crash number
* `pattern_key`: `devices`, `oses`, `app_versions`, `current_views`, `app_status`, `experiments`

#### Key Fields

* **value** — Group label (device, OS, version, etc.)
* **occurrences\_count** — Occurrences in that bucket
* **first\_seen**, **last\_seen** — Timestamp range

#### Usage Examples

* “Break down crash #20 by device.”
* “Show OS patterns for crash #12.”
* “Which views are tied to crash #3?”
* “Group crash #5 by app versions.”

### **3. Occurrences Deep Dive**

***

### `3.1 list_occurences_tokens`

#### What it does

Lists individual **occurrences** of a crash as ULID tokens, so you can pick specific ones to inspect.

#### Use this when

* You want to inspect or debug specific sessions.
* You want to drill down from a crash group to specific user/device sessions.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development
* `number` crash number

#### Useful Filters

* `Foreground/background`
* `Device model`
* `OS version`
* `App version`
* `Experiments`
* `View/screen`
* `Date range`

#### Key Fields

* **states\_tokens\[]** — ULIDs for occurrences
* **total\_occurrences** — Count of matches

#### Usage Examples

* “List all occurrences for crash #28.”
* “Show only foreground occurrences.”
* “Which iOS 17 devices experienced crash 5?”
* “List occurrences from Pixel devices.”

### `3.2 get_occurrence_details`

#### What it does

Shows the **exact context** of one crash occurrence: device, OS, memory, storage, app status, user, and log URLs.

#### Use this when

You need to reproduce or understand a single session.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development
* `number` crash number
* `ulid` state/occurrence ULID token (obtained from `list_occurrences_tokens`)

#### Key Fields

**state.fields:**

* **app\_version** — Version at crash moment
* **device**, **os** — Device info
* **current\_view** — Active screen
* **app\_status** — Foreground/background
* **memory**, **storage** — Resource usage
* **country**, **city** — Location
* **screen\_size**, **density** — Display metrics
* **reported\_at** — Timestamp
* **email**, **user\_name** — User identity

**logs:**

* Downloadable compressed logs
* Experiment logs

**user:**

* Email, UUID, name

**exception\_message:**

* Exception for this specific occurrence

#### Usage Examples

* “Show occurrence details for token X.”
* “Which device caused this occurrence?”
* “Show logs for the earliest occurrence of crash #8.”
* “What view was active during this crash?”

### **4. Stability Beyond Crashes (App Hangs)**

***

### `4.1 list_app_hangs`

#### What it does

Shows grouped **hang** events (UI freezes) for your application.

The server automatically chooses:

* `FATAL_UI_HANG` for iOS
* `ANDROID_FATAL_HANG` for Android
* Both for cross-platform apps

#### Use this when

You want to find “the app froze for me” issues, not just crashes.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development

#### Useful Filters

Same as crashes: `filters.date_ms`, `status_id`, `app_versions`, `devices`, `os_versions`, `platform`, `current_views`

#### Key Fields

* **number** — Hang ID
* **crash\_type** — Hang classification
* **exception** — Hang summary
* **crash\_cause** — Where it froze
* **occurrences\_counter** — Total hangs
* **affected\_users\_counter** — Unique impacted users
* **platform**, **app\_version**
* **last\_occurred\_at** — Recent hang timestamp

#### Usage Examples

* “Show hangs in production for the last 14 days.”
* “List iOS hangs only.”
* “Which hangs are still open?”
* “What views cause most UI hangs?”

### **5. User-Reported Issues**

***

### `5.1 list_bugs`

#### What it does

Shows **user-reported bugs** (reported via Luciq’s SDK), with simple filtering.

#### Use this when

* You want to see user-submitted issues.
* You’re scanning for new or high-priority bugs in a release.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development

#### Useful Filters

* Status: new, closed, in-progress
* Priority: trivial → blocker
* App version

#### Key Fields

* **number** — Bug ID
* **title** — User-entered title
* **email** — Reporter
* **priority\_id**, **status\_id**
* **reported\_at**, **last\_activity**
* **categories**
* **duplicated\_bugs\_count**

#### Usage Examples

* “Show new bugs for version 3.3.”
* “List all open bugs.”
* “Show bugs reported today.”
* “Which bugs are highest priority?”

### `5.2 bug_details`

#### What it does

Returns detailed bug information including logs, user data, and device metadata.

#### Use this when

You need full context to reproduce the bug.

#### Required

* `slug` application slug
* `mode` beta, production, staging, alpha, qa, development
* `number` bug number

#### Key Fields

**Top-level:**

* **title**, **type** — Bug title & type
* **priority\_id**, **status\_id** — Bug priority & status
* **reported\_at**, **last\_activity** — When it was reported, last update time
* **email**, **tags** — Reporter’s email, tags
* **categories**, **team** — Assigned categories, team

**state.fields (context):**

* os, device, country, city
* app\_version, sdk\_version
* current\_view
* screen\_size, density
* bundle\_id
* user\_attributes
* duration (session length)

**state.logs:**

* user\_steps, network\_log, sessions\_profiler, etc. with url and is\_empty\_array.

#### Usage Examples

* “Show details for bug #468.”
* “What steps did the user take?”
* “Which device was used?”
* “Show the network log for this bug.”

### **6. User Sentiment & Store Ratings**

***

### `6.1 list_reviews`

#### What it does

Lists app reviews (e.g., from store/native/custom prompts) with filters for rating, version, country, etc.

#### Use this when

* You want to correlate user feedback with app stability.
* You want to see 1–2 star reviews for a release.
* You’re checking if a performance or crash issue shows up in user feedback.

#### Required

* `application_token` App Token

#### Useful Filters

* `date_ms.gte` / `lte`
* `app_version`
* `rating` – array of star ratings `[1–5]`
* `country`
* `device`
* `prompt_type` – `custom`, `native`, `app_store`
* `os` (for cross-platform)

#### Key Fields

* **title**, **body** — Review content
* **star\_rating** — 1–5 stars
* **username**, **country**
* **app\_version**, **device**
* **date**
* **has\_suspected\_sessions** — Linked to stability issues
* **has\_custom\_suspected\_sessions**

#### Usage Examples

* “Show 1-star reviews for version 3.0.”
* “List negative reviews from the US.”
* “Show native prompt reviews only.”
* “What are the most recent app store reviews?”
