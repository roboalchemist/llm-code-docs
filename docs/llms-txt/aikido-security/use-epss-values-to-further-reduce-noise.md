# Source: https://help.aikido.dev/code-scanning/miscellaneous/use-epss-values-to-further-reduce-noise.md

# Use EPSS Values to Further Reduce Noise

Aikido’s EPSS-based prioritization can further **auto-ignore** or **downgrade low-risk vulnerabilities**, based on EPSS values. EPSS, which stands for Exploit Prediction Scoring System, predicts the real-world likelihood a vulnerability will be exploited in the next 30 days.

### Important notes <a href="#important-notes" id="important-notes"></a>

* We check EPSS on a daily basis. When the value reaches a threshold, an issue will either be **ignored** or **unignored**,
* EPSS is available everywhere in Aikido. From your IDE, over to PR gating in your CI to the feed.
* When you disable EPSS scoring again, all issues that were previously ignored, will be unignored again.

### How to enable EPSS-based Prioritisation <a href="#how-to-enable-epss-based-prioritisation" id="how-to-enable-epss-based-prioritisation"></a>

**Step 1:** Navigate to the **EPSS-Based Prioritization** settings in the [Advanced Settings tab](https://app.aikido.dev/settings/advanced).

**Step 2:** Click the '⚙️ Manage' button in the EPSS-based prioritisation section

![Settings for scan frequency and advanced scan configuration in a security monitoring dashboard.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e1a25c435a748b87a20dd2d7d6ad4a7ae4004eb3%2Fuse-epss-values-to-further-reduce-noise_304f3965-20ad-4d29-a500-cf48ee45e98f.png?alt=media)

**Step 3:** Choose which rules you want to have applied in your Aikido workspace

* **Auto-Ignore issues with an EPSS below 1%**.*This will auto-ignore vulnerabilities that have a very low chance of being exploited.*
* **Lower severity with 10 points for EPSS between 1% and 5%**.*This lowers the severity of vulnerabilities with 10 points. Example. A high severity issue with score 60 will be downgraded to score 50.*
* **Lower severity with 5 points for EPSS between 5% and 10%**.*This lowers the severity of vulnerabilities with 5 points.*

![EPSS-based vulnerability prioritization options for automated issue ignoring and severity adjustment.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-dd55d11be6e942570dcb9331dae13da51dbbe620%2Fuse-epss-values-to-further-reduce-noise_ba92e22d-783f-4716-90b7-1e409e908900.png?alt=media)

**Step 6:** Click **Save EPSS-Based Prioritization** to apply your noise-reduction rules.

> Manually trigger a rescan to apply the new prioritization immediately, or wait until the next scheduled daily scan for changes to take effect.
