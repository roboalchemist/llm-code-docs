# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/design-and-architecture/configuring-the-architecture-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/design-and-architecture/configuring-the-architecture-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/design-and-architecture/configuring-the-architecture-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/design-and-architecture/configuring-the-architecture-analysis.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/design-and-architecture/configuring-the-architecture-analysis.md

# Configuring the architecture analysis

{% hint style="warning" %}
The cycle detection and architecture as code are deprecated, pending removal in January 2026. They will be replaced by improved architecture capabilities. See the [Sonar newsroom](https://www.sonarsource.com/company/newsroom/) page for more information.
{% endhint %}

### The configuration file <a href="#the-configuration-file" id="the-configuration-file"></a>

#### How it models the architecture <a href="#how-it-models-the-architecture" id="how-it-models-the-architecture"></a>

The architecture analysis in Sonar is configured via a YAML or JSON file. It has two functions:

1. To declare the formal architecture of the codebase using *Groups* and *Perspectives*
2. To declare architectural *Constraints* that enforce the formal architecture

A Perspective is a structured view of your codebase, defining how parts of your code are organized into architectural elements, called Groups. Groups can be nested, forming a hierarchy that reflects your domain concepts. A project can have multiple Perspectives, each offering a different view of the architecture. For example, one Perspective might illustrate architectural layers, while another maps features to the relevant parts of the code. See "Groups and Perspectives" below for more information.

A Constraint is a rule your team defines and enforces through Sonar. Constraints are declared in the architecture file, and Sonar verifies them in CI/CD, raising issues when divergences occur.

There are two types of constraints:

* Group constraints - They are defined within a Perspective and apply to hierarchical groups.
* Top-Level constraints - They apply to the entire codebase and use raw code patterns like globs and wildcards

See the "Constraints" section below for more information.

#### Using a configuration file and format <a href="#using-a-configuration-file-and-format" id="using-a-configuration-file-and-format"></a>

The configuration file path can be specified via the`sonar.architecture.configpath` property. The following example runs the analysis in a maven project using the configuration file `myArchitecture.json` in the project root directory:

```css-79elbk
mvn clean verify sonar:sonar -Dsonar.architecture.configpath=./myArchitecture.json
```

It must be provided either in JSON or YAML format; `.json`, `.yaml` and `.yml` are valid file name extensions.

If no configuration file is being specified, the analyzer looks for a file `architecture.json`, `architecture.yaml` or `architecture.yml` in the project root directory by default. If you want no configuration file to be used at all, you can set the following property for the analysis:

```css-79elbk
mvn clean verify sonar:sonar -Dsonar.architecture.noconfig
```

Note that this does not disable the architecture analysis. It just makes features unavailable that need configuration, but features that don’t need configuration (e.g., cycle detection) will still work.

#### All configuration properties <a href="#all-configuration-properties" id="all-configuration-properties"></a>

This section lists all properties available in the architecture configuration file. Refer to the ongoing sections for more information and configuration examples.

**Configuration file:**

* `perspectives` (optional) – An array of `PERSPECTIVE`. These are the perspective declarations that describe the formal architecture of the codebase. See "Groups and Perspectives" below.
* `constraints` (optional) – An array of `TOP-LEVEL-CONSTRAINT`. These are the top-level constraints not tied to an individual perspective. See "Top-Level Constraints Declaration" below.

**PERSPECTIVE**

* `label` (required) – Unique identifier for the perspective, which can contain any character except `/`.
* `description` (optional) – Provides more information about the perspective in human-readable form.
* `groups` (optional) – An array of `GROUP`. A perspective can declare one or many groups. These are the structural elements that make up the perspective. While the property is optional, a perspective without groups would usually be useless.
* `constraints` (optional) – An array of `PERSPECTIVE-CONSTRAINT`. These are the constraints declared for this perspective. See "Perspective Constraints Declaration" below.

**GROUP**

* `label` (required) – Unique identifier for the group within its parent group or perspective. It can contain any character except `/`.
* `description` (optional) – Provides more information about the group in human-readable form.
* `patterns` (required) – Specifies the code elements that are contained in the group in the same way as patterns are used in Constraints. See the "Constraints" section below for more information.
* `groups` (optional) – An array of `GROUP`. A group can declare one or many subgroups, allowing for the nested declaration of groups.

**PERSPECTIVE-CONSTRAINT**

* `from` (required) – Patterns for the elements that use the `to` elements in this constraint. This is an array of strings, each one representing a group path. The pattern can contain globs or regular expressions. See "Perspective Constraints Declaration" and "Wildcards" below.
* `to` (required) – Patterns for the elements used by the `from` elements in this constraint. This is an array of strings, each one representing a file path pattern. The pattern can contain globs or regular expressions. See "Perspective Constraints Declaration" and "Wildcards" below.
* `message` (optional, or stand-alone) – Issue message specific for this constraint if used together with `from` and `to`, or global issue message if used stand-alone. See "Custom Issue Messages" below.
* `relation` (optional) – Indicates whether this is a constraint that allows or denies the access from `from` to `to` elements. Possible values are `deny` and `exclusive-allow`. The constraint type defaults to `deny` if this property is not specified. See "Constraint Types" below.

**TOP-LEVEL-CONSTRAINT**

* `from` (required) – Patterns for the elements that use the `to` elements in this constraint. This is an array of strings, each one representing a file path pattern. The pattern can contain globs or regular expressions. See "File path and name pattern" and "Wildcards" below.
* `to` (required) – Patterns for the elements used by the `from` elements in this constraint. This is an array of strings, each one representing a file path pattern. The pattern can contain globs or regular expressions. See "File path and name pattern" and "Wildcards" below.
* `message` (optional, or stand-alone) – Issue message specific for this constraint if used together with `from` and `to`, or global issue message if used stand-alone. See "Custom issue messages" below.
* `relation` (optional) – Indicates whether this is a constraint that allows or denies the access from `from` to `to` elements. Possible values are `deny` and `exclusive-allow`. The constraint type defaults to `deny` if this property is not specified. See "Constraint Types" below.

#### JSON schema <a href="#json-schema" id="json-schema"></a>

When working on an architecture configuration file in the IDE or text editor of your choice, we recommend using the following JSON Schema. It provides validation and autocompletion features, thereby reducing the risk of errors in your configuration.

{% file src="<https://756198905-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FaGXmdbBYwaT83rOiXBQW%2Fuploads%2FeObOoyPlLUK3BWAA6ZZg%2Fdesign-and-architecture-config-schema.json?alt=media&token=7fae9c2a-86c9-41a3-b125-cfb1cd315a06>" %}

### Groups and Perspectives <a href="#groups-and-perspectives" id="groups-and-perspectives"></a>

#### Declaration <a href="#declaration" id="declaration"></a>

The architecture configuration file can model the different views on the codebase using *Groups* and *Perspectives*. While a perspective represents a specific view, it consists of several groups that represent structural units within that perspective. Perspectives can overlap, include the entire codebase, or comprise just a subset of it. This means that an individual code element can be covered by one or many perspectives, or by no perspective at all.

Under the array property `perspectives`, you can specify one or many perspectives. A perspective has the following properties:

* `label` (required) – Unique identifier for the perspective, which can contain any character except `/`.
* `description` (optional) – Provides more information about the perspective in human-readable form.
* `groups` (optional) – A perspective can declare one or many groups. These are the structural elements that make up the perspective. While the property is optional, a perspective without groups would usually be useless.

Within the `groups` property of a perspective or group, you can specify one or many groups. A group has the following properties:

* `label` (required) – Unique identifier for the group within its parent group or perspective. It can contain any character except `/`.
* `description` (optional) – Provides more information about the group in human-readable form.
* `patterns` (required) – Specifies the code elements that are contained in the group in the same way as patterns are used in Constraints. See the "Constraints" section below for more information.
* `groups` (optional) – A group can declare one or many subgroups, allowing for the nested declaration of groups.

The following example models the architectural layers of a codebase:

```css-79elbk
{
  "perspectives": [
    {
      "label": "Layers",
      "description": "Application Layers",
      "groups": [
        {
          "label": "UI Layer",
          "patterns": ["src/*/com/example/ui/**"]
        },
        {
          "label": "Service Layer",
          "patterns": ["src/*/com/example/services/**"]
        },
        {
          "label": "Data Layer",
          "patterns": [
            "src/*/com/example/repos/**",
            "src/*/com/example/dtos/**"
          ]
        }
      ]
    }
  ]
}
```

#### Multiple perspectives <a href="#multiple-perspectives" id="multiple-perspectives"></a>

The following example adds a *Modules* perspective (which is an orthogonal view to the layers perspective) and a *Main/Test* perspective to the previous example. Each of the perspectives covers the entire codebase.

```css-79elbk
{
  "perspectives": [
    {
      "label": "Layers",
      "description": "Application Layers",
      "groups": [
        {
          "label": "UI Layer",
          "patterns": ["src/*/com/example/ui/**"]
        },
        {
          "label": "Service Layer",
          "patterns": ["src/*/com/example/services/**"]
        },
        {
          "label": "Data Layer",
          "patterns": [
            "src/*/com/example/repos/**",
            "src/*/com/example/dtos/**"
          ]
        }
      ]
    },
    {
      "label": "Modules",
      "description": "Application Functional Units",
      "groups": [
        {
          "label": "Customers",
          "patterns": ["src/*/com/example/*/customers/**"]
        },
        {
          "label": "Products",
          "patterns": ["src/*/com/example/*/products/**"]
        },
        {
          "label": "Events",
          "patterns": ["src/*/com/example/*/events/**"]
        }
      ]
    },
    {
      "label": "Main/Test",
      "description": "Main and Test Code",
      "groups": [
        {
          "label": "Main",
          "description": "Main Code",
          "patterns": ["src/main/**"]
        },
        {
          "label": "Test",
          "description": "Test Code",
          "patterns": ["src/test/**"]
        }
      ]
    }
  ]
```

### Nested groups <a href="#nested-groups" id="nested-groups"></a>

#### Declaration <a href="#declaration" id="declaration"></a>

Groups can declare subgroups, which have the same features as top-level groups. This allows for defining architectures with multiple structural levels, rather than just flat architectures. The following example declares a perspective that distinguishes between modules on the first level and main/test code on the second.

```css-79elbk
{
  "perspectives": [
    {
      "label": "Modules",
      "groups": [
        {
          "label": "Customers",
          "patterns": ["src/*/com/example/*/customers/**"],
          "groups": [
            {
              "label": "Main",
              "patterns": ["src/main/**"]
            },
            {
              "label": "Test",
              "patterns": ["src/test/**"]
            }
          ]
        },
        {
          "label": "Products",
          "patterns": ["src/*/com/example/*/products/**"],
          "groups": [
            {
              "label": "Main",
              "patterns": ["src/main/**"]
            },
            {
              "label": "Test",
              "patterns": ["src/test/**"]
            }
          ]
        },
        {
          "label": "Events",
          "patterns": ["src/*/com/example/*/events/**"],
          "groups": [
            {
              "label": "Main",
              "patterns": ["src/main/**"]
            },
            {
              "label": "Test",
              "patterns": ["src/test/**"]
            }
          ]
        }
      ]
    }
  ]
}
```

#### Label reuse <a href="#label-reuse" id="label-reuse"></a>

A group label must be unique within its parent group or perspective. Outside the enclosing declaration, it can be reused. This is demonstrated in the above example, where the labels `Main` and `Test` are being reused multiple times.

#### Patterns intersection <a href="#patterns-intersection" id="patterns-intersection"></a>

For an element to be covered by a subgroup, it must not only match the patterns of that group, but the patterns of its parent groups as well. Formally, the matcher algorithm traverses up the path from a subgroup through all its parent groups, and a code element is considered a path of the subgroup only if it matches all the patterns along that path.

This simplifies the usage of subgroup patterns, because you do not need to specify the intersection pattern explicitly. Take this excerpt from the above example:

```css-79elbk
{
  "perspectives": [
    {
      "label": "Modules",
      "groups": [
        {
          "label": "Customers",
          "patterns": ["src/*/com/example/*/customers/**"],
          ...
          "groups": [
            {
              "label": "Main",
              "patterns": ["src/main/**"]
            }
          ]
        }, 
        ...
      ]
    }
  ]
}
```

An element will only be part of the subgroup `Main` in group `Modules` if it is located under `src/main/com/example/customers/"`. However, we don’t need to be that specific. To declare the pattern `src/main/*`is sufficient to achieve the same effect. This is a trivial example, but note that patterns can become arbitrarily complex.

### Constraints <a href="#constraints" id="constraints"></a>

#### Top-Level Constraints Declaration <a href="#toplevel-constraints-declaration" id="toplevel-constraints-declaration"></a>

Top-level constraints define which files and folders are allowed or denied access to each other. A constraint is made up of two required properties `from` and `to` that declare from which file or name pattern to which file or name pattern the constraint is applied. By default, constraints are *deny constraints*, which means that elements matching the `from` pattern are not allowed to use elements matching the `to` pattern in any way, such as importing them, or using classes or members from them.

The example configuration file in JSON format below shows the declaration of a simple top-level constraint:

```css-79elbk
{
  "constraints": [
    {
      "from": ["com/example/ui/**"],
      "to": [
        "com/example/repos/**",
        "com/example/dtos/**"
      ]
    }
  ]
}
```

The YAML equivalent looks like this:

```css-79elbk
constraints:
  - from: 
      - "com/example/ui/**"
    to: 
      - "com/example/repos/**"
      - "com/example/dtos/**"
```

The declared constraint prevents any source code element located under the path:

```css-79elbk
com/example/ui
```

from using any source code element located under the paths:

```css-79elbk
com/example/repos
com/example/dtos
```

The following example declares two top-level constraints:

```css-79elbk
{
  "constraints": [
    {
      "from": ["com/example/ui/**"],
      "to": [
        "com/example/repos/**",
        "com/example/dtos/**"
      ]
    },
    {
      "from": ["com/example/services/**"],
      "to": ["com/example/dtos/**"]
    }
  ]
}
```

#### Perspective Constraints Declaration <a href="#perspective-constraints-declaration" id="perspective-constraints-declaration"></a>

Perspective constraints work like top-level constraints in all aspects, except for the patterns used in the `from` and `to` properties. Instead of locating source code elements by file path or fully qualified name (see the "File path and name pattern" section below for more information), perspective constraints use paths to groups or subgroups within the declared groups. For example, if a top-level group `Customer` contains a subgroup `UI`, which contains a subgroup `Test`, then `Customer/UI/Test` is the path to that subgroup.

Perspective constraints are applied between groups and subgroups, not individual files. Wildcards are still supported in perspective constraints, allowing for flexible pattern matching. For instance, the pattern `*/UI/Test` selects the subgroup `Test` in the subgroup `UI` contained in any top-level group.

The following example adds a constraint to the example from the "Declaration" section below that forbids access from main code to test code for the top level group `Customers`:

```css-79elbk
{
  "perspectives": [
    {
      ...
      "constraints": [
        {
          "from": ["Customers/Main"],
          "to": ["Customers/Test"]
        }
      ]
    }
  ]
}
```

The following example adds a constraint that forbids access from main code to test code for all top level groups:

```css-79elbk
{
  "perspectives": [
    {
      ...
      "constraints": [
        {
          "from": ["*/Main"],
          "to": ["*/Test"]
        }
      ]
    }
  ]
}
```

#### Constraint Types <a href="#constraint-types" id="constraint-types"></a>

The constraint type can be specified with the `relation` property. There are two types of constraints:

* `deny` - Access to the `to` elements by any of the `from` elements is denied.
* `exclusive-allow` - Access to the `to` elements is allowed only by the `from` elements, by the `to` elements themselves, and no others.

If not declared, the constraint type defaults to `deny`.

The following example states that elements in `com/example/dtos` can only be used by themselves and by elements in and `com/example/repos`.

```css-79elbk
{
  "constraints": [
    {
      "from": ["com/example/repos/**"],
      "to": ["com/example/dtos/**"],
      "relation": "exclusive-allow"
    }
  ]
}
```

#### Custom Issue Messages <a href="#custom-issue-messages" id="custom-issue-messages"></a>

By default, constraint violations are reported in a generic form:

*$from should not reference $to due to architectural constraints.*

Here, `$from` and `$to` represent the patterns of the constraint being violated.

To provide more context, architects can define custom issue messages. These messages help developers understand which constraint was violated and the rationale behind it, thereby enhancing their comprehension of the architecture and design principles of the codebase.

**Global issue messages**

Custom issue messages can be declared *globally*, applying to a group of constraints, or *locally* for a specific constraint. A global issue message is declared in place of a constraint, like in the following example:

```css-79elbk
{
  "constraints": [
    {
      "message": "Lower application layers should not depend on higher ones"
    }, {
      "from": ["com/example/dtos/**"],
      "to": ["com/example/repos/**"]
    }, {
      "from": ["com/example/repos/**"],
      "to": ["com/example/services/**"]
    }
  ]
}
```

This message applies to all subsequent constraints – unless overridden by a constraint-specific message – until the next message is declared. In the following example shows two different messages applied to subsequent constraints:

```css-79elbk
{
  "constraints": [
    {
      "message": "Lower application layers should not depend on higher ones"
    }, {
      "from": ["com/example/dtos/**"],
      "to": ["com/example/repos/**"]
    }, {
      "from": ["com/example/repos/**"],
      "to": ["com/example/services/**"]
    }, {
      "message": "These modules should not depend on each other"
    }, {
      "from": ["com/example/*/Customers"],
      "to": ["com/example/*/Products"]
    }, 
    ...
  ]
}
```

**Resetting the global message**

To reset the global issue message and revert to the default format:

*$from should not reference $to due to architectural constraints.*

Specify an empty message string. In this example, the custom message applies only to the first two constraints, while the ongoing constraints revert to the default message:

```css-79elbk
{
  "constraints": [
    {
      "message": "Lower application layers should not depend on higher ones"
    }, {
      "from": ["com/example/dtos/**"],
      "to": ["com/example/repos/**"]
    }, {
      "from": ["com/example/repos/**"],
      "to": ["com/example/services/**"]
    }, {
      "message": ""
    }, {
      "from": ["com/example/*/Customers"],
      "to": ["com/example/*/Products"]
    }, 
    ...
  ]
}
```

**Using "from" and "to" pattern in custom issue messages**

Custom issue messages can incorporate the `$from` and `$to` pattern, similar to the default message:

*$from should not reference $to due to architectural constraints.*

This allows for dynamic insertion of the constraints pattern being violated, as demonstrated in the following example:

```css-79elbk
{
  "constraints": [
    {
      "message": "$from module should not depend on $to module"
    }, {
      "from": ["com/example/*/Customers"],
      "to": ["com/example/*/Products"]
    }, 
    ...
  ]
}
```

**Constraint-specific issue messages**

Constraint-specific issue messages override global ones. They are declared as a property of the respective constraint, such as in the following example:

```css-79elbk
{
  "constraints": [
    {
      "message": "Lower application layers should not depend on higher ones"
    }, {
      "message": "DTOs must not depend on data repositories",
      "from": ["com/example/dtos/**"],
      "to": ["com/example/repos/**"]
    }, {
      "from": ["com/example/repos/**"],
      "to": ["com/example/services/**"]
    }
  ]
}
```

#### Exceptions from Constraints <a href="#exceptions-from-constraints" id="exceptions-from-constraints"></a>

If not regulated by a constraint, which means that there is no constraint whose `from` and `to` pattern matches the elements, then the access between two elements is allowed. If multiple constraints match, they are applied in the order in which they appear in the configuration file to determine the accessibility between elements. This allows to specify an exception for a deny-constraint or allow-constraint.

In the following example, elements from `com/example/ui` cannot access elements from `com/example/repos`, except if they are located in `com/example/ui/internal`.

```css-79elbk
{
  "constraints": [
    {
      "from": ["com/example/ui/**"],
      "to": ["com/example/repos/**"],
      "relation": "deny"
    },
    {
      "from": ["com/example/ui/internal/**"],
      "to": ["com/example/repos/**"],
      "relation": "exclusive-allow"
    }
  ]
}
```

#### File path and name pattern <a href="#file-path-and-name-pattern" id="file-path-and-name-pattern"></a>

Currently, constraints can only use file-path patterns. They provide a language-agnostic method to locate source code elements in the file system.

Future versions of the configuration schema will also support fully qualified name patterns. These are more natural to the developer of a language, but they are not language agnostic, as different languages have different concepts for their visibility scopes. For example, in Java, the scope of the package `foo.bar` is not a subscope of the package `foo`, whereas in C#, the namespace `foo.bar` is a subscope of `foo`.

Consider the following example of a constraints declaration for a Java project. This is an invalid example as the constraint patterns use fully qualified names, not file paths. The resulting constraint would never match.

```css-79elbk
{
  "constraints": [
    {
      "from": ["com.example.ui.*"],
      "to": ["com.example.repos.*"]
    }
  ]
}
```

#### Wildcards <a href="#wildcards" id="wildcards"></a>

Constraint patterns can contain wildcards. Both glob patterns and regular expressions are supported.

**Globs**

[Globs](https://en.wikipedia.org/wiki/Glob_\(programming\)) are less powerful than regular expressions but are sufficient for most scenarios and are easier to use. By default, all patterns in the architecture configuration file are globs, while regular expressions are identified by a special marker.

Glob patterns in the architecture configuration file support the following features:

* `?` - Any single character
* `*` - Any sequence of zero or more characters that does not cross path separator boundaries
* `**` - Any sequence of zero or more characters that can cross path separator boundaries
* `[abc]` - Any of the characters `a`, `b`, `c`
* `[^abc]` - Any character except `a`, `b`, `c`

The path separator depends on the path type. For file paths, the separator is `/`, meaning that `foo/*/baz` matches `foo/bar/baz` but not `foo/baz` or `foo/bar/bas/baz`. For Java namespace paths, the separator is `.`, although currently only file paths are supported (see "File path and name pattern" above).

The following example prevents any `.java` file that doesn’t start with letter `X`, located under any `ui` folder from using any element located under any `repos` folder:

```css-79elbk
{
  "constraints": [
    {
      "from": ["**/ui/**/[^X]*.java"],
      "to": ["**/repos/**"]
    }
  ]
}
```

**Regular Expressions**

Patterns that start with `^` and end with `$` are interpreted as regular expressions. They support all features of [Java Regular Expressions](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/regex/Pattern.html). The following example is equivalent to the above, but used regular expression patterns instead of globs:

```css-79elbk
{
  "constraints": [
    {
      "from": ["^.*/ui/.*/[^X][^/]*.java$"],
      "to": ["^.*/repos/.*$"]
    }
  ]
}
```

### Disabling the architecture analysis

To disable architecture analysis, set the `-Dsonar.architecture.enable` property to `false` .
