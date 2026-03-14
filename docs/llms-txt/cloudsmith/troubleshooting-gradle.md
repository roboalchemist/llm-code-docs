# Source: https://help.cloudsmith.io/docs/troubleshooting-gradle.md

# Troubleshooting Gradle

**Occasional Publish Failures**

Gradle + Java8 can experience issues with SNI (Server Name Indicator) endpoints which we use to power our CDN, like **[https://maven.cloudsmith.io](https://maven.cloudsmith.io)**.  If you experience occasional or intermittent publish failures, resulting in a 443 error, then please update your endpoint to **[https://api-g.cloudsmith.io/maven/](https://api-g.cloudsmith.io/maven/)** .

Contact us [here](https://support.cloudsmith.com). We're always happy to help!