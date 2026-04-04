# Source: https://www.aptible.com/docs/core-concepts/security-compliance/ddos-pid-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# DDoS Protection

> Learn how Aptible automatically provides DDoS Protection

# Overview

Aptible VPC-based approach means that most stack components are not accessible from the Internet, and cannot be targeted directly by a distributed denial-of-service (DDoS) attack. Aptible SSL/TLS endpoints include an AWS Elastic Load Balancer, which only supports valid TCP requests, meaning DDoS attacks such as UDP and SYN floods will not reach your app layer.

# PID Limits

Aptible limits the maximum number of tasks (processes or threads) running in your [containers](/core-concepts/architecture/containers/overview) to protect its infrastructure against DDoS attacks, such as fork bombs.

<Note> The PID limit for a single Container is set very high (on the order of the default for a Linux system), so unless your App is misbehaving and allocating too many processes or threads, you're unlikely to ever hit this limit.</Note>

PID usage and PID limit can be monitored through [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview).
