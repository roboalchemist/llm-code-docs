# Source: https://momentic.ai/docs/generating-text.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generating text

AI text generation is currently surfaced through the
[JavaScript](/steps/javascript) step. Within Momentic's JavaScript sandbox, your
code can access a special `ai` object. This object contains the following
utility function:

### Generating text

The `generate` utility function allows you to prompt an LLM to generate text.
The `input` is a string which the LLM will use as the prompt.

<Tabs>
  <Tab title="Function signature">
    ```ts  theme={null}
    async function generate(input: string): Promise<string>
    ```
  </Tab>

  <Tab title="Example">
    ```ts  theme={null}
    const otpCodeSms = "Your verification code is 543890"
    return await ai.generate(`Extract the OTP code and only the OTP code from the following: ${otpCodeSms}`)
    ```
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).