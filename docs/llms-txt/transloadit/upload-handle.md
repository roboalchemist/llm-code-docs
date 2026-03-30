# Source: https://transloadit.com/docs/robots/upload-handle.md

Transloadit handles file uploads by default, so specifying this Robot is optional.

It can still be a good idea to define this Robot, though. It makes your Assembly Instructions explicit, and allows you to configure exactly how uploads should be handled. For example, you can extract specific metadata from the uploaded files.

There are **3 important constraints** when using this Robot:

1. Don’t define a `use` parameter, unlike with other Robots.
2. Use it only once in a single set of Assembly Instructions.
3. Name the Step as `:original`.
