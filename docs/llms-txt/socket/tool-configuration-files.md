# Source: https://docs.socket.dev/docs/tool-configuration-files.md

# Tool Configuration Files

Socket CLI and the VSCode extension share logins when possible to keep tooling from having mismatched results.

They store data in:

* `$HOME/.local/share/socket/settings` on \*nix
* `$LOCALAPPDATA/socket/settings` on Windows
* `$HOME/Libary/Application Support/socket/settings` on Mac OSX

This data takes the form a Base64 encoding of JSON matching the schema:

```Text JSON
{
  "apiKey":"..."
}
```

An example of encoding an API key of "my-api-key" would result in a file with the following contents:

```
ewogICJhcGlLZXkiOiAibXktYXBpLWtleSIKfQo=
```