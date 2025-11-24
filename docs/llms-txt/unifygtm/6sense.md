# Source: https://docs.unifygtm.com/reference/integrations/6sense.md

# 6sense Integration Guide

> Use your existing subscription to identify website visitors.

# Overview

Unify integrates with 6sense in two ways:

* If you already have a 6sense subscription, you can connect it to Unify by
  providing your API key to identify website visitors.
* [Unify Intent](https://app.unifygtm.com/dashboard/settings/integrations/unify-intent)
  identifies website visitors out of the box and is powered by 6sense as well as
  other providers.

Unify uses 6sense along with various other providers to identify website
visitors. If you already have a 6sense subscription, you can connect it to Unify
by providing your API key.

# Setup

To connect your existing 6sense subscription to Unify, simply navigate to
[Settings -> Integrations -> 6sense](https://app.unifygtm.com/dashboard/settings/integrations/6sense)
and enter your API key. Unify will start using your 6sense account to identify
website visitors.

<Note>
  Some customers do not have their 6sense API token enabled by default. If you
  don't see website visitors being identified soon after entering your API key and
  setting up the website tag, this might be the case for you.

  You can reach out to [support@6sense.com](mailto:support@6sense.com) or your dedicated CSM with the following
  message:

  > Hi there,
  >
  > We need an API token to hit the reveal ([https://epsilon.6sense.com/v3/company/details](https://epsilon.6sense.com/v3/company/details)) API in a server to server (not from the browser) mode.
  >
  > Could you please provide the API key?
  >
  > Thanks,

  They should be able to enable access for you.
</Note>
