# Reporters & Preprocessors

Source: https://knip.dev/features/reporters

## Built-in Reporters

Knip provides the following built-in reporters:

- codeowners
- compact
- disclosure
- github-actions
- json
- markdown
- codeclimate
- symbols(default)

Example usage:

```typescript
knip--reportercompact
```

### JSON

The built-injsonreporter output is meant to be consumed by other tools. It
reports in JSON format with unusedfilesandissuesas an array with one
object per file structured like this:

```typescript
{"files":["src/unused.ts"],"issues":[{"file":"package.json","owners":["@org/admin"],"dependencies":[{"name":"jquery","line":5,"col":6,"pos":71}],"devDependencies":[{"name":"lodash","line":9,"col":6,"pos":99}],"unlisted":[{"name":"react"},{"name":"@org/unresolved"}],"exports":[],"types":[],"duplicates":[]},{"file":"src/Registration.tsx","owners":["@org/owner"],"dependencies":[],"devDependencies":[],"binaries":[],"unresolved":[{"name":"./unresolved","line":8,"col":23,"pos":407}],"exports":[{"name":"unusedExport","line":1,"col":14,"pos":13}],"types":[{"name":"unusedEnum","line":3,"col":13,"pos":71},{"name":"unusedType","line":8,"col":14,"pos":145}],"enumMembers":{"MyEnum":[{"name":"unusedMember","line":13,"col":3,"pos":167},{"name":"unusedKey","line":15,"col":3,"pos":205}]},"classMembers":{"MyClass":[{"name":"unusedMember","line":40,"col":3,"pos":687},{"name":"unusedSetter","line":61,"col":14,"pos":1071}]},"duplicates":["Registration","default"]}]}
```

The keys match thereported issue types. Example usage:

```typescript
knip--reporterjson
```

### Github Actions

Example usage:

```typescript
knip--reportergithub-actions
```

### Markdown

The built-inmarkdownreporter output is meant to be saved to a Markdown file.
This allows following the changes in issues over time. It reports issues in
Markdown tables separated by issue types as headings, for example:

```typescript
# Knip report## Unused files (1)- src/unused.ts## Unlisted dependencies (2)| Name            | Location          | Severity ||:--------------|:----------------|:-------|| unresolved      | src/index.ts:8:23 | error    || @org/unresolved | src/index.ts:9:23 | error    |## Unresolved imports (1)| Name         | Location           | Severity ||:-----------|:-----------------|:-------|| ./unresolved | src/index.ts:10:12 | error    |
```

### Disclosure

This reporter is useful for sharing large reports. Groups of issues are rendered
in a closed state initially. The reporter renders this:

```typescript
$ knip --reporter disclosure<details><summary>Unused files (2)</summary>```unused.tsdangling.js```</details><details><summary>Unused dependencies (2)</summary>```unused-dep     package.jsonmy-package     package.json```</details>
```

The above can be copy-pasted where HTML and Markdown is supported, such as a
GitHub issue or pull request, and renders like so:

```typescript
unused.tsdangling.js
```

```typescript
unused-dep     package.jsonmy-package     package.json
```

### CodeClimate

The built-incodeclimatereporter generates output in the Code Climate Report
JSON format. Example usage:

```typescript
$ knip --reporter codeclimate[{"type": "issue","check_name": "Unused exports","description": "isUnused","categories": ["Bug Risk"],"location": {"path": "path/to/file.ts","positions": {"begin": {"line": 6,"column": 1}}}"severity": "major","fingerprint": "e9789995c1fe9f7d75eed6a0c0f89e84",}]
```

## Custom Reporters

When the provided built-in reporters are not sufficient, a custom local reporter
can be implemented or an external reporter can be used. Multiple reporters can
be used at once by repeating the--reporterargument.

The results are passed to the function from its default export and can be used
to write issues tostdout, a JSON or CSV file, or sent to a service. It
supports a local JavaScript or TypeScript file or an external dependency.

### Local

The default export of the reporter should be a function with this interface:

```typescript
typeReporter=async(options:ReporterOptions):void;typeReporterOptions={report:Report;issues:Issues;counters:Counters;configurationHints:ConfigurationHints;isDisableConfigHints:boolean;isTreatConfigHintsAsErrors:boolean;cwd:string;isProduction:boolean;isShowProgress:boolean;options:string;};
```

The data can then be used to write issues tostdout, a JSON or CSV file, or
sent to a service.

Here’s a most minimal reporter example:

```typescript
importtype{ Reporter }from'knip';constreporter:Reporter=function(options) {console.log(options.issues);console.log(options.counters);};exportdefaultreporter;
```

Example usage:

```typescript
knip--reporter./my-reporter.ts
```

### External

Pass--reporter [pkg-name]to use an external reporter. The default exported
function of themainscript (default:index.js) will be invoked with theReporterOptions, just like a local reporter.

## Preprocessors

A preprocessor is a function that runs after the analysis is finished. It
receives the results from the analysis and should return data in the same
shape/structure (unless you pass it to only your own reporter).

The data goes through the preprocessors before the final data is passed to the
reporters. There are no built-in preprocessors. Just like reporters, use e.g.--preprocessor ./my-preprocessorfrom the command line (can be repeated).

The default export of the preprocessor should be a function with this interface:

```typescript
typePreprocessor=async(options:ReporterOptions)=>ReporterOptions;
```

Like reporters, you can use local JavaScript or TypeScript files and external
npm packages as preprocessors.

Example preprocessor:

```typescript
importtype{ Preprocessor }from'knip';constpreprocess:Preprocessor=function(options) {// modify options.issues and options.countersreturnoptions;};exportdefaultpreprocess;
```

Example usage:

```typescript
knip--preprocessor./preprocess.ts
```

ISC License© 2024Lars Kappert

