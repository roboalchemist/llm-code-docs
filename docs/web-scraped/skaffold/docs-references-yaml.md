# Source: https://skaffold.dev/docs/references/yaml/

Title: skaffold.yaml

URL Source: https://skaffold.dev/docs/references/yaml/

Markdown Content:
SKAFFOLD
Documentation
skaffold.yaml
Versions 
Documentation
Installing Skaffold
Upgrading from Skaffold v1 to Skaffold v2 [NEW]
Quickstart
Guides
Getting Started With Your Project
Continuous Development
Debugging
Continuous Delivery
Managing ARM workloads [NEW]
Skaffold Pipeline Stages
Init
Build
Builder types
Docker
Jib
Bazel
Custom
Buildpacks
ko
Environments
Local build
In cluster
Google Cloud Build
Cross/multi-platform
Deploy [UPDATED]
Kubectl
Kpt [UPDATED]
Helm [UPDATED]
Docker
Google Cloud Run [NEW]
Render [NEW]
Raw YAML
Kpt [NEW]
Kustomize
Helm [UPDATED]
Test
Container Structure Test
Custom Test
Tag
File Sync
Log Tailing
Verify [NEW]
Deploy Status Checking
Lifecycle Hooks
Port Forwarding
Cleanup
Custom Actions
Architecture and Design
Skaffold Pipeline
Global Configuration
Skaffold API
Environment Management
Load ENV from a file
Local Cluster
Image Repository Handling
Profiles
Kube-context Activation
Templated Fields
Tutorials
Build and deploy on Kubernetes
Manage CRDs w/ Skaffold - Configuring Which K8s Resources & Fields Skaffold Manages
Build Dependencies
Config Dependencies
Custom Build Script
Developer Journey
Go integration test coverage profiles
Overriding the buildpacks run image
Skaffold in CI/CD
References
CLI
skaffold.yaml
API
gRPC API
HTTP API
API V2
gRPC API
HTTP API
Privacy Settings
Deprecation Policy
Resources
Skaffold Feedback
Telemetry
 Edit this page
 Create documentation issue


Schema Versions
v4beta13
v4beta12
v4beta11
v4beta10
v4beta9
v4beta8
v4beta7
v4beta6
v4beta5
v4beta4
v4beta3
v4beta2
v4beta1
v3
v3alpha1
v2beta29
v2beta28
v2beta27
v2beta26
v2beta25
v2beta24
v2beta23
v2beta22
v2beta21
v2beta20
v2beta19
v2beta18
v2beta17
v2beta16
v2beta15
v2beta14
v2beta13
v2beta12
v2beta11
v2beta10
v2beta9
v2beta8
v2beta7
v2beta6
v2beta5
v2beta4
v2beta3
v2beta2
v2beta1
v2alpha4
v2alpha3
v2alpha2
v2alpha1
v1beta17
v1beta16
v1beta15
v1beta14
v1beta13
v1beta12
v1beta11
v1beta10
v1beta9
v1beta8
v1beta7
v1beta6
v1beta5
v1beta4
v1beta3
v1beta2
v1beta1
v1alpha5
v1alpha4
v1alpha3
v1alpha2
v1alpha1
v1
Documentation
References
skaffold.yaml
skaffold.yaml
💡 Tip

The Cloud Code IDE extensions (see install options) provide authoring assistance for skaffold.yaml files in the form of schema based validation, diagnostics, quick documentation, code completions, and snippets, that can make it easier to create and edit these files.

You can now navigate the skaffold.yaml reference from an inner element to its upper levels using the tooltip that appears on hover, clicking on the parent element you want to go:

Note

Important: To use this schema, you need Skaffold version 2.15.0 or later. Release Notes

apiVersion: skaffold/v4beta13 latest	# 	version of the configuration.
kind: Config	# 	always Config.
metadata:	# 	holds additional information about the config.
name:	# 	an identifier for the project.
labels: {}	# 	a map of labels identifying the project.
annotations: {}	# 	a map of annotations providing additional metadata about the project.
requires:	# 	describes a list of other required configs for the current config.
- configs: []	# 	includes specific named configs within the file path. If empty, then all configs in the file are included.
path:	# 	describes the path to the file containing the required configs.
git:	# 	describes a remote git repository containing the required configs.
repo:	# 	git repository the package should be cloned from. e.g. https://github.com/GoogleContainerTools/skaffold.git.
path:	# 	relative path from the repo root to the skaffold configuration file. eg. getting-started/skaffold.yaml.
ref:	# 	git ref the package should be cloned from. eg. master or main.
sync:	# 	when set to true will reset the cached repository to the latest commit from remote on every run. To use the cached repository with uncommitted changes or unpushed commits, it needs to be set to false.
googleCloudStorage:	# 	describes remote Google Cloud Storage objects containing the required configs.
source:	# 	Google Cloud Storage objects to copy. e.g. gs://my-bucket/dir1/dir2/*.
path:	# 	relative path from the source to the skaffold configuration file. e.g. configs/skaffold.yaml.
sync:	# 	when set to true will reset the cached object to the latest remote version on every run.
googleCloudBuildRepoV2:	# 	describes a Google Cloud Build repository (2nd gen) that points to a repo with the required configs.
projectID:	# 	ID of the GCP project where the repository is configured.
region:	# 	GCP region where the repository is configured.
connection:	# 	name of the GCB repository connection associated with the repo.
repo:	# 	name of repository under the given connection.
path:	# 	relative path from the repo root to the skaffold configuration file. eg. getting-started/skaffold.yaml.
ref:	# 	git ref the repo should be cloned from. e.g. master or main.
sync:	# 	when set to true will reset the cached repository to the latest commit from remote on every run. To use the cached repository with uncommitted changes or unpushed commits, it needs to be set to false.
activeProfiles:	# 	describes the list of profiles to activate when resolving the required configs. These profiles must exist in the imported config.
- name:	# 	describes name of the profile to activate in the dependency config. It should exist in the dependency config.
activatedBy: []	# 	describes a list of profiles in the current config that when activated will also activate the named profile in the dependency config. If empty then the named profile is always activated.
build:	# 	describes how images are built.
hooks:	# 	describes a set of lifecycle hooks that are executed before and after the build phase of the Pipeline, where the artifacts are built.
before:	# 	describes the list of lifecycle hooks to execute before each artifact build step.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
after:	# 	describes the list of lifecycle hooks to execute after each artifact build step.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
artifacts:	# 	the images you're going to be building.
- image: gcr.io/k8s-skaffold/example	# 	name of the image to be built.
context: .	# 	directory containing the artifact's sources.
sync: infer: ["**/*"]	# 	beta local files synced to pods instead of triggering an image build when modified. If no files are listed, sync all the files and infer the destination.
manual:	# 	manual sync rules indicating the source and destination.
- src: "css/**/*.css"	# 	a glob pattern to match local paths against. Directories should be delimited by / on all platforms.
dest: "app/"	# 	destination path in the container where the files should be synced to.
strip: "css/"	# 	specifies the path prefix to remove from the source path when transplanting the files into the destination folder.
infer: []	# 	file patterns which may be synced into the container The container destination is inferred by the builder based on the instructions of a Dockerfile. Available for docker and kaniko artifacts and custom artifacts that declare dependencies on a dockerfile.
auto:	# 	delegates discovery of sync rules to the build system. Only available for jib and buildpacks.
hooks:	# 	describes a set of lifecycle hooks that are executed before and after each file sync action on the target artifact's containers.
before:	# 	describes the list of lifecycle hooks to execute before each artifact sync step.
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
after:	# 	describes the list of lifecycle hooks to execute after each artifact sync step.
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
requires:	# 	describes build artifacts that this artifact depends on.
- image:	# 	a reference to an artifact's image name.
alias:	# 	a token that is replaced with the image reference in the builder definition files. For example, the docker builder will use the alias as a build-arg key. Defaults to the value of image.
hooks:	# 	describes a set of lifecycle hooks that are executed before and after each build of the target artifact.
before:	# 	describes the list of lifecycle hooks to execute before each artifact build step.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
after:	# 	describes the list of lifecycle hooks to execute after each artifact build step.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
platforms: []	# 	list of platforms to build this artifact image for. It overrides the values inferred through heuristics or provided in the top level platforms property or in the global config. If the target builder cannot build for atleast one of the specified platforms, then the build fails. Each platform is of the format os[/arch[/variant]], e.g., linux/amd64. Example: ["linux/amd64", "linux/arm64"].
runtimeType:	# 	specifies the target language runtime for this artifact that is used to configure debug support. Should be one of go, nodejs, jvm, python or netcore. If unspecified the language runtime is inferred from common heuristics for the list of supported runtimes.
docker:	# 	beta describes an artifact built from a Dockerfile.
dockerfile: Dockerfile	# 	locates the Dockerfile relative to workspace.
target:	# 	Dockerfile target name to build.
buildArgs:	# 	arguments passed to the docker build.
key1:value1	# 
key2:{{ .ENV_VAR }}	# 
network:	# 	passed through to docker and overrides the network configuration of docker builder. If unset, use whatever is configured in the underlying docker daemon. Examples: host: use the host's networking stack. bridge: use the bridged network configuration. container:<name|id>: reuse another container's network stack. none: no networking in the container. my-custom-network: user-defined network.
addHost:	# 	add host.
- "host1:ip1"	# 
- "host2:ip2"	# 
cacheFrom:	# 	the Docker images used as cache sources.
- "golang:1.10.1-alpine3.7"	# 
- "alpine:3.7"	# 
cliFlags: []	# 	any additional flags to pass to the local daemon during a build. These flags are only used during a build through the Docker CLI.
pullParent: false	# 	used to attempt pulling the parent image even if an older image exists locally.
noCache: false	# 	set to true to pass in --no-cache to docker build, which will prevent caching.
squash: false	# 	used to pass in --squash to docker build to squash docker image layers into single layer.
secrets:	# 	used to pass in --secret to docker build, useBuildKit: true is required.
- id:	# 	id of the secret.
src:	# 	path to the secret on the host machine.
env:	# 	environment variable name containing the secret value.
ssh:	# 	used to pass in --ssh to docker build to use SSH agent. Format is "default|[=|[,]]".
bazel:	# 	beta requires bazel CLI to be installed and the sources to contain Bazel configuration files.
target: //:skaffold_example.tar	# 	bazel build target to run.
args:	# 	additional args to pass to bazel build.
- "-flag"	# 
- "--otherflag"	# 
platforms:	# 	configure the --platforms flag for bazel build based on the configured skaffold target platform.
- platform:	# 	skaffold platform.
target:	# 	bazel platform target to be passed to bazel's --platforms flag.
ko:	# 	builds images using ko.
fromImage:	# 	overrides the default ko base image (gcr.io/distroless/static:nonroot). Corresponds to, and overrides, the defaultBaseImage in .ko.yaml.
dependencies:	# 	file dependencies that Skaffold should watch for both rebuilding and file syncing for this artifact.
paths:	# 	should be set to the file dependencies for this artifact, so that the Skaffold file watcher knows when to rebuild and perform file synchronization.
- "**/*.go"	# 
ignore: []	# 	specifies the paths that should be ignored by Skaffold's file watcher. If a file exists in both paths and in ignore, it will be ignored, and will be excluded from both rebuilds and file synchronization.
dir:	# 	directory where the go tool will be run. The value is a directory path relative to the context directory. If empty, the go tool will run in the context directory. Example: ./my-app-sources.
env:	# 	environment variables, in the key=value form, passed to the build. These environment variables are only used at build time. They are not set in the resulting container image.
- "GOPRIVATE=git.example.com"	# 
- "GOCACHE=/workspace/.gocache"	# 
flags:	# 	additional build flags passed to go build.
- "-trimpath"	# 
- "-v"	# 
labels:	# 	key-value string pairs to add to the image config.
foo:bar	# 
ldflags:	# 	linker flags passed to the builder.
- "-buildid="	# 
- "-s"	# 
- "-w"	# 
main:	# 	location of the main package. It is the pattern passed to go build. If main is specified as a relative path, it is relative to the context directory. If main is empty, the ko builder uses a default value of .. If main is a pattern with wildcards, such as ./..., the expansion must contain only one main package, otherwise ko fails. Main is ignored if the ImageName starts with ko://. Example: ./cmd/foo.
jib:	# 	builds images using the Jib plugins for Maven or Gradle.
project:	# 	selects which sub-project to build for multi-module builds.
args:	# 	additional build flags passed to the builder.
- "--no-build-cache"	# 
type:	# 	the Jib builder type; normally determined automatically. Valid types are maven: for Maven. gradle: for Gradle.
fromImage:	# 	overrides the configured jib base image.
kaniko:	# 	builds images using kaniko.
cleanup: false	# 	to clean the filesystem at the end of the build.
insecure: false	# 	if you want to push images to a plain HTTP registry.
insecurePull: false	# 	if you want to pull images from a plain HTTP registry.
force: false	# 	building outside of a container.
logTimestamp: false	# 	to add timestamps to log format.
reproducible: false	# 	used to strip timestamps out of the built image.
singleSnapshot: false	# 	takes a single snapshot of the filesystem at the end of the build. So only one layer will be appended to the base image.
skipTLS: false	# 	skips TLS certificate validation when pushing to a registry.
skipTLSVerifyPull: false	# 	skips TLS certificate validation when pulling from a registry.
skipUnusedStages: false	# 	builds only used stages if defined to true. Otherwise it builds by default all stages, even the unnecessaries ones until it reaches the target stage / end of Dockerfile.
useNewRun: false	# 	to Use the experimental run implementation for detecting changes without requiring file system snapshots. In some cases, this may improve build performance by 75%.
whitelistVarRun: false	# 	used to ignore /var/run when taking image snapshot. Set it to false to preserve /var/run/* in destination image.
dockerfile: Dockerfile	# 	locates the Dockerfile relative to workspace.
target:	# 	to indicate which build stage is the target build stage.
initImage:	# 	image used to run init container which mounts kaniko context.
image:	# 	Docker image used by the Kaniko pod. Defaults to the latest released version of gcr.io/kaniko-project/executor.
imagePullSecret:	# 	name of the Kubernetes secret for pulling kaniko image and kaniko init image from a private registry.
destination: []	# 	additional tags to push.
digestFile:	# 	to specify a file in the container. This file will receive the digest of a built image. This can be used to automatically track the exact image built by kaniko.
imageFSExtractRetry:	# 	number of retries that should happen for extracting an image filesystem.
imageNameWithDigestFile:	# 	specify a file to save the image name with digest of the built image to.
logFormat:	# 	to set the log format.
ociLayoutPath:	# 	to specify a directory in the container where the OCI image layout of a built image will be placed. This can be used to automatically track the exact image built by kaniko.
registryMirror:	# 	if you want to use a registry mirror instead of default index.docker.io.
snapshotMode:	# 	how Kaniko will snapshot the filesystem.
pushRetry:	# 	Set this flag to the number of retries that should happen for the push of an image to a remote destination.
tarPath:	# 	path to save the image as a tarball at path instead of pushing the image.
verbosity:	# 	to set the logging level.
insecureRegistry: []	# 	to use plain HTTP requests when accessing a registry.
skipTLSVerifyRegistry: []	# 	skips TLS certificate validation when accessing a registry.
env:	# 	environment variables passed to the kaniko pod. It also accepts environment variables via the go template syntax.
- {"name":"key1","value":"value1"}	# 
- {"name":"key2","value":"value2"}	# 
- {"name":"key3","value":"'{{.ENV_VARIABLE}}'"}	# 
cache:	# 	configures Kaniko caching. If a cache is specified, Kaniko will use a remote cache which will speed up builds.
repo:	# 	a remote repository to store cached layers. If none is specified, one will be inferred from the image name. See Kaniko Caching.
hostPath:	# 	specifies a path on the host that is mounted to each pod as read only cache volume containing base images. If set, must exist on each node and prepopulated with kaniko-warmer.
ttl:	# 	Cache timeout in hours.
cacheCopyLayers: false	# 	enables caching of copy layers.
cacheRunLayers:	# 	enables caching of run layers (default=true).
registryCertificate: {}	# 	to provide a certificate for TLS communication with a given registry. my.registry.url: /path/to/the/certificate.cert is the expected format.
label: {}	# 	key: value to set some metadata to the final image. This is equivalent as using the LABEL within the Dockerfile.
buildArgs:	# 	arguments passed to the docker build. It also accepts environment variables and generated values via the go template syntax. Exposed generated values: IMAGEREPO, IMAGENAME, IMAGE_TAG.
key1:value1	# 
key2:value2	# 
key3:'{{.ENV_VARIABLE}}'	# 
volumeMounts: []	# 	volume mounts passed to kaniko pod.
contextSubPath:	# 	to specify a sub path within the context.
ignorePaths: []	# 	a list of ignored paths when making an image snapshot.
copyMaxRetries: 3	# 	number of times to retry copy build contexts to a cluster if it fails.
copyTimeout:	# 	timeout for copying build contexts to a cluster. Defaults to 5 minutes (5m).
buildContextCompressionLevel: 1	# 	gzip compression level(0-9) for the build context. 0: NoCompression. 1: BestSpeed. 9: BestCompression. -1: DefaultCompression. -2: HuffmanOnly.
buildpacks:	# 	builds images using Cloud Native Buildpacks.
builder:	# 	builder image used.
runImage:	# 	overrides the stack's default run image.
env:	# 	environment variables, in the key=value form, passed to the build. Values can use the go template syntax.
- "key1=value1"	# 
- "key2=value2"	# 
- "key3={{.ENV_VARIABLE}}"	# 
buildpacks: []	# 	a list of strings, where each string is a specific buildpack to use with the builder. If you specify buildpacks the builder image automatic detection will be ignored. These buildpacks will be used to build the Image from your source code. Order matters.
trustBuilder: false	# 	indicates that the builder should be trusted.
clearCache: false	# 	removes old cache volume associated with the specific image and supplies a clean cache volume for build.
projectDescriptor: project.toml	# 	path to the project descriptor file.
dependencies:	# 	file dependencies that skaffold should watch for both rebuilding and file syncing for this artifact.
paths: []	# 	should be set to the file dependencies for this artifact, so that the skaffold file watcher knows when to rebuild and perform file synchronization.
ignore: []	# 	specifies the paths that should be ignored by skaffold's file watcher. If a file exists in both paths and in ignore, it will be ignored, and will be excluded from both rebuilds and file synchronization. Will only work in conjunction with paths.
volumes:	# 	support mounting host volumes into the container.
- host:	# 	local volume or absolute directory of the path to mount.
target:	# 	path where the file or directory is available in the container. It is strongly recommended to not specify locations under /cnb or /layers.
options:	# 	specify a list of comma-separated mount options. Valid options are: ro (default): volume contents are read-only. rw: volume contents are readable and writable. volume-opt=<key>=<value>: can be specified more than once, takes a key-value pair.
custom:	# 	beta builds images using a custom build script written by the user.
buildCommand:	# 	command executed to build the image.
dependencies:	# 	file dependencies that skaffold should watch for both rebuilding and file syncing for this artifact.
dockerfile:	# 	should be set if the artifact is built from a Dockerfile, from which skaffold can determine dependencies.
path:	# 	locates the Dockerfile relative to workspace.
buildArgs:	# 	key/value pairs used to resolve values of ARG instructions in a Dockerfile. Values can be constants or environment variables via the go template syntax.
key1:value1	# 
key2:value2	# 
key3:'{{.ENV_VARIABLE}}'	# 
command:	# 	represents a custom command that skaffold executes to obtain dependencies. The output of this command must be a valid JSON array.
paths: []	# 	should be set to the file dependencies for this artifact, so that the skaffold file watcher knows when to rebuild and perform file synchronization.
ignore: []	# 	specifies the paths that should be ignored by skaffold's file watcher. If a file exists in both paths and in ignore, it will be ignored, and will be excluded from both rebuilds and file synchronization. Will only work in conjunction with paths.
insecureRegistries: []	# 	a list of registries declared by the user to be insecure. These registries will be connected to via HTTP instead of HTTPS.
tagPolicy:	# 	beta determines how images are tagged. A few strategies are provided here, although you most likely won't need to care! If not specified, it defaults to gitCommit: {variant: Tags}.
gitCommit:	# 	beta tags images with the git tag or commit of the artifact's workspace.
variant:	# 	determines the behavior of the git tagger. Valid variants are: Tags (default): use git tags or fall back to abbreviated commit hash. CommitSha: use the full git commit sha. AbbrevCommitSha: use the abbreviated git commit sha. TreeSha: use the full tree hash of the artifact workingdir. AbbrevTreeSha: use the abbreviated tree hash of the artifact workingdir.
prefix:	# 	adds a fixed prefix to the tag.
ignoreChanges: false	# 	specifies whether to omit the -dirty postfix if there are uncommitted changes.
sha256: {}	# 	beta tags images with their sha256 digest.
envTemplate:	# 	beta tags images with a configurable template string.
template: {{.RELEASE}}	# 	used to produce the image name and tag. See golang text/template. The template is executed against the current environment, with those variables injected.
dateTime:	# 	beta tags images with the build timestamp.
format: 2006-01-02_15-04-05.999_MST	# 	formats the date and time. See #Time.Format.
timezone:	# 	sets the timezone for the date and time. See Time.LoadLocation. Defaults to the local timezone.
customTemplate:	# 	beta tags images with a configurable template string composed of other taggers.
template: {{.DATE}}	# 	used to produce the image name and tag. See golang text/template. The template is executed against the provided components with those variables injected.
components:	# 	TaggerComponents that the template (see field above) can be executed against.
inputDigest: {}	# 	beta tags images with their sha256 digest of their content.
platforms: []	# 	list of platforms to build all artifact images for. It can be overridden by the individual artifact's platforms property. If the target builder cannot build for atleast one of the specified platforms, then the build fails. Each platform is of the format os[/arch[/variant]], e.g., linux/amd64. Example: ["linux/amd64", "linux/arm64"].
local:	# 	beta describes how to do a build on the local docker daemon and optionally push to a repository.
push:	# 	should images be pushed to a registry. If not specified, images are pushed only if the current Kubernetes context connects to a remote cluster.
tryImportMissing: false	# 	whether to attempt to import artifacts from Docker (either a local or remote registry) if not in the cache.
useDockerCLI: false	# 	use docker command-line interface instead of Docker Engine APIs.
useBuildkit:	# 	use BuildKit to build Docker images. If unspecified, uses the Docker default.
concurrency: 1	# 	how many artifacts can be built concurrently. 0 means "no-limit".
googleCloudBuild:	# 	beta describes how to do a remote build on Google Cloud Build.
projectId:	# 	ID of your Cloud Platform Project. If it is not provided, Skaffold will guess it from the image name. For example, given the artifact image name gcr.io/myproject/image, Skaffold will use the myproject GCP project.
diskSizeGb:	# 	disk size of the VM that runs the build. See Cloud Build Reference.
machineType:	# 	type of the VM that runs the build. See Cloud Build Reference.
timeout:	# 	amount of time (in seconds) that this build should be allowed to run. See Cloud Build Reference.
logging:	# 	specifies the logging mode. Valid modes are: LOGGING_UNSPECIFIED: The service determines the logging mode. LEGACY: Stackdriver logging and Cloud Storage logging are enabled (default). GCS_ONLY: Only Cloud Storage logging is enabled. See Cloud Build Reference.
logStreamingOption:	# 	specifies the behavior when writing build logs to Google Cloud Storage. Valid options are: STREAM_DEFAULT: Service may automatically determine build log streaming behavior. STREAM_ON: Build logs should be streamed to Google Cloud Storage. STREAM_OFF: Build logs should not be streamed to Google Cloud Storage; they will be written when the build is completed. See Cloud Build Reference.
dockerImage: gcr.io/cloud-builders/docker	# 	image that runs a Docker build. See Cloud Builders.
kanikoImage: gcr.io/kaniko-project/executor	# 	image that runs a Kaniko build. See Cloud Builders.
mavenImage: gcr.io/cloud-builders/mvn	# 	image that runs a Maven build. See Cloud Builders.
gradleImage: gcr.io/cloud-builders/gradle	# 	image that runs a Gradle build. See Cloud Builders.
packImage: gcr.io/k8s-skaffold/pack	# 	image that runs a Cloud Native Buildpacks build. See Cloud Builders.
koImage: gcr.io/k8s-skaffold/skaffold	# 	image that runs a ko build. The image must contain Skaffold, Go, and a shell (runnable as sh) that supports here documents. See Cloud Builders.
bucket:	# 	specifies the Cloud Storage bucket to store the staged build sources.
concurrency: 0	# 	how many artifacts can be built concurrently. 0 means "no-limit".
workerPool:	# 	configures a pool of workers to run the build.
region:	# 	configures the region to run the build. If WorkerPool is configured, the region will be deduced from the WorkerPool configuration. If neither WorkerPool nor Region is configured, the build will be run in global(non-regional). See Cloud Build locations.
platformEmulatorInstallStep:	# 	specifies a pre-build step to install the required tooling for QEMU emulation on the GoogleCloudBuild containers. This enables performing cross-platform builds on GoogleCloudBuild. If unspecified, Skaffold uses the docker/binfmt image by default.
image:	# 	specifies the image that will install the required tooling for QEMU emulation on the GoogleCloudBuild containers.
args: []	# 	specifies arguments passed to the emulator installer image.
entrypoint:	# 	specifies the ENTRYPOINT argument to the emulator installer image.
serviceAccount:	# 	Google Cloud platform service account used by Cloud Build. If unspecified, it defaults to the Cloud Build service account generated when the Cloud Build API is enabled.
cluster:	# 	beta describes how to do an on-cluster build.
HTTP_PROXY:	# 	for kaniko pod.
HTTPS_PROXY:	# 	for kaniko pod.
pullSecretPath:	# 	path to the Google Cloud service account secret key file.
pullSecretName: kaniko-secret	# 	name of the Kubernetes secret for pulling base images and pushing the final image. If given, the secret needs to contain the Google Cloud service account secret key under the key kaniko-secret.
pullSecretMountPath:	# 	path the pull secret will be mounted at within the running container.
namespace:	# 	Kubernetes namespace. Defaults to current namespace in Kubernetes configuration.
timeout:	# 	amount of time (in seconds) that this build is allowed to run. Defaults to 20 minutes (20m).
dockerConfig:	# 	describes how to mount the local Docker configuration into a pod.
path:	# 	path to the docker config.json.
secretName:	# 	Kubernetes secret that contains the config.json Docker configuration. Note that the expected secret type is not 'kubernetes.io/dockerconfigjson' but 'Opaque'.
serviceAccount:	# 	describes the Kubernetes service account to use for the pod. Defaults to 'default'.
tolerations: []	# 	describes the Kubernetes tolerations for the pod.
nodeSelector: {}	# 	describes the Kubernetes node selector for the pod.
annotations: {}	# 	describes the Kubernetes annotations for the pod.
labels: {}	# 	describes the Kubernetes labels for the pod.
runAsUser:	# 	defines the UID to request for running the container. If omitted, no SecurityContext will be specified for the pod and will therefore be inherited from the service account.
resources:	# 	define the resource requirements for the kaniko pod.
requests:	# 	resource requests for the Kaniko pod.
cpu: 2`, `2.0` or `200m	# 	the number cores to be used.
memory: 1Gi` or `1000Mi	# 	the amount of memory to allocate to the pod.
ephemeralStorage: 1Gi` or `1000Mi	# 	the amount of Ephemeral storage to allocate to the pod.
resourceStorage: 1Gi` or `1000Mi	# 	the amount of resource storage to allocate to the pod.
limits:	# 	resource limits for the Kaniko pod.
cpu: 2`, `2.0` or `200m	# 	the number cores to be used.
memory: 1Gi` or `1000Mi	# 	the amount of memory to allocate to the pod.
ephemeralStorage: 1Gi` or `1000Mi	# 	the amount of Ephemeral storage to allocate to the pod.
resourceStorage: 1Gi` or `1000Mi	# 	the amount of resource storage to allocate to the pod.
concurrency: 0	# 	how many artifacts can be built concurrently. 0 means "no-limit".
volumes: []	# 	defines container mounts for ConfigMap and Secret resources.
randomPullSecret: false	# 	adds a random UUID postfix to the default name of the pull secret to facilitate parallel builds, e.g. kaniko-secretdocker-cfgfd154022-c761-416f-8eb3-cf8258450b85.
randomDockerConfigSecret: false	# 	adds a random UUID postfix to the default name of the docker secret to facilitate parallel builds, e.g. docker-cfgfd154022-c761-416f-8eb3-cf8258450b85.
test:	# 	describes how images are tested.
- image: gcr.io/k8s-skaffold/example	# 	artifact on which to run those tests.
context: .	# 	directory containing the test sources.
custom:	# 	the set of custom tests to run after an artifact is built.
- command:	# 	custom command to be executed. If the command exits with a non-zero return code, the test will be considered to have failed.
timeoutSeconds:	# 	sets the wait time for skaffold for the command to complete. If unset or 0, Skaffold will wait until the command completes.
dependencies:	# 	additional test-specific file dependencies; changes to these files will re-run this test.
command:	# 	represents a command that skaffold executes to obtain dependencies. The output of this command must be a valid JSON array.
paths:	# 	locates the file dependencies for the command relative to workspace. Paths should be set to the file dependencies for this command, so that the skaffold file watcher knows when to retest and perform file synchronization.
- "src/test/**"	# 
ignore: []	# 	specifies the paths that should be ignored by skaffold's file watcher. If a file exists in both paths and in ignore, it will be ignored, and will be excluded from both retest and file synchronization. Will only work in conjunction with paths.
structureTests:	# 	the Container Structure Tests to run on that artifact.
- "./test/*"	# 
structureTestsArgs:	# 	additional configuration arguments passed to container-structure-test binary.
- "--driver=tar"	# 
- "--no-color"	# 
- "-q"	# 
manifests:	# 	describes how the original manifests are hydrated, validated and transformed.
rawYaml: []	# 	defines the raw kubernetes resources.
remoteManifests:	# 	Kubernetes manifests in remote clusters.
- manifest:	# 	specifies the Kubernetes manifest in the remote cluster.
kubeContext: minikube	# 	Kubernetes context that Skaffold should deploy to.
kustomize:	# 	defines the paths to be modified with kustomize, along with extra flags to be passed to kustomize.
paths:	# 	path to Kustomization files.
- "."	# 
buildArgs: []	# 	additional args passed to kustomize build.
helm:	# 	defines the helm charts used in the application. NOTE: Defines cherts in this section to render via helm but deployed via kubectl or kpt deployer. To use helm to deploy, please see deploy.helm section.
flags:	# 	additional option flags that are passed on the command line to helm.
global: []	# 	additional flags passed on every command.
install: []	# 	additional flags passed to (helm install).
upgrade: []	# 	additional flags passed to (helm upgrade).
depBuild: []	# 	additional flags passed to (helm dep build).
template: []	# 	additional flags passed to (helm template).
releases:	# 	a list of Helm releases.
- name:	# 	name of the Helm release. It accepts environment variables via the go template syntax.
chartPath:	# 	local path to a packaged Helm chart or an unpacked Helm chart directory.
remoteChart:	# 	refers to a remote Helm chart reference or URL.
valuesFiles: []	# 	paths to the Helm values files.
namespace:	# 	Kubernetes namespace.
version:	# 	version of the chart.
setValues:	# 	key-value pairs. If present, Skaffold will send --set flag to Helm CLI and append all pairs after the flag.
setValueTemplates:	# 	key-value pairs. If present, Skaffold will try to parse the value part of each key-value pair using environment variables in the system, then send --set flag to Helm CLI and append all parsed pairs after the flag.
setFiles: {}	# 	key-value pairs. If present, Skaffold will send --set-file flag to Helm CLI and append all pairs after the flag.
createNamespace:	# 	if true, Skaffold will send --create-namespace flag to Helm CLI. --create-namespace flag is available in Helm since version 3.2. Defaults is false.
wait: false	# 	if true, Skaffold will send --wait flag to Helm CLI.
recreatePods: false	# 	if true, Skaffold will send --recreate-pods flag to Helm CLI when upgrading a new version of a chart in subsequent dev loop deploy.
skipBuildDependencies: false	# 	should build dependencies be skipped. Ignored for remoteChart.
skipTests: false	# 	should ignore helm test during manifests generation.
useHelmSecrets: false	# 	instructs skaffold to use secrets plugin on deployment.
repo:	# 	specifies the helm repository for remote charts. If present, Skaffold will send --repo Helm CLI flag or flags.
upgradeOnChange:	# 	specifies whether to upgrade helm chart on code changes. Default is true when helm chart is local (has chartPath). Default is false when helm chart is remote (has remoteChart).
overrides:	# 	key-value pairs. If present, Skaffold will build a Helm values file that overrides the original and use it to call Helm CLI (--f flag).
packaged:	# 	parameters for packaging helm chart (helm package).
version:	# 	sets the version on the chart to this semver version.
appVersion:	# 	sets the appVersion on the chart to this version.
dependsOn: []	# 	a list of Helm release names that this deploy depends on.
kpt: []	# 	defines the kpt resources in the application.
hooks:	# 	describes a set of lifecycle hooks that are executed before and after every render.
before:	# 	describes the list of lifecycle hooks to execute before each render step. Container hooks will only run if the container exists from a previous deployment step (for instance the successive iterations of a dev-loop during skaffold dev).
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
after:	# 	describes the list of lifecycle hooks to execute after each render step.
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
withChange: false	# 	preserves changes made on the manifests by the hook.
transform:	# 	defines a set of transformation operations to run in series.
validate:	# 	defines a set of validator operations to run in series.
output:	# 	path to the hydrated directory.
deploy:	# 	describes how the manifests are deployed.
docker:	# 	alpha uses the docker CLI to create application containers in Docker.
useCompose: false	# 	tells skaffold whether or not to deploy using docker-compose.
images: []	# 	container images to run in Docker.
helm:	# 	beta uses the helm CLI to apply the charts to the cluster.
concurrency: 1	# 	how many packages can be installed concurrently. 0 means "no-limit".
releases:	# 	a list of Helm releases.
- name:	# 	name of the Helm release. It accepts environment variables via the go template syntax.
chartPath:	# 	local path to a packaged Helm chart or an unpacked Helm chart directory.
remoteChart:	# 	refers to a remote Helm chart reference or URL.
valuesFiles: []	# 	paths to the Helm values files.
namespace:	# 	Kubernetes namespace.
version:	# 	version of the chart.
setValues:	# 	key-value pairs. If present, Skaffold will send --set flag to Helm CLI and append all pairs after the flag.
setValueTemplates:	# 	key-value pairs. If present, Skaffold will try to parse the value part of each key-value pair using environment variables in the system, then send --set flag to Helm CLI and append all parsed pairs after the flag.
setFiles: {}	# 	key-value pairs. If present, Skaffold will send --set-file flag to Helm CLI and append all pairs after the flag.
createNamespace:	# 	if true, Skaffold will send --create-namespace flag to Helm CLI. --create-namespace flag is available in Helm since version 3.2. Defaults is false.
wait: false	# 	if true, Skaffold will send --wait flag to Helm CLI.
recreatePods: false	# 	if true, Skaffold will send --recreate-pods flag to Helm CLI when upgrading a new version of a chart in subsequent dev loop deploy.
skipBuildDependencies: false	# 	should build dependencies be skipped. Ignored for remoteChart.
skipTests: false	# 	should ignore helm test during manifests generation.
useHelmSecrets: false	# 	instructs skaffold to use secrets plugin on deployment.
repo:	# 	specifies the helm repository for remote charts. If present, Skaffold will send --repo Helm CLI flag or flags.
upgradeOnChange:	# 	specifies whether to upgrade helm chart on code changes. Default is true when helm chart is local (has chartPath). Default is false when helm chart is remote (has remoteChart).
overrides:	# 	key-value pairs. If present, Skaffold will build a Helm values file that overrides the original and use it to call Helm CLI (--f flag).
packaged:	# 	parameters for packaging helm chart (helm package).
version:	# 	sets the version on the chart to this semver version.
appVersion:	# 	sets the appVersion on the chart to this version.
dependsOn: []	# 	a list of Helm release names that this deploy depends on.
flags:	# 	additional option flags that are passed on the command line to helm.
global: []	# 	additional flags passed on every command.
install: []	# 	additional flags passed to (helm install).
upgrade: []	# 	additional flags passed to (helm upgrade).
depBuild: []	# 	additional flags passed to (helm dep build).
template: []	# 	additional flags passed to (helm template).
hooks:	# 	describes a set of lifecycle hooks that are executed before and after every deploy.
before:	# 	describes the list of lifecycle hooks to execute before each deployer step. Container hooks will only run if the container exists from a previous deployment step (for instance the successive iterations of a dev-loop during skaffold dev).
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
podName:	# 	name of the pod to execute the command in.
containerName:	# 	name of the container to execute the command in.
after:	# 	describes the list of lifecycle hooks to execute after each deployer step.
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
podName:	# 	name of the pod to execute the command in.
containerName:	# 	name of the container to execute the command in.
kpt:	# 	alpha uses the kpt CLI to manage and deploy manifests.
dir:	# 	equivalent to the dir in kpt live apply <dir>. If not provided, skaffold deploys from the default hydrated path <WORKDIR>/.kpt-pipeline.
applyFlags: []	# 	additional flags passed to kpt live apply.
flags: []	# 	kpt global flags.
name:	# 	alpha inventory object name.
inventoryID:	# 	alpha inventory ID which annotates the resources being lively applied by kpt.
namespace:	# 	alpha sets the inventory namespace.
force: false	# 	used in kpt live init, which forces the inventory values to be updated, even if they are already set.
defaultNamespace:	# 	default namespace passed to kpt on deployment if no other override is given.
kubectl:	# 	beta uses a client side kubectl apply to deploy manifests. You'll need a kubectl CLI version installed that's compatible with your cluster.
flags:	# 	additional flags passed to kubectl.
global: []	# 	additional flags passed on every command.
apply: []	# 	additional flags passed on creations (kubectl apply).
delete: []	# 	additional flags passed on deletions (kubectl delete).
disableValidation: false	# 	passes the --validate=false flag to supported kubectl commands when enabled.
remoteManifests: []	# 	Kubernetes manifests in remote clusters.
defaultNamespace:	# 	default namespace passed to kubectl on deployment if no other override is given.
hooks:	# 	describes a set of lifecycle hooks that are executed before and after every deploy.
before:	# 	describes the list of lifecycle hooks to execute before each deployer step. Container hooks will only run if the container exists from a previous deployment step (for instance the successive iterations of a dev-loop during skaffold dev).
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
podName:	# 	name of the pod to execute the command in.
containerName:	# 	name of the container to execute the command in.
after:	# 	describes the list of lifecycle hooks to execute after each deployer step.
host:	# 	describes a single lifecycle hook to run on the host machine.
command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
container:	# 	describes a single lifecycle hook to run on a container.
command: []	# 	command to execute.
podName:	# 	name of the pod to execute the command in.
containerName:	# 	name of the container to execute the command in.
cloudrun:	# 	alpha deploys to Google Cloud Run using the Cloud Run v1 API.
projectid:	# 	the GCP Project to use for Cloud Run. If specified, all Services will be deployed to this project. If not specified, each Service will be deployed to the project specified in metadata.namespace of the Cloud Run manifest.
region:	# 	GCP location to use for the Cloud Run Deploy. Must be one of the regions listed in https://cloud.google.com/run/docs/locations.
hooks:	# 	describes a set of lifecycle host hooks that are executed before and after the Cloud Run deployer.
before:	# 	describes the list of lifecycle hooks to execute before the Cloud Run deployer.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
after:	# 	describes the list of lifecycle hooks to execute after the Cloud Run deployer.
- command: []	# 	command to execute.
os: []	# 	an optional slice of operating system names. If the host machine OS is different, then it skips execution.
dir:	# 	specifies the working directory of the command. If empty, the command runs in the calling process's current directory.
statusCheck:	# 	beta enables waiting for deployments to stabilize.
statusCheckDeadlineSeconds:	# 	beta deadline for deployments to stabilize in seconds.
tolerateFailuresUntilDeadline: false	# 	configures the Skaffold "status-check" to tolerate failures (flapping deployments, etc.) until the statusCheckDeadlineSeconds duration or k8s object timeouts such as progressDeadlineSeconds, etc.
kubeContext: minikube	# 	Kubernetes context that Skaffold should deploy to.
logs:	# 	configures how container logs are printed as a result of a deployment.
prefix: auto	# 	defines the prefix shown on each log line. Valid values are container: prefix logs lines with the name of the container. podAndContainer: prefix logs lines with the names of the pod and of the container. auto: same as podAndContainer except that the pod name is skipped if it's the same as the container name. none: don't add a prefix.
jsonParse:	# 	defines the rules for parsing/outputting json logs.
fields: []	# 	specifies which top level fields should be printed.
portForward:	# 	describes user defined resources to port-forward.
- resourceType:	# 	resource type that should be port forwarded. Acceptable resource types include kubernetes types: Service, Pod and Controller resource type that has a pod spec: ReplicaSet, ReplicationController, Deployment, StatefulSet, DaemonSet, Job, CronJob. Standalone Container is also valid for Docker deployments.
resourceName:	# 	name of the Kubernetes resource or local container to port forward.
namespace:	# 	namespace of the resource to port forward. Does not apply to local containers.
port:	# 	resource port that will be forwarded.
address:	# 	local address to bind to. Defaults to the loopback address 127.0.0.1.
localPort:	# 	local port to forward to. If the port is unavailable, Skaffold will choose a random open port to forward to. Optional.
resourceSelector:	# 	describes user defined filters describing how skaffold should treat objects/fields during rendering.
allow:	# 	configures an allowlist for transforming manifests.
- groupKind:	# 	compact format of a resource type.
image: []	# 	an optional slice of JSON-path-like paths of where to rewrite images.
labels: []	# 	an optional slice of JSON-path-like paths of where to add a labels block if missing.
podSpec: []	# 	an optional slice of JSON-path-like paths of where pod spec properties can be overwritten.
deny:	# 	configures an allowlist for transforming manifests.
- groupKind:	# 	compact format of a resource type.
image: []	# 	an optional slice of JSON-path-like paths of where to rewrite images.
labels: []	# 	an optional slice of JSON-path-like paths of where to add a labels block if missing.
podSpec: []	# 	an optional slice of JSON-path-like paths of where pod spec properties can be overwritten.
verify:	# 	describes how images are verified (via verification tests).
- name:	# 	name descriptor for the verify test.
timeout:	# 	indicates the max time (in seconds) that the verify test is allowed to run.
container:	# 	container information for the verify test.
name:	# 	name of the container.
image:	# 	container image name.
command: []	# 	entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided.
args: []	# 	arguments to the entrypoint. The container image's CMD is used if this is not provided.
env:	# 	list of environment variables to set in the container.
- name:	# 	of the environment variable. Must be a C_IDENTIFIER.
value:	# 	of the environment variable.
executionMode:	# 	execution mode used to execute the verify test case.
local:	# 	uses the docker CLI to create verify test case containers on the host machine in Docker. This is the default execution mode.
useLocalImages: false	# 	if true, will first check if the containers images exist locally before triggering a pull. Defaults to false.
kubernetesCluster:	# 	uses the kubectl CLI to create veriy test case container in a kubernetes cluster.
overrides:	# 	inline JSON override to use for the generated kubernetes Job. If this is non-empty, it is used to override the generated object. Similar to the --overrides kubectl flag.
jobManifestPath:	# 	path to the kubernetes Job manifest to use for the verify test This manifest will be deployed into the cluster with the Container information replaced by the information in the Container field.
customActions:	# 	describes a list of user defined actions that can be triggered with skaffold exec.
- name:	# 	unique name assigned to the action.
failFast:	# 	indicates if the action should be executed with a fail-fast strategy or not (fail-safe). Defaults to true.
timeout:	# 	indicates the max time (in seconds) that the action is allowed to run.
executionMode:	# 	describes the execution mode used to execute the custom action.
local:	# 	uses the docker CLI to create verify test case containers on the host machine in Docker. This is the default execution mode.
useLocalImages: false	# 	if true, will first check if the containers images exist locally before triggering a pull. Defaults to false.
kubernetesCluster:	# 	uses the kubectl CLI to create veriy test case container in a kubernetes cluster.
overrides:	# 	inline JSON override to use for the generated kubernetes Job. If this is non-empty, it is used to override the generated object. Similar to the --overrides kubectl flag.
jobManifestPath:	# 	path to the kubernetes Job manifest to use for the verify test This manifest will be deployed into the cluster with the Container information replaced by the information in the Container field.
containers:	# 	containers list to execute as part of the custom action.
- name:	# 	name of the container.
image:	# 	container image name.
command: []	# 	entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided.
args: []	# 	arguments to the entrypoint. The container image's CMD is used if this is not provided.
env:	# 	list of environment variables to set in the container.
- name:	# 	of the environment variable. Must be a C_IDENTIFIER.
value:	# 	of the environment variable.
profiles:	# 	beta can override be used to build, test or deploy configuration.
- name: profile-prod	# 	a unique profile name.
activation:	# 	criteria by which a profile can be auto-activated. The profile is auto-activated if any one of the activations are triggered. An activation is triggered if all of the criteria (env, kubeContext, command) are triggered.
- env: ENV=production	# 	a key=pattern pair. The profile is auto-activated if an Environment Variable key matches the pattern. If the pattern starts with !, activation happens if the remaining pattern is not matched. The pattern matches if the Environment Variable value is exactly pattern, or the regex pattern is found in it. An empty pattern (e.g. env: "key=") always only matches if the Environment Variable is undefined or empty.
kubeContext: minikube	# 	a Kubernetes context for which the profile is auto-activated.
command: dev	# 	a Skaffold command for which the profile is auto-activated.
requiresAllActivations: false	# 	activation strategy of the profile. When true, the profile is auto-activated only when all of its activations are triggered. When false, the profile is auto-activated when any one of its activations is triggered.
patches:	# 	patches applied to the configuration. Patches use the JSON patch notation.
- op: replace	# 	operation carried by the patch: add, remove, replace, move, copy or test.
path: /build/artifacts/0/docker/dockerfile	# 	position in the yaml where the operation takes place. For example, this targets the dockerfile of the first artifact built.
from:	# 	source position in the yaml, used for copy or move operations.
value:	# 	value to apply. Can be any portion of yaml.
build: {}	# 	describes how images are built.
test: {}	# 	describes how images are tested.
manifests: {}	# 	describes how the original manifests are hydrated, validated and transformed.
deploy: {}	# 	describes how the manifests are deployed.
portForward: {}	# 	describes user defined resources to port-forward.
resourceSelector: {}	# 	describes user defined filters describing how skaffold should treat objects/fields during rendering.
verify: {}	# 	describes how images are verified (via verification tests).
customActions: {}	# 	describes a list of user defined actions that can be triggered with skaffold exec.
YAML anchors

Anchors can be defined by having top-level keys starting with a dot, e.g. .common_stuff: &alias_name. You can then reuse the value using *alias_name.

Organizing multiple configurations

Multiple configurations can define dependencies on each other to construct an arbitrarily nested tree of project component dependencies. Management of multiple configurations can be simplified by grouping them together in the same file (separated by --- in YAML).

Last modified November 13, 2025: chore: Skaffold 2.17 release (#9912) (561ce51e)
   
© 2025 Skaffold Authors All Rights Reserved
Privacy Policy
