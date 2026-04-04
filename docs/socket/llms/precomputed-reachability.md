# Source: https://docs.socket.dev/docs/precomputed-reachability.md

# Precomputed Reachability

Precomputed reachability enhances dependency reachability by filtering out CVEs that affect functions never called within transitive dependencies.

> 📘 See [Reachability Analysis](https://docs.socket.dev/docs/reachability-analysis) for an overview of all Reachability Analysis capabilities in Socket. This page is about just one of the reachability techniques that Socket offers.

Dependency reachability filters out vulnerabilities in modules that are not loaded, typically resulting in about a 35% reduction in alerts.
However, the fact that a module is loaded doesn’t guarantee that all of its functions or methods are actually used.

Precomputed reachability builds on this by answering the question, *“What functions are actually called in your dependencies?”* Since most functions in a typical application are unused, **Precomputed reachability enables Socket to flag around 60% of vulnerabilities in transitive dependencies as irrelevant**.

The benefits of precomputed reachability include:

* **Good noise reduction** – It offers better noise reduction than dependency reachability by analyzing usage at the function level.
* **High performance** – Results for most dependency chains are precomputed and cached by Socket, making the analysis extremely fast.
* **Manifest-based** – It works solely from your manifest files (e.g., `package.json`, `go.mod`, etc.).
* **No source code access required** – It does not require access to your application’s source code.
* **Zero setup** – It’s available immediately to all Socket users with no additional configuration.

## Example of an Unreachable Vulnerability

Let’s walk through a typical example. The vulnerability [CVE-2024-37890](https://github.com/advisories/GHSA-3h5v-q93c-6h6q) affects the npm package [*ws*](https://socket.dev/npm/package/ws), which is used to create WebSocket clients and servers. It’s a serious issue—an attacker can crash a ws server just by sending a request with many headers. If you’re using the `WebSocketServer` from ws directly, you should patch this vulnerability as soon as possible.

But many developers don’t depend on *ws* directly. Instead, they inherit it as an indirect/transitive dependency through other packages in the npm ecosystem. Even if you never import *ws* yourself, you’ll still get an alert about this CVE if some package in your dependency tree pulls it in. These indirect usages might still be vulnerable—but in many cases, reachability analysis can prove they’re not.

Consider the package *jsdom*, which depends on *ws* (See *jsdom's*[ package.json](https://socket.dev/npm/package/jsdom/files/20.0.3/package.json#L47)). Its usage of *ws* is not vulnerable since it only uses the client-side functionality of *ws*. Specifically, it calls `WebSocket` at [this location](https://socket.dev/npm/package/jsdom/files/20.0.3/lib/jsdom/living/websockets/WebSocket-impl.js#L129), without ever touching `WebSocketServer`. So if *ws* is used in your project through *jsdom*, CVE-2024-37890 isn’t something you need to worry about.

A static reachability analysis can check that *jsdom* doesn’t use the vulnerable part of *ws*, and this information can be stored in a database. So, when an SCA tool detects CVE-2024-37890 in your SBOM or dependency tree, it can safely mark it as unreachable—if *jsdom* is the only package that depends on *ws*. If more packages depends on *ws*, then reachability information must be computed for these packages as well.

## How Precomputed Reachability Works

### 1. From Manifest to Dependency Graph

The analysis begins similarly to dependency reachability, starting with your manifest files (`package.json`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`, and others).
From these files, a complete list of direct and transitive dependencies — along with the dependency graph that connects them — is extracted.

### 2. Scanning for CVEs

Socket scans for CVEs in the dependency graph using a [standard vulnerability scan](https://docs.socket.dev/docs/vulnerability).

### 3. Computing Vulnerability Reachability

For every detected CVE, Socket identifies all the paths in the dependency graph that lead to the affected package. For each of these paths, a static analysis is performed to check the reachability of the affected function (You can learn more about Socket's static reachability analysis [here](static-reachability-analysis)). If reachability has already been computed for a specific path, the result is reused.

### 4. Reachable vs Unreachable CVEs

If the affected function(s) are unreachable through all paths in the dependency graph, the CVE is marked as unreachable. Unreachable CVEs are safe to ignore, as the vulnerable code cannot be invoked at runtime.

If the CVE is reachable through one or more paths, the vulnerability is flagged as *maybe reachable*.
For maybe reachable CVEs, Socket shows the list of function calls in your dependencies that may trigger the vulnerability.

The term *maybe reachable* is used instead of *definitely reachable* because, even if a vulnerable function is reachable from a direct dependency, it doesn’t necessarily mean that the relevant parts of that dependency are used by your application’s own source code.

## Limitations

### Phantom Dependencies

Precomputed reachability operates under the assumption that your application only loads its declared direct dependencies. This means that if your code loads a [phantom dependency](phantom-dependencies)—a package not listed in your manifest file—vulnerabilities in that package may be incorrectly classified as unreachable.

We consider this limitation minor, as phantom dependencies are both a poor practice and relatively uncommon in most projects. However, if you’re concerned about vulnerability reachability in phantom dependencies, we recommend using the [Full Application Reachability mode](full-application-reachability). This mode can both detect phantom dependencies and accurately assess the reachability of vulnerabilities within them.

### Direct Dependency Vulnerabilities

The precomputed reachability analysis only works on vulnerabilities in transitive/indirect dependencies. This means the analysis works best when most vulnerabilities are in the transitive dependencies. You need to use the [Full Application Reachability analysis](full-application-reachability) on applications with a low fraction of transitive dependencies.

### Private Package Dependencies

If your project uses private package dependencies, you may experience a drop in quality of results. This limitation is especially prevalent if your project does not use lock files.

Consider a Go project with the following dependency structure:

* Package `A` (public, direct dependency) → depends on `B`
* Package `P` (private, direct dependency) → depends on `B`
* Package `B` (public, transitive dependency) has a vulnerability

Socket's SBOM resolver can correctly identify all three packages (`A`, `B`, and `P`) in your project. However, it cannot determine that `P` depends on `B` because analyzing `P` requires access to the private package. Socket may conclude that the vulnerability in `B` is unreachable from `A`, but this analysis doesn't account for the fact that the vulnerability in `B` may actually be reachable through the private package `P`.

### General Static Analysis Limitations

See the [Static Reachability Analysis](static-reachability-analysis#limitations)  for more information about what the static reachability analysis can and cannot detect.

## FAQ

### How does Socket determine which functions are affected by a CVE?

You can learn more about how the Socket team identifies functions affected by vulnerabilities in the FAQ section of the [Static Reachability Analysis](static-reachability-analysis#faq) page.

### How does *Precomputed Reachability* compare to *Full Application Reachability*

Precomputed reachability analysis considers only the code within your dependencies, whereas [full application reachability](full-application-reachability) also scans your application’s own source code. While full application analysis provides better noise reduction and richer context for triaging reachable vulnerabilities, it comes with some trade-offs: it requires manual setup and is generally slower, as the static analysis is compute-intensive.