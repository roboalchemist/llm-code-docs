# Source: https://docs.luciq.ai/organization-settings/others/sdk-performance-and-footprint.md

# SDK Performance & Footprint

### Introduction

Luciq’s SDK is built with performance in mind. This page provides a transparent overview of the SDK’s performance overhead and footprint, including launch time impact, app size increase, memory usage, network payload, and on-disk storage.

We also outline the internal practices and commitments that ensure the SDK remains lightweight and reliable.

By understanding these metrics and policies, you can be confident that Luciq won’t compromise your app’s user experience.

### Launch Time

Luciq adds only a very small delay to your app’s launch. The SDK initializes quickly, deferring heavy operations to background threads so as not to block the main thread. In our measurements, Luciq’s initialization contributes roughly **10–40 milliseconds** to cold app startup, varying by device performance and platform. On modern high-end devices the added overhead is around 10 ms, while on older or low-end devices it can be up to \~40 ms (still a fraction of a second, and typically imperceptible to users).

| Platform    | Test Device    | Extra Cold-Launch Time |
| ----------- | -------------- | ---------------------- |
| **iOS**     | iPhone 14 Pro  | **+54 ms**             |
|             | iPhone 12 Pro  | **+64 ms**             |
| **Android** | Samsung S20 FE | **+38.9 ms**           |
|             | Pixel 5A       | **+50 ms**             |

**Why the hit is small?**

* SDK initialization runs on low-priority background threads.
* Heavy work is lazily loaded after the first frame.
* A CI gate blocks any commit that regresses launch by > 10 % on Pixel 6.

Note: These values represent the additional time during app launch with Luciq integrated.

### App Size

The Luciq SDK is lightweight in terms of binary size. Integrating Luciq will increase your app’s size by only a few megabytes:

| Metric                                          | iOS         | Android     |
| ----------------------------------------------- | ----------- | ----------- |
| **Download size** (what users fetch) \[APK/IPA] | **+3.6 MB** | **+4 MB**   |
| **Install size** (on device)                    | **+10 MB**  | **+6.8 MB** |

The **download size** overhead (\~3 MB) is the additional size users download from the app store due to Luciq. The **install size** overhead (approximately 5–8 MB) is the extra storage taken on the device once the app is installed.

The exact numbers vary by platform and architecture (for example, iOS app thinning ensures that only the necessary slices are downloaded for a device, on the lower end of the range). We continuously optimize and strip unnecessary assets from the SDK to minimize these values.

### Memory

Luciq’s in-app memory footprint is modest. At runtime, the SDK uses roughly **7.3 MB of RAM on iOS** and about **28 MB on Android** under typical conditions.

| Platform    | Typical Memory Usage (RAM) |
| ----------- | -------------------------- |
| **iOS**     | **\~7.3 MB**               |
| **Android** | **\~28 MB**                |

These figures represent the approximate memory overhead introduced by Luciq in a running app. The difference between iOS and Android usage is expected due to platform internals and how each OS manages memory (e.g., Android includes the JVM and additional libraries).

In both cases, the memory overhead is a small fraction of what most apps consume and should not affect your app’s performance. We also ensure that Luciq’s memory usage remains stable over time (no leaks) and clean up any temporary allocations quickly.

**What we do to keep memory low?**

* Large screenshots and logs are streamed to disk, not held in RAM.
* Static-analysis and long-run tests ensure zero memory leaks.

### Network Overhead

Luciq only uses network bandwidth when necessary (for sending reports or performance data), and the payload sizes are relatively small. There is no continuous or significant background network traffic from the SDK. Typical payload sizes for different Luciq features are:

| Payload Type                       | Typical Size     |
| ---------------------------------- | ---------------- |
| **Bug report** (screenshot + logs) | **200 – 300 KB** |
| **Crash report**                   | **100 – 200 KB** |
| **APM metric** (Performance Trace) | **3 – 5 KB**     |

* **Bug Reports:** When a user submits a bug report via Luciq, the SDK sends diagnostic data including a screenshot, device details, console logs, and user steps. The screenshot is the largest component (usually a few hundred kilobytes when compressed). In total, a bug report's network payload typically ranges from a few hundred KB to around 1 MB. This size isn't from a single request: it’s split across multiple parts: the main report request, logs, and any attachments. If users include extra images or chat logs, the total size can be higher, but that’s driven by user content.
* **Crash Reports:** Crash reports contain the crash stack trace, device and session info, and logs. Like bug reports, the data is sent in multiple small requests and typically totals in the hundreds of kilobytes. Luciq sends crash reports on the next app launch, and the overall payload remains minimal.
* **APM (Application Performance Monitoring):** Luciq’s APM module sends performance metrics (like app launch time, network request traces, etc.). These are extremely lightweight. Metrics are batched and sent periodically, and each payload is only a few KB. This ensures that even with APM enabled, the continuous network overhead is negligible.

Overall, Luciq’s network impact is minor and will not noticeably affect your users’ data usage or app networking performance.

**How do we optimize network overhead?**

* No continuous background traffic.
* Uploads are compressed and retried later if offline.
* A Wi-Fi-only flag is available.

### Disk Usage

Luciq stores some data on the device to support its features, but this on-disk footprint remains small. We categorize the data stored by the SDK into **transient** vs. **persistent** storage:

| Data class                   | Storage                   | Lifecycle                        |
| ---------------------------- | ------------------------- | -------------------------------- |
| Console Logs                 | Persistent for one launch | Cleared on next start            |
| Network Logs                 | Persistent                | Kept on disk until limit reached |
| Crash stack traces           | Transient                 | Deleted after upload             |
| Attachments (screens, files) | Transient                 | Deleted after upload             |
| User attributes & settings   | Persistent                | Developer-controlled (< 1 MB)    |
| Session & APM data           | Transient                 | Auto-purged once sent            |

* **Transient data:** Temporary files and caches that are **not permanent**. This includes unsent reports, captured logs, crash dumps, and other working files. For example, if a crash happens offline, the report is saved to disk and retried later – that file is transient. These files are automatically cleaned up by the SDK after they are sent or once they are no longer needed. Transient data may grow to a few megabytes in worst-case scenarios (e.g., several reports pending), but the SDK actively purges older data to avoid using too much storage.
* **Persistent data:** Small pieces of data that remain on disk between sessions. This includes things like Luciq SDK settings, user identity (if set), feature flags, and cached configuration received from Luciq’s servers. This persistent footprint is very minimal (on the order of only a few hundred kilobytes). It’s limited to what’s necessary to keep the SDK functioning smoothly and doesn’t significantly grow over time.

In summary, the SDK’s disk usage is lightweight. It won’t bloat your app’s storage, and any temporary files it writes are self-managed and removed in a timely manner. There are also APIs and settings to control data retention if needed (for example, you can manually invoke functions to clear logs or reset the Luciq data if your app has such requirements).

**What do we do to optimize disk usage?**

* Per-bucket caps keep total on-disk use in the low-megabyte range.
* **Manual reset APIs** let you wipe all SDK data if your own storage policy demands it.

### CI Quality Gates

To ensure Luciq remains performant, our engineering process includes **Continuous Integration (CI) quality gates** focused on performance metrics. Every change to the SDK is tested against these gates to catch regressions early:

* **App size gate:** We monitor the SDK’s binary size on each build. If a code change would increase the app download or install size beyond our acceptable threshold, the build is flagged. This prevents unexpected bloat, we fail the build if the SDK grows too large. By enforcing a size budget, we keep the added size around the \~3 MB (download) level and avoid regressions.
* **Launch time gate:** We measure app launch performance with the SDK during development. There is an internal threshold (based on the 10–40 ms overhead window) for what is considered acceptable. If a proposed change causes the SDK initialization to slow down app launch beyond that threshold, it’s caught in CI. This way, we maintain a consistently fast startup. Any increase in startup time must be justified and addressed before release.

These quality gates act as automated guardians of performance. Thanks to them, Luciq’s performance profile stays consistent or improves over time – we don’t allow new releases to suddenly use more memory, be slower, or heavier than previous versions. Our team also regularly profiles the SDK to find further optimizations in CPU, memory, and I/O usage before they ever reach your users.
