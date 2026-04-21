<!-- Source: https://namespace.so/docs/architecture/compute/macos -->

# macOS

MacOS instances run on Apple M2 Pro or M4 Pro processors, delivering native Apple Silicon performance.
These processors provide hardware acceleration for graphics, machine learning, and compute workloads.

## Built for Apple Development

The platform includes native support for the complete Apple development ecosystem, including Xcode, iOS, and Metal.

Our macOS environment is optimized for Apple development workflows:

- Fast access to the latest Xcode and macOS versions
- Multiple supported OS versions: Sonoma (14), Sequoia (15) and Tahoe (26)
  - Use [shape selectors](#base-image-selection) to specify desired base image.
- Build and test native iOS and macOS applications
- Support for up to 12 vCPU and 56GB of RAM
  - [List of available shapes](/docs/architecture/compute/machine-shapes#macos-configurations)

## VNC Integration

Namespace supports visual debug access which is invaluable for debugging GUI applications, testing user interfaces, and investigating display-related issues.

Access your Mac runners through Remote Display (VNC) directly from the Namespace [dashboard](https://cloud.namespace.so/workspace/instances).

![Tahoe Remote Display](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftahoeremotedisplay.b8f208ef.png&w=1200&q=75)

You can also start a VNC session using our [CLI](/docs/reference/cli/installation):

```
$

```
nsc vnc <instance-id>
```
```

VNC support is currently available for macOS runners. Support for other platforms is in development.

## Base Image Selection

When starting a macOS workload on Namespace you can define requirements for the desired base
image in form of selectors. The selectors are a sequence of name-value pairs passed to instance
creation request. Note that there may be multiple selectors for the same name (all of them will
try to be satisfied).

### Available Selectors

These are the available selectors and options:

| Name | Value | Description |
| --- | --- | --- |
| macos.version |  | base system version |
| `14.x` | macOS Sonoma |
| `15.x` | macOS Sequoia |
| `26.x` | macOS Tahoe |
| image.with |  | can be specified multiple times |
| `xcode-26` | with Xcode 26 |
| `xcode-beta` | with beta versions of Xcode |

Using these selectors you can identify the following images:

`macos.version=14.x`
:   macOS Sonoma

`macos.version=15.x`
:   macOS Sequoia with Xcode 16

`macos.version=15.x,image.with=xcode-26`
:   macOS Sequoia with Xcode 26 and betas

`macos.version=26.x`
:   macOS Tahoe with Xcode 26

`macos.version=26.x,image.with=xcode-beta`
:   macOS Tahoe with Xcode 26 beta

### How to Use

The selectors can be specified on the command line when [`nsc` CLI is used](/docs/reference/cli/create):

```
nsc create --selectors name1=value1,name2=value2 ...
```

They are part of [InstanceShape message](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta#namespace.cloud.compute.v1beta.InstanceShape)
in Namespace SDK.

## macOS Image Updates

Namespace team continuously makes changes to macOS runner images to keep the software up-to-date
and add new Xcode versions as soon as Apple releases them. To get notified about upcoming changes and
releases subscribe to the RSS feed:

[Base Images Updates](https://global.namespaceapis.com/feed/images/githubrunner.rss)

## Xcode 26 Compilation Cache

Xcode 26 introduces a new Compilation Cache feature that significantly speeds up build times by reusing compiled outputs
across checkouts and builds. This feature can be used in conjunction with Namespace
[Cache Volumes](/docs/architecture/storage/cache-volumes) to leverage the compilation cache across CI runs.

### Xcode Caching on GitHub Runners

Xcode caching is fully integrated into Namespace GitHub Runners:

1. [Turn on caching](/docs/solutions/github-actions/caching) for your runners via Runner Profile or runner labels.
2. Add `namespacelabs/nscloud-cache-action` step to your workflow to configure Xcode to use the cache
   (also SwiftPM and CocoaPods caches):

```
    - name: Configure Xcode Caching
      uses: namespacelabs/nscloud-cache-action@v1
      with:
        cache: |
          xcode
          swiftpm
          cocoapods
```

You can verify that the caching kicks in by looking at the `CompilationCacheMetrics` section in the logs that
`xcodebuild` outputs:

```
...
CompilationCacheMetrics
note: 4 hits / 4 cacheable tasks (100%)
...
```

Last updated March 4, 2026
