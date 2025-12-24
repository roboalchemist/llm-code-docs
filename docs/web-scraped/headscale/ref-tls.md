# Source: https://headscale.net/stable/ref/tls/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/tls.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/tls.md "View source of this page")

# Running the service via TLS (optional)[¶](#running-the-service-via-tls-optional "Permanent link")

## Bring your own certificate[¶](#bring-your-own-certificate "Permanent link")

Headscale can be configured to expose its web service via TLS. To configure the certificate and key file manually, set the `tls_cert_path` and `tls_key_path` configuration parameters. If the path is relative, it will be interpreted as relative to the directory the configuration file was read from.

[config.yaml]

    tls_cert_path: ""
    tls_key_path: ""

The certificate should contain the full chain, else some clients, like the Tailscale Android client, will reject it.

## Let\'s Encrypt / ACME[¶](#lets-encrypt-acme "Permanent link")

To get a certificate automatically via [Let\'s Encrypt](https://letsencrypt.org/), set `tls_letsencrypt_hostname` to the desired certificate hostname. This name must resolve to the IP address(es) headscale is reachable on (i.e., it must correspond to the `server_url` configuration parameter). The certificate and Let\'s Encrypt account credentials will be stored in the directory configured in `tls_letsencrypt_cache_dir`. If the path is relative, it will be interpreted as relative to the directory the configuration file was read from.

[config.yaml]

    tls_letsencrypt_hostname: ""
    tls_letsencrypt_listen: ":http"
    tls_letsencrypt_cache_dir: ".cache"
    tls_letsencrypt_challenge_type: HTTP-01

### Challenge types[¶](#challenge-types "Permanent link")

Headscale only supports two values for `tls_letsencrypt_challenge_type`: `HTTP-01` (default) and `TLS-ALPN-01`.

#### HTTP-01[¶](#http-01 "Permanent link")

For `HTTP-01`, headscale must be reachable on port 80 for the Let\'s Encrypt automated validation, in addition to whatever port is configured in `listen_addr`. By default, headscale listens on port 80 on all local IPs for Let\'s Encrypt automated validation.

If you need to change the ip and/or port used by headscale for the Let\'s Encrypt validation process, set `tls_letsencrypt_listen` to the appropriate value. This can be handy if you are running headscale as a non-root user (or can\'t run `setcap`). Keep in mind, however, that Let\'s Encrypt will *only* connect to port 80 for the validation callback, so if you change `tls_letsencrypt_listen` you will also need to configure something else (e.g. a firewall rule) to forward the traffic from port 80 to the ip:port combination specified in `tls_letsencrypt_listen`.

#### TLS-ALPN-01[¶](#tls-alpn-01 "Permanent link")

For `TLS-ALPN-01`, headscale listens on the ip:port combination defined in `listen_addr`. Let\'s Encrypt will *only* connect to port 443 for the validation callback, so if `listen_addr` is not set to port 443, something else (e.g. a firewall rule) will be required to forward the traffic from port 443 to the ip:port combination specified in `listen_addr`.

### Technical description[¶](#technical-description "Permanent link")

Headscale uses [autocert](https://pkg.go.dev/golang.org/x/crypto/acme/autocert), a Golang library providing [ACME protocol](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment) verification, to facilitate certificate renewals via [Let\'s Encrypt](https://letsencrypt.org/about/). Certificates will be renewed automatically, and the following can be expected:

- Certificates provided from Let\'s Encrypt have a validity of 3 months from date issued.
- Renewals are only attempted by headscale when 30 days or less remains until certificate expiry.
- Renewal attempts by autocert are triggered at a random interval of 30-60 minutes.
- No log output is generated when renewals are skipped, or successful.

#### Checking certificate expiry[¶](#checking-certificate-expiry "Permanent link")

If you want to validate that certificate renewal completed successfully, this can be done either manually, or through external monitoring software. Two examples of doing this manually:

1.  Open the URL for your headscale server in your browser of choice, and manually inspecting the expiry date of the certificate you receive.
2.  Or, check remotely from CLI using `openssl`:

    $ openssl s_client -servername [hostname] -connect [hostname]:443 | openssl x509 -noout -dates
    (...)
    notBefore=Feb  8 09:48:26 2024 GMT
    notAfter=May  8 09:48:25 2024 GMT

#### Log output from the autocert library[¶](#log-output-from-the-autocert-library "Permanent link")

As these log lines are from the autocert library, they are not strictly generated by headscale itself.

    acme/autocert: missing server name

Likely caused by an incoming connection that does not specify a hostname, for example a `curl` request directly against the IP of the server, or an unexpected hostname.

    acme/autocert: host "[foo]" not configured in HostWhitelist

Similarly to the above, this likely indicates an invalid incoming request for an incorrect hostname, commonly just the IP itself.

The source code for autocert can be found [here](https://cs.opensource.google/go/x/crypto/+/refs/tags/v0.19.0:acme/autocert/autocert.go)