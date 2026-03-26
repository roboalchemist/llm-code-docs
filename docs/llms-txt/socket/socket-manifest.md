# Source: https://docs.socket.dev/docs/socket-manifest.md

# socket manifest

Generate local manifests for certain languages

Generate manifest files for languages without a simple default/declarative manifest format.

```
$ socket manifest --help

  Generate a dependency manifest for given file or dir

  Usage
    $ socket manifest <command>

  Commands
    auto              Auto-detect build and attempt to generate manifest file
    cdxgen            Create an SBOM with CycloneDX generator (cdxgen)
    conda             [beta] Convert a Conda environment.yml file to a python requirements.txt
    gradle            [beta] Use Gradle to generate a manifest file (`pom.xml`) for a Gradle/Java/Kotlin/etc project
    kotlin            [beta] Use Gradle to generate a manifest file (`pom.xml`) for a Kotlin project
    scala             [beta] Generate a manifest file (`pom.xml`) from Scala's `build.sbt` file
    setup             Start interactive configurator to customize default flag values for `socket manifest` in this dir

  Options
    (none)

  Examples
    $ socket manifest --help
```

Some languages are harder to process than others. While we can process the manifest files *(like`package.json` for npm)* on our servers, some languages make this almost impossible without full access to the source code.

## Generate manifest files

In order to work around this `socket manifest` attempts to offer a way for you to generate the manifest files so you can generate a Scan for them and get a report back from your CI/CD pipeline.

```
socket manifest auto ./proj
```

At the time of writing, there are two ecosystems supported this way: Scala's sbt and Gradle.

```
socket manifest gradle ./proj
```

Note: Gradle support implies support for Scala / Kotlin / Maven projects and anything else that uses Gradle.

These commands leverage your local environment to generate the necessary manifest files, which you can then upload to get scanned by calling `socket scan create` on the output directory.

You can see detailed help per language by calling help, for example: `socket manifest gradle --help`

We are still improving use of this command. Please let us know if you run into issues and we'll try to get them resolved as soon as possible.

## Default setup

You can generate a file that overrides defaults per project by running

```
socket manifest setup ./proj
```

This interactive tool will try to detect eligible languages for which it can generate a manifest. You pick any language, regardless of detection, and then pick defaults for flags if you want to. The result is stored in the root of the dir / project in a file called `socket.json` ([more details here](https://docs.socket.dev/docs/socketjson) .

You can setup the defaults this way for multiple languages per project dir. These defaults are picked up when you run the manifest generator directly (ie. `socket manifest gradle ./proj` will apply defaults defined in `./proj/socket.json`) but also `socket manifest auto` and something like `socket scan create --auto-manifest` would leverage these defaults.

## Generate and scan

Once you've setup the manifest defaults for the languages you want to target you can generate the manifest files and run a scan in one go by running

```
socket scan create --auto-manifest ./proj
```

This will first run the equivalent to `socket manifest auto ./proj`, which in turn will try to detect the eligible files in your target directory, generate manifests for languages it found (*applying`socket.json` if available*), and then proceed with a regular `socket scan create` to upload the generated manifest files to do a scan.

## CycloneDX

There is another tool that this command exposes: CycloneDX.

This generates a whole SBOM ("Software Bill Of Materials").

```
socket manifest cdxgen -t java
```

We dedicated a [docs page for cdxgen](socket-cdxgen).