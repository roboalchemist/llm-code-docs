# Source: https://docs.xano.com/troubleshooting-and-support/troubleshooting-performance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Performance

### Debugging Performance Issues

502 errors when calling APIs or otherwise experiencing slow performance typically means that you are maxing out your instance resources. This means you should consider ways to increase performance. It is almost impossible to make a strict determination on “what package do I need” because everyone’s logic and data volume is different.

There are several variables to look at when addressing performance issues, including:

* The volume of API requests and the time between them

* The complexity of the business logic

* The amount of data being sent/received.

<Warning>
  If your instance hits maximum resource usage, reported statistics may no longer be accurate.
</Warning>

<Card title="When a single workflow feels slow" href="/troubleshooting-and-support/troubleshooting-performance/when-a-single-workflow-feels-slow" />

<Card title="When everything feels slow" href="/troubleshooting-and-support/troubleshooting-performance/when-everything-feels-slow" />


Built with [Mintlify](https://mintlify.com).