# Source: https://docs.verda.com/storage/container-registry/tag-rules-syntax.md

# Tag rules syntax

Tag rules follow the doublestar (aka globstar: `**`) matching pattern. Regex is unfortunately unsupported.

#### Patterns

**doublestar** supports the following special terms in the patterns:

<table data-full-width="false"><thead><tr><th width="158.92251586914062">Special Terms</th><th width="319.5">Meaning</th><th width="190.5">Example pattern</th><th width="190">Example matches</th><th width="203.3526611328125">Example doesn't match</th><th width="270">Reason</th></tr></thead><tbody><tr><td><code>*</code></td><td>matches any sequence of characters (excludes /)</td><td><code>env-*/app</code></td><td><p><code>env-prod/app</code></p><p><code>env-dev/app</code></p></td><td><code>env-prod/sub/app</code></td><td>Only matches the single directory level</td></tr><tr><td><code>**</code></td><td>matches any sequence of characters (includes /)</td><td><code>**/redis</code></td><td><p><code>lib/redis</code></p><p><code>proj/cache/redis</code></p></td><td><code>lib/redis-proxy</code></td><td>Matches any path ending in exactly <code>/redis</code></td></tr><tr><td><code>?</code></td><td>matches any single character (excludes /)</td><td><code>qa-team?/*</code></td><td><code>qa-team0</code><br><code>qa-team9</code></td><td><code>qa-team10/app</code></td><td>Forces a single digit/letter suffix</td></tr><tr><td><code>[class]</code></td><td>matches any single character against a class of characters (See below) (excludes /)</td><td></td><td></td><td></td><td>see below</td></tr><tr><td><code>{alt1,alt2,...}</code></td><td>matches a sequence of characters if one of the comma-separated alternatives matches</td><td><code>release-{beta,rc}</code></td><td><p><code>release-beta</code></p><p><code>release-rc</code></p></td><td><code>release-alpha</code></td><td><code>alpha</code> is not an alternative</td></tr></tbody></table>

Any character with a special meaning can be escaped with a backslash (`\`).

**Character classes** support the following:

<table data-full-width="false"><thead><tr><th width="128">Class</th><th width="250.5">Meaning</th><th width="179">Example pattern</th><th width="163.5">Example matches</th><th width="201">Example doesn't match</th><th width="276.5">Reason</th></tr></thead><tbody><tr><td><code>[abc]</code></td><td>matches any single character within the set</td><td><code>service-[ab]</code></td><td><code>service-a</code><br><code>service-b</code></td><td><code>service-c</code></td><td><code>c</code> is not in Character class <code>[ab]</code></td></tr><tr><td><code>[a-z]</code><br><code>[0-9]</code></td><td>matches any single character in the range</td><td><code>build-[0-9]</code></td><td><code>build-1</code><br><code>build-7</code></td><td><code>build-a</code></td><td><code>a</code> not in range</td></tr><tr><td><code>[^class]</code></td><td>matches any single character which does <em>not</em> match the class</td><td><code>release-[^9]*</code></td><td><code>release-1.0</code></td><td><code>release-9.0</code></td><td><code>9</code> is excluded from the class</td></tr></tbody></table>

**Example for common tag pattern: Semantic Versioning (SemVer):**

This is the most common versioning strategy (e.g., `v1.0.1`, `1.5.2`).

This pattern uses alt-matches with an empty alt option, matching "nothing":

* The pattern `{v,}` matches `v` or an empty string ("nothing") which means it can match strings which start with `v` or not.
* The pattern `[0-9]{,[0-9],[0-9][0-9]}` matches a single digit (always) and one of 3 alt options: empty, single digit, or two digits; this gives us a matching pattern between 0 to 999
  * This limits us to to max version of `v999.999.999` which should suffice for most usage. If not enough, just add another alt choice with more digits: `[0-9]{,[0-9],[0-9][0-9],[0-9][0-9][0-9]}`

<table data-full-width="false"><thead><tr><th>Goal</th><th>Pattern</th><th>Matches</th><th>Does Not Match</th></tr></thead><tbody><tr><td>Strict 3-part SemVer with optional <code>v</code> prefix</td><td><code>{v,}[0-9]{,[0-9],[0-9][0-9]}.[0-9]{,[0-9],[0-9][0-9]}.[0-9]{,[0-9],[0-9][0-9]}</code></td><td><p><code>v1.5.9</code></p><p><code>7.10.3</code></p><p><code>1.250.22</code></p></td><td><code>v1</code><br><code>v1.0</code><br><code>latest</code></td></tr></tbody></table>
