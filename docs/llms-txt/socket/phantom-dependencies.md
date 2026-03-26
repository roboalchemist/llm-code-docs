# Source: https://docs.socket.dev/docs/phantom-dependencies.md

# Phantom Dependencies

Phantom dependencies are dependencies that are used in your code but are not explicitly declared in your manifest file (e.g., package.json, go.mod, etc.).

A phantom dependency is a dependency that is used in your code but not properly declared in a manifest file.

For example, consider a scenario where you specify a dependency on [Axios](https://socket.dev/npm/package/axios/overview/) in your `package.json`.

```json
{
  "dependencies": {
    "axios": "^1.7.2"
  }
}
```

The Axios package internally depends on [follow-redirects](https://socket.dev/npm/package/follow-redirects/overview) ([see Axios' package.json](https://socket.dev/npm/package/axios/files/1.9.0/package.json#L150)).

Even though follow-redirects is a dependency of Axios and not explicitly declared in your package.json, it is still possible to load it in your code. For example:

```javascript
const followRedirects = require('follow-redirects');
console.log(followRedirects);
```

This behavior is possible because the npm package manager installs follow-redirects into the `node_modules` folder when Axios is installed. The `require` function does not check your package.json; it simply loads any module present in `node_modules`, regardless of whether it’s explicitly declared.

Using phantom dependencies is generally considered an anti-pattern, as it can lead to bugs and unpredictable behavior. For example, if Axios is updated to a version that no longer depends on follow-redirects, your code will break if it relied on follow-redirects being available.

This issue isn’t unique to JavaScript—most programming languages and package managers suffer from design quirks that allow phantom dependencies to be used in code.

## Phantom Dependencies and Reachability Analysis

Since phantom dependencies are relatively common, reachability analyses should be designed to scan for vulnerable functions in them. Socket's reachability analysis does exactly that—it scans all dependencies, regardless of how they are declared. If a reachable vulnerability is found in a phantom dependency, the UI clearly labels it as such.

Vulnerabilities in phantom dependencies are no more or less severe than those in explicitly declared dependencies—they pose the same risk if reachable from your application.