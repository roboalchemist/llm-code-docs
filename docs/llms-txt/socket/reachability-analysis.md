# Source: https://docs.socket.dev/docs/reachability-analysis.md

# Reachability Analysis

Socket SCA with Reachability Analysis allows you to safely disregard unreachable vulnerabilities and easily patch the ones that matter.

Socket SCA with Reachability Analysis allows you to safely disregard unreachable vulnerabilities and easily patch the ones that matter.

Modern applications are built on mountains of open‑source code. A single `package.json` or `pom.xml` can pull in hundreds—sometimes thousands—of transitive packages. Traditional security scanners treat every one of those packages the same, burying you in vulnerability alerts that may never be exploitable in your code base.

**Reachability Analysis changes that.** By understanding which dependencies your application actually uses, Socket filters out CVEs that can’t affect you — allowing you to focus on the ones that can.

## The Problem: Noise Overload

If you’ve ever opened a security dashboard to find hundreds of “critical” issues, you know the feeling:

* **Alert fatigue.** When everything looks urgent, nothing feels urgent.
* **Wasted cycles.** Triaging false‑positive CVEs steals hours from real work.
* **Slow remediation.** Teams struggle to identify the vulnerabilities that really matter to their application.

We developed reachability analysis to fundamentally change this dynamic.

# Key features

* Based on top-tier research.
* Scans direct and indirect dependencies.
* Works with any CI platform. No complex configurations. No agents required.

## Before Socket: Overwhelming Noise

Traditional SCA tools do not distinguish between exploitable and unexploitable vulnerabilities. As a consequence, more than 80% of the vulnerabilities that developers are remediating are irrelevant and can be safely ignored.

## After Socket: Clean Signal

Socket employs Reachability Analysis to eliminate more than 80% false positives. As a consequence, developers only need to remediate the remaining few vulnerabilities that are relevant.

# Reachability Tiers

Socket offers 3 tiers of reachability analysis with increasingly better levels of false positive reduction.

The differences are as follows:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th />

      <th>
        Tier 3 — 

        [Dependency Reachability](https://docs.socket.dev/docs/dependency-reachability)
      </th>

      <th>
        Tier 2 –

        [Precomputed Reachability](precomputed-reachability)
      </th>

      <th>
        Tier 1 –

        [Full Application Reachability](full-application-reachability)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **False positive reduction**
        (varies between codebases)
      </td>

      <td>
        Eliminate **up to 35%** false positives.
      </td>

      <td>
        Eliminate **up to 80%** false positives in transitive dependencies.
      </td>

      <td>
        Eliminate **up to 90%** false positives.
      </td>
    </tr>

    <tr>
      <td>
        **Works out of the box**
      </td>

      <td>
        * *Yes.*\* Works via all Socket integrations (API, CLI, Socket for GitHub, etc.)
      </td>

      <td>
        * *Yes.*\* Works via all Socket integrations (API, CLI, Socket for GitHub, etc.)
      </td>

      <td>
        * *No, but easy to setup.*\* Need to add a CLI command or GitHub Action to the repository.
      </td>
    </tr>

    <tr>
      <td>
        **Direct vs. Transitive**
      </td>

      <td>
        Identify reachable vulnerabilities in **transitive** dependencies.
      </td>

      <td>
        Identify reachable vulnerabilities in **transitive** dependencies.
      </td>

      <td>
        Identify reachable vulnerabilities in both **direct and transitive** dependencies.
      </td>
    </tr>

    <tr>
      <td>
        **Reachability**
      </td>

      <td>
        • Eliminates unreachable vulnerabilities at the **package level**.

        • Scans all dependency source code to determine which packages are imported/required.
      </td>

      <td>
        • Eliminates unreachable vulnerabilities in **transitive dependencies** at a **function level** on **dependency code**.

        • Scans all dependency source code to determine which functions are called through your direct dependencies.
      </td>

      <td>
        • Eliminates unreachable vulnerabilities at a **function level**  on **application and dependency code**.

        • Pinpoints the exact locations in your code affected by reachable vulnerabilities.
      </td>
    </tr>

    <tr>
      <td>
        **Availability**
      </td>

      <td>
        Available for customers on the **Free, Team, and Enterprise plans**.
      </td>

      <td>
        Available for customers on the **Team and Enterprise plans**.
      </td>

      <td>
        Available for customers on the **Enterprise plan**.
      </td>
    </tr>
  </tbody>
</Table>

# Reachability Ecosystem Support

| Ecosystem                       | Package manager           | Tier 3 — [Dependency Reachability](https://docs.socket.dev/docs/dependency-reachability) | Tier 2 – [Precomputed Reachability](precomputed-reachability) | Tier 1 – [Full Application Reachability](full-application-reachability) |
| :------------------------------ | :------------------------ | :--------------------------------------------------------------------------------------- | :------------------------------------------------------------ | :---------------------------------------------------------------------- |
| **JavaScript and TypeScript**   | npm, yarn, pnpm           | ✅                                                                                        | ✅                                                             | ✅                                                                       |
| **Python**                      | uv, pip, Poetry, Anaconda | ✅                                                                                        | ✅                                                             | ✅                                                                       |
| **Go**                          | Go Modules                | ✅                                                                                        | ✅                                                             | ✅                                                                       |
| **Java**                        | Maven, Gradle             | ✅                                                                                        | ✅                                                             | ✅                                                                       |
| **.NET (C#, F#, Visual Basic)** | Nuget, Paket              | 🌙 Not planned\*                                                                         | ✅                                                             | ✅                                                                       |
| **Scala**                       | sbt, Maven, Gradle        | ✅                                                                                        | ✅                                                             | ✅ ( CDX SBOM required)                                                  |
| **Kotlin**                      | Maven, Gradle             | ✅                                                                                        | ✅                                                             | ✅ ( CDX SBOM required)                                                  |
| **Ruby**                        | Bundler                   | ✅                                                                                        | ✅                                                             | ✅                                                                       |
| **Rust**                        | cargo                     | 🌙 Not planned                                                                           | ✅                                                             | ✅                                                                       |

\**Note: Our research has shown that NuGet published packages have a low likelihood to contain extra dependencies that are detectable at the package level. As a result, we’re focusing on improved detection through Tier 2 Reachability instead.*