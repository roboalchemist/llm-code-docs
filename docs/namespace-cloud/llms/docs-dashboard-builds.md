<!-- Source: https://namespace.so/docs/dashboard/builds -->

# Builds UI

## Overview

The Build Dashboard provides comprehensive insights into your build performance and failures through detailed traces, step logs, and contextual information.
This centralized view helps you quickly identify, debug, and optimize your Docker builds.

## Build Failure Analysis

**Failure Detection & Highlighting**
The dashboard automatically extracts and highlights build failure causes directly in the main view. Failed builds are prominently displayed with clear error indicators and quick access to detailed diagnostics.

![build failure extraction](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffailure.478a9824.png&w=1200&q=75)

**Step-by-Step Logs**
Navigate to the logs view to examine detailed output for each build step. This granular visibility allows you to understand the exact context and sequence of events leading to failures.

![build step logs](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogs.9410cf1f.png&w=1200&q=75)

**Build Attribution**
Each build failure includes contextual information showing the specific commit used as the build base and the build machine that executed the build.
This attribution data is essential for determining whether failures stem from recent code changes or infrastructure issues.

![build attribution](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fattribution.583b872e.png&w=1200&q=75)

## Performance Monitoring

**Cache Utilization Overview**
The dashboard provides at-a-glance visibility into which build steps utilized cache effectively. Cached steps are clearly marked, helping you identify unexpected cache misses that may indicate suboptimal build definitions.

![cached build steps](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcached-steps.36cd64df.png&w=1200&q=75)

**Critical Path Analysis**
The build trace view visualizes your build execution's critical path, highlighting bottlenecks and parallel execution opportunities.

![build layer performance tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftracing.b7ce532c.png&w=1200&q=75)

Critical path analysis for Docker builds

## Builds in Context

**Integrated Workflow Attribution**
When builds are initiated from Namespace compute environments, the dashboard records and displays these connections, enabling you to trace builds back to their originating workflows.

![build attribution](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fattribution.583b872e.png&w=1200&q=75)

**Bidirectional Navigation**
The connection tracking works both ways - from the dashboard, you can navigate to associated GitHub Actions runs, and from GitHub Actions debugging views, you can inspect related builds with a single click.

![Container Builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainer-builds.7d9275bb.png&w=640&q=75)![Build Tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbuildtrace.c35385df.png&w=828&q=75)

Last updated July 4, 2025
