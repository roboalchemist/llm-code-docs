# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/design-and-architecture/cycle-detection.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/design-and-architecture/cycle-detection.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/design-and-architecture/cycle-detection.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/design-and-architecture/cycle-detection.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/design-and-architecture/cycle-detection.md

# Cycle detection

{% hint style="warning" %}
The cycle detection and architecture as code are deprecated, pending removal in January 2026. They will be replaced by improved architecture capabilities. See the [Sonar newsroom](https://www.sonarsource.com/company/newsroom/) page for more information.
{% endhint %}

No additional configuration is needed beyond ensuring that the rule is included in your Quality Profile. Depending on the language, Sonar enables the rules by default in the Sonar Way profile.

Circular dependencies occur when two or more classes, modules, or elements reference each other, either directly or indirectly. This creates a cyclic dependency graph, preventing a clear and intuitive hierarchy in the codebase, and typically indicates a divergence from the intended abstraction. As a result, understanding, maintaining, and refactoring the code becomes significantly more challenging.

<figure><img src="https://756198905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FaGXmdbBYwaT83rOiXBQW%2Fuploads%2Fgit-blob-564559eb4dcafddeb719acb50658c1c98ae88d50%2Fcycle-detection.png?alt=media" alt="Cycle detection in SonarQube Server"><figcaption></figcaption></figure>

#### Why Circular Dependencies are problematic <a href="#why-circular-dependencies-are-problematic" id="why-circular-dependencies-are-problematic"></a>

Circular dependencies increase architectural complexity, making it harder for teams to modify and extend the code. They introduce tight coupling, reducing modularity and reusability while increasing the risk of unintended side effects when making changes. Additionally, they can cause issues such as:

* Compilation and runtime errors: Some languages struggle to resolve circular dependencies at compile time, leading to build failures or unexpected runtime behavior.
* Code fragility: Changes to one part of the code can have unintended consequences elsewhere, increasing the risk of regressions.
* Performance issues: In dynamically loaded environments, circular dependencies can lead to memory leaks or inefficient initialization sequences.

As a project grows, circular dependencies often lead to even more circular dependencies, further entangling the architecture and increasing technical debt. Over time, resolving these issues becomes significantly more difficult, requiring major refactoring efforts.

By automatically identifying circular dependencies, Sonar helps developers maintain a clean and scalable architecture, improving the maintainability and long-term health of the codebase.
