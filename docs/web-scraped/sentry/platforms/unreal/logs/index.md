---
---
title: Set Up Logs
description: "Structured logs allow you to send, view and query logs sent from your applications within Sentry."
---

With Sentry Structured Logs, you can send text-based log information from your Unreal Engine applications to Sentry. Once in Sentry, these logs can be viewed alongside relevant errors, searched by text-string, or searched using their individual attributes.

## Requirements

## Setup

## Usage

## Options

## Default Attributes

## Performance Considerations

- Logs are sent asynchronously to avoid impacting game performance
- Consider disabling Debug level logs in production to avoid excessive log volume
- Each severity level can be individually controlled to fine-tune what gets sent to Sentry
- Use categories to organize logs and make them easier to search and filter
- Before-log handlers are executed synchronously, so keep processing lightweight