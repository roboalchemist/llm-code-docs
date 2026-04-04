# Yq Documentation

Source: https://mikefarah.gitbook.io/llms-full.txt

---

# yq

a lightweight and portable command-line YAML, JSON, INI and XML processor. `yq` uses [jq](https://github.com/stedolan/jq) like syntax but works with yaml files as well as json, xml, ini, properties, csv and tsv. It doesn't yet support everything `jq` does - but it does support the most common operations and functions, and more is being added continuously.

yq is written in go - so you can download a dependency free binary for your platform and you are good to go! If you prefer there are a variety of package managers that can be used as well as Docker and Podman, all listed below.

## Quick Usage Guide

Read a value:

```bash
yq '.a.b[0].c' file.yaml
```

Pipe from STDIN:

```bash
yq '.a.b[0].c' < file.yaml
```

Update a yaml file, in place

```bash
yq -i '.a.b[0].c = "cool"' file.yaml
```

Update using environment variables

```bash
NAME=mike yq -i '.a.b[0].c = strenv(NAME)' file.yaml
```

Merge multiple files

```bash
# merge two files
yq -n 'load("file1.yaml") * load("file2.yaml")'

# merge using globs:
# note the use of `ea` to evaluate all the files at once
# instead of in sequence
yq ea '. as $item ireduce ({}; . * $item )' path/to/*.yml
```

Multiple updates to a yaml file

```bash
yq -i '
  .a.b[0].c = "cool" |
  .x.y.z = "foobar" |
  .person.name = strenv(NAME)
' file.yaml
```

Find and update an item in an array:

```bash
yq '(.[] | select(.name == "foo") | .address) = "12 cat st"'
```

Convert JSON to YAML

```bash
yq -Poy sample.json
```

See [recipes](https://mikefarah.gitbook.io/yq/recipes) for more examples and the [documentation](https://mikefarah.gitbook.io/yq/) for more information.

Take a look at the discussions for [common questions](https://github.com/mikefarah/yq/discussions/categories/q-a), and [cool ideas](https://github.com/mikefarah/yq/discussions/categories/show-and-tell)

## Install

See the [github page](https://github.com/mikefarah/yq/#install) for the various ways you can install and use `yq`

## Known Issues / Missing Features

* `yq` attempts to preserve comment positions and whitespace as much as possible, but it does not handle all scenarios (see <https://github.com/go-yaml/yaml/tree/v3> for details)
* Powershell has its own...[opinions on quoting yq](https://mikefarah.gitbook.io/yq/usage/tips-and-tricks#quotes-in-windows-powershell)

See [tips and tricks](https://mikefarah.gitbook.io/yq/usage/tips-and-tricks) for more common problems and solutions.


# How It Works

In `yq`, expressions are made up of operators and pipes. A context of nodes is passed through the expression, and each operation takes the context as input and returns a new context as output. That output is piped in as input for the next operation in the expression.

Let's break down the process step by step using a diagram. We'll start with a single YAML document, apply an expression, and observe how the context changes at each step.

Given a document like:

```yaml
root:
  items:
    - name: apple
      type: fruit
    - name: carrot
      type: vegetable
    - name: banana
      type: fruit
```

You can use dot notation to access nested structures. For example, to access the `name` of the first item, you would use the expression `.root.items[0].name`, which would return `apple`.

But lets see how we could find all the fruit under `items`

## Step 1: Initial Context

The context starts at the root of the YAML document. In this case, the entire document is the initial context.

```
root
└── items
    ├── name: apple
    │   type: fruit
    ├── name: carrot
    │   type: vegetable
    └── name: banana
        type: fruit
```

## Step 2: Splatting the Array

Using the expression `.root.items[]`, we "splat" the items array. This means each element of the array becomes its own node in the context:

```
Node 1: { name: apple, type: fruit }
Node 2: { name: carrot, type: vegetable }
Node 3: { name: banana, type: fruit }
```

## Step 3: Filtering the Nodes

Next, we apply a filter to select only the nodes where type is fruit. The expression `.root.items[] | select(.type == "fruit")` filters the nodes:

```
Filtered Node 1: { name: apple, type: fruit }
Filtered Node 2: { name: banana, type: fruit }
```

## Step 4: Extracting a Field

Finally, we extract the name field from the filtered nodes using `.root.items[] | select(.type == "fruit") | .name` This results in:

```
apple
banana
```

## Simple assignment example

Given a document like:

```yaml
a: cat
b: dog
```

with an expression:

```
.a = .b
```

Like math expressions - operator precedence is important.

The `=` operator takes two arguments, a `lhs` expression, which in this case is `.a` and `rhs` expression which is `.b`.

It pipes the current, lets call it 'root' context through the `lhs` expression of `.a` to return the node

```yaml
cat
```

Side note: this node holds not only its value 'cat', but comments and metadata too, including path and parent information.

The `=` operator then pipes the 'root' context through the `rhs` expression of `.b` to return the node

```yaml
dog
```

Both sides have now been evaluated, so now the operator copies across the value from the RHS (`.b`) to the LHS (`.a`), and it returns the now updated context:

```yaml
a: dog
b: dog
```

## Complex assignment, operator precedence rules

Just like math expressions - `yq` expressions have an order of precedence. The pipe `|` operator has a low order of precedence, so operators with higher precedence will get evaluated first.

Most of the time, this is intuitively what you'd want, for instance `.a = "cat" | .b = "dog"` is effectively: `(.a = "cat") | (.b = "dog")`.

However, this is not always the case, particularly if you have a complex LHS or RHS expression, for instance if you want to select particular nodes to update.

Lets say you had:

```yaml
- name: bob
  fruit: apple
- name: sally
  fruit: orange

```

Lets say you wanted to update the `sally` entry to have fruit: 'mango'. The *incorrect* way to do that is: `.[] | select(.name == "sally") | .fruit = "mango"`.

Because `|` has a low operator precedence, this will be evaluated (*incorrectly*) as : `(.[]) | (select(.name == "sally")) | (.fruit = "mango")`. What you'll see is only the updated segment returned:

```yaml
name: sally
fruit: mango
```

**Important**: To properly update this YAML, you must wrap the entire LHS in parentheses. Think of it like using brackets in math to ensure the correct order of operations. `(.[] | select(.name == "sally") | .fruit) = "mango"`

Now that entire LHS expression is passed to the 'assign' (`=`) operator, and the yaml is correctly updated and returned:

```yaml
- name: bob
  fruit: apple
- name: sally
  fruit: mango

```

## Relative update (e.g. `|=`)

There is another form of the `=` operator which we call the relative form. It's very similar to `=` but with one key difference when evaluating the RHS expression.

In the plain form, we pass in the 'root' level context to the RHS expression. In relative form, we pass in *each result of the LHS* to the RHS expression. Let's go through an example.

Given a document like:

```yaml
a: 1
b: thing
```

with an expression:

```
.a |= . + 1
```

Similar to the `=` operator, `|=` takes two operands, the LHS and RHS.

It pipes the current context (the whole document) through the LHS expression of `.a` to get the node value:

```
1
```

Now it pipes *that LHS context* into the RHS expression `. + 1` (whereas in the `=` plain form it piped the original document context into the RHS) to yield:

```
2
```

The assignment operator then copies across the value from the RHS to the value on the LHS, and it returns the now updated 'root' context:

```yaml
a: 2
b: thing
```


# Recipes

These examples are intended to show how you can use multiple operators together so you get an idea of how you can perform complex data manipulation.

Please see the details [operator docs](https://mikefarah.gitbook.io/yq/operators) for details on each individual operator.

## Find items in an array

We have an array and we want to find the elements with a particular name.

Given a sample.yml file of:

```yaml
- name: Foo
  numBuckets: 0
- name: Bar
  numBuckets: 0
```

then

```bash
yq '.[] | select(.name == "Foo")' sample.yml
```

will output

```yaml
name: Foo
numBuckets: 0
```

### Explanation:

* `.[]` splats the array, and puts all the items in the context.
* These items are then piped (`|`) into `select(.name == "Foo")` which will select all the nodes that have a name property set to 'Foo'.
* See the [select](https://mikefarah.gitbook.io/yq/operators/select) operator for more information.

## Find and update items in an array

We have an array and we want to *update* the elements with a particular name.

Given a sample.yml file of:

```yaml
- name: Foo
  numBuckets: 0
- name: Bar
  numBuckets: 0
```

then

```bash
yq '(.[] | select(.name == "Foo") | .numBuckets) |= . + 1' sample.yml
```

will output

```yaml
- name: Foo
  numBuckets: 1
- name: Bar
  numBuckets: 0
```

### Explanation:

* Following from the example above`.[]` splats the array, selects filters the items.
* We then pipe (`|`) that into `.numBuckets`, which will select that field from all the matching items
* Splat, select and the field are all in brackets, that whole expression is passed to the `|=` operator as the left hand side expression, with `. + 1` as the right hand side expression.
* `|=` is the operator that updates fields relative to their own value, which is referenced as dot (`.`).
* The expression `. + 1` increments the numBuckets counter.
* See the [assign](https://mikefarah.gitbook.io/yq/operators/assign-update) and [add](https://mikefarah.gitbook.io/yq/operators/add) operators for more information.

## Deeply prune a tree

Say we are only interested in child1 and child2, and want to filter everything else out.

Given a sample.yml file of:

```yaml
parentA:
  - bob
parentB:
  child1: i am child1
  child3: hiya
parentC:
  childX: cool
  child2: me child2
```

then

```bash
yq '(
  .. | # recurse through all the nodes
  select(has("child1") or has("child2")) | # match parents that have either child1 or child2
  (.child1, .child2) | # select those children
  select(.) # filter out nulls
) as $i ireduce({};  # using that set of nodes, create a new result map
  setpath($i | path; $i) # and put in each node, using its original path
)' sample.yml
```

will output

```yaml
parentB:
  child1: i am child1
parentC:
  child2: me child2
```

### Explanation:

* Find all the matching child1 and child2 nodes
* Using ireduce, create a new map using just those nodes
* Set each node into the new map using its original path

## Multiple or complex updates to items in an array

We have an array and we want to *update* the elements with a particular name in reference to its type.

Given a sample.yml file of:

```yaml
myArray:
  - name: Foo
    type: cat
  - name: Bar
    type: dog
```

then

```bash
yq 'with(.myArray[]; .name = .name + " - " + .type)' sample.yml
```

will output

```yaml
myArray:
  - name: Foo - cat
    type: cat
  - name: Bar - dog
    type: dog
```

### Explanation:

* The with operator will effectively loop through each given item in the first given expression, and run the second expression against it.
* `.myArray[]` splats the array in `myArray`. So `with` will run against each item in that array
* `.name = .name + " - " + .type` this expression is run against every item, updating the name to be a concatenation of the original name as well as the type.
* See the [with](https://mikefarah.gitbook.io/yq/operators/with) operator for more information and examples.

## Sort an array by a field

Given a sample.yml file of:

```yaml
myArray:
  - name: Foo
    numBuckets: 1
  - name: Bar
    numBuckets: 0
```

then

```bash
yq '.myArray |= sort_by(.numBuckets)' sample.yml
```

will output

```yaml
myArray:
  - name: Bar
    numBuckets: 0
  - name: Foo
    numBuckets: 1
```

### Explanation:

* We want to resort `.myArray`.
* `sort_by` works by piping an array into it, and it pipes out a sorted array.
* So, we use `|=` to update `.myArray`. This is the same as doing `.myArray = (.myArray | sort_by(.numBuckets))`

## Filter, flatten, sort and unique

Lets find the unique set of names from the document.

Given a sample.yml file of:

```yaml
- type: foo
  names:
    - Fred
    - Catherine
- type: bar
  names:
    - Zelda
- type: foo
  names: Fred
- type: foo
  names: Ava
```

then

```bash
yq '[.[] | select(.type == "foo") | .names] | flatten | sort | unique' sample.yml
```

will output

```yaml
- Ava
- Catherine
- Fred
```

### Explanation:

* `.[] | select(.type == "foo") | .names` will select the array elements of type "foo"
* Splat `.[]` will unwrap the array and match all the items. We need to do this so we can work on the child items, for instance, filter items out using the `select` operator.
* But we still want the final results back into an array. So after we're doing working on the children, we wrap everything back into an array using square brackets around the expression. `[.[] | select(.type == "foo") | .names]`
* Now have have an array of all the 'names' values. Which includes arrays of strings as well as strings on their own.
* Pipe `|` this array through `flatten`. This will flatten nested arrays. So now we have a flat list of all the name value strings
* Next we pipe `|` that through `sort` and then `unique` to get a sorted, unique list of the names!
* See the [flatten](https://mikefarah.gitbook.io/yq/operators/flatten), [sort](https://mikefarah.gitbook.io/yq/operators/sort) and [unique](https://mikefarah.gitbook.io/yq/operators/unique) for more information and examples.

## Export as environment variables (script), or any custom format

Given a yaml document, lets output a script that will configure environment variables with that data. This same approach can be used for exporting into custom formats.

Given a sample.yml file of:

```yaml
var0: string0
var1: string1
fruit:
  - apple
  - banana
  - peach
```

then

```bash
yq '.[] |(
	( select(kind == "scalar") | key + "='\''" + . + "'\''"),
	( select(kind == "seq") | key + "=(" + (map("'\''" + . + "'\''") | join(",")) + ")")
)' sample.yml
```

will output

```yaml
var0='string0'
var1='string1'
fruit=('apple','banana','peach')
```

### Explanation:

* `.[]` matches all top level elements
* We need a string expression for each of the different types that will produce the bash syntax, we'll use the union operator, to join them together
* Scalars, we just need the key and quoted value: `( select(kind == "scalar") | key + "='" + . + "'")`
* Sequences (or arrays) are trickier, we need to quote each value and `join` them with `,`: `map("'" + . + "'") | join(",")`

## Custom format with nested data

Like the previous example, but lets handle nested data structures. In this custom example, we're going to join the property paths with \_. The important thing to keep in mind is that our expression is not recursive (despite the data structure being so). Instead we match *all* elements on the tree and operate on them.

Given a sample.yml file of:

```yaml
simple: string0
simpleArray:
  - apple
  - banana
  - peach
deep:
  property: value
  array:
    - cat
```

then

```bash
yq '.. |(
	( select(kind == "scalar" and parent | kind != "seq") | (path | join("_")) + "='\''" + . + "'\''"),
	( select(kind == "seq") | (path | join("_")) + "=(" + (map("'\''" + . + "'\''") | join(",")) + ")")
)' sample.yml
```

will output

```yaml
simple='string0'
deep_property='value'
simpleArray=('apple','banana','peach')
deep_array=('cat')
```

### Explanation:

* You'll need to understand how the previous example works to understand this extension.
* `..` matches *all* elements, instead of `.[]` from the previous example that just matches top level elements.
* Like before, we need a string expression for each of the different types that will produce the bash syntax, we'll use the union operator, to join them together
* This time, however, our expression matches every node in the data structure.
* We only want to print scalars that are not in arrays (because we handle the separately), so well add `and parent | kind != "seq"` to the select operator expression for scalars
* We don't just want the key any more, we want the full path. So instead of `key` we have `path | join("_")`
* The expression for sequences follows the same logic


# Upgrading from V3

Version 4 of `yq` is quite different from previous versions (and I apologise for that) - however it will be very familiar if you have used `jq` before as it now uses a similar syntax. Most commands that you could do in `v3` are longer in `v4` as a result of having a more expressive syntax language.

Note that `v4` by default now:

* prints all documents of a yaml file.
* prints in color (when outputting to a terminal).
* document separators are printed out by default

## How to do v3 things in v4:

In `v3` yq had seperate commands for reading/writing/deleting and more. In `v4` all these have been embedded into a single expression you specify to either the `eval` command (which runs the expression against each yaml document for each file given in sequence) or the `eval-all` command, which reads all documents of all files, and runs the given expression once.

Many flags from `v3` have been put into the expression language, for instance `stripComments` allowing you to specify which nodes to strip comments from instead of only being able to apply the flag to the entire document.

Lets have a look at the commands for the most common tasks:

### Navigating

v3:

```
yq r sample.yaml 'a.b.c'
```

v4:

```
yq '.a.b.c' sample.yaml
```

### Reading with default value

v3:

```
yq r sample.yaml --defaultValue frog path.not.there
```

v4: (use the [alternative](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md) operator)

```
yq '.path.not.there // "frog"' sample.yaml
```

### Finding nodes

v3:

```bash
yq r sample.yaml 'a.(b.d==cat).f'
```

v4:

```bash
yq '.a | select(.b.d == "cat") | .f' sample.yaml
```

### Recursively match nodes

v3:

```
yq r sample.yaml 'thing.**.name'
```

v4:

```
yq '.thing | .. | select(has("name"))' sample.yaml
```

### Multiple documents

v3:

```bash
yq r -d1 sample.yaml 'b.c'
```

v4 (via the document index operator):

```bash
yq 'select(documentIndex == 1) | .b.c' sample.yml
```

### Updating / writing documents

v3:

```
yq w sample.yaml 'a.b.c' fred
```

v4:

```
yq '.a.b.c = "fred"' sample.yaml
```

### Deleting documents

v3:

```bash
yq d sample.yaml 'a.b.c'
```

v4:

```bash
yq 'del(.a.b.c)' sample.yaml
```

### Merging documents

Like `jq`, merge is done via the multiply operator. In yq, the merge operator can take extra options to modify how it works.

For `v3` compatability, use the `n` option to only merge in new fields.

```bash
yq '. *n load("file2.yaml")' file1.yaml
```

See the [multiply documentation](https://mikefarah.gitbook.io/yq/operators/multiply-merge) for more example and options.

### Prefix yaml

Use the [Create / Collect Into Object ](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md)operator to create a new object with the desired prefix.

v3:

```
yq p data1.yaml c.d
```

v4:

```
yq '{"c": {"d": . }}' data1.yml
```

### Create new yaml documents

Note that in v4 you can no longer run expressions against an empty file to populate it - because the file is empty, there are no matches for `yq` to run through the expression pipeline - for what it's worth, this is what `jq` does as well. Instead use the `--null-input/-n` flag and pipe out the results to the file you want directly (see example below).

v3:

```
yq n b.c cat
```

v4:

```
yq -n '.b.c = "cat"'
```

### Validate documents

v3:

```
yq validate some.file
```

v4:

```
yq 'true' some.file > /dev/null
```

Note that passing 'true' as the expression saves having to reencode the yaml (only to pipe it to stdout). In v4 you can also do a slightly more sophisticated validation and assert the tag on the root level, so you can ensure the yaml file is a map or array at the top level:

```
yq --exit-status 'tag == "!!map" or tag== "!!seq"' some.file > /dev/null
```

### Comparing yaml files

v3:

```
yq compare --prettyPrint file1.yml file2.yml 
```

v4:

In v4 there is no built in compare command, instead it relies on using diff. The downside is longer syntax, the upside is that you can use the full power of diff.

```
diff <(yq -P file1.yml) <(yq -P file2.yml)
```

### Script files

v3 had a script feature that let you run an array of commands specified in a file in one go. The format for this looked like

```yaml
- command: update 
  path: a.key1
  value: things
- command: delete
  path: a.ab.key2
```

V4 doesn't have a similar feature, however the fact that you can run multiple operations in a single expression makes it easier to come up with a shell script that does the same thing:

```bash
#!/bin/bash

yq '
  .a.key1 = "things" |
  del(.a.ab.key2)
' ./examples/data1.yaml
```

### Some new things you can do in v4:

Construct dynamic yaml [maps ](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md)and [arrays ](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md)based on input yaml

Using the [union ](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md)operator, you can run multiple updates in one go and read multiple paths in one go

Fine grain merging of maps using the [multiply](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md) operator

Read and and control yaml metadata better (e.g. [tags](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md), [paths](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md), [document indexes](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md), [anchors and aliases](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md), [comments](https://github.com/mikefarah/yq/blob/gitbook/broken-reference/README.md)).

Work with multiple files (not just for merge)

The underlying expression language is much more powerful than `v3` so expect to see more features soon!

###


# Evaluate

Evaluates the given expression against each yaml document in each file, in sequence

Note that (as of 4.18.1) this is the default command when none is supplied to yq.

## Usage:

```bash
yq eval [expression] [yaml_file1]... [flags]
```

Aliases: `eval, e`

Note that you can pass in `-` as a filename to pipe from STDIN.

## Examples:

```bash
# runs the expression against each file, in series
yq '.a.b | length' f1.yml f2.yml 

# '-' will pipe from STDIN
cat file.yml | yq '.a.b' f1.yml -  f2.yml

# prints out the file
yq sample.yaml 
cat sample.yml | yq e

# prints a new yaml document
yq -n '.a.b.c = "cat"' 

# updates file.yaml directly
yq '.a.b = "cool"' -i file.yaml 
```

## Flags:

```
  -h, --help          help for eval
  -C, --colors        force print with colors
  -e, --exit-status   set exit status if there are no matches or null or false is returned
  -I, --indent int    sets indent level for output (default 2)
  -i, --inplace       update the yaml file inplace of first yaml file given.
  -M, --no-colors     force print with no colors
  -N, --no-doc        Don't print document separators (---)
  -n, --null-input    Don't read input, simply evaluate the expression given. Useful for creating yaml docs from scratch.
  -j, --tojson        output as json. Set indent to 0 to print json in one line.
  -v, --verbose       verbose mode
```


# Evaluate All

Read all documents of all given yaml files into memory, then run the given expression once against the lot.

Evaluate All is most useful when needing to run expressions that depend on multiple yaml documents or files. Merge is probably the most common reason why evaluate all would be used. Note that `eval-all` consumes more memory than `evaluate`.

Like `evaluate` you can use `-` to pipe from STDIN.

## Usage

```bash
yq eval-all [expression] [yaml_file1]... [flags]
```

Aliases: `eval-all, ea`

## Examples

```bash
# merges f2.yml into f1.yml (inplace)
yq eval-all --inplace 'select(fileIndex == 0) * select(fileIndex == 1)' f1.yml f2.yml

# you can merge into a file, piping from STDIN
cat somefile.yml | yq eval-all --inplace 'select(fileIndex == 0) * select(fileIndex == 1)' f1.yml -
```

## Flags

```bash
  -h, --help          help for eval-all
  -C, --colors        force print with colors
  -e, --exit-status   set exit status if there are no matches or null or false is returned
  -I, --indent int    sets indent level for output (default 2)
  -i, --inplace       update the yaml file inplace of first yaml file given.
  -M, --no-colors     force print with no colors
  -N, --no-doc        Don't print document separators (---)
  -n, --null-input    Don't read input, simply evaluate the expression given. Useful for creating yaml docs from scratch.
  -j, --tojson        output as json. Set indent to 0 to print json in one line.
  -v, --verbose       verbose mode
```


# Shell Completion

Generate a shell completion file for supported shells (bash/fish/zsh/powershell)

```bash
yq shell-completion zsh
```

Prints to StdOut a shell completion script for zsh shell.

### Bash (default)

```bash
source <(yq shell-completion bash)
```

#### To load completions for each session, execute once:

Linux:

```bash
yq shell-completion bash > /etc/bash_completion.d/yq 
```

MacOS:

```bash
yq shell-completion bash > /usr/local/etc/bash_completion.d/yq
```

### zsh

If shell completion is not already enabled in your environment you will need to enable it. You can execute the following once:

```bash
echo "autoload -U compinit; compinit" >> ~/.zshrc
```

#### To load completions for each session, execute once:

```bash
yq shell-completion zsh > "${fpath[1]}/_yq"
```

You will need to start a new shell for this setup to take effect.

### fish

```bash
yq shell-completion fish | source
```

#### To load completions for each session, execute once:

```
yq shell-completion fish > ~/.config/fish/completions/yq.fish
```

### PowerShell

```bash
yq shell-completion powershell
```

Users need PowerShell version 5.0 or above, which comes with Windows 10 and can be downloaded separately for Windows 7 or 8.1. They can then write the completions to a file and source this file from their PowerShell profile, which is referenced by the $Profile environment variable.


# Operators


# Add

Add behaves differently according to the type of the LHS:

* arrays: concatenate
* number scalars: arithmetic addition
* string scalars: concatenate
* maps: shallow merge (use the multiply operator (`*`) to deeply merge)

Use `+=` as a relative append assign for things like increment. Note that `.a += .x` is equivalent to running `.a = .a + .x`.

## Concatenate arrays

Given a sample.yml file of:

```yaml
a:
  - 1
  - 2
b:
  - 3
  - 4
```

then

```bash
yq '.a + .b' sample.yml
```

will output

```yaml
- 1
- 2
- 3
- 4
```

## Concatenate to existing array

Note that the styling of `a` is kept.

Given a sample.yml file of:

```yaml
a: [1,2]
b:
  - 3
  - 4
```

then

```bash
yq '.a += .b' sample.yml
```

will output

```yaml
a: [1, 2, 3, 4]
b:
  - 3
  - 4
```

## Concatenate null to array

Given a sample.yml file of:

```yaml
a:
  - 1
  - 2
```

then

```bash
yq '.a + null' sample.yml
```

will output

```yaml
- 1
- 2
```

## Append to existing array

Note that the styling is copied from existing array elements

Given a sample.yml file of:

```yaml
a: ['dog']
```

then

```bash
yq '.a += "cat"' sample.yml
```

will output

```yaml
a: ['dog', 'cat']
```

## Prepend to existing array

Given a sample.yml file of:

```yaml
a:
  - dog
```

then

```bash
yq '.a = ["cat"] + .a' sample.yml
```

will output

```yaml
a:
  - cat
  - dog
```

## Add new object to array

Given a sample.yml file of:

```yaml
a:
  - dog: woof
```

then

```bash
yq '.a + {"cat": "meow"}' sample.yml
```

will output

```yaml
- dog: woof
- cat: meow
```

## Relative append

Given a sample.yml file of:

```yaml
a:
  a1:
    b:
      - cat
  a2:
    b:
      - dog
  a3: {}
```

then

```bash
yq '.a[].b += ["mouse"]' sample.yml
```

will output

```yaml
a:
  a1:
    b:
      - cat
      - mouse
  a2:
    b:
      - dog
      - mouse
  a3:
    b:
      - mouse
```

## String concatenation

Given a sample.yml file of:

```yaml
a: cat
b: meow
```

then

```bash
yq '.a += .b' sample.yml
```

will output

```yaml
a: catmeow
b: meow
```

## Number addition - float

If the lhs or rhs are floats then the expression will be calculated with floats.

Given a sample.yml file of:

```yaml
a: 3
b: 4.9
```

then

```bash
yq '.a = .a + .b' sample.yml
```

will output

```yaml
a: 7.9
b: 4.9
```

## Number addition - int

If both the lhs and rhs are ints then the expression will be calculated with ints.

Given a sample.yml file of:

```yaml
a: 3
b: 4
```

then

```bash
yq '.a = .a + .b' sample.yml
```

will output

```yaml
a: 7
b: 4
```

## Increment numbers

Given a sample.yml file of:

```yaml
a: 3
b: 5
```

then

```bash
yq '.[] += 1' sample.yml
```

will output

```yaml
a: 4
b: 6
```

## Date addition

You can add durations to dates. Assumes RFC3339 date time format, see [date-time operators](https://mikefarah.gitbook.io/yq/operators/date-time-operators) for more information.

Given a sample.yml file of:

```yaml
a: 2021-01-01T00:00:00Z
```

then

```bash
yq '.a += "3h10m"' sample.yml
```

will output

```yaml
a: 2021-01-01T03:10:00Z
```

## Date addition - custom format

You can add durations to dates. See [date-time operators](https://mikefarah.gitbook.io/yq/operators/date-time-operators) for more information.

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

then

```bash
yq 'with_dtf("Monday, 02-Jan-06 at 3:04PM MST", .a += "3h1m")' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 6:00AM GMT
```

## Add to null

Adding to null simply returns the rhs

Running

```bash
yq --null-input 'null + "cat"'
```

will output

```yaml
cat
```

## Add maps to shallow merge

Adding objects together shallow merges them. Use `*` to deeply merge.

Given a sample.yml file of:

```yaml
a:
  thing:
    name: Astuff
    value: x
  a1: cool
b:
  thing:
    name: Bstuff
    legs: 3
  b1: neat
```

then

```bash
yq '.a += .b' sample.yml
```

will output

```yaml
a:
  thing:
    name: Bstuff
    legs: 3
  a1: cool
  b1: neat
b:
  thing:
    name: Bstuff
    legs: 3
  b1: neat
```

## Custom types: that are really strings

When custom tags are encountered, yq will try to decode the underlying type.

Given a sample.yml file of:

```yaml
a: !horse cat
b: !goat _meow
```

then

```bash
yq '.a += .b' sample.yml
```

will output

```yaml
a: !horse cat_meow
b: !goat _meow
```

## Custom types: that are really numbers

When custom tags are encountered, yq will try to decode the underlying type.

Given a sample.yml file of:

```yaml
a: !horse 1.2
b: !goat 2.3
```

then

```bash
yq '.a += .b' sample.yml
```

will output

```yaml
a: !horse 3.5
b: !goat 2.3
```


# Alternative (Default value)

This operator is used to provide alternative (or default) values when a particular expression is either null or false.

## LHS is defined

Given a sample.yml file of:

```yaml
a: bridge
```

then

```bash
yq '.a // "hello"' sample.yml
```

will output

```yaml
bridge
```

## LHS is not defined

Given a sample.yml file of:

```yaml
{}
```

then

```bash
yq '.a // "hello"' sample.yml
```

will output

```yaml
hello
```

## LHS is null

Given a sample.yml file of:

```yaml
a: ~
```

then

```bash
yq '.a // "hello"' sample.yml
```

will output

```yaml
hello
```

## LHS is false

Given a sample.yml file of:

```yaml
a: false
```

then

```bash
yq '.a // "hello"' sample.yml
```

will output

```yaml
hello
```

## RHS is an expression

Given a sample.yml file of:

```yaml
a: false
b: cat
```

then

```bash
yq '.a // .b' sample.yml
```

will output

```yaml
cat
```

## Update or create - entity exists

This initialises `a` if it's not present

Given a sample.yml file of:

```yaml
a: 1
```

then

```bash
yq '(.a // (.a = 0)) += 1' sample.yml
```

will output

```yaml
a: 2
```

## Update or create - entity does not exist

This initialises `a` if it's not present

Given a sample.yml file of:

```yaml
b: camel
```

then

```bash
yq '(.a // (.a = 0)) += 1' sample.yml
```

will output

```yaml
b: camel
a: 1
```


# Anchor and Alias Operators

Use the `alias` and `anchor` operators to read and write yaml aliases and anchors. The `explode` operator normalises a yaml file (dereference (or expands) aliases and remove anchor names).

`yq` supports merge aliases (like `<<: *blah`) however this is no longer in the standard yaml spec (1.2) and so `yq` will automatically add the `!!merge` tag to these nodes as it is effectively a custom tag.

## NOTE --yaml-fix-merge-anchor-to-spec flag

`yq` doesn't merge anchors `<<:` to spec, in some circumstances it incorrectly overrides existing keys when the spec documents not to do that.

To minimise disruption while still fixing the issue, a flag has been added to toggle this behaviour. This will first default to false; and log warnings to users. Then it will default to true (and still allow users to specify false if needed).

This flag also enables advanced merging, like inline maps, as well as fixes to ensure when exploding a particular path, neighbours are not affect ed.

Long story short, you should be setting this flag to true.

See examples of the flag differences below, where LEGACY is with the flag off; and FIXED is with the flag on.

## Merge one map

see <https://yaml.org/type/merge.html>

Given a sample.yml file of:

```yaml
- &CENTER
  x: 1
  y: 2
- &LEFT
  x: 0
  y: 2
- &BIG
  r: 10
- &SMALL
  r: 1
- !!merge <<: *CENTER
  r: 10
```

then

```bash
yq '.[4] | explode(.)' sample.yml
```

will output

```yaml
x: 1
y: 2
r: 10
```

## Get anchor

Given a sample.yml file of:

```yaml
a: &billyBob cat
```

then

```bash
yq '.a | anchor' sample.yml
```

will output

```yaml
billyBob
```

## Set anchor

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a anchor = "foobar"' sample.yml
```

will output

```yaml
a: &foobar cat
```

## Set anchor relatively using assign-update

Given a sample.yml file of:

```yaml
a:
  b: cat
```

then

```bash
yq '.a anchor |= .b' sample.yml
```

will output

```yaml
a: &cat
  b: cat
```

## Get alias

Given a sample.yml file of:

```yaml
b: &billyBob meow
a: *billyBob
```

then

```bash
yq '.a | alias' sample.yml
```

will output

```yaml
billyBob
```

## Set alias

Given a sample.yml file of:

```yaml
b: &meow purr
a: cat
```

then

```bash
yq '.a alias = "meow"' sample.yml
```

will output

```yaml
b: &meow purr
a: *meow
```

## Set alias to blank does nothing

Given a sample.yml file of:

```yaml
b: &meow purr
a: cat
```

then

```bash
yq '.a alias = ""' sample.yml
```

will output

```yaml
b: &meow purr
a: cat
```

## Set alias relatively using assign-update

Given a sample.yml file of:

```yaml
b: &meow purr
a:
  f: meow
```

then

```bash
yq '.a alias |= .f' sample.yml
```

will output

```yaml
b: &meow purr
a: *meow
```

## Explode alias and anchor

Given a sample.yml file of:

```yaml
f:
  a: &a cat
  b: *a
```

then

```bash
yq 'explode(.f)' sample.yml
```

will output

```yaml
f:
  a: cat
  b: cat
```

## Explode with no aliases or anchors

Given a sample.yml file of:

```yaml
a: mike
```

then

```bash
yq 'explode(.a)' sample.yml
```

will output

```yaml
a: mike
```

## Explode with alias keys

Given a sample.yml file of:

```yaml
f:
  a: &a cat
  *a : b
```

then

```bash
yq 'explode(.f)' sample.yml
```

will output

```yaml
f:
  a: cat
  cat: b
```

## Dereference and update a field

Use explode with multiply to dereference an object

Given a sample.yml file of:

```yaml
item_value: &item_value
  value: true
thingOne:
  name: item_1
  !!merge <<: *item_value
thingTwo:
  name: item_2
  !!merge <<: *item_value
```

then

```bash
yq '.thingOne |= (explode(.) | sort_keys(.)) * {"value": false}' sample.yml
```

will output

```yaml
item_value: &item_value
  value: true
thingOne:
  name: item_1
  value: false
thingTwo:
  name: item_2
  !!merge <<: *item_value
```

## LEGACY: Explode with merge anchors

Caution: this is for when --yaml-fix-merge-anchor-to-spec=false; it's not to YAML spec because the merge anchors incorrectly override the object values (foobarList.b is set to bar\_b when it should still be foobarList\_b). Flag will default to true in late 2025

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq 'explode(.)' sample.yml
```

will output

```yaml
foo:
  a: foo_a
  thing: foo_thing
  c: foo_c
bar:
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: bar_b
  thing: foo_thing
  c: foobarList_c
  a: foo_a
foobar:
  c: foo_c
  a: foo_a
  thing: foobar_thing
```

## LEGACY: Merge multiple maps

see <https://yaml.org/type/merge.html>. This has the correct data, but the wrong key order; set --yaml-fix-merge-anchor-to-spec=true to fix the key order.

Given a sample.yml file of:

```yaml
- &CENTER
  x: 1
  y: 2
- &LEFT
  x: 0
  y: 2
- &BIG
  r: 10
- &SMALL
  r: 1
- !!merge <<:
    - *CENTER
    - *BIG
```

then

```bash
yq '.[4] | explode(.)' sample.yml
```

will output

```yaml
r: 10
x: 1
y: 2
```

## LEGACY: Override

see <https://yaml.org/type/merge.html>. This has the correct data, but the wrong key order; set --yaml-fix-merge-anchor-to-spec=true to fix the key order.

Given a sample.yml file of:

```yaml
- &CENTER
  x: 1
  y: 2
- &LEFT
  x: 0
  y: 2
- &BIG
  r: 10
- &SMALL
  r: 1
- !!merge <<:
    - *BIG
    - *LEFT
    - *SMALL
  x: 1
```

then

```bash
yq '.[4] | explode(.)' sample.yml
```

will output

```yaml
r: 10
x: 1
y: 2
```

## FIXED: Explode with merge anchors

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour (flag will default to true in late 2025). Observe that foobarList.b property is still foobarList\_b.

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq 'explode(.)' sample.yml
```

will output

```yaml
foo:
  a: foo_a
  thing: foo_thing
  c: foo_c
bar:
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  a: foo_a
  thing: foo_thing
  c: foobarList_c
foobar:
  c: foobar_c
  a: foo_a
  thing: foobar_thing
```

## FIXED: Merge multiple maps

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour (flag will default to true in late 2025). Taken from <https://yaml.org/type/merge.html>. Same values as legacy, but with the correct key order.

Given a sample.yml file of:

```yaml
- &CENTER
  x: 1
  y: 2
- &LEFT
  x: 0
  y: 2
- &BIG
  r: 10
- &SMALL
  r: 1
- !!merge <<:
    - *CENTER
    - *BIG
```

then

```bash
yq '.[4] | explode(.)' sample.yml
```

will output

```yaml
x: 1
y: 2
r: 10
```

## FIXED: Override

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour (flag will default to true in late 2025). Taken from <https://yaml.org/type/merge.html>. Same values as legacy, but with the correct key order.

Given a sample.yml file of:

```yaml
- &CENTER
  x: 1
  y: 2
- &LEFT
  x: 0
  y: 2
- &BIG
  r: 10
- &SMALL
  r: 1
- !!merge <<:
    - *BIG
    - *LEFT
    - *SMALL
  x: 1
```

then

```bash
yq '.[4] | explode(.)' sample.yml
```

will output

```yaml
r: 10
y: 2
x: 1
```

## Exploding inline merge anchor

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour (flag will default to true in late 2025).

Given a sample.yml file of:

```yaml
a:
  b: &b 42
!!merge <<:
  c: *b
```

then

```bash
yq 'explode(.) | sort_keys(.)' sample.yml
```

will output

```yaml
a:
  b: 42
c: 42
```


# Array to Map

Use this operator to convert an array to..a map. The indices are used as map keys, null values in the array are skipped over.

Behind the scenes, this is implemented using reduce:

```
(.[] | select(. != null) ) as $i ireduce({}; .[$i | key] = $i)
```

## Simple example

Given a sample.yml file of:

```yaml
cool:
  - null
  - null
  - hello
```

then

```bash
yq '.cool |= array_to_map' sample.yml
```

will output

```yaml
cool:
  2: hello
```


# Assign (Update)

This operator is used to update node values. It can be used in either the:

### plain form: `=`

Which will set the LHS node values equal to the RHS node values. The RHS expression is run against the matching nodes in the pipeline.

### relative form: `|=`

This will do a similar thing to the plain form, but the RHS expression is run with *each LHS node as context*. This is useful for updating values based on old values, e.g. increment.

### Flags

* `c` clobber custom tags

## Create yaml file

Running

```bash
yq --null-input '.a.b = "cat" | .x = "frog"'
```

will output

```yaml
a:
  b: cat
x: frog
```

## Update node to be the child value

Given a sample.yml file of:

```yaml
a:
  b:
    g: foof
```

then

```bash
yq '.a |= .b' sample.yml
```

will output

```yaml
a:
  g: foof
```

## Double elements in an array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq '.[] |= . * 2' sample.yml
```

will output

```yaml
- 2
- 4
- 6
```

## Update node from another file

Note this will also work when the second file is a scalar (string/number)

Given a sample.yml file of:

```yaml
a: apples
```

And another sample another.yml file of:

```yaml
b: bob
```

then

```bash
yq eval-all 'select(fileIndex==0).a = select(fileIndex==1) | select(fileIndex==0)' sample.yml another.yml
```

will output

```yaml
a:
  b: bob
```

## Update node to be the sibling value

Given a sample.yml file of:

```yaml
a:
  b: child
b: sibling
```

then

```bash
yq '.a = .b' sample.yml
```

will output

```yaml
a: sibling
b: sibling
```

## Updated multiple paths

Given a sample.yml file of:

```yaml
a: fieldA
b: fieldB
c: fieldC
```

then

```bash
yq '(.a, .c) = "potato"' sample.yml
```

will output

```yaml
a: potato
b: fieldB
c: potato
```

## Update string value

Given a sample.yml file of:

```yaml
a:
  b: apple
```

then

```bash
yq '.a.b = "frog"' sample.yml
```

will output

```yaml
a:
  b: frog
```

## Update string value via |=

Note there is no difference between `=` and `|=` when the RHS is a scalar

Given a sample.yml file of:

```yaml
a:
  b: apple
```

then

```bash
yq '.a.b |= "frog"' sample.yml
```

will output

```yaml
a:
  b: frog
```

## Update deeply selected results

Note that the LHS is wrapped in brackets! This is to ensure we don't first filter out the yaml and then update the snippet.

Given a sample.yml file of:

```yaml
a:
  b: apple
  c: cactus
```

then

```bash
yq '(.a[] | select(. == "apple")) = "frog"' sample.yml
```

will output

```yaml
a:
  b: frog
  c: cactus
```

## Update array values

Given a sample.yml file of:

```yaml
- candy
- apple
- sandy
```

then

```bash
yq '(.[] | select(. == "*andy")) = "bogs"' sample.yml
```

will output

```yaml
- bogs
- apple
- bogs
```

## Update empty object

Given a sample.yml file of:

```yaml
{}
```

then

```bash
yq '.a.b |= "bogs"' sample.yml
```

will output

```yaml
a:
  b: bogs
```

## Update node value that has an anchor

Anchor will remain

Given a sample.yml file of:

```yaml
a: &cool cat
```

then

```bash
yq '.a = "dog"' sample.yml
```

will output

```yaml
a: &cool dog
```

## Update empty object and array

Given a sample.yml file of:

```yaml
{}
```

then

```bash
yq '.a.b.[0] |= "bogs"' sample.yml
```

will output

```yaml
a:
  b:
    - bogs
```

## Custom types are maintained by default

Given a sample.yml file of:

```yaml
a: !cat meow
b: !dog woof
```

then

```bash
yq '.a = .b' sample.yml
```

will output

```yaml
a: !cat woof
b: !dog woof
```

## Custom types: clobber

Use the `c` option to clobber custom tags

Given a sample.yml file of:

```yaml
a: !cat meow
b: !dog woof
```

then

```bash
yq '.a =c .b' sample.yml
```

will output

```yaml
a: !dog woof
b: !dog woof
```


# Boolean Operators

The `or` and `and` operators take two parameters and return a boolean result.

`not` flips a boolean from true to false, or vice versa.

`any` will return `true` if there are any `true` values in an array sequence, and `all` will return true if *all* elements in an array are true.

`any_c(condition)` and `all_c(condition)` are like `any` and `all` but they take a condition expression that is used against each element to determine if it's `true`. Note: in `jq` you can simply pass a condition to `any` or `all` and it simply works - `yq` isn't that clever..yet

These are most commonly used with the `select` operator to filter particular nodes.

## Related Operators

* equals / not equals (`==`, `!=`) operators [here](https://mikefarah.gitbook.io/yq/operators/equals)
* comparison (`>=`, `<` etc) operators [here](https://mikefarah.gitbook.io/yq/operators/compare)
* select operator [here](https://mikefarah.gitbook.io/yq/operators/select)

## `or` example

Running

```bash
yq --null-input 'true or false'
```

will output

```yaml
true
```

## "yes" and "no" are strings

In the yaml 1.2 standard, support for yes/no as booleans was dropped - they are now considered strings. See '10.2.1.2. Boolean' in <https://yaml.org/spec/1.2.2/>

Given a sample.yml file of:

```yaml
- yes
- no
```

then

```bash
yq '.[] | tag' sample.yml
```

will output

```yaml
!!str
!!str
```

## `and` example

Running

```bash
yq --null-input 'true and false'
```

will output

```yaml
false
```

## Matching nodes with select, equals and or

Given a sample.yml file of:

```yaml
- a: bird
  b: dog
- a: frog
  b: bird
- a: cat
  b: fly
```

then

```bash
yq '[.[] | select(.a == "cat" or .b == "dog")]' sample.yml
```

will output

```yaml
- a: bird
  b: dog
- a: cat
  b: fly
```

## `any` returns true if any boolean in a given array is true

Given a sample.yml file of:

```yaml
- false
- true
```

then

```bash
yq 'any' sample.yml
```

will output

```yaml
true
```

## `any` returns false for an empty array

Given a sample.yml file of:

```yaml
[]
```

then

```bash
yq 'any' sample.yml
```

will output

```yaml
false
```

## `any_c` returns true if any element in the array is true for the given condition.

Given a sample.yml file of:

```yaml
a:
  - rad
  - awesome
b:
  - meh
  - whatever
```

then

```bash
yq '.[] |= any_c(. == "awesome")' sample.yml
```

will output

```yaml
a: true
b: false
```

## `all` returns true if all booleans in a given array are true

Given a sample.yml file of:

```yaml
- true
- true
```

then

```bash
yq 'all' sample.yml
```

will output

```yaml
true
```

## `all` returns true for an empty array

Given a sample.yml file of:

```yaml
[]
```

then

```bash
yq 'all' sample.yml
```

will output

```yaml
true
```

## `all_c` returns true if all elements in the array are true for the given condition.

Given a sample.yml file of:

```yaml
a:
  - rad
  - awesome
b:
  - meh
  - 12
```

then

```bash
yq '.[] |= all_c(tag == "!!str")' sample.yml
```

will output

```yaml
a: true
b: false
```

## Not true is false

Running

```bash
yq --null-input 'true | not'
```

will output

```yaml
false
```

## Not false is true

Running

```bash
yq --null-input 'false | not'
```

will output

```yaml
true
```

## String values considered to be true

Running

```bash
yq --null-input '"cat" | not'
```

will output

```yaml
false
```

## Empty string value considered to be true

Running

```bash
yq --null-input '"" | not'
```

will output

```yaml
false
```

## Numbers are considered to be true

Running

```bash
yq --null-input '1 | not'
```

will output

```yaml
false
```

## Zero is considered to be true

Running

```bash
yq --null-input '0 | not'
```

will output

```yaml
false
```

## Null is considered to be false

Running

```bash
yq --null-input '~ | not'
```

will output

```yaml
true
```


# Collect into Array

This creates an array using the expression between the square brackets.

## Collect empty

Running

```bash
yq --null-input '[]'
```

will output

```yaml
[]
```

## Collect single

Running

```bash
yq --null-input '["cat"]'
```

will output

```yaml
- cat
```

## Collect many

Given a sample.yml file of:

```yaml
a: cat
b: dog
```

then

```bash
yq '[.a, .b]' sample.yml
```

will output

```yaml
- cat
- dog
```


# Column

Returns the column of the matching node. Starts from 1, 0 indicates there was no column data.

Column is the number of characters that precede that node on the line it starts.

## Returns column of *value* node

Given a sample.yml file of:

```yaml
a: cat
b: bob
```

then

```bash
yq '.b | column' sample.yml
```

will output

```yaml
4
```

## Returns column of *key* node

Pipe through the key operator to get the column of the key

Given a sample.yml file of:

```yaml
a: cat
b: bob
```

then

```bash
yq '.b | key | column' sample.yml
```

will output

```yaml
1
```

## First column is 1

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a | key | column' sample.yml
```

will output

```yaml
1
```

## No column data is 0

Running

```bash
yq --null-input '{"a": "new entry"} | column'
```

will output

```yaml
0
```


# Comment Operators

Use these comment operators to set or retrieve comments. Note that line comments on maps/arrays are actually set on the *key* node as opposed to the *value* (map/array). See below for examples.

Like the `=` and `|=` assign operators, the same syntax applies when updating comments:

### plain form: `=`

This will set the LHS nodes' comments equal to the expression on the RHS. The RHS is run against the matching nodes in the pipeline

### relative form: `|=`

This is similar to the plain form, but it evaluates the RHS with *each matching LHS node as context*. This is useful if you want to set the comments as a relative expression of the node, for instance its value or path.

## Set line comment

Set the comment on the key node for more reliability (see below).

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a line_comment="single"' sample.yml
```

will output

```yaml
a: cat # single
```

## Set line comment of a maps/arrays

For maps and arrays, you need to set the line comment on the *key* node. This will also work for scalars.

Given a sample.yml file of:

```yaml
a:
  b: things
```

then

```bash
yq '(.a | key) line_comment="single"' sample.yml
```

will output

```yaml
a: # single
  b: things
```

## Use update assign to perform relative updates

Given a sample.yml file of:

```yaml
a: cat
b: dog
```

then

```bash
yq '.. line_comment |= .' sample.yml
```

will output

```yaml
a: cat # cat
b: dog # dog
```

## Where is the comment - map key example

The underlying yaml parser can assign comments in a document to surprising nodes. Use an expression like this to find where you comment is. 'p' indicates the path, 'isKey' is if the node is a map key (as opposed to a map value). From this, you can see the 'hello-world-comment' is actually on the 'hello' key

Given a sample.yml file of:

```yaml
hello: # hello-world-comment
  message: world
```

then

```bash
yq '[... | {"p": path | join("."), "isKey": is_key, "hc": headComment, "lc": lineComment, "fc": footComment}]' sample.yml
```

will output

```yaml
- p: ""
  isKey: false
  hc: ""
  lc: ""
  fc: ""
- p: hello
  isKey: true
  hc: ""
  lc: hello-world-comment
  fc: ""
- p: hello
  isKey: false
  hc: ""
  lc: ""
  fc: ""
- p: hello.message
  isKey: true
  hc: ""
  lc: ""
  fc: ""
- p: hello.message
  isKey: false
  hc: ""
  lc: ""
  fc: ""
```

## Retrieve comment - map key example

From the previous example, we know that the comment is on the 'hello' *key* as a lineComment

Given a sample.yml file of:

```yaml
hello: # hello-world-comment
  message: world
```

then

```bash
yq '.hello | key | line_comment' sample.yml
```

will output

```yaml
hello-world-comment
```

## Where is the comment - array example

The underlying yaml parser can assign comments in a document to surprising nodes. Use an expression like this to find where you comment is. 'p' indicates the path, 'isKey' is if the node is a map key (as opposed to a map value). From this, you can see the 'under-name-comment' is actually on the first child

Given a sample.yml file of:

```yaml
name:
  # under-name-comment
  - first-array-child
```

then

```bash
yq '[... | {"p": path | join("."), "isKey": is_key, "hc": headComment, "lc": lineComment, "fc": footComment}]' sample.yml
```

will output

```yaml
- p: ""
  isKey: false
  hc: ""
  lc: ""
  fc: ""
- p: name
  isKey: true
  hc: ""
  lc: ""
  fc: ""
- p: name
  isKey: false
  hc: ""
  lc: ""
  fc: ""
- p: name.0
  isKey: false
  hc: under-name-comment
  lc: ""
  fc: ""
```

## Retrieve comment - array example

From the previous example, we know that the comment is on the first child as a headComment

Given a sample.yml file of:

```yaml
name:
  # under-name-comment
  - first-array-child
```

then

```bash
yq '.name[0] | headComment' sample.yml
```

will output

```yaml
under-name-comment
```

## Set head comment

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '. head_comment="single"' sample.yml
```

will output

```yaml
# single
a: cat
```

## Set head comment of a map entry

Given a sample.yml file of:

```yaml
f: foo
a:
  b: cat
```

then

```bash
yq '(.a | key) head_comment="single"' sample.yml
```

will output

```yaml
f: foo
# single
a:
  b: cat
```

## Set foot comment, using an expression

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '. foot_comment=.a' sample.yml
```

will output

```yaml
a: cat
# cat
```

## Remove comment

Given a sample.yml file of:

```yaml
a: cat # comment
b: dog # leave this
```

then

```bash
yq '.a line_comment=""' sample.yml
```

will output

```yaml
a: cat
b: dog # leave this
```

## Remove (strip) all comments

Note the use of `...` to ensure key nodes are included.

Given a sample.yml file of:

```yaml
# hi

a: cat # comment
# great
b: # key comment
```

then

```bash
yq '... comments=""' sample.yml
```

will output

```yaml
a: cat
b:
```

## Get line comment

Given a sample.yml file of:

```yaml
# welcome!

a: cat # meow
# have a great day
```

then

```bash
yq '.a | line_comment' sample.yml
```

will output

```yaml
meow
```

## Get head comment

Given a sample.yml file of:

```yaml
# welcome!

a: cat # meow

# have a great day
```

then

```bash
yq '. | head_comment' sample.yml
```

will output

```yaml
welcome!

```

## Head comment with document split

Given a sample.yml file of:

```yaml
# welcome!
---
# bob
a: cat # meow

# have a great day
```

then

```bash
yq 'head_comment' sample.yml
```

will output

```yaml
welcome!
bob
```

## Get foot comment

Given a sample.yml file of:

```yaml
# welcome!

a: cat # meow

# have a great day
# no really
```

then

```bash
yq '. | foot_comment' sample.yml
```

will output

```yaml
have a great day
no really
```


# Compare Operators

Comparison operators (`>`, `>=`, `<`, `<=`) can be used for comparing scalar values of the same time.

The following types are currently supported:

* numbers
* strings
* datetimes

## Related Operators

* equals / not equals (`==`, `!=`) operators [here](https://mikefarah.gitbook.io/yq/operators/equals)
* boolean operators (`and`, `or`, `any` etc) [here](https://mikefarah.gitbook.io/yq/operators/boolean-operators)
* select operator [here](https://mikefarah.gitbook.io/yq/operators/select)

## Compare numbers (>)

Given a sample.yml file of:

```yaml
a: 5
b: 4
```

then

```bash
yq '.a > .b' sample.yml
```

will output

```yaml
true
```

## Compare equal numbers (>=)

Given a sample.yml file of:

```yaml
a: 5
b: 5
```

then

```bash
yq '.a >= .b' sample.yml
```

will output

```yaml
true
```

## Compare strings

Compares strings by their bytecode.

Given a sample.yml file of:

```yaml
a: zoo
b: apple
```

then

```bash
yq '.a > .b' sample.yml
```

will output

```yaml
true
```

## Compare date times

You can compare date times. Assumes RFC3339 date time format, see [date-time operators](https://mikefarah.gitbook.io/yq/operators/date-time-operators) for more information.

Given a sample.yml file of:

```yaml
a: 2021-01-01T03:10:00Z
b: 2020-01-01T03:10:00Z
```

then

```bash
yq '.a > .b' sample.yml
```

will output

```yaml
true
```

## Both sides are null: > is false

Running

```bash
yq --null-input '.a > .b'
```

will output

```yaml
false
```

## Both sides are null: >= is true

Running

```bash
yq --null-input '.a >= .b'
```

will output

```yaml
true
```


# Contains

This returns `true` if the context contains the passed in parameter, and false otherwise. For arrays, this will return true if the passed in array is contained within the array. For strings, it will return true if the string is a substring.

{% hint style="warning" %}
*Note* that, just like jq, when checking if an array of strings `contains` another, this will use `contains` and *not* equals to check each string. This means an expression like `contains(["cat"])` will return true for an array `["cats"]`.

See the "Array has a subset array" example below on how to check for a subset.
{% endhint %}

## Array contains array

Array is equal or subset of

Given a sample.yml file of:

```yaml
- foobar
- foobaz
- blarp
```

then

```bash
yq 'contains(["baz", "bar"])' sample.yml
```

will output

```yaml
true
```

## Array has a subset array

Subtract the superset array from the subset, if there's anything left, it's not a subset

Given a sample.yml file of:

```yaml
- foobar
- foobaz
- blarp
```

then

```bash
yq '["baz", "bar"] - . | length == 0' sample.yml
```

will output

```yaml
false
```

## Object included in array

Given a sample.yml file of:

```yaml
"foo": 12
"bar":
  - 1
  - 2
  - "barp": 12
    "blip": 13
```

then

```bash
yq 'contains({"bar": [{"barp": 12}]})' sample.yml
```

will output

```yaml
true
```

## Object not included in array

Given a sample.yml file of:

```yaml
"foo": 12
"bar":
  - 1
  - 2
  - "barp": 12
    "blip": 13
```

then

```bash
yq 'contains({"foo": 12, "bar": [{"barp": 15}]})' sample.yml
```

will output

```yaml
false
```

## String contains substring

Given a sample.yml file of:

```yaml
foobar
```

then

```bash
yq 'contains("bar")' sample.yml
```

will output

```yaml
true
```

## String equals string

Given a sample.yml file of:

```yaml
meow
```

then

```bash
yq 'contains("meow")' sample.yml
```

will output

```yaml
true
```


# Create, Collect into Object

This is used to construct objects (or maps). This can be used against existing yaml, or to create fresh yaml documents.

## Collect empty object

Running

```bash
yq --null-input '{}'
```

will output

```yaml
{}
```

## Wrap (prefix) existing object

Given a sample.yml file of:

```yaml
name: Mike
```

then

```bash
yq '{"wrap": .}' sample.yml
```

will output

```yaml
wrap:
  name: Mike
```

## Using splat to create multiple objects

Given a sample.yml file of:

```yaml
name: Mike
pets:
  - cat
  - dog
```

then

```bash
yq '{.name: .pets.[]}' sample.yml
```

will output

```yaml
Mike: cat
Mike: dog
```

## Working with multiple documents

Given a sample.yml file of:

```yaml
name: Mike
pets:
  - cat
  - dog
---
name: Rosey
pets:
  - monkey
  - sheep
```

then

```bash
yq '{.name: .pets.[]}' sample.yml
```

will output

```yaml
Mike: cat
Mike: dog
---
Rosey: monkey
Rosey: sheep
```

## Creating yaml from scratch

Running

```bash
yq --null-input '{"wrap": "frog"}'
```

will output

```yaml
wrap: frog
```

## Creating yaml from scratch with multiple objects

Running

```bash
yq --null-input '(.a.b = "foo") | (.d.e = "bar")'
```

will output

```yaml
a:
  b: foo
d:
  e: bar
```


# Date Time

Various operators for parsing and manipulating dates.

## Date time formattings

This uses Golang's built in time library for parsing and formatting date times.

When not specified, the RFC3339 standard is assumed `2006-01-02T15:04:05Z07:00` for parsing.

To specify a custom parsing format, use the `with_dtf` operator. The first parameter sets the datetime parsing format for the expression in the second parameter. The expression can be any valid `yq` expression tree.

```bash
yq 'with_dtf("myformat"; .a + "3h" | tz("Australia/Melbourne"))'
```

See the [library docs](https://pkg.go.dev/time#pkg-constants) for examples of formatting options.

## Timezones

This uses Golang's built in LoadLocation function to parse timezones strings. See the [library docs](https://pkg.go.dev/time#LoadLocation) for more details.

## Durations

Durations are parsed using Golang's built in [ParseDuration](https://pkg.go.dev/time#ParseDuration) function.

You can add durations to time using the `+` operator.

## Format: from standard RFC3339 format

Providing a single parameter assumes a standard RFC3339 datetime format. If the target format is not a valid yaml datetime format, the result will be a string tagged node.

Given a sample.yml file of:

```yaml
a: 2001-12-15T02:59:43.1Z
```

then

```bash
yq '.a |= format_datetime("Monday, 02-Jan-06 at 3:04PM")' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 2:59AM
```

## Format: from custom date time

Use with\_dtf to set a custom datetime format for parsing.

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM
```

then

```bash
yq '.a |= with_dtf("Monday, 02-Jan-06 at 3:04PM"; format_datetime("2006-01-02"))' sample.yml
```

will output

```yaml
a: 2001-12-15
```

## Format: get the day of the week

Given a sample.yml file of:

```yaml
a: 2001-12-15
```

then

```bash
yq '.a | format_datetime("Monday")' sample.yml
```

will output

```yaml
Saturday
```

## Now

Given a sample.yml file of:

```yaml
a: cool
```

then

```bash
yq '.updated = now' sample.yml
```

will output

```yaml
a: cool
updated: 2021-05-19T01:02:03Z
```

## From Unix

Converts from unix time. Note, you don't have to pipe through the tz operator :)

Running

```bash
yq --null-input '1675301929 | from_unix | tz("UTC")'
```

will output

```yaml
2023-02-02T01:38:49Z
```

## To Unix

Converts to unix time

Running

```bash
yq --null-input 'now | to_unix'
```

will output

```yaml
1621386123
```

## Timezone: from standard RFC3339 format

Returns a new datetime in the specified timezone. Specify standard IANA Time Zone format or 'utc', 'local'. When given a single parameter, this assumes the datetime is in RFC3339 format.

Given a sample.yml file of:

```yaml
a: cool
```

then

```bash
yq '.updated = (now | tz("Australia/Sydney"))' sample.yml
```

will output

```yaml
a: cool
updated: 2021-05-19T11:02:03+10:00
```

## Timezone: with custom format

Specify standard IANA Time Zone format or 'utc', 'local'

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

then

```bash
yq '.a |= with_dtf("Monday, 02-Jan-06 at 3:04PM MST"; tz("Australia/Sydney"))' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 1:59PM AEDT
```

## Add and tz custom format

Specify standard IANA Time Zone format or 'utc', 'local'

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

then

```bash
yq '.a |= with_dtf("Monday, 02-Jan-06 at 3:04PM MST"; tz("Australia/Sydney"))' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 1:59PM AEDT
```

## Date addition

Given a sample.yml file of:

```yaml
a: 2021-01-01T00:00:00Z
```

then

```bash
yq '.a += "3h10m"' sample.yml
```

will output

```yaml
a: 2021-01-01T03:10:00Z
```

## Date subtraction

You can subtract durations from dates. Assumes RFC3339 date time format, see [date-time operators](https://mikefarah.gitbook.io/yq/operators/datetime#date-time-formattings) for more information.

Given a sample.yml file of:

```yaml
a: 2021-01-01T03:10:00Z
```

then

```bash
yq '.a -= "3h10m"' sample.yml
```

will output

```yaml
a: 2021-01-01T00:00:00Z
```

## Date addition - custom format

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

then

```bash
yq 'with_dtf("Monday, 02-Jan-06 at 3:04PM MST"; .a += "3h1m")' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 6:00AM GMT
```

## Date script with custom format

You can embed full expressions in with\_dtf if needed.

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

then

```bash
yq 'with_dtf("Monday, 02-Jan-06 at 3:04PM MST"; .a = (.a + "3h1m" | tz("Australia/Perth")))' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 2:00PM AWST
```


# Delete

Deletes matching entries in maps or arrays.

## Delete entry in map

Given a sample.yml file of:

```yaml
a: cat
b: dog
```

then

```bash
yq 'del(.b)' sample.yml
```

will output

```yaml
a: cat
```

## Delete nested entry in map

Given a sample.yml file of:

```yaml
a:
  a1: fred
  a2: frood
```

then

```bash
yq 'del(.a.a1)' sample.yml
```

will output

```yaml
a:
  a2: frood
```

## Delete entry in array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq 'del(.[1])' sample.yml
```

will output

```yaml
- 1
- 3
```

## Delete nested entry in array

Given a sample.yml file of:

```yaml
- a: cat
  b: dog
```

then

```bash
yq 'del(.[0].a)' sample.yml
```

will output

```yaml
- b: dog
```

## Delete no matches

Given a sample.yml file of:

```yaml
a: cat
b: dog
```

then

```bash
yq 'del(.c)' sample.yml
```

will output

```yaml
a: cat
b: dog
```

## Delete matching entries

Given a sample.yml file of:

```yaml
a: cat
b: dog
c: bat
```

then

```bash
yq 'del( .[] | select(. == "*at") )' sample.yml
```

will output

```yaml
b: dog
```

## Recursively delete matching keys

Given a sample.yml file of:

```yaml
a:
  name: frog
  b:
    name: blog
    age: 12
```

then

```bash
yq 'del(.. | select(has("name")).name)' sample.yml
```

will output

```yaml
a:
  b:
    age: 12
```


# Divide

Divide behaves differently according to the type of the LHS:

* strings: split by the divider
* number: arithmetic division

## String split

Given a sample.yml file of:

```yaml
a: cat_meow
b: _
```

then

```bash
yq '.c = .a / .b' sample.yml
```

will output

```yaml
a: cat_meow
b: _
c:
  - cat
  - meow
```

## Number division

The result during division is calculated as a float

Given a sample.yml file of:

```yaml
a: 12
b: 2.5
```

then

```bash
yq '.a = .a / .b' sample.yml
```

will output

```yaml
a: 4.8
b: 2.5
```

## Number division by zero

Dividing by zero results in +Inf or -Inf

Given a sample.yml file of:

```yaml
a: 1
b: -1
```

then

```bash
yq '.a = .a / 0 | .b = .b / 0' sample.yml
```

will output

```yaml
a: !!float +Inf
b: !!float -Inf
```


# Document Index

Use the `documentIndex` operator (or the `di` shorthand) to select nodes of a particular document.

## Retrieve a document index

Given a sample.yml file of:

```yaml
a: cat
---
a: frog
```

then

```bash
yq '.a | document_index' sample.yml
```

will output

```yaml
0
---
1
```

## Retrieve a document index, shorthand

Given a sample.yml file of:

```yaml
a: cat
---
a: frog
```

then

```bash
yq '.a | di' sample.yml
```

will output

```yaml
0
---
1
```

## Filter by document index

Given a sample.yml file of:

```yaml
a: cat
---
a: frog
```

then

```bash
yq 'select(document_index == 1)' sample.yml
```

will output

```yaml
a: frog
```

## Filter by document index shorthand

Given a sample.yml file of:

```yaml
a: cat
---
a: frog
```

then

```bash
yq 'select(di == 1)' sample.yml
```

will output

```yaml
a: frog
```

## Print Document Index with matches

Given a sample.yml file of:

```yaml
a: cat
---
a: frog
```

then

```bash
yq '.a | ({"match": ., "doc": document_index})' sample.yml
```

will output

```yaml
match: cat
doc: 0
---
match: frog
doc: 1
```


# Encode / Decode

Encode operators will take the piped in object structure and encode it as a string in the desired format. The decode operators do the opposite, they take a formatted string and decode it into the relevant object structure.

Note that you can optionally pass an indent value to the encode functions (see below).

These operators are useful to process yaml documents that have stringified embedded yaml/json/props in them.

| Format     | Decode (from string) | Encode (to string) |
| ---------- | -------------------- | ------------------ |
| Yaml       | from\_yaml/@yamld    | to\_yaml(i)/@yaml  |
| JSON       | from\_json/@jsond    | to\_json(i)/@json  |
| Properties | from\_props/@propsd  | to\_props/@props   |
| CSV        | from\_csv/@csvd      | to\_csv/@csv       |
| TSV        | from\_tsv/@tsvd      | to\_tsv/@tsv       |
| XML        | from\_xml/@xmld      | to\_xml(i)/@xml    |
| Base64     | @base64d             | @base64            |
| URI        | @urid                | @uri               |
| Shell      |                      | @sh                |

See CSV and TSV [documentation](https://mikefarah.gitbook.io/yq/usage/csv-tsv) for accepted formats.

XML uses the `--xml-attribute-prefix` and `xml-content-name` flags to identify attributes and content fields.

Base64 assumes [rfc4648](https://rfc-editor.org/rfc/rfc4648.html) encoding. Encoding and decoding both assume that the content is a utf-8 string and not binary content.

## Encode value as json string

Given a sample.yml file of:

```yaml
a:
  cool: thing
```

then

```bash
yq '.b = (.a | to_json)' sample.yml
```

will output

```yaml
a:
  cool: thing
b: |
  {
    "cool": "thing"
  }
```

## Encode value as json string, on one line

Pass in a 0 indent to print json on a single line.

Given a sample.yml file of:

```yaml
a:
  cool: thing
```

then

```bash
yq '.b = (.a | to_json(0))' sample.yml
```

will output

```yaml
a:
  cool: thing
b: '{"cool":"thing"}'
```

## Encode value as json string, on one line shorthand

Pass in a 0 indent to print json on a single line.

Given a sample.yml file of:

```yaml
a:
  cool: thing
```

then

```bash
yq '.b = (.a | @json)' sample.yml
```

will output

```yaml
a:
  cool: thing
b: '{"cool":"thing"}'
```

## Decode a json encoded string

Keep in mind JSON is a subset of YAML. If you want idiomatic yaml, pipe through the style operator to clear out the JSON styling.

Given a sample.yml file of:

```yaml
a: '{"cool":"thing"}'
```

then

```bash
yq '.a | from_json | ... style=""' sample.yml
```

will output

```yaml
cool: thing
```

## Encode value as props string

Given a sample.yml file of:

```yaml
a:
  cool: thing
```

then

```bash
yq '.b = (.a | @props)' sample.yml
```

will output

```yaml
a:
  cool: thing
b: |
  cool = thing
```

## Decode props encoded string

Given a sample.yml file of:

```yaml
a: |-
  cats=great
  dogs=cool as well
```

then

```bash
yq '.a |= @propsd' sample.yml
```

will output

```yaml
a:
  cats: great
  dogs: cool as well
```

## Decode csv encoded string

Given a sample.yml file of:

```yaml
a: |-
  cats,dogs
  great,cool as well
```

then

```bash
yq '.a |= @csvd' sample.yml
```

will output

```yaml
a:
  - cats: great
    dogs: cool as well
```

## Decode tsv encoded string

Given a sample.yml file of:

```yaml
a: |-
  cats	dogs
  great	cool as well
```

then

```bash
yq '.a |= @tsvd' sample.yml
```

will output

```yaml
a:
  - cats: great
    dogs: cool as well
```

## Encode value as yaml string

Indent defaults to 2

Given a sample.yml file of:

```yaml
a:
  cool:
    bob: dylan
```

then

```bash
yq '.b = (.a | to_yaml)' sample.yml
```

will output

```yaml
a:
  cool:
    bob: dylan
b: |
  cool:
    bob: dylan
```

## Encode value as yaml string, with custom indentation

You can specify the indentation level as the first parameter.

Given a sample.yml file of:

```yaml
a:
  cool:
    bob: dylan
```

then

```bash
yq '.b = (.a | to_yaml(8))' sample.yml
```

will output

```yaml
a:
  cool:
    bob: dylan
b: |
  cool:
          bob: dylan
```

## Decode a yaml encoded string

Given a sample.yml file of:

```yaml
a: 'foo: bar'
```

then

```bash
yq '.b = (.a | from_yaml)' sample.yml
```

will output

```yaml
a: 'foo: bar'
b:
  foo: bar
```

## Update a multiline encoded yaml string

Given a sample.yml file of:

```yaml
a: |
  foo: bar
  baz: dog

```

then

```bash
yq '.a |= (from_yaml | .foo = "cat" | to_yaml)' sample.yml
```

will output

```yaml
a: |
  foo: cat
  baz: dog
```

## Update a single line encoded yaml string

Given a sample.yml file of:

```yaml
a: 'foo: bar'
```

then

```bash
yq '.a |= (from_yaml | .foo = "cat" | to_yaml)' sample.yml
```

will output

```yaml
a: 'foo: cat'
```

## Encode array of scalars as csv string

Scalars are strings, numbers and booleans.

Given a sample.yml file of:

```yaml
- cat
- thing1,thing2
- true
- 3.40
```

then

```bash
yq '@csv' sample.yml
```

will output

```yaml
cat,"thing1,thing2",true,3.40
```

## Encode array of arrays as csv string

Given a sample.yml file of:

```yaml
- - cat
  - thing1,thing2
  - true
  - 3.40
- - dog
  - thing3
  - false
  - 12
```

then

```bash
yq '@csv' sample.yml
```

will output

```yaml
cat,"thing1,thing2",true,3.40
dog,thing3,false,12
```

## Encode array of arrays as tsv string

Scalars are strings, numbers and booleans.

Given a sample.yml file of:

```yaml
- - cat
  - thing1,thing2
  - true
  - 3.40
- - dog
  - thing3
  - false
  - 12
```

then

```bash
yq '@tsv' sample.yml
```

will output

```yaml
cat	thing1,thing2	true	3.40
dog	thing3	false	12
```

## Encode value as xml string

Given a sample.yml file of:

```yaml
a:
  cool:
    foo: bar
    +@id: hi
```

then

```bash
yq '.a | to_xml' sample.yml
```

will output

```yaml
<cool id="hi">
  <foo>bar</foo>
</cool>

```

## Encode value as xml string on a single line

Given a sample.yml file of:

```yaml
a:
  cool:
    foo: bar
    +@id: hi
```

then

```bash
yq '.a | @xml' sample.yml
```

will output

```yaml
<cool id="hi"><foo>bar</foo></cool>

```

## Encode value as xml string with custom indentation

Given a sample.yml file of:

```yaml
a:
  cool:
    foo: bar
    +@id: hi
```

then

```bash
yq '{"cat": .a | to_xml(1)}' sample.yml
```

will output

```yaml
cat: |
  <cool id="hi">
   <foo>bar</foo>
  </cool>
```

## Decode a xml encoded string

Given a sample.yml file of:

```yaml
a: <foo>bar</foo>
```

then

```bash
yq '.b = (.a | from_xml)' sample.yml
```

will output

```yaml
a: <foo>bar</foo>
b:
  foo: bar
```

## Encode a string to base64

Given a sample.yml file of:

```yaml
coolData: a special string
```

then

```bash
yq '.coolData | @base64' sample.yml
```

will output

```yaml
YSBzcGVjaWFsIHN0cmluZw==
```

## Encode a yaml document to base64

Pipe through @yaml first to convert to a string, then use @base64 to encode it.

Given a sample.yml file of:

```yaml
a: apple
```

then

```bash
yq '@yaml | @base64' sample.yml
```

will output

```yaml
YTogYXBwbGUK
```

## Encode a string to uri

Given a sample.yml file of:

```yaml
coolData: this has & special () characters *
```

then

```bash
yq '.coolData | @uri' sample.yml
```

will output

```yaml
this+has+%26+special+%28%29+characters+%2A
```

## Decode a URI to a string

Given a sample.yml file of:

```yaml
this+has+%26+special+%28%29+characters+%2A
```

then

```bash
yq '@urid' sample.yml
```

will output

```yaml
this has & special () characters *
```

## Encode a string to sh

Sh/Bash friendly string

Given a sample.yml file of:

```yaml
coolData: strings with spaces and a 'quote'
```

then

```bash
yq '.coolData | @sh' sample.yml
```

will output

```yaml
strings' with spaces and a '\'quote\'
```

## Decode a base64 encoded string

Decoded data is assumed to be a string.

Given a sample.yml file of:

```yaml
coolData: V29ya3Mgd2l0aCBVVEYtMTYg8J+Yig==
```

then

```bash
yq '.coolData | @base64d' sample.yml
```

will output

```yaml
Works with UTF-16 😊
```

## Decode a base64 encoded yaml document

Pipe through `from_yaml` to parse the decoded base64 string as a yaml document.

Given a sample.yml file of:

```yaml
coolData: YTogYXBwbGUK
```

then

```bash
yq '.coolData |= (@base64d | from_yaml)' sample.yml
```

will output

```yaml
coolData:
  a: apple
```


# Entries

Similar to the same named functions in `jq` these functions convert to/from an object and an array of key-value pairs. This is most useful for performing operations on keys of maps.

Use `with_entries(op)` as a syntactic sugar for doing `to_entries | op | from_entries`.

## to\_entries Map

Given a sample.yml file of:

```yaml
a: 1
b: 2
```

then

```bash
yq 'to_entries' sample.yml
```

will output

```yaml
- key: a
  value: 1
- key: b
  value: 2
```

## to\_entries Array

Given a sample.yml file of:

```yaml
- a
- b
```

then

```bash
yq 'to_entries' sample.yml
```

will output

```yaml
- key: 0
  value: a
- key: 1
  value: b
```

## to\_entries null

Given a sample.yml file of:

```yaml
null
```

then

```bash
yq 'to_entries' sample.yml
```

will output

```yaml
```

## from\_entries map

Given a sample.yml file of:

```yaml
a: 1
b: 2
```

then

```bash
yq 'to_entries | from_entries' sample.yml
```

will output

```yaml
a: 1
b: 2
```

## from\_entries with numeric key indices

from\_entries always creates a map, even for numeric keys

Given a sample.yml file of:

```yaml
- a
- b
```

then

```bash
yq 'to_entries | from_entries' sample.yml
```

will output

```yaml
0: a
1: b
```

## Use with\_entries to update keys

Given a sample.yml file of:

```yaml
a: 1
b: 2
```

then

```bash
yq 'with_entries(.key |= "KEY_" + .)' sample.yml
```

will output

```yaml
KEY_a: 1
KEY_b: 2
```

## Use with\_entries to update keys recursively

We use (.. | select(tag="map")) to find all the maps in the doc, then |= to update each one of those maps. In the update, with\_entries is used.

Given a sample.yml file of:

```yaml
a: 1
b:
  b_a: nested
  b_b: thing
```

then

```bash
yq '(.. | select(tag=="!!map")) |= with_entries(.key |= "KEY_" + .)' sample.yml
```

will output

```yaml
KEY_a: 1
KEY_b:
  KEY_b_a: nested
  KEY_b_b: thing
```

## Custom sort map keys

Use to\_entries to convert to an array of key/value pairs, sort the array using sort/sort\_by/etc, and convert it back.

Given a sample.yml file of:

```yaml
a: 1
c: 3
b: 2
```

then

```bash
yq 'to_entries | sort_by(.key) | reverse | from_entries' sample.yml
```

will output

```yaml
c: 3
b: 2
a: 1
```

## Use with\_entries to filter the map

Given a sample.yml file of:

```yaml
a:
  b: bird
c:
  d: dog
```

then

```bash
yq 'with_entries(select(.value | has("b")))' sample.yml
```

will output

```yaml
a:
  b: bird
```


# Env Variable Operators

These operators are used to handle environment variables usage in expressions and documents. While environment variables can, of course, be passed in via your CLI with string interpolation, this often comes with complex quote escaping and can be tricky to write and read.

There are three operators:

* `env` which takes a single environment variable name and parse the variable as a yaml node (be it a map, array, string, number of boolean)
* `strenv` which also takes a single environment variable name, and always parses the variable as a string.
* `envsubst` which you pipe strings into and it interpolates environment variables in strings using [envsubst](https://github.com/a8m/envsubst).

## EnvSubst Options

You can optionally pass envsubst any of the following options:

* nu: NoUnset, this will fail if there are any referenced variables that are not set
* ne: NoEmpty, this will fail if there are any referenced variables that are empty
* ff: FailFast, this will abort on the first failure (rather than collect all the errors)

E.g: `envsubst(ne, ff)` will fail on the first empty variable.

See [Imposing Restrictions](https://github.com/a8m/envsubst#imposing-restrictions) in the `envsubst` documentation for more information, and below for examples.

## Tip

To replace environment variables across all values in a document, `envsubst` can be used with the recursive descent operator as follows:

```bash
yq '(.. | select(tag == "!!str")) |= envsubst' file.yaml
```

## Disabling env operators

If required, you can use the `--security-disable-env-ops` to disable env operations.

## Read string environment variable

Running

```bash
myenv="cat meow" yq --null-input '.a = env(myenv)'
```

will output

```yaml
a: cat meow
```

## Read boolean environment variable

Running

```bash
myenv="true" yq --null-input '.a = env(myenv)'
```

will output

```yaml
a: true
```

## Read numeric environment variable

Running

```bash
myenv="12" yq --null-input '.a = env(myenv)'
```

will output

```yaml
a: 12
```

## Read yaml environment variable

Running

```bash
myenv="{b: fish}" yq --null-input '.a = env(myenv)'
```

will output

```yaml
a: {b: fish}
```

## Read boolean environment variable as a string

Running

```bash
myenv="true" yq --null-input '.a = strenv(myenv)'
```

will output

```yaml
a: "true"
```

## Read numeric environment variable as a string

Running

```bash
myenv="12" yq --null-input '.a = strenv(myenv)'
```

will output

```yaml
a: "12"
```

## Dynamically update a path from an environment variable

The env variable can be any valid yq expression.

Given a sample.yml file of:

```yaml
a:
  b:
    - name: dog
    - name: cat
```

then

```bash
pathEnv=".a.b[0].name"  valueEnv="moo" yq 'eval(strenv(pathEnv)) = strenv(valueEnv)' sample.yml
```

will output

```yaml
a:
  b:
    - name: moo
    - name: cat
```

## Dynamic key lookup with environment variable

Given a sample.yml file of:

```yaml
cat: meow
dog: woof
```

then

```bash
myenv="cat" yq '.[env(myenv)]' sample.yml
```

will output

```yaml
meow
```

## Replace strings with envsubst

Running

```bash
myenv="cat" yq --null-input '"the ${myenv} meows" | envsubst'
```

will output

```yaml
the cat meows
```

## Replace strings with envsubst, missing variables

Running

```bash
yq --null-input '"the ${myenvnonexisting} meows" | envsubst'
```

will output

```yaml
the  meows
```

## Replace strings with envsubst(nu), missing variables

(nu) not unset, will fail if there are unset (missing) variables

Running

```bash
yq --null-input '"the ${myenvnonexisting} meows" | envsubst(nu)'
```

will output

```bash
Error: variable ${myenvnonexisting} not set
```

## Replace strings with envsubst(ne), missing variables

(ne) not empty, only validates set variables

Running

```bash
yq --null-input '"the ${myenvnonexisting} meows" | envsubst(ne)'
```

will output

```yaml
the  meows
```

## Replace strings with envsubst(ne), empty variable

(ne) not empty, will fail if a references variable is empty

Running

```bash
myenv="" yq --null-input '"the ${myenv} meows" | envsubst(ne)'
```

will output

```bash
Error: variable ${myenv} set but empty
```

## Replace strings with envsubst, missing variables with defaults

Running

```bash
yq --null-input '"the ${myenvnonexisting-dog} meows" | envsubst'
```

will output

```yaml
the dog meows
```

## Replace strings with envsubst(nu), missing variables with defaults

Having a default specified skips over the missing variable.

Running

```bash
yq --null-input '"the ${myenvnonexisting-dog} meows" | envsubst(nu)'
```

will output

```yaml
the dog meows
```

## Replace strings with envsubst(ne), missing variables with defaults

Fails, because the variable is explicitly set to blank.

Running

```bash
myEmptyEnv="" yq --null-input '"the ${myEmptyEnv-dog} meows" | envsubst(ne)'
```

will output

```bash
Error: variable ${myEmptyEnv} set but empty
```

## Replace string environment variable in document

Given a sample.yml file of:

```yaml
v: ${myenv}
```

then

```bash
myenv="cat meow" yq '.v |= envsubst' sample.yml
```

will output

```yaml
v: cat meow
```

## (Default) Return all envsubst errors

By default, all errors are returned at once.

Running

```bash
yq --null-input '"the ${notThere} ${alsoNotThere}" | envsubst(nu)'
```

will output

```bash
Error: variable ${notThere} not set
variable ${alsoNotThere} not set
```

## Fail fast, return the first envsubst error (and abort)

Running

```bash
yq --null-input '"the ${notThere} ${alsoNotThere}" | envsubst(nu,ff)'
```

will output

```bash
Error: variable ${notThere} not set
```

## env() operation fails when security is enabled

Use `--security-disable-env-ops` to disable env operations for security.

Running

```bash
yq --null-input 'env("MYENV")'
```

will output

```bash
Error: env operations have been disabled
```

## strenv() operation fails when security is enabled

Use `--security-disable-env-ops` to disable env operations for security.

Running

```bash
yq --null-input 'strenv("MYENV")'
```

will output

```bash
Error: env operations have been disabled
```

## envsubst() operation fails when security is enabled

Use `--security-disable-env-ops` to disable env operations for security.

Running

```bash
yq --null-input '"value: ${MYENV}" | envsubst'
```

will output

```bash
Error: env operations have been disabled
```


# Equals

This is a boolean operator that will return `true` if the LHS is equal to the RHS and `false` otherwise.

```
.a == .b
```

It is most often used with the select operator to find particular nodes:

```
select(.a == .b)
```

The not equals `!=` operator returns `false` if the LHS is equal to the RHS.

## Related Operators

* comparison (`>=`, `<` etc) operators [here](https://mikefarah.gitbook.io/yq/operators/compare)
* boolean operators (`and`, `or`, `any` etc) [here](https://mikefarah.gitbook.io/yq/operators/boolean-operators)
* select operator [here](https://mikefarah.gitbook.io/yq/operators/select)

## Match string

Given a sample.yml file of:

```yaml
- cat
- goat
- dog
```

then

```bash
yq '.[] | (. == "*at")' sample.yml
```

will output

```yaml
true
true
false
```

## Don't match string

Given a sample.yml file of:

```yaml
- cat
- goat
- dog
```

then

```bash
yq '.[] | (. != "*at")' sample.yml
```

will output

```yaml
false
false
true
```

## Match number

Given a sample.yml file of:

```yaml
- 3
- 4
- 5
```

then

```bash
yq '.[] | (. == 4)' sample.yml
```

will output

```yaml
false
true
false
```

## Don't match number

Given a sample.yml file of:

```yaml
- 3
- 4
- 5
```

then

```bash
yq '.[] | (. != 4)' sample.yml
```

will output

```yaml
true
false
true
```

## Match nulls

Running

```bash
yq --null-input 'null == ~'
```

will output

```yaml
true
```

## Non existent key doesn't equal a value

Given a sample.yml file of:

```yaml
a: frog
```

then

```bash
yq 'select(.b != "thing")' sample.yml
```

will output

```yaml
a: frog
```

## Two non existent keys are equal

Given a sample.yml file of:

```yaml
a: frog
```

then

```bash
yq 'select(.b == .c)' sample.yml
```

will output

```yaml
a: frog
```


# Eval

Use `eval` to dynamically process an expression - for instance from an environment variable.

`eval` takes a single argument, and evaluates that as a `yq` expression. Any valid expression can be used, be it a path `.a.b.c | select(. == "cat")`, or an update `.a.b.c = "gogo"`.

Tip: This can be a useful way to parameterise complex scripts.

## Dynamically evaluate a path

Given a sample.yml file of:

```yaml
pathExp: .a.b[] | select(.name == "cat")
a:
  b:
    - name: dog
    - name: cat
```

then

```bash
yq 'eval(.pathExp)' sample.yml
```

will output

```yaml
name: cat
```

## Dynamically update a path from an environment variable

The env variable can be any valid yq expression.

Given a sample.yml file of:

```yaml
a:
  b:
    - name: dog
    - name: cat
```

then

```bash
pathEnv=".a.b[0].name"  valueEnv="moo" yq 'eval(strenv(pathEnv)) = strenv(valueEnv)' sample.yml
```

will output

```yaml
a:
  b:
    - name: moo
    - name: cat
```


# File Operators

File operators are most often used with merge when needing to merge specific files together. Note that when doing this, you will need to use `eval-all` to ensure all yaml documents are loaded into memory before performing the merge (as opposed to `eval` which runs the expression once per document).

Note that the `fileIndex` operator has a short alias of `fi`.

## Merging files

Note the use of eval-all to ensure all documents are loaded into memory.

```bash
yq eval-all 'select(fi == 0) * select(filename == "file2.yaml")' file1.yaml file2.yaml
```

## Get filename

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq 'filename' sample.yml
```

will output

```yaml
sample.yml
```

## Get file index

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq 'file_index' sample.yml
```

will output

```yaml
0
```

## Get file indices of multiple documents

Given a sample.yml file of:

```yaml
a: cat
```

And another sample another.yml file of:

```yaml
a: cat
```

then

```bash
yq eval-all 'file_index' sample.yml another.yml
```

will output

```yaml
0
1
```

## Get file index alias

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq 'fi' sample.yml
```

will output

```yaml
0
```


# Filter Operator

Filters an array (or map values) by the expression given. Equivalent to doing `map(select(exp))`.

## Filter array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq 'filter(. < 3)' sample.yml
```

will output

```yaml
- 1
- 2
```

## Filter map values

Given a sample.yml file of:

```yaml
c:
  things: cool
  frog: yes
d:
  things: hot
  frog: false
```

then

```bash
yq 'filter(.things == "cool")' sample.yml
```

will output

```yaml
- things: cool
  frog: yes
```


# First Operator

Returns the first matching element in an array, or first matching value in a map.

Can be given an expression to match with, otherwise will just return the first.

## First matching element from array

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'first(.a == "cat")' sample.yml
```

will output

```yaml
a: cat
```

## First matching element from array with multiple matches

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
  b: firstCat
- a: apple
- a: cat
  b: secondCat
```

then

```bash
yq 'first(.a == "cat")' sample.yml
```

will output

```yaml
a: cat
b: firstCat
```

## First matching element from array with numeric condition

Given a sample.yml file of:

```yaml
- a: 10
- a: 100
- a: 1
- a: 101
```

then

```bash
yq 'first(.a > 50)' sample.yml
```

will output

```yaml
a: 100
```

## First matching element from array with boolean condition

Given a sample.yml file of:

```yaml
- a: false
- a: true
  b: firstTrue
- a: false
- a: true
  b: secondTrue
```

then

```bash
yq 'first(.a == true)' sample.yml
```

will output

```yaml
a: true
b: firstTrue
```

## First matching element from array with null values

Given a sample.yml file of:

```yaml
- a: null
- a: cat
- a: apple
```

then

```bash
yq 'first(.a != null)' sample.yml
```

will output

```yaml
a: cat
```

## First matching element from array with complex condition

Given a sample.yml file of:

```yaml
- a: dog
  b: 7
- a: cat
  b: 3
- a: apple
  b: 5
```

then

```bash
yq 'first(.b > 4 and .b < 6)' sample.yml
```

will output

```yaml
a: apple
b: 5
```

## First matching element from map

Given a sample.yml file of:

```yaml
x:
  a: banana
y:
  a: cat
z:
  a: apple
```

then

```bash
yq 'first(.a == "cat")' sample.yml
```

will output

```yaml
a: cat
```

## First matching element from map with numeric condition

Given a sample.yml file of:

```yaml
x:
  a: 10
y:
  a: 100
z:
  a: 101
```

then

```bash
yq 'first(.a > 50)' sample.yml
```

will output

```yaml
a: 100
```

## First matching element from nested structure

Given a sample.yml file of:

```yaml
items:
  - a: banana
  - a: cat
  - a: apple
```

then

```bash
yq '.items | first(.a == "cat")' sample.yml
```

will output

```yaml
a: cat
```

## First matching element with no matches

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'first(.a == "dog")' sample.yml
```

will output

```yaml
```

## First matching element from empty array

Given a sample.yml file of:

```yaml
[]
```

then

```bash
yq 'first(.a == "cat")' sample.yml
```

will output

```yaml
```

## First matching element from scalar node

Given a sample.yml file of:

```yaml
hello
```

then

```bash
yq 'first(. == "hello")' sample.yml
```

will output

```yaml
```

## First matching element from null node

Given a sample.yml file of:

```yaml
null
```

then

```bash
yq 'first(. == "hello")' sample.yml
```

will output

```yaml
```

## First matching element with string condition

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'first(.a | test("^c"))' sample.yml
```

will output

```yaml
a: cat
```

## First matching element with length condition

Given a sample.yml file of:

```yaml
- a: hi
- a: hello
- a: world
```

then

```bash
yq 'first(.a | length > 4)' sample.yml
```

will output

```yaml
a: hello
```

## First matching element from array of strings

Given a sample.yml file of:

```yaml
- banana
- cat
- apple
```

then

```bash
yq 'first(. == "cat")' sample.yml
```

will output

```yaml
cat
```

## First matching element from array of numbers

Given a sample.yml file of:

```yaml
- 10
- 100
- 1
```

then

```bash
yq 'first(. > 50)' sample.yml
```

will output

```yaml
100
```

## First element with no filter from array

Given a sample.yml file of:

```yaml
- 10
- 100
- 1
```

then

```bash
yq 'first' sample.yml
```

will output

```yaml
10
```

## First element with no filter from array of maps

Given a sample.yml file of:

```yaml
- a: 10
- a: 100
```

then

```bash
yq 'first' sample.yml
```

will output

```yaml
a: 10
```


# Flatten

This recursively flattens arrays.

## Flatten

Recursively flattens all arrays

Given a sample.yml file of:

```yaml
- 1
- - 2
- - - 3
```

then

```bash
yq 'flatten' sample.yml
```

will output

```yaml
- 1
- 2
- 3
```

## Flatten with depth of one

Given a sample.yml file of:

```yaml
- 1
- - 2
- - - 3
```

then

```bash
yq 'flatten(1)' sample.yml
```

will output

```yaml
- 1
- 2
- - 3
```

## Flatten empty array

Given a sample.yml file of:

```yaml
- []
```

then

```bash
yq 'flatten' sample.yml
```

will output

```yaml
[]
```

## Flatten array of objects

Given a sample.yml file of:

```yaml
- foo: bar
- - foo: baz
```

then

```bash
yq 'flatten' sample.yml
```

will output

```yaml
- foo: bar
- foo: baz
```


# Group By

This is used to group items in an array by an expression.

## Group by field

Given a sample.yml file of:

```yaml
- foo: 1
  bar: 10
- foo: 3
  bar: 100
- foo: 1
  bar: 1
```

then

```bash
yq 'group_by(.foo)' sample.yml
```

will output

```yaml
- - foo: 1
    bar: 10
  - foo: 1
    bar: 1
- - foo: 3
    bar: 100
```

## Group by field, with nulls

Given a sample.yml file of:

```yaml
- cat: dog
- foo: 1
  bar: 10
- foo: 3
  bar: 100
- no: foo for you
- foo: 1
  bar: 1
```

then

```bash
yq 'group_by(.foo)' sample.yml
```

will output

```yaml
- - cat: dog
  - no: foo for you
- - foo: 1
    bar: 10
  - foo: 1
    bar: 1
- - foo: 3
    bar: 100
```


# Has

This operation returns true if the key exists in a map (or index in an array), false otherwise.

## Has map key

Given a sample.yml file of:

```yaml
- a: yes
- a: ~
- a:
- b: nope
```

then

```bash
yq '.[] | has("a")' sample.yml
```

will output

```yaml
true
true
true
false
```

## Select, checking for existence of deep paths

Simply pipe in parent expressions into `has`

Given a sample.yml file of:

```yaml
- a:
    b:
      c: cat
- a:
    b:
      d: dog
```

then

```bash
yq '.[] | select(.a.b | has("c"))' sample.yml
```

will output

```yaml
a:
  b:
    c: cat
```

## Has array index

Given a sample.yml file of:

```yaml
- []
- [1]
- [1, 2]
- [1, null]
- [1, 2, 3]

```

then

```bash
yq '.[] | has(1)' sample.yml
```

will output

```yaml
false
false
true
true
true
```


# Keys

Use the `keys` operator to return map keys or array indices.

## Map keys

Given a sample.yml file of:

```yaml
dog: woof
cat: meow
```

then

```bash
yq 'keys' sample.yml
```

will output

```yaml
- dog
- cat
```

## Array keys

Given a sample.yml file of:

```yaml
- apple
- banana
```

then

```bash
yq 'keys' sample.yml
```

will output

```yaml
- 0
- 1
```

## Retrieve array key

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq '.[1] | key' sample.yml
```

will output

```yaml
1
```

## Retrieve map key

Given a sample.yml file of:

```yaml
a: thing
```

then

```bash
yq '.a | key' sample.yml
```

will output

```yaml
a
```

## No key

Given a sample.yml file of:

```yaml
{}
```

then

```bash
yq 'key' sample.yml
```

will output

```yaml
```

## Update map key

Given a sample.yml file of:

```yaml
a:
  x: 3
  y: 4
```

then

```bash
yq '(.a.x | key) = "meow"' sample.yml
```

will output

```yaml
a:
  meow: 3
  y: 4
```

## Get comment from map key

Given a sample.yml file of:

```yaml
a:
  # comment on key
  x: 3
  y: 4
```

then

```bash
yq '.a.x | key | headComment' sample.yml
```

will output

```yaml
comment on key
```

## Check node is a key

Given a sample.yml file of:

```yaml
a:
  b:
    - cat
  c: frog
```

then

```bash
yq '[... | { "p": path | join("."), "isKey": is_key, "tag": tag }]' sample.yml
```

will output

```yaml
- p: ""
  isKey: false
  tag: '!!map'
- p: a
  isKey: true
  tag: '!!str'
- p: a
  isKey: false
  tag: '!!map'
- p: a.b
  isKey: true
  tag: '!!str'
- p: a.b
  isKey: false
  tag: '!!seq'
- p: a.b.0
  isKey: false
  tag: '!!str'
- p: a.c
  isKey: true
  tag: '!!str'
- p: a.c
  isKey: false
  tag: '!!str'
```


# Kind

The `kind` operator identifies the type of a node as either `scalar`, `map`, or `seq`.

This can be used for filtering or transforming nodes based on their type.

Note that `null` values are treated as `scalar`.

## Get kind

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f: []
g: {}
h: null
```

then

```bash
yq '.. | kind' sample.yml
```

will output

```yaml
map
scalar
scalar
scalar
scalar
seq
map
scalar
```

## Get kind, ignores custom tags

Unlike tag, kind is not affected by custom tags.

Given a sample.yml file of:

```yaml
a: !!thing cat
b: !!foo {}
c: !!bar []
```

then

```bash
yq '.. | kind' sample.yml
```

will output

```yaml
map
scalar
map
seq
```

## Add comments only to scalars

An example of how you can use kind

Given a sample.yml file of:

```yaml
a:
  b: 5
  c: 3.2
e: true
f: []
g: {}
h: null
```

then

```bash
yq '(.. | select(kind == "scalar")) line_comment = "this is a scalar"' sample.yml
```

will output

```yaml
a:
  b: 5 # this is a scalar
  c: 3.2 # this is a scalar
e: true # this is a scalar
f: []
g: {}
h: null # this is a scalar
```


# Length

Returns the lengths of the nodes. Length is defined according to the type of the node.

## String length

returns length of string

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a | length' sample.yml
```

will output

```yaml
3
```

## null length

Given a sample.yml file of:

```yaml
a: null
```

then

```bash
yq '.a | length' sample.yml
```

will output

```yaml
0
```

## Map length

returns number of entries

Given a sample.yml file of:

```yaml
a: cat
c: dog
```

then

```bash
yq 'length' sample.yml
```

will output

```yaml
2
```

## Array length

returns number of elements

Given a sample.yml file of:

```yaml
- 2
- 4
- 6
- 8
```

then

```bash
yq 'length' sample.yml
```

will output

```yaml
4
```


# Line

Returns the line of the matching node. Starts from 1, 0 indicates there was no line data.

## Returns line of *value* node

Given a sample.yml file of:

```yaml
a: cat
b:
  c: cat
```

then

```bash
yq '.b | line' sample.yml
```

will output

```yaml
3
```

## Returns line of *key* node

Pipe through the key operator to get the line of the key

Given a sample.yml file of:

```yaml
a: cat
b:
  c: cat
```

then

```bash
yq '.b | key | line' sample.yml
```

will output

```yaml
2
```

## First line is 1

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a | line' sample.yml
```

will output

```yaml
1
```

## No line data is 0

Running

```bash
yq --null-input '{"a": "new entry"} | line'
```

will output

```yaml
0
```


# Load

The load operators allows you to load in content from another file.

Note that you can use string operators like `+` and `sub` to modify the value in the yaml file to a path that exists in your system.

You can load files of the following supported types:

| Format       | Load Operator |
| ------------ | ------------- |
| Yaml         | load          |
| XML          | load\_xml     |
| Properties   | load\_props   |
| Plain String | load\_str     |
| Base64       | load\_base64  |

Note that load\_base64 only works for base64 encoded utf-8 strings.

## Samples files for tests:

### yaml

`../../examples/thing.yml`:

```yaml
a: apple is included
b: cool
```

### xml

`small.xml`:

```xml
<this>is some xml</this>
```

### properties

`small.properties`:

```properties
this.is = a properties file
```

### base64

`base64.txt`:

```
bXkgc2VjcmV0IGNoaWxsaSByZWNpcGUgaXMuLi4u
```

## Disabling file operators

If required, you can use the `--security-disable-file-ops` to disable file operations.

## Simple example

Given a sample.yml file of:

```yaml
myFile: ../../examples/thing.yml
```

then

```bash
yq 'load(.myFile)' sample.yml
```

will output

```yaml
a: apple is included
b: cool.
```

## Replace node with referenced file

Note that you can modify the filename in the load operator if needed.

Given a sample.yml file of:

```yaml
something:
  file: thing.yml
```

then

```bash
yq '.something |= load("../../examples/" + .file)' sample.yml
```

will output

```yaml
something:
  a: apple is included
  b: cool.
```

## Replace *all* nodes with referenced file

Recursively match all the nodes (`..`) and then filter the ones that have a 'file' attribute.

Given a sample.yml file of:

```yaml
something:
  file: thing.yml
over:
  here:
    - file: thing.yml
```

then

```bash
yq '(.. | select(has("file"))) |= load("../../examples/" + .file)' sample.yml
```

will output

```yaml
something:
  a: apple is included
  b: cool.
over:
  here:
    - a: apple is included
      b: cool.
```

## Replace node with referenced file as string

This will work for any text based file

Given a sample.yml file of:

```yaml
something:
  file: thing.yml
```

then

```bash
yq '.something |= load_str("../../examples/" + .file)' sample.yml
```

will output

```yaml
something: |-
  a: apple is included
  b: cool.
```

## Load from XML

Given a sample.yml file of:

```yaml
cool: things
```

then

```bash
yq '.more_stuff = load_xml("../../examples/small.xml")' sample.yml
```

will output

```yaml
cool: things
more_stuff:
  this: is some xml
```

## Load from Properties

Given a sample.yml file of:

```yaml
cool: things
```

then

```bash
yq '.more_stuff = load_props("../../examples/small.properties")' sample.yml
```

will output

```yaml
cool: things
more_stuff:
  this:
    is: a properties file
```

## Merge from properties

This can be used as a convenient way to update a yaml document

Given a sample.yml file of:

```yaml
this:
  is: from yaml
  cool: ay
```

then

```bash
yq '. *= load_props("../../examples/small.properties")' sample.yml
```

will output

```yaml
this:
  is: a properties file
  cool: ay
```

## Load from base64 encoded file

Given a sample.yml file of:

```yaml
cool: things
```

then

```bash
yq '.more_stuff = load_base64("../../examples/base64.txt")' sample.yml
```

will output

```yaml
cool: things
more_stuff: my secret chilli recipe is....
```

## load() operation fails when security is enabled

Use `--security-disable-file-ops` to disable file operations for security.

Running

```bash
yq --null-input 'load("../../examples/thing.yml")'
```

will output

```bash
Error: file operations have been disabled
```

## load\_str() operation fails when security is enabled

Use `--security-disable-file-ops` to disable file operations for security.

Running

```bash
yq --null-input 'load_str("../../examples/thing.yml")'
```

will output

```bash
Error: file operations have been disabled
```

## load\_xml() operation fails when security is enabled

Use `--security-disable-file-ops` to disable file operations for security.

Running

```bash
yq --null-input 'load_xml("../../examples/small.xml")'
```

will output

```bash
Error: file operations have been disabled
```

## load\_props() operation fails when security is enabled

Use `--security-disable-file-ops` to disable file operations for security.

Running

```bash
yq --null-input 'load_props("../../examples/small.properties")'
```

will output

```bash
Error: file operations have been disabled
```

## load\_base64() operation fails when security is enabled

Use `--security-disable-file-ops` to disable file operations for security.

Running

```bash
yq --null-input 'load_base64("../../examples/base64.txt")'
```

will output

```bash
Error: file operations have been disabled
```


# Min

Computes the minimum among an incoming sequence of scalar values.

## Minimum int

Given a sample.yml file of:

```yaml
- 99
- 16
- 12
- 6
- 66
```

then

```bash
yq 'min' sample.yml
```

will output

```yaml
6
```

## Minimum string

Given a sample.yml file of:

```yaml
- foo
- bar
- baz
```

then

```bash
yq 'min' sample.yml
```

will output

```yaml
bar
```

## Minimum of empty

Given a sample.yml file of:

```yaml
[]
```

then

```bash
yq 'min' sample.yml
```

will output

```yaml
```


# Map

Maps values of an array. Use `map_values` to map values of an object.

## Map array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq 'map(. + 1)' sample.yml
```

will output

```yaml
- 2
- 3
- 4
```

## Map object values

Given a sample.yml file of:

```yaml
a: 1
b: 2
c: 3
```

then

```bash
yq 'map_values(. + 1)' sample.yml
```

will output

```yaml
a: 2
b: 3
c: 4
```


# Max

Computes the maximum among an incoming sequence of scalar values.

## Maximum int

Given a sample.yml file of:

```yaml
- 99
- 16
- 12
- 6
- 66
```

then

```bash
yq 'max' sample.yml
```

will output

```yaml
99
```

## Maximum string

Given a sample.yml file of:

```yaml
- foo
- bar
- baz
```

then

```bash
yq 'max' sample.yml
```

will output

```yaml
foo
```

## Maximum of empty

Given a sample.yml file of:

```yaml
[]
```

then

```bash
yq 'max' sample.yml
```

will output

```yaml
```


# Modulo

Arithmetic modulo operator, returns the remainder from dividing two numbers.

## Number modulo - int

If the lhs and rhs are ints then the expression will be calculated with ints.

Given a sample.yml file of:

```yaml
a: 13
b: 2
```

then

```bash
yq '.a = .a % .b' sample.yml
```

will output

```yaml
a: 1
b: 2
```

## Number modulo - float

If the lhs or rhs are floats then the expression will be calculated with floats.

Given a sample.yml file of:

```yaml
a: 12
b: 2.5
```

then

```bash
yq '.a = .a % .b' sample.yml
```

will output

```yaml
a: !!float 2
b: 2.5
```

## Number modulo - int by zero

If the lhs is an int and rhs is a 0 the result is an error.

Given a sample.yml file of:

```yaml
a: 1
b: 0
```

then

```bash
yq '.a = .a % .b' sample.yml
```

will output

```bash
Error: cannot modulo by 0
```

## Number modulo - float by zero

If the lhs is a float and rhs is a 0 the result is NaN.

Given a sample.yml file of:

```yaml
a: 1.1
b: 0
```

then

```bash
yq '.a = .a % .b' sample.yml
```

will output

```yaml
a: !!float NaN
b: 0
```


# Multiply (Merge)

## Multiply (Merge)

Like the multiple operator in jq, depending on the operands, this multiply operator will do different things. Currently numbers, arrays and objects are supported.

### Objects and arrays - merging

Objects are merged *deeply* matching on matching keys. By default, array values override and are not deeply merged.

You can use the add operator `+`, to shallow merge objects, see more info [here](https://mikefarah.gitbook.io/yq/operators/add).

Note that when merging objects, this operator returns the merged object (not the parent). This will be clearer in the examples below.

#### Merge Flags

You can control how objects are merged by using one or more of the following flags. Multiple flags can be used together, e.g. `.a *+? .b`. See examples below

* `+` append arrays
* `d` deeply merge arrays
* `?` only merge *existing* fields
* `n` only merge *new* fields
* `c` clobber custom tags

To perform a shallow merge only, use the add operator `+`, see more info [here](https://mikefarah.gitbook.io/yq/operators/add).

#### Merge two files together

This uses the load operator to merge file2 into file1.

```bash
yq '. *= load("file2.yml")' file1.yml
```

#### Merging all files

Note the use of `eval-all` to ensure all documents are loaded into memory.

```bash
yq eval-all '. as $item ireduce ({}; . * $item )' *.yml
```

## Merging complex arrays together by a key field

By default - `yq` merge is naive. It merges maps when they match the key name, and arrays are merged either by appending them together, or merging the entries by their position in the array.

For more complex array merging (e.g. merging items that match on a certain key) please see the example [here](https://mikefarah.gitbook.io/yq/operators/multiply-merge#merge-arrays-of-objects-together-matching-on-a-key)

### Multiply integers

Given a sample.yml file of:

```yaml
a: 3
b: 4
```

then

```bash
yq '.a *= .b' sample.yml
```

will output

```yaml
a: 12
b: 4
```

### Multiply string node X int

Given a sample.yml file of:

```yaml
b: banana
```

then

```bash
yq '.b * 4' sample.yml
```

will output

```yaml
bananabananabananabanana
```

### Multiply int X string node

Given a sample.yml file of:

```yaml
b: banana
```

then

```bash
yq '4 * .b' sample.yml
```

will output

```yaml
bananabananabananabanana
```

### Multiply string X int node

Given a sample.yml file of:

```yaml
n: 4
```

then

```bash
yq '"banana" * .n' sample.yml
```

will output

```yaml
bananabananabananabanana
```

### Multiply int node X string

Given a sample.yml file of:

```yaml
n: 4
```

then

```bash
yq '.n * "banana"' sample.yml
```

will output

```yaml
bananabananabananabanana
```

### Merge objects together, returning merged result only

Given a sample.yml file of:

```yaml
a:
  field: me
  fieldA: cat
b:
  field:
    g: wizz
  fieldB: dog
```

then

```bash
yq '.a * .b' sample.yml
```

will output

```yaml
field:
  g: wizz
fieldA: cat
fieldB: dog
```

### Merge objects together, returning parent object

Given a sample.yml file of:

```yaml
a:
  field: me
  fieldA: cat
b:
  field:
    g: wizz
  fieldB: dog
```

then

```bash
yq '. * {"a":.b}' sample.yml
```

will output

```yaml
a:
  field:
    g: wizz
  fieldA: cat
  fieldB: dog
b:
  field:
    g: wizz
  fieldB: dog
```

### Merge keeps style of LHS

Given a sample.yml file of:

```yaml
a: {things: great}
b:
  also: "me"
```

then

```bash
yq '. * {"a":.b}' sample.yml
```

will output

```yaml
a: {things: great, also: "me"}
b:
  also: "me"
```

### Merge arrays

Given a sample.yml file of:

```yaml
a:
  - 1
  - 2
  - 3
b:
  - 3
  - 4
  - 5
```

then

```bash
yq '. * {"a":.b}' sample.yml
```

will output

```yaml
a:
  - 3
  - 4
  - 5
b:
  - 3
  - 4
  - 5
```

### Merge, only existing fields

Given a sample.yml file of:

```yaml
a:
  thing: one
  cat: frog
b:
  missing: two
  thing: two
```

then

```bash
yq '.a *? .b' sample.yml
```

will output

```yaml
thing: two
cat: frog
```

### Merge, only new fields

Given a sample.yml file of:

```yaml
a:
  thing: one
  cat: frog
b:
  missing: two
  thing: two
```

then

```bash
yq '.a *n .b' sample.yml
```

will output

```yaml
thing: one
cat: frog
missing: two
```

### Merge, appending arrays

Given a sample.yml file of:

```yaml
a:
  array:
    - 1
    - 2
    - animal: dog
  value: coconut
b:
  array:
    - 3
    - 4
    - animal: cat
  value: banana
```

then

```bash
yq '.a *+ .b' sample.yml
```

will output

```yaml
array:
  - 1
  - 2
  - animal: dog
  - 3
  - 4
  - animal: cat
value: banana
```

### Merge, only existing fields, appending arrays

Given a sample.yml file of:

```yaml
a:
  thing:
    - 1
    - 2
b:
  thing:
    - 3
    - 4
  another:
    - 1
```

then

```bash
yq '.a *?+ .b' sample.yml
```

will output

```yaml
thing:
  - 1
  - 2
  - 3
  - 4
```

### Merge, deeply merging arrays

Merging arrays deeply means arrays are merged like objects, with indices as their key. In this case, we merge the first item in the array and do nothing with the second.

Given a sample.yml file of:

```yaml
a:
  - name: fred
    age: 12
  - name: bob
    age: 32
b:
  - name: fred
    age: 34
```

then

```bash
yq '.a *d .b' sample.yml
```

will output

```yaml
- name: fred
  age: 34
- name: bob
  age: 32
```

### Merge arrays of objects together, matching on a key

This is a fairly complex expression - you can use it as is by providing the environment variables as seen in the example below.

It merges in the array provided in the second file into the first - matching on equal keys.

Explanation:

The approach, at a high level, is to reduce into a merged map (keyed by the unique key) and then convert that back into an array.

First the expression will create a map from the arrays keyed by the idPath, the unique field we want to merge by. The reduce operator is merging '({}; . \* $item )', so array elements with the matching key will be merged together.

Next, we convert the map back to an array, using reduce again, concatenating all the map values together.

Finally, we set the result of the merged array back into the first doc.

Thanks Kev from [stackoverflow](https://stackoverflow.com/a/70109529/1168223)

Given a sample.yml file of:

```yaml
myArray:
  - a: apple
    b: appleB
  - a: kiwi
    b: kiwiB
  - a: banana
    b: bananaB
something: else
```

And another sample another.yml file of:

```yaml
newArray:
  - a: banana
    c: bananaC
  - a: apple
    b: appleB2
  - a: dingo
    c: dingoC
```

then

```bash
idPath=".a"  originalPath=".myArray"  otherPath=".newArray" yq eval-all '
(
  (( (eval(strenv(originalPath)) + eval(strenv(otherPath)))  | .[] | {(eval(strenv(idPath))):  .}) as $item ireduce ({}; . * $item )) as $uniqueMap
  | ( $uniqueMap  | to_entries | .[]) as $item ireduce([]; . + $item.value)
) as $mergedArray
| select(fi == 0) | (eval(strenv(originalPath))) = $mergedArray
' sample.yml another.yml
```

will output

```yaml
myArray:
  - a: apple
    b: appleB2
  - a: kiwi
    b: kiwiB
  - a: banana
    b: bananaB
    c: bananaC
  - a: dingo
    c: dingoC
something: else
```

### Merge to prefix an element

Given a sample.yml file of:

```yaml
a: cat
b: dog
```

then

```bash
yq '. * {"a": {"c": .a}}' sample.yml
```

will output

```yaml
a:
  c: cat
b: dog
```

### Merge with simple aliases

Given a sample.yml file of:

```yaml
a: &cat
  c: frog
b:
  f: *cat
c:
  g: thongs
```

then

```bash
yq '.c * .b' sample.yml
```

will output

```yaml
g: thongs
f: *cat
```

### Merge copies anchor names

Given a sample.yml file of:

```yaml
a:
  c: &cat frog
b:
  f: *cat
c:
  g: thongs
```

then

```bash
yq '.c * .a' sample.yml
```

will output

```yaml
g: thongs
c: &cat frog
```

### Merge with merge anchors

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar * .foobarList' sample.yml
```

will output

```yaml
c: foobarList_c
!!merge <<:
  - *foo
  - *bar
thing: foobar_thing
b: foobarList_b
```

### Custom types: that are really numbers

When custom tags are encountered, yq will try to decode the underlying type.

Given a sample.yml file of:

```yaml
a: !horse 2
b: !goat 3
```

then

```bash
yq '.a = .a * .b' sample.yml
```

will output

```yaml
a: !horse 6
b: !goat 3
```

### Custom types: that are really maps

Custom tags will be maintained.

Given a sample.yml file of:

```yaml
a: !horse
  cat: meow
b: !goat
  dog: woof
```

then

```bash
yq '.a = .a * .b' sample.yml
```

will output

```yaml
a: !horse
  cat: meow
  dog: woof
b: !goat
  dog: woof
```

### Custom types: clobber tags

Use the `c` option to clobber custom tags. Note that the second tag is now used.

Given a sample.yml file of:

```yaml
a: !horse
  cat: meow
b: !goat
  dog: woof
```

then

```bash
yq '.a *=c .b' sample.yml
```

will output

```yaml
a: !goat
  cat: meow
  dog: woof
b: !goat
  dog: woof
```

### Merging a null with a map

Running

```bash
yq --null-input 'null * {"some": "thing"}'
```

will output

```yaml
some: thing
```

### Merging a map with null

Running

```bash
yq --null-input '{"some": "thing"} * null'
```

will output

```yaml
some: thing
```

### Merging a null with an array

Running

```bash
yq --null-input 'null * ["some"]'
```

will output

```yaml
- some
```

### Merging an array with null

Running

```bash
yq --null-input '["some"] * null'
```

will output

```yaml
- some
```


# Omit

Works like `pick`, but instead you specify the keys/indices that you *don't* want included.

## Omit keys from map

Note that non existent keys are skipped.

Given a sample.yml file of:

```yaml
myMap:
  cat: meow
  dog: bark
  thing: hamster
  hamster: squeak
```

then

```bash
yq '.myMap |= omit(["hamster", "cat", "goat"])' sample.yml
```

will output

```yaml
myMap:
  dog: bark
  thing: hamster
```

## Omit indices from array

Note that non existent indices are skipped.

Given a sample.yml file of:

```yaml
- cat
- leopard
- lion
```

then

```bash
yq 'omit([2, 0, 734, -5])' sample.yml
```

will output

```yaml
- leopard
```


# Parent

Parent simply returns the parent nodes of the matching nodes.

## Simple example

Given a sample.yml file of:

```yaml
a:
  nested: cat
```

then

```bash
yq '.a.nested | parent' sample.yml
```

will output

```yaml
nested: cat
```

## Parent of nested matches

Given a sample.yml file of:

```yaml
a:
  fruit: apple
  name: bob
b:
  fruit: banana
  name: sam
```

then

```bash
yq '.. | select(. == "banana") | parent' sample.yml
```

will output

```yaml
fruit: banana
name: sam
```

## Get parent attribute

Given a sample.yml file of:

```yaml
a:
  fruit: apple
  name: bob
b:
  fruit: banana
  name: sam
```

then

```bash
yq '.. | select(. == "banana") | parent.name' sample.yml
```

will output

```yaml
sam
```

## Get parents

Match all parents

Given a sample.yml file of:

```yaml
a:
  b:
    c: cat
```

then

```bash
yq '.a.b.c | parents' sample.yml
```

will output

```yaml
- c: cat
- b:
    c: cat
- a:
    b:
      c: cat
```

## N-th parent

You can optionally supply the number of levels to go up for the parent, the default being 1.

Given a sample.yml file of:

```yaml
a:
  b:
    c: cat
```

then

```bash
yq '.a.b.c | parent(2)' sample.yml
```

will output

```yaml
b:
  c: cat
```

## N-th parent - another level

Given a sample.yml file of:

```yaml
a:
  b:
    c: cat
```

then

```bash
yq '.a.b.c | parent(3)' sample.yml
```

will output

```yaml
a:
  b:
    c: cat
```

## No parent

Given a sample.yml file of:

```yaml
{}
```

then

```bash
yq 'parent' sample.yml
```

will output

```yaml
```


# Path

The `path` operator can be used to get the traversal paths of matching nodes in an expression. The path is returned as an array, which if traversed in order will lead to the matching node.

You can get the key/index of matching nodes by using the `path` operator to return the path array then piping that through `.[-1]` to get the last element of that array, the key.

Use `setpath` to set a value to the path array returned by `path`, and similarly `delpaths` for an array of path arrays.

## Map path

Given a sample.yml file of:

```yaml
a:
  b: cat
```

then

```bash
yq '.a.b | path' sample.yml
```

will output

```yaml
- a
- b
```

## Get map key

Given a sample.yml file of:

```yaml
a:
  b: cat
```

then

```bash
yq '.a.b | path | .[-1]' sample.yml
```

will output

```yaml
b
```

## Array path

Given a sample.yml file of:

```yaml
a:
  - cat
  - dog
```

then

```bash
yq '.a.[] | select(. == "dog") | path' sample.yml
```

will output

```yaml
- a
- 1
```

## Get array index

Given a sample.yml file of:

```yaml
a:
  - cat
  - dog
```

then

```bash
yq '.a.[] | select(. == "dog") | path | .[-1]' sample.yml
```

will output

```yaml
1
```

## Print path and value

Given a sample.yml file of:

```yaml
a:
  - cat
  - dog
  - frog
```

then

```bash
yq '.a[] | select(. == "*og") | [{"path":path, "value":.}]' sample.yml
```

will output

```yaml
- path:
    - a
    - 1
  value: dog
- path:
    - a
    - 2
  value: frog
```

## Set path

Given a sample.yml file of:

```yaml
a:
  b: cat
```

then

```bash
yq 'setpath(["a", "b"]; "things")' sample.yml
```

will output

```yaml
a:
  b: things
```

## Set on empty document

Running

```bash
yq --null-input 'setpath(["a", "b"]; "things")'
```

will output

```yaml
a:
  b: things
```

## Set path to prune deep paths

Like pick but recursive. This uses `ireduce` to deeply set the selected paths into an empty object.

Given a sample.yml file of:

```yaml

parentA: bob
parentB:
  child1: i am child1
  child2: i am child2
parentC:
  child1: me child1
  child2: me child2
```

then

```bash
yq '(.parentB.child2, .parentC.child1) as $i
  ireduce({}; setpath($i | path; $i))' sample.yml
```

will output

```yaml
parentB:
  child2: i am child2
parentC:
  child1: me child1
```

## Set array path

Given a sample.yml file of:

```yaml
a:
  - cat
  - frog
```

then

```bash
yq 'setpath(["a", 0]; "things")' sample.yml
```

will output

```yaml
a:
  - things
  - frog
```

## Set array path empty

Running

```bash
yq --null-input 'setpath(["a", 0]; "things")'
```

will output

```yaml
a:
  - things
```

## Delete path

Notice delpaths takes an *array* of paths.

Given a sample.yml file of:

```yaml
a:
  b: cat
  c: dog
  d: frog
```

then

```bash
yq 'delpaths([["a", "c"], ["a", "d"]])' sample.yml
```

will output

```yaml
a:
  b: cat
```

## Delete array path

Given a sample.yml file of:

```yaml
a:
  - cat
  - frog
```

then

```bash
yq 'delpaths([["a", 0]])' sample.yml
```

will output

```yaml
a:
  - frog
```

## Delete - wrong parameter

delpaths does not work with a single path array

Given a sample.yml file of:

```yaml
a:
  - cat
  - frog
```

then

```bash
yq 'delpaths(["a", 0])' sample.yml
```

will output

```bash
Error: DELPATHS: expected entry [0] to be a sequence, but its a !!str. Note that delpaths takes an array of path arrays, e.g. [["a", "b"]]
```


# Pick

Filter a map by the specified list of keys. Map is returned with the key in the order of the pick list.

Similarly, filter an array by the specified list of indices.

## Pick keys from map

Note that the order of the keys matches the pick order and non existent keys are skipped.

Given a sample.yml file of:

```yaml
myMap:
  cat: meow
  dog: bark
  thing: hamster
  hamster: squeak
```

then

```bash
yq '.myMap |= pick(["hamster", "cat", "goat"])' sample.yml
```

will output

```yaml
myMap:
  hamster: squeak
  cat: meow
```

## Pick keys from map, included all the keys

We create a map of the picked keys plus all the current keys, and run that through unique

Given a sample.yml file of:

```yaml
myMap:
  cat: meow
  dog: bark
  thing: hamster
  hamster: squeak
```

then

```bash
yq '.myMap |= pick( (["thing"] + keys) | unique)' sample.yml
```

will output

```yaml
myMap:
  thing: hamster
  cat: meow
  dog: bark
  hamster: squeak
```

## Pick indices from array

Note that the order of the indices matches the pick order and non existent indices are skipped.

Given a sample.yml file of:

```yaml
- cat
- leopard
- lion
```

then

```bash
yq 'pick([2, 0, 734, -5])' sample.yml
```

will output

```yaml
- lion
- cat
```


# Pipe

Pipe the results of an expression into another. Like the bash operator.

## Simple Pipe

Given a sample.yml file of:

```yaml
a:
  b: cat
```

then

```bash
yq '.a | .b' sample.yml
```

will output

```yaml
cat
```

## Multiple updates

Given a sample.yml file of:

```yaml
a: cow
b: sheep
c: same
```

then

```bash
yq '.a = "cat" | .b = "dog"' sample.yml
```

will output

```yaml
a: cat
b: dog
c: same
```


# Pivot

Emulates the `PIVOT` function supported by several popular RDBMS systems.

## Pivot a sequence of sequences

Given a sample.yml file of:

```yaml
- - foo
  - bar
  - baz
- - sis
  - boom
  - bah
```

then

```bash
yq 'pivot' sample.yml
```

will output

```yaml
- - foo
  - sis
- - bar
  - boom
- - baz
  - bah
```

## Pivot sequence of heterogeneous sequences

Missing values are "padded" to null.

Given a sample.yml file of:

```yaml
- - foo
  - bar
  - baz
- - sis
  - boom
  - bah
  - blah
```

then

```bash
yq 'pivot' sample.yml
```

will output

```yaml
- - foo
  - sis
- - bar
  - boom
- - baz
  - bah
- -
  - blah
```

## Pivot sequence of maps

Given a sample.yml file of:

```yaml
- foo: a
  bar: b
  baz: c
- foo: x
  bar: y
  baz: z
```

then

```bash
yq 'pivot' sample.yml
```

will output

```yaml
foo:
  - a
  - x
bar:
  - b
  - y
baz:
  - c
  - z
```

## Pivot sequence of heterogeneous maps

Missing values are "padded" to null.

Given a sample.yml file of:

```yaml
- foo: a
  bar: b
  baz: c
- foo: x
  bar: y
  baz: z
  what: ever
```

then

```bash
yq 'pivot' sample.yml
```

will output

```yaml
foo:
  - a
  - x
bar:
  - b
  - y
baz:
  - c
  - z
what:
  -
  - ever
```


# Recursive Descent (Glob)

This operator recursively matches (or globs) all children nodes given of a particular element, including that node itself. This is most often used to apply a filter recursively against all matches.

## match values form `..`

This will, like the `jq` equivalent, recursively match all *value* nodes. Use it to find/manipulate particular values.

For instance to set the `style` of all *value* nodes in a yaml doc, excluding map keys:

```bash
yq '.. style= "flow"' file.yaml
```

## match values and map keys form `...`

The also includes map keys in the results set. This is particularly useful in YAML as unlike JSON, map keys can have their own styling and tags and also use anchors and aliases.

For instance to set the `style` of all nodes in a yaml doc, including the map keys:

```bash
yq '... style= "flow"' file.yaml
```

## Recurse map (values only)

Given a sample.yml file of:

```yaml
a: frog
```

then

```bash
yq '..' sample.yml
```

will output

```yaml
a: frog
frog
```

## Recursively find nodes with keys

Note that this example has wrapped the expression in `[]` to show that there are two matches returned. You do not have to wrap in `[]` in your path expression.

Given a sample.yml file of:

```yaml
a:
  name: frog
  b:
    name: blog
    age: 12
```

then

```bash
yq '[.. | select(has("name"))]' sample.yml
```

will output

```yaml
- name: frog
  b:
    name: blog
    age: 12
- name: blog
  age: 12
```

## Recursively find nodes with values

Given a sample.yml file of:

```yaml
a:
  nameA: frog
  b:
    nameB: frog
    age: 12
```

then

```bash
yq '.. | select(. == "frog")' sample.yml
```

will output

```yaml
frog
frog
```

## Recurse map (values and keys)

Note that the map key appears in the results

Given a sample.yml file of:

```yaml
a: frog
```

then

```bash
yq '...' sample.yml
```

will output

```yaml
a: frog
a
frog
```

## Aliases are not traversed

Given a sample.yml file of:

```yaml
a: &cat
  c: frog
b: *cat
```

then

```bash
yq '[..]' sample.yml
```

will output

```yaml
- a: &cat
    c: frog
  b: *cat
- &cat
  c: frog
- frog
- *cat
```

## Merge docs are not traversed

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar | [..]' sample.yml
```

will output

```yaml
- c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
- foobar_c
- *foo
- foobar_thing
```


# Reduce

Reduce is a powerful way to process a collection of data into a new form.

```
<exp> as $<name> ireduce (<init>; <block>)
```

e.g.

```
.[] as $item ireduce (0; . + $item)
```

On the LHS we are configuring the collection of items that will be reduced `<exp>` as well as what each element will be called `$<name>`. Note that the array has been splatted into its individual elements.

On the RHS there is `<init>`, the starting value of the accumulator and `<block>`, the expression that will update the accumulator for each element in the collection. Note that within the block expression, `.` will evaluate to the current value of the accumulator.

## yq vs jq syntax

Reduce syntax in `yq` is a little different from `jq` - as `yq` (currently) isn't as sophisticated as `jq` and its only supports infix notation (e.g. a + b, where the operator is in the middle of the two parameters) - where as `jq` uses a mix of infix notation with *prefix* notation (e.g. `reduce a b` is like writing `+ a b`).

To that end, the reduce operator is called `ireduce` for backwards compatibility if a `jq` like prefix version of `reduce` is ever added.

## Sum numbers

Given a sample.yml file of:

```yaml
- 10
- 2
- 5
- 3
```

then

```bash
yq '.[] as $item ireduce (0; . + $item)' sample.yml
```

will output

```yaml
20
```

## Merge all yaml files together

Given a sample.yml file of:

```yaml
a: cat
```

And another sample another.yml file of:

```yaml
b: dog
```

then

```bash
yq eval-all '. as $item ireduce ({}; . * $item )' sample.yml another.yml
```

will output

```yaml
a: cat
b: dog
```

## Convert an array to an object

Given a sample.yml file of:

```yaml
- name: Cathy
  has: apples
- name: Bob
  has: bananas
```

then

```bash
yq '.[] as $item ireduce ({}; .[$item | .name] = ($item | .has) )' sample.yml
```

will output

```yaml
Cathy: apples
Bob: bananas
```


# Reverse

Reverses the order of the items in an array

## Reverse

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq 'reverse' sample.yml
```

will output

```yaml
- 3
- 2
- 1
```

## Sort descending by string field

Use sort with reverse to sort in descending order.

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'sort_by(.a) | reverse' sample.yml
```

will output

```yaml
- a: cat
- a: banana
- a: apple
```


# Select

Select is used to filter arrays and maps by a boolean expression.

## Related Operators

* equals / not equals (`==`, `!=`) operators [here](https://mikefarah.gitbook.io/yq/operators/equals)
* comparison (`>=`, `<` etc) operators [here](https://mikefarah.gitbook.io/yq/operators/compare)
* boolean operators (`and`, `or`, `any` etc) [here](https://mikefarah.gitbook.io/yq/operators/boolean-operators)

## Select elements from array using wildcard prefix

Given a sample.yml file of:

```yaml
- cat
- goat
- dog
```

then

```bash
yq '.[] | select(. == "*at")' sample.yml
```

will output

```yaml
cat
goat
```

## Select elements from array using wildcard suffix

Given a sample.yml file of:

```yaml
- go-kart
- goat
- dog
```

then

```bash
yq '.[] | select(. == "go*")' sample.yml
```

will output

```yaml
go-kart
goat
```

## Select elements from array using wildcard prefix and suffix

Given a sample.yml file of:

```yaml
- ago
- go
- meow
- going
```

then

```bash
yq '.[] | select(. == "*go*")' sample.yml
```

will output

```yaml
ago
go
going
```

## Select elements from array with regular expression

See more regular expression examples under the [`string` operator docs](https://mikefarah.gitbook.io/yq/operators/string-operators).

Given a sample.yml file of:

```yaml
- this_0
- not_this
- nor_0_this
- thisTo_4
```

then

```bash
yq '.[] | select(test("[a-zA-Z]+_[0-9]$"))' sample.yml
```

will output

```yaml
this_0
thisTo_4
```

## Select items from a map

Given a sample.yml file of:

```yaml
things: cat
bob: goat
horse: dog
```

then

```bash
yq '.[] | select(. == "cat" or test("og$"))' sample.yml
```

will output

```yaml
cat
dog
```

## Use select and with\_entries to filter map keys

Given a sample.yml file of:

```yaml
name: bob
legs: 2
game: poker
```

then

```bash
yq 'with_entries(select(.key | test("ame$")))' sample.yml
```

will output

```yaml
name: bob
game: poker
```

## Select multiple items in a map and update

Note the brackets around the entire LHS.

Given a sample.yml file of:

```yaml
a:
  things: cat
  bob: goat
  horse: dog
```

then

```bash
yq '(.a.[] | select(. == "cat" or . == "goat")) |= "rabbit"' sample.yml
```

will output

```yaml
a:
  things: rabbit
  bob: rabbit
  horse: dog
```


# Shuffle

Shuffles an array. Note that this command does *not* use a cryptographically secure random number generator to randomise the array order.

## Shuffle array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
- 4
- 5
```

then

```bash
yq 'shuffle' sample.yml
```

will output

```yaml
- 5
- 2
- 4
- 1
- 3
```

## Shuffle array in place

Given a sample.yml file of:

```yaml
cool:
  - 1
  - 2
  - 3
  - 4
  - 5
```

then

```bash
yq '.cool |= shuffle' sample.yml
```

will output

```yaml
cool:
  - 5
  - 2
  - 4
  - 1
  - 3
```


# Slice Array

The slice array operator takes an array as input and returns a subarray. Like the `jq` equivalent, `.[10:15]` will return an array of length 5, starting from index 10 inclusive, up to index 15 exclusive. Negative numbers count backwards from the end of the array.

You may leave out the first or second number, which will refer to the start or end of the array respectively.

## Slicing arrays

Given a sample.yml file of:

```yaml
- cat
- dog
- frog
- cow
```

then

```bash
yq '.[1:3]' sample.yml
```

will output

```yaml
- dog
- frog
```

## Slicing arrays - without the first number

Starts from the start of the array

Given a sample.yml file of:

```yaml
- cat
- dog
- frog
- cow
```

then

```bash
yq '.[:2]' sample.yml
```

will output

```yaml
- cat
- dog
```

## Slicing arrays - without the second number

Finishes at the end of the array

Given a sample.yml file of:

```yaml
- cat
- dog
- frog
- cow
```

then

```bash
yq '.[2:]' sample.yml
```

will output

```yaml
- frog
- cow
```

## Slicing arrays - use negative numbers to count backwards from the end

Given a sample.yml file of:

```yaml
- cat
- dog
- frog
- cow
```

then

```bash
yq '.[1:-1]' sample.yml
```

will output

```yaml
- dog
- frog
```

## Inserting into the middle of an array

using an expression to find the index

Given a sample.yml file of:

```yaml
- cat
- dog
- frog
- cow
```

then

```bash
yq '(.[] | select(. == "dog") | key + 1) as $pos | .[0:($pos)] + ["rabbit"] + .[$pos:]' sample.yml
```

will output

```yaml
- cat
- dog
- rabbit
- frog
- cow
```


# Sort

Sorts an array. Use `sort` to sort an array as is, or `sort_by(exp)` to sort by a particular expression (e.g. subfield).

To sort by descending order, pipe the results through the `reverse` operator after sorting.

Note that at this stage, `yq` only sorts scalar fields.

## Sort by string field

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'sort_by(.a)' sample.yml
```

will output

```yaml
- a: apple
- a: banana
- a: cat
```

## Sort by multiple fields

Given a sample.yml file of:

```yaml
- a: dog
- a: cat
  b: banana
- a: cat
  b: apple
```

then

```bash
yq 'sort_by(.a, .b)' sample.yml
```

will output

```yaml
- a: cat
  b: apple
- a: cat
  b: banana
- a: dog
```

## Sort descending by string field

Use sort with reverse to sort in descending order.

Given a sample.yml file of:

```yaml
- a: banana
- a: cat
- a: apple
```

then

```bash
yq 'sort_by(.a) | reverse' sample.yml
```

will output

```yaml
- a: cat
- a: banana
- a: apple
```

## Sort array in place

Given a sample.yml file of:

```yaml
cool:
  - a: banana
  - a: cat
  - a: apple
```

then

```bash
yq '.cool |= sort_by(.a)' sample.yml
```

will output

```yaml
cool:
  - a: apple
  - a: banana
  - a: cat
```

## Sort array of objects by key

Note that you can give sort\_by complex expressions, not just paths

Given a sample.yml file of:

```yaml
cool:
  - b: banana
  - a: banana
  - c: banana
```

then

```bash
yq '.cool |= sort_by(keys | .[0])' sample.yml
```

will output

```yaml
cool:
  - a: banana
  - b: banana
  - c: banana
```

## Sort a map

Sorting a map, by default this will sort by the values

Given a sample.yml file of:

```yaml
y: b
z: a
x: c
```

then

```bash
yq 'sort' sample.yml
```

will output

```yaml
z: a
y: b
x: c
```

## Sort a map by keys

Use sort\_by to sort a map using a custom function

Given a sample.yml file of:

```yaml
Y: b
z: a
x: c
```

then

```bash
yq 'sort_by(key | downcase)' sample.yml
```

will output

```yaml
x: c
Y: b
z: a
```

## Sort is stable

Note the order of the elements in unchanged when equal in sorting.

Given a sample.yml file of:

```yaml
- a: banana
  b: 1
- a: banana
  b: 2
- a: banana
  b: 3
- a: banana
  b: 4
```

then

```bash
yq 'sort_by(.a)' sample.yml
```

will output

```yaml
- a: banana
  b: 1
- a: banana
  b: 2
- a: banana
  b: 3
- a: banana
  b: 4
```

## Sort by numeric field

Given a sample.yml file of:

```yaml
- a: 10
- a: 100
- a: 1
```

then

```bash
yq 'sort_by(.a)' sample.yml
```

will output

```yaml
- a: 1
- a: 10
- a: 100
```

## Sort by custom date field

Given a sample.yml file of:

```yaml
- a: 12-Jun-2011
- a: 23-Dec-2010
- a: 10-Aug-2011
```

then

```bash
yq 'with_dtf("02-Jan-2006"; sort_by(.a))' sample.yml
```

will output

```yaml
- a: 23-Dec-2010
- a: 12-Jun-2011
- a: 10-Aug-2011
```

## Sort, nulls come first

Given a sample.yml file of:

```yaml
- 8
- 3
- null
- 6
- true
- false
- cat
```

then

```bash
yq 'sort' sample.yml
```

will output

```yaml
- null
- false
- true
- 3
- 6
- 8
- cat
```


# Sort Keys

The Sort Keys operator sorts maps by their keys (based on their string value). This operator does not do anything to arrays or scalars (so you can easily recursively apply it to all maps).

Sort is particularly useful for diffing two different yaml documents:

```bash
yq -i -P 'sort_keys(..)' file1.yml
yq -i -P 'sort_keys(..)' file2.yml
diff file1.yml file2.yml
```

Note that `yq` does not yet consider anchors when sorting by keys - this may result in invalid yaml documents if you are using merge anchors.

For more advanced sorting, you can use the [sort\_by](https://mikefarah.gitbook.io/yq/operators/sort) function on a map, and give it a custom function like `sort_by(key | downcase)`.

## Sort keys of map

Given a sample.yml file of:

```yaml
c: frog
a: blah
b: bing
```

then

```bash
yq 'sort_keys(.)' sample.yml
```

will output

```yaml
a: blah
b: bing
c: frog
```

## Sort keys recursively

Note the array elements are left unsorted, but maps inside arrays are sorted

Given a sample.yml file of:

```yaml
bParent:
  c: dog
  array:
    - 3
    - 1
    - 2
aParent:
  z: donkey
  x:
    - c: yum
      b: delish
    - b: ew
      a: apple
```

then

```bash
yq 'sort_keys(..)' sample.yml
```

will output

```yaml
aParent:
  x:
    - b: delish
      c: yum
    - a: apple
      b: ew
  z: donkey
bParent:
  array:
    - 3
    - 1
    - 2
  c: dog
```


# Split into Documents

This operator splits all matches into separate documents

## Split empty

Running

```bash
yq --null-input 'split_doc'
```

will output

```yaml
```

## Split array

Given a sample.yml file of:

```yaml
- a: cat
- b: dog
```

then

```bash
yq '.[] | split_doc' sample.yml
```

will output

```yaml
a: cat
---
b: dog
```


# String Operators

## RegEx

This uses Golang's native regex functions under the hood - See their [docs](https://github.com/google/re2/wiki/Syntax) for the supported syntax.

Case insensitive tip: prefix the regex with `(?i)` - e.g. `test("(?i)cats")`.

### match(regEx)

This operator returns the substring match details of the given regEx.

### capture(regEx)

Capture returns named RegEx capture groups in a map. Can be more convenient than `match` depending on what you are doing.

## test(regEx)

Returns true if the string matches the RegEx, false otherwise.

## sub(regEx, replacement)

Substitutes matched substrings. The first parameter is the regEx to match substrings within the original string. The second parameter specifies what to replace those matches with. This can refer to capture groups from the first RegEx.

## String blocks, bash and newlines

Bash is notorious for chomping on precious trailing newline characters, making it tricky to set strings with newlines properly. In particular, the `$( exp )` *will trim trailing newlines*.

For instance to get this yaml:

```
a: |
  cat
```

Using `$( exp )` wont work, as it will trim the trailing newline.

```
m=$(echo "cat\n") yq -n '.a = strenv(m)'
a: cat
```

However, using printf works:

```
printf -v m "cat\n" ; m="$m" yq -n '.a = strenv(m)'
a: |
  cat
```

As well as having multiline expressions:

```
m="cat
"  yq -n '.a = strenv(m)'
a: |
  cat
```

Similarly, if you're trying to set the content from a file, and want a trailing newline:

```
IFS= read -rd '' output < <(cat my_file)
output=$output ./yq '.data.values = strenv(output)' first.yml
```

## Interpolation

Given a sample.yml file of:

```yaml
value: things
another: stuff
```

then

```bash
yq '.message = "I like \(.value) and \(.another)"' sample.yml
```

will output

```yaml
value: things
another: stuff
message: I like things and stuff
```

## Interpolation - not a string

Given a sample.yml file of:

```yaml
value:
  an: apple
```

then

```bash
yq '.message = "I like \(.value)"' sample.yml
```

will output

```yaml
value:
  an: apple
message: 'I like an: apple'
```

## To up (upper) case

Works with unicode characters

Given a sample.yml file of:

```yaml
água
```

then

```bash
yq 'upcase' sample.yml
```

will output

```yaml
ÁGUA
```

## To down (lower) case

Works with unicode characters

Given a sample.yml file of:

```yaml
ÁgUA
```

then

```bash
yq 'downcase' sample.yml
```

will output

```yaml
água
```

## Join strings

Given a sample.yml file of:

```yaml
- cat
- meow
- 1
- null
- true
```

then

```bash
yq 'join("; ")' sample.yml
```

will output

```yaml
cat; meow; 1; ; true
```

## Trim strings

Given a sample.yml file of:

```yaml
- ' cat'
- 'dog '
- ' cow cow '
- horse
```

then

```bash
yq '.[] | trim' sample.yml
```

will output

```yaml
cat
dog
cow cow
horse
```

## Match string

Given a sample.yml file of:

```yaml
foo bar foo
```

then

```bash
yq 'match("foo")' sample.yml
```

will output

```yaml
string: foo
offset: 0
length: 3
captures: []
```

## Match string, case insensitive

Given a sample.yml file of:

```yaml
foo bar FOO
```

then

```bash
yq '[match("(?i)foo"; "g")]' sample.yml
```

will output

```yaml
- string: foo
  offset: 0
  length: 3
  captures: []
- string: FOO
  offset: 8
  length: 3
  captures: []
```

## Match with global capture group

Given a sample.yml file of:

```yaml
abc abc
```

then

```bash
yq '[match("(ab)(c)"; "g")]' sample.yml
```

will output

```yaml
- string: abc
  offset: 0
  length: 3
  captures:
    - string: ab
      offset: 0
      length: 2
    - string: c
      offset: 2
      length: 1
- string: abc
  offset: 4
  length: 3
  captures:
    - string: ab
      offset: 4
      length: 2
    - string: c
      offset: 6
      length: 1
```

## Match with named capture groups

Given a sample.yml file of:

```yaml
foo bar foo foo  foo
```

then

```bash
yq '[match("foo (?P<bar123>bar)? foo"; "g")]' sample.yml
```

will output

```yaml
- string: foo bar foo
  offset: 0
  length: 11
  captures:
    - string: bar
      offset: 4
      length: 3
      name: bar123
- string: foo  foo
  offset: 12
  length: 8
  captures:
    - string: null
      offset: -1
      length: 0
      name: bar123
```

## Capture named groups into a map

Given a sample.yml file of:

```yaml
xyzzy-14
```

then

```bash
yq 'capture("(?P<a>[a-z]+)-(?P<n>[0-9]+)")' sample.yml
```

will output

```yaml
a: xyzzy
n: "14"
```

## Match without global flag

Given a sample.yml file of:

```yaml
cat cat
```

then

```bash
yq 'match("cat")' sample.yml
```

will output

```yaml
string: cat
offset: 0
length: 3
captures: []
```

## Match with global flag

Given a sample.yml file of:

```yaml
cat cat
```

then

```bash
yq '[match("cat"; "g")]' sample.yml
```

will output

```yaml
- string: cat
  offset: 0
  length: 3
  captures: []
- string: cat
  offset: 4
  length: 3
  captures: []
```

## Test using regex

Like jq's equivalent, this works like match but only returns true/false instead of full match details

Given a sample.yml file of:

```yaml
- cat
- dog
```

then

```bash
yq '.[] | test("at")' sample.yml
```

will output

```yaml
true
false
```

## Substitute / Replace string

This uses Golang's regex, described [here](https://github.com/google/re2/wiki/Syntax).\
Note the use of `|=` to run in context of the current string value.

Given a sample.yml file of:

```yaml
a: dogs are great
```

then

```bash
yq '.a |= sub("dogs", "cats")' sample.yml
```

will output

```yaml
a: cats are great
```

## Substitute / Replace string with regex

This uses Golang's regex, described [here](https://github.com/google/re2/wiki/Syntax).\
Note the use of `|=` to run in context of the current string value.

Given a sample.yml file of:

```yaml
a: cat
b: heat
```

then

```bash
yq '.[] |= sub("(a)", "${1}r")' sample.yml
```

will output

```yaml
a: cart
b: heart
```

## Custom types: that are really strings

When custom tags are encountered, yq will try to decode the underlying type.

Given a sample.yml file of:

```yaml
a: !horse cat
b: !goat heat
```

then

```bash
yq '.[] |= sub("(a)", "${1}r")' sample.yml
```

will output

```yaml
a: !horse cart
b: !goat heart
```

## Split strings

Given a sample.yml file of:

```yaml
cat; meow; 1; ; true
```

then

```bash
yq 'split("; ")' sample.yml
```

will output

```yaml
- cat
- meow
- "1"
- ""
- "true"
```

## Split strings one match

Given a sample.yml file of:

```yaml
word
```

then

```bash
yq 'split("; ")' sample.yml
```

will output

```yaml
- word
```

## To string

Note that you may want to force `yq` to leave scalar values wrapped by passing in `--unwrapScalar=false` or `-r=f`

Given a sample.yml file of:

```yaml
- 1
- true
- null
- ~
- cat
- an: object
- - array
  - 2
```

then

```bash
yq '.[] |= to_string' sample.yml
```

will output

```yaml
- "1"
- "true"
- "null"
- "~"
- cat
- "an: object"
- "- array\n- 2"
```


# Style

The style operator can be used to get or set the style of nodes (e.g. string style, yaml style). Use this to control the formatting of the document in yaml.

## Update and set style of a particular node (simple)

Given a sample.yml file of:

```yaml
a:
  b: thing
  c: something
```

then

```bash
yq '.a.b = "new" | .a.b style="double"' sample.yml
```

will output

```yaml
a:
  b: "new"
  c: something
```

## Update and set style of a particular node using path variables

Given a sample.yml file of:

```yaml
a:
  b: thing
  c: something
```

then

```bash
yq 'with(.a.b ; . = "new" | . style="double")' sample.yml
```

will output

```yaml
a:
  b: "new"
  c: something
```

## Set tagged style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="tagged"' sample.yml
```

will output

```yaml
!!map
a: !!str cat
b: !!int 5
c: !!float 3.2
e: !!bool true
f: !!seq
  - !!int 1
  - !!int 2
  - !!int 3
g: !!map
  something: !!str cool
```

## Set double quote style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="double"' sample.yml
```

will output

```yaml
a: "cat"
b: "5"
c: "3.2"
e: "true"
f:
  - "1"
  - "2"
  - "3"
g:
  something: "cool"
```

## Set double quote style on map keys too

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '... style="double"' sample.yml
```

will output

```yaml
"a": "cat"
"b": "5"
"c": "3.2"
"e": "true"
"f":
  - "1"
  - "2"
  - "3"
"g":
  "something": "cool"
```

## Set single quote style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="single"' sample.yml
```

will output

```yaml
a: 'cat'
b: '5'
c: '3.2'
e: 'true'
f:
  - '1'
  - '2'
  - '3'
g:
  something: 'cool'
```

## Set literal quote style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="literal"' sample.yml
```

will output

```yaml
a: |-
  cat
b: |-
  5
c: |-
  3.2
e: |-
  true
f:
  - |-
    1
  - |-
    2
  - |-
    3
g:
  something: |-
    cool
```

## Set folded quote style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="folded"' sample.yml
```

will output

```yaml
a: >-
  cat
b: >-
  5
c: >-
  3.2
e: >-
  true
f:
  - >-
    1
  - >-
    2
  - >-
    3
g:
  something: >-
    cool
```

## Set flow quote style

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

then

```bash
yq '.. style="flow"' sample.yml
```

will output

```yaml
{a: cat, b: 5, c: 3.2, e: true, f: [1, 2, 3], g: {something: cool}}
```

## Reset style - or pretty print

Set empty (default) quote style, note the usage of `...` to match keys too. Note that there is a `--prettyPrint/-P` short flag for this.

Given a sample.yml file of:

```yaml
{a: cat, "b": 5, 'c': 3.2, "e": true,  f: [1,2,3], "g": { something: "cool"} }
```

then

```bash
yq '... style=""' sample.yml
```

will output

```yaml
a: cat
b: 5
c: 3.2
e: true
f:
  - 1
  - 2
  - 3
g:
  something: cool
```

## Set style relatively with assign-update

Given a sample.yml file of:

```yaml
a: single
b: double
```

then

```bash
yq '.[] style |= .' sample.yml
```

will output

```yaml
a: 'single'
b: "double"
```

## Read style

Given a sample.yml file of:

```yaml
{a: "cat", b: 'thing'}
```

then

```bash
yq '.. | style' sample.yml
```

will output

```yaml
flow
double
single
```


# Subtract

You can use subtract to subtract numbers as well as remove elements from an array.

## Array subtraction

Running

```bash
yq --null-input '[1,2] - [2,3]'
```

will output

```yaml
- 1
```

## Array subtraction with nested array

Running

```bash
yq --null-input '[[1], 1, 2] - [[1], 3]'
```

will output

```yaml
- 1
- 2
```

## Array subtraction with nested object

Note that order of the keys does not matter

Given a sample.yml file of:

```yaml
- a: b
  c: d
- a: b
```

then

```bash
yq '. - [{"c": "d", "a": "b"}]' sample.yml
```

will output

```yaml
- a: b
```

## Number subtraction - float

If the lhs or rhs are floats then the expression will be calculated with floats.

Given a sample.yml file of:

```yaml
a: 3
b: 4.5
```

then

```bash
yq '.a = .a - .b' sample.yml
```

will output

```yaml
a: -1.5
b: 4.5
```

## Number subtraction - int

If both the lhs and rhs are ints then the expression will be calculated with ints.

Given a sample.yml file of:

```yaml
a: 3
b: 4
```

then

```bash
yq '.a = .a - .b' sample.yml
```

will output

```yaml
a: -1
b: 4
```

## Decrement numbers

Given a sample.yml file of:

```yaml
a: 3
b: 5
```

then

```bash
yq '.[] -= 1' sample.yml
```

will output

```yaml
a: 2
b: 4
```

## Date subtraction

You can subtract durations from dates. Assumes RFC3339 date time format, see [date-time operators](https://mikefarah.gitbook.io/yq/operators/date-time-operators) for more information.

Given a sample.yml file of:

```yaml
a: 2021-01-01T03:10:00Z
```

then

```bash
yq '.a -= "3h10m"' sample.yml
```

will output

```yaml
a: 2021-01-01T00:00:00Z
```

## Date subtraction - custom format

Use with\_dtf to specify your datetime format. See [date-time operators](https://mikefarah.gitbook.io/yq/operators/date-time-operators) for more information.

Given a sample.yml file of:

```yaml
a: Saturday, 15-Dec-01 at 6:00AM GMT
```

then

```bash
yq 'with_dtf("Monday, 02-Jan-06 at 3:04PM MST", .a -= "3h1m")' sample.yml
```

will output

```yaml
a: Saturday, 15-Dec-01 at 2:59AM GMT
```

## Custom types: that are really numbers

When custom tags are encountered, yq will try to decode the underlying type.

Given a sample.yml file of:

```yaml
a: !horse 2
b: !goat 1
```

then

```bash
yq '.a -= .b' sample.yml
```

will output

```yaml
a: !horse 1
b: !goat 1
```


# Tag

The tag operator can be used to get or set the tag of nodes (e.g. `!!str`, `!!int`, `!!bool`).

## Get tag

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f: []
```

then

```bash
yq '.. | tag' sample.yml
```

will output

```yaml
!!map
!!str
!!int
!!float
!!bool
!!seq
```

## type is an alias for tag

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
f: []
```

then

```bash
yq '.. | type' sample.yml
```

will output

```yaml
!!map
!!str
!!int
!!float
!!bool
!!seq
```

## Set custom tag

Given a sample.yml file of:

```yaml
a: str
```

then

```bash
yq '.a tag = "!!mikefarah"' sample.yml
```

will output

```yaml
a: !!mikefarah str
```

## Find numbers and convert them to strings

Given a sample.yml file of:

```yaml
a: cat
b: 5
c: 3.2
e: true
```

then

```bash
yq '(.. | select(tag == "!!int")) tag= "!!str"' sample.yml
```

will output

```yaml
a: cat
b: "5"
c: 3.2
e: true
```


# To Number

Parses the input as a number. yq will try to parse values as an int first, failing that it will try float. Values that already ints or floats will be left alone.

## Converts strings to numbers

Given a sample.yml file of:

```yaml
- "3"
- "3.1"
- "-1e3"
```

then

```bash
yq '.[] | to_number' sample.yml
```

will output

```yaml
3
3.1
-1e3
```

## Doesn't change numbers

Given a sample.yml file of:

```yaml
- 3
- 3.1
- -1e3
```

then

```bash
yq '.[] | to_number' sample.yml
```

will output

```yaml
3
3.1
-1e3
```

## Cannot convert null

Running

```bash
yq --null-input '.a.b | to_number'
```

will output

```bash
Error: cannot convert node value [null] at path a.b of tag !!null to number
```


# Traverse (Read)

This is the simplest (and perhaps most used) operator. It is used to navigate deeply into yaml structures.

## NOTE --yaml-fix-merge-anchor-to-spec flag (v4.47.1 [#2110](https://github.com/mikefarah/yq/issues/2110))

`yq` doesn't merge anchors `<<:` to spec, in some circumstances it incorrectly overrides existing keys when the spec documents not to do that.

To minimise disruption while still fixing the issue, a flag has been added to toggle this behaviour. This will first default to false; and log warnings to users. Then it will default to true (and still allow users to specify false if needed)

See examples of the flag differences below, where LEGACY is the flag off; and FIXED is with the flag on.

## Simple map navigation

Given a sample.yml file of:

```yaml
a:
  b: apple
```

then

```bash
yq '.a' sample.yml
```

will output

```yaml
b: apple
```

## Splat

Often used to pipe children into other operators

Given a sample.yml file of:

```yaml
- b: apple
- c: banana
```

then

```bash
yq '.[]' sample.yml
```

will output

```yaml
b: apple
c: banana
```

## Optional Splat

Just like splat, but won't error if you run it against scalars

Given a sample.yml file of:

```yaml
cat
```

then

```bash
yq '.[]' sample.yml
```

will output

```yaml
```

## Special characters

Use quotes with square brackets around path elements with special characters

Given a sample.yml file of:

```yaml
"{}": frog
```

then

```bash
yq '.["{}"]' sample.yml
```

will output

```yaml
frog
```

## Nested special characters

Given a sample.yml file of:

```yaml
a:
  "key.withdots":
    "another.key": apple
```

then

```bash
yq '.a["key.withdots"]["another.key"]' sample.yml
```

will output

```yaml
apple
```

## Keys with spaces

Use quotes with square brackets around path elements with special characters

Given a sample.yml file of:

```yaml
"red rabbit": frog
```

then

```bash
yq '.["red rabbit"]' sample.yml
```

will output

```yaml
frog
```

## Dynamic keys

Expressions within \[] can be used to dynamically lookup / calculate keys

Given a sample.yml file of:

```yaml
b: apple
apple: crispy yum
banana: soft yum
```

then

```bash
yq '.[.b]' sample.yml
```

will output

```yaml
crispy yum
```

## Children don't exist

Nodes are added dynamically while traversing

Given a sample.yml file of:

```yaml
c: banana
```

then

```bash
yq '.a.b' sample.yml
```

will output

```yaml
null
```

## Optional identifier

Like jq, does not output an error when the yaml is not an array or object as expected

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq '.a?' sample.yml
```

will output

```yaml
```

## Wildcard matching

Given a sample.yml file of:

```yaml
a:
  cat: apple
  mad: things
```

then

```bash
yq '.a."*a*"' sample.yml
```

will output

```yaml
apple
things
```

## Aliases

Given a sample.yml file of:

```yaml
a: &cat
  c: frog
b: *cat
```

then

```bash
yq '.b' sample.yml
```

will output

```yaml
*cat
```

## Traversing aliases with splat

Given a sample.yml file of:

```yaml
a: &cat
  c: frog
b: *cat
```

then

```bash
yq '.b[]' sample.yml
```

will output

```yaml
frog
```

## Traversing aliases explicitly

Given a sample.yml file of:

```yaml
a: &cat
  c: frog
b: *cat
```

then

```bash
yq '.b.c' sample.yml
```

will output

```yaml
frog
```

## Traversing arrays by index

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
```

then

```bash
yq '.[0]' sample.yml
```

will output

```yaml
1
```

## Traversing nested arrays by index

Given a sample.yml file of:

```yaml
[[], [cat]]
```

then

```bash
yq '.[1][0]' sample.yml
```

will output

```yaml
cat
```

## Maps with numeric keys

Given a sample.yml file of:

```yaml
2: cat
```

then

```bash
yq '.[2]' sample.yml
```

will output

```yaml
cat
```

## Maps with non existing numeric keys

Given a sample.yml file of:

```yaml
a: b
```

then

```bash
yq '.[0]' sample.yml
```

will output

```yaml
null
```

## Traversing merge anchors

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar.a' sample.yml
```

will output

```yaml
foo_a
```

## Traversing merge anchors with local override

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar.thing' sample.yml
```

will output

```yaml
foobar_thing
```

## Select multiple indices

Given a sample.yml file of:

```yaml
a:
  - a
  - b
  - c
```

then

```bash
yq '.a[0, 2]' sample.yml
```

will output

```yaml
a
c
```

## LEGACY: Traversing merge anchors with override

This is legacy behaviour, see --yaml-fix-merge-anchor-to-spec

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar.c' sample.yml
```

will output

```yaml
foo_c
```

## LEGACY: Traversing merge anchor lists

Note that the later merge anchors override previous, but this is legacy behaviour, see --yaml-fix-merge-anchor-to-spec

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobarList.thing' sample.yml
```

will output

```yaml
bar_thing
```

## LEGACY: Splatting merge anchors

With legacy override behaviour, see --yaml-fix-merge-anchor-to-spec

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar[]' sample.yml
```

will output

```yaml
foo_c
foo_a
foobar_thing
```

## LEGACY: Splatting merge anchor lists

With legacy override behaviour, see --yaml-fix-merge-anchor-to-spec

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobarList[]' sample.yml
```

will output

```yaml
bar_b
foo_a
bar_thing
foobarList_c
```

## FIXED: Traversing merge anchors with override

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour.

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar.c' sample.yml
```

will output

```yaml
foobar_c
```

## FIXED: Traversing merge anchor lists

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour. Note that the keys earlier in the merge anchors sequence override later ones

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobarList.thing' sample.yml
```

will output

```yaml
foo_thing
```

## FIXED: Splatting merge anchors

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour. Note that the keys earlier in the merge anchors sequence override later ones

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobar[]' sample.yml
```

will output

```yaml
foo_a
foobar_thing
foobar_c
```

## FIXED: Splatting merge anchor lists

Set `--yaml-fix-merge-anchor-to-spec=true` to get this correct merge behaviour. Note that the keys earlier in the merge anchors sequence override later ones

Given a sample.yml file of:

```yaml
foo: &foo
  a: foo_a
  thing: foo_thing
  c: foo_c
bar: &bar
  b: bar_b
  thing: bar_thing
  c: bar_c
foobarList:
  b: foobarList_b
  !!merge <<:
    - *foo
    - *bar
  c: foobarList_c
foobar:
  c: foobar_c
  !!merge <<: *foo
  thing: foobar_thing
```

then

```bash
yq '.foobarList[]' sample.yml
```

will output

```yaml
foobarList_b
foo_thing
foobarList_c
foo_a
```


# Union

This operator is used to combine different results together.

## Combine scalars

Running

```bash
yq --null-input '1, true, "cat"'
```

will output

```yaml
1
true
cat
```

## Combine selected paths

Given a sample.yml file of:

```yaml
a: fieldA
b: fieldB
c: fieldC
```

then

```bash
yq '.a, .c' sample.yml
```

will output

```yaml
fieldA
fieldC
```


# Unique

This is used to filter out duplicated items in an array. Note that the original order of the array is maintained.

## Unique array of scalars (string/numbers)

Note that unique maintains the original order of the array.

Given a sample.yml file of:

```yaml
- 2
- 1
- 3
- 2
```

then

```bash
yq 'unique' sample.yml
```

will output

```yaml
- 2
- 1
- 3
```

## Unique nulls

Unique works on the node value, so it considers different representations of nulls to be different

Given a sample.yml file of:

```yaml
- ~
- null
- ~
- null
```

then

```bash
yq 'unique' sample.yml
```

will output

```yaml
- ~
- null
```

## Unique all nulls

Run against the node tag to unique all the nulls

Given a sample.yml file of:

```yaml
- ~
- null
- ~
- null
```

then

```bash
yq 'unique_by(tag)' sample.yml
```

will output

```yaml
- ~
```

## Unique array objects

Given a sample.yml file of:

```yaml
- name: harry
  pet: cat
- name: billy
  pet: dog
- name: harry
  pet: cat
```

then

```bash
yq 'unique' sample.yml
```

will output

```yaml
- name: harry
  pet: cat
- name: billy
  pet: dog
```

## Unique array of objects by a field

Given a sample.yml file of:

```yaml
- name: harry
  pet: cat
- name: billy
  pet: dog
- name: harry
  pet: dog
```

then

```bash
yq 'unique_by(.name)' sample.yml
```

will output

```yaml
- name: harry
  pet: cat
- name: billy
  pet: dog
```

## Unique array of arrays

Given a sample.yml file of:

```yaml
- - cat
  - dog
- - cat
  - sheep
- - cat
  - dog
```

then

```bash
yq 'unique' sample.yml
```

will output

```yaml
- - cat
  - dog
- - cat
  - sheep
```


# Variable Operators

Like the `jq` equivalents, variables are sometimes required for the more complex expressions (or swapping values between fields).

Note that there is also an additional `ref` operator that holds a reference (instead of a copy) of the path, allowing you to make multiple changes to the same path.

## Single value variable

Given a sample.yml file of:

```yaml
a: cat
```

then

```bash
yq '.a as $foo | $foo' sample.yml
```

will output

```yaml
cat
```

## Multi value variable

Given a sample.yml file of:

```yaml
- cat
- dog
```

then

```bash
yq '.[] as $foo | $foo' sample.yml
```

will output

```yaml
cat
dog
```

## Using variables as a lookup

Example taken from [jq](https://stedolan.github.io/jq/manual/#Variable/SymbolicBindingOperator:...as$identifier|...)

Given a sample.yml file of:

```yaml
"posts":
  - "title": First post
    "author": anon
  - "title": A well-written article
    "author": person1
"realnames":
  "anon": Anonymous Coward
  "person1": Person McPherson
```

then

```bash
yq '.realnames as $names | .posts[] | {"title":.title, "author": $names[.author]}' sample.yml
```

will output

```yaml
title: First post
author: Anonymous Coward
title: A well-written article
author: Person McPherson
```

## Using variables to swap values

Given a sample.yml file of:

```yaml
a: a_value
b: b_value
```

then

```bash
yq '.a as $x  | .b as $y | .b = $x | .a = $y' sample.yml
```

will output

```yaml
a: b_value
b: a_value
```

## Use ref to reference a path repeatedly

Note: You may find the `with` operator more useful.

Given a sample.yml file of:

```yaml
a:
  b: thing
  c: something
```

then

```bash
yq '.a.b ref $x | $x = "new" | $x style="double"' sample.yml
```

will output

```yaml
a:
  b: "new"
  c: something
```


# With

Use the `with` operator to conveniently make multiple updates to a deeply nested path, or to update array elements relatively to each other. The first argument expression sets the root context, and the second expression runs against that root context.

## Update and style

Given a sample.yml file of:

```yaml
a:
  deeply:
    nested: value
```

then

```bash
yq 'with(.a.deeply.nested; . = "newValue" | . style="single")' sample.yml
```

will output

```yaml
a:
  deeply:
    nested: 'newValue'
```

## Update multiple deeply nested properties

Given a sample.yml file of:

```yaml
a:
  deeply:
    nested: value
    other: thing
```

then

```bash
yq 'with(.a.deeply; .nested = "newValue" | .other= "newThing")' sample.yml
```

will output

```yaml
a:
  deeply:
    nested: newValue
    other: newThing
```

## Update array elements relatively

The second expression runs with each element of the array as it's contextual root. This allows you to make updates relative to the element.

Given a sample.yml file of:

```yaml
myArray:
  - a: apple
  - a: banana
```

then

```bash
yq 'with(.myArray[]; .b = .a + " yum")' sample.yml
```

will output

```yaml
myArray:
  - a: apple
    b: apple yum
  - a: banana
    b: banana yum
```


# Output format

Flags to control yaml and json output format

These flags are available for all `yq` commands.

## Color

By default, `yq` prints with colours if it detects a terminal. You can manually change this by using either

The `--colors/-C` flag to force print with colors.

The `--no-colors/-M` flag to force print without colours

## Pretty Print

To print out idiomatic `yaml` use the `--prettyPrint/-P` flag. Note that this is shorthand for using the [style](https://mikefarah.gitbook.io/yq/operators/style) operator `... style=""`

## Indent

Use the indent flag `--indent/-I` to control the number of spaces used for indentation. This also works for JSON output. The default value is 2.

Note that lists are indented at the same level as the map key at indent level 2, but are more deeply indented at indent level 4 and greater. This is (currently) a quirk of the underlying [yaml parser](https://github.com/go-yaml/yaml/tree/v3).

Given:

```
apples:
  collection:
  - name: Green
  - name: Blue
  favourite: Pink Lady
```

Then:

```
yq -I4 sample.yaml
```

Will print out:

```yaml
apples:
    collection:
      - name: Green
      - name: Blue
    favourite: Pink Lady
```

This also works with json

```
yq -j -I4 sample.yaml
```

yields

```javascript
{
    "apples": {
        "collection": [
            {
                "name": "Green"
            },
            {
                "name": "Blue"
            }
        ],
        "favourite": "Pink Lady"
    }
}
```

## Unwrap scalars

By default scalar values are 'unwrapped', that is only their value is printed (except when outputting as JSON). To print out the node as-is, with the original formatting an any comments pass in `--unwrapScalar=false`

Given data.yml:

```yaml
a: "Things" # cool stuff
```

Then:

`yq --unwrapScalar=false '.a' data.yml`

Will yield:

```yaml
"Things" # cool stuff
```

where as without setting the flag to false you would get:

```yaml
Things
```


# Working with Base64

Encode and decode to and from Base64.

Base64 assumes [RFC4648](https://rfc-editor.org/rfc/rfc4648.html) encoding. Encoding and decoding both assume that the content is a UTF-8 string and not binary content.

See below for examples

## Decode base64: simple

Decoded data is assumed to be a string.

Given a sample.txt file of:

```
YSBzcGVjaWFsIHN0cmluZw==
```

then

```bash
yq -p=base64 -oy '.' sample.txt
```

will output

```yaml
a special string
```

## Decode base64: UTF-8

Base64 decoding supports UTF-8 encoded strings.

Given a sample.txt file of:

```
V29ya3Mgd2l0aCBVVEYtMTYg8J+Yig==
```

then

```bash
yq -p=base64 -oy '.' sample.txt
```

will output

```yaml
Works with UTF-16 😊
```

## Decode with extra spaces

Extra leading/trailing whitespace is stripped

Given a sample.txt file of:

```

 YSBzcGVjaWFsIHN0cmluZw==  

```

then

```bash
yq -p=base64 -oy '.' sample.txt
```

will output

```yaml
a special string
```

## Encode base64: string

Given a sample.yml file of:

```yaml
"a special string"
```

then

```bash
yq -o=base64 '.' sample.yml
```

will output

````
YSBzcGVjaWFsIHN0cmluZw==```

## Encode base64: string from document
Extract a string field and encode it to base64.

Given a sample.yml file of:
```yaml
coolData: "a special string"
````

then

```bash
yq -o=base64 '.coolData' sample.yml
```

will output

````
YSBzcGVjaWFsIHN0cmluZw==```

````


# Working with CSV, TSV

Encode/Decode/Roundtrip CSV and TSV files.

## Encode

Currently supports arrays of homogeneous flat objects, that is: no nesting and it assumes the *first* object has all the keys required:

```yaml
- name: Bobo
  type: dog
- name: Fifi
  type: cat
```

As well as arrays of arrays of scalars (strings/numbers/booleans):

```yaml
- [Bobo, dog]
- [Fifi, cat]
```

## Decode

Decode assumes the first CSV/TSV row is the header row, and all rows beneath are the entries. The data will be coded into an array of objects, using the header rows as keys.

```csv
name,type
Bobo,dog
Fifi,cat
```

## Encode CSV simple

Given a sample.yml file of:

```yaml
- [i, like, csv]
- [because, excel, is, cool]
```

then

```bash
yq -o=csv sample.yml
```

will output

```csv
i,like,csv
because,excel,is,cool
```

## Encode TSV simple

Given a sample.yml file of:

```yaml
- [i, like, csv]
- [because, excel, is, cool]
```

then

```bash
yq -o=tsv sample.yml
```

will output

```tsv
i	like	csv
because	excel	is	cool
```

## Encode array of objects to csv

Given a sample.yml file of:

```yaml
- name: Gary
  numberOfCats: 1
  likesApples: true
  height: 168.8
- name: Samantha's Rabbit
  numberOfCats: 2
  likesApples: false
  height: -188.8

```

then

```bash
yq -o=csv sample.yml
```

will output

```csv
name,numberOfCats,likesApples,height
Gary,1,true,168.8
Samantha's Rabbit,2,false,-188.8
```

## Encode array of objects to custom csv format

Add the header row manually, then the we convert each object into an array of values - resulting in an array of arrays. Pick the columns and call the header whatever you like.

Given a sample.yml file of:

```yaml
- name: Gary
  numberOfCats: 1
  likesApples: true
  height: 168.8
- name: Samantha's Rabbit
  numberOfCats: 2
  likesApples: false
  height: -188.8

```

then

```bash
yq -o=csv '[["Name", "Number of Cats"]] +  [.[] | [.name, .numberOfCats ]]' sample.yml
```

will output

```csv
Name,Number of Cats
Gary,1
Samantha's Rabbit,2
```

## Encode array of objects to csv - missing fields behaviour

First entry is used to determine the headers, and it is missing 'likesApples', so it is not included in the csv. Second entry does not have 'numberOfCats' so that is blank

Given a sample.yml file of:

```yaml
- name: Gary
  numberOfCats: 1
  height: 168.8
- name: Samantha's Rabbit
  height: -188.8
  likesApples: false

```

then

```bash
yq -o=csv sample.yml
```

will output

```csv
name,numberOfCats,height
Gary,1,168.8
Samantha's Rabbit,,-188.8
```

## Parse CSV into an array of objects

First row is assumed to be the header row. By default, entries with YAML/JSON formatting will be parsed!

Given a sample.csv file of:

```csv
name,numberOfCats,likesApples,height,facts
Gary,1,true,168.8,cool: true
Samantha's Rabbit,2,false,-188.8,tall: indeed

```

then

```bash
yq -p=csv sample.csv
```

will output

```yaml
- name: Gary
  numberOfCats: 1
  likesApples: true
  height: 168.8
  facts:
    cool: true
- name: Samantha's Rabbit
  numberOfCats: 2
  likesApples: false
  height: -188.8
  facts:
    tall: indeed
```

## Parse CSV into an array of objects, no auto-parsing

First row is assumed to be the header row. Entries with YAML/JSON will be left as strings.

Given a sample.csv file of:

```csv
name,numberOfCats,likesApples,height,facts
Gary,1,true,168.8,cool: true
Samantha's Rabbit,2,false,-188.8,tall: indeed

```

then

```bash
yq -p=csv --csv-auto-parse=f sample.csv
```

will output

```yaml
- name: Gary
  numberOfCats: 1
  likesApples: true
  height: 168.8
  facts: 'cool: true'
- name: Samantha's Rabbit
  numberOfCats: 2
  likesApples: false
  height: -188.8
  facts: 'tall: indeed'
```

## Parse TSV into an array of objects

First row is assumed to be the header row.

Given a sample.tsv file of:

```tsv
name	numberOfCats	likesApples	height
Gary	1	true	168.8
Samantha's Rabbit	2	false	-188.8

```

then

```bash
yq -p=tsv sample.tsv
```

will output

```yaml
- name: Gary
  numberOfCats: 1
  likesApples: true
  height: 168.8
- name: Samantha's Rabbit
  numberOfCats: 2
  likesApples: false
  height: -188.8
```

## Round trip

Given a sample.csv file of:

```csv
name,numberOfCats,likesApples,height
Gary,1,true,168.8
Samantha's Rabbit,2,false,-188.8

```

then

```bash
yq -p=csv -o=csv '(.[] | select(.name == "Gary") | .numberOfCats) = 3' sample.csv
```

will output

```csv
name,numberOfCats,likesApples,height
Gary,3,true,168.8
Samantha's Rabbit,2,false,-188.8
```


# Working with JSON

Encode and decode to and from JSON. Supports multiple JSON documents in a single file (e.g. NDJSON).

Note that YAML is a superset of (single document) JSON - so you don't have to use the JSON parser to read JSON when there is only one JSON document in the input. You will probably want to pretty print the result in this case, to get idiomatic YAML styling.

## Parse json: simple

JSON is a subset of yaml, so all you need to do is prettify the output

Given a sample.json file of:

```json
{"cat": "meow"}
```

then

```bash
yq -p=json sample.json
```

will output

```yaml
cat: meow
```

## Parse json: complex

JSON is a subset of yaml, so all you need to do is prettify the output

Given a sample.json file of:

```json
{"a":"Easy! as one two three","b":{"c":2,"d":[3,4]}}
```

then

```bash
yq -p=json sample.json
```

will output

```yaml
a: Easy! as one two three
b:
  c: 2
  d:
    - 3
    - 4
```

## Encode json: simple

Given a sample.yml file of:

```yaml
cat: meow
```

then

```bash
yq -o=json '.' sample.yml
```

will output

```json
{
  "cat": "meow"
}
```

## Encode json: simple - in one line

Given a sample.yml file of:

```yaml
cat: meow # this is a comment, and it will be dropped.
```

then

```bash
yq -o=json -I=0 '.' sample.yml
```

will output

```json
{"cat":"meow"}
```

## Encode json: comments

Given a sample.yml file of:

```yaml
cat: meow # this is a comment, and it will be dropped.
```

then

```bash
yq -o=json '.' sample.yml
```

will output

```json
{
  "cat": "meow"
}
```

## Encode json: anchors

Anchors are dereferenced

Given a sample.yml file of:

```yaml
cat: &ref meow
anotherCat: *ref
```

then

```bash
yq -o=json '.' sample.yml
```

will output

```json
{
  "cat": "meow",
  "anotherCat": "meow"
}
```

## Encode json: multiple results

Each matching node is converted into a json doc. This is best used with 0 indent (json document per line)

Given a sample.yml file of:

```yaml
things: [{stuff: cool}, {whatever: cat}]
```

then

```bash
yq -o=json -I=0 '.things[]' sample.yml
```

will output

```json
{"stuff":"cool"}
{"whatever":"cat"}
```

## Roundtrip JSON Lines / NDJSON

Given a sample.json file of:

```json
{"this": "is a multidoc json file"}
{"each": ["line is a valid json document"]}
{"a number": 4}

```

then

```bash
yq -p=json -o=json -I=0 sample.json
```

will output

```yaml
{"this":"is a multidoc json file"}
{"each":["line is a valid json document"]}
{"a number":4}
```

## Roundtrip multi-document JSON

The parser can also handle multiple multi-line json documents in a single file (despite this not being in the JSON Lines / NDJSON spec). Typically you would have one entire JSON document per line, but the parser also supports multiple multi-line json documents

Given a sample.json file of:

```json
{
	"this": "is a multidoc json file"
}
{
	"it": [
		"has",
		"consecutive",
		"json documents"
	]
}
{
	"a number": 4
}

```

then

```bash
yq -p=json -o=json -I=2 sample.json
```

will output

```yaml
{
  "this": "is a multidoc json file"
}
{
  "it": [
    "has",
    "consecutive",
    "json documents"
  ]
}
{
  "a number": 4
}
```

## Update a specific document in a multi-document json

Documents are indexed by the `documentIndex` or `di` operator.

Given a sample.json file of:

```json
{"this": "is a multidoc json file"}
{"each": ["line is a valid json document"]}
{"a number": 4}

```

then

```bash
yq -p=json -o=json -I=0 '(select(di == 1) | .each ) += "cool"' sample.json
```

will output

```yaml
{"this":"is a multidoc json file"}
{"each":["line is a valid json document","cool"]}
{"a number":4}
```

## Find and update a specific document in a multi-document json

Use expressions as you normally would.

Given a sample.json file of:

```json
{"this": "is a multidoc json file"}
{"each": ["line is a valid json document"]}
{"a number": 4}

```

then

```bash
yq -p=json -o=json -I=0 '(select(has("each")) | .each ) += "cool"' sample.json
```

will output

```yaml
{"this":"is a multidoc json file"}
{"each":["line is a valid json document","cool"]}
{"a number":4}
```

## Decode JSON Lines / NDJSON

Given a sample.json file of:

```json
{"this": "is a multidoc json file"}
{"each": ["line is a valid json document"]}
{"a number": 4}

```

then

```bash
yq -p=json sample.json
```

will output

```yaml
this: is a multidoc json file
---
each:
  - line is a valid json document
---
a number: 4
```


# Working with Properties

Encode/Decode/Roundtrip to/from a property file. Line comments on value nodes will be copied across.

By default, empty maps and arrays are not encoded - see below for an example on how to encode a value for these.

## Encode properties

Note that empty arrays and maps are not encoded by default.

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props sample.yml
```

will output

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets.0 = cat
person.pets.1.nested.0 = list entry
person.food.0 = pizza
```

## Encode properties with array brackets

Declare the --properties-array-brackets flag to give array paths in brackets (e.g. SpringBoot).

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props --properties-array-brackets sample.yml
```

will output

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets[0] = cat
person.pets[1].nested[0] = list entry
person.food[0] = pizza
```

## Encode properties - custom separator

Use the --properties-separator flag to specify your own key/value separator.

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props --properties-separator=" :@ " sample.yml
```

will output

```properties
# block comments come through
# comments on values appear
person.name :@ Mike Wazowski

# comments on array values appear
person.pets.0 :@ cat
person.pets.1.nested.0 :@ list entry
person.food.0 :@ pizza
```

## Encode properties: scalar encapsulation

Note that string values with blank characters in them are encapsulated with double quotes

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props --unwrapScalar=false sample.yml
```

will output

```properties
# block comments come through
# comments on values appear
person.name = "Mike Wazowski"

# comments on array values appear
person.pets.0 = cat
person.pets.1.nested.0 = "list entry"
person.food.0 = pizza
```

## Encode properties: no comments

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props '... comments = ""' sample.yml
```

will output

```properties
person.name = Mike Wazowski
person.pets.0 = cat
person.pets.1.nested.0 = list entry
person.food.0 = pizza
```

## Encode properties: include empty maps and arrays

Use a yq expression to set the empty maps and sequences to your desired value.

Given a sample.yml file of:

```yaml
# block comments come through
person: # neither do comments on maps
    name: Mike Wazowski # comments on values appear
    pets: 
    - cat # comments on array values appear
    - nested:
        - list entry
    food: [pizza] # comments on arrays do not
emptyArray: []
emptyMap: []

```

then

```bash
yq -o=props '(.. | select( (tag == "!!map" or tag =="!!seq") and length == 0)) = ""' sample.yml
```

will output

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets.0 = cat
person.pets.1.nested.0 = list entry
person.food.0 = pizza
emptyArray = 
emptyMap = 
```

## Decode properties

Given a sample.properties file of:

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets.0 = cat
person.pets.1.nested.0 = list entry
person.food.0 = pizza

```

then

```bash
yq -p=props sample.properties
```

will output

```yaml
person:
  # block comments come through
  # comments on values appear
  name: Mike Wazowski
  pets:
    # comments on array values appear
    - cat
    - nested:
        - list entry
  food:
    - pizza
```

## Decode properties: numbers

All values are assumed to be strings when parsing properties, but you can use the `from_yaml` operator on all the strings values to autoparse into the correct type.

Given a sample.properties file of:

```properties
a.b = 10
```

then

```bash
yq -p=props ' (.. | select(tag == "!!str")) |= from_yaml' sample.properties
```

will output

```yaml
a:
  b: 10
```

## Decode properties - array should be a map

If you have a numeric map key in your property files, use array\_to\_map to convert them to maps.

Given a sample.properties file of:

```properties
things.10 = mike
```

then

```bash
yq -p=props '.things |= array_to_map' sample.properties
```

will output

```yaml
things:
  10: mike
```

## Roundtrip

Given a sample.properties file of:

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets.0 = cat
person.pets.1.nested.0 = list entry
person.food.0 = pizza

```

then

```bash
yq -p=props -o=props '.person.pets.0 = "dog"' sample.properties
```

will output

```properties
# block comments come through
# comments on values appear
person.name = Mike Wazowski

# comments on array values appear
person.pets.0 = dog
person.pets.1.nested.0 = list entry
person.food.0 = pizza
```


# Working with XML

Encode and decode to and from XML. Whitespace is not conserved for round trips - but the order of the fields are.

Consecutive xml nodes with the same name are assumed to be arrays.

XML content data, attributes processing instructions and directives are all created as plain fields.

This can be controlled by:

| Flag                     | Default                     | Sample XML                                 |
| ------------------------ | --------------------------- | ------------------------------------------ |
| `--xml-attribute-prefix` | `+` (changing to `+@` soon) | Legs in `<cat legs="4"/>`                  |
| `--xml-content-name`     | `+content`                  | Meow in `<cat>Meow <fur>true</true></cat>` |
| `--xml-directive-name`   | `+directive`                | `<!DOCTYPE config system "blah">`          |
| `--xml-proc-inst-prefix` | `+p_`                       | `<?xml version="1"?>`                      |

{% hint style="warning" %}
Default Attribute Prefix will be changing in v4.30! In order to avoid name conflicts (e.g. having an attribute named "content" will create a field that clashes with the default content name of "+content") the attribute prefix will be changing to "+@".

This will affect users that have not set their own prefix and are not roundtripping XML changes.
{% endhint %}

## Encoder / Decoder flag options

In addition to the above flags, there are the following xml encoder/decoder options controlled by flags:

| Flag                    | Default | Description                                                                                                                                                                                                                   |
| ----------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--xml-strict-mode`     | false   | Strict mode enforces the requirements of the XML specification. When switched off the parser allows input containing common mistakes. See [the Golang xml decoder ](https://pkg.go.dev/encoding/xml#Decoder)for more details. |
| `--xml-keep-namespace`  | true    | Keeps the namespace of attributes                                                                                                                                                                                             |
| `--xml-raw-token`       | true    | Does not verify that start and end elements match and does not translate name space prefixes to their corresponding URLs.                                                                                                     |
| `--xml-skip-proc-inst`  | false   | Skips over processing instructions, e.g. `<?xml version="1"?>`                                                                                                                                                                |
| `--xml-skip-directives` | false   | Skips over directives, e.g. `<!DOCTYPE config system "blah">`                                                                                                                                                                 |

See below for examples

## Parse xml: simple

Notice how all the values are strings, see the next example on how you can fix that.

Given a sample.xml file of:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<cat>
  <says>meow</says>
  <legs>4</legs>
  <cute>true</cute>
</cat>
```

then

```bash
yq -oy sample.xml
```

will output

```yaml
+p_xml: version="1.0" encoding="UTF-8"
cat:
  says: meow
  legs: "4"
  cute: "true"
```

## Parse xml: number

All values are assumed to be strings when parsing XML, but you can use the `from_yaml` operator on all the strings values to autoparse into the correct type.

Given a sample.xml file of:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<cat>
  <says>meow</says>
  <legs>4</legs>
  <cute>true</cute>
</cat>
```

then

```bash
yq -oy ' (.. | select(tag == "!!str")) |= from_yaml' sample.xml
```

will output

```yaml
+p_xml: version="1.0" encoding="UTF-8"
cat:
  says: meow
  legs: 4
  cute: true
```

## Parse xml: array

Consecutive nodes with identical xml names are assumed to be arrays.

Given a sample.xml file of:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<animal>cat</animal>
<animal>goat</animal>
```

then

```bash
yq -oy sample.xml
```

will output

```yaml
+p_xml: version="1.0" encoding="UTF-8"
animal:
  - cat
  - goat
```

## Parse xml: force as an array

In XML, if your array has a single item, then yq doesn't know its an array. This is how you can consistently force it to be an array. This handles the 3 scenarios of having nothing in the array, having a single item and having multiple.

Given a sample.xml file of:

```xml
<zoo><animal>cat</animal></zoo>
```

then

```bash
yq -oy '.zoo.animal |= ([] + .)' sample.xml
```

will output

```yaml
zoo:
  animal:
    - cat
```

## Parse xml: force all as an array

Given a sample.xml file of:

```xml
<zoo><thing><frog>boing</frog></thing></zoo>
```

then

```bash
yq -oy '.. |= [] + .' sample.xml
```

will output

```yaml
- zoo:
    - thing:
        - frog:
            - boing
```

## Parse xml: attributes

Attributes are converted to fields, with the default attribute prefix '+'. Use '--xml-attribute-prefix\` to set your own.

Given a sample.xml file of:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<cat legs="4">
  <legs>7</legs>
</cat>
```

then

```bash
yq -oy sample.xml
```

will output

```yaml
+p_xml: version="1.0" encoding="UTF-8"
cat:
  +@legs: "4"
  legs: "7"
```

## Parse xml: attributes with content

Content is added as a field, using the default content name of `+content`. Use `--xml-content-name` to set your own.

Given a sample.xml file of:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<cat legs="4">meow</cat>
```

then

```bash
yq -oy sample.xml
```

will output

```yaml
+p_xml: version="1.0" encoding="UTF-8"
cat:
  +content: meow
  +@legs: "4"
```

## Parse xml: content split between comments/children

Multiple content texts are collected into a sequence.

Given a sample.xml file of:

```xml
<root>  value  <!-- comment-->anotherValue <a>frog</a> cool!</root>
```

then

```bash
yq -oy sample.xml
```

will output

```yaml
root:
  +content: # comment
    - value
    - anotherValue
    - cool!
  a: frog
```

## Parse xml: custom dtd

DTD entities are processed as directives.

Given a sample.xml file of:

```xml

<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY writer "Blah.">
<!ENTITY copyright "Blah">
]>
<root>
    <item>&writer;&copyright;</item>
</root>
```

then

```bash
yq sample.xml
```

will output

```xml
<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY writer "Blah.">
<!ENTITY copyright "Blah">
]>
<root>
  <item>&amp;writer;&amp;copyright;</item>
</root>
```

## Parse xml: skip custom dtd

DTDs are directives, skip over directives to skip DTDs.

Given a sample.xml file of:

```xml

<?xml version="1.0"?>
<!DOCTYPE root [
<!ENTITY writer "Blah.">
<!ENTITY copyright "Blah">
]>
<root>
    <item>&writer;&copyright;</item>
</root>
```

then

```bash
yq --xml-skip-directives sample.xml
```

will output

```xml
<?xml version="1.0"?>
<root>
  <item>&amp;writer;&amp;copyright;</item>
</root>
```

## Parse xml: with comments

A best attempt is made to preserve comments.

Given a sample.xml file of:

```xml

<!-- before cat -->
<cat>
	<!-- in cat before -->
	<x>3<!-- multi
line comment 
for x --></x>
	<!-- before y -->
	<y>
		<!-- in y before -->
		<d><!-- in d before -->z<!-- in d after --></d>
		
		<!-- in y after -->
	</y>
	<!-- in_cat_after -->
</cat>
<!-- after cat -->

```

then

```bash
yq -oy sample.xml
```

will output

```yaml
# before cat
cat:
  # in cat before
  x: "3" # multi
  # line comment 
  # for x
  # before y

  y:
    # in y before
    # in d before
    d: z # in d after
    # in y after
  # in_cat_after
# after cat
```

## Parse xml: keep attribute namespace

Defaults to true

Given a sample.xml file of:

```xml
<?xml version="1.0"?>
<map xmlns="some-namespace" xmlns:xsi="some-instance" xsi:schemaLocation="some-url">
  <item foo="bar">baz</item>
  <xsi:item>foobar</xsi:item>
</map>

```

then

```bash
yq --xml-keep-namespace=false sample.xml
```

will output

```xml
<?xml version="1.0"?>
<map xmlns="some-namespace" xsi="some-instance" schemaLocation="some-url">
  <item foo="bar">baz</item>
  <item>foobar</item>
</map>
```

instead of

```xml
<?xml version="1.0"?>
<map xmlns="some-namespace" xmlns:xsi="some-instance" xsi:schemaLocation="some-url">
  <item foo="bar">baz</item>
  <xsi:item>foobar</xsi:item>
</map>
```

## Parse xml: keep raw attribute namespace

Defaults to true

Given a sample.xml file of:

```xml
<?xml version="1.0"?>
<map xmlns="some-namespace" xmlns:xsi="some-instance" xsi:schemaLocation="some-url">
  <item foo="bar">baz</item>
  <xsi:item>foobar</xsi:item>
</map>

```

then

```bash
yq --xml-raw-token=false sample.xml
```

will output

```xml
<?xml version="1.0"?>
<some-namespace:map xmlns="some-namespace" xmlns:xsi="some-instance" some-instance:schemaLocation="some-url">
  <some-namespace:item foo="bar">baz</some-namespace:item>
  <some-instance:item>foobar</some-instance:item>
</some-namespace:map>
```

instead of

```xml
<?xml version="1.0"?>
<map xmlns="some-namespace" xmlns:xsi="some-instance" xsi:schemaLocation="some-url">
  <item foo="bar">baz</item>
  <xsi:item>foobar</xsi:item>
</map>
```

## Encode xml: simple

Given a sample.yml file of:

```yaml
cat: purrs
```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<cat>purrs</cat>
```

## Encode xml: array

Given a sample.yml file of:

```yaml
pets:
  cat:
    - purrs
    - meows
```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<pets>
  <cat>purrs</cat>
  <cat>meows</cat>
</pets>
```

## Encode xml: attributes

Fields with the matching xml-attribute-prefix are assumed to be attributes.

Given a sample.yml file of:

```yaml
cat:
  +@name: tiger
  meows: true

```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<cat name="tiger">
  <meows>true</meows>
</cat>
```

## Encode xml: attributes with content

Fields with the matching xml-content-name is assumed to be content.

Given a sample.yml file of:

```yaml
cat:
  +@name: tiger
  +content: cool

```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<cat name="tiger">cool</cat>
```

## Encode xml: comments

A best attempt is made to copy comments to xml.

Given a sample.yml file of:

```yaml
#
# header comment
# above_cat
#
cat: # inline_cat
  # above_array
  array: # inline_array
    - val1 # inline_val1
    # above_val2
    - val2 # inline_val2
# below_cat

```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<!--
header comment
above_cat
-->
<!-- inline_cat -->
<cat><!-- above_array inline_array -->
  <array>val1<!-- inline_val1 --></array>
  <array><!-- above_val2 -->val2<!-- inline_val2 --></array>
</cat><!-- below_cat -->
```

## Encode: doctype and xml declaration

Use the special xml names to add/modify proc instructions and directives.

Given a sample.yml file of:

```yaml
+p_xml: version="1.0"
+directive: 'DOCTYPE config SYSTEM "/etc/iwatch/iwatch.dtd" '
apple:
  +p_coolioo: version="1.0"
  +directive: 'CATYPE meow purr puss '
  b: things

```

then

```bash
yq -o=xml sample.yml
```

will output

```xml
<?xml version="1.0"?>
<!DOCTYPE config SYSTEM "/etc/iwatch/iwatch.dtd" >
<apple><?coolioo version="1.0"?><!CATYPE meow purr puss >
  <b>things</b>
</apple>
```

## Round trip: with comments

A best effort is made, but comment positions and white space are not preserved perfectly.

Given a sample.xml file of:

```xml

<!-- before cat -->
<cat>
	<!-- in cat before -->
	<x>3<!-- multi
line comment 
for x --></x>
	<!-- before y -->
	<y>
		<!-- in y before -->
		<d><!-- in d before -->z<!-- in d after --></d>
		
		<!-- in y after -->
	</y>
	<!-- in_cat_after -->
</cat>
<!-- after cat -->

```

then

```bash
yq sample.xml
```

will output

```xml
<!-- before cat -->
<cat><!-- in cat before -->
  <x>3<!-- multi
line comment 
for x --></x><!-- before y -->
  <y><!-- in y before
in d before -->
    <d>z<!-- in d after --></d><!-- in y after -->
  </y><!-- in_cat_after -->
</cat><!-- after cat -->
```

## Roundtrip: with doctype and declaration

yq parses XML proc instructions and directives into nodes. Unfortunately the underlying XML parser loses whitespace information.

Given a sample.xml file of:

```xml
<?xml version="1.0"?>
<!DOCTYPE config SYSTEM "/etc/iwatch/iwatch.dtd" >
<apple>
  <?coolioo version="1.0"?>
  <!CATYPE meow purr puss >
  <b>things</b>
</apple>

```

then

```bash
yq sample.xml
```

will output

```xml
<?xml version="1.0"?>
<!DOCTYPE config SYSTEM "/etc/iwatch/iwatch.dtd" >
<apple><?coolioo version="1.0"?><!CATYPE meow purr puss >
  <b>things</b>
</apple>
```


# Working with HCL

Encode and decode to and from [HashiCorp Configuration Language (HCL)](https://github.com/hashicorp/hcl).

HCL is commonly used in HashiCorp tools like Terraform for configuration files. The yq HCL encoder and decoder support:

* Blocks and attributes
* String interpolation and expressions (preserved without quotes)
* Comments (leading, head, and line comments)
* Nested structures (maps and lists)
* Syntax colorization when enabled

## Parse HCL

Given a sample.hcl file of:

```hcl
io_mode = "async"
```

then

```bash
yq -oy sample.hcl
```

will output

```yaml
io_mode: "async"
```

## Roundtrip: Sample Doc

Given a sample.hcl file of:

```hcl
service "cat" {
  process "main" {
    command = ["/usr/local/bin/awesome-app", "server"]
  }

  process "management" {
    command = ["/usr/local/bin/awesome-app", "management"]
  }
}

```

then

```bash
yq sample.hcl
```

will output

```hcl
service "cat" {
  process "main" {
    command = ["/usr/local/bin/awesome-app", "server"]
  }
  process "management" {
    command = ["/usr/local/bin/awesome-app", "management"]
  }
}
```

## Roundtrip: With an update

Given a sample.hcl file of:

```hcl
service "cat" {
  process "main" {
    command = ["/usr/local/bin/awesome-app", "server"]
  }

  process "management" {
    command = ["/usr/local/bin/awesome-app", "management"]
  }
}

```

then

```bash
yq '.service.cat.process.main.command += "meow"' sample.hcl
```

will output

```hcl
service "cat" {
  process "main" {
    command = ["/usr/local/bin/awesome-app", "server", "meow"]
  }
  process "management" {
    command = ["/usr/local/bin/awesome-app", "management"]
  }
}
```

## Parse HCL: Sample Doc

Given a sample.hcl file of:

```hcl
service "cat" {
  process "main" {
    command = ["/usr/local/bin/awesome-app", "server"]
  }

  process "management" {
    command = ["/usr/local/bin/awesome-app", "management"]
  }
}

```

then

```bash
yq -oy sample.hcl
```

will output

```yaml
service:
  cat:
    process:
      main:
        command:
          - "/usr/local/bin/awesome-app"
          - "server"
      management:
        command:
          - "/usr/local/bin/awesome-app"
          - "management"
```

## Parse HCL: with comments

Given a sample.hcl file of:

```hcl
# Configuration
port = 8080 # server port
```

then

```bash
yq -oy sample.hcl
```

will output

```yaml
# Configuration
port: 8080 # server port
```

## Roundtrip: with comments

Given a sample.hcl file of:

```hcl
# Configuration
port = 8080
```

then

```bash
yq sample.hcl
```

will output

```hcl
# Configuration
port = 8080
```

## Roundtrip: With templates, functions and arithmetic

Given a sample.hcl file of:

```hcl
# Arithmetic with literals and application-provided variables
sum = 1 + addend

# String interpolation and templates
message = "Hello, ${name}!"

# Application-provided functions
shouty_message = upper(message)
```

then

```bash
yq sample.hcl
```

will output

```hcl
# Arithmetic with literals and application-provided variables
sum = 1 + addend
# String interpolation and templates
message = "Hello, ${name}!"
# Application-provided functions
shouty_message = upper(message)
```

## Roundtrip: Separate blocks with same name.

Given a sample.hcl file of:

```hcl
resource "aws_instance" "web" {
  ami = "ami-12345"
}
resource "aws_instance" "db" {
  ami = "ami-67890"
}
```

then

```bash
yq sample.hcl
```

will output

```hcl
resource "aws_instance" "web" {
  ami = "ami-12345"
}
resource "aws_instance" "db" {
  ami = "ami-67890"
}
```


# Working with LUA

### Basic input example

Given a sample.lua file of:

```lua
return {
	["country"] = "Australia"; -- this place
	["cities"] = {
		"Sydney",
		"Melbourne",
		"Brisbane",
		"Perth",
	};
};

```

then

```bash
yq -oy '.' sample.lua
```

will output

```yaml
country: Australia
cities:
  - Sydney
  - Melbourne
  - Brisbane
  - Perth
```

### Basic output example

Given a sample.yml file of:

```yaml
---
country: Australia # this place
cities:
- Sydney
- Melbourne
- Brisbane
- Perth
```

then

```bash
yq -o=lua '.' sample.yml
```

will output

```lua
return {
	["country"] = "Australia"; -- this place
	["cities"] = {
		"Sydney",
		"Melbourne",
		"Brisbane",
		"Perth",
	};
};
```

### Unquoted keys

Uses the `--lua-unquoted` option to produce a nicer-looking output.

Given a sample.yml file of:

```yaml
---
country: Australia # this place
cities:
- Sydney
- Melbourne
- Brisbane
- Perth
```

then

```bash
yq -o=lua --lua-unquoted '.' sample.yml
```

will output

```lua
return {
	country = "Australia"; -- this place
	cities = {
		"Sydney",
		"Melbourne",
		"Brisbane",
		"Perth",
	};
};
```

### Globals

Uses the `--lua-globals` option to export the values into the global scope.

Given a sample.yml file of:

```yaml
---
country: Australia # this place
cities:
- Sydney
- Melbourne
- Brisbane
- Perth
```

then

```bash
yq -o=lua --lua-globals '.' sample.yml
```

will output

```lua
country = "Australia"; -- this place
cities = {
	"Sydney",
	"Melbourne",
	"Brisbane",
	"Perth",
};
```

### Elaborate example

Given a sample.yml file of:

```yaml
---
hello: world
tables:
  like: this
  keys: values
  ? look: non-string keys
  : True
numbers:
  - decimal: 12345
  - hex: 0x7fabc123
  - octal: 0o30
  - float: 123.45
  - infinity: .inf
    plus_infinity: +.inf
    minus_infinity: -.inf
  - not: .nan

```

then

```bash
yq -o=lua '.' sample.yml
```

will output

```lua
return {
	["hello"] = "world";
	["tables"] = {
		["like"] = "this";
		["keys"] = "values";
		[{
			["look"] = "non-string keys";
		}] = true;
	};
	["numbers"] = {
		{
			["decimal"] = 12345;
		},
		{
			["hex"] = 0x7fabc123;
		},
		{
			["octal"] = 24;
		},
		{
			["float"] = 123.45;
		},
		{
			["infinity"] = (1/0);
			["plus_infinity"] = (1/0);
			["minus_infinity"] = (-1/0);
		},
		{
			["not"] = (0/0);
		},
	};
};
```


# Working with TOML

Decode from TOML. Note that `yq` does not yet support outputting in TOML format (and therefore it cannot roundtrip)

## Parse: Simple

Given a sample.toml file of:

```toml
A = "hello"
B = 12

```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
A: hello
B: 12
```

## Parse: Deep paths

Given a sample.toml file of:

```toml
person.name = "hello"
person.address = "12 cat st"

```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
person:
  name: hello
  address: 12 cat st
```

## Encode: Scalar

Given a sample.toml file of:

```toml
person.name = "hello"
person.address = "12 cat st"

```

then

```bash
yq '.person.name' sample.toml
```

will output

```yaml
hello
```

## Parse: inline table

Given a sample.toml file of:

```toml
name = { first = "Tom", last = "Preston-Werner" }
```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
name:
  first: Tom
  last: Preston-Werner
```

## Parse: Array Table

Given a sample.toml file of:

```toml

[owner.contact]
name = "Tom Preston-Werner"
age = 36

[[owner.addresses]]
street = "first street"
suburb = "ok"

[[owner.addresses]]
street = "second street"
suburb = "nice"

```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
owner:
  contact:
    name: Tom Preston-Werner
    age: 36
  addresses:
    - street: first street
      suburb: ok
    - street: second street
      suburb: nice
```

## Parse: Array of Array Table

Given a sample.toml file of:

```toml

[[fruits]]
name = "apple"
[[fruits.varieties]]  # nested array of tables
name = "red delicious"
```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
fruits:
  - name: apple
    varieties:
      - name: red delicious
```

## Parse: Empty Table

Given a sample.toml file of:

```toml

[dependencies]

```

then

```bash
yq -oy '.' sample.toml
```

will output

```yaml
dependencies: {}
```


# Working with Shell Output

### Encode shell variables

Note that comments are dropped and values will be enclosed in single quotes as needed.

Given a sample.yml file of:

```yaml
# comment
name: Mike Wazowski
eyes:
  color: turquoise
  number: 1
friends:
  - James P. Sullivan
  - Celia Mae
```

then

```bash
yq -o=shell sample.yml
```

will output

```sh
name='Mike Wazowski'
eyes_color=turquoise
eyes_number=1
friends_0='James P. Sullivan'
friends_1='Celia Mae'
```

### Encode shell variables: illegal variable names as key.

Keys that would be illegal as variable keys are adapted.

Given a sample.yml file of:

```yaml
ascii_=_symbols: replaced with _
"ascii_	_controls": dropped (this example uses \t)
nonascii_א_characters: dropped
effort_expeñded_tò_preserve_accented_latin_letters: moderate (via unicode NFKD)

```

then

```bash
yq -o=shell sample.yml
```

will output

```sh
ascii___symbols='replaced with _'
ascii__controls='dropped (this example uses \t)'
nonascii__characters=dropped
effort_expended_to_preserve_accented_latin_letters='moderate (via unicode NFKD)'
```

### Encode shell variables: empty values, arrays and maps

Empty values are encoded to empty variables, but empty arrays and maps are skipped.

Given a sample.yml file of:

```yaml
empty:
  value:
  array: []
  map:   {}
```

then

```bash
yq -o=shell sample.yml
```

will output

```sh
empty_value=
```

### Encode shell variables: single quotes in values

Single quotes in values are encoded as '"'"' (close single quote, double-quoted single quote, open single quote).

Given a sample.yml file of:

```yaml
name: Miles O'Brien
```

then

```bash
yq -o=shell sample.yml
```

will output

```sh
name='Miles O'"'"'Brien'
```

### Encode shell variables: custom separator

Use --shell-key-separator to specify a custom separator between keys. This is useful when the original keys contain underscores.

Given a sample.yml file of:

```yaml
my_app:
  db_config:
    host: localhost
    port: 5432
```

then

```bash
yq -o=shell --shell-key-separator="__" sample.yml
```

will output

```sh
my_app__db_config__host=localhost
my_app__db_config__port=5432
```


# Front Matter

`yq` can process files with `yaml` front matter (e.g. jekyll, assemble and others) - this is done via the `--front-matter/-f` flag.

Note that `yq` only processes the first passed in file for front-matter. If you'd like to process multiple files, you can:

```bash
find -name  "*.md" -exec yq --front-matter="process" '.updated_at = now' {} \;
```

## Process front matter

Use `--front-matter=process` to process the front matter, that is run the expression against the `yaml` content, and output back the entire file, included the non-yaml content block. For example:

File:

```
---
a: apple
b: bannana
---
<h1>I like {{a}} and {{b}} </h1>
```

The running

```
yq --front-matter=process '.a="chocolate"' file.jekyll
```

Will yield:

```
---
a: chocolate
b: bannana
---
<h1>I like {{a}} and {{b}} </h1>
```

## Extract front matter

Running with `--front-matter=extract` will only output the yaml contents and ignore the rest. From the previous example, if you were to instead run:

```
yq --front-matter=extract '.a="chocolate"' file.jekyll
```

Then this would yield:

```
---
a: chocolate
b: bannana
```


# Split into multiple files

`yq` can split out the results into multiple files with the `--split-exp/s` flag. You will need to give this flag an expression (that returns a string), this will be used as the filename for each result. In this expression, you can use `$index` to represent the result index in the name, if desired.

## Split documents into files

Given a file like

```yaml
a: test_doc1
--- 
a: test_doc2
```

Then running:

```bash
yq -s '.a' myfile.yml
```

will result in two files:

test\_doc1.yml:

```yaml
a: test_doc1
```

test\_doc2.yml:

```yaml
---
a: test_doc2
```

TIP: if you don't want the leading document separators (`---`), then run with the `--no-doc` flag.

## Split documents into files, using index

This is like the example above, but we'll use `$index` for the filename. Note that this variable is only defined for the `--split-exp/s` flag.

```
yq -s '"file_" + $index' myfile.yml
```

This will create two files, `file_0.yml` and `file_1.yml`.

## Split single document into files

You can also split results into separate files. Notice

```yaml
- name: bob
  age: 23
- name: tim
  age: 17
```

Then, by splatting the array into individual results, we can split the content into several files:

```bash
yq '.[]' file.yml -s '"user_" + .name'
```

will result in two files:

user\_bob.yml:

```yaml
name: bob
age: 23
```

user\_tim.yml:

```yaml
name: tim
age: 17
```


# GitHub Action

## Guide

You can use `yq` in your GitHub action, for instance:

```yaml
  - uses: actions/checkout@v2
  - name: Get SDK Version from config
    id: lookupSdkVersion
    uses: mikefarah/yq@master
    with:
      cmd: yq '.renutil.version' 'config.yml'
  - name: Restore Cache
    id: restore-cache
    uses: actions/cache@v2
    with:
      path: ../renpy
      key:  ${{ runner.os }}-sdk-${{ steps.lookupSdkVersion.outputs.result }}
      restore-keys: |
        ${{ runner.os }}-sdk
  # ... more
```

The `yq` action sets a `result` variable in its output, making it available to subsequent steps. In this case it's available as `steps.lookupSdkVersion.outputs.result`.

Details of how the GitHub action itself is configured can be found [here](https://github.com/mikefarah/yq/issues/844#issuecomment-856700574)

If you [enable step debug logging](https://docs.github.com/en/actions/managing-workflow-runs/enabling-debug-logging#enabling-step-debug-logging), you can see additional information about the exact command sent as well as the response returned within the GitHub Action logs.

Thanks @[**devorbitus**](https://github.com/devorbitus)**!**

## Environment variables with Github Actions:

GitHub Actions escape and interpolate rules can conflict with some yq syntax. Here is an example of how to quote a variable that could contain dots in a query path (more usage context: ambanum/OpenTermsArchive#899).

```yaml
  - name: Get an entry with a variable that might contain dots or spaces
    id: get_username
    uses: mikefarah/yq@master
    with:
      cmd: yq '.all.children.["${{ matrix.ip_address }}"].username' ops/inventories/production.yml
  - name: Reuse a variable obtained in another step
    run: echo ${{ steps.get_username.outputs.result }}
```

Thanks @MattiSG!

## Troubleshooting

### Write in-place file permission errors

The default user in github action dockerfiles (at the time of writing) seems to be 1001. This is what the `yq` github action is configured to run with (see the docker file [here](https://github.com/mikefarah/yq/blob/master/github-action/Dockerfile))

There's a working example defined [here](https://github.com/mikefarah/yq/blob/master/.github/workflows/test-yq.yml) and you can see the Github action [results here](https://github.com/mikefarah/yq/actions/workflows/test-yq.yml)

If you need to set the action to another user, follow the advice [here](https://stackoverflow.com/questions/58955666/how-to-set-the-docker-user-in-github-actions).


# Tips, Tricks, Troubleshooting

## Validating yaml files

Yaml files can be surprisingly lenient in what can be parsed as a yaml file. A reasonable way of validation a yaml file is to ensure the top level is a map or array (although it is valid yaml to have scalars at the top level, but often this is not what you want). This can be done by:

```
yq --exit-status 'tag == "!!map" or tag== "!!seq"' file.txt > /dev/null
```

## Split expressions over multiple lines to improve readability

Feel free to use multiple lines in your expression to improve readability.

Use `with` if you need to make several updates to the same path.

Use `# comments` to explain things

```bash
yq --inplace '
  with(.a.deeply.nested;
    . = "newValue" | . style="single" # line comment about styles
  ) |
  #
  # Block comment that explains what is happening.
  #
  with(.b.another.nested; 
    . = "cool" | . style="folded"
  )
' my_file.yaml
```

## Create bash array

Given a yaml file like

```yaml
coolActions:
  - create
  - edit
  - delete
```

You can create a bash array named `actions` by:

```bash
> readarray actions < <(yq '.coolActions[]' sample.yaml)
> echo "${actions[1]}"
edit
```

## yq in a bash loop

For a given yaml file like:

```
identities:
- arn: "arn:aws:iam::ARN1"
  group: "system:masters"
  user: "user1"
- arn: "arn:aws:iam::ARN2"
  group: "system:masters"
  user: "user2"
```

You can loop over the results in a bash loop like:

```
# load array into a bash array
# output each entry as a single line json
readarray identityMappings < <(yq -o=j -I=0 '.identities[]' test.yml )

for identityMapping in "${identityMappings[@]}"; do
    # identity mapping is a single json snippet representing a single entry
    roleArn=$(echo "$identityMapping" | yq '.arn' -)
    echo "roleArn: $roleArn"
done

```

## Set contents from another file

Use the [load](https://mikefarah.gitbook.io/yq/operators/load) operator to load contents from another file.

## Special characters in strings

The `strenv` operator is a great way to handle special characters in strings:

```bash
VAL='.a |!@  == "string2"' yq '.a = strenv(VAL)' example.yaml
```

## Update multiple files

`yq` doesn't have a way of updating multiple files in a single command (yet?) - but you can use your shell's built in tools like `find`:

```
find *.yaml -exec yq '. += "cow"' -i {} \;
```

This will run the `'. += "cow"'` expression against every matching file, and update it in place (`-i`).

## String blocks and newline issues

There are a couple of tricks to getting the right string representation, take a look at [string operators](https://mikefarah.gitbook.io/yq/operators/string-operators#string-blocks-bash-and-newlines) for more details:

## Quotes in Windows Powershell

Powershell has its [own](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-7.1) way of handling quotes:

```bash
PS > yq -n '.test = ""something""'
test: something
PS >
```

See <https://github.com/mikefarah/yq/issues/747> for more trickery.

## Merge / combine all documents into one

To merge all given yaml files into one, use the `reduce` operator with the `*` (multiply) operator. Note the use of `ea` or `eval-all` to load all files into memory so that they can be merged.

```
yq ea '. as $item ireduce ({}; . * $item )' file1.yml file2.yml ...
```

## Merge - showing the source file and line

To see the original source file and line number of your merged result, you can pre-process the files and add that information in as line comments, then perform the merge.

```bash
yq ea '(..  lineComment |= filename + ":" + line) | select(fi==0) * select(fi==1)' data1.yaml data2.yaml
```

## Merge an array of objects by key

See [here](https://mikefarah.gitbook.io/yq/operators/multiply-merge#merge-arrays-of-objects-together-matching-on-a-key) for a working example.

## Creating a new file / working with blank documents

To create a new `yaml` file simply:

```
yq -n '.someNew="content"' > newfile.yml
```

## Comparing yaml files

The best way to run a diff is to use `yq` to normalise the yaml files and then just use diff. Here is a simple example of using pretty print `-P` to normalise the styling and running diff:

```
diff <(yq -P 'sort_keys(..)' -o=props file1.yaml) <(yq -P 'sort_keys(..)' -o=props file2.yaml)
```

This way you can use the full power of `diff` and normalise the yaml files as you like.

You may also want to remove all comments using `... comments=""`

## Reading multiple streams (STDINs)

Like `diff` and other bash commands, you can use `<(exp)` to pipe in multiple streams of data into `yq`. instance:

```
yq '.apple' <(curl -s https://somewhere/data1.yaml) <(cat file.yml)
```

## Updating deeply selected paths

### or why is yq only returning the updated yaml

The most important thing to remember to do is to have brackets around the LHS expression - otherwise what `yq` will do is first filter by the selection, and then, separately, update the filtered result and return that subset.

```
yq '(.foo.bar[] | select(.name == "fred") | .apple) = "cool"'
```

## Combining multiple files into one

In order to combine multiple yaml files into a single file (with `---` separators) you can just:

```
yq '.' somewhere/*.yaml
```

## Multiple updates to the same path

You can use the [with](https://mikefarah.gitbook.io/yq/operators/with) operator to set a nested context:

```
yq 'with(.a.deeply ; .nested = "newValue" | .other= "newThing")' sample.yml
```

The first argument expression sets the root context, and the second expression runs against that root context.

## Logic without if/elif/else

`yq` has not yet added `if` expressions - however you should be able to use `with` and `select` to achieve the same outcome. Lets use an example:

```yaml
- animal: cat
- animal: dog
- animal: frog
```

Now, if you were using good ol' jq - you may have a script with `if`s like so:

```bash
jq ' .[] |=
if (.animal == "cat") then
  .noise = "meow" |
  .whiskers = true
elif (.animal == "dog") then
  .noise = "woof" |
  .happy = true
else 
  .noise = "??"
end
' < file.yaml
```

Using `yq` - you can get the same result by:

```bash
yq '.[] |= (
  with(select(.animal == "cat"); 
    .noise = "meow" | 
    .whiskers = true
  ) |
  with(select(.animal == "dog"); 
    .noise = "woof" | 
    .happy = true
  ) |
  with(select(.noise == null); 
    .noise = "???"
  )
)' < file.yml
```

Note that the logic isn't quite the same, as there is no concept of 'else'. So you may need to put additional logic in the expressions, as this has for the 'else' logic.

## yq adds a !!merge tag automatically

The merge functionality from yaml v1.1 (e.g. `<<:`has actually been removed in the 1.2 spec. Thankfully, `yq` underlying yaml parser still supports that tag - and it's extra nice in that it explicitly puts the `!!merge` tag on key of the map entry. This tag tells other yaml parsers that this entry is a merge entry, as opposed to a regular string key that happens to have a value of `<<:`. This is backwards compatible with the 1.1 spec of yaml, it's simply an explicit way of specifying the type (for instance, you can use a `!!str` tag to enforce a particular value to be a string.

Although this does affect the readability of the yaml to humans, it still works and processes fine with various yaml processors.


# yq

yq is a lightweight and portable command-line YAML processor

&#x20;![Build](https://github.com/mikefarah/yq/workflows/Build/badge.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/mikefarah/yq.svg) ![Github Releases (by Release)](https://img.shields.io/github/downloads/mikefarah/yq/total.svg) ![Go Report](https://goreportcard.com/badge/github.com/mikefarah/yq)

## Deprecated Notice

v3 is now deprecated, critical bug fixes and security fixes will still be applied until August 2021.

## Install

`yq` has pre-built binaries for most platforms - checkout the [releases page](https://github.com/mikefarah/yq/releases) for the latest build. Alternatively - you can use one of the methods below:

### MacOs / Linux via Homebrew:

```bash
brew install yq@3
```

Note that as this is a versioned brew it will not add the `yq` command to your path automatically. Please follow the instructions given by brew upon installation.

### On Windows:

```bash
choco install yq
```

Kindly maintained by @chillum (<https://github.com/chillum/choco-packages/tree/master/yq>), <https://chocolatey.org/packages/yq>

### Alpine Linux

* Enable edge/community repo by adding `$MIRROR/alpine/edge/community` to `/etc/apk/repositories`
* Update database index with `apk update`
* Install yq with `apk add yq`

Supported by Tuan Hoang <https://pkgs.alpinelinux.org/package/edge/community/x86/yq>

### On Ubuntu and other Linux distributions supporting `snap` packages:

```bash
snap install yq --channel=v3/stable
```

#### Snap notes

`yq` installs with with [*strict confinement*](https://docs.snapcraft.io/snap-confinement/6233) in snap, this means it doesn't have direct access to root files. To read root files you can:

```bash
sudo cat /etc/myfile | yq r - somecommand
```

And to write to a root file you can either use [sponge](https://linux.die.net/man/1/sponge):

```bash
sudo cat /etc/myfile | yq r - somecommand | sudo sponge /etc/myfile
```

or write to a temporary file:

```bash
sudo cat /etc/myfile | yq r - somecommand | sudo tee /etc/myfile.tmp
sudo mv /etc/myfile.tmp /etc/myfile
rm /etc/myfile.tmp
```

### On Ubuntu 16.04 or higher from Debian package:

```bash
sudo add-apt-repository ppa:rmescandon/yq
sudo apt update
sudo apt install yq -y
```

Kindly maintained by @rmescandon

### go get:

```
GO111MODULE=on go get github.com/mikefarah/yq/v3
```

## Docker

Oneshot use:

```bash
docker run --rm -v ${PWD}:/workdir mikefarah/yq yq [flags] <command> FILE...
```

Run commands interactively:

```bash
docker run --rm -it -v ${PWD}:/workdir mikefarah/yq sh
```

It can be useful to have a bash function to avoid typing the whole docker command:

```bash
yq() {
  docker run --rm -i -v ${PWD}:/workdir mikefarah/yq yq $@
}
```

## Parsing engine and YAML spec support

Under the hood, yq uses [go-yaml v3](https://github.com/go-yaml/yaml/tree/v3) as the yaml parser, which supports [yaml spec 1.2](https://yaml.org/spec/1.2/spec.html). In particular, note that in 1.2 the values 'yes'/'no' are no longer interpreted as booleans, but as strings.


# Upgrading from V2

New features and breaking changes

## New Features

* Keeps yaml comments and formatting, can specify yaml [tags](https://mikefarah.gitbook.io/yq/usage/value-parsing#using-the-tag-field-to-override) when updating.
* Handles anchors!
* Can print out matching paths and values when splatting, more info [here](https://mikefarah.gitbook.io/yq/commands/read#printing-matching-paths).
* JSON output works for all commands! Yaml files with multiple documents are printed out as one JSON document per line, more info [here](https://mikefarah.gitbook.io/yq/usage/convert)
* Deep splat (`**`) to match arbitrary paths and match nodes by their children, more info [here](https://mikefarah.gitbook.io/yq/usage/path-expressions)

## Breaking Changes

### Parsing values from the CLI

In V3 users are able to better control how values are treated when updating YAML by using a new `--tag` argument (see more info [here](https://mikefarah.gitbook.io/yq/usage/value-parsing)). A result of this however, is that quoting values, e.g. "true" will no longer have an effect on how the value is interpreted like it did in V2.

For instance, to get the *string* "true" into a yaml file:

V2:

```
yq n a.path '"true"'
```

V3

```
yq n a.path --tag '!!str' true
```

### Reading paths that don't exist

In V2 this would return null, V3 does not return anything.

Similarly, reading null yaml values `null`, `~` and , V2 returns null whereas V3 returns the values as is.

This is a result of taking effort not to format values coming in and out of the original YAML.

### Update scripts file format has changed to be more powerful.

Comments can be added, and delete commands have been introduced.

V2

```
b.e[+].name: Mike Farah
```

V3

```yaml
- command: update 
  path: b.e[+].thing
  value:
    #great 
    things: frog # wow!
- command: delete
  path: b.d
```

### Reading and splatting, matching results are printed once per line.

e.g:

```yaml
parent:
  childA: 
    no: matches here
  childB:
    there: matches
    hi: no match
    there2: also matches
```

```
yq r sample.yaml 'parent.*.there*'
```

V2

```
- null
- - matches
  - also matches
```

V3

```
matches
also matches
```

### Converting JSON to YAML

As JSON is a subset of YAML, and `yq` now preserves the formatting of the passed in document, you will most likely need to use the `--prettyPrint` flag to format the JSON document as idiomatic YAML. See [Working with JSON](https://mikefarah.gitbook.io/yq/usage/convert#json-to-yaml) for more info.


# Read

Returns matching nodes/values of a path expression for a given yaml document

```
yq r <yaml_file|json_file> <path_expression>
```

Returns the matching nodes of the path expression for the given yaml file (or STDIN).

See docs for [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) for more details.

## Basic

Given a sample.yaml file of:

```yaml
b:
  c: 2
```

then

```bash
yq r sample.yaml b.c
```

will output the value of '2'.

## From Stdin

Given a sample.yaml file of:

```bash
cat sample.yaml | yq r - b.c
```

will output the value of '2'.

## Default values

Using the `--defaultValue/-D` flag you can specify a default value to be printed when no matching nodes are found for an expression

```
yq r sample.yaml --defaultValue frog path.not.there
```

will yield (assuming `path.not.there` does not match any nodes):

```
frog
```

## Printing matching paths

By default, yq will only print the value of the path expression for the yaml document. By specifying `--printMode` or `-p` you can print the matching paths.

```yaml
a:
  thing_a: 
    animal: cat
  other: 
    animal: frog
  thing_b: 
    vehicle: car
```

### Path Only

```bash
yq r --printMode p "a.thing*.*"
```

will print

```
a.thing_a.animal
a.thing_b.vehicle
```

### Path and Value

```bash
yq r --printMode pv "a.thing*.*"
```

will print

```
a.thing_a.animal: cat
a.thing_b.vehicle: car
```

## Collect results into an array

By default, results are printed out line by line as independent matches. This is handy for both readability as well as piping into tools like `xargs`. However, if you would like to collect the matching results into an array then use the `--collect/-c` flag. This is particularly useful with the `length` flag described below.

Given:

```yaml
a:
  thing_a: 
    animal: cat
  other: 
    animal: frog
  thing_b: 
    vehicle: car
```

```
yq r sample.yaml --collect a.*.animal
```

will print

```
- cat
- frog
```

## Printing length of the results

Use the `--length/-l` flag to print the length of results. For arrays this will be the number of items, objects the number of entries and scalars the length of the value.

Given

```
animals:
  - cats
  - dog
  - cheetah
```

```
yq r sample.yml --length animals
```

will print&#x20;

```
3
```

### Length of filtered results

By default, filtered results are printed *independently* so you will get the length of each result printed on a separate line:

```
yq r sample.yaml --length --printMode pv 'animals.(.==c*)'
```

```
animals.[0]: 4
animals.[2]: 7
```

However, you'll often want to know the count of the filtered results - use the `--collect` flag to collect the results in the array. The length will then return the size of the array.&#x20;

```
yq r sample.yaml --length --collect 'animals.(.==c*)' 
```

```
2
```

## Anchors and Aliases

The read command will print out the anchors of a document and can also traverse them.

Lets take a look at a simple example file:

```yaml
foo: &foo
  a: 1

foobar: *foo
```

### Printing anchors

```bash
yq r sample.yml foo
```

will print out

```yaml
&foo
a: 1
```

Similarly,

```
yq r sample.yml foobar
```

prints out

```yaml
*foo
```

### Traversing anchors

To traverse an anchor, we need to either explicitly reference merged in values:

```
yq r sample.yml foobar.a
```

to get

```
1
```

or we can use deep splat to get all the values

```bash
yq r sample.yml -p pv "foobar.**"
```

prints

```yaml
foobar.a: 1
```

The same methods work for the `<<: [*blah, *thing]`anchors.

### Exploding Anchors

By default anchors are not exploded (or expanded/de-referenced) for viewing, and the yaml is shown as-is. Use the `--explodeAnchors/-X` flag to show the anchor values.

Given sample.yml:

```yaml
foo: &foo
  a: original
  thing: coolasdf
  thirsty: yep

bar: &bar
  b: 2
  thing: coconut
  c: oldbar

foobarList:
  <<: [*foo,*bar]
  c: newbar
```

Then

```
yq r -X sample.yml foobarList
```

yields

```
c: newbar
b: 2
thing: coconut
a: original
thirsty: yep
```

Note that yq processes the merge anchor list in reverse order, to ensure that the last items in the list override the preceding.

## Multiple Documents

### Reading from a single document

Given a sample.yaml file of:

```yaml
something: else
---
b:
  c: 2
```

then

```bash
yq r -d1 sample.yaml b.c
```

will output the value of '2'.

### Read from all documents

Reading all documents will return the result as an array. This can be converted to json using the '-j' flag if desired.

Given a sample.yaml file of:

```yaml
name: Fred
age: 22
---
name: Stella
age: 23
---
name: Android
age: 232
```

then

```bash
yq r -d'*' sample.yaml name
```

will output:

```
Fred
Stella
Android
```


# Validate

Validate a given yaml file

```
yq v <yaml_file|->
```

Validates the given yaml file, does nothing if its valid, otherwise it will print errors to Stderr and exit with a non 0 exit code. This works like the [read command](https://mikefarah.gitbook.io/yq/commands/read) - but does not take a path expression and does not print the yaml if it is valid.

## Basic - valid

```
yq v valid.yaml
```

This will not print anything, and finish with a successful (0) exit code.

## Basic - invalid, from stdin

```
echo '[1234' | yq v -
```

This will print the parsing error to stderr:

```bash
﻿﻿10:43:09 main [ERRO] yaml: line 1: did not find expected ',' or ']'
```

And return a error exit code (1)

## Multiple documents

Like other commands, by default the validate command will only run against the first document in the yaml file. Note that when running against other specific document indexes, *all previous documents will also be validated.*

### Validating a single document

```bash
yq v -d1 multidoc.yml
```

This will validate both document 0 and document 1 (but not document 2)

### Validating all documents

```bash
yq v -d'*' multidoc.yml
```

This will validate all documents in the yaml file. Note that \* is quoted to avoid the CLI from processing the wildcard.


# Compare

Deeply compare two yaml documents

```bash
yq compare <yaml_file_1> <yaml_file_2> <path_expression>
```

Compares the matching yaml nodes at path expression in the two yaml documents. See [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) for more details. Difference calculated line by line, and is printed out line by line where the first character of each line is either:

* &#x20; a space, indicating no change at this line
* `-` a minus ,indicating the line is not present in the second document (it's removed)
* `+` a plus, indicating that the line is not present in the first document (it's added)

If there are differences then `yq` will print out the differences and exit with code 1. If there are no differences, then nothing will be printed and the exit code will be 0.

## Example data

Given data1.yaml

```yaml
"apples": are nice
somethingElse: cool # this is nice
favouriteNumbers: [1,2,3]
noDifference: it's the same
```

and data2.yaml

```yaml
apples: are nice
somethingElse: cool # yeah i like it
favouriteNumbers:
- 1
- 3
- 4
noDifference: it's the same
```

## Basic

Basic will compare the yaml documents 'as-is'

```yaml
yq compare data1.yaml data2.yaml
```

yields

```
-"apples": are nice
-somethingElse: cool # this is nice
-favouriteNumbers: [1, 2, 3]
+apples: are nice
+somethingElse: cool # yeah i like it
+favouriteNumbers:
+- 1
+- 3
+- 4
 noDifference: it's the same
```

## Formatted

Most of the time, it will make sense to [format](https://mikefarah.gitbook.io/yq/usage/output-format#pretty-print) the documents before comparing:

```
yq compare --prettyPrint data1.yaml data2.yml
```

yields

```
 apples: are nice
-somethingElse: cool # this is nice
+somethingElse: cool # yeah i like it
 favouriteNumbers:
 - 1
-- 2
 - 3
+- 4
 noDifference: it's the same
```

## Using path expressions

Use [path expressions](https://mikefarah.gitbook.io/yq/usage/path-expressions) to compare subsets of yaml documents

```
yq compare -P data1.yaml data2.yml favouriteNumbers
```

yields

```
 - 1
-- 2
 - 3
+- 4
```


# Write

Updates all the matching nodes of path expression in a yaml file to the supplied value.

```bash
yq w <yaml_file> <path_expression> <new value>
```

See docs for [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) and [value parsing](https://mikefarah.gitbook.io/yq/usage/value-parsing) for more details, including controlling quotes and tags.

## Basic

Given a sample.yaml file of:

```yaml
b:
  c: 2
```

then

```bash
yq w sample.yaml b.c cat
```

will output:

```yaml
b:
  c: cat
```

### Updating files in-place

```bash
yq w -i sample.yaml b.c cat
```

will update the sample.yaml file so that the value of 'c' is cat.

## From STDIN

```bash
cat sample.yaml | yq w - b.c blah
```

## Adding new fields

Any missing fields in the path will be created on the fly.

Given a sample.yaml file of:

```yaml
b:
  c: 2
```

then

```bash
yq w sample.yaml b.d[+] "new thing"
```

will output:

```yaml
b:
  c: cat
  d:
    - new thing
```

## Appending value to an array field

Given a sample.yaml file of:

```yaml
b:
  c: 2
  d:
    - new thing
    - foo thing
```

then

```bash
yq w sample.yaml "b.d[+]" "bar thing"
```

will output:

```yaml
b:
  c: cat
  d:
    - new thing
    - foo thing
    - bar thing
```

Note that the path is in quotes to avoid the square brackets being interpreted by your shell.

## Multiple Documents

### Update a single document

Given a sample.yaml file of:

```yaml
something: else
---
b:
  c: 2
```

then

```bash
yq w -d1 sample.yaml b.c 5
```

will output:

```yaml
something: else
---
b:
  c: 5
```

### Update all documents

Given a sample.yaml file of:

```yaml
something: else
---
b:
  c: 2
```

then

```bash
yq w -d'*' sample.yaml b.c 5
```

will output:

```yaml
something: else
b:
  c: 5
---
b:
  c: 5
```

## Writing Anchors

The `---anchorName` flag can be used to set the anchor name of a node

Given a sample document of:

```yaml
commonStuff:
    flavour: vanilla
```

Then:

```bash
yq write sample.yaml commonStuff --anchorName=commonBits
```

Will yield

```yaml
commonStuff: &commonBits
    flavour: vanilla
```

## Writing Aliases

The `--makeAlias` flag can create (or update) a node to be an alias to an anchor.

Given a sample file of:

```yaml
commonStuff: &commonBits
    flavour: vanilla
```

Then

```bash
yq write sample.yaml --makeAnchor foo commonBits
```

Will yield:

```yaml
commonStuff: &commonBits
    flavour: vanilla
foo: *commonBits
```

## Updating only styles/tags without affecting values

You can use the write command to update the quoting style of nodes, or their tags, without re-specifying the values. This is done by omitting the value argument:

Given a sample document:

```yaml
a:
  c: things
  d: other things
```

Then

```bash
yq write sample.yaml --style=single a.*
```

Will yield:

```yaml
a:
  c: 'things'
  d: 'other things'
```

## Using a script file to update

Given a sample.yaml file of:

```yaml
b:
  d: be gone
  c: 2
  e:
    - name: Billy Bob # comment over here
```

and a script update\_instructions.yaml of:

```yaml
- command: update 
  path: b.c
  value:
    #great 
    things: frog # wow!
- command: delete
  path: b.d
```

then

```bash
yq w -s update_instructions.yaml sample.yaml
```

will output:

```yaml
b:
  c:
    #great
    things: frog # wow!
  e:
  - name: Billy Bob # comment over here
```

And, of course, you can pipe the instructions in using '-':

```bash
cat update_instructions.yaml | yq w -s - sample.yaml
```


# Create

```
yq n <path_expression> <new value>
```

This works in the same way as the write command, but you don't pass in an existing Yaml file. Currently this does not support creating multiple documents in a single yaml file.

See docs for [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) and [value parsing](https://mikefarah.gitbook.io/yq/usage/value-parsing) for more details, including controlling quotes and tags.

## Creating a simple yaml file

```bash
yq n b.c cat
```

will output:

```yaml
b:
  c: cat
```

## Creating using a create script

Create scripts follow the same format as the update scripts.

Given a script create\_instructions.yaml of:

```yaml
- command: update 
  path: b.c
  value:
    #great 
    things: frog # wow!
```

then

```bash
yq n -s create_instructions.yaml
```

will output:

```yaml
b:
  c:
    #great
    things: frog # wow!
```

You can also pipe the instructions in:

```bash
cat create_instructions.yaml | yq n -s -
```


# Delete

Deletes all the matching nodes for the path expression in the given yaml input

```
yq delete <yaml_file|-> <path_expression>
```

See docs for [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) for more details.

## Deleting from a simple document

Given a sample.yaml file of:

```yaml
b:
  c: 2
  apples: green
```

then

```bash
yq d sample.yaml b.c
```

will output

```yaml
b:
  apples: green
```

## From STDIN

Use "-" (without quotes) in-place of a file name if you wish to pipe in input from STDIN.

```bash
cat sample.yaml | yq d - b.c
```

## Deleting in-place

```bash
yq d -i sample.yaml b.c
```

will update the sample.yaml file so that the 'c' node is deleted

## Multiple Documents

### Delete from single document

Given a sample.yaml file of:

```yaml
something: else
field: leaveMe
---
b:
  c: 2
field: deleteMe
```

then

```bash
yq d -d1 sample.yaml field
```

will output:

```yaml
something: else
field: leaveMe
---
b:
  c: 2
```

### Delete from all documents

Given a sample.yaml file of:

```yaml
something: else
field: deleteMe
---
b:
  c: 2
field: deleteMeToo
```

then

```bash
yq d -d'*' sample.yaml field
```

will output:

```yaml
something: else
---
b:
  c: 2
```


# Merge

Merge multiple yaml files into a one

Yaml files can be merged using the 'merge' command. Each additional file merged with the first file will set values for any key not existing already or where the key has no value.

```
yq m <yaml_file> <yaml_file2> <yaml_file3>...
```

## Merge example

Given a data1.yaml file of:

```yaml
a: simple
b: [1, 2]
```

and data2.yaml file of:

```yaml
a: other
c:
  test: 1
```

then

```bash
yq merge data1.yaml data2.yaml
```

will output:

```yaml
a: simple
b: [1, 2]
c:
  test: 1
```

## Updating files in-place

```bash
yq m -i data1.yaml data2.yaml
```

will update the data1.yaml file with the merged result.

## Overwrite values

Given a data1.yaml file of:

```yaml
a: simple
b: [1, 2]
d: left alone
```

and data2.yaml file of:

```yaml
a: other
b: [3, 4]
c:
  test: 1
```

then

```bash
yq m -x data1.yaml data2.yaml
```

will output:

```yaml
a: other
b: [3, 4]
c:
  test: 1
d: left alone
```

Notice that 'b' does not result in the merging of the values within an array.

## Append values with arrays

Given a data1.yaml file of:

```yaml
a: simple
b: [1, 2]
d: hi
```

and data2.yaml file of:

```yaml
a: something
b: [3, 4]
c:
  test: 2
  other: true
```

then

```bash
yq m --arrays=append data1.yaml data2.yaml
```

will output:

```yaml
a: simple
b: [1, 2, 3, 4]
c:
  test: 2
  other: true
d: hi
```

Note that the 'b' array has concatenated the values from the second data file. Also note that other map keys are not overridden (field a).

## Auto-create

By default, `yq` will automatically create any missing entries in the target yaml file. This can be turned off so that only matching paths are merged in. When turned off - you will most likely want to use the [override flag](#overwrite-values).

Given a data1.yml file of:

```yaml
a: thing
b: something else
```

and data2.yml file of:

```yaml
b: new value
d: not in original
```

Then

```yaml
yq m --overwrite --autocreate=false data1.yml data2.yml
```

will yield

```yaml
a: thing
b: new value
```

## Multiple Documents

### Merge into single document

Currently yq only has multi-document support for the *first* document being merged into. The remaining yaml files will have their first document selected.

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

and data3.yaml file of:

```yaml
b: dog
```

then

```bash
yq m -x -d1 data1.yaml data3.yaml
```

will output:

```yaml
something: else
---
a: simple
b: dog
```

### Merge into all documents

Currently yq only has multi-document support for the *first* document being merged into. The remaining yaml files will have their first document selected.

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

and data3.yaml file of:

```yaml
b: dog
```

then

```bash
yq m -x -d'*' data1.yaml data3.yaml
```

will output:

```yaml
b: dog
something: else
---
a: simple
b: dog
```


# Prefix

Prefixes a yaml document with the given path expression. The complete yaml content will be nested inside the new prefix path.

```
yq p <yaml_file> <path>
```

See docs for [path expression](https://mikefarah.gitbook.io/yq/usage/path-expressions) for more details.

## Prefix a document

Given a data1.yaml file of:

```yaml
a:
  b: [1, 2]
```

then

```bash
yq p data1.yaml c.d
```

will output:

```yaml
c:
  d:
    a:
      b: [1, 2]
```

## Updating files in-place

```bash
yq p -i data1.yaml c
```

will update the data1.yaml file so that the path 'c' prefixes the document.

## Multiple Documents

### Prefix a single document

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

then

```bash
yq p -d1 data1.yaml c
```

will output:

```yaml
something: else
---
c:
  a: simple
  b: cat
```

### Prefix all documents

Given a data1.yaml file of:

```yaml
something: else
---
a: simple
b: cat
```

then

```bash
yq p -d'*' data1.yaml c
```

will output:

```yaml
c:
  something: else
---
c:
  a: simple
  b: cat
```


# Shell Completion

Generate a shell completion file for supported shells (bash/fish/zsh/powershell)

```bash
yq shell-completion --variation=zsh
```

Prints to StdOut a shell completion script for zsh shell.

### Bash (default)

```bash
yq shell-completion
```

To configure your bash shell to load completions for each session add to your bashrc

```
# ~/.bashrc or ~/.profile
. <(yq shell-completion)
```

### zsh

```bash
yq shell-completion --variation=zsh
```

The generated completion script should be put somewhere in your $fpath named \_yq

### fish

```bash
yq shell-completion --variation=fish
```

Save the output to a '.fish' file and add it to your completions directory.

### PowerShell

```bash
yq shell-completion --variation=powershell
```

Users need PowerShell version 5.0 or above, which comes with Windows 10 and can be downloaded separately for Windows 7 or 8.1. They can then write the completions to a file and source this file from their PowerShell profile, which is referenced by the $Profile environment variable.


# Output format

Flags to control yaml and json output format

These flags are available for all `yq` commands.&#x20;

## Colorize Output

Use the `--colors/-C`flag to print out yaml with colors. This does not work when outputing in JSON format.

## Pretty Print

Use the `--prettyPrint/-P` flag to enforce a formatting style for yaml documents. This is particularly useful when reading a json file (which is a subset of yaml) and wanting to format it in a more conventional yaml format.

Given:

```
{
  "apples": [
    {
      "are": "great"
    }
  ]
}
```

Then:

```
yq r --prettyPrint sample.json
```

Will print out:

```
apples:
- are: great
```

This works in the same manner for yaml files:

```
"apples": [are: great]
```

will format to:

```
apples:
- are: great
```

## Indent

Use the indent flag `--indent/-I` to control the number of spaces used for indentation. This also works for JSON output. The default value is 2.&#x20;

Note that lists are indented at the same level as the map key at indent level 2, but are more deeply indented at indent level 4 and greater. This is (currently) a quirk of the underlying [yaml parser](https://github.com/go-yaml/yaml/tree/v3).

Given:

```
apples:
  collection:
  - name: Green
  - name: Blue
  favourite: Pink Lady
```

Then:

```
yq r -I4 sample.yaml
```

Will print out:

```
apples:
    collection:
      - name: Green
      - name: Blue
    favourite: Pink Lady
```

With json, you must also specify the `--prettyPrint/-P` flag

```
yq r -j -P -I4 sample.yaml
```

yields

```
{
    "apples": {
        "collection": [
            {
                "name": "Green"
            },
            {
                "name": "Blue"
            }
        ],
        "favourite": "Pink Lady"
    }
}
```

## Unwrap scalars

By default scalar values are 'unwrapped', that is only their value is printed (except when outputting as JSON). To print out the node as-is, with the original formatting an any comments pass in `--unwrapScalar=false`

Given data.yml:

```yaml
a: "Things" # cool stuff
```

Then:

`yq r --unwrapScalar=false data.yml a`

Will yield:

```yaml
"Things" # cool stuff
```

where as without setting the flag to false you would get:

```yaml
Things
```

## Strip comments

Use the `--stripComments` flag to print out the yaml file without any of the original comments.

Given data.yml of:

```yaml
a:
  b: # there is where the good stuff is
    c: hi
```

Then

```yaml
yq r data.yml a --stripComments
```

Will yield:

```yaml
b:
  c: hi
```


# Path Expressions

Path expressions are used to deeply navigate and match particular yaml nodes.

*As a general rule, you should wrap paths in quotes to prevent your CLI from processing `*`, `[]` and other special characters.*

## Simple expressions

### Maps

`'a.b.c'`

```yaml
a:
  b:
    c: thing # MATCHES
```

### Arrays

`'a.b[1].c'`

```yaml
a:
  b:
  - c: thing0 
  - c: thing1 # MATCHES
  - c: thing2
```

#### Appending to arrays

(e.g. when using the write command)

`'a.b[+].c'`

```yaml
a:
  b:
  - c: thing0
```

Will add a new entry:

```yaml
a:
  b:
  - c: thing0 
  - c: thing1 # NEW entry from [+] on B array.
```

#### Negative Array indexes

Negative array indexes can be used to traverse the array in reverse

`'a.b[-1].c'`

Will access the last element in the `b` array and yield:

```yaml
thing2
```

## Splat

### Maps

`'a.*.c'`

```yaml
a:
  b1:
    c: thing # MATCHES
    d: whatever
  b2:
    c: thing # MATCHES
    f: something irrelevant
```

#### Prefix splat

`'bob.item*.cats'`

```yaml
bob:
  item:
    cats: bananas # MATCHES
  something:
    cats: lemons
  itemThing:
    cats: more bananas # MATCHES
  item2:
    cats: apples # MATCHES
  thing:
    cats: oranges
```

### Arrays

`'a.b[*].c'`

```yaml
a:
  b:
  - c: thing0 # MATCHES
    d: what..ever
  - c: thing1 # MATCHES
    d: blarh
  - c: thing2 # MATCHES
    f: thingamabob
```

## Deep Splat

`**` will match arbitrary nodes for both maps and arrays:

`'a.**.c'`

```yaml
a:
  b1:
    c: thing1 # MATCHES
    d: cat cat
  b2:
    c: thing2 # MATCHES
    d: dog dog
  b3:
    d:
    - f:
        c: thing3 # MATCHES
        d: beep
    - f:
        g:
          c: thing4 # MATCHES
          d: boop
    - d: mooo
```

## Search by children nodes

You can search children by nodes - note that this will return the *parent* of the matching expression, in the example below the parent(s) will be the matching indices of the 'a' array. We can then navigate down to get 'b.c' of each matching indice.

`'a.(b.d==cat).b.c'`

```yaml
a:
  - b:
      c: thing0
      d: leopard
    ba: fast
  - b:
      c: thing1 # MATCHES
      d: cat
    ba: meowy
  - b:
      c: thing2
      d: caterpillar
    ba: icky
  - b:
      c: thing3 # MATCHES
      d: cat
    ba: also meowy
```

### With prefixes

`'a.(b.d==cat*).c'`

```yaml
a:
  - b:
      c: thing0
      d: leopard
    ba: fast
  - b:
      c: thing1 # MATCHES
      d: cat
    ba: meowy
  - b:
      c: thing2 # MATCHES
      d: caterpillar
    ba: icky
  - b:
      c: thing3 # MATCHES
      d: cat
    ba: also meowy
```

### Matching children values

`'animals(.==cat)'`

```yaml
animals:
  - dog
  - cat # MATCHES  
  - rat
```

this also works in maps, and with prefixes

`'animals(.==c*)'`

```yaml
animals:
  friendliest: cow # MATCHES
  favourite: cat # MATCHES
  smallest: rat
```

## Special Characters

When your yaml field has special characters that overlap with `yq` path expression characters, you will need to escape them in order for the command to work.

### Keys with dots

When specifying a key that has a dot use key lookup indicator.

```yaml
b:
  foo.bar: 7
```

```bash
yaml r sample.yaml 'b."foo.bar"'
```

```bash
yaml w sample.yaml 'b."foo.bar"' 9
```

Any valid yaml key can be specified as part of a key lookup.

Note that the path is in single quotes to avoid the double quotes being interpreted by your shell.

### Keys (and values) with leading dashes

The flag terminator needs to be used to stop the app from attempting to parse the subsequent arguments as flags, if they start if a dash.

```bash
yq n -j -- --key --value
```

Will result in

```
--key: --value
```


# Value Parsing

How values are parsed from the CLI to commands that create/update yaml (e.g. new/write).

`yq` attempts to parse values intelligently, e.g. when a number is passed it - it will assume it's a number as opposed to a string. `yq` will not alter the representation of what you give. So if you pass '03.0' in, it will assume it's a number and keep the value formatted as it was passed in, that is '03.0'.

The `--tag` flag can be used to override the tag type to force particular tags.

## Default behavior

### Integers

*Given*

```bash
yq new key 3
```

results in

```yaml
key: 3
```

*Given a formatted number*

```bash
yq new key 03
```

results in

```yaml
key: 03
```

`yq` keeps the number formatted as it was passed in.

### Float

*Given*

```bash
yq new key "3.1"
```

results in

```yaml
key: 3.1
```

Note that quoting the number does not make a difference.

*Given a formatted decimal number*

```bash
yq new key 03.0
```

results in

```yaml
key: 03.0
```

`yq` keeps the number formatted as it was passed in

### Booleans

Note that `yq` supports yaml spec 1.2  - which means the values yes/no are no longer parsed as booleans, but as strings see <https://yaml.org/spec/1.2/spec.html> and <https://github.com/go-yaml/yaml/tree/v3> for more information.

```bash
yq new key true
```

results in

```yaml
key: true
```

### Nulls

```bash
yq new key null
```

results in

```yaml
key: null
```

```bash
yq new key '~'
```

results in

```yaml
key: ~
```

```bash
yq new key ''
```

results in

```yaml
key:
```

### Strings

```bash
yq new key whatever
```

results in

```yaml
key: whatever
```

```bash
yq new key ' whatever '
```

results in

```yaml
key: ' whatever '
```

## Using the tag flag to cast

Previous versions of yq required double quoting to force values to be strings, this no longer works - instead use the --tag flag.

### Casting booleans

```bash
yq new --tag '!!str' key true
```

results in

```yaml
key: "true"
```

### Casting nulls

```bash
yq new --tag '!!str' key null
```

results in

```yaml
key: "null"
```

### Custom types

```bash
yq new --tag '!!farah' key gold
```

results in

```yaml
key: !!farah gold
```

## The style flag

The `--style` flag can be used to specify the quote or block style of the node value. Valid values are

* single
* double
* folded
* flow
* literal
* tagged

For example, given:

```bash
MULTILINE=$(cat <<END
    This is line one.
    This is line two.
END
)

SINGLE="only one line"
```

### Single

```yaml
yq n --style single things "$MULTILINE"
```

```yaml
things: 'This is line one.

  This is line two.'
```

### Double

```yaml
things: "This is line one.\nThis is line two."
```

### Folded:

```yaml
things: >-
  This is line one.

  This is line two.

```

#### Folded single line:

```yaml
things: >-
  only one line
```

### Flow:

```yaml
things: |-
  This is line one.
  This is line two.

```

#### Flow single line:

```yaml
things: only one line
```

### Literal

```yaml
things: |-
  This is line one.
  This is line two.

```

#### Literal single line

```yaml
things: |-
  only one line
```

### Tagged

Always show the tag, note - you must also pass in `--tag='!!str'`

```yaml
things: !!str |-
  This is line one.
  This is line two.

```

#### Tagged single line

```yaml
things: !!str only one line
```


# Working with JSON

## Yaml to Json

To convert output to json, use the `--tojson` (or `-j`) flag. This is supported by all commands. You can change the json output format by using the [pretty print](https://mikefarah.gitbook.io/yq/output-format#pretty-print) or [indent](https://mikefarah.gitbook.io/yq/output-format#indent) flags. *Note that due to the implementation of the JSON marshaller in GO, object keys will be sorted on output (*[*https://golang.org/pkg/encoding/json/#Marshal*](https://golang.org/pkg/encoding/json/#Marshal)*).*

Given a sample.yaml file of:

```yaml
b:
  c: 2
```

then

```bash
yq r -j sample.yaml
```

will output

```javascript
{"b":{"c":2}}
```

To format the json:

```yaml
yq r --prettyPrint -j sample.yaml
```

will yield

```yaml
{
  "b": {
    "c": 2
  }
}
```

### Multiple matches

Each matching yaml node will be converted to json and printed out on a separate line. The [prettyPrint](https://mikefarah.gitbook.io/yq/output-format#pretty-print) and [indent](https://mikefarah.gitbook.io/yq/output-format#indent) flags will still work too.&#x20;

Given a sample.yaml file of:

```yaml
bob:
  c: 2
bab:
  c: 5
```

then

```bash
yq r -j sample.yaml b*
```

will output

```javascript
{"c":2}
{"c":5}
```

## Json to Yaml

To read in json, just pass in a json file instead of yaml, it will just work - as json is a subset of yaml. However, you will probably want to [pretty print the output](https://mikefarah.gitbook.io/yq/output-format#pretty-print) to look more like an idiomatic yaml document.

e.g given a json file

```javascript
{"a":"Easy! as one two three","b":{"c":2,"d":[3,4]}}
```

then

```bash
yq r --prettyPrint sample.json
```

will output

```yaml
a: Easy! as one two three
b:
  c: 2
  d:
  - 3
  - 4
```


