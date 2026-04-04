# Source: https://infisical.com/docs/documentation/platform/dynamic-secrets/totp.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TOTP

> Learn how to dynamically generate time-based one-time passwords.

The Infisical TOTP dynamic secret allows you to generate time-based one-time passwords on demand.

## Prerequisite

* Infisical requires either an OTP url or a secret key from a TOTP provider.

## Set up Dynamic Secrets with TOTP

<Steps>
  <Step title="Open Secret Overview Dashboard">
    Open the Secret Overview dashboard and select the environment in which you would like to add a dynamic secret.
  </Step>

  <Step title="Click on the 'Add Dynamic Secret' button">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/add-dynamic-secret-button.png" alt="Add Dynamic Secret Button" />
  </Step>

  <Step title="Select TOTP">
        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-modal-totp.png" alt="Dynamic Secret Modal" />
  </Step>

  <Step title="Provide the inputs for dynamic secret parameters">
    <ParamField path="Secret Name" type="string" required>
      Name by which you want the secret to be referenced
    </ParamField>

    <ParamField path="Configuration Type" type="string" required>
      There are two supported configuration types - `url` and `manual`.

      When `url` is selected, you can configure the TOTP generator using the OTP URL.

      When `manual` is selected, you can configure the TOTP generator using the secret key along with other configurations like period, number of digits, and algorithm.
    </ParamField>

    <ParamField path="URL" type="string">
      OTP URL in `otpauth://` format used to generate TOTP codes.
    </ParamField>

    <ParamField path="Secret Key" type="string">
      Base32 encoded secret used to generate TOTP codes.
    </ParamField>

    <ParamField path="Period" type="number">
      Time interval in seconds between generating new TOTP codes.
    </ParamField>

    <ParamField path="Digits" type="number">
      Number of digits to generate in each TOTP code.
    </ParamField>

    <ParamField path="Algorithm" type="string">
      Hash algorithm to use when generating TOTP codes. The supported algorithms are sha1, sha256, and sha512.
    </ParamField>

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-setup-modal-totp-url.png" alt="Dynamic Secret Setup Modal" />
    <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-setup-modal-totp-manual.png" alt="Dynamic Secret Setup Modal" />
  </Step>

  <Step title="Click 'Submit'">
    After submitting the form, you will see a dynamic secret created in the dashboard.
  </Step>

  <Step title="Generate dynamic secrets">
    Once you've successfully configured the dynamic secret, you're ready to generate on-demand TOTPs.
    To do this, simply click on the 'Generate' button which appears when hovering over the dynamic secret item.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/dynamic-secret-generate.png" alt="Dynamic Secret" />

    Once you click the `Generate` button, a new secret lease will be generated and the TOTP will be shown to you.

        <img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/dynamic-secrets/totp-lease-value.png" alt="Provision Lease" />
  </Step>
</Steps>
