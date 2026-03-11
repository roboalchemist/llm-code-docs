# Source: https://docs.anyscale.com/kb/validate-runtime-custom-image.md

# Validate Anyscale Runtime in custom Docker images

[View Markdown](/kb/validate-runtime-custom-image.md)

# Validate Anyscale Runtime in custom Docker images

This article explains how to test whether the Anyscale Runtime is properly injected into your custom Docker image using an Anyscale job. Use this validation in your CI/CD pipeline or as a manual check after building a custom image.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before running this validation, ensure you've built your custom Docker image following the requirements in [Requirements for an Anyscale container image](/container-image/image-requirement.md). This validation works with both `uv` and `pip` for managed dependencies.

## Solution[​](#solution "Direct link to Solution")

Create a Python script that checks for the Anyscale Runtime, then run it as an Anyscale job using your custom image.

### 1. Create the validation script[​](#1-create-the-validation-script "Direct link to 1. Create the validation script")

Create a file named `validate_runtime.py` with the following content:

```
import ray

@ray.remote
def func():
    from ray import anyscale
    return hasattr(ray, 'anyscale')

if __name__ == "__main__":
    result = ray.get(func.remote())
    print(f"Anyscale Runtime installed: {result}")
```

### 2. Submit the validation job[​](#2-submit-the-validation-job "Direct link to 2. Submit the validation job")

Submit the job using the Anyscale CLI with your custom image:

```
anyscale job submit \
  --image-uri <your-custom-image-uri> \
  --entrypoint "python validate_runtime.py" \
  --working-dir . \
  --runtime-env '{"pip": []}'
```

Replace `<your-custom-image-uri>` with your actual image URI. If the Anyscale Runtime is properly configured, the job outputs:

```
Anyscale Runtime installed: True
```

If the output shows `False`, the Anyscale Runtime isn't properly configured in your image.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

If the validation returns `False`, review your Docker image build process. Ensure you're following the requirements in [Requirements for an Anyscale container image](/container-image/image-requirement.md) and copying the Anyscale Runtime files correctly. See [Tutorial: Build a custom container image](/container-image/build-image-tutorial.md) for a complete example Dockerfile.

## Related resources[​](#related "Direct link to Related resources")

* [Requirements for an Anyscale container image](/container-image/image-requirement.md) - Container image requirements
* [Tutorial: Build a custom container image](/container-image/build-image-tutorial.md) - Building custom images tutorial
* [What are Anyscale jobs?](/jobs.md) - Anyscale jobs documentation
