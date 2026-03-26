# Source: https://docs.debricked.com/tips-and-tricks/workarounds/scanning-conan-c++-projects.md

# Scanning Conan (C++) projects

OpenText Core SCA supports scanning of CycloneDX SBOMs. To scan a Conan project, you can use the following GitHub Action that generates an SBOM and scans it with the OpenText Core SCA tool:

{% @github-files/github-code-block url="<https://github.com/Debricked-Community/conan-example/blob/master/.github/workflows/debricked.yml>" %}

It uses the official [CycloneDX Conan generator](https://github.com/CycloneDX/cyclonedx-conan) from the CycloneDX project.<br>
