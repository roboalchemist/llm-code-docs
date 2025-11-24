# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/enabling-http-response.md

# Enabling HTTP Response Streaming

## Problem

An Aptible user is attempting to stream HTTP responses from the server but notices that they are being buffered.

## Cause

By default, Aptible buffers requests at the proxy layer to protect against attacks that exploit slow uploads such as \[Slowloris]\(/docs/([https://en.wikipedia.org/wiki/Slowloris\_(computer\_security)](https://en.wikipedia.org/wiki/Slowloris_\(computer_security\))).

## Resolution

Aptible users can set the [`X-Accel-Buffering`](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/#x-accel-buffering) header to `no` to disable proxy buffering for these types of requests.

###### Enabling HTTP Response Streaming

* [Problem](/how-to-guides/troubleshooting/common-errors-issues/enabling-http-response#problem)
* [Cause](/how-to-guides/troubleshooting/common-errors-issues/enabling-http-response#cause)
* [Resolution](/how-to-guides/troubleshooting/common-errors-issues/enabling-http-response#resolution)
