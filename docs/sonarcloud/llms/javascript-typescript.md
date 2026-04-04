# Source: https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/languages/javascript-typescript.md

# JavaScript/TypeScript

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

In order to analyze JavaScript or TypeScript code, you need to have supported version of Node.js installed on the machine running the scan. Supported versions are current LTS versions (v10, v12, v14) and latest version v15. Odd (non LTS) versions might work, but are not actively tested. We recommend using the latest available LTS version (v14 as of today) for optimal stability and performance.

If standard `node` is not available, you have to set property `sonar.nodejs.executable` to an absolute path to Node.js executable.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

Discover and update the JavaScript / TypeScript [analysis-parameters](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/analysis-parameters "mention") in: **Administration > General Settings > JavaScript / TypeScript**.

### Supported frameworks, versions and languages <a href="#supported" id="supported"></a>

* ECMAScript 5 / ECMAScript 2015 (ECMAScript 6) / ECMAScript 2016-2017-2018
* TypeScript 4
* React JSX
* Vue.js
* Flow

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

#### Slow or unresponsive analysis <a href="#slow-or-unresponsive-analysis" id="slow-or-unresponsive-analysis"></a>

On a big project, more memory may need to be allocated to analyze the project. This would be manifested by analysis getting stuck and the following stacktrace might appear in the logs

```css-79elbk
ERROR: Failed to get response while analyzing [file].ts
java.io.InterruptedIOException: timeout
```

You can use `sonar.javascript.node.maxspace` property to allow the analysis to use more memory. Set this property to `4096` or `8192` for big projects. This property should be set in `sonar-project.properties` file or on command line for scanner (with `-Dsonar.javascript.node.maxspace=4096`).

#### Default exclusions <a href="#default-exclusions" id="default-exclusions"></a>

By default, analysis will exclude files from dependencies in usual directories, such as `node_modules`, `bower_components`, `dist`, `vendor`, and `external`. It will also ignore `.d.ts` files. If for some reason analysis of files in these directories is desired, it can be configured by setting `sonar.javascript.exclusions` property to empty value, i.e. `sonar.javascript.exclusions=""`, or to comma separated list of paths to be excluded. This property will exclude the files also for other languages, similar to `sonar.exclusions` property, however `sonar.exclusions` property should be preferred to configure general exclusions for the project.

#### Custom rules <a href="#custom-rules" id="custom-rules"></a>

{% hint style="warning" %}
This feature is deprecated
{% endhint %}

As a replacement, we suggest you to have a look at [ESLint](https://eslint.org/docs/developer-guide/), it provides custom rules that you can then import thanks to the [importing-third-party-issues](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/importing-external-issues/importing-third-party-issues "mention") feature.

#### TypeScript files are not analyzed <a href="#typescript-files-are-not-analyzed" id="typescript-files-are-not-analyzed"></a>

Using a TypeScript version that is higher than the one supported by SonarQube can cause false positives or issues with parsing, and some options (such as the `useUnknownInCatchVariables` compiler option) might not get recognized, causing TypeScript files to be ignored by the analysis.

We recommend checking that the version of TypeScript used is supported by SonarQube, and upgrading to a higher SonarQube version if needed.

#### Overview <a href="#overview" id="overview"></a>

The JavaScript Analyzer parses the source code, creates an Abstract Syntax Tree (AST) and then walks through the entire tree. A coding rule is a visitor that is able to visit nodes from this AST.

As soon as the coding rule visits a node, it can navigate the tree around the node and log issues if necessary.

#### Create SonarQube Plugin <a href="#create-sonarqube-plugin" id="create-sonarqube-plugin"></a>

Custom rules for JavaScript can be added by writing a SonarQube Plugin and using JavaScript analyzer APIs.

To get started a sample plugin can be found here: [javascript-custom-rules](https://github.com/SonarSource/sonar-custom-rules-examples/tree/master/javascript-custom-rules). Here are the step to follow:

* Create a standard SonarQube plugin project
* Attach this plugin to the SonarQube JavaScript analyzer through the `pom.xml`:
  * Add the dependency to the JavaScript analyzer.
  * Add the following line in the sonar-packaging-maven-plugin configuration. `<basePlugin>javascript</basePlugin>`
* Implement the following extension points:
  * [Plugin](http://javadocs.sonarsource.org/latest/apidocs/index.html?org/sonar/api/Plugin.html)
  * [RulesDefinition](http://javadocs.sonarsource.org/latest/apidocs/index.html?org/sonar/api/server/rule/RulesDefinition.html)
  * `CustomRuleRepository`, this interface registers rule classes with JavaScript plugin, so they are invoked during analysis of JavaScript files.
* Declare `RulesDefinition` as an extension in the `Plugin` extension point.

You can implement both `RulesDefinition` and `CustomRulesRepository` in a single class.

#### Implement a Rule <a href="#implement-a-rule" id="implement-a-rule"></a>

* Create a class that will hold the implementation of the rule. It should:
  * Extend `DoubleDispatchVisitorCheck` or `SubscriptionVisitorCheck`
  * Define the rule name, key, tags, etc. with Java annotations.
* Declare this class in the `RulesDefinition`.

#### Implementation Details <a href="#implementation-details" id="implementation-details"></a>

**Using DoubleDispatchVisitorCheck**

`DoubleDispatchVisitorCheck` extends `DoubleDispatchVisitor` which provide a set of methods to visit specific tree nodes (these methods’ names start with `visit`). To explore a part of the AST, override the required method(s). For example, if you want to explore `if` statement nodes, override the `DoubleDispatchVisitor#visitIfStatement` method that will be called each time an `IfStatementTree` node is encountered in the AST.

When overriding a visit method, you must call the `super` method in order to allow the visitor to visit the rest of the tree.

**Using SubscriptionVisitorCheck**

`SubscriptionVisitorCheck` extends `SubscriptionVisitor`. To explore a part of the AST, override `SubscribtionVisitor#nodesToVisit()` by returning the list of the `Tree#Kind` of node you want to visit. For example, if you want to explore `if` statement nodes the method will return a list containing the element `Tree#Kind#IF_STATEMENT`.

**Create issues**

Use these methods to log an issue:

* `JavaScriptCheck#addIssue(tree, message)` creates and returns an instance of `PreciseIssue`. In the SonarQube UI this issue will highlight all code corresponding to the tree passed as the first parameter. To add cost (effort to fix) or secondary locations provide these values to your just-created instance of `PreciseIssue`.
* `JavaScriptCheck#addIssue(issue)` creates and returns the instance of `Issue`. Use this method to create non-standard issues (e.g. for a file-level issue instantiate `FileIssue`).

**Check context**

Check context is provided by `DoubleDispatchVisitorCheck` or `SubscriptionVisitorCheck` by calling the `JavaScriptCheck#getContext` method. Check context provides you access to the root tree of the file, the file itself and the symbol model (information about variables).

**Test rule**

To test the rule you can use `JavaScriptCheckVerifier#verify()` or `JavaScriptCheckVerifier#issues()`. To be able to use these methods add a dependency to your project:

```css-79elbk
<dependency>
  <groupId>org.sonarsource.javascript</groupId>
  <artifactId>javascript-checks-testkit</artifactId>
  <version>XXX</version>
  <scope>test</scope>
</dependency>
```

#### API Changes <a href="#api-changes" id="api-changes"></a>

**SonarJS 6.0**

* Feature and API are deprecated.

**SonarJS 4.2.1**

* `CustomJavaScriptRulesDefinition` is deprecated. Implement extension `RulesDefinition` and `CustomRuleRepository` instead.

**SonarJS 4.0**

* Method `TreeVisitorContext#getFile()` is removed.

### Related Pages <a href="#related-pages" id="related-pages"></a>

* [importing-third-party-issues](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/importing-external-issues/importing-third-party-issues "mention") (ESLint, TSLint)
* [test-coverage-and-execution](https://docs.sonarsource.com/sonarqube-server/8.9/analyzing-source-code/test-coverage-and-execution "mention") (LCOV format)
* [SonarJS plugin for ESLint](https://github.com/SonarSource/eslint-plugin-sonarjs)
* [adding-coding-rules](https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/adding-coding-rules "mention")

### Issue tracker <a href="#issue-tracker" id="issue-tracker"></a>

Check the [issue tracker](https://github.com/SonarSource/sonar-javascript/issues) for this language.
