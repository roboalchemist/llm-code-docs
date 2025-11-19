# Source: https://docs.baseten.co/development/model/base-images.md

# Base Docker images

> A guide to configuring a base image for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. While the default Truss image works for most cases, you may need a custom base image to meet specific package or system requirements.

## Setting a base image in`config.yaml`

Specify a custom base image in `config.yaml`:

```yaml config.yaml theme={"system"}
base_image:
  image: <image_name:tag>
  python_executable_path: <path-to-python>
```

* `image`: The Docker image to use.
* `python_executable_path`: The path to the Python binary inside the container.

### Example: NVIDIA NeMo Model

Using a custom image to deploy [NVIDIA NeMo TitaNet](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large) model:

```yaml config.yaml theme={"system"}
base_image:
  image: nvcr.io/nvidia/nemo:23.03
  python_executable_path: /usr/bin/python
apply_library_patches: true
requirements:
  - PySoundFile
resources:
  accelerator: T4
  cpu: 2500m
  memory: 4512Mi
  use_gpu: true
secrets: {}
system_packages:
  - python3.8-venv
```

## Using Private Base Images

If your base image is private, ensure that you have configured your model to use a [private registry](/development/model/private-registries)

## Creating a custom base image

You can build a new base image using Truss’s base images as a foundation. Available images are listed on [Docker Hub](https://hub.docker.com/r/baseten/truss-server-base/tags).

#### Example: Customizing a Truss Base Image

```Dockerfile Dockerfile theme={"system"}
FROM baseten/truss-server-base:3.11-gpu-v0.7.16
RUN pip uninstall cython -y
RUN pip install cython==0.29.30
```

#### Building & Pushing Your Custom Image

Ensure Docker is installed and running. Then, build, tag, and push your image:

```sh  theme={"system"}
docker build -t my-custom-base-image:0.1 .
docker tag my-custom-base-image:0.1 your-docker-username/my-custom-base-image:0.1
docker push your-docker-username/my-custom-base-image:0.1
```
