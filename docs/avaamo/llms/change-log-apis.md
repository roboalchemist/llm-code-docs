# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis.md

# Change log APIs

An agent goes through several changes by different users in its life cycle (Development, Testing, Staging, Production). For operational efficiency, troubleshooting and auditing, it is important to understand:

* Who did the changes?
* What were the changes performed?
* When was it changed?

You can use Changelog API to get a list of changes made to an agent. The following illustration depicts how analysis can be performed using Changelog API:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZyG113DvYFZLqgT7iREB%2Fimage.png?alt=media\&token=f4070c10-2643-4973-a5a3-3f1bb94a4861)

### **Changelog API versions**

There are two versions of Changelog API available in the platform.

* **Changelog (v1)**: This is the first version of Changelog API. The traceability, logs, and auditing are limited in this version. See [Changelog API (v1)](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api), for more information.
* **Changelog (v2)**: The latest version of the Changelog API, which is available from the v6.0 release onwards. This is a more scalable and extensive version of the changelog API. See [Changelog API (v2)](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api-v2), for more information.

The following table lists a high-level comparison of two versions of changelog API:

<table><thead><tr><th width="201.01514409557424"></th><th width="230.73298532838828">Changelog API (v1)</th><th>Changelog API (v2)</th></tr></thead><tbody><tr><td>Signature</td><td><code>https://cx.avaamo.com/dashboard/change_logs</code></td><td><code>https://cx.avaamo.com/api/v2/change_logs.json</code></td></tr><tr><td>Log Coverage</td><td>Limited</td><td>Extensive</td></tr><tr><td>Response JSON structure</td><td>Nested</td><td>Simplified</td></tr><tr><td>Answers skill changes</td><td>Not Supported</td><td>Supported</td></tr></tbody></table>
