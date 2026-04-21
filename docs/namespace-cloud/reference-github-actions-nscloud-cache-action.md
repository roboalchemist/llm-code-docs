<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-cache-action -->

# namespacelabs/nscloud-cache-action

namespacelabs/nscloud-cache-action@v1

Namespace platform provides [Cache Volumes](/docs/solutions/github-actions/caching#cache-volumes)
feature that allows workflows to share data across invocations.

The action performs necessary wiring to store cacheable workflow data on the attached Cache Volume.

The action works by linking the listed directories to directories in the mounted cache volume
(using bind-mounts on Linux and symbolic links on macOS). The content written to the cached
directories will be transparently stored on the mounted cache volume. This way the action does not
need to spend time explicitly downloading and uploading cache content to remote locations.

## Prerequisites

In order to use `nscloud-cache-action`, you need to ensure that a cache volume is attached to the GitHub Actions job.
Check out the [Cache Volumes guide](/docs/solutions/github-actions/caching#cache-volumes)
for details.

It is important to run the cache action *after* the checkout action in the workflow sequence. Checkout action automatically wipes the workspace directory, so it would remove the cached content and prevent new content from being stored on the cache volume.

## Examples

Select languages and frameworksCache arbitrary files

```
name: Tests
jobs:
  tests:
    runs-on: namespace-profile-my-profile
 
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
 
      - name: Install Go
        uses: actions/setup-go@v6
        with:
          cache: false # Skip remote GitHub caching
 
      - name: Set up Go cache
        uses: namespacelabs/nscloud-cache-action@v1
        with:
          cache: go
 
      - name: Go tests
        run: go test ./...
```

## Options

### detect

*`string`* A list of cache modes to enable only if detected in the environment. Set to `true` to detect all available cache modes. See `cache` for a list of available cache modes.

Optional.

### cache

*`string`* A list caching modes to enable. Currently supported languages/frameworks are:

AptBunCocoaPodsComposerDenoGoGolangCI-LintGradleHomebrewMavenMiseNixNPMPlaywrightPNPMPoetryPythonRubyRustSwiftPMUVXcodeYarn

Apt

Cache mode `apt` caches downloaded APT packages on the attached Cache Volume.

The `apt-config` executable must be available before `namespacelabs/nscloud-cache-action` is called.

```
- name: Set up apt cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: apt
```

Bun

Cache mode `bun` caches downloaded packages on the attached Cache Volume.

To enable `bun` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `oven-sh/setup-bun`, no additional configuration is needed:

```
- name: Setup Bun

uses: oven-sh/setup-bun@v2
```

Now you can cache `bun` packages across runs.

```
- name: Set up bun cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: bun
```

CocoaPods

Cache mode `cocoapods` caches CocoaPods cache on the attached Cache Volume.

This mode caches `./Pods` and `~/Library/Caches/CocoaPods`.

```
- name: Set up cocoapods cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: cocoapods
```

Composer

Cache mode `composer` caches downloaded packages which Composer retains in a global Cache, on the attached Cache Volume.

To enable `composer` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `shivammathur/setup-php`, no additional configuration is needed:

```
- name: Setup PHP

uses: shivammathur/setup-php@v2

with:

php-version: '8.3'
```

Composer stores zip archives of downloaded PHP packages in a global cache. The cache action retains this global cache on the attached Cache Volume.

```
- name: Set up composer cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: composer
```

Deno

Cache mode `deno` caches downloaded packages on the attached Cache Volume.

To enable `deno` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `denoland/setup-deno`, disable its built-in cache:

```
- name: Setup Deno

uses: denoland/setup-deno@v2

with:

cache: false
```

Now you can cache Deno packages across runs. The cache action stores the Deno cache directory (from `deno info --json`) on the attached Cache Volume.

```
- name: Set up deno cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: deno
```

Go

Cache mode `go` caches Go modules and Go build artifacts on the attached Cache Volume.

To enable `go` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `actions/setup-go`, disable its built-in cache:

```
- name: Setup Go

uses: actions/setup-go@v5

with:

go-version-file: go.mod

cache: false
```

Now you can cache Go modules and build artifacts across runs. The cache action stores `GOCACHE` and `GOMODCACHE` on the attached Cache Volume.

```
- name: Set up go cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: go
```

GolangCI-Lint

Cache mode `golangci-lint` caches analysis results on the attached Cache Volume. Combine this with the `go` cache mode, as GolangCI-Lint will make use of the Go build cache to speed up things further.

To enable `golangci-lint` cache mode, the `golangci-lint` executable must be available before `namespacelabs/nscloud-cache-action` is called.

Typically you achieve this by first installing `golangci-lint`:

```
- name: Setup golangci-lint

uses: golangci/golangci-lint-action@v8

with:

version: 2.8

install-only: true

skip-cache: true
```

Next, setup the cache:

```
- name: Set up golangci-lint cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: golangci-lint
```

To finish you can either call `golangci-lint` manually, or through the action (skipping the install step):

```
- name: Setup golangci-lint

uses: golangci/golangci-lint-action@v8

with:

version: 2.8

install-mode: none
```

Gradle

Cache mode `gradle` caches Gradle build artifacts on the attached Cache Volume.

When using `actions/setup-java`, disable its built-in cache:

```
- name: Setup Java

uses: actions/setup-java@v5

with:

distribution: temurin

java-version: '21'

cache: ''
```

Now you can cache Gradle build artifacts across runs. The cache action stores `~/.gradle/caches` and `~/.gradle/wrapper` on the attached Cache Volume.

```
- name: Set up gradle cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: gradle
```

Homebrew

Cache mode `brew` retains Homebrew artifact downloads across runs.

The `brew` executable must be available before `namespacelabs/nscloud-cache-action` is called.
This is available by default on macOS runners.

```
- name: Set up brew cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: brew
```

Maven

Cache mode `maven` caches Maven artifacts on the attached Cache Volume.

When using `actions/setup-java`, disable its built-in cache:

```
- name: Setup Java

uses: actions/setup-java@v5

with:

distribution: temurin

java-version: '21'

cache: ''
```

Now you can cache Maven artifacts across runs. The cache action stores `~/.m2/repository` on the attached Cache Volume, which contains remote downloads and temporary build artifacts.

```
- name: Set up maven cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: maven
```

Mise

Cache mode `mise` caches downloaded tools on the attached Cache Volume.

First setup the cache before installing Mise:

```
- name: Set up mise cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: mise
```

Now setup Mise and install packages, making sure to disable its built-in cache:

```
- name: Setup mise

uses: jdx/mise-action@v2

with:

cache: false
```

Nix

Cache mode `nix` caches the Nix store and user cache on the attached Cache Volume.

First setup the cache before installing Nix:

```
- name: Set up nix cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: nix
```

Now install Nix. The `/nix` store will already be mounted from the cache:

```
- name: Install Nix

uses: cachix/install-nix-action@v31

with:

extra_nix_config: |

access-tokens = github.com=${{ secrets.GITHUB_TOKEN }}

system-features = kvm nixos-test
```

NPM

Cache mode `npm` caches downloaded packages on the attached Cache Volume.

To enable `npm` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `actions/setup-node`, make sure to disable its built-in caching with `package-manager-cache: false`:

```
- name: Setup Node

uses: actions/setup-node@v6

with:

package-manager-cache: false
```

Now you can cache npm packages across runs.

```
- name: Set up npm cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: npm
```

Playwright

Cache mode `playwright` stores the downloaded browsers on the attached Cache Volume.

The cache action detects the browser cache directory automatically based on the platform.

```
- name: Set up playwright cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: playwright
```

See the [example repo](https://github.com/namespace-integration-demos/playwright) for a working example.

PNPM

Cache mode `pnpm` caches downloaded packages on the attached Cache Volume.

To enable `pnpm` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `pnpm/action-setup`, no additional configuration is needed:

```
- name: Setup pnpm

uses: pnpm/action-setup@v4
```

Now you can cache pnpm packages across runs.

```
- name: Set up pnpm cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: pnpm
```

Poetry

Cache mode `poetry` caches downloaded packages on the attached Cache Volume.

To enable `poetry` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

One way of achieving that is via `pipx`:

```
- name: Install Poetry

run: pipx install poetry
```

Now you can cache Poetry packages across runs.

```
- name: Set up poetry cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: poetry
```

Python

Cache mode `python` retains the pip cache directory across runs.

The `pip` executable is available by default on GitHub runners.

```
- name: Set up python cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: python
```

Ruby

Cache mode `ruby` caches Bundler packages on the attached Cache Volume.

When using `ruby/setup-ruby`, disable its built-in cache:

```
- name: Setup Ruby

uses: ruby/setup-ruby@v1

with:

ruby-version: '3.2'

bundler-cache: false
```

Now you can cache Bundler packages across runs.

```
- name: Set up ruby cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: ruby
```

Rust

Cache mode `rust` caches Cargo registry, git dependencies, and build artifacts on the attached Cache Volume.

When using `actions-rust-lang/setup-rust-toolchain`, disable its built-in cache:

```
- name: Setup Rust

uses: actions-rust-lang/setup-rust-toolchain@v1

with:

cache: false
```

Now you can cache Rust packages across runs.

```
- name: Set up rust cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: rust
```

SwiftPM

Cache mode `swiftpm` caches Swift Package Manager build artifacts and module cache on the attached Cache Volume.

The cache action stores `./.build`, `~/Library/Caches/org.swift.swiftpm`, and `~/Library/org.swift.swiftpm` on the attached Cache Volume.

```
- name: Set up swiftpm cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: swiftpm
```

UV

Cache mode `uv` caches downloaded packages on the attached Cache Volume.

To enable `uv` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

When using `astral-sh/setup-uv`, disable its built-in cache:

```
- name: Setup uv

uses: astral-sh/setup-uv@v5

with:

enable-cache: false
```

Now you can cache uv packages across runs.

```
- name: Set up uv cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: uv
```

Xcode

Cache mode `xcode` caches Xcode's DerivedData and Compilation Cache on the attached Cache Volume.

The `xcodebuild` executable is available by default on macOS runners. This cache mode also enables Xcode's Compilation Cache feature.

```
- name: Set up xcode cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: xcode
```

Yarn

To enable `yarn` cache mode, the executable must be available before `namespacelabs/nscloud-cache-action` is called.

You can enable Yarn using Corepack (included with Node.js), making sure to not set a cache value:

```
- name: Setup Node

uses: actions/setup-node@v4

with:

node-version: '22'

cache: ''

- name: Enable Corepack

run: corepack enable
```

Yarn stores every package in a global cache. The cache action retains this global cache on the attached Cache Volume. The cache location is detected automatically based on Yarn version (v1 uses `yarn cache dir`, v2+ uses `yarn config get cacheFolder`).

```
- name: Set up yarn cache

uses: namespacelabs/nscloud-cache-action@v1

with:

cache: yarn
```

You can enable multiple caching modes and can also add additional paths to the cache using `path`.

```
- name: Set up Go and Rust cache
  uses: namespacelabs/nscloud-cache-action@v1
  with:
    cache: |
      go
      rust
```

### path

*`string`* A list of files, directories, to cache and restore. `~` is resolved to `$HOME`. Can be used in concert with `cache`.

```
- name: Set up Go cache
  uses: namespacelabs/nscloud-cache-action@v1
  with:
    path: |
      /home/runner/.cache/go-build
      /home/runner/go/pkg/mod
```

Note: Contents of [`${{ runner.temp }}`](https://docs.github.com/en/actions/reference/contexts-reference#runner-context) cannot be cached as this directory is emptied at the beginning and end of each job.

### fail-on-cache-miss

*`boolean`* If enabled, fail the workflow if the path is not found on the cache volume.

---

## Advanced: Running GitHub Jobs in Containers

We recommend using a separate profile for your workflows that run in containers.

GitHub Actions run as user runner by default. Running in a container can change the user. Sharing caches from different users may lead to permission errors when accessing the cache.

[Details →](/docs/solutions/github-actions#configure-your-runners)

When using [containers to run GitHub Jobs](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container), extra configuration is required to make
the cache action work correctly.

1. The Cache Volume path `/cache` must be mounted into the container.
2. The env var `NSC_CACHE_PATH` must be set.
3. Container needs to have `SYS_ADMIN` capability, so that the cache action has permissions to call the `mount` command.
4. The `sudo`, `mkdir` and `chown` binaries must be available in the container image, or must be installed.

This action relies on specific properties of the environment and may require tuning to work with images that significantly diverge from Ubuntu. Please reach out to us at [support@namespace.so](mailto:support@namespace.so) for assistance.

See the following snippet for a working example.

```
name: NPM tests on Playwright
jobs:
  tests:
    runs-on: namespace-profile-my-profile-for-containers
 
    container:
      image: mcr.microsoft.com/playwright:v1.39.0
      env:
        NSC_CACHE_PATH: ${{ env.NSC_CACHE_PATH }} # env.NSC_CACHE_PATH contains the path to Cache Volume directory, that is `/cache`.
      volumes:
        - /cache:/cache # Where the Cache Volume is mounted.
      options: --cap-add=SYS_ADMIN # Required to by nscloud-cache-action to call `mount`.
 
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
 
      - name: Install sudo
        run: |
          apt-get update -y && apt-get install -y sudo
 
      - name: Setup PNPM cache
        uses: namespacelabs/nscloud-cache-action@v1
        with:
          cache: pnpm
 
      - name: Install dependencies and run tests
        run: |
          pnpm install
          pnpm run test
```

Last updated February 13, 2026
