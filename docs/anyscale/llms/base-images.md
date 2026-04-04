# Source: https://docs.anyscale.com/reference/base-images.md

# Anyscale base images

[View Markdown](/reference/base-images.md)

# Anyscale base images

Anyscale provides a set of pre-built base container images to use with workspaces, jobs, and services.

For each supported version of Ray, Anyscale releases base images with pre-configured Python and Debian packages. Anyscale tests these environments to ensure the installed packages are compatible with the version of Ray, Python, and CUDA installed on the cluster.

These environments include the packages required by most common Ray workloads. You can modify these environments with new libraries and use Anyscale tools to manage these dependencies as you move your applications from development to production.

To compare dependencies between base images, see [Compare Anyscale base images](/reference/base-images/compare).

## Image naming conventions[​](#image-naming-conventions "Direct link to Image naming conventions")

Anyscale uses the following naming convention for base images:

```
anyscale/ray:<ray-version>-<image-type>-<python-version>-<cuda-version>
```

For example, the `anyscale/ray:2.30.0-slim-py310-cu123` image means the following:

* Ray version is **2.30.0**.
* Image type is **slim**.
* Python version is **3.10**.
* CUDA version is **12.3**.

*Slim images* contain the minimum set of dependencies required to run on Anyscale. Anyscale recommends starting with slim images to reduce the size of images, which reduces latency when building images, interacting with image registries, and deploying containers.

important

Anyscale has deprecated `ray-ml` base images.

You can continue to use these images when building your own custom images or using a containerfile. Anyscale recommends migrating all workloads to supported base images.

### Anyscale Ray LLM images[​](#anyscale-ray-llm-images "Direct link to Anyscale Ray LLM images")

Anyscale releases a single `anyscale/ray-llm` image for each Ray release. These images include the compatible vLLM versions for the Ray Serve and Ray Data LLM APIs and additional dependencies frequently used in LLM workloads.

For example, [Ray 2.52.1, LLM, CUDA version 12.8](/reference/base-images/ray-2521/py311#ray-llm-2-52-1-py311-cu128).

## Image list by Ray version[​](#image-list-by-ray-version "Direct link to Image list by Ray version")

See the following pages to view the included packages for each image and version of Ray and Python:

2.54.0

* [Python 3.13 (experimental)](/reference/base-images/ray-2540/py313)
* [Python 3.12](/reference/base-images/ray-2540/py312)
* [Python 3.11](/reference/base-images/ray-2540/py311)
* [Python 3.10](/reference/base-images/ray-2540/py310)

2.53.0

* [Python 3.12](/reference/base-images/ray-2530/py312)
* [Python 3.11](/reference/base-images/ray-2530/py311)
* [Python 3.10](/reference/base-images/ray-2530/py310)

2.52.1

* [Python 3.12](/reference/base-images/ray-2521/py312)
* [Python 3.11](/reference/base-images/ray-2521/py311)
* [Python 3.10](/reference/base-images/ray-2521/py310)

2.52.0

* [Python 3.12](/reference/base-images/ray-2520/py312)
* [Python 3.11](/reference/base-images/ray-2520/py311)
* [Python 3.10](/reference/base-images/ray-2520/py310)

2.51.2

* [Python 3.12](/reference/base-images/ray-2512/py312)
* [Python 3.11](/reference/base-images/ray-2512/py311)
* [Python 3.10](/reference/base-images/ray-2512/py310)
* [Python 3.9](/reference/base-images/ray-2512/py39)

2.51.1

* [Python 3.12](/reference/base-images/ray-2511/py312)
* [Python 3.11](/reference/base-images/ray-2511/py311)
* [Python 3.10](/reference/base-images/ray-2511/py310)
* [Python 3.9](/reference/base-images/ray-2511/py39)

2.51.0

* [Python 3.12](/reference/base-images/ray-2510/py312)
* [Python 3.11](/reference/base-images/ray-2510/py311)
* [Python 3.10](/reference/base-images/ray-2510/py310)
* [Python 3.9](/reference/base-images/ray-2510/py39)

2.50.1

* [Python 3.12](/reference/base-images/ray-2501/py312)
* [Python 3.11](/reference/base-images/ray-2501/py311)
* [Python 3.10](/reference/base-images/ray-2501/py310)
* [Python 3.9](/reference/base-images/ray-2501/py39)

2.50.0

* [Python 3.12](/reference/base-images/ray-2500/py312)
* [Python 3.11](/reference/base-images/ray-2500/py311)
* [Python 3.10](/reference/base-images/ray-2500/py310)
* [Python 3.9](/reference/base-images/ray-2500/py39)

2.49.2

* [Python 3.12](/reference/base-images/ray-2492/py312)
* [Python 3.11](/reference/base-images/ray-2492/py311)
* [Python 3.10](/reference/base-images/ray-2492/py310)
* [Python 3.9](/reference/base-images/ray-2492/py39)

2.49.1

* [Python 3.12](/reference/base-images/ray-2491/py312)
* [Python 3.11](/reference/base-images/ray-2491/py311)
* [Python 3.10](/reference/base-images/ray-2491/py310)
* [Python 3.9](/reference/base-images/ray-2491/py39)

2.49.0

* [Python 3.12](/reference/base-images/ray-2490/py312)
* [Python 3.11](/reference/base-images/ray-2490/py311)
* [Python 3.10](/reference/base-images/ray-2490/py310)
* [Python 3.9](/reference/base-images/ray-2490/py39)

2.48.0

* [Python 3.12](/reference/base-images/ray-2480/py312)
* [Python 3.11](/reference/base-images/ray-2480/py311)
* [Python 3.10](/reference/base-images/ray-2480/py310)
* [Python 3.9](/reference/base-images/ray-2480/py39)

2.47.1

* [Python 3.12](/reference/base-images/ray-2471/py312)
* [Python 3.11](/reference/base-images/ray-2471/py311)
* [Python 3.10](/reference/base-images/ray-2471/py310)
* [Python 3.9](/reference/base-images/ray-2471/py39)

2.47.0

* [Python 3.12](/reference/base-images/ray-2470/py312)
* [Python 3.11](/reference/base-images/ray-2470/py311)
* [Python 3.10](/reference/base-images/ray-2470/py310)
* [Python 3.9](/reference/base-images/ray-2470/py39)

2.46.0

* [Python 3.12](/reference/base-images/ray-2460/py312)
* [Python 3.11](/reference/base-images/ray-2460/py311)
* [Python 3.10](/reference/base-images/ray-2460/py310)
* [Python 3.9](/reference/base-images/ray-2460/py39)

2.45.0

* [Python 3.12](/reference/base-images/ray-2450/py312)
* [Python 3.11](/reference/base-images/ray-2450/py311)
* [Python 3.10](/reference/base-images/ray-2450/py310)
* [Python 3.9](/reference/base-images/ray-2450/py39)

2.44.1

* [Python 3.12](/reference/base-images/ray-2441/py312)
* [Python 3.11](/reference/base-images/ray-2441/py311)
* [Python 3.10](/reference/base-images/ray-2441/py310)
* [Python 3.9](/reference/base-images/ray-2441/py39)

2.44.0

* [Python 3.12](/reference/base-images/ray-2440/py312)
* [Python 3.11](/reference/base-images/ray-2440/py311)
* [Python 3.10](/reference/base-images/ray-2440/py310)
* [Python 3.9](/reference/base-images/ray-2440/py39)

2.43.0

* [Python 3.12](/reference/base-images/ray-2430/py312)
* [Python 3.11](/reference/base-images/ray-2430/py311)
* [Python 3.10](/reference/base-images/ray-2430/py310)
* [Python 3.9](/reference/base-images/ray-2430/py39)

2.42.1

* [Python 3.12](/reference/base-images/ray-2421/py312)
* [Python 3.11](/reference/base-images/ray-2421/py311)
* [Python 3.10](/reference/base-images/ray-2421/py310)
* [Python 3.9](/reference/base-images/ray-2421/py39)

2.42.0

* [Python 3.12](/reference/base-images/ray-2420/py312)
* [Python 3.11](/reference/base-images/ray-2420/py311)
* [Python 3.10](/reference/base-images/ray-2420/py310)
* [Python 3.9](/reference/base-images/ray-2420/py39)

2.41.0

* [Python 3.12](/reference/base-images/ray-2410/py312)
* [Python 3.11](/reference/base-images/ray-2410/py311)
* [Python 3.10](/reference/base-images/ray-2410/py310)
* [Python 3.9](/reference/base-images/ray-2410/py39)

2.40.0

* [Python 3.12](/reference/base-images/ray-2400/py312)
* [Python 3.11](/reference/base-images/ray-2400/py311)
* [Python 3.10](/reference/base-images/ray-2400/py310)
* [Python 3.9](/reference/base-images/ray-2400/py39)

2.39.0

* [Python 3.12](/reference/base-images/ray-2390/py312)
* [Python 3.11](/reference/base-images/ray-2390/py311)
* [Python 3.10](/reference/base-images/ray-2390/py310)
* [Python 3.9](/reference/base-images/ray-2390/py39)

2.38.0

* [Python 3.12](/reference/base-images/ray-2380/py312)
* [Python 3.11](/reference/base-images/ray-2380/py311)
* [Python 3.10](/reference/base-images/ray-2380/py310)
* [Python 3.9](/reference/base-images/ray-2380/py39)

2.37.0

* [Python 3.12](/reference/base-images/ray-2370/py312)
* [Python 3.11](/reference/base-images/ray-2370/py311)
* [Python 3.10](/reference/base-images/ray-2370/py310)
* [Python 3.9](/reference/base-images/ray-2370/py39)

2.36.1

* [Python 3.12](/reference/base-images/ray-2361/py312)
* [Python 3.11](/reference/base-images/ray-2361/py311)
* [Python 3.10](/reference/base-images/ray-2361/py310)
* [Python 3.9](/reference/base-images/ray-2361/py39)

2.36.0

* [Python 3.12](/reference/base-images/ray-2360/py312)
* [Python 3.11](/reference/base-images/ray-2360/py311)
* [Python 3.10](/reference/base-images/ray-2360/py310)
* [Python 3.9](/reference/base-images/ray-2360/py39)

2.35.0

* [Python 3.12](/reference/base-images/ray-2350/py312)
* [Python 3.11](/reference/base-images/ray-2350/py311)
* [Python 3.10](/reference/base-images/ray-2350/py310)
* [Python 3.9](/reference/base-images/ray-2350/py39)

2.34.0

* [Python 3.11](/reference/base-images/ray-2340/py311)
* [Python 3.10](/reference/base-images/ray-2340/py310)
* [Python 3.9](/reference/base-images/ray-2340/py39)

2.33.0

* [Python 3.11](/reference/base-images/ray-2330/py311)
* [Python 3.10](/reference/base-images/ray-2330/py310)
* [Python 3.9](/reference/base-images/ray-2330/py39)

2.32.0

* [Python 3.11](/reference/base-images/ray-2320/py311)
* [Python 3.10](/reference/base-images/ray-2320/py310)
* [Python 3.9](/reference/base-images/ray-2320/py39)

2.31.0

* [Python 3.11](/reference/base-images/ray-2310/py311)
* [Python 3.10](/reference/base-images/ray-2310/py310)
* [Python 3.9](/reference/base-images/ray-2310/py39)

2.30.0

* [Python 3.11](/reference/base-images/ray-2300/py311)
* [Python 3.10](/reference/base-images/ray-2300/py310)
* [Python 3.9](/reference/base-images/ray-2300/py39)

Older Ray versions

2.24.0

* [Python 3.11](/reference/base-images/ray-2240/py311)
* [Python 3.10](/reference/base-images/ray-2240/py310)
* [Python 3.9](/reference/base-images/ray-2240/py39)

2.23.0

* [Python 3.11](/reference/base-images/ray-2230/py311)
* [Python 3.10](/reference/base-images/ray-2230/py310)
* [Python 3.9](/reference/base-images/ray-2230/py39)

2.22.0

* [Python 3.11](/reference/base-images/ray-2220/py311)
* [Python 3.10](/reference/base-images/ray-2220/py310)
* [Python 3.9](/reference/base-images/ray-2220/py39)

2.21.0

* [Python 3.11](/reference/base-images/ray-2210/py311)
* [Python 3.10](/reference/base-images/ray-2210/py310)
* [Python 3.9](/reference/base-images/ray-2210/py39)

2.20.0

* [Python 3.11](/reference/base-images/ray-2200/py311)
* [Python 3.10](/reference/base-images/ray-2200/py310)
* [Python 3.9](/reference/base-images/ray-2200/py39)

2.12.0

* [Python 3.11](/reference/base-images/ray-2120/py311)
* [Python 3.10](/reference/base-images/ray-2120/py310)
* [Python 3.9](/reference/base-images/ray-2120/py39)

2.11.0

* [Python 3.11](/reference/base-images/ray-2110/py311)
* [Python 3.10](/reference/base-images/ray-2110/py310)
* [Python 3.9](/reference/base-images/ray-2110/py39)
