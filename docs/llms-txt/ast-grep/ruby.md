# Source: https://ast-grep.github.io/catalog/ruby.md

---
url: /catalog/ruby.md
---
# Ruby

This page curates a list of example ast-grep rules to check and to rewrite Ruby applications.

## Migrate action\_filter in Ruby on Rails&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1YnkiLCJxdWVyeSI6ImNvbnNvbGUubG9nKCRNQVRDSCkiLCJyZXdyaXRlIjoibG9nZ2VyLmxvZygkTUFUQ0gpIiwiY29uZmlnIjoiIyBhc3QtZ3JlcCBZQU1MIFJ1bGUgaXMgcG93ZXJmdWwgZm9yIGxpbnRpbmchXG4jIGh0dHBzOi8vYXN0LWdyZXAuZ2l0aHViLmlvL2d1aWRlL3J1bGUtY29uZmlnLmh0bWwjcnVsZVxucnVsZTpcbiAgYW55OlxuICAgIC0gcGF0dGVybjogYmVmb3JlX2ZpbHRlciAkJCRBQ1RJT05cbiAgICAtIHBhdHRlcm46IGFyb3VuZF9maWx0ZXIgJCQkQUNUSU9OXG4gICAgLSBwYXR0ZXJuOiBhZnRlcl9maWx0ZXIgJCQkQUNUSU9OXG4gIGhhczpcbiAgICBwYXR0ZXJuOiAkRklMVEVSXG4gICAgZmllbGQ6IG1ldGhvZFxuZml4OiBcbiAgJE5FV19BQ1RJT04gJCQkQUNUSU9OXG50cmFuc2Zvcm06XG4gIE5FV19BQ1RJT046XG4gICAgcmVwbGFjZTpcbiAgICAgIHNvdXJjZTogJEZJTFRFUlxuICAgICAgcmVwbGFjZTogX2ZpbHRlclxuICAgICAgYnk6IF9hY3Rpb24iLCJzb3VyY2UiOiJjbGFzcyBUb2Rvc0NvbnRyb2xsZXIgPCBBcHBsaWNhdGlvbkNvbnRyb2xsZXJcbiAgYmVmb3JlX2ZpbHRlciA6YXV0aGVudGljYXRlXG4gIGFyb3VuZF9maWx0ZXIgOndyYXBfaW5fdHJhbnNhY3Rpb24sIG9ubHk6IDpzaG93XG4gIGFmdGVyX2ZpbHRlciBkbyB8Y29udHJvbGxlcnxcbiAgICBmbGFzaFs6ZXJyb3JdID0gXCJZb3UgbXVzdCBiZSBsb2dnZWQgaW5cIlxuICBlbmRcblxuICBkZWYgaW5kZXhcbiAgICBAdG9kb3MgPSBUb2RvLmFsbFxuICBlbmRcbmVuZFxuIn0=)

### Description

This rule is used to migrate `{before,after,around}_filter` to `{before,after,around}_action` in Ruby on Rails controllers.

These are methods that run before, after or around an action is executed, and they can be used to check permissions, set variables, redirect requests, log events, etc. However, these methods are [deprecated](https://stackoverflow.com/questions/16519828/rails-4-before-filter-vs-before-action) in Rails 5.0 and will be removed in Rails 5.1. `{before,after,around}_action` are the new syntax for the same functionality.

This rule will replace all occurrences of `{before,after,around}_filter` with `{before,after,around}_action` in the controller code.

### YAML

```yaml
id: migration-action-filter
language: ruby
rule:
  any:
    - pattern: before_filter $$$ACTION
    - pattern: around_filter $$$ACTION
    - pattern: after_filter $$$ACTION
  has:
    pattern: $FILTER
    field: method
fix:
  $NEW_ACTION $$$ACTION
transform:
  NEW_ACTION:
    replace:
      source: $FILTER
      replace: _filter
      by: _action
```

### Example

```rb {2-4}
class TodosController < ApplicationController
  before_filter :authenticate
  around_filter :wrap_in_transaction, only: :show
  after_filter do |controller|
    flash[:error] = "You must be logged in"
  end

  def index
    @todos = Todo.all
  end
end
```

### Diff

```rb
class TodosController < ApplicationController
  before_action :authenticate  # [!code --]
  before_filter :authenticate # [!code ++]
  around_action :wrap_in_transaction, only: :show # [!code --]
  around_filter :wrap_in_transaction, only: :show # [!code ++]
  after_action do |controller|  # [!code --]
     flash[:error] = "You must be logged in" # [!code --]
  end # [!code --]
  after_filter do |controller| # [!code ++]
    flash[:error] = "You must be logged in" # [!code ++]
  end # [!code ++]

  def index
    @todos = Todo.all
  end
end
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim), inspired by [Future of Ruby - AST Tooling](https://dev.to/baweaver/future-of-ruby-ast-tooling-9i1).

## Prefer Symbol over Proc&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1YnkiLCJxdWVyeSI6IiRMSVNULnNlbGVjdCB7IHwkVnwgJFYuJE1FVEhPRCB9IiwicmV3cml0ZSI6IiRMSVNULnNlbGVjdCgmOiRNRVRIT0QpIiwiY29uZmlnIjoiaWQ6IHByZWZlci1zeW1ib2wtb3Zlci1wcm9jXG5ydWxlOlxuICBwYXR0ZXJuOiAkTElTVC4kSVRFUiB7IHwkVnwgJFYuJE1FVEhPRCB9XG5sYW5ndWFnZTogUnVieVxuY29uc3RyYWludHM6XG4gIElURVI6XG4gICAgcmVnZXg6ICdtYXB8c2VsZWN0fGVhY2gnXG5maXg6ICckTElTVC4kSVRFUigmOiRNRVRIT0QpJ1xuIiwic291cmNlIjoiWzEsIDIsIDNdLnNlbGVjdCB7IHx2fCB2LmV2ZW4/IH1cbigxLi4xMDApLmVhY2ggeyB8aXwgaS50b19zIH1cbm5vdF9saXN0Lm5vX21hdGNoIHsgfHZ8IHYuZXZlbj8gfVxuIn0=)

### Description

Ruby has a more concise symbol shorthand `&:` to invoke methods.
This rule simplifies `proc` to `symbol`.
This example is inspired by this [dev.to article](https://dev.to/baweaver/future-of-ruby-ast-tooling-9i1).

### YAML

```yaml
id: prefer-symbol-over-proc
language: ruby
rule:
  pattern: $LIST.$ITER { |$V| $V.$METHOD }
constraints:
  ITER:
    regex: 'map|select|each'
fix: '$LIST.$ITER(&:$METHOD)'
```

### Example

```rb {1,2}
[1, 2, 3].select { |v| v.even? }
(1..100).each { |i| i.to_s }
not_list.no_match { |v| v.even? }
```

### Diff

```rb
[1, 2, 3].select { |v| v.even? } # [!code --]
[1, 2, 3].select(&:even?) # [!code ++]
(1..100).each { |i| i.to_s } # [!code --]
(1..100).each(&:to_s) # [!code ++]

not_list.no_match { |v| v.even? }
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim)

## Detect Path Traversal Vulnerability in Rails

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1YnkiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoiYXN0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogcGF0aC10cmF2ZXJzYWxcbm1lc3NhZ2U6IFBvdGVudGlhbCBQYXRoIFRyYXZlcnNhbCB2dWxuZXJhYmlsaXR5IGRldGVjdGVkLiBVc2VyIGlucHV0IGlzIGJlaW5nIHVzZWQgdG8gY29uc3RydWN0IGZpbGUgcGF0aHMgd2l0aG91dCB2YWxpZGF0aW9uLlxuc2V2ZXJpdHk6IGhpbnRcbmxhbmd1YWdlOiBSdWJ5XG5ub3RlOiB8XG4gIFBhdGggVHJhdmVyc2FsIChEaXJlY3RvcnkgVHJhdmVyc2FsKSBvY2N1cnMgd2hlbiB1c2VyIGlucHV0IGlzIHVzZWQgdG8gY29uc3RydWN0IGZpbGUgcGF0aHNcbiAgd2l0aG91dCBwcm9wZXIgdmFsaWRhdGlvbi4gVGhpcyBhbGxvd3MgYXR0YWNrZXJzIHRvIGFjY2VzcyBmaWxlcyBvdXRzaWRlIHRoZSBpbnRlbmRlZCBkaXJlY3RvcnkuXG4gIFZhbGlkYXRlIGFuZCBzYW5pdGl6ZSBmaWxlIHBhdGhzLCBhbmQgdXNlIEZpbGUuYmFzZW5hbWUoKSBvciBzaW1pbGFyIGZ1bmN0aW9ucy5cblxucnVsZTpcbiAgYW55OlxuICAgIC0gcGF0dGVybjogUmFpbHMucm9vdC5qb2luKCQkJCwgJFZBUiwgJCQkKVxuICAgIC0gcGF0dGVybjogRmlsZS5qb2luKCQkJCwgJFZBUiwgJCQkKVxuICAgIC0gcGF0dGVybjogc2VuZF9maWxlICRWQVIiLCJzb3VyY2UiOiIjIOaknOWHuuOBleOCjOOCi+OCs+ODvOODieS+i1xuIyDjg5Hjgr/jg7zjg7MxOiBSYWlscy5yb290LmpvaW4gd2l0aCB2YXJpYWJsZVxuUmFpbHMucm9vdC5qb2luKCd1cGxvYWRzJywgcGFyYW1zWzpmaWxlbmFtZV0pXG5SYWlscy5yb290LmpvaW4oJ2RhdGEnLCB1c2VyX2lucHV0LCAnZmlsZS50eHQnKVxuXG4jIOODkeOCv+ODvOODszI6IEZpbGUuam9pbiB3aXRoIHZhcmlhYmxlXG5GaWxlLmpvaW4oJy92YXIvd3d3JywgcGFyYW1zWzpwYXRoXSlcbkZpbGUuam9pbihiYXNlX3BhdGgsIHVzZXJfaWQsIGZpbGVuYW1lKVxuXG4jIOODkeOCv+ODvOODszM6IHNlbmRfZmlsZSB3aXRoIHZhcmlhYmxlXG5zZW5kX2ZpbGUgcGFyYW1zWzpmaWxlXVxuc2VuZF9maWxlIHVzZXIuZG9jdW1lbnRfcGF0aCJ9)

### Description

Path Traversal (Directory Traversal) occurs when user input is used to construct file paths without proper validation. This allows attackers to access files outside the intended directory by using special characters like `../` to navigate the filesystem.

This rule detects common path traversal patterns in Rails applications where user-controlled variables are used in:

* `Rails.root.join()` - Building file paths relative to the Rails application root
* `File.join()` - Constructing file paths
* `send_file` - Sending files to users

To prevent path traversal vulnerabilities, always validate and sanitize file paths, use `File.basename()` to extract only the filename, or use allowlists for permitted files.

### YAML

```yaml
id: path-traversal
message: Potential Path Traversal vulnerability detected. User input is being used to construct file paths without validation.
severity: hint
language: Ruby
note: |
  Path Traversal (Directory Traversal) occurs when user input is used to construct file paths
  without proper validation. This allows attackers to access files outside the intended directory.
  Validate and sanitize file paths, and use File.basename() or similar functions.

rule:
  any:
    - pattern: Rails.root.join($$$, $VAR, $$$)
    - pattern: File.join($$$, $VAR, $$$)
    - pattern: send_file $VAR
```

### Example

```rb {2,3,6,7,10,11}
# Pattern 1: Rails.root.join with variable
Rails.root.join('uploads', params[:filename])
Rails.root.join('data', user_input, 'file.txt')

# Pattern 2: File.join with variable
File.join('/var/www', params[:path])
File.join(base_path, user_id, filename)

# Pattern 3: send_file with variable
send_file params[:file]
send_file user.document_path
```

### Contributed by

[sora fs0414](https://x.com/_fs0414) from this [blog post](https://fs0414.hatenablog.com/entry/2025/11/02/032114)
