# Source: https://docs.sonarsource.com/sonarqube-community-build/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/javascript-typescript-css.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/javascript-typescript-css.md

# JavaScript/TypeScript/CSS

### Supported versions <a href="#supported-versions" id="supported-versions"></a>

The level of support for a language is defined as follows:

* Fully supported: Analysis will complete. All the language features are understood and examined.
* Supported: Most language features are understood and examined but the version includes unsupported features. Analysis might break or provide incomplete results.

#### ECMAScript <a href="#ecmascript" id="ecmascript"></a>

All versions up to ECMAScript 2024 are supported.

#### TypeScript <a href="#typescript" id="typescript"></a>

All versions up to 5.9.3 are supported.

#### CSS <a href="#css" id="css"></a>

CSS 3 is supported.

### Supported frameworks and tools <a href="#supported-frameworks-and-tools" id="supported-frameworks-and-tools"></a>

#### Tools <a href="#tools" id="tools"></a>

React JSX, Angular, Vue.js, Node.js, Express, Flow.

#### Test Frameworks <a href="#test-frameworks" id="test-frameworks"></a>

Mocha, Chai.

#### CSS extensions <a href="#css-extensions" id="css-extensions"></a>

SASS, LESS, SCSS, Less, ‘style’ inside PHP, HTML, and VueJS files.

### Requirements and recommendations <a href="#requirements" id="requirements"></a>

This section describes requirements or recommendations regarding the machine running the scanner that are specific to the analysis of JavaScript/TypeScript/CSS. For general requirements, see [general-requirements](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/scanner-environment/general-requirements "mention").

#### Memory <a href="#memory" id="memory"></a>

A minimum of 4GB memory is recommended.

To allow the analysis to use more memory, see **Slow or unresponsive analysis** in the **Troubleshooting** section below.

#### Node.js <a href="#nodejs" id="nodejs"></a>

The scanner performs the analysis using the Node.js runtime environment. If your architecture is Linux x64, Windows x64, or Apple ARM64, no Node.js installation is required because the Sonar JS analyzer embeds its own Node.JS.

If you want to use your own Node.js, SonarQube requires one of these Node.js Major.Minor versions:

* for Node v20, it must be at least 20.12.0.
* for Node v22 the [Active LTS](https://nodejs.org/en/about/previous-releases#release-schedule), it must be at least 22.11.0, with acceptance of v23 and v24.

The scanner will look for and retrieve a locally installed Node.js runtime according to the following options in order:

1. The Node.js defined through the parameter `sonar.nodejs.executable` (absolute path to your Node.js). The runtime version must be compatible.
2. The Node.js downloaded by the scanner from the SonarQube Server during analysis if the detected architecture is one of the supported ones: Linux x64, Windows x64, and Apple ARM64.
3. The Node.js defined with `node` in the `PATH`. The runtime version must be compatible.

**Notes for option 1 and 3:**

If your architecture is neither Linux x64, Windows x64, nor Apple ARM64, you must set up option 1 or 3 ( see the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page to set up option 1). The same minimum version requirements listed above still apply.

**Notes for option 2:**

When relying on the [Node.js](http://node.js) downloaded by the scanner as described in option 2, the scanner temporarily deploys the Node.js runtime installed on the host machine. It considers the following possible deployment locations in order:

1. As defined by the scanner property `sonar.userHome`.
2. As defined by the environment variable `SONAR_USER_HOME`.
3. If no Node.js is defined in location 1 or 2, it the SonarScanner creates a `.sonar` directory in the user’s home directory for deployment.

If none of these options are suitable for your environment, you can choose to skip the deployment of the embedded Node.js runtime altogether by using either:

* The scanner property `sonar.scanner.skipNodeProvisioning` set to `true`, or
* The scanner property `sonar.nodejs.executable` set to a Node.js runtime path.

The deployment may fail due to insufficient permissions on the location directory. If this occurs, the scanner property or environment variable must refer to a folder with adequate permissions.

#### File encoding <a href="#file-encoding" id="file-encoding"></a>

During analysis, the scanner defaults to the host file encoding. However, analyzing JavaScript and TypeScript source files requires always using the UTF-8 file encoding. If this is not the case, set the scanner property `sonar.sourceEncoding` to `UTF-8`.

#### TypeScript configuration <a href="#typescript-configuration" id="typescript-configuration"></a>

The scanner analyzes JavaScript and TypeScript using the TypeScript compiler. It leverages TypeScript’s semantic model and features like type-checking to improve analysis accuracy. The scanner will use a TypeScript configuration (`tsconfig.json`) if it is already present in your project or transparently create one in the background if it is not available.

When the analysis starts, the scanner follows these strategies to resolve all the TSConfig files of the project:

1. It considers only TSConfig files based on the scanner property `sonar.typescript.tsconfigPaths`.
   1. The property expects a comma-separated list of TSConfig path patterns.
2. If not specified, it traverses the filesystem from the project root to collect all the existing TSConfig files.
   1. This operation is time-consuming and can impact the analysis. If that’s the case, and as a workaround, users can explicitly define which TSConfig files the scanner should use.
3. If none are found, it creates a single temporary TSConfig file.

Either way, the TypeScript compiler will resolve all the files that belong to a TSConfig file. However, the scanner will only analyze the files specified through the scanner property `sonar.sources`. Therefore, the value of this property needs to be consistent with your TypeScript configuration.

#### Other <a href="#other" id="other"></a>

If you have a community plugin for CSS analysis installed on your SonarQube Cloud instance it will conflict with analysis of CSS, so it should be removed.

### ESLint <a href="#eslint" id="eslint"></a>

Along with dedicated rules, Sonar includes a selection of rules from ESLint and some of its plugins.

If there are rules that you use that we do not support yet, you can import them thanks to the External Issues feature using the ESLint format for exporting issues.

To facilitate the integration of your ESLint setup with our analysis, if you import issues for rules that we already raised in our analysis, issues won’t be duplicated.

Sonar takes into account ESLint’s issue-silencing comments that you might have in your code, so you won’t have to do additional work.

See the [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") page for more details on importing rules.

### Language-specific properties <a href="#language-specific-properties" id="language-specific-properties"></a>

To discover and update the JavaScript / TypeScript-specific properties, navigate in SonarQube Cloud to *Your Project* > **Administration** > **General Settings** > **Languages** > **JavaScript / TypeScript**.

Discover and update the CSS-specific properties in: **Project Administration** > **General Settings** > **Languages** > **CSS**.

See the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page for more information about specific properties for any of these languages.

### Supported frameworks and versions <a href="#supported-frameworks-and-versions" id="supported-frameworks-and-versions"></a>

* ECMAScript 3, 5, 2015, 2016, 2017, 2018, 2019, 2020, 2021 and 2022
* TypeScript 5.0
* React JSX, Vue.js, Angular
* Flow
* CSS, SCSS, Less, also ‘style’ inside PHP, HTML and VueJS files

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

#### Slow or unresponsive analysis <a href="#slow-or-unresponsive-analysis" id="slow-or-unresponsive-analysis"></a>

On a big project, more memory may need to be allocated to analyze the project. This would be manifested by analysis getting stuck and the following stacktrace might appear in the logs

`ERROR: Failed to get response while analyzing [file].ts`\
`java.io.InterruptedIOException: timeout`

You can use `sonar.javascript.node.maxspace` property to allow the analysis to use more memory. Set this property to `4096` or `8192` for big projects. This property should be set in `sonar-project.properties` file or on command line for scanner (with `-Dsonar.javascript.node.maxspace=4096`).

#### File encoding errors <a href="#file-encoding-errors" id="file-encoding-errors"></a>

If you encounter file encoding errors, use `sonar.sourceEncoding=UTF-8` configuration. To know how to perform this configuration, check out what's on the [analysis-parameters](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters "mention") page.

#### Default exclusions for JS/TS <a href="#default-exclusions-for-jsts" id="default-exclusions-for-jsts"></a>

By default, analysis excludes files from dependencies in common directories, such as `node_modules`, `bower_components`, `dist`, `vendor`, and `external`. It also ignores `.d.ts` files. Use the following parameters to manage exclusions:

* `sonar.javascript.exclusions` - exclude JavaScript files by assigning comma-separated paths, or assign an empty value to include analysis in all directories, for example: `sonar.javascript.exclusions=""`.
* `sonar.exclusions` - exclude all files from the analysis. This method is preferred when configuring general exclusions for the project.
* `sonar.javascript.maxFileSize` - use this parameter to change the maximum file size limit on the scanner. By default, the analysis will exclude all files that are larger than 1000 KB. You can also change the limit in SonarQube Server UI under **Project Settings** > **General Settings** > **Languages** > **JavaScript / TypeScript** at project level or **Administration** > **Configuration** > **General Settings** > **Languages** > **JavaScript / TypeScript** at global level.

#### Detection of code bundles <a href="#detection-of-code-bundles" id="detection-of-code-bundles"></a>

The analyzer will attempt to detect bundled code or generated code. This means code that was automatically transformed and optimized with tools such as Webpack and similar. We consider generated code out of scope of the analysis since developers are not able to act upon the findings in such code. Whenever generated code is detected, the analysis will print a log message: once per the whole project on `INFO` level, and for each file on the `DEBUG` level. If you want to opt-in for analyzing the generated code or in case the detection is incorrect, you can disable it by setting `sonar.javascript.detectBundles=false`.

#### Custom rules for JS/TS <a href="#custom-rules-for-jsts" id="custom-rules-for-jsts"></a>

Custom rules are not supported by the analyzer. As an alternative we suggest you to have a look at [ESLint](https://eslint.org/docs/developer-guide/), it provides custom rules that you can then import thanks to the [External Issues](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports) feature.

#### Running out of memory <a href="#running-out-of-memory" id="running-out-of-memory"></a>

While analyzing a large project or file, the scanner may run out of memory. If this occurs, you will be notified with the following analysis logs:

```log
The analysis will stop due to the Node.js process running out of memory
You can see how Node.js heap usage evolves during analysis with "sonar.javascript.node.debugMemory=true"
Try setting "sonar.javascript.node.maxspace" to a higher value to increase Node.js heap size limit
If the problem persists, please report the issue at https://community.sonarsource.com
```

Consider the property `setting sonar.javascript.node.maxspace` to a higher value depending on the host’s available memory.

#### Large projects and monorepos <a href="#large-projects-and-monorepos" id="large-projects-and-monorepos"></a>

When analyzing a large project, you may encounter memory issues, such as with monorepo projects. In these cases, a possible workaround is to divide the analysis into subfolders. Given this project structure:

```json
my-app/
├─ app1/
│  ├─ tsconfig.sonar.json
├─ app2/
│  ├─ tsconfig.sonar.json
├─ ...
├─ tsconfig.json
```

The default analysis will use the root `tsconfig.json` which may include too many files if the project is very big and creates memory issues. Splitting the project into several TSConfig files should help in that case. To do so, create intermediate `tsconfig.sonar.json` for each of the subfolders and use:

```json
sonar.typescript.tsconfigPaths=my-app/app1/tsconfig.sonar.json,my-app/app2/tsconfig.sonar.json
```

#### Unavailable dependencies <a href="#unavailable-dependencies" id="unavailable-dependencies"></a>

In certain situations, analysis may be conducted in environments where dependencies are not available, such as with Autoscan. If possible, it is recommended to install these dependencies (e.g. `npm ci`) to enhance TypeScript type inference precision. If a `tsconfig.json` file extends external TSConfigs and cannot locate them, unexpected analysis results may occur due to potential differences in `compilerOptions`. In these cases, it’s advised to directly copy the essential contents of the extended TSConfigs into a custom `tsconfig.sonar.json` file and use it for analysis.

#### Unsupported compiler options <a href="#unsupported-compiler-options" id="unsupported-compiler-options"></a>

The scanner includes a recent version of the TypeScript compiler. Sometimes, a project might use new TSConfig options that are not supported by the embedded scanner version. We suggest holding off on using these options until the scanner is updated to the new version. If that’s not possible, you can create a custom `tsconfig.sonar.json` for the analysis without using those options.

### Related Pages <a href="#related-pages" id="related-pages"></a>

* The [external-analyzer-reports](https://docs.sonarsource.com/sonarqube-cloud/enriching/external-analyzer-reports "mention") page has information about importing external issues such as ESLint, TSLint, and/or StyleLint.
* Test coverage [overview](https://docs.sonarsource.com/sonarqube-cloud/enriching/test-coverage/overview "mention") (LCOV format)
* [SonarJS Plugin for ESLint](https://www.npmjs.com/package/eslint-plugin-sonarjs)
