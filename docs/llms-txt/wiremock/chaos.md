# Source: https://docs.wiremock.io/chaos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Chaos settings - Basics

> Proxying requests to other systems

The idea of the chaos settings is to introduce an element of failure into your
environment and observe how clients cope with it.

WireMock Cloud now allows introducing a random element of chaos across all the
calls to a particular API. This would allow you to check that your client
behaves appropriately; closes resources correctly, times out correctly, conveys
sensible error messages to the end user and to your monitoring systems, perhaps
opens circuit breakers to take load off the upstream system or other resilience
mechanisms.

## Enabling Chaos

You enable chaos by toggling the "Enable chaos" switch.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=b7cf24f04b7b1dffa437343d6cc201d9" alt="Enable chaos" data-og-width="617" width="617" data-og-height="104" height="104" data-path="images/chaos/enable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=894a878f5a25eddefb06d843e0c7775e 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=99184d039971ae67ad857da66ede8fd2 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=2a0ec42adb67ca734006c5ef889372c7 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ccd6cc7b587c521cb2339467cf6f877e 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8e34f4992380ea545fd562553963f2f5 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/enable.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=70dfd6d826fcf52a6c98a9f58b6f73ea 2500w" />

Once chaos is enabled, you can set a percentage of requests to that API to
experience a failure using the slider, or type it directly.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=184f2b77342e3da6457cbf187f1afc8e" alt="Chaos percentage slider" data-og-width="633" width="633" data-og-height="116" height="116" data-path="images/chaos/slider.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=cfb4289efa08d35576f83af704a9636f 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=73c9621e1d878c852f8fb42027f70007 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=b9e6bb93d986542a0ba49ad83b935a62 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6823458960b5beeb5923c90149ec96b9 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=884e0c67e3225e24513bf8d29c6f9164 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/slider.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=5bda0a2375f789f72ab4e8e0d8992439 2500w" />

The configured percentage of failures will be distributed evenly among the
failure modes.

We support five failure modes:

### [Socket close](#socket-close)

A request will just have the socket closed, with no data returned to the client
at all. This would allow you to check that your client closes all resources
appropriately in response.

### [Socket reset](#socket-reset)

The server will close the connection, setting `SO_LINGER` to 0 and thus
preventing the `TIME_WAIT` state being entered. Typically causes a
"Connection reset by peer" type error to be thrown by the client.

Note: this only seems to work properly on \*nix OSs. On Windows it will most
likely cause the connection to hang rather than reset.

This would allow you to check that your client closes all resources
appropriately in response.

### [Invalid HTTP](#invalid-http)

The server will start by responding with a valid HTTP status line, then will
return random bytes, so an invalid HTTP response. Then it will close the
connection.

### [Long delay](#long-delay)

The server will delay for the configured amount of time before responding. This
would allow you to check that you have appropriately configured timeouts.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=9a3e0bda31631f4dbc00013aa556e727" alt="Chaos long delay" data-og-width="641" width="641" data-og-height="115" height="115" data-path="images/chaos/long-delay.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=780a69018796e9051700c291638cf315 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ecca5481f476e01e82bfab1390f2bb87 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=fb7d2d2ad264ec0d0f4a505afb5aa0de 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a067978b52e34a6a38fa45390114b664 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=8b4a9e6c6610b6c25ce00b599fc83967 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/long-delay.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=dbc47d43b06f27295a6e2c4d9864b0f3 2500w" />

### [HTTP Error status](#http-error-status)

The server will return valid HTTP responses with the configured error status
codes.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e79ede560b123f38e9b7671da0278f27" alt="Chaos http errors" data-og-width="652" width="652" data-og-height="111" height="111" data-path="images/chaos/http-errors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d8e79684ee97f54a2ea2b67494e4ccba 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=dea861acc7e52f3467cf807f7a7c66eb 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a9212cff4b88f749f19e2c0f8eaf505a 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=4f89c7cd383cfba9c6fae8a1ba25d1bb 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=04cba760914f4da82cdb7c85e306c9d0 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/chaos/http-errors.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=515995cdde120f2c1c7ef0cd99a72fb6 2500w" />
