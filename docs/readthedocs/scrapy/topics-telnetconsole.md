# Telnet Console

Scrapy comes with a built-in telnet console for inspecting and controlling a
Scrapy running process. The telnet console is just a regular python shell
running inside the Scrapy process, so you can do literally anything from it.

The telnet console is a built-in Scrapy extension which comes enabled by default, but you can also
disable it if you want. For more information about the extension itself see
Log Count extension.

Warning

It is not secure to use telnet console via public networks, as telnet
doesn’t provide any transport-layer security. Having username/password
authentication doesn’t change that.

Intended usage is connecting to a running Scrapy spider locally
(spider process and telnet client are on the same machine)
or over a secure connection (VPN, SSH tunnel).
Please avoid using telnet console over insecure connections,
or disable it completely using `TELNETCONSOLE_ENABLED` option.