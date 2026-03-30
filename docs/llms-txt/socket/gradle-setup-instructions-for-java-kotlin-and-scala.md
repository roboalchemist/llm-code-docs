# Source: https://docs.socket.dev/docs/gradle-setup-instructions-for-java-kotlin-and-scala.md

# Gradle setup instructions (for Java, Kotlin, and Scala)

## `gradle.lockfile`

Committing a `gradle.lockfile` to your source control is the easiest way to use Socket with Gradle. If you haven't already, [enable lockfiles in gradle](https://docs.gradle.org/current/userguide/dependency_locking.html) , and then commit the generated `gradle.lockfile` to source control. No extra setup is required!

### Add dependency locking configuration to `build.gradle`.

1. **Add locking configuration to `build.gradle`:**
   ```groovy
   dependencyLocking {
       lockAllConfigurations()
   }
   ```
   This tells Gradle to track locked versions for all configurations (compileClasspath, runtimeClasspath, etc.)

2. **Run the write-locks command:**
   ```bash
   ./gradlew dependencies --write-locks
   ```
   With locking enabled, this resolves all dependencies and writes their exact versions to `gradle.lockfile`.

### What the lockfile does

* Pins every dependency (direct and transitive) to exact versions
* Ensures reproducible builds across machines/CI
* Fails the build if resolved versions differ from locked versions (unless you explicitly update)

### To update locks later

```bash
./gradlew dependencies --write-locks
```

Or update a single dependency:

```bash
./gradlew dependencies --update-locks org.slf4j:slf4j-api
```

<br />

## CycloneDX

If you are unable to enable `gradle.lockfile`s, then you can use the open source [CycloneDX Gradle plugin](https://github.com/CycloneDX/cyclonedx-gradle-plugin)  to generate and commit an SBOM which Socket will scan.

You can run `socket cdxgen --help` for details.

To setup a single CycloneDX file that can be checked in you can run:

```
socket cdxgen -t gradle -o socket-gradle.cdx.json --install-deps --lifecycle build
```

Alternatively the CLI has made it easier to generate manifest files using your local Gradle setup.

You can use `socket manifest gradle --help` to get more information on how to run Gradle more directly. This will work for Gradle, Kotlin, and Scala projects that use Gradle (not `sbt`, see [Scala setup instructions](https://docs.socket.dev/docs/scala-setup-instructions) for working with Scala's `sbt` files).

After generating the manifest files you can use `socket scan create` to [create a report](https://docs.socket.dev/docs/socket-scan).