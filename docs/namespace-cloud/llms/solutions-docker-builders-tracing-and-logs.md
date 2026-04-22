<!-- Source: https://namespace.so/docs/solutions/docker-builders/tracing-and-logs -->

# Docker Build Observability

Gain comprehensive insights into build failures and your build performance with detailed traces, step logs, and attributions.

## Debugging build failures

For any build failure, Namespace extracts and highlights the cause directly in the build dashboard.

![build failure extraction](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ffailure.478a9824.png&w=1200&q=75)

To dive into the failing step, navigate to the logs view.
You can find detailed logs for each step allowing you to understand the context of the failure.

![build step logs](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogs.9410cf1f.png&w=1200&q=75)

To understand the full context of a build failure, Namespace also highlights which commit was used as a base for the build and which build machine executed the build.

![build attribution](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fattribution.583b872e.png&w=1200&q=75)

This contextual information is crucial for debugging because build failures often stem from recent code changes.
You can quickly determine if the failure is related to a specific code change that needs to be reverted, or if environmental factors may play a role.

## Performance Analysis

Moving your builds to Namespace already speeds them up significantly.
The build dashboard also makes it trivial to identify bottlenecks and unlock further performance gains.
To get started, take a look a the slowest recent builds.

![slow builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fslow-builds.c489d4b5.png&w=1200&q=75)

When selecting a build, you can see at a glance which steps were cached.

![cached build steps](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcached-steps.36cd64df.png&w=1200&q=75)

When you frequently find surprising cache misses, this may be indicative of a suboptimal build definition.
Sign up for a [consultation session](mailto:support@namespace.so) to talk to one of our engineers.

When investigating the performance of non-cached steps, the build trace view allows a deeper analysis.
It visualizes the critical path of your build execution and highlights which steps ran in parallel.
This view is ideal to spot which steps dominate the overall build time.

![build layer performance tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftracing.b7ce532c.png&w=1200&q=75)

Critical path analysis for Docker builds

## Build Connections

If your build was requested from within Namespace compute, the connection is recorded and explained in the dashboard.
This allows you to easily go back and understand the context of a build.
When using GitHub Actions, you can jump directly to the run that issued the build.

![build attribution](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fattribution.583b872e.png&w=1200&q=75)

The connection is symmetric. When [debugging GitHub actions](/docs/solutions/github-actions/debugging), you can inspect any associated build with a single click.

![Container Builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainer-builds.7d9275bb.png&w=640&q=75)![Build Tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbuildtrace.c35385df.png&w=828&q=75)

## Hands-on Support

Got stuck? Need help with debugging one of your workflows? Our team is here to assist:

- **Technical Support**: Reach out to [support@namespace.so](mailto:support@namespace.so) to talk to one of our engineers.
- **Community**: Join our community [Discord](https://discord.gg/DqMzDFR6Hc) to learn about tips and best practices.

Last updated August 13, 2025
