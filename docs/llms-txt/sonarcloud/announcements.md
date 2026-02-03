# Source: https://docs.sonarsource.com/sonarqube-cloud/appendices/announcements.md

# Announcements

{% hint style="info" %}
Deprecations are now announced on the [deprecations-and-removals](https://docs.sonarsource.com/sonarqube-cloud/deprecations-and-removals "mention") page.
{% endhint %}

### January 15, 2024 - End of support for Java 11 <a href="#january-15-end-of-support-for-java-11" id="january-15-end-of-support-for-java-11"></a>

Java 11 is no longer supported as scanner runtime environment. The minimum required version of Java is now Java 17.

The installation of Java discussed here refers specifically to the JDK or JRE installed and used in the context where your SonarQube Cloud scanner analysis tool is running. This may be your local build environment or your CI service.

This does not have any impact on the Java version targeted by your project code. You can still analyze Java projects that target versions earlier than 17.

### December 2023 - Node.js 14 and 16 end of service <a href="#december-2023-nodejs-14-and-16-end-of-service" id="december-2023-nodejs-14-and-16-end-of-service"></a>

If you are using a deprecated version of Node.js, versions 14 or 16, in the analysis environment, you must upgrade to Node.js 20, [the active LTS](https://nodejs.org/en/about/previous-releases#release-schedule), to avoid disruption.

* *Node.js 14 is no longer supported*. Your analysis will stop working unless you upgrade your environment. This change is now effective in SonarQube Cloud and will soon be effective in the coming SonarQube Server and SonarQube for IDE versions.
* *Node.js 16 support ends in mid-January 2024*. SonarQube Server 10.4 will be the last version supporting Node.js 16.

From now on, analysis failures will occur immediately for misconfigurations or unsupported versions. This will prevent failed analysis from going unnoticed for long periods of time, which could happen before.

Note that this will only affect your analysis environment, likely part of your CI/CD. Please ensure your analysis environment is using the latest Node.js LTS version, currently Node.js 20. If you are using Automatic Analysis in SonarQube Cloud, no action is needed.

See the [Sonar Community announcement](https://community.sonarsource.com/t/node-js-v14-no-longer-supported-v16-stops-early-next-year/105428) to get more information and help if needed.

### July 2023 - Deprecated support for SonarScanner for Ant <a href="#july-2023-deprecated-support-for-sonarscanner-for-ant" id="july-2023-deprecated-support-for-sonarscanner-for-ant"></a>

The SonarScanner for Ant provides a `task` that is a wrapper of SonarScanner to allow integration of SonarQube Cloud analysis into an Apache Ant build script. It is now deprecated and will be removed in the future. We recommend adjusting your configuration to use the [sonarscanner-cli](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/ci-based-analysis/sonarscanner-cli "mention") directly.

### July 2023 - Deprecated support for Java 11 <a href="#july-2023-deprecated-support-for-java-11" id="july-2023-deprecated-support-for-java-11"></a>

We recommend updating the version of Java installed in the scanner environment to at least Java 17. Java 11 is now deprecated and scanners using this version will stop functioning in the future.

The installation of Java discussed here refers specifically to the JDK or JRE installed and used in the context where your SonarQube Cloud scanner analysis tool is running. This may be your local build environment or your CI service.

This does *not* have any impact on the Java version targeted by your project code. You can still analyze Java projects that target versions earlier than 17.

### September 15, 2022 - Deprecated support for Node.js 12 <a href="#september-15-2022-deprecated-support-for-nodejs-12" id="september-15-2022-deprecated-support-for-nodejs-12"></a>

A Node.js runtime is required to run CI-based analysis of JavaScript, TypeScript or CSS. The minimum version requirement for this runtime will change soon:

We would like to inform you that, as of September 15, 2022, the use of Node.js 12 will no longer be supported by analyses targeting SonarQube Cloud. It has been considered EOL by OpenJS Foundation since March 2022 and has been deprecated since then. This means that support will also be removed in the latest version of SonarQube for IDE. Support for Node.js 12 will end today.

* This means that starting today, analysis of JS/TS/CSS will stop working in Node.js 12 environments. You will no longer be able to create new projects within these environments.
* This will make the minimum supported version of Node.Js 14, but we recommend using the latest LTS version 16.

To continue to enjoy the latest rule updates, you should move your Node.js environment to a supported version as soon as possible:

* The minimum supported version will be Node.js 14.
* The recommended supported version is the latest LTS, which is currently Node.js 16.

The change applies specifically to the version of Node.js installed and used by the SonarQube Cloud scanner analysis tool, either in your local build environment or in your cloud CI service. Please note that this change does not have any impact outside of your analysis runtime.

For more information on how payment and billing work, see [updating-billing-payment-details](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/updating-billing-payment-details "mention").
