# Source: https://docs.gitguardian.com/secrets-detection/customize-detection/detector-settings.md

# Detector settings

> Activate, deactivate, and request custom secrets detectors in GitGuardian workspace settings.

You can find the exhaustive list of GitGuardian secrets detectors in the [settings](https://dashboard.gitguardian.com/settings/secrets/detectors) of your workspace.

![Table of secrets detectors](/img/secrets-detection/customize-detection/secrets-detection-table-of-detectors.png)

### Activate or deactivate detectors

In [your workspace settings, on the detectors page](https://dashboard.gitguardian.com/settings/secrets/detectors), you can activate or deactivate secrets detectors on an individual basis to refine your focus on incidents.

When you deactivate a detector:

- you will not receive a notification for incidents that this detector raises,
- incidents for deactivated detectors will not be displayed in your dashboard. However, the detector will still detect and store such incidents shall you reactivate the detector later.

### Custom detectors

It is not possible to customize the detectors provided with the GitGuardian library. However, you can create your own custom detectors using regular expressions. Please note that this feature is only available for workspaces under our Business plan (or in Business trial).

:::info
This feature is designed to help you detect secrets specific to your organization (e.g internal API tokens), **all requests for detecting patterns like Personal Identifiable Information (PII) or Protected Health Information (PHI) will be rejected**.
:::

#### Submit your custom detector request

1. Navigate to Settings > Secrets > [Detectors](https://dashboard.gitguardian.com/settings/secrets/detectors?sort_f=true)
2. In the navigation bar, click `Table of Detectors` (or scroll down until you get there)
3. Click `Add a custom detector`, a modal will open
   ![Add a custom detector](/img/secrets-detection/customize-detection/secrets_detection_custom_detector_1.png)
4. Enter the details for your new custom detector:
   - You must at least provide the name for your detector, and a set of examples for the format of your internal secret pattern.
   - If you have the regular expression for the desired pattern, please provide it.
   - You can provide additional information on the pattern, surrounding content or additional match requirements for the secret format you're after.
     ![Add a custom detector - form](/img/secrets-detection/customize-detection/secrets_detection_custom_detector_2.png)
     ![Add a custom detector - ticket](/img/secrets-detection/customize-detection/secrets_detection_custom_detector_3.png)

> Only Managers can create custom detector requests.
>
> Please note that every workspace is only allowed to have 5 custom detector requests at a time. To place a new request, you will have to wait until one of your requests is accepted or rejected, or you can simply delete one of your `submitted` requests.

#### Leverage your custom detector

After submitting your request, our engineering team will promptly acknowledge it and reach out to you for validation of the regular expression. Given the complexity of regular expressions and the potential for high-volume alerts, it is crucial that we thoroughly review the results produced by your custom pattern. This ensures the delivery of precise and highly accurate alerts before deploying it to your workspace.

> Requests in the `submitted` state can be modified or deleted. However, requests in the `acknowledged` or `under implementation` state cannot be deleted.

Once the implementation of your custom detector is complete, the GitGuardian team will notify you, and your new detector will be ready for detection.

![Add a custom detector - table filtered](/img/secrets-detection/customize-detection/secrets_detection_custom_detector_4.png)

#### If you are using a GitGuardian self-hosted instance

:::caution
Custom detectors are available for self-hosted instances starting version 2023.9.0.
:::

If you are using a GitGuardian self-hosted instance, the procedure mentioned above undergoes slight modifications due to the inherent constraints of self-hosting:

1. Your request should be sent to the email address indicated in the final modal of the request procedure.
    
   ![Add a custom detector - Manual sending for self-hosted](/img/secrets-detection/customize-detection/secrets-detection-custom-detector-self-hosted-manual-sending.png)
2. upon finalization of your custom detector implementation by our R&D team, you will receive a YAML file that needs to be uploaded to complete the creation of your custom detector.
   ![Add a custom detector - YAML uploard](/img/secrets-detection/customize-detection/secrets-detection-custom-detector-self-hosted-yaml-upload.png)

> If you delete the request before the upload of the YAML file, a brand new request must be submitted.

> Ensure that you first import the YAML file to your staging instance for validation. Once satisfied, import it to your production environment.
