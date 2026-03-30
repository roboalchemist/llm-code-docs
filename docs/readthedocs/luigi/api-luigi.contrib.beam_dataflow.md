# luigi.contrib.beam_dataflow

Classes

`BeamDataflowJobTask`(*args, **kwargs)

Luigi wrapper for a Dataflow job.

`DataflowParamKeys`()

Defines the naming conventions for Dataflow execution params.

class luigi.contrib.beam_dataflow.DataflowParamKeys

Defines the naming conventions for Dataflow execution params.
For example, the Java API expects param names in lower camel case, whereas
the Python implementation expects snake case.

abstract property runner

abstract property project

abstract property zone

abstract property region

abstract property staging_location

abstract property temp_location

abstract property gcp_temp_location

abstract property num_workers

abstract property autoscaling_algorithm

abstract property max_num_workers

abstract property disk_size_gb

abstract property worker_machine_type

abstract property worker_disk_type

abstract property job_name

abstract property service_account

abstract property network

abstract property subnetwork

abstract property labels

class luigi.contrib.beam_dataflow.BeamDataflowJobTask(**args*, ***kwargs*)

Luigi wrapper for a Dataflow job. Must be overridden for each Beam SDK
with that SDK’s dataflow_executable().

For more documentation, see:

https://cloud.google.com/dataflow/docs/guides/specifying-exec-params

The following required Dataflow properties must be set:

project                 # GCP project ID
temp_location           # Cloud storage path for temporary files

The following optional Dataflow properties can be set:

runner                  # PipelineRunner implementation for your Beam job.

Default: DirectRunner

num_workers             # The number of workers to start the task with

Default: Determined by Dataflow service

autoscaling_algorithm   # The Autoscaling mode for the Dataflow job

Default: THROUGHPUT_BASED

max_num_workers         # Used if the autoscaling is enabled

Default: Determined by Dataflow service

network                 # Network in GCE to be used for launching workers

Default: a network named “default”

subnetwork              # Subnetwork in GCE to be used for launching workers

Default: Determined by Dataflow service

disk_size_gb            # Remote worker disk size. Minimum value is 30GB

Default: set to 0 to use GCP project default

worker_machine_type     # Machine type to create Dataflow worker VMs

Default: Determined by Dataflow service

job_name                # Custom job name, must be unique across project’s

active jobs

worker_disk_type        # Specify SSD for local disk or defaults to hard

disk as a full URL of disk type resource
Default: Determined by Dataflow service.

service_account         # Service account of Dataflow VMs/workers

Default: active GCE service account

region                  # Region to deploy Dataflow job to

Default: us-central1

zone                    # Availability zone for launching workers instances

Default: an available zone in the specified region

staging_location        # Cloud Storage bucket for Dataflow to stage binary

files
Default: the value of temp_location

gcp_temp_location       # Cloud Storage path for Dataflow to stage temporary

files
Default: the value of temp_location

labels                  # Custom GCP labels attached to the Dataflow job

Default: nothing

project = None

runner = None

temp_location = None

staging_location = None

gcp_temp_location = None

num_workers = None

autoscaling_algorithm = None

max_num_workers = None

network = None

subnetwork = None

disk_size_gb = None

worker_machine_type = None

job_name = None

worker_disk_type = None

service_account = None

zone = None

region = None

labels: dict[str, str] = {}

cmd_line_runner

alias of `_CmdLineRunner`

dataflow_params = None

abstractmethod dataflow_executable()

Command representing the Dataflow executable to be run.
For example:

return [‘java’, ‘com.spotify.luigi.MyClass’, ‘-Xmx256m’]

args()

Extra String arguments that will be passed to your Dataflow job.
For example:

return [’–setup_file=setup.py’]

before_run()

Hook that gets called right before the Dataflow job is launched.
Can be used to setup any temporary files/tables, validate input, etc.

on_successful_run()

Callback that gets called right after the Dataflow job has finished
successfully but before validate_output is run.

validate_output()

Callback that can be used to validate your output before it is moved to
its final location. Returning false here will cause the job to fail, and
output to be removed instead of published.

file_pattern()

If one/some of the input target files are not in the pattern of part-*,
we can add the key of the required target and the correct file pattern
that should be appended in the command line here. If the input target key is not found
in this dict, the file pattern will be assumed to be part-* for that target.

:return A dictionary of overridden file pattern that is not part-* for the inputs

on_successful_output_validation()

Callback that gets called after the Dataflow job has finished
successfully if validate_output returns True.

cleanup_on_error(*error*)

Callback that gets called after the Dataflow job has finished
unsuccessfully, or validate_output returns False.

run()

The task run method, to be overridden in a subclass.

See Task.run

static get_target_path(*target*)

Given a luigi Target, determine a stringly typed path to pass as a
Dataflow job argument.