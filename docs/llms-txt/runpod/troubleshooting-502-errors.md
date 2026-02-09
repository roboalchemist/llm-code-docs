# Source: https://docs.runpod.io/references/troubleshooting/troubleshooting-502-errors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# 502 errors

502 errors can occur when users attempt to access a program running on a specific port of a deployed pod and the program isn't running or has encountered an error. This document provides guidance to help you troubleshoot this error.

### Check your Pod's GPU

The first step to troubleshooting a 502 error is to check whether your pod has a GPU attached.

1. **Access your pod's settings**: Click on your pod's settings in the user interface to access detailed information about your pod.

2. **Verify GPU attachment**: Here, you should be able to see if your pod has a GPU attached. If it does not, you will need to attach a GPU.

If a GPU is attached, you will see it under the Pods screen (e.g. 1 x A6000). If a GPU is not attached, this number will be 0. Runpod does allow you to spin up a pod with 0 GPUs so that you can connect to it via a Terminal or CloudSync to access data. However, the options to connect to Runpod via the web interface will be nonfunctional, even if they are lit up.

<Frame caption="">
  <img src="https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=fad8d9c2a2e5d2f1d958f8bbd7414655" data-og-width="410" width="410" data-og-height="123" height="123" data-path="images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=280&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=958cb114230af110f7f73bbb21e82afb 280w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=560&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=40ea85aafbc935cb718b80c2eddfe099 560w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=840&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=90be55546153783aa06bb38c63d6ddec 840w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=1100&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=98fb9aea95218542ec4971a7301b90ad 1100w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=1650&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=fde447d1e990cbe04114acafbd652774 1650w, https://mintcdn.com/runpod-b18f5ded/QcR4sHy3480YmZ2d/images/1950025a-fb4c0dd-image-a00848a71ff50d8ce10e5e7f35cc33ff.png?w=2500&fit=max&auto=format&n=QcR4sHy3480YmZ2d&q=85&s=ead41dc8f012dfdfaf09b6f608e9b46b 2500w" />
</Frame>

### Check your Pod's logs

After confirming that your pod has a GPU attached, the next step is to check your pod's logs for any errors.

1. **Access your pod's logs**: You can view the logs from the pod's settings in the user interface.

2. <Frame caption="">
     <img src="https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=3a0a7b5c75cba78bd2bbcebb5528343e" data-og-width="419" width="419" data-og-height="200" height="200" data-path="images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=280&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=30635c8a3a2dc083ce8f27844110a24a 280w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=560&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=d519146c5c00fc91cd4ba7dcd8ddeb45 560w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=840&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=2a817c4a40956bfef984766ecc16131f 840w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=1100&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=e3ddf07c28e76b714572182abad683c4 1100w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=1650&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=0f33daa8e8a8c4249b0423aa4d4160c5 1650w, https://mintcdn.com/runpod-b18f5ded/45mQOiVf5AVJdF5-/images/ef293f09-3500eba-image-dc2d7107a41028eb6ed2c97919c4e61c.png?w=2500&fit=max&auto=format&n=45mQOiVf5AVJdF5-&q=85&s=625ed83fe87457a174fb23241b04d729 2500w" />
   </Frame>
   **Look for errors**: Browse through the logs to find any error messages that may provide clues about why you're experiencing a 502 error.

### Verify additional steps for official templates

In some cases, for our official templates, the user interface does not work right away and may require additional steps to be performed by the user.

1. **Access the template's ReadMe**: Navigate to the template's page and open the ReadMe file.

2. **Follow additional steps**: The ReadMe file should provide instructions on any additional steps you need to perform to get the UI functioning properly. Make sure to follow these instructions closely.

Remember, each template may have unique requirements or steps for setup. It is always recommended to thoroughly review the documentation associated with each template.

If you continue to experience 502 errors after following these steps, please contact our support team. We're here to help ensure that your experience on our platform is as seamless as possible.
