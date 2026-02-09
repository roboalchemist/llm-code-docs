# Source: https://docs.zapier.com/platform/build/form-mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use form mode to setup your API calls

> In the Platform UI, when building your authentication, triggers and actions, the default setting under _API Configuration_ is to create each component of your integration using Form Mode.

## Capabilities

With Form Mode you can:

* Add the API endpoint for the request to be made
* Choose the API request type
* Set any custom URL parameters, HTTP headers and the request body under *Show Options*.

By default, the configured authentication is included as HTTP Headers, which you can modify if needed.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d593853850d8a3fa87705b688a7951df" data-og-width="1021" width="1021" data-og-height="831" height="831" data-path="images/e380a04c42f0332d57df4fd0d1532590.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=9b6bf47505c9a3befbf6dddcf23c82a8 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=4275b9bfd2b2f1a9c04a0b11cabbd40a 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=d91d557b5a42cfc6caee46eeba56aa34 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=a65519bfafb21226c6e1f94386934a63 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=ae02e66c99a79f5b9e7e4267de784fe6 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/e380a04c42f0332d57df4fd0d1532590.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=93cb6d8791d594fa8cd403eb511174f0 2500w" />

  {" "}
</Frame>

By default, any Input fields are included as URL Params. To instead include them within the API endpoint, use format \`\` where `fieldkey` is the key of the input field.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f0e96346159ab83c34db7ea1897370a4" data-og-width="1010" width="1010" data-og-height="825" height="825" data-path="images/fdc8807e9b6d41427d937d1362f20fbd.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=280&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=c7847322a51a5709b36909fe2da5fab9 280w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=560&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=85a7c1f4a4116a2f7fd8d5db779cbda3 560w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=840&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=ea3e4162658260e6a418c3e5b207a31f 840w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=1100&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=163008947b2ea62a2f3fee11b5c2ad1d 1100w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=1650&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=18a167da790b10d7e55b1d48bcb8383b 1650w, https://mintcdn.com/zapier-82f0e938/FKPl8SjhZXHXKd0_/images/fdc8807e9b6d41427d937d1362f20fbd.webp?w=2500&fit=max&auto=format&n=FKPl8SjhZXHXKd0_&q=85&s=f2f5ce320550201e8069500b996feaf6 2500w" />

  {" "}
</Frame>

When the request runs, Zapier parses JSON-encoded responses into individual output fields to use in subsequent Zap steps.

Form Mode is the simplest way to set up most API calls and options in your Platform UI integration's authentication, triggers, and actions.

## Refine the API call further

If your API calls need more customization than Form Mode offers or your API response is in a non-JSON format, you will need to write custom JavaScript code to handle your API call and/or response parsing. To do so, use [Code Mode](/platform/build/code-mode).

The first time you switch to Code Mode, Zapier copies everything entered in Form Mode, including any custom options added, and converts that to JavaScript code. It then changes the UI to include a code block, where you can add code for your API call.

Zapier uses the currently visible option when running each part of your integration. To check which mode and settings Zapier is using for each API call, open that part of your Zapier integration and visually check to see if the Form or Code Mode is visible.

To switch back to the Form Mode, click the *Switch to Form Mode* button to see the form options as they were when you *first switched*. Zapier will save the code you entered, but will not convert it back to the Form Mode nor use the custom code in your API Request.

If you then switch back to Code Mode again — you will see the last saved version of your code, and no changes you made in Form Mode will be refelcted in that code.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
