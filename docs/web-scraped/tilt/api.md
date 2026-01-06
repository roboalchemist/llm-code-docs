# Tilt Documentation
# Source: https://docs.tilt.dev/api.html
# Path: api.html

  * [ Getting Started ](/index.html) [ Getting Started ](/docs_nav_gettingstarted.html)
  * [ Guides ](/tiltfile_authoring.html) [ Guides ](/docs_nav_guides.html)
  * [ Tiltfile & CLI ](/api.html) [ Tiltfile & CLI ](/docs_nav_reference.html)
  * [ Tilt API ](https://api.tilt.dev) [ Tilt API ](https://api.tilt.dev)

Tiltfile API Reference

    

  * [ Overview ](/api.html)
  * Functions 
    
  * [ Overview ](/api.html#functions)
  * [ allow_k8s_contexts ](/api.html#api.allow_k8s_contexts)
  * [ analytics_settings ](/api.html#api.analytics_settings)
  * [ blob ](/api.html#api.blob)
  * [ ci_settings ](/api.html#api.ci_settings)
  * [ custom_build ](/api.html#api.custom_build)
  * [ dc_resource ](/api.html#api.dc_resource)
  * [ decode_json ](/api.html#api.decode_json)
  * [ decode_yaml ](/api.html#api.decode_yaml)
  * [ decode_yaml_stream ](/api.html#api.decode_yaml_stream)
  * [ default_registry ](/api.html#api.default_registry)
  * [ disable_snapshots ](/api.html#api.disable_snapshots)
  * [ docker_build ](/api.html#api.docker_build)
  * [ docker_compose ](/api.html#api.docker_compose)
  * [ docker_prune_settings ](/api.html#api.docker_prune_settings)
  * [ enable_feature ](/api.html#api.enable_feature)
  * [ encode_json ](/api.html#api.encode_json)
  * [ encode_yaml ](/api.html#api.encode_yaml)
  * [ encode_yaml_stream ](/api.html#api.encode_yaml_stream)
  * [ exec_action ](/api.html#api.exec_action)
  * [ exit ](/api.html#api.exit)
  * [ fail ](/api.html#api.fail)
  * [ fall_back_on ](/api.html#api.fall_back_on)
  * [ filter_yaml ](/api.html#api.filter_yaml)
  * [ helm ](/api.html#api.helm)
  * [ http_get_action ](/api.html#api.http_get_action)
  * [ include ](/api.html#api.include)
  * [ k8s_context ](/api.html#api.k8s_context)
  * [ k8s_custom_deploy ](/api.html#api.k8s_custom_deploy)
  * [ k8s_kind ](/api.html#api.k8s_kind)
  * [ k8s_namespace ](/api.html#api.k8s_namespace)
  * [ k8s_resource ](/api.html#api.k8s_resource)
  * [ k8s_yaml ](/api.html#api.k8s_yaml)
  * [ kustomize ](/api.html#api.kustomize)
  * [ link ](/api.html#api.link)
  * [ listdir ](/api.html#api.listdir)
  * [ load ](/api.html#api.load)
  * [ load_dynamic ](/api.html#api.load_dynamic)
  * [ local ](/api.html#api.local)
  * [ local_resource ](/api.html#api.local_resource)
  * [ port_forward ](/api.html#api.port_forward)
  * [ probe ](/api.html#api.probe)
  * [ read_file ](/api.html#api.read_file)
  * [ read_json ](/api.html#api.read_json)
  * [ read_yaml ](/api.html#api.read_yaml)
  * [ read_yaml_stream ](/api.html#api.read_yaml_stream)
  * [ restart_container ](/api.html#api.restart_container)
  * [ run ](/api.html#api.run)
  * [ secret_settings ](/api.html#api.secret_settings)
  * [ set_team ](/api.html#api.set_team)
  * [ struct ](/api.html#api.struct)
  * [ sync ](/api.html#api.sync)
  * [ tcp_socket_action ](/api.html#api.tcp_socket_action)
  * [ trigger_mode ](/api.html#api.trigger_mode)
  * [ update_settings ](/api.html#api.update_settings)
  * [ version_settings ](/api.html#api.version_settings)
  * [ warn ](/api.html#api.warn)
  * [ watch_file ](/api.html#api.watch_file)
  * [ watch_settings ](/api.html#api.watch_settings)
  * [ workload_to_resource_function ](/api.html#api.workload_to_resource_function)
  * [ os.getcwd ](/api.html#api.os.getcwd)
  * [ os.getenv ](/api.html#api.os.getenv)
  * [ os.putenv ](/api.html#api.os.putenv)
  * [ os.unsetenv ](/api.html#api.os.unsetenv)
  * [ os.path.abspath ](/api.html#api.os.path.abspath)
  * [ os.path.basename ](/api.html#api.os.path.basename)
  * [ os.path.dirname ](/api.html#api.os.path.dirname)
  * [ os.path.exists ](/api.html#api.os.path.exists)
  * [ os.path.join ](/api.html#api.os.path.join)
  * [ os.path.realpath ](/api.html#api.os.path.realpath)
  * [ os.path.relpath ](/api.html#api.os.path.relpath)
  * [ config.clear_enabled_resources ](/api.html#api.config.clear_enabled_resources)
  * [ config.define_bool ](/api.html#api.config.define_bool)
  * [ config.define_string ](/api.html#api.config.define_string)
  * [ config.define_string_list ](/api.html#api.config.define_string_list)
  * [ config.parse ](/api.html#api.config.parse)
  * [ config.set_enabled_resources ](/api.html#api.config.set_enabled_resources)
  * [ shlex.quote ](/api.html#api.shlex.quote)
  * [ v1alpha1.cmd ](/api.html#api.v1alpha1.cmd)
  * [ v1alpha1.config_map ](/api.html#api.v1alpha1.config_map)
  * [ v1alpha1.config_map_disable_source ](/api.html#api.v1alpha1.config_map_disable_source)
  * [ v1alpha1.disable_source ](/api.html#api.v1alpha1.disable_source)
  * [ v1alpha1.exec_action ](/api.html#api.v1alpha1.exec_action)
  * [ v1alpha1.extension ](/api.html#api.v1alpha1.extension)
  * [ v1alpha1.extension_repo ](/api.html#api.v1alpha1.extension_repo)
  * [ v1alpha1.file_watch ](/api.html#api.v1alpha1.file_watch)
  * [ v1alpha1.forward ](/api.html#api.v1alpha1.forward)
  * [ v1alpha1.handler ](/api.html#api.v1alpha1.handler)
  * [ v1alpha1.http_get_action ](/api.html#api.v1alpha1.http_get_action)
  * [ v1alpha1.http_header ](/api.html#api.v1alpha1.http_header)
  * [ v1alpha1.ignore_def ](/api.html#api.v1alpha1.ignore_def)
  * [ v1alpha1.kubernetes_apply ](/api.html#api.v1alpha1.kubernetes_apply)
  * [ v1alpha1.kubernetes_apply_cmd ](/api.html#api.v1alpha1.kubernetes_apply_cmd)
  * [ v1alpha1.kubernetes_discovery ](/api.html#api.v1alpha1.kubernetes_discovery)
  * [ v1alpha1.kubernetes_discovery_template_spec ](/api.html#api.v1alpha1.kubernetes_discovery_template_spec)
  * [ v1alpha1.kubernetes_image_locator ](/api.html#api.v1alpha1.kubernetes_image_locator)
  * [ v1alpha1.kubernetes_image_object_descriptor ](/api.html#api.v1alpha1.kubernetes_image_object_descriptor)
  * [ v1alpha1.kubernetes_watch_ref ](/api.html#api.v1alpha1.kubernetes_watch_ref)
  * [ v1alpha1.label_selector ](/api.html#api.v1alpha1.label_selector)
  * [ v1alpha1.label_selector_requirement ](/api.html#api.v1alpha1.label_selector_requirement)
  * [ v1alpha1.object_selector ](/api.html#api.v1alpha1.object_selector)
  * [ v1alpha1.pod_log_stream_template_spec ](/api.html#api.v1alpha1.pod_log_stream_template_spec)
  * [ v1alpha1.port_forward_template_spec ](/api.html#api.v1alpha1.port_forward_template_spec)
  * [ v1alpha1.probe ](/api.html#api.v1alpha1.probe)
  * [ v1alpha1.restart_on_spec ](/api.html#api.v1alpha1.restart_on_spec)
  * [ v1alpha1.start_on_spec ](/api.html#api.v1alpha1.start_on_spec)
  * [ v1alpha1.tcp_socket_action ](/api.html#api.v1alpha1.tcp_socket_action)
  * [ v1alpha1.ui_bool_input_spec ](/api.html#api.v1alpha1.ui_bool_input_spec)
  * [ v1alpha1.ui_button ](/api.html#api.v1alpha1.ui_button)
  * [ v1alpha1.ui_component_location ](/api.html#api.v1alpha1.ui_component_location)
  * [ v1alpha1.ui_hidden_input_spec ](/api.html#api.v1alpha1.ui_hidden_input_spec)
  * [ v1alpha1.ui_input_spec ](/api.html#api.v1alpha1.ui_input_spec)
  * [ v1alpha1.ui_text_input_spec ](/api.html#api.v1alpha1.ui_text_input_spec)
  * Types 
    
  * [ Overview ](/api.html#types)
  * [ Blob ](/api.html#api.Blob)
  * [ ExecAction ](/api.html#api.ExecAction)
  * [ HTTPGetAction ](/api.html#api.HTTPGetAction)
  * [ K8sObjectID ](/api.html#api.K8sObjectID)
  * [ Link ](/api.html#api.Link)
  * [ LiveUpdateStep ](/api.html#api.LiveUpdateStep)
  * [ PortForward ](/api.html#api.PortForward)
  * [ Probe ](/api.html#api.Probe)
  * [ TCPSocketAction ](/api.html#api.TCPSocketAction)
  * [ TriggerMode ](/api.html#api.TriggerMode)
  * [ v1alpha1.ConfigMapDisableSource ](/api.html#api.v1alpha1.ConfigMapDisableSource)
  * [ v1alpha1.DisableSource ](/api.html#api.v1alpha1.DisableSource)
  * [ v1alpha1.ExecAction ](/api.html#api.v1alpha1.ExecAction)
  * [ v1alpha1.Forward ](/api.html#api.v1alpha1.Forward)
  * [ v1alpha1.HTTPGetAction ](/api.html#api.v1alpha1.HTTPGetAction)
  * [ v1alpha1.HTTPHeader ](/api.html#api.v1alpha1.HTTPHeader)
  * [ v1alpha1.Handler ](/api.html#api.v1alpha1.Handler)
  * [ v1alpha1.IgnoreDef ](/api.html#api.v1alpha1.IgnoreDef)
  * [ v1alpha1.KubernetesImageLocator ](/api.html#api.v1alpha1.KubernetesImageLocator)
  * [ v1alpha1.KubernetesWatchRef ](/api.html#api.v1alpha1.KubernetesWatchRef)
  * [ v1alpha1.ObjectSelector ](/api.html#api.v1alpha1.ObjectSelector)
  * [ v1alpha1.PodLogStreamTemplateSpec ](/api.html#api.v1alpha1.PodLogStreamTemplateSpec)
  * [ v1alpha1.PortForwardTemplateSpec ](/api.html#api.v1alpha1.PortForwardTemplateSpec)
  * [ v1alpha1.Probe ](/api.html#api.v1alpha1.Probe)
  * [ v1alpha1.RestartOnSpec ](/api.html#api.v1alpha1.RestartOnSpec)
  * [ v1alpha1.StartOnSpec ](/api.html#api.v1alpha1.StartOnSpec)
  * [ v1alpha1.TCPSocketAction ](/api.html#api.v1alpha1.TCPSocketAction)
  * [ v1alpha1.UIBoolInputSpec ](/api.html#api.v1alpha1.UIBoolInputSpec)
  * [ v1alpha1.UIComponentLocation ](/api.html#api.v1alpha1.UIComponentLocation)
  * [ v1alpha1.UIHiddenInputSpec ](/api.html#api.v1alpha1.UIHiddenInputSpec)
  * [ v1alpha1.UIInputSpec ](/api.html#api.v1alpha1.UIInputSpec)
  * [ v1alpha1.UITextInputSpec ](/api.html#api.v1alpha1.UITextInputSpec)
  * Data 
    
  * [ Overview ](/api.html#data)
  * [ __file__ ](/api.html#api.__file__)
  * [ os.environ ](/api.html#api.os.environ)
  * [ os.name ](/api.html#api.os.name)
  * [ config.main_dir ](/api.html#api.config.main_dir)
  * [ config.main_path ](/api.html#api.config.main_path)
  * [ config.tilt_subcommand ](/api.html#api.config.tilt_subcommand)
  * [ sys.argv ](/api.html#api.sys.argv)
  * [ sys.executable ](/api.html#api.sys.executable)
  * [ Extensions ](/api.html#extensions)

Tilt CLI Reference

    

  * [ tilt ](/cli/tilt.html)
  * [ tilt alpha ](/cli/tilt_alpha.html)
  * [ tilt analytics ](/cli/tilt_analytics.html)
  * [ tilt api-resources ](/cli/tilt_api-resources.html)
  * [ tilt apply ](/cli/tilt_apply.html)
  * [ tilt args ](/cli/tilt_args.html)
  * [ tilt ci ](/cli/tilt_ci.html)
  * [ tilt completion ](/cli/tilt_completion.html)
  * [ tilt create ](/cli/tilt_create.html)
  * [ tilt delete ](/cli/tilt_delete.html)
  * [ tilt demo ](/cli/tilt_demo.html)
  * [ tilt describe ](/cli/tilt_describe.html)
  * [ tilt disable ](/cli/tilt_disable.html)
  * [ tilt docker ](/cli/tilt_docker.html)
  * [ tilt docker-prune ](/cli/tilt_docker-prune.html)
  * [ tilt doctor ](/cli/tilt_doctor.html)
  * [ tilt down ](/cli/tilt_down.html)
  * [ tilt dump ](/cli/tilt_dump.html)
  * [ tilt edit ](/cli/tilt_edit.html)
  * [ tilt enable ](/cli/tilt_enable.html)
  * [ tilt explain ](/cli/tilt_explain.html)
  * [ tilt get ](/cli/tilt_get.html)
  * [ tilt logs ](/cli/tilt_logs.html)
  * [ tilt lsp ](/cli/tilt_lsp.html)
  * [ tilt patch ](/cli/tilt_patch.html)
  * [ tilt snapshot ](/cli/tilt_snapshot.html)
  * [ tilt trigger ](/cli/tilt_trigger.html)
  * [ tilt up ](/cli/tilt_up.html)
  * [ tilt verify-install ](/cli/tilt_verify-install.html)
  * [ tilt version ](/cli/tilt_version.html)
  * [ tilt wait ](/cli/tilt_wait.html)

#  Tiltfile API Reference

Tiltfiles are written in _Starlark_ , a dialect of Python. For more
information on Starlarkâs built-ins, [see the **Starlark
Spec**](https://github.com/bazelbuild/starlark/blob/master/spec.md). The rest
of this page details Tiltfile-specific functionality.

> ð **Looking for Examples?**  
>  Check out our [Tiltfile Snippets](/snippets.html)!

## Functions

  * allow_k8s_contexts
  * analytics_settings
  * blob
  * ci_settings
  * custom_build
  * dc_resource
  * decode_json
  * decode_yaml
  * decode_yaml_stream
  * default_registry
  * disable_snapshots
  * docker_build
  * docker_compose
  * docker_prune_settings
  * enable_feature
  * encode_json
  * encode_yaml
  * encode_yaml_stream
  * exec_action
  * exit
  * fail
  * fall_back_on
  * filter_yaml
  * helm
  * http_get_action
  * include
  * k8s_context
  * k8s_custom_deploy
  * k8s_kind
  * k8s_namespace
  * k8s_resource
  * k8s_yaml
  * kustomize
  * link
  * listdir
  * load
  * load_dynamic
  * local
  * local_resource
  * port_forward
  * probe
  * read_file
  * read_json
  * read_yaml
  * read_yaml_stream
  * restart_container
  * run
  * secret_settings
  * set_team
  * struct
  * sync
  * tcp_socket_action
  * trigger_mode
  * update_settings
  * version_settings
  * warn
  * watch_file
  * watch_settings
  * workload_to_resource_function
  * os.getcwd
  * os.getenv
  * os.putenv
  * os.unsetenv
  * os.path.abspath
  * os.path.basename
  * os.path.dirname
  * os.path.exists
  * os.path.join
  * os.path.realpath
  * os.path.relpath
  * config.clear_enabled_resources
  * config.define_bool
  * config.define_string
  * config.define_string_list
  * config.parse
  * config.set_enabled_resources
  * shlex.quote
  * v1alpha1.cmd
  * v1alpha1.config_map
  * v1alpha1.config_map_disable_source
  * v1alpha1.disable_source
  * v1alpha1.exec_action
  * v1alpha1.extension
  * v1alpha1.extension_repo
  * v1alpha1.file_watch
  * v1alpha1.forward
  * v1alpha1.handler
  * v1alpha1.http_get_action
  * v1alpha1.http_header
  * v1alpha1.ignore_def
  * v1alpha1.kubernetes_apply
  * v1alpha1.kubernetes_apply_cmd
  * v1alpha1.kubernetes_discovery
  * v1alpha1.kubernetes_discovery_template_spec
  * v1alpha1.kubernetes_image_locator
  * v1alpha1.kubernetes_image_object_descriptor
  * v1alpha1.kubernetes_watch_ref
  * v1alpha1.label_selector
  * v1alpha1.label_selector_requirement
  * v1alpha1.object_selector
  * v1alpha1.pod_log_stream_template_spec
  * v1alpha1.port_forward_template_spec
  * v1alpha1.probe
  * v1alpha1.restart_on_spec
  * v1alpha1.start_on_spec
  * v1alpha1.tcp_socket_action
  * v1alpha1.ui_bool_input_spec
  * v1alpha1.ui_button
  * v1alpha1.ui_component_location
  * v1alpha1.ui_hidden_input_spec
  * v1alpha1.ui_input_spec
  * v1alpha1.ui_text_input_spec

* * *

allow_k8s_contexts  (  _ contexts  _ )  ï

    

Specifies that Tilt is allowed to run against the specified k8s context names.

To help reduce the chances you accidentally use Tilt to deploy to your
production cluster, Tilt will only push to clusters that have been allowed for
local development.

By default, Tilt automatically allows Minikube, Docker for Desktop, Microk8s,
Red Hat CodeReady Containers, Kind, K3D, and Krucible.

To add your development cluster to the allow list, add a line in your
Tiltfile:

    
    
    allow_k8s_contexts('context-name')
    

where âcontext-nameâ is the name returned by  kubectl config current-
context  .

If your team connects to many remote dev clusters, a common approach is to
disable the check entirely and add your own validation:

    
    
    allow_k8s_contexts(k8s_context())
    local('./validate-dev-cluster.sh')
    

For more on which cluster context is right for you, see [ Choosing a Local Dev
Cluster ](choosing_clusters.html) .

Parameters

    

**contexts** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â a string
or list of strings, specifying one or more k8s context names that Tilt is
allowed to run in. This list is in addition to the default of all known-local
clusters.

Example

    
    
    allow_k8s_contexts('my-staging-cluster')
    
    allow_k8s_contexts([
      'my-staging-cluster',
      'gke_my-project-name_my-dev-cluster-name'
    ])
    
    allow_k8s_contexts(k8s_context()) # disable check
    

Return type

    

` None  `

analytics_settings  (  _ enable  _ )  ï

    

Overrides Tilt telemetry.

By default, Tilt does not send telemetry. After you successfully run a
Tiltfile, the Tilt web UI will nudge you to opt in or opt out of telemetry.

The Tiltfile can override these telemetry settings, for teams that always want
telemetry enabled or disabled.

Parameters

    

**enable** ( ` bool  ` ) â if true, telemetry will be turned on. If false,
telemetry will be turned off.

Return type

    

` None  `

blob  (  _ contents  _ )  ï

    

Creates a Blob object that wraps the provided string. Useful for passing
strings in to functions that expect a  Blob  , e.g. ` k8s_yaml  ` .

Return type

    

` Blob  `

ci_settings  (  _ k8s_grace_period  =  '' _ , _ timeout  =  '30m' _ , _
readiness_timeout  =  '5m' _ )  ï

    

Configures âtilt ciâ mode.

Parameters

    

  * **k8s_grace_period** ( ` str  ` ) â Grace period given for Kubernetes resources to recover after they start failing. A duration string. 

  * **timeout** ( ` str  ` ) â Timeout for the whole CI pipeline. A duration string. Defaults to â30mâ. 

  * **readiness_timeout** ( ` str  ` ) â Timeout for a resource to become ready before the CI pipeline fails. Measured from the time the resource is started. Defaults to â5mâ. 

Return type

    

` None  `

custom_build  (  _ ref  _ , _ command  _ , _ deps  _ , _ tag  =  '' _ , _
disable_push  =  False  _ , _ skips_local_docker  =  False  _ , _ live_update
=  []  _ , _ match_in_env_vars  =  False  _ , _ ignore  =  []  _ , _
entrypoint  =  []  _ , _ command_bat_val  =  '' _ , _ outputs_image_ref_to  =
'' _ , _ command_bat  =  '' _ , _ image_deps  =  []  _ , _ env  =  {}  _ , _
dir  =  '' _ )  ï

    

Provide a custom command that will build an image.

Example

    
    
    custom_build(
      'gcr.io/my-project/frontend-server',
      'docker build -t $EXPECTED_REF .',
      ['.'],
    )
    

Please read the [ Custom Image Builders Guide ](custom_build.html) on how to
use this function.

All custom build scripts build an image and put it somewhere. But there are
several different patterns for where they put the image, how they compute a
digest of the contents, and how they push the image to the cluster. `
custom_build  ` has many options to support different combinations of each
mode. The guide has some examples of common combinations.

Parameters

    

  * **ref** ( ` str  ` ) â name for this image (e.g. âmyproj/backendâ or âmyregistry/myproj/backendâ). If this image will be used in a k8s resource(s), this ref must match the ` spec.container.image  ` param for that resource(s). 

  * **command** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â a command that, when run in the shell, builds an image puts it in the registry as ` ref  ` . In the default mode, must produce an image named ` $EXPECTED_REF  ` . If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **deps** ( ` List  ` [ ` str  ` ]) â a list of files or directories to be added as dependencies to this image. Tilt will watch those files and will rebuild the image when they change. Only accepts real paths, not file globs. 

  * **tag** ( ` str  ` ) â Some tools canât change the image tag at runtime. They need a pre-specified tag. Tilt will set ` $EXPECTED_REF  =  image_name:tag  ` , then re-tag it with its own tag before pushing to your cluster. 

  * **disable_push** ( ` bool  ` ) â whether Tilt should push the image in to the registry that the Kubernetes cluster has access to. Set this to true if your command handles pushing as well. 

  * **skips_local_docker** ( ` bool  ` ) â Whether your build command writes the image to your local Docker image store. Set this to true if youâre using a cloud-based builder or independent image builder like ` buildah  ` . 

  * **live_update** ( ` List  ` [  ` LiveUpdateStep  ` ]) â 

set of steps for updating a running container (see [ Live Update documentation
](live_update_reference.html) ).

  * **match_in_env_vars** ( ` bool  ` ) â specifies that k8s objects can reference this image in their environment variables, and Tilt will handle those variables the same as it usually handles a k8s container specâs ` image  ` s. 

  * **ignore** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â set of file patterns that will be ignored. Ignored files will not trigger builds and will not be included in images. Follows the [ dockerignore syntax ](https://docs.docker.com/engine/reference/builder/#dockerignore-file) . Patterns/filepaths will be evaluated relative to each ` dep  ` (e.g. if you specify ` deps=['dep1',  'dep2']  ` and ` ignores=['foobar']  ` , Tilt will ignore both ` deps1/foobar  ` and ` dep2/foobar  ` ). 

  * **entrypoint** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â command to run when this container starts. Takes precedence over the containerâs ` CMD  ` or ` ENTRYPOINT  ` , and over a [ container command specified in k8s YAML ](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) . If specified as a string, will be evaluated in a shell context (e.g. ` entrypoint="foo.sh  bar" ` will be executed in the container as ` /bin/sh  -c  'foo.sh  bar' ` ); if specified as a list, will be passed to the operating system as program name and args. Kubernetes-only. 

  * **command_bat_val** ( ` str  ` ) â Deprecated, use command_bat. 

  * **outputs_image_ref_to** ( ` str  ` ) â Specifies a file path. When set, the custom build command must write a content-based tagged image ref to this file. Tilt will read that file after the cmd runs to get the image ref, and inject that image ref into the YAML. For more on content-based tags, see [ why tilt uses immutable tags ](custom_build.html#why-tilt-uses-immutable-tags)

  * **command_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` command  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **image_deps** ( ` List  ` [ ` str  ` ]) â 

a list of image builds that this deploy depends on. The tagged image names
will be injected into the environment of the the custom build command in the
form:

TILT_IMAGE_i  \- The reference to the image #i (0-based) from the point of
view of the local host.

TILT_IMAGE_MAP_i  \- The name of the image map #i (0-based) with the current
status of the image.

  * **env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â Environment variables to pass to the executed ` command  ` . Values specified here will override any variables passed to the Tilt parent process. 

  * **dir** ( ` str  ` ) â Working directory of the executed ` command  ` . Defaults to the Tiltfile directory. 

dc_resource  (  _ name  _ , _ trigger_mode  =  TRIGGER_MODE_AUTO  _ , _
resource_deps  =  []  _ , _ links  =  []  _ , _ labels  =  []  _ , _ auto_init
=  True  _ , _ project_name  =  '' _ , _ new_name  =  '' _ , _ infer_links  =
True  _ )  ï

    

Configures the Docker Compose resource of the given name. Note: Tilt does an
amount of resource configuration for you(for more info, see [ Tiltfile
Concepts: Resources ](tiltfile_concepts.html#resources) ); you only need to
invoke this function if you want to configure your resource beyond what Tilt
does automatically.

Parameters

    

  * **name** ( ` str  ` ) â The name of the resource in the docker-compose yaml. 

  * **trigger_mode** (  ` TriggerMode  ` ) â one of ` TRIGGER_MODE_AUTO  ` or ` TRIGGER_MODE_MANUAL  ` . For more info, see the [ Manual Update Control docs ](manual_update_control.html) . 

  * **resource_deps** ( ` List  ` [ ` str  ` ]) â a list of resources on which this resource depends. See the [ Resource Dependencies docs ](resource_dependencies.html) . 

  * **links** ( ` Union  ` [ ` str  ` ,  ` Link  ` , ` List  ` [ ` Union  ` [ ` str  ` ,  ` Link  ` ]]]) â one or more links to be associated with this resource in the UI. For more info, see [ Accessing Resource Endpoints ](accessing_resource_endpoints.html#arbitrary-links) . 

  * **labels** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â used to group resources in the Web UI, (e.g. you want all frontend services displayed together, while test and backend services are displayed separately). A label must start and end with an alphanumeric character, can include ` _  ` , ` -  ` , and ` .  ` , and must be 63 characters or less. For an example, see [ Resource Grouping ](tiltfile_concepts.html#resource-groups) . 

  * **auto_init** ( ` bool  ` ) â 

whether this resource runs on ` tilt  up  ` . Defaults to ` True  ` . For more
info, see the [ Manual Update Control docs ](manual_update_control.html) .

  * **project_name** ( ` str  ` ) â The Docker Compose project name to match the corresponding project loaded by ` docker_compose  ` , if necessary for disambiguation. 

  * **new_name** ( ` str  ` ) â If non-empty, will be used as the new name for this resource. 

  * **infer_links** ( ` bool  ` ) â whether to include the default localhost links. Defaults to ` True  ` . If ` False  ` , only links explicitly provided via the links argument will be displayed. 

Return type

    

` None  `

decode_json  (  _ json  _ )  ï

    

Deserializes the given JSON into a starlark object

Parameters

    

**json** ( ` Union  ` [ ` str  ` ,  ` Blob  ` ]) â the JSON to deserialize

Return type

    

` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ]]

decode_yaml  (  _ yaml  _ )  ï

    

Deserializes the given yaml document into a starlark object

Parameters

    

**yaml** ( ` Union  ` [ ` str  ` ,  ` Blob  ` ]) â the yaml to deserialize

Return type

    

` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ]]

decode_yaml_stream  (  _ yaml  _ )  ï

    

Deserializes the given yaml stream (i.e., any number of yaml documents,
separated by ` "\n---\n" ` ) into a list of starlark objects.

Parameters

    

**yaml** ( ` Union  ` [ ` str  ` ,  ` Blob  ` ]) â the yaml to deserialize

Return type

    

` List  ` [ ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any
` ]]]

default_registry  (  _ host  _ , _ host_from_cluster  =  None  _ , _
single_name  =  '' _ )  ï

    

Specifies that any images that Tilt builds should be renamed so that they have
the specified Docker registry.

This is useful if, e.g., a repo is configured to push to Google Container
Registry, but you want to use Elastic Container Registry instead, without
having to edit a bunch of configs. For example, `
default_registry("gcr.io/myrepo")  ` would cause ` docker.io/alpine  ` to be
rewritten to ` gcr.io/myrepo/docker.io_alpine  `

For more info, see our [ Using a Personal Registry Guide
](personal_registry.html) .

Parameters

    

  * **host** ( ` str  ` ) â host of the registry that all built images should be renamed to use. 

  * **host_from_cluster** ( ` Optional  ` [ ` str  ` ]) â registry host to use when referencing images from inside the cluster (i.e. in Kubernetes YAML). Only include this arg if it is different from ` host  ` . For more on this use case, [ see this guide ](personal_registry.html#different-urls-from-inside-your-cluster) . 

  * **single_name** ( ` str  ` ) â In ECR, each repository in a registry needs to be created up-front. single_name lets you set a single repository to push to (e.g., a personal dev repository), and embeds the image name in the tag instead. 

Images are renamed following these rules:

  1. Replace ` /  ` and ` @  ` with ` _  ` . 

  2. Prepend the value of ` host  ` and a ` /  ` . 

e.g., with ` default_registry('gcr.io/myorg')  ` , an image called ` user-
service  ` becomes ` gcr.io/myorg/user-service  ` .

Return type

    

` None  `

disable_snapshots  (  )  ï

    

Disables Tiltâs [ snapshots ](snapshots.html) feature, hiding it from the
UI.

This is intended for use in projects where there might be some kind of data
policy that does not allow developers to upload snapshots to TiltCloud.

Note that this directive does not provide any real security, since a developer
can always simply edit it out of the Tiltfile, but it at least ensures a
pretty high bar of intent.

Return type

    

` None  `

docker_build  (  _ ref  _ , _ context  _ , _ build_args  =  {}  _ , _
dockerfile  =  'Dockerfile' _ , _ dockerfile_contents  =  '' _ , _ live_update
=  []  _ , _ match_in_env_vars  =  False  _ , _ ignore  =  []  _ , _ only  =
[]  _ , _ entrypoint  =  []  _ , _ target  =  '' _ , _ ssh  =  '' _ , _
network  =  '' _ , _ secret  =  '' _ , _ extra_tag  =  '' _ , _ container_args
=  None  _ , _ cache_from  =  []  _ , _ pull  =  False  _ , _ platform  =  ''
_ , _ extra_hosts  =  []  _ )  ï

    

Builds a docker image.

The invocation

    
    
    docker_build('myregistry/myproj/backend', '/path/to/code')
    

is roughly equivalent to the shell call

    
    
    docker build /path/to/code -t myregistry/myproj/backend
    

For more information on the  ignore  and  only  parameters, see our [ Guide to
File Changes ](/file_changes.html) .

Note that you canât set both the  dockerfile  and  dockerfile_contents
arguments (will throw an error).

Note also that the  entrypoint  parameter is not supported for Docker Compose
resources.

When using Docker Compose, Tilt expects the image build to be either managed
by your Docker Compose file (via the [ build
](https://docs.docker.com/compose/compose-file/compose-file-v3/#build) key) OR
by Tiltâs  ` docker_build()  ` , but not both. (Follow this [ GitHub issue
](https://github.com/tilt-dev/tilt/issues/5196) to be notified of changes to
this expectation.)

Finally, Tilt will put the image in a place where the target runtime can
access it. Tilt will make a best effort to detect what kind of runtime
youâre using (Docker Compose, Kind, GKE, etc), and pick the best strategy
for getting the image into it fast. See [
https://docs.tilt.dev/choosing_clusters.html
](https://docs.tilt.dev/choosing_clusters.html) for more info.

Parameters

    

  * **ref** ( ` str  ` ) â name for this image (e.g. âmyproj/backendâ or âmyregistry/myproj/backendâ). If this image will be used in a k8s resource(s), this ref must match the ` spec.container.image  ` param for that resource(s). 

  * **context** ( ` str  ` ) â path to use as the Docker build context. 

  * **build_args** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â build-time variables that are accessed like regular environment variables in the ` RUN  ` instruction of the Dockerfile. See [ the Docker Build Arg documentation ](https://docs.docker.com/engine/reference/commandline/build/#set-build-time-variables---build-arg) . 

  * **dockerfile** ( ` str  ` ) â path to the Dockerfile to build. 

  * **dockerfile_contents** ( ` Union  ` [ ` str  ` ,  ` Blob  ` ]) â raw contents of the Dockerfile to use for this build. 

  * **live_update** ( ` List  ` [  ` LiveUpdateStep  ` ]) â 

set of steps for updating a running container (see [ Live Update documentation
](live_update_reference.html) ).

  * **match_in_env_vars** ( ` bool  ` ) â specifies that k8s objects can reference this image in their environment variables, and Tilt will handle those variables the same as it usually handles a k8s container specâs ` image  ` s. 

  * **ignore** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â 

set of file patterns that will be ignored, in addition to ` .git  ` directory
thatâs [ ignored by default ](file_changes.html#where-ignores-come-from) .
Ignored files will not trigger builds and will not be included in images.
Follows the [ dockerignore syntax
](https://docs.docker.com/engine/reference/builder/#dockerignore-file) .
Patterns will be evaluated relative to the ` context  ` parameter.

  * **only** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â set of file paths that should be considered for the build. All other changes will not trigger a build and will not be included in images. Inverse of ignore parameter. Only accepts real paths, not file globs. Patterns will be evaluated relative to the ` context  ` parameter. 

  * **entrypoint** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â 

command to run when this container starts. Takes precedence over the
containerâs ` CMD  ` or ` ENTRYPOINT  ` , and over a [ container command
specified in k8s YAML ](https://kubernetes.io/docs/tasks/inject-data-
application/define-command-argument-container/) . If specified as a string,
will be evaluated in a shell context (e.g. ` entrypoint="foo.sh  bar" ` will
be executed in the container as ` /bin/sh  -c  'foo.sh  bar' ` ); if specified
as a list, will be passed to the operating system as program name and args.

  * **target** ( ` str  ` ) â Specify a build stage in the Dockerfile. Equivalent to the ` docker  build  --target  ` flag. 

  * **ssh** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Include SSH secrets in your build. Use ssh=âdefaultâ to clone private repositories inside a Dockerfile. Uses the syntax in the [ docker build âssh flag ](https://docs.docker.com/develop/develop-images/build_enhancements/#using-ssh-to-access-private-data-in-builds) . 

  * **network** ( ` str  ` ) â Set the networking mode for RUN instructions. Equivalent to the ` docker  build  --network  ` flag. 

  * **secret** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Include secrets in your build in a way that wonât show up in the image. Uses the same syntax as the [ docker build âsecret flag ](https://docs.docker.com/develop/develop-images/build_enhancements/#new-docker-build-secret-information) . 

  * **extra_tag** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Tag an image with one or more extra references after each build. Useful when running Tilt in a CI pipeline, where you want each image to be tagged with the pipeline ID so you can find it later. Uses the same syntax as the ` docker  build  --tag  ` flag. 

  * **container_args** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â args to run when this container starts. Takes precedence over a [ container args specified in k8s YAML ](https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/) . 

  * **cache_from** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Cache image builds from a remote registry. Uses the same syntax as [ docker build âcache-from flag ](https://docs.docker.com/engine/reference/commandline/build/#specifying-external-cache-sources) . 

  * **pull** ( ` bool  ` ) â Force pull the latest version of parent images. Equivalent to the ` docker  build  --pull  ` flag. 

  * **platform** ( ` str  ` ) â Target platform for build (e.g. ` linux/amd64  ` ). Defaults to the value of the ` DOCKER_DEFAULT_PLATFORM  ` environment variable. Equivalent to the ` docker  build  --platform  ` flag. 

  * **extra_hosts** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Add a custom host-to-IP mapping (host:ip). Equivalent to the ` docker  build  --add-host  ` flag. 

Return type

    

` None  `

docker_compose  (  _ configPaths  _ , _ env_file  =  None  _ , _ project_name
=  '' _ , _ profiles  =  []  _ , _ wait  =  False  _ )  ï

    

Run containers with Docker Compose.

Tilt will read your Docker Compose YAML and separate out the services. We will
infer which services defined in your YAML correspond to images defined
elsewhere in your ` Tiltfile  ` (matching based on the DockerImage ref).

You can set up Docker Compose with a path to a file, a Blob containing Compose
YAML, or a list of paths and/or Blobs.

Tilt will watch your Docker Compose YAML and reload if it changes.

For more info, see [ the guide to Tilt with Docker Compose
](docker_compose.html) .

Examples:

    
    
    # Path to file
    docker_compose('./docker-compose.yml')
    
    # List of files
    docker_compose(['./docker-compose.yml', './docker-compose.override.yml'])
    
    # Inline compose definition
    services = {'redis': {'image': 'redis', 'ports': '6379:6379'}}
    docker_compose(encode_yaml({'services': services}))
    
    # File with inline override
    services = {'app': {'environment': {'DEBUG': 'true'}}}
    docker_compose(['docker-compose.yml', encode_yaml({'services': services})])
    

Parameters

    

  * **configPaths** ( ` Union  ` [ ` str  ` ,  ` Blob  ` , ` List  ` [ ` Union  ` [ ` str  ` ,  ` Blob  ` ]]]) â Path(s) and/or Blob(s) to Docker Compose yaml files or content. 

  * **env_file** ( ` Optional  ` [ ` str  ` ]) â Path to env file to use; defaults to ` .env  ` in current directory. 

  * **project_name** ( ` str  ` ) â The Docker Compose project name. If unspecified, uses either the name of the directory containing the first compose file, or, in the case of inline YAML, the current Tiltfileâs directory name. 

  * **profiles** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â List of Docker Compose profiles to use. 

  * **wait** â If ` True  ` , append âwait to docker compose up command. Defaults to ` False  ` . 

Return type

    

` None  `

docker_prune_settings  (  _ disable  =  False  _ , _ max_age_mins  =  360  _ ,
_ num_builds  =  0  _ , _ interval_hrs  =  1  _ , _ keep_recent  =  2  _ )
ï

    

Configures Tiltâs Docker Pruner, which runs occasionally in the background
and prunes Docker images associated with your current project.

The pruner runs soon after startup (as soon as at least some resources are
declared, and there are no pending builds). Subsequently, it runs after every
` num_builds  ` Docker builds, or, if ` num_builds  ` is not set, every `
interval_hrs  ` hours.

The pruner will prune:

    

  * stopped containers built by Tilt that are at least ` max_age_mins  ` mins old 

  * images built by Tilt and associated with this Tilt run that are at least ` max_age_mins  ` mins old, and not in the ` keep_recent  ` most recent builds for that image name 

  * dangling build caches that are at least ` max_age_mins  ` mins old 

Parameters

    

  * **disable** ( ` bool  ` ) â if true, disable the Docker Pruner 

  * **max_age_mins** ( ` int  ` ) â maximum age, in minutes, of images/containers to retain. Defaults to 360 mins., i.e. 6 hours 

  * **num_builds** ( ` int  ` ) â number of Docker builds after which to run a prune. (If unset, the pruner instead runs every ` interval_hrs  ` hours) 

  * **interval_hrs** ( ` int  ` ) â run a Docker Prune every ` interval_hrs  ` hours (unless ` num_builds  ` is set, in which case use the âprune every X buildsâ logic). Defaults to 1 hour 

  * **keep_recent** ( ` int  ` ) â when pruning, retain at least the ` keep_recent  ` most recent images for each image name. Defaults to 2 

Return type

    

` None  `

enable_feature  (  _ feature_name  _ )  ï

    

Configures Tilt to enable non-default features (e.g., experimental or
deprecated).

The Tilt features controlled by this are generally in an unfinished state, and
not yet documented.

As a Tiltfile author, you donât need to worry about this function unless
something else directs you to (e.g., an experimental feature doc, or a
conversation with a Tilt contributor).

As a Tiltfile reader, you can probably ignore this, or you can ask the person
who added it to the Tiltfile what itâs doing there.

Parameters

    

**feature_name** ( ` str  ` ) â name of the feature to enable

Return type

    

` None  `

encode_json  (  _ obj  _ )  ï

    

Serializes the given starlark object into JSON.

Only supports maps with string keys, lists, strings, ints, and bools.

Parameters

    

**obj** ( ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  `
]]) â the object to serialize

Return type

    

` Blob  `

encode_yaml  (  _ obj  _ )  ï

    

Serializes the given starlark object into YAML.

Only supports maps with string keys, lists, strings, ints, and bools.

Parameters

    

**obj** ( ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  `
]]) â the object to serialize

Return type

    

` Blob  `

encode_yaml_stream  (  _ objs  _ )  ï

    

Serializes the given starlark objects into a YAML stream (i.e., multiple YAML
documents, separated by ` "\n---\n" ` ).

Only supports maps with string keys, lists, strings, ints, and bools.

Parameters

    

**objs** ( ` List  ` [ ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List
` [ ` Any  ` ]]]) â the object to serialize

Return type

    

` Blob  `

exec_action  (  _ command  _ )  ï

    

Creates an  ` ExecAction  ` for use with a  ` Probe  ` that runs a command to
determine service readiness based on exit code.

The probe is successful if the process terminates normally with an exit code
of 0 within the timeout.

Parameters

    

**command** ( ` List  ` [ ` str  ` ]) â Command with arguments to execute.

Return type

    

` ExecAction  `

exit  (  _ code  _ )  ï

    

Stops Tiltfile execution without an error.

Can be used anywhere in a Tiltfile. If used in a loaded Tiltfile or extension,
execution will be stopped up to and including the root Tiltfile.

Requires Tilt v0.22.3+.

See  ` fail()  ` to stop execution immediately and propagate an error.

Parameters

    

**code** ( ` Any  ` ) â Message or object (will be stringified) to log
before halting execution.

Return type

    

` None  `

fail  (  _ msg  _ )  ï

    

Stops Tiltfile execution and raises an error.

Can be used anywhere in a Tiltfile. If used in a loaded Tiltfile or extension,
execution will be stopped up to and including the root Tiltfile.

See  ` exit()  ` to stop execution immediately without triggering an error.

Parameters

    

**msg** ( ` str  ` ) â Error message.

Return type

    

` None  `

fall_back_on  (  _ files  _ )  ï

    

Specify that any changes to the given files will cause Tilt to _fall back_ to
a full image build (rather than performing a live update).

` fall_back_on  ` step(s) may only go at the beginning of your list of steps.

(Files must be a subset of the files that weâre already watching for this
image; that is, if any files fall outside of DockerBuild.context or
CustomBuild.deps, an error will be raised.)

For more info, see the [ Live Update Reference ](live_update_reference.html) .

Parameters

    

**files** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â a string or
list of strings of files. If relative, will be evaluated relative to the
Tiltfile. Tilt compares these to the local paths of edited files when
determining whether to fall back to a full image build.

Return type

    

` LiveUpdateStep  `

filter_yaml  (  _ yaml  _ , _ labels  =  None  _ , _ name  =  None  _ , _
namespace  =  None  _ , _ kind  =  None  _ , _ api_version  =  None  _ )  ï

    

Call this with a path to a file that contains YAML, or with a ` Blob  ` of
YAML. (E.g. it can be called on the output of ` kustomize  ` or ` helm  ` .)

Captures the YAML entities that meet the filter criteria and returns them as a
blob; returns the non-matching YAML as the second return value.

For example, if you have a file of _all_ your YAML, but only want to pass a
few elements to Tilt:

    
    
    # extract all YAMLs matching labels "app=foobar"
    foobar_yaml, rest = filter_yaml('all.yaml', labels={'app': 'foobar'})
    k8s_yaml(foobar_yaml)
    
    # extract YAMLs of kind "deployment" with metadata.name regex-matching "baz", also matching "bazzoo" and "bar-baz"
    baz_yaml, rest = filter_yaml(rest, name='baz', kind='deployment')
    k8s_yaml(baz_yaml)
    
    # extract YAMLs of kind "deployment" exactly matching metadata.name "foo"
    foo_yaml, rest = filter_yaml(rest, name='^foo$', kind='deployment')
    k8s_yaml(foo_yaml)
    

Parameters

    

  * **yaml** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ],  ` Blob  ` ]) â Path(s) to YAML, or YAML as a ` Blob  ` . 

  * **labels** ( ` Optional  ` [ ` dict  ` ]) â return only entities matching these labels. (Matching entities must satisfy all of the specified label constraints, though they may have additional labels as well: see the [ Kubernetes docs ](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) for more info.) 

  * **name** ( ` Optional  ` [ ` str  ` ]) â Case-insensitive regexp specifying the ` metadata.name  ` property of entities to match 

  * **namespace** ( ` Optional  ` [ ` str  ` ]) â Case-insensitive regexp specifying the ` metadata.namespace  ` property of entities to match 

  * **kind** ( ` Optional  ` [ ` str  ` ]) â Case-insensitive regexp specifying the kind of entities to match (e.g. âServiceâ, âDeploymentâ, etc.). 

  * **api_version** ( ` Optional  ` [ ` str  ` ]) â Case-insensitive regexp specifying the apiVersion for  kind  , (e.g., âapps/v1â) 

Returns

    

2-element tuple containing

  * **matching** (  ` Blob  ` ): blob of YAML entities matching given filters 

  * **rest** (  ` Blob  ` ): the rest of the YAML entities 

helm  (  _ pathToChartDir  _ , _ name  =  '' _ , _ namespace  =  '' _ , _
values  =  []  _ , _ set  =  []  _ , _ kube_version  =  '' _ , _ skip_crds  =
False  _ )  ï

    

Run [ helm template ](https://helm.sh/docs/helm/helm_template/) on a given
directory that contains a chart and return the fully rendered YAML as a Blob
Chart directory is watched (See ` watch_file  ` ).

For more examples, see the [ Helm Cookbook ](helm.html) .

Parameters

    

  * **pathToChartDir** ( ` str  ` ) â Path to the directory locally (absolute, or relative to the location of the Tiltfile). 

  * **name** ( ` str  ` ) â The release name. Equivalent to the helm  [NAME]  argument. 

  * **namespace** ( ` str  ` ) â The namespace to deploy the chart to. Equivalent to the helm  ânamespace  flag 

  * **values** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Specify one or more values files (in addition to the  values.yaml  file in the chart). Equivalent to the Helm ` --values  ` or ` -f  ` flags ( [ see docs ](https://helm.sh/docs/chart_template_guide/values_files) ). 

  * **set** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Specify one or more values. Equivalent to the Helm ` --set  ` flag. 

  * **kube_version** ( ` str  ` ) â Specify for which kubernetes version template will be generated. Equivalent to the Helm ` --kube-version  ` flag. 

  * **skip_crds** ( ` bool  ` ) â If set, no CRDs will be installed. By default, CRDs are installed. 

Return type

    

` Blob  `

http_get_action  (  _ port  _ , _ host  =  'localhost' _ , _ scheme  =  'http'
_ , _ path  =  '' _ )  ï

    

Creates a  ` HTTPGetAction  ` for use with a  ` Probe  ` that performs an HTTP
GET request to determine service readiness based on response status code.

The probe is successful if a valid HTTP response is received within the
timeout and has a status code >= 200 and < 400\.

Parameters

    

  * **host** ( ` str  ` ) â Hostname to use for HTTP request. 

  * **port** ( ` int  ` ) â Port to use for HTTP request. 

  * **scheme** ( ` str  ` ) â URI scheme to use for HTTP request, valid values are  http  and  https  . 

  * **path** ( ` str  ` ) â URI path for HTTP request. 

Return type

    

` HTTPGetAction  `

include  (  _ path  _ )  ï

    

Execute another Tiltfile.

Discouraged. Please use  ` load()  ` or  ` load_dynamic()  ` .

Example

    
    
    include('./frontend/Tiltfile')
    include('./backend/Tiltfile')
    

k8s_context  (  )  ï

    

Returns the name of the Kubernetes context Tilt is connecting to.

Example

    
    
    if k8s_context() == 'prod':
      fail("failing early to avoid overwriting prod")
    

Return type

    

` str  `

k8s_custom_deploy  (  _ name  _ , _ apply_cmd  _ , _ delete_cmd  _ , _ deps  _
, _ image_selector  =  '' _ , _ live_update  =  []  _ , _ apply_dir  =  '' _ ,
_ apply_env  =  {}  _ , _ apply_cmd_bat  =  '' _ , _ delete_dir  =  '' _ , _
delete_env  =  {}  _ , _ delete_cmd_bat  =  '' _ , _ container_selector  =  ''
_ , _ image_deps  =  []  _ )  ï

    

Deploy resources to Kubernetes using a custom command.

For deployment tools that cannot output templated YAML for use with  `
k8s_yaml()  ` or need to perform additional work as part of deployment, `
k8s_custom_deploy  ` enables integration with Tilt.

The ` apply_cmd  ` will be run whenever a path from ` deps  ` changes and
should output the YAML of the objects it applied to the Kubernetes cluster to
stdout. Tilt will track workload status and stream pod logs based on this
result.

The ` delete_cmd  ` is run on ` tilt  down  ` so that the tool can clean up
any objects it created in the cluster as well as any state of its own.

Both ` apply_cmd  ` and ` delete_cmd  ` MUST be idempotent. For example,
itâs possible that some objects might already exist when the ` apply_cmd  `
is invoked, and objects might have already been deleted before ` delete_cmd  `
is invoked. The ` apply_cmd  ` should have similar semantics to ` kubectl
apply  ` and the ` delete_cmd  ` should behave similar to ` kubectl  delete
--ignore-not-found  ` .

Port forwards and other behavior can be configured using  ` k8s_resource()  `
using the ` name  ` as specified here.

If ` live_update  ` rules are specified, exactly one of ` image_selector  ` or
` container_selector  ` must be specified to determine which container(s) are
eligible for in-place updates. ` image_selector  ` will match containers based
on an image reference, while ` container_selector  ` will match a single
container by name.

Parameters

    

  * **name** ( ` str  ` ) â resource name to use in Tilt UI and for further customization via  ` k8s_resource()  `

  * **apply_cmd** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â command that deploys objects to the Kubernetes cluster. If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **delete_cmd** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â command that deletes objects in the Kubernetes cluster. If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **deps** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â paths to watch and trigger a re-apply on change 

  * **image_selector** ( ` str  ` ) â image reference to determine containers eligible for Live Update 

  * **live_update** ( ` List  ` [  ` LiveUpdateStep  ` ]) â 

set of steps for updating a running container (see [ Live Update documentation
](live_update_reference.html) ).

  * **apply_dir** ( ` str  ` ) â working directory for ` apply_cmd  `

  * **apply_env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â environment variables for ` apply_cmd  `

  * **apply_cmd_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` apply_cmd  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **delete_dir** ( ` str  ` ) â working directory for ` delete_cmd  `

  * **delete_env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â environment variables for ` delete_cmd  `

  * **delete_cmd_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` delete_cmd  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **container_selector** ( ` str  ` ) â container name to determine container for Live Update 

  * **image_deps** ( ` List  ` [ ` str  ` ]) â 

a list of image builds that this deploy depends on. The tagged image names
will be injected into the environment of the the apply command in the form:

TILT_IMAGE_i  \- The reference to the image #i (0-based) from the point of
view of the cluster container runtime.

TILT_IMAGE_MAP_i  \- The name of the image map #i (0-based) with the current
status of the image.

Return type

    

` None  `

k8s_kind  (  _ kind  _ , _ api_version  =  None  _ , _ *  _ , _
image_json_path  =  []  _ , _ image_object_json_path  =  None  _ , _
pod_readiness  =  '' _ )  ï

    

Tells Tilt about a k8s kind.

For CRDs that use images built by Tilt: call this with  image_json_path  or
image_object  to tell Tilt where in the CRDâs spec the image is specified.

For CRDs that do not use images built by Tilt, but have pods you want in a
Tilt resource: call this without  image_json_path  , simply to specify that
this type is a Tilt workload. Then call  ` k8s_resource()  ` with
extra_pod_selectors  to specify which pods Tilt should associate with this
resource.

(Note the  *  in the signature means  image_json_path  must be passed as a
keyword, e.g.,  image_json_path=â{.spec.image}â  )

Example

    
    
    # Fission has a CRD named "Environment"
    k8s_yaml('deploy/fission.yaml')
    k8s_kind('Environment', image_json_path='{.spec.runtime.image}')
    

Hereâs an example that specifies the image location in [ a UselessMachine
Custom Resource ](https://github.com/tilt-
dev/tilt/blob/master/integration/crd/Tiltfile#L8) .

Parameters

    

  * **kind** ( ` str  ` ) â Case-insensitive regexp specifying he value of the  kind  field in the k8s object definition (e.g.,  âDeploymentâ  ) 

  * **api_version** ( ` Optional  ` [ ` str  ` ]) â Case-insensitive regexp specifying the apiVersion for  kind  , (e.g., âapps/v1â) 

  * **image_json_path** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Either a string or a list of string containing json path(s) within that kindâs definition specifying images deployed with k8s objects of that type. This uses the k8s json path template syntax, described [ here ](https://kubernetes.io/docs/reference/kubectl/jsonpath/) . 

  * **image_object** â A specifier of the form  image_object={âjson_pathâ: â{.path.to.field}â, ârepo_fieldâ: ârepoâ, âtag_fieldâ: âtagâ}  . Used to tell Tilt how to inject images into Custom Resources that express the image repo and tag as separate fields. 

  * **pod_readiness** ( ` str  ` ) â Possible values: âignoreâ, âwaitâ. Controls whether Tilt waits for pods to be ready before the resource is considered healthy (and dependencies can start building). By default, Tilt will wait for pods to be ready if it thinks a resource has pods. This can be overridden on a resource-by-resource basis by the  k8s_resource  function. 

k8s_namespace  (  )  ï

    

Returns the name of the Kubernetes namespace Tilt is connecting to.

Example

    
    
    if k8s_namespace() == 'default':
      fail("failing early to avoid deploying to 'default' namespace")
    

Return type

    

` str  `

k8s_resource  (  _ workload  =  '' _ , _ new_name  =  '' _ , _ port_forwards
=  []  _ , _ extra_pod_selectors  =  []  _ , _ trigger_mode  =
TRIGGER_MODE_AUTO  _ , _ resource_deps  =  []  _ , _ objects  =  []  _ , _
auto_init  =  True  _ , _ pod_readiness  =  '' _ , _ links  =  []  _ , _
labels  =  []  _ , _ discovery_strategy  =  '' _ )  ï

    

Configures or creates the specified Kubernetes resource.

A âresourceâ is a bundle of work managed by Tilt: a Kubernetes resource
consists of one or more Kubernetes objects to deploy, and zero or more image
build directives for the images referenced therein.

Tilt assembles Kubernetes resources automatically, as described in [ Tiltfile
Concepts: Resources ](tiltfile_concepts.html#resources) . You may call `
k8s_resource  ` to configure an automatically created Kubernetes resource, or
to create and configure a new one:

  * If configuring an automatically created resource: the ` workload  ` parameter must be specified. 

  * If creating a new resource: both the ` objects  ` and ` new_name  ` parameters must be specified. 

Calling ` k8s_resource  ` is _optional_ ; you can use this function to
configure port forwarding for your resource, to rename it, or to adjust any of
the other settings specified below, but in many cases, Tiltâs default
behavior is sufficient.

Examples:

    
    
    # load Deployment foo
    k8s_yaml('foo.yaml')
    
    # modify the resource called "foo" (auto-assembled by Tilt)
    # to forward container port 8080 to localhost:8080
    k8s_resource(workload='foo', port_forwards=8080)
    
    
    
    # load CRD "bar", Service "bar", and Secret "bar-password"
    k8s_yaml('bar.yaml')
    
    # create a new resource called "bar" which contains the objects
    # loaded above (none of which are workloads, so none of which
    # would be automatically assigned to a resource). Note that the
    # first two object selectors specify both 'name' and 'kind',
    # since just the string "bar" does not uniquely specify a single object.
    # As the object name "bar-password" is unique, "bar-password" suffices as
    # an object selector (though a more qualified object selector
    # like "bar-password:secret" or "bar-password:secret:default" would
    # be accepted as well).
    k8s_resource(
      objects=['bar:crd', 'bar:service', 'bar-password'],
      new_name='bar'
    )
    

For more examples, see [ Tiltfile Concepts: Resources
](tiltfile_concepts.html#resources) .

Parameters

    

  * **workload** ( ` str  ` ) â The name of an existing auto-assembled resource to configure (Tilt generates resource names when it [ assembles resources by workload ](tiltfile_concepts.html#resources) ). (If you instead want to create/configure a _new_ resource, use the ` objects  ` parameter in conjunction with ` new_name  ` .) 

  * **new_name** ( ` str  ` ) â If non-empty, will be used as the new name for this resource. (To programmatically rename all resources, see  ` workload_to_resource_function()  ` .) 

  * **port_forwards** ( ` Union  ` [ ` str  ` , ` int  ` ,  ` PortForward  ` , ` List  ` [ ` Union  ` [ ` str  ` , ` int  ` ,  ` PortForward  ` ]]]) â 

Host port to connect to the pod. Takes 3 forms:

` '9000' ` (port only) - Connect localhost:9000 to the containerâs port
9000, if it is exposed. Otherwise connect to the containerâs default port.

` '9000:8000' ` (host port to container port) - Connect localhost:9000 to the
container port 8000).

` 'elastic.local:9200:8000' ` (host address to container port) - Bind
elasticsearch:9200 on the host to container port 8000. You will also need to
update /etc/host to make âelastic.localâ point to localhost.

Multiple port forwards can be specified (e.g., ` ['9000:8000',  '9001:8001']
` ). The string-based syntax is sugar over the more explicit `
port_forward(9000,  8000)  ` .

  * **extra_pod_selectors** ( ` Union  ` [ ` Dict  ` [ ` str  ` , ` str  ` ], ` List  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]]) â In addition to relying on Tiltâs heuristics to automatically find Kubernetes resources associated with this resource, a user may specify extra labelsets to force pods to be associated with this resource. An pod will be associated with this resource if it has all of the labels in at least one of the entries specified (but still also if it meets any of Tiltâs usual mechanisms). 

  * **trigger_mode** (  ` TriggerMode  ` ) â 

One of ` TRIGGER_MODE_AUTO  ` or ` TRIGGER_MODE_MANUAL  ` . For more info, see
the [ Manual Update Control docs ](manual_update_control.html) .

  * **resource_deps** ( ` List  ` [ ` str  ` ]) â 

A list of resources on which this resource depends. See the [ Resource
Dependencies docs ](resource_dependencies.html) .

  * **objects** ( ` List  ` [ ` str  ` ]) â A list of Kubernetes objects to be added to this resource, specified via Tiltâs [ Kubernetes Object Selector ](tiltfile_concepts.html#kubernetes-object-selectors) syntax. If the ` workload  ` parameter is specified, these objects will be added to the existing resource; otherwise, these objects will form a new resource with name ` new_name  ` . If an object selector matches more than one Kubernetes object, or matches an object already associated with a resource, ` k8s_resource  ` raises an error. 

  * **auto_init** ( ` bool  ` ) â 

whether this resource runs on ` tilt  up  ` . Defaults to ` True  ` . For more
info, see the [ Manual Update Control docs ](manual_update_control.html) .

  * **pod_readiness** ( ` str  ` ) â Possible values: âignoreâ, âwaitâ. Controls whether Tilt waits for pods to be ready before the resource is considered healthy (and dependencies can start building). By default, Tilt will wait for pods to be ready if it thinks a resource has pods. 

  * **links** ( ` Union  ` [ ` str  ` ,  ` Link  ` , ` List  ` [ ` Union  ` [ ` str  ` ,  ` Link  ` ]]]) â 

one or more links to be associated with this resource in the UI. For more
info, see [ Accessing Resource Endpoints
](accessing_resource_endpoints.html#arbitrary-links) .

  * **labels** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â 

used to group resources in the Web UI, (e.g. you want all frontend services
displayed together, while test and backend services are displayed separately).
A label must start and end with an alphanumeric character, can include ` _  `
, ` -  ` , and ` .  ` , and must be 63 characters or less. For an example, see
[ Resource Grouping ](tiltfile_concepts.html#resource-groups) .

  * **discovery_strategy** ( ` str  ` ) â Possible values: ââ, âdefaultâ, âselectors-onlyâ. When ââ or âdefaultâ, Tilt both uses  extra_pod_selectors  and traces k8s owner references to identify this resourceâs pods. When âselectors-onlyâ, Tilt uses only  extra_pod_selectors  . 

Return type

    

` None  `

k8s_yaml  (  _ yaml  _ , _ allow_duplicates  =  False  _ )  ï

    

Call this with a path to a file that contains YAML, or with a ` Blob  ` of
YAML.

We will infer what (if any) of the k8s resources defined in your YAML
correspond to Images defined elsewhere in your ` Tiltfile  ` (matching based
on the DockerImage ref and on pod selectors). Any remaining YAML is YAML that
Tilt applies to your k8s cluster independently.

Any YAML files are watched (See ` watch_file  ` ).

Examples:

    
    
    # path to file
    k8s_yaml('foo.yaml')
    
    # list of paths
    k8s_yaml(['foo.yaml', 'bar.yaml'])
    
    # Blob, i.e. `local` output (in this case, script output)
    templated_yaml = local('./template_yaml.sh')
    k8s_yaml(templated_yaml)
    

Parameters

    

  * **yaml** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ],  ` Blob  ` ]) â Path(s) to YAML, or YAML as a ` Blob  ` . 

  * **allow_duplicates** ( ` bool  ` ) â If you try to register the same Kubernetes resource twice, this function will assume this is a mistake and emit an error. Set allow_duplicates=True to allow duplicates. There are some Helm charts that have duplicate resources for esoteric reasons. 

Return type

    

` None  `

kustomize  (  _ pathToDir  _ , _ kustomize_bin  =  None  _ , _ flags  =  []  _
)  ï

    

Run [ kustomize ](https://github.com/kubernetes-sigs/kustomize) on a given
directory and return the resulting YAML as a Blob Directory is watched (see `
watch_file  ` ). Checks for and uses separately installed kustomize first, if
it exists. Otherwise, uses kubectlâs kustomize. See [ blog post
](https://blog.tilt.dev/2020/02/04/are-you-my-kustomize.html) .

Parameters

    

  * **pathToDir** ( ` str  ` ) â Path to the directory locally (absolute, or relative to the location of the Tiltfile). 

  * **kustomize_bin** ( ` Optional  ` [ ` str  ` ]) â Custom path to the ` kustomize  ` binary executable. Defaults to searching $PATH for kustomize. 

  * **flags** ( ` List  ` [ ` str  ` ]) â Additional flags to pass to ` kustomize  build  `

Return type

    

` Blob  `

link  (  _ url  _ , _ name  _ )  ï

    

Creates a  ` Link  ` object that describes a link associated with a resource.

Parameters

    

  * **url** ( _str_ ) â the URL to link to 

  * **name** ( _str_ _,_ _optional_ ) â the name of the link. If provided, this will be the text of this URL when displayed in the Web UI. This parameter can be useful for disambiguating between multiple links on a single resource, e.g. naming one link âAppâ and one âDebugger.â If not given, the Web UI displays the URL itself (e.g. âlocalhost:8888â). 

Return type

    

` Link  `

listdir  (  _ directory  _ , _ recursive  =  False  _ )  ï

    

Returns all the files of the provided directory.

If ` recursive  ` is set to ` True  ` , the directoryâs contents will be
recursively watched, and a change to any file will trigger a re-execution of
the Tiltfile.

This function returns absolute paths. Subdirectory names are not returned.

Parameters

    

  * **directory** ( ` str  ` ) â Path to the directory locally (absolute, or relative to the location of the Tiltfile). 

  * **recursive** ( ` bool  ` ) â Walk the given directory tree recursively and return all files in it; additionally, recursively watch for changes in the directory tree. 

Return type

    

` List  ` [ ` str  ` ]

load  (  _ path  _ , _ *  args  _ )  ï

    

Execute another Tiltfile, and import the named variables into the current
scope.

Used when you want to define common functions or constants to share across
Tiltfiles.

Example

    
    
    load('./lib/Tiltfile', 'create_namespace')
    create_namespace('frontend')
    

A Tiltfile may only be executed once. If a Tiltfile is loaded multiple times,
the second load will use the results of the last execution.

If ` path  ` starts with ` "ext://" ` the path will be treated as a [ Tilt
Extension ](extensions.html) .

Example

    
    
    load('ext://hello_world', 'hi') # Resolves to https://github.com/tilt-dev/tilt-extensions/blob/master/hello_world/Tiltfile
    hi() # prints "Hello world!"
    

Note that ` load()  ` is a language built-in. Read the [ specification
](https://github.com/google/starlark-go/blob/master/doc/spec.md#load-
statements) for its complete syntax.

Because ` load()  ` is analyzed at compile-time, the first argument MUST be a
string literal.

load_dynamic  (  _ path  _ )  ï

    

Execute another Tiltfile, and return a dict of the global variables it
creates.

Used when you want to define common functions or constants to share across
Tiltfiles.

Example

    
    
    symbols = load_dynamic('./lib/Tiltfile')
    create_namespace = symbols['create_namespace']
    create_namespace('frontend')
    

Like  ` load()  ` , each Tiltfile will only be executed once. Can also be used
to load a [ Tilt Extension ](extensions.html) .

Because ` load_dynamic()  ` is executed at run-time, you can use it to do
meta-programming that you cannot do with ` load()  ` (like determine which
file to load by running a script first). But you need to unpack the variables
yourself - you donât get the nice syntactic sugar of binding local
variables.

Return type

    

` Dict  ` [ ` str  ` , ` Any  ` ]

local  (  _ command  _ , _ quiet  =  False  _ , _ command_bat  =  '' _ , _
echo_off  =  False  _ , _ env  =  {}  _ , _ dir  =  '' _ , _ stdin  =  None  _
)  ï

    

Runs a command on the _host_ machine, waits for it to finish, and returns its
stdout as a ` Blob  `

Parameters

    

  * **command** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Command to run. If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **quiet** ( ` bool  ` ) â If set to True, skips printing output to log. 

  * **command_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` command  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **echo_off** ( ` bool  ` ) â If set to True, skips printing command to log. 

  * **env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â Environment variables to pass to the executed ` command  ` . Values specified here will override any variables passed to the Tilt parent process. 

  * **dir** ( ` str  ` ) â Working directory for ` command  ` . Defaults to the Tiltfileâs location. 

  * **stdin** ( ` Union  ` [ ` str  ` ,  ` Blob  ` , ` None  ` ]) â If not ` None  ` , will be written to ` command  ` âs stdin. 

Return type

    

` Blob  `

local_resource  (  _ name  _ , _ cmd  _ , _ deps  =  None  _ , _ trigger_mode
=  TRIGGER_MODE_AUTO  _ , _ resource_deps  =  []  _ , _ ignore  =  []  _ , _
auto_init  =  True  _ , _ serve_cmd  =  '' _ , _ cmd_bat  =  '' _ , _
serve_cmd_bat  =  '' _ , _ allow_parallel  =  False  _ , _ links  =  []  _ , _
labels  =  []  _ , _ env  =  {}  _ , _ serve_env  =  {}  _ , _ readiness_probe
=  None  _ , _ dir  =  '' _ , _ serve_dir  =  '' _ )  ï

    

Configures one or more commands to run on the _host_ machine (not in a remote
cluster).

By default, Tilt performs an update on local resources on ` tilt  up  ` and
whenever any of their ` deps  ` change.

When Tilt performs an update on a local resource:

  * if  cmd  is non-empty, it is executed 

  * if  cmd  succeeds: \- Tilt kills any extant  serve_cmd  process from previous updates of this resource \- if  serve_cmd  is non-empty, it is executed 

For more info, see the [ Local Resource docs ](local_resource.html) .

Parameters

    

  * **name** ( ` str  ` ) â will be used as the new name for this resource 

  * **cmd** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â command to be executed on host machine. If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **deps** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ], ` None  ` ]) â a list of files or directories to be added as dependencies to this cmd. Tilt will watch those files and will run the cmd when they change. Only accepts real paths, not file globs. 

  * **trigger_mode** (  ` TriggerMode  ` ) â 

one of ` TRIGGER_MODE_AUTO  ` or ` TRIGGER_MODE_MANUAL  ` . For more info, see
the [ Manual Update Control docs ](manual_update_control.html) .

  * **resource_deps** ( ` List  ` [ ` str  ` ]) â 

a list of resources on which this resource depends. See the [ Resource
Dependencies docs ](resource_dependencies.html) .

  * **ignore** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â 

set of file patterns that will be ignored. Ignored files will not trigger
runs. Follows the [ dockerignore syntax
](https://docs.docker.com/engine/reference/builder/#dockerignore-file) .
Patterns will be evaluated relative to the Tiltfile.

  * **auto_init** ( ` bool  ` ) â 

whether this resource runs on ` tilt  up  ` . Defaults to ` True  ` . For more
info, see the [ Manual Update Control docs ](manual_update_control.html) .

  * **serve_cmd** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Tilt will run this command on update and expect it to not exit. If a string, executed with ` sh  -c  ` on macOS/Linux, or ` cmd  /S  /C  ` on Windows; if a list, will be passed to the operating system as program name and args. 

  * **cmd_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` cmd  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **serve_cmd_bat** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â If non-empty and on Windows, takes precedence over ` serve_cmd  ` . Ignored on other platforms. If a string, executed as a Windows batch command executed with ` cmd  /S  /C  ` ; if a list, will be passed to the operating system as program name and args. 

  * **allow_parallel** ( ` bool  ` ) â By default, all local resources are presumed unsafe to run in parallel, due to race conditions around modifying a shared file system. Set to True to allow them to run in parallel. 

  * **links** ( ` Union  ` [ ` str  ` ,  ` Link  ` , ` List  ` [ ` Union  ` [ ` str  ` ,  ` Link  ` ]]]) â one or more links to be associated with this resource in the Web UI (e.g. perhaps you have a âreset databaseâ workflow and want to attach a link to the database web console). Provide one or more strings (the URLs to link to) or  ` Link  ` objects. 

  * **labels** ( ` List  ` [ ` str  ` ]) â 

used to group resources in the Web UI, (e.g. you want all frontend services
displayed together, while test and backend services are displayed separately).
A label must start and end with an alphanumeric character, can include ` _  `
, ` -  ` , and ` .  ` , and must be 63 characters or less. For an example, see
[ Resource Grouping ](tiltfile_concepts.html#resource-groups) .

  * **env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â Environment variables to pass to the executed ` cmd  ` . Values specified here will override any variables passed to the Tilt parent process. 

  * **serve_env** ( ` Dict  ` [ ` str  ` , ` str  ` ]) â Environment variables to pass to the executed ` serve_cmd  ` . Values specified here will override any variables passed to the Tilt parent process. 

  * **readiness_probe** ( ` Optional  ` [  ` Probe  ` ]) â Optional readiness probe to use for determining ` serve_cmd  ` health state. Fore more info, see the  ` probe()  ` function. 

  * **dir** ( ` str  ` ) â Working directory for ` cmd  ` . Defaults to the Tiltfile directory. 

  * **serve_dir** ( ` str  ` ) â Working directory for ` serve_cmd  ` . Defaults to the Tiltfile directory. 

Return type

    

` None  `

port_forward  (  _ local_port  _ , _ container_port  =  None  _ , _ name  =
None  _ , _ link_path  =  None  _ , _ host  =  None  _ )  ï

    

Creates a  ` PortForward  ` object specifying how to set up and display a
Kubernetes port forward.

By default, the host for a port-forward is ` localhost  ` . This can be
changed with the ` --host  ` flag when invoking Tilt via the CLI.

Parameters

    

  * **local_port** ( _int_ ) â the local port to forward traffic to. 

  * **container_port** ( _int_ _,_ _optional_ ) â if provided, the container port to forward traffic _from_ . If not provided, Tilt will forward traffic from ` local_port  ` , if exposed, and otherwise, from the first default container port. E.g.: ` PortForward(1111)  ` forwards traffic from container port 1111 (if exposed; otherwise first default container port) to ` localhost:1111  ` . 

  * **name** ( _str_ _,_ _optional_ ) â the name of the link. If provided, this will be text of this URL when displayed in the Web UI. This parameter can be useful for disambiguating between multiple port-forwards on a single resource, e.g. naming one link âAppâ and one âDebugger.â If not given, the Web UI displays the URL itself (e.g. âlocalhost:8888â). 

  * **link_path** ( _str_ _,_ _optional_ ) â if given, the path at the port forward URL to link to; e.g. a port forward on localhost:8888 with ` link_path='/v1/app' ` would surface a link in the UI to ` localhost:8888/v1/app  ` . 

  * **host** ( _str_ _,_ _optional_ ) â if given, the host of the port forward (by default, ` localhost  ` ). E.g. a call to  port_forward(8888, host=âelastic.localâ)  would forward container port 8888 to ` elastic.local:8888  ` . 

Return type

    

` PortForward  `

probe  (  _ initial_delay_secs  =  0  _ , _ timeout_secs  =  1  _ , _
period_secs  =  10  _ , _ success_threshold  =  1  _ , _ failure_threshold  =
3  _ , _ exec  =  None  _ , _ http_get  =  None  _ , _ tcp_socket  =  None  _
)  ï

    

Creates a  ` Probe  ` for use with local_resource readiness checks.

Exactly one of exec, http_get, or tcp_socket must be specified.

Parameters

    

  * **initial_delay_secs** ( ` int  ` ) â Number of seconds after the resource has started before the probe is first initiated (default is 0). 

  * **timeout_secs** ( ` int  ` ) â Number of seconds after which probe execution is aborted and it is considered to have failed (default is 1, must be greater than 0). 

  * **period_secs** ( ` int  ` ) â How often in seconds to perform the probe (default is 10, must be greater than 0). 

  * **success_threshold** ( ` int  ` ) â Minimum number of consecutive successes for the result to be considered successful after having failed (default is 1, must be greater than 0). 

  * **failure_threshold** ( ` int  ` ) â Minimum number of consecutive failures for the result to be considered failing after having succeeded (default is 3, must be greater than 0). 

  * **exec** ( ` Optional  ` [  ` ExecAction  ` ]) â Process execution handler to determine probe success. 

  * **http_get** ( ` Optional  ` [  ` HTTPGetAction  ` ]) â HTTP GET handler to determine probe success. 

  * **tcp_socket** ( ` Optional  ` [  ` TCPSocketAction  ` ]) â TCP socket connection handler to determine probe success. 

Return type

    

` Probe  `

read_file  (  _ file_path  _ , _ default  =  None  _ )  ï

    

Reads file and returns its contents.

If the  file_path  does not exist and  default  is not  None  ,  default  will
be returned. In any other case, an error reading  file_path  will be a
Tiltfile load error.

Parameters

    

  * **file_path** ( ` str  ` ) â Path to the file locally (absolute, or relative to the location of the Tiltfile). 

  * **default** ( ` Optional  ` [ ` str  ` ]) â If not  None  and the file at  file_path  does not exist, this value will be returned. 

Return type

    

` Blob  `

read_json  (  _ path  _ , _ default  =  None  _ )  ï

    

Reads the file at  path  and deserializes its contents as JSON

If the  path  does not exist and  default  is not  None  ,  default  will be
returned. In any other case, an error reading  path  will be a Tiltfile load
error.

Parameters

    

  * **path** ( ` str  ` ) â Path to the file locally (absolute, or relative to the location of the Tiltfile). 

  * **default** ( ` Optional  ` [ ` str  ` ]) â If not  None  and the file at  path  does not exist, this value will be returned. 

Return type

    

` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ]]

read_yaml  (  _ path  _ , _ default  =  None  _ )  ï

    

Reads the file at  path  and deserializes its contents into a starlark object

If the  path  does not exist and  default  is not  None  ,  default  will be
returned. In any other case, an error reading  path  will be a Tiltfile load
error.

Parameters

    

  * **path** ( ` str  ` ) â Path to the file locally (absolute, or relative to the location of the Tiltfile). 

  * **default** ( ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ], ` None  ` ]) â If not  None  and the file at  path  does not exist, this value will be returned. 

Return type

    

` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ]]

read_yaml_stream  (  _ path  _ , _ default  =  None  _ )  ï

    

Reads a yaml stream (i.e., yaml documents separated by ` "\n---\n" ` ) from
the file at  path  and deserializes its contents into a starlark object

If the  path  does not exist and  default  is not  None  ,  default  will be
returned. In any other case, an error reading  path  will be a Tiltfile load
error.

Parameters

    

  * **path** ( ` str  ` ) â Path to the file locally (absolute, or relative to the location of the Tiltfile). 

  * **default** ( ` Optional  ` [ ` List  ` [ ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any  ` ]]]]) â If not  None  and the file at  path  does not exist, this value will be returned. 

Return type

    

` List  ` [ ` Union  ` [ ` Dict  ` [ ` str  ` , ` Any  ` ], ` List  ` [ ` Any
` ]]]

restart_container  (  )  ï

    

**For use with Docker Compose resources only.**

Specify that a container should be restarted when it is live-updated. In
practice, this means that the container re-executes its  ENTRYPOINT  within
the changed filesystem.

May only be included in a  live_update  once, and only as the last step.

For more info (and for the equivalent functionality for Kubernetes resources),
see the [ Live Update Reference ](live_update_reference.html#restarting-your-
process) .

Return type

    

` LiveUpdateStep  `

run  (  _ cmd  _ , _ trigger  =  []  _ , _ echo_off  =  False  _ )  ï

    

Specify that the given  cmd  should be executed when updating an imageâs
container

May not precede any  sync  steps in a  live_update  .

For more info, see the [ Live Update Reference ](live_update_reference.html) .

Parameters

    

  * **cmd** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â Command to run. If a string, executed with ` sh  -c  ` ; if a list, will be passed to the operating system as program name and args. 

  * **trigger** ( ` Union  ` [ ` List  ` [ ` str  ` ], ` str  ` ]) â If the ` trigger  ` argument is specified, the build step is only run when there are changes to the given file(s). Paths relative to Tiltfile. (Note that in addition to matching the trigger, file changes must also match at least one of this Live Updateâs syncs in order to trigger this run. File changes that do not match any syncs will be ignored.) 

  * **bool** â If ` echo_off  ` is set to ` True  ` , the commandâs output will not be echoed to the Tilt UI. 

Return type

    

` LiveUpdateStep  `

secret_settings  (  _ disable_scrub  =  False  _ )  ï

    

Configures Tiltâs handling of Kubernetes Secrets. By default, Tilt scrubs
the text of any Secrets from the logs; e.g. if Tilt applies a Secret with
contents âmysecurepasswordâ, Tilt redacts this string if ever it appears
in the logs, to prevent users from accidentally sharing sensitive information
in snapshots etc.

Parameters

    

**disable_scrub** ( ` bool  ` ) â if True, Tilt will _not_ scrub secrets
from logs.

Return type

    

` None  `

set_team  (  _ team_id  _ )  ï

    

Associates this Tiltfile with the [ team ](teams.html) identified by  team_id
.

Sends usage information to Tilt Cloud periodically.

Return type

    

` None  `

struct  (  _ **  kwargs  _ )  ï

    

Creates an object with arbitrary fields.

Examples:

    
    
    x = struct(a="foo", b=6)
    print("%s %d" % (x.a, x.b)) # prints "foo 6"
    

Return type

    

` Any  `

sync  (  _ local_path  _ , _ remote_path  _ )  ï

    

Specify that any changes to  localPath  should be synced to  remotePath

May not follow any  run  steps in a  live_update  .

For more info, see the [ Live Update Reference ](live_update_reference.html) .

Parameters

    

  * **localPath** â A path relative to the Tiltfileâs directory. Changes to files matching this path will be synced to  remotePath  . Can be a file (in which case just that file will be synced) or directory (in which case any files recursively under that directory will be synced). 

  * **remotePath** â container path to which changes will be synced. Must be absolute. 

Return type

    

` LiveUpdateStep  `

tcp_socket_action  (  _ port  _ , _ host  =  'localhost' _ )  ï

    

Creates a  ` TCPSocketAction  ` for use with a  ` Probe  ` that establishes a
TCP socket connection to determine service readiness.

The probe is successful if a TCP socket can be established within the timeout.
No data is sent or read from the socket.

Parameters

    

  * **host** ( ` str  ` ) â Hostname to use for TCP socket connection. 

  * **port** ( ` int  ` ) â Port to use for TCP socket connection. 

Return type

    

` TCPSocketAction  `

trigger_mode  (  _ trigger_mode  _ )  ï

    

Sets the default  ` TriggerMode  ` for resources in this Tiltfile. (Trigger
mode may still be adjusted per-resource with  ` k8s_resource()  ` .)

If this function is not invoked, the default trigger mode for all resources is
` TRIGGER  MODE  AUTO  ` .

See also: [ Manual Update Control documentation ](manual_update_control.html)

Parameters

    

**trigger_mode** (  ` TriggerMode  ` ) â may be one of ` TRIGGER_MODE_AUTO
` or ` TRIGGER_MODE_MANUAL  `

update_settings  (  _ max_parallel_updates  =  3  _ , _
k8s_upsert_timeout_secs  =  30  _ , _ suppress_unused_image_warnings  =  None
_ )  ï

    

Configures Tiltâs updates to your resources. (An update is any execution of
or change to a resource. Examples of updates include: doing a docker build +
deploy to Kubernetes; running a live update on an existing container; and
executing a local resource command).

Parameters

    

  * **max_parallel_updates** ( ` int  ` ) â maximum number of updates Tilt will execute in parallel. Default is 3. Must be a positive integer. 

  * **k8s_upsert_timeout_secs** ( ` int  ` ) â timeout (in seconds) for Kubernetes upserts (i.e. ` create  ` / ` apply  ` calls). Minimum value is 1. 

  * **suppress_unused_image_warnings** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ], ` None  ` ]) â suppresses warnings about images that arenât deployed. Accepts a list of image names, or â*â to suppress warnings for all images. 

Return type

    

` None  `

version_settings  (  _ check_updates  =  True  _ , _ constraint  =  '' _ )
ï

    

Controls Tiltâs behavior with regard to its own version.

Parameters

    

  * **check_updates** ( ` bool  ` ) â If true, Tilt will check GitHub for new versions of itself and display a notification in the web UI when an upgrade is available. 

  * **constraint** ( ` str  ` ) â 

If non-empty, Tilt will check its currently running version against this
constraint and generate an error if it doesnât match. Examples:

    * <0.17.0  \- less than 0.17.0 

    * >=0.13.2  \- at least 0.13.2 

See more at the [ constraint syntax documentation
](https://github.com/blang/semver#ranges) .

Return type

    

` None  `

warn  (  _ msg  _ )  ï

    

Emits a warning.

Warnings are both displayed in the logs and aggregated as alerts.

Parameters

    

**msg** ( ` str  ` ) â The message.

Return type

    

` None  `

watch_file  (  _ file_path  _ )  ï

    

Watches a file. If the file is changed a re-execution of the Tiltfile is
triggered.

If the path is a directory, its contents will be recursively watched.

Parameters

    

**file_path** ( ` str  ` ) â Path to the file locally (absolute, or relative
to the location of the Tiltfile).

Return type

    

` None  `

watch_settings  (  _ ignore  _ )  ï

    

Configures global watches.

May be called multiple times to add more ignore patterns.

Parameters

    

**ignore** ( ` Union  ` [ ` str  ` , ` List  ` [ ` str  ` ]]) â A string or
list of strings that should not trigger updates. Equivalent to adding patterns
to .tiltignore. Relative patterns are evaluated relative to the current
working dir. See [ Debugging File Changes ](file_changes.html) for more
details.

Return type

    

` None  `

workload_to_resource_function  (  _ fn  _ )  ï

    

Provide a function that will be used to name [ Tilt resources
](tiltfile_concepts.html#resources) .

Tilt will auto-generate resource names for you. If you do not like the names
it generates, you can use this to customize how Tilt generates names.

Example

    
    
    # name all tilt resources after the k8s object namespace + name
    def resource_name(id):
      return id.namespace + '-' + id.name
    workload_to_resource_function(resource_name)
    

The names it generates must be unique (i.e., two workloads canât map to the
same resource name).

Parameters

    

**fn** ( ` Callable  ` [[  ` K8sObjectID  ` ], ` str  ` ]) â A function that
takes a  ` K8sObjectID  ` and returns a  str  . Tilt will call this function
once for each workload to determine that workloadâs resourceâs name.

Return type

    

` None  `

os.  getcwd  (  )  ï

    

Returns a string representation of the current working directory.

The current working directory is the directory containing the currently
executing Tiltfile. If your Tiltfile runs any commands, they run from this
directory.

While calling :meth:load or :meth:include to execute another Tiltfile, returns
the directory of the loaded/included Tiltfile.

Return type

    

` str  `

os.  getenv  (  _ key  _ , _ default  =  None  _ )  ï

    

Return the value of the environment variable key if it exists, or default if
it doesnât.

Parameters

    

  * **key** ( ` str  ` ) â An environment variable name. 

  * **default** â The value to return if the variable doesnât exist. 

Return type

    

` str  `

os.  putenv  (  _ key  _ , _ value  _ )  ï

    

Set the environment variable named key to the string value. Takes effect
immediately in the Tilt process. Any new subprocesses will have this
environment value.

Parameters

    

  * **key** ( ` str  ` ) â An environment variable name. 

  * **value** ( ` str  ` ) â The new value. 

os.  unsetenv  (  _ key  _ , _ value  _ )  ï

    

Delete the environment variable named key. Takes effect immediately in the
Tilt process. Any new subprocesses will not have this variable.

Parameters

    

**key** ( ` str  ` ) â An environment variable name.

os.path.  abspath  (  _ path  _ )  ï

    

Return a normalized, absolute version of the path, relative to the current
working directory.

Parameters

    

**path** ( ` str  ` ) â A filesystem path

Return type

    

` str  `

os.path.  basename  (  _ path  _ )  ï

    

Return the basename of the path.

Parameters

    

**path** ( ` str  ` ) â A filesystem path

Return type

    

` str  `

os.path.  dirname  (  _ path  _ )  ï

    

Return the directory name of the path.

Parameters

    

**path** ( ` str  ` ) â A filesystem path

Return type

    

` str  `

os.path.  exists  (  _ path  _ )  ï

    

Checks if a file or directory exists at the specified path.

Returns false if this is a broken symlink, or if the user doesnât have
permission to stat the file at this path.

On Tilt v0.18.3 and below, watches the path, and reloads the Tiltfile if the
contents change.

On Tilt v0.18.4 and up, does no watching.

Parameters

    

**path** ( ` str  ` ) â A filesystem path

Return type

    

` bool  `

os.path.  join  (  _ path  _ , _ *  paths  _ )  ï

    

Join one or more path components with the OS-specific file separator.

Parameters

    

  * **path** â A filesystem path component 

  * **paths** ( ` str  ` ) â A variable list of components to join 

Return type

    

` str  `

os.path.  realpath  (  _ path  _ )  ï

    

Return the canonical path of the specified filename, eliminating any symbolic
links encountered in the path (if they are supported by the operating system).

Parameters

    

**path** ( ` str  ` ) â A filesystem path

Return type

    

` str  `

os.path.  relpath  (  _ targpath  _ , _ basepath  =  '' _ )  ï

    

Return the path of  targpath  relative to  basepath  (by default, relative to
CWD). On success, the returned path will always be relative to  basepath  ,
even if  basepath  and  targpath  share no elements. An error is raised if
targpath  canât be made relative to  basepath  .

e.g. for the Tiltfile at  /code/Tiltfile  :

  * relpath(â/code/foo/barâ)  â> foo/bar 

  * relpath(â/code/foo/barâ, â/code/fooâ)  â> bar 

  * relpath(â/code/fooâ, â/code/bazâ)  â> ../foo 

  * relpath(â/code/fooâ, âother/pathâ)  â> error 

Parameters

    

  * **targpath** ( ` str  ` ) â Filesystem path to be made relative 

  * **basepath** ( ` str  ` ) â Filesystem path (defaults to the current working directory) 

Return type

    

` str  `

config.  clear_enabled_resources  (  )  ï

    

Tells Tilt that all resources should be disabled. This allows the user to
manually enable only the resources they want once Tilt is running.

Return type

    

` None  `

config.  define_bool  (  _ name  _ , _ args  =  False  _ , _ usage  =  '' _ )
ï

    

Defines a config setting of type  bool  .

Allows the user invoking Tilt to configure a key named ` name  ` to be in the
dict returned by  ` parse()  ` .

For instance, at runtime, to set a flag of this type named  foo  to value
True  , run ` tilt  up  --  --foo  ` . To set a value to ` False  ` , you can
run ` tilt  up  --  --foo=False  ` , or use a default value, e.g.:

    
    
    config.define_bool('foo')
    cfg = config.parse()
    do_stuff = cfg.get('foo', False)
    

See the [ Tiltfile config documentation ](tiltfile_config.html) for examples
and more information.

Parameters

    

  * **name** ( ` str  ` ) â The name of the config setting 

  * **args** ( ` bool  ` ) â 

If False, the config setting is specified by its name. (e.g., if itâs named
âfooâ, ` tilt  up  --  --foo  ` this setting would be ` True  ` .)

If True, the config setting is specified by unnamed positional args. (e.g., in
` tilt  up  --  True  ` , this setting would be ` True  ` .) (This usage
isnât likely to be what you want)

  * **usage** ( ` str  ` ) â When arg parsing fails, what to print for this settingâs description. 

Return type

    

` None  `

config.  define_string  (  _ name  _ , _ args  =  False  _ , _ usage  =  '' _
)  ï

    

Defines a config setting of type  str  .

Allows the user invoking Tilt to configure a key named ` name  ` to be in the
dict returned by  ` parse()  ` .

For instance, at runtime, to set a flag of this type named  foo  to value
âbarâ, run ` tilt  up  --  --foo  bar  ` .

See the [ Tiltfile config documentation ](tiltfile_config.html) for examples
and more information.

Parameters

    

  * **name** ( ` str  ` ) â The name of the config setting 

  * **args** ( ` bool  ` ) â 

If False, the config setting is specified by its name. (e.g., if itâs named
âfooâ, ` tilt  up  --  --foo  bar  ` this setting would be ` "bar" ` .)

If True, the config setting is specified by unnamed positional args. (e.g., in
` tilt  up  --  1  ` , this setting would be ` "1" ` .)

  * **usage** ( ` str  ` ) â When arg parsing fails, what to print for this settingâs description. 

Return type

    

` None  `

config.  define_string_list  (  _ name  _ , _ args  =  False  _ , _ usage  =
'' _ )  ï

    

Defines a config setting of type  List[str]  .

Allows the user invoking Tilt to configure a key named ` name  ` to be in the
dict returned by  ` parse()  ` .

See the [ Tiltfile config documentation ](tiltfile_config.html) for examples
and more information.

Parameters

    

  * **name** ( ` str  ` ) â The name of the config setting 

  * **args** ( ` bool  ` ) â 

If False, the config setting is specified by its name. (e.g., if itâs named
âfooâ, ` tilt  up  --  --foo  bar  ` this setting would be ` ["bar"]  ` .)

If True, the config setting is specified by unnamed positional args. (e.g., in
` tilt  up  --  1  2  3  ` , this setting would be ` ["1" "2" "3"]  ` .)

  * **usage** ( ` str  ` ) â When arg parsing fails, what to print for this settingâs description. 

Return type

    

` None  `

config.  parse  (  )  ï

    

Loads config settings from tilt_config.json, overlays config settings from
Tiltfile command-line args, validates them using the setting definitions
specified in the Tiltfile, and returns a Dict of the resulting settings.

Settings that are defined in the Tiltfile but not specified in the config file
or command-line args will be absent from the dict. Access values via, e.g.,
cfg.get(âfooâ, [âhelloâ])  to have a default value.

Note: by default, Tilt interprets the Tilt command-line args as the names of
Tilt resources to run. When a Tiltfile calls  ` parse()  ` , that behavior is
suppressed, since those args are now managed by :meth:parse. If a Tiltfile
uses  ` parse()  ` and also needs to allow specifying a set of resources to
run, it needs to call  ` set_enabled_resources()  ` .

See the [ Tiltfile config documentation ](tiltfile_config.html) for examples
and more information.

Return type

    

` Dict  ` [ ` str  ` , ` Any  ` ]

Returns

    

A Dict where the keys are settings names and the values are their values.

config.  set_enabled_resources  (  _ resources  _ )  ï

    

Tells Tilt to only run the specified resources. (takes precedence over the
default behavior of ârun the resources specified on the command lineâ)

Calling this with an empty list results in all resources being run.

See the [ Tiltfile config documentation ](tiltfile_config.html) for examples
and more information.

Parameters

    

**resources** ( ` List  ` [ ` str  ` ]) â The names of the resources to run,
or an empty list to run them all.

Return type

    

` None  `

shlex.  quote  (  _ s  _ )  ï

    

Returns a shell-escaped version of ` s  ` , which can be safely interpolated
as a single token in a shell command.

e.g.:

    
    
    mystring = "foo's bar"
    
    # bad - runs: `docker run -e foo=foo's bar myimage` (invalid shell - unmatched ')
    local('docker run -e foo=%s myimage' % mystring)
    
    # good - runs: `docker run -e foo='foo'"'"'s bar' myimage`
    #        which correctly sets $foo to "foo's bar"
    local('docker run -e foo=%s myimage' % shlex.quote(mystring))
    

Return type

    

` str  `

v1alpha1.  cmd  (  _ name  _ , _ labels  =  None  _ , _ annotations  =  None
_ , _ args  =  None  _ , _ dir  =  '' _ , _ env  =  None  _ , _
readiness_probe  =  None  _ , _ restart_on  =  None  _ , _ start_on  =  None
_ , _ disable_source  =  None  _ )  ï

    

Cmd represents a process on the host machine.

When the process exits, we will make a best-effort attempt (within OS
limitations) to kill any spawned descendant processes.

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **args** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â Command-line arguments. Must have length at least 1. 

  * **dir** ( ` str  ` ) â 

Process working directory.

If the working directory is not specified, the command is run in the default
Tilt working directory.

  * **env** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

Additional variables process environment.

Expressed as a C-style array of strings of the form [âKEY1=VALUE1â,
âKEY2=VALUE2â, â¦].

Environment variables are layered on top of the environment variables that
Tilt runs with.

  * **readiness_probe** ( ` Optional  ` [  ` Probe  ` ]) â Periodic probe of service readiness. 

  * **restart_on** ( ` Optional  ` [  ` RestartOnSpec  ` ]) â 

Indicates objects that can trigger a restart of this command.

When a restart is triggered, Tilt will try to gracefully shutdown any
currently running process, waiting for it to exit before starting a new
process. If the process doesnât shutdown within the allotted time, Tilt will
kill the process abruptly.

Restarts can happen even if the command is already done.

Logs of the current process after the restart are discarded.

  * **start_on** ( ` Optional  ` [  ` StartOnSpec  ` ]) â 

Indicates objects that can trigger a start/restart of this command.

Restarts behave the same as RestartOn. The key difference is that a Cmd with
any StartOn triggers will not have its command run until its StartOn is
satisfied.

  * **disable_source** ( ` Optional  ` [  ` DisableSource  ` ]) â Specifies how to disable this. 

v1alpha1.  config_map  (  _ name  _ , _ labels  =  None  _ , _ annotations  =
None  _ , _ data  =  None  _ )  ï

    

ConfigMap stores unstructured data that other controllers can read and write.

Useful for sharing data from one system and subscribing to it from another.

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **data** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â Data contains the configuration data. Each key must consist of alphanumeric characters, â-â, â_â or â.â. 

v1alpha1.  config_map_disable_source  (  _ name  =  '' _ , _ key  =  '' _ )
ï

    

Specifies a ConfigMap to control a DisableSource

Parameters

    

  * **name** ( ` str  ` ) â The name of the ConfigMap 

  * **key** ( ` str  ` ) â The key where the enable/disable state is stored. 

Return type

    

` ConfigMapDisableSource  `

v1alpha1.  disable_source  (  _ config_map  =  None  _ )  ï

    

Points at a thing that can control whether something is disabled

Parameters

    

**config_map** ( ` Optional  ` [  ` ConfigMapDisableSource  ` ]) â This
DisableSource is controlled by a ConfigMap

Return type

    

` DisableSource  `

v1alpha1.  exec_action  (  _ command  =  None  _ )  ï

    

ExecAction describes a ârun in containerâ action.

Parameters

    

**command** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â Command is the
command line to execute inside the container, the working directory for the
command is root (â/â) in the containerâs filesystem. The command is
simply execâd, it is not run inside a shell, so traditional shell
instructions (â|â, etc) wonât work. To use a shell, you need to
explicitly call out to that shell. Exit status of 0 is treated as live/healthy
and non-zero is unhealthy.

Return type

    

` ExecAction  `

v1alpha1.  extension  (  _ name  _ , _ labels  =  None  _ , _ annotations  =
None  _ , _ repo_name  =  '' _ , _ repo_path  =  '' _ , _ args  =  None  _ )
ï

    

Extension defines an extension thatâs evaluated on Tilt startup.

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **repo_name** ( ` str  ` ) â 

RepoName specifies the ExtensionRepo object where we should find this
extension.

The Extension controller should watch for changes to this repo, and may update
if this repo is deleted or moved.

  * **repo_path** ( ` str  ` ) â 

RepoPath specifies the path to the extension directory inside the repo.

Once the repo is downloaded, this path should point to a directory with a
Tiltfile as the main âentrypointâ of the extension.

  * **args** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

Arguments to the Tiltfile loaded by this extension.

Arguments can be positional ([âaâ, âbâ, âcâ]) or flag-based
(ââto-edit=aâ). By default, a list of arguments indicates the list of
services in the tiltfile that should be enabled.

v1alpha1.  extension_repo  (  _ name  _ , _ labels  =  None  _ , _ annotations
=  None  _ , _ url  =  '' _ , _ ref  =  '' _ )  ï

    

ExtensionRepo specifies a repo or folder where a set of extensions live.

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **url** ( ` str  ` ) â 

The URL of the repo.

Allowed: https: URLs that point to a public git repo file: URLs that point to
a location on disk.

  * **ref** ( ` str  ` ) â A reference to sync the repo to. If empty, Tilt will always update the repo to the latest version. 

v1alpha1.  file_watch  (  _ name  _ , _ labels  =  None  _ , _ annotations  =
None  _ , _ watched_paths  =  None  _ , _ ignores  =  None  _ , _
disable_source  =  None  _ )  ï

    

FileWatch

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **watched_paths** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â WatchedPaths are paths of directories or files to watch for changes to. It cannot be empty. 

  * **ignores** ( ` Optional  ` [ ` List  ` [  ` IgnoreDef  ` ]]) â Ignores are optional rules to filter out a subset of changes matched by WatchedPaths. 

  * **disable_source** ( ` Optional  ` [  ` DisableSource  ` ]) â Specifies how to disable this. 

v1alpha1.  forward  (  _ local_port  =  0  _ , _ container_port  =  0  _ , _
host  =  '' _ )  ï

    

Forward defines a port forward to execute on a given pod.

Parameters

    

  * **local_port** ( ` int  ` ) â 

The port to expose on the current machine.

If not specified (or 0), a random free port will be chosen and can be
discovered via the status once established.

  * **container_port** ( ` int  ` ) â The port on the Kubernetes pod to connect to. Required. 

  * **host** ( ` str  ` ) â Optional host to bind to on the current machine (localhost by default) 

Return type

    

` Forward  `

v1alpha1.  handler  (  _ exec  =  None  _ , _ http_get  =  None  _ , _
tcp_socket  =  None  _ )  ï

    

Handler defines a specific action that should be taken in a probe.

Parameters

    

  * **exec** ( ` Optional  ` [  ` ExecAction  ` ]) â One and only one of the following should be specified. Exec specifies the action to take. 

  * **http_get** ( ` Optional  ` [  ` HTTPGetAction  ` ]) â HTTPGet specifies the http request to perform. 

  * **tcp_socket** ( ` Optional  ` [  ` TCPSocketAction  ` ]) â TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported TODO: implement a realistic TCP lifecycle hook 

Return type

    

` Handler  `

v1alpha1.  http_get_action  (  _ path  =  '' _ , _ port  =  0  _ , _ host  =
'' _ , _ scheme  =  '' _ , _ http_headers  =  None  _ )  ï

    

HTTPGetAction describes an action based on HTTP Get requests.

Parameters

    

  * **path** ( ` str  ` ) â Path to access on the HTTP server. 

  * **port** ( ` int  ` ) â Name or number of the port to access on the container. Number must be in the range 1 to 65535. 

  * **host** ( ` str  ` ) â Host name to connect to, defaults to the pod IP. You probably want to set âHostâ in httpHeaders instead. 

  * **scheme** ( ` str  ` ) â Scheme to use for connecting to the host. Defaults to HTTP. 

  * **http_headers** ( ` Optional  ` [ ` List  ` [  ` HTTPHeader  ` ]]) â Custom headers to set in the request. HTTP allows repeated headers. 

Return type

    

` HTTPGetAction  `

v1alpha1.  http_header  (  _ name  =  '' _ , _ value  =  '' _ )  ï

    

HTTPHeader describes a custom header to be used in HTTP probes

Parameters

    

  * **name** ( ` str  ` ) â The header field name 

  * **value** ( ` str  ` ) â The header field value 

Return type

    

` HTTPHeader  `

v1alpha1.  ignore_def  (  _ base_path  =  '' _ , _ patterns  =  None  _ )  ï

    

Describes sets of file paths that the FileWatch should ignore.

Parameters

    

  * **base_path** ( ` str  ` ) â 

BasePath is the base path for the patterns. It cannot be empty.

If no patterns are specified, everything under it will be recursively ignored.

  * **patterns** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

Patterns are dockerignore style rules. Absolute-style patterns will be rooted
to the BasePath.

See [ https://docs.docker.com/engine/reference/builder/#dockerignore-file
](https://docs.docker.com/engine/reference/builder/#dockerignore-file) .

Return type

    

` IgnoreDef  `

v1alpha1.  kubernetes_apply  (  _ name  _ , _ labels  =  None  _ , _
annotations  =  None  _ , _ yaml  =  '' _ , _ image_maps  =  None  _ , _
image_locators  =  None  _ , _ timeout  =  '' _ , _
kubernetes_discovery_template_spec  =  None  _ , _ port_forward_template_spec
=  None  _ , _ pod_log_stream_template_spec  =  None  _ , _ discovery_strategy
=  '' _ , _ disable_source  =  None  _ , _ cmd  =  None  _ , _ restart_on  =
None  _ )  ï

    

KubernetesApply specifies a blob of YAML to apply, and a set of ImageMaps that
the YAML depends on.

The KubernetesApply controller will resolve the ImageMaps into immutable image
references. The controller will process the spec YAML, then apply it to the
cluster. Those processing steps might include:

  * Injecting the resolved image references. 

  * Adding custom labels so that Tilt can track the progress of the apply. 

  * Modifying image pull rules to ensure the image is pulled correctly. 

The controller wonât apply anything until all ImageMaps resolve to real
images.

The controller will watch all the image maps, and redeploy the entire YAML if
any of the maps resolve to a new image.

The status field will contain both the raw applied object, and derived fields
to help other controllers figure out how to watch the apply progress.

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **yaml** ( ` str  ` ) â 

YAML to apply to the cluster.

Exactly one of YAML OR Cmd MUST be provided.

  * **image_maps** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

Names of image maps that this applier depends on.

The controller will watch all the image maps, and redeploy the entire YAML if
any of the maps resolve to a new image.

  * **image_locators** ( ` Optional  ` [ ` List  ` [  ` KubernetesImageLocator  ` ]]) â 

Descriptors of how to find images in the YAML.

Needed when injecting images into CRDs.

  * **timeout** ( ` str  ` ) â 

The timeout on the apply operation.

Weâve had problems with both: 1) CRD apiservers that take an arbitrarily
long time to apply, and 2) Infinite loops in the apimachinery So we offer the
ability to set a timeout on Kubernetes apply operations.

The default timeout is 30s.

  * **kubernetes_discovery_template_spec** ( ` Optional  ` [ ` KubernetesDiscoveryTemplateSpec  ` ]) â 

KubernetesDiscoveryTemplateSpec describes how we discover pods for resources
created by this Apply.

If not specified, the KubernetesDiscovery controller will listen to all pods,
and follow owner references to find the pods owned by these resources.

  * **port_forward_template_spec** ( ` Optional  ` [  ` PortForwardTemplateSpec  ` ]) â 

PortForwardTemplateSpec describes the data model for port forwards that
KubernetesApply should set up.

Underneath the hood, weâll create a KubernetesDiscovery object that finds
the pods and sets up the port-forwarding. Only one PortForward will be active
at a time.

  * **pod_log_stream_template_spec** ( ` Optional  ` [  ` PodLogStreamTemplateSpec  ` ]) â 

PodLogStreamTemplateSpec describes the data model for PodLogStreams that
KubernetesApply should set up.

Underneath the hood, weâll create a KubernetesDiscovery object that finds
the pods and sets up the pod log streams.

If no template is specified, the controller will stream all pod logs available
from the apiserver.

  * **discovery_strategy** ( ` str  ` ) â DiscoveryStrategy describes how we set up pod watches for the applied resources. This affects all systems that attach to pods, including PortForwards, PodLogStreams, resource readiness, and live-updates. 

  * **disable_source** ( ` Optional  ` [  ` DisableSource  ` ]) â Specifies how to disable this. 

  * **cmd** ( ` Optional  ` [ ` KubernetesApplyCmd  ` ]) â 

Cmd is a custom command to generate the YAML to apply.

The Cmd MUST return valid Kubernetes YAML for the entities it applied to the
cluster.

Exactly one of YAML OR Cmd MUST be provided.

  * **restart_on** ( ` Optional  ` [  ` RestartOnSpec  ` ]) â RestartOn determines external triggers that will result in an apply. 

v1alpha1.  kubernetes_apply_cmd  (  _ args  =  None  _ , _ dir  =  '' _ , _
env  =  None  _ )  ï

    

Parameters

    

  * **args** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â Args are the command-line arguments for the apply command. Must have length >= 1. 

  * **dir** ( ` str  ` ) â 

Process working directory.

If not specified, will default to Tilt working directory.

  * **env** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

Env are additional variables for the process environment.

Environment variables are layered on top of the environment variables that
Tilt runs with.

Return type

    

` KubernetesApplyCmd  `

v1alpha1.  kubernetes_discovery  (  _ name  _ , _ labels  =  None  _ , _
annotations  =  None  _ , _ watches  =  None  _ , _ extra_selectors  =  None
_ , _ port_forward_template_spec  =  None  _ , _ pod_log_stream_template_spec
=  None  _ )  ï

    

KubernetesDiscovery

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **watches** ( ` Optional  ` [ ` List  ` [  ` KubernetesWatchRef  ` ]]) â 

Watches determine what resources are discovered.

If a discovered resource (e.g. Pod) matches the KubernetesWatchRef UID
exactly, it will be reported. If a discovered resource is transitively owned
by the KubernetesWatchRef UID, it will be reported.

  * **extra_selectors** ( ` Optional  ` [ ` List  ` [ ` LabelSelector  ` ]]) â 

ExtraSelectors are label selectors that will force discovery of a Pod even if
it does not match the AncestorUID.

This should only be necessary in the event that a CRD creates Pods but does
not set an owner reference to itself.

  * **port_forward_template_spec** ( ` Optional  ` [  ` PortForwardTemplateSpec  ` ]) â 

PortForwardTemplateSpec describes the data model for port forwards that
KubernetesDiscovery should set up.

The KubernetesDiscovery controller will choose a âbestâ candidate for
attaching the port-forwarding. Only one PortForward will be active at a time.

  * **pod_log_stream_template_spec** ( ` Optional  ` [  ` PodLogStreamTemplateSpec  ` ]) â 

PodLogStreamTemplateSpec describes the data model for PodLogStreams that
KubernetesDiscovery should set up.

The KubernetesDiscovery controller will attach PodLogStream objects to all
active pods it discovers.

If no template is specified, the controller will stream all pod logs available
from the apiserver.

v1alpha1.  kubernetes_discovery_template_spec  (  _ extra_selectors  =  None
_ )  ï

    

Parameters

    

**extra_selectors** ( ` Optional  ` [ ` List  ` [ ` LabelSelector  ` ]]) â

ExtraSelectors are label selectors that will force discovery of a Pod even if
it does not match the AncestorUID.

This should only be necessary in the event that a CRD creates Pods but does
not set an owner reference to itself.

Return type

    

` KubernetesDiscoveryTemplateSpec  `

v1alpha1.  kubernetes_image_locator  (  _ object_selector  =  None  _ , _ path
=  '' _ , _ object  =  None  _ )  ï

    

Finds image references in Kubernetes YAML.

Parameters

    

  * **object_selector** ( ` Optional  ` [  ` ObjectSelector  ` ]) â Selects which objects to look in. 

  * **path** ( ` str  ` ) â 

A JSON path to the image reference field.

If Object is empty, the field should be a string.

If Object is non-empty, the field should be an object with subfields.

  * **object** ( ` Optional  ` [ ` KubernetesImageObjectDescriptor  ` ]) â A descriptor of the path and structure of an object that describes an image reference. This is a common way to describe images in CRDs, breaking them down into an object rather than an image reference string. 

Return type

    

` KubernetesImageLocator  `

v1alpha1.  kubernetes_image_object_descriptor  (  _ repo_field  =  '' _ , _
tag_field  =  '' _ )  ï

    

Parameters

    

  * **repo_field** ( ` str  ` ) â The name of the field that contains the image repository. 

  * **tag_field** ( ` str  ` ) â The name of the field that contains the image tag. 

Return type

    

` KubernetesImageObjectDescriptor  `

v1alpha1.  kubernetes_watch_ref  (  _ uid  =  '' _ , _ namespace  =  '' _ , _
name  =  '' _ )  ï

    

KubernetesWatchRef is similar to v1.ObjectReference from the Kubernetes API
and is used to determine what objects should be reported on based on
discovery.

Parameters

    

  * **uid** ( ` str  ` ) â 

UID is a Kubernetes object UID.

It should either be the exact object UID or the transitive owner.

  * **namespace** ( ` str  ` ) â Namespace is the Kubernetes namespace for discovery. Required. 

  * **name** ( ` str  ` ) â 

Name is the Kubernetes object name.

This is not directly used in discovery; it is extra metadata.

Return type

    

` KubernetesWatchRef  `

v1alpha1.  label_selector  (  _ match_labels  =  None  _ , _ match_expressions
=  None  _ )  ï

    

Parameters

    

  * **match_labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is âkeyâ, the operator is âInâ, and the values array contains only âvalueâ. The requirements are ANDed. 

  * **match_expressions** ( ` Optional  ` [ ` List  ` [ ` LabelSelectorRequirement  ` ]]) â matchExpressions is a list of label selector requirements. The requirements are ANDed. 

Return type

    

` LabelSelector  `

v1alpha1.  label_selector_requirement  (  _ key  =  '' _ , _ operator  =  '' _
, _ values  =  None  _ )  ï

    

Parameters

    

  * **key** ( ` str  ` ) â key is the label key that the selector applies to. 

  * **operator** ( ` str  ` ) â operator represents a keyâs relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. 

  * **values** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. 

Return type

    

` LabelSelectorRequirement  `

v1alpha1.  object_selector  (  _ api_version_regexp  =  '' _ , _ kind_regexp
=  '' _ , _ name_regexp  =  '' _ , _ namespace_regexp  =  '' _ )  ï

    

Selector for any Kubernetes-style API.

Parameters

    

  * **api_version_regexp** ( ` str  ` ) â A regular expression apiVersion match. 

  * **kind_regexp** ( ` str  ` ) â A regular expression kind match. 

  * **name_regexp** ( ` str  ` ) â A regular expression name match. 

  * **namespace_regexp** ( ` str  ` ) â A regular expression namespace match. 

Return type

    

` ObjectSelector  `

v1alpha1.  pod_log_stream_template_spec  (  _ only_containers  =  None  _ , _
ignore_containers  =  None  _ )  ï

    

PodLogStreamTemplateSpec describes common attributes for PodLogStreams that
can be shared across pods.

Parameters

    

  * **only_containers** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

The names of containers to include in the stream.

If  onlyContainers  and  ignoreContainers  are not set, will watch all
containers in the pod.

  * **ignore_containers** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â 

The names of containers to exclude from the stream.

If  onlyContainers  and  ignoreContainers  are not set, will watch all
containers in the pod.

Return type

    

` PodLogStreamTemplateSpec  `

v1alpha1.  port_forward_template_spec  (  _ forwards  =  None  _ )  ï

    

PortForwardTemplateSpec describes common attributes for PortForwards that can
be shared across pods.

Parameters

    

**forwards** ( ` Optional  ` [ ` List  ` [  ` Forward  ` ]]) â One or more
port forwards to execute on the given pod. Required.

Return type

    

` PortForwardTemplateSpec  `

v1alpha1.  probe  (  _ handler  =  None  _ , _ initial_delay_seconds  =  0  _
, _ timeout_seconds  =  0  _ , _ period_seconds  =  0  _ , _ success_threshold
=  0  _ , _ failure_threshold  =  0  _ )  ï

    

Probe describes a health check to be performed to determine whether it is
alive or ready to receive traffic.

Parameters

    

  * **handler** ( ` Optional  ` [  ` Handler  ` ]) â The action taken to determine the health of a container 

  * **initial_delay_seconds** ( ` int  ` ) â Number of seconds after the container has started before liveness probes are initiated. More info: [ https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes ](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes)

  * **timeout_seconds** ( ` int  ` ) â Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: [ https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes ](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes)

  * **period_seconds** ( ` int  ` ) â How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. 

  * **success_threshold** ( ` int  ` ) â Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. 

  * **failure_threshold** ( ` int  ` ) â Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. 

Return type

    

` Probe  `

v1alpha1.  restart_on_spec  (  _ file_watches  =  None  _ , _ ui_buttons  =
None  _ )  ï

    

RestartOnSpec indicates the set of objects that can trigger a restart of this
object.

Parameters

    

  * **file_watches** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â FileWatches that can trigger a restart. 

  * **ui_buttons** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â UIButtons that can trigger a restart. 

Return type

    

` RestartOnSpec  `

v1alpha1.  start_on_spec  (  _ ui_buttons  =  None  _ )  ï

    

StartOnSpec indicates the set of objects that can trigger a start/restart of
this object.

Parameters

    

**ui_buttons** ( ` Optional  ` [ ` List  ` [ ` str  ` ]]) â UIButtons that
can trigger a start/restart.

Return type

    

` StartOnSpec  `

v1alpha1.  tcp_socket_action  (  _ port  =  0  _ , _ host  =  '' _ )  ï

    

TCPSocketAction describes an action based on opening a socket

Parameters

    

  * **port** ( ` int  ` ) â Number or name of the port to access on the container. Number must be in the range 1 to 65535. 

  * **host** ( ` str  ` ) â Optional: Host name to connect to, defaults to the pod IP. 

Return type

    

` TCPSocketAction  `

v1alpha1.  ui_bool_input_spec  (  _ default_value  =  False  _ , _ true_string
=  None  _ , _ false_string  =  None  _ )  ï

    

Describes a boolean checkbox input field attached to a button.

Parameters

    

  * **default_value** ( ` bool  ` ) â Whether the input is initially true or false. 

  * **true_string** ( ` Optional  ` [ ` str  ` ]) â If the inputâs value is converted to a string, use this when the value is true. If unspecified, its string value will be  âtrueâ 

  * **false_string** ( ` Optional  ` [ ` str  ` ]) â If the inputâs value is converted to a string, use this when the value is false. If unspecified, its string value will be  âfalseâ 

Return type

    

` UIBoolInputSpec  `

v1alpha1.  ui_button  (  _ name  _ , _ labels  =  None  _ , _ annotations  =
None  _ , _ location  =  None  _ , _ text  =  '' _ , _ icon_name  =  '' _ , _
icon_svg  =  '' _ , _ disabled  =  False  _ , _ requires_confirmation  =
False  _ , _ inputs  =  None  _ )  ï

    

UIButton

Parameters

    

  * **name** ( ` str  ` ) â The name in the Object metadata. 

  * **labels** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for grouping objects. 

  * **annotations** ( ` Optional  ` [ ` Dict  ` [ ` str  ` , ` str  ` ]]) â A set of key/value pairs in the Object metadata for attaching data to objects. 

  * **location** ( ` Optional  ` [  ` UIComponentLocation  ` ]) â Location associates the button with another component for layout. 

  * **text** ( ` str  ` ) â Text to appear on the button itself or as hover text (depending on button location). 

  * **icon_name** ( ` str  ` ) â 

IconName is a Material Icon to appear next to button text or on the button
itself (depending on button location).

Valid values are icon font ligature names from the Material Icons set. See [
https://fonts.google.com/icons ](https://fonts.google.com/icons) for the full
list of available icons.

If both IconSVG and IconName are specified, IconSVG will take precedence.

  * **icon_svg** ( ` str  ` ) â 

IconSVG is an SVG to use as the icon to appear next to button text or on the
button itself (depending on button location).

This should be an <svg> element scaled for a 24x24 viewport.

If both IconSVG and IconName are specified, IconSVG will take precedence.

  * **disabled** ( ` bool  ` ) â If true, the button will be rendered, but with an effect indicating itâs disabled. It will also be unclickable. 

  * **requires_confirmation** ( ` bool  ` ) â If true, the UI will require the user to click the button a second time to confirm before taking action 

  * **inputs** ( ` Optional  ` [ ` List  ` [  ` UIInputSpec  ` ]]) â Any inputs for this button. 

v1alpha1.  ui_component_location  (  _ component_id  =  '' _ , _
component_type  =  '' _ )  ï

    

UIComponentLocation specifies where to put a UI component.

Parameters

    

  * **component_id** ( ` str  ` ) â 

ComponentID is the identifier of the parent component to associate this
component with.

For example, this is a resource name if the ComponentType is Resource.

  * **component_type** ( ` str  ` ) â ComponentType is the type of the parent component. 

Return type

    

` UIComponentLocation  `

v1alpha1.  ui_hidden_input_spec  (  _ value  =  '' _ )  ï

    

Describes a hidden input field attached to a button, with a value to pass on
any submit.

Parameters

    

**value** ( ` str  ` ) â Documentation missing

Return type

    

` UIHiddenInputSpec  `

v1alpha1.  ui_input_spec  (  _ name  =  '' _ , _ label  =  '' _ , _ text  =
None  _ , _ bool  =  None  _ , _ hidden  =  None  _ )  ï

    

Defines an Input to render in the UI. If UIButton is analogous to an HTML
<form>, UIInput is analogous to an HTML <input>.

Parameters

    

  * **name** ( ` str  ` ) â Name of this input. Must be unique within the UIButton. 

  * **label** ( ` str  ` ) â A label to display next to this input in the UI. 

  * **text** ( ` Optional  ` [  ` UITextInputSpec  ` ]) â A Text input that takes a string. 

  * **bool** ( ` Optional  ` [  ` UIBoolInputSpec  ` ]) â A Bool input that is true or false 

  * **hidden** ( ` Optional  ` [  ` UIHiddenInputSpec  ` ]) â An input that has a constant value and does not display to the user 

Return type

    

` UIInputSpec  `

v1alpha1.  ui_text_input_spec  (  _ default_value  =  '' _ , _ placeholder  =
'' _ )  ï

    

Describes a text input field attached to a button.

Parameters

    

  * **default_value** ( ` str  ` ) â Initial value for this field. 

  * **placeholder** ( ` str  ` ) â A short hint that describes the expected input of this field. 

Return type

    

` UITextInputSpec  `

* * *

## Types

  * Blob
  * ExecAction
  * HTTPGetAction
  * K8sObjectID
  * Link
  * LiveUpdateStep
  * PortForward
  * Probe
  * TCPSocketAction
  * TriggerMode
  * v1alpha1.ConfigMapDisableSource
  * v1alpha1.DisableSource
  * v1alpha1.ExecAction
  * v1alpha1.Forward
  * v1alpha1.HTTPGetAction
  * v1alpha1.HTTPHeader
  * v1alpha1.Handler
  * v1alpha1.IgnoreDef
  * v1alpha1.KubernetesImageLocator
  * v1alpha1.KubernetesWatchRef
  * v1alpha1.ObjectSelector
  * v1alpha1.PodLogStreamTemplateSpec
  * v1alpha1.PortForwardTemplateSpec
  * v1alpha1.Probe
  * v1alpha1.RestartOnSpec
  * v1alpha1.StartOnSpec
  * v1alpha1.TCPSocketAction
  * v1alpha1.UIBoolInputSpec
  * v1alpha1.UIComponentLocation
  * v1alpha1.UIHiddenInputSpec
  * v1alpha1.UIInputSpec
  * v1alpha1.UITextInputSpec

* * *

_ class  _ Blob  ï

    

The result of executing a command on your local system.

Under the hood, a  Blob  is just a string, but we wrap it this way so Tilt
knows the difference between a string meant to convey content and a string
indicating, say, a filepath.

To wrap a string as a blob, call ` blob(my_str)  `

_ class  _ ExecAction  ï

    

Specification for a command to execute that determines resource readiness.

For details, see the  ` probe()  ` and  ` exec_action()  ` functions.

_ class  _ HTTPGetAction  ï

    

Specification for a HTTP GET request to perform that determines resource
readiness.

For details, see the  ` probe()  ` and  ` http_get_action()  ` functions.

_ class  _ K8sObjectID  ï

    

name  ï

    

The objectâs name (e.g.,  âmy-serviceâ  )

Type

    

str

kind  ï

    

The objectâs kind (e.g.,  âdeploymentâ  )

Type

    

str

namespace  ï

    

The objectâs namespace (e.g.,  âdefaultâ  )

Type

    

str

group  ï

    

The objectâs group (e.g.,  âappsâ  )

Type

    

str

_ class  _ Link  ï

    

Specifications for a link associated with a resource in the Web UI.

For details, see the  ` link()  ` method.

_ class  _ LiveUpdateStep  ï

    

A step in the process of performing a LiveUpdate on an imageâs container.

For details, see the [ Live Update documentation ](live_update_reference.html)
.

_ class  _ PortForward  ï

    

Specifications for setting up and displaying a Kubernetes port-forward.

For details, see the  ` port_forward()  ` method.

_ class  _ Probe  ï

    

Specification for a resource readiness check.

For details, see the  ` probe()  ` function.

_ class  _ TCPSocketAction  ï

    

Specification for a TCP socket connection to perform that determines resource
readiness.

For details, see the  ` probe()  ` and  ` tcp_socket_action()  ` functions.

_ class  _ TriggerMode  ï

    

A set of constants that describe how Tilt triggers an update for a resource.
Possible values are:

  * ` TRIGGER_MODE_AUTO  ` : the default. When Tilt detects a change to files or config files associated with this resource, it triggers an update. 

  * ` TRIGGER_MODE_MANUAL  ` : user manually triggers update for dirty resources (i.e. resources with pending changes) via a button in the UI. (Note that the initial build always occurs automatically.) 

The default trigger mode for all manifests may be set with the top-level
function  ` trigger_mode()  ` (if not set, defaults to ` TRIGGER_MODE_AUTO  `
), and per-resource with  ` k8s_resource()  ` /  ` dc_resource()  ` .

See also: [ Manual Update Control documentation ](manual_update_control.html)

_ class  _ v1alpha1.  ConfigMapDisableSource  ï

    

Specifies a ConfigMap to control a DisableSource

_ class  _ v1alpha1.  DisableSource  ï

    

Points at a thing that can control whether something is disabled

_ class  _ v1alpha1.  ExecAction  ï

    

ExecAction describes a ârun in containerâ action.

_ class  _ v1alpha1.  Forward  ï

    

Forward defines a port forward to execute on a given pod.

_ class  _ v1alpha1.  HTTPGetAction  ï

    

HTTPGetAction describes an action based on HTTP Get requests.

_ class  _ v1alpha1.  HTTPHeader  ï

    

HTTPHeader describes a custom header to be used in HTTP probes

_ class  _ v1alpha1.  Handler  ï

    

Handler defines a specific action that should be taken in a probe.

_ class  _ v1alpha1.  IgnoreDef  ï

    

Describes sets of file paths that the FileWatch should ignore.

_ class  _ v1alpha1.  KubernetesImageLocator  ï

    

Finds image references in Kubernetes YAML.

_ class  _ v1alpha1.  KubernetesWatchRef  ï

    

KubernetesWatchRef is similar to v1.ObjectReference from the Kubernetes API
and is used to determine what objects should be reported on based on
discovery.

_ class  _ v1alpha1.  ObjectSelector  ï

    

Selector for any Kubernetes-style API.

_ class  _ v1alpha1.  PodLogStreamTemplateSpec  ï

    

PodLogStreamTemplateSpec describes common attributes for PodLogStreams that
can be shared across pods.

_ class  _ v1alpha1.  PortForwardTemplateSpec  ï

    

PortForwardTemplateSpec describes common attributes for PortForwards that can
be shared across pods.

_ class  _ v1alpha1.  Probe  ï

    

Probe describes a health check to be performed to determine whether it is
alive or ready to receive traffic.

_ class  _ v1alpha1.  RestartOnSpec  ï

    

RestartOnSpec indicates the set of objects that can trigger a restart of this
object.

_ class  _ v1alpha1.  StartOnSpec  ï

    

StartOnSpec indicates the set of objects that can trigger a start/restart of
this object.

_ class  _ v1alpha1.  TCPSocketAction  ï

    

TCPSocketAction describes an action based on opening a socket

_ class  _ v1alpha1.  UIBoolInputSpec  ï

    

Describes a boolean checkbox input field attached to a button.

_ class  _ v1alpha1.  UIComponentLocation  ï

    

UIComponentLocation specifies where to put a UI component.

_ class  _ v1alpha1.  UIHiddenInputSpec  ï

    

Describes a hidden input field attached to a button, with a value to pass on
any submit.

_ class  _ v1alpha1.  UIInputSpec  ï

    

Defines an Input to render in the UI. If UIButton is analogous to an HTML
<form>, UIInput is analogous to an HTML <input>.

_ class  _ v1alpha1.  UITextInputSpec  ï

    

Describes a text input field attached to a button.

* * *

## Data

  * __file__
  * os.environ
  * os.name
  * config.main_dir
  * config.main_path
  * config.tilt_subcommand
  * sys.argv
  * sys.executable

* * *

__file__  _ :  str  _ _ =  '' _ ï

    

The path of the Tiltfile. Set as a local variable in each Tiltfile as it
loads.

os.  environ  ï

    

A dictionary of your environment variables.

For example, ` os.environ['HOME']  ` is usually your home directory.

Captured each time the Tiltfile begins execution.

Tiltfile dictionaries support many of the same methods as Python dictionaries,
including:

  * dict.get(key, default) 

  * dict.items() 

See the [ Starlark spec
](https://github.com/bazelbuild/starlark/blob/master/spec.md#built-in-methods)
for more.

alias of ` Dict  ` [ ` str  ` , ` str  ` ]

os.  name  _ :  str  _ _ =  '' _ ï

    

The name of the operating system. âposixâ (for Linux and MacOS) or
ântâ (for Windows).

Designed for consistency with [ os.name in Python
](https://docs.python.org/3/library/os.html#os.name) .

config.  main_dir  _ :  str  _ _ =  '' _ ï

    

The absolute directory of the main Tiltfile.

Often used to determine the location of vendored code and caches.

config.  main_path  _ :  str  _ _ =  '' _ ï

    

The absolute path of the main Tiltfile.

config.  tilt_subcommand  _ :  str  _ _ =  '' _ ï

    

The sub-command with which  tilt  was invoked. Does not include extra args or
options.

Examples:

  * run  tilt down  -> config.tilt_subcommand == âdownâ 

  * run  tilt up frontend backend  -> config.tilt_subcommand == âupâ 

  * run  tilt alpha tiltfile-result  -> config.tilt_subcommand == âalpha tiltfile-resultâ 

sys.  argv  _ :  List  [  str  ]  _ _ =  []  _ ï

    

The list of command line arguments passed to Tilt on start.

argv[0]  is the Tilt binary name.

sys.  executable  _ :  str  _ _ =  '' _ ï

    

A string giving the absolute path of the Tilt binary.

Based on how Tilt was originally invoked. There is no guarantee that the path
is still pointing to a valid Tilt binary. If the path has a symlink, the
behavior is operating system dependent.

* * *

## Extensions

Canât find what youâre looking for in this reference?

Tilt users can contribute [extensions](extensions.html) to share with other
users. Browse them for examples of what you can do with a Tiltfile. Load them
into your own Tiltfile. Includes:

  * [`api_server_logs`](https://github.com/tilt-dev/tilt-extensions/tree/master/api_server_logs): Print API server logs. Example from [Contribute an Extension](https://docs.tilt.dev/contribute_extension.html).
  * [`cancel`](https://github.com/tilt-dev/tilt-extensions/tree/master/cancel): Adds a cancel button to the UI.
  * [`cert_manager`](https://github.com/tilt-dev/tilt-extensions/tree/master/cert_manager): Deploys cert-manager.
  * [`color`](https://github.com/tilt-dev/tilt-extensions/tree/master/color): Allows colorful log prints.
  * [`configmap`](https://github.com/tilt-dev/tilt-extensions/tree/master/configmap): Create configmaps from files and auto-deploy them.
  * [`conftest`](https://github.com/tilt-dev/tilt-extensions/tree/master/conftest): Use [Conftest](https://www.conftest.dev/) to test your configuration files.
  * [`coreos_prometheus`](https://github.com/tilt-dev/tilt-extensions/tree/master/coreos_prometheus): Deploys Prometheus to a monitoring namespace, managed by the CoreOS Prometheus Operator and CRDs
  * [`current_namespace`](https://github.com/tilt-dev/tilt-extensions/tree/master/current_namespace): Reads the default namespace from your kubectl config.
  * [`custom_build_with_restart`](https://github.com/tilt-dev/tilt-extensions/tree/master/restart_process): Wrap a `custom_build` to restart the given entrypoint after a Live Update
  * [`deployment`](https://github.com/tilt-dev/tilt-extensions/tree/master/deployment): Create K8s deployments, jobs, and services without manifest YAML files.
  * [`docker_build_sub`](https://github.com/tilt-dev/tilt-extensions/tree/master/docker_build_sub): Specify extra Dockerfile directives in your Tiltfile beyond [`docker_build`](https://docs.tilt.dev/api.html#api.docker_build).
  * [`docker_build_with_restart`](https://github.com/tilt-dev/tilt-extensions/tree/master/restart_process): Wrap a `docker_build` to restart the given entrypoint after a Live Update
  * [`dotenv`](https://github.com/tilt-dev/tilt-extensions/tree/master/dotenv): Load environment variables from `.env` or another file.
  * [`file_sync_only`](https://github.com/tilt-dev/tilt-extensions/tree/master/file_sync_only): No-build, no-push, file sync-only development. Useful when you want to live-reload a single config file into an existing public image, like nginx.
  * [`git_resource`](https://github.com/tilt-dev/tilt-extensions/tree/master/git_resource): Deploy a dockerfile from a remote repository â or specify the path to a local checkout for local development.
  * [`hasura`](https://github.com/tilt-dev/tilt-extensions/tree/master/hasura): Deploys [Hasura GraphQL Engine](https://hasura.io/) and monitors metadata/migrations changes locally.
  * [`hello_world`](https://github.com/tilt-dev/tilt-extensions/tree/master/hello_world): Print âHello world!â. Used in [Extensions](https://docs.tilt.dev/extensions.html).
  * [`helm_remote`](https://github.com/tilt-dev/tilt-extensions/tree/master/helm_remote): Install a remote Helm chart (in a way that gets properly uninstalled when running `tilt down`)
  * [`helm_resource`](https://github.com/tilt-dev/tilt-extensions/tree/master/helm_resource): Deploy with the Helm CLI. New Tilt users should prefer this approach over `helm_remote`.
  * [`honeycomb`](https://github.com/tilt-dev/tilt-extensions/tree/master/honeycomb): Report dev env health metrics to [Honeycomb](https://honeycomb.io).
  * [`jest_test_runner`](https://github.com/tilt-dev/tilt-extensions/tree/master/jest_test_runner): Jest JavaScript test runner. Example from [Contribute an Extension](https://docs.tilt.dev/contribute_extension.html).
  * [`k8s_attach`](https://github.com/tilt-dev/tilt-extensions/tree/master/k8s_attach): Attach to an existing Kubernetes resource thatâs already in your cluster. View their health and live-update them in-place.
  * [`kim`](https://github.com/tilt-dev/tilt-extensions/tree/master/kim): Use [kim](https://github.com/rancher/kim) to build images for Tilt
  * [`knative`](https://github.com/tilt-dev/tilt-extensions/tree/master/knative): Use [knative serving](https://knative.dev/docs/serving/) to iterate on scale-to-zero servers.
  * [`ko`](https://github.com/tilt-dev/tilt-extensions/tree/master/ko): Use [Ko](https://github.com/google/ko) to build Go-based container images
  * [`kubebuilder`](https://github.com/tilt-dev/tilt-extensions/tree/master/kubebuilder): Enable live-update for developing [Kubebuilder](https://github.com/kubernetes-sigs/kubebuilder) projects.
  * [`kubectl_build`](https://github.com/tilt-dev/tilt-extensions/tree/master/kubectl_build): Get faster build cycles and smaller disk usage by building docker images directly in the k8s cluster with [BuildKit CLI for kubectl](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl).
  * [`kubefwd`](https://github.com/tilt-dev/tilt-extensions/tree/master/kubefwd): Use [Kubefwd](https://kubefwd.com/) to bulk-forward Kubernetes services.
  * [`local_output`](https://github.com/tilt-dev/tilt-extensions/tree/master/local_output): Run a `local` command and get the output as string
  * [`min_k8s_version`](https://github.com/tilt-dev/tilt-extensions/tree/master/min_k8s_version): Require a minimum Kubernetes version to run this Tiltfile.
  * [`min_tilt_version`](https://github.com/tilt-dev/tilt-extensions/tree/master/min_tilt_version): Require a minimum Tilt version to run this Tiltfile.
  * [`namespace`](https://github.com/tilt-dev/tilt-extensions/tree/master/namespace): Functions for interacting with namespaces.
  * [`nix`](https://github.com/tilt-dev/tilt-extensions/tree/master/nix): Use [nix](https://nixos.org/guides/install-nix.html) to build nix-based container images.
  * [`ngrok`](https://github.com/tilt-dev/tilt-extensions/tree/master/ngrok): Expose public URLs for your services with [`ngrok`](https://ngrok.com/).
  * [`pack`](https://github.com/tilt-dev/tilt-extensions/tree/master/pack): Build container images using [pack](https://buildpacks.io/docs/install-pack/) and [buildpacks](https://buildpacks.io/).
  * [`podman`](https://github.com/tilt-dev/tilt-extensions/tree/master/podman): Build container images using [podman](https://podman.io)
  * [`print_tiltfile_dir`](https://github.com/tilt-dev/tilt-extensions/tree/master/print_tiltfile_dir): Print all files in the Tiltfile directory. If recursive is set to True, also prints files in all recursive subdirectories.
  * [`procfile`](https://github.com/tilt-dev/tilt-extensions/tree/master/procfile): Create Tilt resources from a foreman Procfile.
  * [`restart_process`](https://github.com/tilt-dev/tilt-extensions/tree/master/restart_process): Wrap a `docker_build` to restart the given entrypoint after a Live Update (replaces `restart_container()`)
  * [`secret`](https://github.com/tilt-dev/tilt-extensions/tree/master/secret): Functions for creating secrets.
  * [`snyk`](https://github.com/tilt-dev/tilt-extensions/tree/master/snyk): Use [Snyk](https://snyk.io) to test your containers, configuration files, and open source dependencies.
  * [`syncback`](https://github.com/tilt-dev/tilt-extensions/tree/master/syncback): Sync files/directories from your container back to your local FS.
  * [`tarfetch`](https://github.com/tilt-dev/tilt-extensions/tree/master/tarfetch): Fetch new and updated files from a container to your local FS.
  * [`tests`](https://github.com/tilt-dev/tilt-extensions/tree/master/tests): Some common configurations for running your tests in Tilt.
  * [`tilt_inspector`](https://github.com/tilt-dev/tilt-extensions/tree/master/tilt_inspector): Debugging server for exploring internal Tilt state.
  * [`uibutton`](https://github.com/tilt-dev/tilt-extensions/tree/master/uibutton): Customize your Tilt dashboard with [buttons to run a command](https://blog.tilt.dev/2021/06/21/uibutton.html).
  * [`wait_for_it`](https://github.com/tilt-dev/tilt-extensions/tree/master/wait_for_it): Wait until command output is equal to given output.

â Back to top  [ Edit on GitHub  ](https://github.com/tilt-
dev/tilt.build/tree/master/docs/api.md)







### Was this doc helpful?

Yes No

