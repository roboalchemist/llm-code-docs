# Source: https://docs.socket.dev/docs/socket-optimize.md

# socket optimize

Optimize dependencies with @socketregistry overrides

## socket optimize --help

```
$ socket optimize --help

  Optimize dependencies with @socketregistry overrides

  Usage
    $ socket optimize [options] [CWD=.]

  Options
    --pin             Pin overrides to their latest version
    --prod            Only add overrides for production dependencies

  Examples
    $ socket optimize
    $ socket optimize ./proj/tree --pin
```