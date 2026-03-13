# luigi.contrib.docker_runner

Docker container wrapper for Luigi.

Enables running a docker container as a task in luigi.
This wrapper uses the Docker Python SDK to communicate directly with the
Docker API avoiding the common pattern to invoke the docker client
from the command line. Using the SDK it is possible to detect and properly
handle errors occurring when pulling, starting or running the containers.
On top of this, it is possible to mount a single file in the container
and a temporary directory is created on the host and mounted allowing
the handling of files bigger than the container limit.

Requires:

- 

docker: `pip install docker`

Written and maintained by Andrea Pierleoni (@apierleoni).
Contributions by Eliseo Papa (@elipapa).

Classes

`DockerTask`(*args, **kwargs)

When a new instance of the DockerTask class gets created: - call the parent class __init__ method - start the logger - init an instance of the docker client - create a tmp dir - add the temp dir to the volume binds specified in the task

class luigi.contrib.docker_runner.DockerTask(**args*, ***kwargs*)

When a new instance of the DockerTask class gets created:
- call the parent class __init__ method
- start the logger
- init an instance of the docker client
- create a tmp dir
- add the temp dir to the volume binds specified in the task

property image

property command

property name

property host_config_options

Override this to specify host_config options like gpu requests or shm
size e.g. {“device_requests”: [docker.types.DeviceRequest(count=1, capabilities=[[“gpu”]])]}

See https://docker-py.readthedocs.io/en/stable/api.html#docker.api.container.ContainerApiMixin.create_host_config

property container_options

Override this to specify container options like user or ports e.g.
{“user”: f”{os.getuid()}:{os.getgid()}”}

See https://docker-py.readthedocs.io/en/stable/api.html#docker.api.container.ContainerApiMixin.create_container

property environment

property container_tmp_dir

property binds

Override this to mount local volumes, in addition to the /tmp/luigi
which gets defined by default. This should return a list of strings.
e.g. [‘/hostpath1:/containerpath1’, ‘/hostpath2:/containerpath2’]

property network_mode

property docker_url

property auto_remove

property force_pull

property mount_tmp

run()

The task run method, to be overridden in a subclass.

See Task.run