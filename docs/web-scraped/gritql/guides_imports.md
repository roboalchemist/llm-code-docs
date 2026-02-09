**Source:** https://docs.grit.io

# File Imports

Since managing package imports is a common task, Grit includes standard patterns for declaratively adding, removing, and updating imports.
`ensure_import_from`This pattern ensures that the given `$value` is imported from the given `$source` (adding the import if it does not exist).
Note: because this is a *pattern* you must match some `$value` against it.
pattern `class $_ extends $comp { $_ }` where {
  $comp <: `Component`,
  $source = `"React"`,
  $comp <: ensure_import_from($source)
}Before class Button extends Component {
  // ...
}After import { Component } from &#x27;React&#x27;;

class Button extends Component {
  // ...
}
