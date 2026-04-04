# Source: https://docs.datadoghq.com/security/code_security/static_analysis/custom_rules/tutorial.md

---
title: Static Code Analysis Custom Rule Creation Tutorial
description: Learn how to define a custom rule within Datadog.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > Static
  Code Analysis (SAST) Custom Rules > Static Code Analysis Custom Rule Creation
  Tutorial
---

# Static Code Analysis Custom Rule Creation Tutorial

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

This tutorial shows how to write a custom rule to check code. The tutorial uses a very simple rule that checks if we have a Python function call to a function `foo` with an argument called `bar`.

Here is the sample code we want to detect:

```python
foo(bar)
```

## Step 1: Create a ruleset{% #step-1-create-a-ruleset %}

Navigate to [custom rulesets](https://app.datadoghq.com/ci/code-analysis/static-analysis/custom-rulesets) and create a new ruleset named `tutorial`.

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/custom_rule_tutorial_ruleset.8b1e7c43f2dd44c523aaf0000bc1d176.png?auto=format"
   alt="Ruleset created" /%}

## Step 2: Create a rule{% #step-2-create-a-rule %}

Create a rule named `tutorial-rule`. Ensure you select the `Python` language.

### Step 2.1: Test the rule with an example{% #step-21-test-the-rule-with-an-example %}

Add a code example to test the rule. At each modification or update of the rule (tree-sitter capture or test code), Datadog will execute the rule against the code and provide feedback.

Enter the filename `test.py` and add the code below.

```python
foo(bar)
foo(baz)
```

### Step 2.2: Write a tree-sitter query{% #step-22-write-a-tree-sitter-query %}

Write a [tree-sitter query](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/index.html) that defines the nodes to capture in the code. In the current example, the goal is to capture a function call where the function name is `foo` and any argument is `bar`.

The tree-sitter query is shown below. It has three captures:

- `funcName` captures the name of the function and runs a predicate to check its name.
- `arg` captures the name of the arguments.
- `func` captures the function call with all arguments. This is used to report the violation in code.

```
(call
    function: (identifier) @funcName
    arguments: (argument_list
        (identifier) @arg
    )
    (#eq? @funcName "foo")
    (#eq? @arg "bar")
)@func
```

### Step 2.3: Write JavaScript rule code{% #step-23-write-javascript-rule-code %}

Write the JavaScript code to report the violation. The code first fetch the captures (`func` and `funcName`), and then checks if the name of the function is different from `foo` and returns if true. Lastly, it reports a violation.

Note that the `buildError` function 6th and 7th arguments are the severity and category. We support the following severity: `ERROR`, `WARNING`, `NOTICE` and `INFO`. We support the following categories: `BEST_PRACTICES`, `CODE_STYLE`, `ERROR_PRONE`, `PERFORMANCE` and `SECURITY`.

```javascript
function visit(query, filename, code) {
  // Get the func captures so that we can know the line/col where to put a violation
  const func = query.captures["func"];

  // Get the funcname to later get the name of the function
  const funcNameNode = query.captures["funcName"];

  // Check if the name of the function is not foo. This is already done in the tree-sitter query
  // and here only to show how to use getCodeForNode
  const funcNameFromCode = getCodeForNode(funcNameNode, code);
  if (funcNameFromCode !== "foo") {
    return;
  }

  // Report a violation
  addError(
    buildError(
      func.start.line, func.start.col,
      func.end.line, func.end.col,
      "do not use bar as argument",
      "WARNING",
      "BEST_PRACTICES"
    )
  )
}
```

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/custom_rule_tutorial_rule_created.10fa7df782da203eb3279f2301672af9.png?auto=format"
   alt="Rule created" /%}

## Step 3: Use the rule{% #step-3-use-the-rule %}

To use the rule, do one of the following:

- Create a `static-analysis.datadog.yaml` file at the root of your repository with the ruleset.
- Add the rule in [your settings](https://app.datadoghq.com/security/configuration/code-security/settings), either for the org-wide or repo-level configuration.

A valid configuration for using this ruleset (and no other ruleset) look like this:

```yaml
rulesets:
  - tutorial
```

{% image
   source="https://datadog-docs.imgix.net/images/security/code_security/custom_rule_tutorial_configuration.1747d431edb06cce229314ec508587a1.png?auto=format"
   alt="Configuration with Custom Rule" /%}
