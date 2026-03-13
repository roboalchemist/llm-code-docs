# Source: https://ngrok.com/docs/using-ngrok-with/ftp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok with FTP, FTPS, SFTP

> Learn how to use ngrok with SFTP for secure file transfers, and why FTP/FTPS are not recommended due to multiple port requirements.

This guide explains how to use ngrok with SFTP and why FTP or FTPS are not a good fit for TCP tunneling.

## Compatibility with FTP and FTPS

FTP and FTPS (FTP over SSL) require multiple dynamic ports for data transfer between server and client, so ngrok is not a good solution for that traffic.
Use SFTP instead, which uses a single port.

## ngrok with SFTP

You can use ngrok for SFTP by starting a TCP endpoint on the port your SFTP server uses, usually port `22` (the same as SSH).

```bash  theme={null}
ngrok tcp 22
```

<Warning>
  TCP endpoints are only available on a free plan after [adding a valid payment method](https://dashboard.ngrok.com/settings#id-verification) to your account.
</Warning>

From there, use the resulting TCP address in your preferred SFTP client to connect to your local server.

## Alternatives to FTP for sharing files

If you're just looking for a quick way to serve local files, ngrok has a [built-in file server](../universal-gateway/http/#serving-file-directories).


Built with [Mintlify](https://mintlify.com).