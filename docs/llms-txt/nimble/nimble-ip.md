# Source: https://docs.nimbleway.io/general/faqs/nimble-ip.md

# Nimble IP

<details>

<summary>How do I start using Nimble IP?</summary>

To start using Nimble IP, you first need to open an account ([reach out to our sales to open one](https://nimbleway.com/contact-general/)).

Once you have an account, check out our [quick start guide](https://docs.nimbleway.com/scraping-infrastructure/nimble-ip-quick-start-guide) for an easy walkthrough of the basic steps of using Nimble IP.

</details>

<details>

<summary>What is the Backconnect Gateway?</summary>

The Backconnect Gateway is a server that manages your proxy requests. It’s accessed through a single address that automatically rotates proxy IPs for you, freeing you from managing proxy lists.

The Backconnect Gateway matches your request with the best IP available and rotates IPs in keeping with your needs.

</details>

<details>

<summary>Where can I find the user name and password for accessing Nimble IP?</summary>

Nimble IP is accessed through our Backconnect Gateway - a single point of entry for automatic proxy access and rotation.

The Backconnect Gateway is accessible at:

* [x] **Host :** ip.nimbleway.com
* [x] **Proxy IP Port :** 7000

The welcome email sent when your account was opened included credentials to access the Backconnect Gateway.

Here is an example of accessing the gateway with username and password authentication:

`curl -x https://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io`

**accountName**: Your company gateway name.

**pipelineName**: The pipeline you wish to use (every new account comes with a quick-start pipeline named “residential”).

**pipelinePassword**: the password for the selected pipeline.

You can view your pipeline, create new pipelines, and set their passwords by using the Admin API. See our [Admin API Documentation](https://docs.nimbleway.com/management-tools/nimble-admin-api) for a full walkthrough.

</details>

<details>

<summary>Are my proxy gateway credentials forwarded to the target site?</summary>

No.

When you use Nimble proxies, the target website only receives the request headers you choose to send. Your proxy credentials are for accessing the proxy gateway itself, and are never forwarded.

</details>

<details>

<summary>Which ports and protocols are supported?</summary>

We currently support HTTP ports 80 and 443, and we’re working on adding SOCKS5 support.

</details>

<details>

<summary>Which Geolocations does Nimble IP support?</summary>

You can find the list of supported countries [here](https://api.nimbleway.com/api/v1/location/cities).

When using US-based proxies, you can also select IPs from a particular state using these [state codes](https://www.bls.gov/respondents/mwr/electronic-data-interchange/appendix-d-usps-state-abbreviations-and-fips-codes.htm).

If the country you need is not available, [please let us know](https://nimbleway.com/contact-general/) and we’ll work on adding it to the list.

</details>

<details>

<summary>Can I send a request through a random country?</summary>

Yes.

A country is selected randomly for proxy requests that do not include a target country.

If your requests are not receiving a random country, make sure that:

1\. Your pipeline settings do not include a target country, and are set to ALL.

2\. You are not sending a country parameter in your request.

</details>

<details>

<summary>Does Nimble IP auto-rotate IPs?</summary>

Nimble proxies auto-rotate IPs by default. Every request you make will be sent through a different exit node, in accordance with your pipeline settings.

If you’d like to maintain an IP for long periods of time, you can start a sticky session.

For a detailed walkthrough and examples, see our [Backconnect Gateway Documentation](https://docs.nimbleway.com/scraping-infrastructure/backconnect-gateway).

</details>

<details>

<summary>How do I start a session (Sticky IP)?</summary>

To get a sticky IP, add “-session-\<random\_string>” to the username segment of the authentication string.

For example:

<https://account-nimble-pipeline-residential-session-rand\\_sess\\_123:\\><password>@ip.nimblway.com:7000

&#x20;

If you’re using a whitelist instead of username/password authentication, you can start a session by choosing a port between 9000 and 10000. Once you’re finished working with the session, you can simply change ports to start a new one.

</details>

<details>

<summary>How many threads (concurrent sessions) can I have?</summary>

Nimble’s infrastructure is designed to handle any number of threads, so there’s no limit on the number of sessions running at the same time.

</details>

<details>

<summary>What is the session length limit?</summary>

Once you start a sticky session, Nimble will keep the connection open for as long as you need (subject to peer availability). Sticky sessions are closed only after 10 minutes of inactivity.

If you’d like a new IP, simple start a new session.

</details>
