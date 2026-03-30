# Source: https://docs.api7.ai/enterprise/best-practices/verify-api7-image-signatures.md

# Verify API7 Image Signatures

To secure the software supply chain, API7's Docker container images follow industry best practices by using the open-source tool **Cosign** for signing. All signatures are stored in a public Docker Hub repository, `api7/notary`. Our build and release process utilizes GitHub Actions and leverages GitHub's OIDC (OpenID Connect) identity to sign the images, which provides an additional layer of trusted authentication.

By verifying the image signature, you can be confident that:

* **Authentic Source**: The image was built and published from API7's official GitHub Actions workflow.
* **Integrity**: The image has not been modified by any third party during the process from release to pull.

This guide walks you through the process of verifying API7 image signatures.

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

1. Install [Cosign](https://www.sigstore.dev/) to verify container image signatures.
2. Install [regctl](https://regclient.org/install/) to retrieve the container image digest.

## Verify Signatures[â](#verify-signatures "Direct link to Verify Signatures")

To verify an API7 container image signature, you will configure the location of the signature repository, retrieve the image digest, and verify the signature using Cosign.

### Set the Signature Repository[â](#set-the-signature-repository "Direct link to Set the Signature Repository")

Set the `COSIGN_REPOSITORY` environment variable to specify the location where image signatures are stored:

```
export COSIGN_REPOSITORY=api7/notary
```

### Get the Image Digest[â](#get-the-image-digest "Direct link to Get the Image Digest")

Every Docker image has a unique SHA-256 digest that represents a snapshot of its content. To ensure you are verifying the exact image content (rather than a mutable tag), retrieve the image digest using `regctl`:

```
regctl manifest digest api7/api7-ee-3-gateway:3.9.1
```

You should see the image's digest:

```
sha256:61a531d7ca8339712888bfdf7ad7af6d63f0e423e466818be96f0aaa3fc89578
```

### Run Cosign Verification[â](#run-cosign-verification "Direct link to Run Cosign Verification")

After obtaining the image digest, run the `cosign verify` command to verify the image signature. This command validates the signature, certificate chain, and associated claims:

```
cosign verify \
  'api7/api7-ee-3-gateway:3.9.1@sha256:61a531d7ca8339712888bfdf7ad7af6d63f0e423e466818be96f0aaa3fc89578' \
  --certificate-oidc-issuer='https://token.actions.githubusercontent.com' \
  --certificate-identity-regexp='https://github.com/api7/api7-ee-3-gateway/.github/workflows/push-release-image.yaml'
```

If the verification is successful, you will see a response similar to the following, which includes a summary of the checks performed:

```
Verification for index.docker.io/api7/api7-ee-3-gateway@sha256:61a531d7ca8339712888bfdf7ad7af6d63f0e423e466818be96f0aaa3fc89578 --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The code-signing certificate was verified using trusted certificate authority certificates
```

The command also outputs a JSON object containing detailed metadata about the signature, such as the build workflow, code repository, and trigger event:

```
[
  {
    "critical":{
      "identity":{
        "docker-reference":"index.docker.io/api7/api7-ee-3-gateway"
      },
      "image":{
        "docker-manifest-digest":"sha256:61a531d7ca8339712888bfdf7ad7af6d63f0e423e466818be96f0aaa3fc89578"
      },
      "type":"cosign container image signature"
    },
    "optional":{
      "1.3.6.1.4.1.57264.1.1":"https://token.actions.githubusercontent.com",
      "1.3.6.1.4.1.57264.1.2":"push",
      "1.3.6.1.4.1.57264.1.3":"757582d641f7bdcad3c1299cb7da113224f4f383",
      "1.3.6.1.4.1.57264.1.4":"Build And Push Release Docker Image",
      "1.3.6.1.4.1.57264.1.5":"api7/api7-ee-3-gateway",
      "1.3.6.1.4.1.57264.1.6":"refs/tags/v3.9.1",
      "Bundle":{
        "SignedEntryTimestamp":"MEUCIQCj1Xupisdx7YosnqpdByE6pGpeMzeRcBF3H6+wgK0txgIgCImsRsV+tG+96tVkGiXcr6iNifirhk7Q4lW+S3tuOX4=",
        "Payload":{
          "body":"eyJhcGlWZXJzaW9uIjoiMC4wLjEiLCJraW5kIjoiaGFzaGVkcmVrb3JkIiwic3BlYyI6eyJkYXRhIjp7Imhhc2giOnsiYWxnb3JpdGhtIjoic2hhMjU2IiwidmFsdWUiOiI4ZjAyMzdlYzRhNTBlMzkwNWFjYWQ1ZWExYzE4ODFmMzMyZWM4NmE3Y2Y5ZGQ0OWU2NmQwYmQyMTVjMDBiZDlhIn19LCJzaWduYXR1cmUiOnsiY29udGVudCI6Ik1FWUNJUUQrM1U2T1NFYnpoVk9qZlFFWnRSWmZpYlgrSWVyWWpxWEMzb1U1ZWozYTBBSWhBTENYSG1yRXUvUXhHVUlncTdSZDQ2cVhCQkVwQS9qbm03ZTJtR1B6TE8yeiIsInB1YmxpY0tleSI6eyJjb250ZW50IjoiTFMwdExTMUNSVWRKVGlCRFJWSlVTVVpKUTBGVVJTMHRMUzB0Q2sxSlNVaEJha05EUW05cFowRjNTVUpCWjBsVlN5ODNUVmM0YTNodlYyUjFkRTFCYnpkMVFYUmtOVFpZY21aTmQwTm5XVWxMYjFwSmVtb3dSVUYzVFhjS1RucEZWazFDVFVkQk1WVkZRMmhOVFdNeWJHNWpNMUoyWTIxVmRWcEhWakpOVWpSM1NFRlpSRlpSVVVSRmVGWjZZVmRrZW1SSE9YbGFVekZ3WW01U2JBcGpiVEZzV2tkc2FHUkhWWGRJYUdOT1RXcFpkMDFVUVRSTlJFMTVUa1JOZVZkb1kwNU5hbGwzVFZSQk5FMUVUWHBPUkUxNVYycEJRVTFHYTNkRmQxbElDa3R2V2tsNmFqQkRRVkZaU1V0dldrbDZhakJFUVZGalJGRm5RVVZoUzJzelRFVmlRa0psVWtsaFNsWTFVbGw1YVZod1dtRXZVUzlaVEU1bVVtbFhOVTBLZFhweGJFbFVka1ptUWxCQ1YyRTNjRXBLZFZoTGEwOVZSVmxZT0VOUmJHRXlNMmg1TkN0MlNXdFliRmRITm05elRVdFBRMEpoWTNkbloxZHFUVUUwUndwQk1WVmtSSGRGUWk5M1VVVkJkMGxJWjBSQlZFSm5UbFpJVTFWRlJFUkJTMEpuWjNKQ1owVkdRbEZqUkVGNlFXUkNaMDVXU0ZFMFJVWm5VVlZwVGtONUNtcFVVMUY1YzJsTU9XbE5NbU50Ym5wd1ltbEtNVTl2ZDBoM1dVUldVakJxUWtKbmQwWnZRVlV6T1ZCd2VqRlphMFZhWWpWeFRtcHdTMFpYYVhocE5Ga0tXa1E0ZDJObldVUldVakJTUVZGSUwwSkhaM2RhYjFwcllVaFNNR05JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKR2QyRlVZM1paV0VKd1Rua3hiQXBhVXpCNlRGZGthR1JIVmpOWldHdDJURzFrY0dSSGFERlphVGt6WWpOS2NscHRlSFprTTAxMlkwaFdlbUZETVhsYVYzaHNXVmhPYkV4WGJIUlpWMlJzQ2t4dWJHaGlWM2hCWTIxV2JXTjVPVEJaVjJSNlRETlpla3hxYTNWTlZFRTFRbWR2Y2tKblJVVkJXVTh2VFVGRlFrSkRkRzlrU0ZKM1kzcHZka3d6VW5ZS1lUSldkVXh0Um1wa1IyeDJZbTVOZFZveWJEQmhTRlpwWkZoT2JHTnRUblppYmxKc1ltNVJkVmt5T1hSTlFrbEhRMmx6UjBGUlVVSm5OemgzUVZGSlJRcENTRUl4WXpKbmQwNW5XVXRMZDFsQ1FrRkhSSFo2UVVKQmQxRnZUbnBWTTA1VVozbGFSRmt3VFZkWk0xbHRVbXBaVjFGNldYcEZlVTlVYkdwWmFtUnJDbGxVUlhoTmVrbDVUa2RaTUZwcVRUUk5la0Y0UW1kdmNrSm5SVVZCV1U4dlRVRkZSVUpEVGtOa1YyeHpXa05DUW1KdFVXZFZTRlo2WVVOQ1UxcFhlR3dLV1ZoT2JFbEZVblpaTW5Sc1kybENTbUpYUm01YVZFRnJRbWR2Y2tKblJVVkJXVTh2VFVGRlJrSkNXbWhqUjJzelRESkdkMkZVWTNSYVYxVjBUWGt4YmdwWldGSnNaREpHTlUxQ05FZERhWE5IUVZGUlFtYzNPSGRCVVZsRlJVaEtiRnB1VFhaa1IwWnVZM2s1TWsxNU5EVk1ha1YzVDNkWlMwdDNXVUpDUVVkRUNuWjZRVUpEUVZGMFJFTjBiMlJJVW5kamVtOTJURE5TZG1FeVZuVk1iVVpxWkVkc2RtSnVUWFZhTW13d1lVaFdhV1JZVG14amJVNTJZbTVTYkdKdVVYVUtXVEk1ZEUxSVVVZERhWE5IUVZGUlFtYzNPSGRCVVd0RldtZDRhMkZJVWpCalNFMDJUSGs1Ym1GWVVtOWtWMGwxV1RJNWRFd3lSbmRoVkdOMldWaENjQXBPZVRGc1dsTXdla3hYWkdoa1IxWXpXVmhyZGt4dFpIQmtSMmd4V1drNU0ySXpTbkphYlhoMlpETk5kbU5JVm5waFF6RjVXbGQ0YkZsWVRteE1WMngwQ2xsWFpHeE1ibXhvWWxkNFFXTnRWbTFqZVRrd1dWZGtla3d6V1hwTWFtdDFUVlJCTkVKbmIzSkNaMFZGUVZsUEwwMUJSVXRDUTI5TlMwUmpNVTU2VlRRS1RXMVJNazVFUm0xT01rcHJXVEpHYTAweVRYaE5hbXMxV1RKSk0xcEhSWGhOVkUxNVRXcFNiVTVIV1hwUFJFMTNSM2RaUzB0M1dVSkNRVWRFZG5wQlFncERkMUZPUkVGMGVscFhlRzFNVjJoMll6TlNiRnBFUVRWQ1oyOXlRbWRGUlVGWlR5OU5RVVZOUWtOelRVdFhhREJrU0VKNlQyazRkbG95YkRCaFNGWnBDa3h0VG5aaVV6bG9ZMGRyTTB3eVJuZGhWR04wV2xkVmRFMTVNVzVaV0ZKc1pESkdOVTFFWjBkRGFYTkhRVkZSUW1jM09IZEJVVEJGUzJkM2IwNTZWVE1LVGxSbmVWcEVXVEJOVjFreldXMVNhbGxYVVhwWmVrVjVUMVJzYWxscVpHdFpWRVY0VFhwSmVVNUhXVEJhYWswMFRYcEJaMEpuYjNKQ1owVkZRVmxQTHdwTlFVVlBRa0pKVFVWSVNteGFiazEyWkVkR2JtTjVPVEpOZVRRMVRHcEZkMGRSV1V0TGQxbENRa0ZIUkhaNlFVSkVkMUZNUkVGck1rNUVWVE5OYWtGM0NrNXFXWGRLZDFsTFMzZFpRa0pCUjBSMmVrRkNSVUZSV2tSQ1pHOWtTRkozWTNwdmRrd3laSEJrUjJneFdXazFhbUl5TUhaWldFSndUbnBCV1VKbmIzSUtRbWRGUlVGWlR5OU5RVVZTUWtGdlRVTkVXWGhOUkdNMFRrUlZlRTFJVVVkRGFYTkhRVkZSUW1jM09IZEJVa2xGV21kNGEyRklVakJqU0UwMlRIazViZ3BoV0ZKdlpGZEpkVmt5T1hSTU1rWjNZVlJqZGxsWVFuQk9lVEZzV2xNd2VreFhaR2hrUjFZeldWaHJka3h0WkhCa1IyZ3hXV2s1TTJJelNuSmFiWGgyQ21RelRYWmpTRlo2WVVNeGVWcFhlR3haV0U1c1RGZHNkRmxYWkd4TWJteG9ZbGQ0UVdOdFZtMWplVGt3V1Zka2Vrd3pXWHBNYW10MVRWUkJORUpuYjNJS1FtZEZSVUZaVHk5TlFVVlVRa052VFV0RVl6Rk9lbFUwVFcxUk1rNUVSbTFPTWtwcldUSkdhMDB5VFhoTmFtczFXVEpKTTFwSFJYaE5WRTE1VFdwU2JRcE9SMWw2VDBSTmQwWkJXVXRMZDFsQ1FrRkhSSFo2UVVKR1FWRkhSRUZTZDJSWVRtOU5SakJIUTJselIwRlJVVUpuTnpoM1FWSlZSVlIzZUU1aFNGSXdDbU5JVFRaTWVUbHVZVmhTYjJSWFNYVlpNamwwVERKR2QyRlVZM1paV0VKd1Rua3hiRnBUTUhwTVYyUm9aRWRXTTFsWWEzWlpWMDR3WVZjNWRXTjVPWGtLWkZjMWVreDZTWGRQUkVFd1RWUlpNRTlFUlhwTU1rWXdaRWRXZEdOSVVucE1la1YzUm5kWlMwdDNXVUpDUVVkRWRucEJRa1puVVVwRVFXUjNZMjFzTWdwWldGSnNUVWxIUzBKbmIzSkNaMFZGUVdSYU5VRm5VVU5DU0hkRlpXZENORUZJV1VFelZEQjNZWE5pU0VWVVNtcEhValJqYlZkak0wRnhTa3RZY21wbENsQkxNeTlvTkhCNVowTTRjRGR2TkVGQlFVZGliVFpLZERCUlFVRkNRVTFCVW5wQ1JrRnBRa1F6TlhGRk5YSnNLM0pSYTJOeGFGQnJjRmhSWVdSMVEwd0tNbWMxVGpkbGFFRnBjalpxVEROTVUxZEJTV2hCVFRNM1FXWlJaRmhQY1VsblZWSkdVSE5GWjJwSlQwdFFaV2xtUkdnM1UxaDZhM0YzTmpWV2VFMDJiZ3BOUVc5SFEwTnhSMU5OTkRsQ1FVMUVRVEpuUVUxSFZVTk5VVU56U2xKUmFXVk9OMUl3WmxOa1JtbGxkVlZqU0ZGTk9GTk5kekJWV1U4d1dYSmFUWGxQQ21WSWVFSjFXVmRqWVdobGNuTjZSbEpVZWtsWFMyMUpWVmRWYTBOTlF6QTJiM0ZuTjNBNWFVNUVPWGd6Wm5GeVZsQldja3BrYUhGelp6ZHNlVXBVWW1jS2JrOWtNRXM1WlRSTGFDdHhTbnBwTkhRMFIwTTRVbXRRWlhBelYzcG5QVDBLTFMwdExTMUZUa1FnUTBWU1ZFbEdTVU5CVkVVdExTMHRMUW89In19fX0=",
          "integratedTime":1767842673,
          "logIndex":804165791,
          "logID":"c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d"
        }
      },
      "Issuer":"https://token.actions.githubusercontent.com",
      "Subject":"https://github.com/api7/api7-ee-3-gateway/.github/workflows/push-release-image.yaml@refs/tags/v3.9.1",
      "githubWorkflowName":"Build And Push Release Docker Image",
      "githubWorkflowRef":"refs/tags/v3.9.1",
      "githubWorkflowRepository":"api7/api7-ee-3-gateway",
      "githubWorkflowSha":"757582d641f7bdcad3c1299cb7da113224f4f383",
      "githubWorkflowTrigger":"push"
    }
  }
]
```

## Certificate Identity and Workflow[â](#certificate-identity-and-workflow "Direct link to Certificate Identity and Workflow")

The `--certificate-identity-regexp` parameter ensures that the signing certificate matches the expected GitHub Actions workflow. This verifies that the image was built through the correct automated process.

Because each API7 image is released by a specific workflow, you must use the matching regular expression for verification. Use the table below to find the correct `--certificate-identity-regexp` value for the certificate of the image you are verifying:

| Image Name                         | Certificate Identity RegExp                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| `api7/api7-ee-3-gateway`           | `https://github.com/api7/api7-ee-3-gateway/.github/workflows/push-release-image.yaml` |
| `api7/api7-ee-3-integrated`        | `https://github.com/api7/api7ee-3-control-plane/.github/workflows/release.yaml`       |
| `api7/api7-ee-dp-manager`          | `https://github.com/api7/api7ee-3-control-plane/.github/workflows/release.yaml`       |
| `api7/api7-ee-developer-portal`    | `https://github.com/api7/api7ee-3-control-plane/.github/workflows/release.yaml`       |
| `api7/api7-ee-developer-portal-fe` | `https://github.com/api7/api7ee-developer-portal/.github/workflows/release.yml`       |
