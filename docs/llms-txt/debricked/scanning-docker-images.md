# Source: https://docs.debricked.com/tips-and-tricks/workarounds/scanning-docker-images.md

# Scanning Docker images

OpenText Core SCA doesn't have official Docker image support yet, but scanning is possible using the following workaround.

To scan Docker images with OpenText Core SCA:

1. Install and run the Docker SBOM CLI plugin from <https://github.com/docker/sbom-cli-plugin> in order to generate a CycloneDX report. Make sure to change the format to CycloneDX, for example,\
   docker sbom username/imagename:latest --format cyclonedx-json --output imagename.sbom.json
2. Run OpenText Core SCA CLI from [https://github.com/debricked/cli,](https://github.com/debricked/cli) and it will automatically pick up the CycloneDX report files. You can view the results in pipeline and OpenText Core SCA UI.
