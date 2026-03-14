# Source: https://help.aikido.dev/code-scanning/scanning-practices/java-scala-kotlin-projects-using-gradle-security-scanning-best-practices.md

# Java/Scala/Kotlin Projects Using Gradle: Security Scanning Best Practices

Aikido can find known vulnerabilities (CVE) in your Java dependencies as well as dangerous licenses being used by those dependencies.

How does Aikido find those dependencies and their transitive subdependencies?

Out of the box, Aikido supports the following files for scanning:

* gradle.lockfile
* pom.xml
* .jar/.war/.ear

It should be noted that build.gradle.\* (Gradle manifest) files might not contain exact versions for some of your dependencies. This can cause Aikido to not find the full range of risks in your application.

It's recommended to use Gradle lockfiles that contain an exact version for each dependency as well as the subdependencies.

There are other reasons to use lockfiles besides making security scanning easier for Aikido:

* Using a lockfile protects you against supply chain attacks via malicious packages. This kind of attack is becoming more popular
* Using a lockfiles makes your build more predictable as everyone is using the exact same minor version of packages. Less chance of 'works on my machine'
* Faster build times: no need for dependency resolution anymore

## How to start using lockfiles in your Gradle project? <a href="#how-to-start-using-lockfiles-in-your-gradle-project" id="how-to-start-using-lockfiles-in-your-gradle-project"></a>

Add a few lines of code to your Gradle manifest files as seen in this documentation:

<https://docs.gradle.org/current/userguide/dependency_locking.html#ex-locking-all-configurations>

Then, run "gradle dependencies --write-locks" to create lockfiles and commit those to your repository. You should never manually edit this file, similar to how you would use a package-lock.json file in NPM in NodeJS world.

After adding these files, Aikido will be able to scan your dependencies.

***
