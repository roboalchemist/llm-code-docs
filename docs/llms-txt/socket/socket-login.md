# Source: https://docs.socket.dev/docs/socket-login.md

# socket login

Socket API login

If you have a Socket.dev API token you can use `socket login` to store the token in a file such that it will automatically use that token when you run commands.

## socket login --help

```
$ socket login --help

  Socket API login

  Usage
    $ socket login [options]

  API Token Requirements
    - Quota: 1 unit

  Logs into the Socket API by prompting for an API key

  Options
    --apiBaseUrl      API server to connect to for login
    --apiProxy        Proxy to use when making connection to API server

  Examples
    $ socket login
    $ socket login --api-proxy=http://localhost:1234
```