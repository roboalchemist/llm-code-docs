# Source: https://docs.anchorbrowser.io/examples/form-filling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Form Filling Automation

The following example shows form filling, including the ability to self-complete missing data in the form filling process.

<CodeGroup>
  ```tsx node.js theme={null}
  const result = await anchorClient.agent.task(
    `Go to https://www.wix.com/demone2/nicol-rider, read the resume,
    understand the details, and complete the form at
    https://formspree.io/library/donation/charity-donation-form/preview.html
    as if you were her. Limit the donation to $10.`
  )
  console.log(result);
  ```

  ```python python theme={null}
  result = anchor_client.agent.task(
    '''Go to https://www.wix.com/demone2/nicol-rider, read the resume,
    understand the details, and complete the form at
    https://formspree.io/library/donation/charity-donation-form/preview.html
    as if you were her. Limit the donation to $10.'''
  )
  print(result)
  ```
</CodeGroup>
