# Source: https://smartcar.com/docs/errors/connect-errors/returned-to-application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://smartcar.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# User returned to application

> This error occurs when a user leaves the Connect flow after hitting **Back to application** before granting your application access to their vehicle.

| Parameter           | Required | Description                                                     |
| ------------------- | -------- | --------------------------------------------------------------- |
| `error`             | `true`   | `user_manually_returned_to_application`                         |
| `error_description` | `true`   | The user exited Connect before granting your application access |

There are cases where a user may wish to exit Connect before granting your application access to their vehicle. In these cases, if the user hits **Back to application** instead of closing out the window, Smartcar will return this error to your callback URI. Below are places in the Connect flow users can return to your application.

<Tabs>
  <Tab title="Missing Permissions">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=caf4655b12fd4622a2388b729cef6062" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-additional-permissions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7cf587cf7e0c1b2cba08681729975d9e 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=b94ebb2859f7703254342641165a2d7c 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=13387fa92a3ac36533ddaab14c3af732 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=902b6cccab69e580117ea816dcb6d204 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=58179df631724a774f59bc7b98dbb47c 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-additional-permissions.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=7c40443504cd03750b11751769993a57 2500w" />
    </Frame>
  </Tab>

  <Tab title="MFA Entry">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=24d212a190bb5054eab9c1e83b45de2a" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-mfa-entry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=4323baa7ecf4a9fa7e5971757b3e5dee 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ff92419e74ba4365700a712145ae1eac 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=12451d2285e032eba9906d29562ef065 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ebb517ebff6f72c834d4a4e238aa36b6 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=18561fd163d8e8d3358b966139d99ca4 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-mfa-entry.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=74115eb37105c0e0ab92e9e08a1d9666 2500w" />
    </Frame>
  </Tab>

  <Tab title="PIN Entry">
    <Frame caption="Vehicle Incompatible">
      <img src="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=e746980cc79f0b5c73184434ff772f0f" data-og-width="750" width="750" data-og-height="1334" height="1334" data-path="images/errors/connect-errors/r2a-pin-entry.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=280&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=ffea845ea4f7aa0c0790939bd2335c21 280w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=560&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=66528ca361146aa98f3178ab2b9edf65 560w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=840&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=30d5044e008af730f9de6961af43f6eb 840w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=1100&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=d71c7eb73761877c3c13b9343620d98f 1100w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=1650&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=19679505e4bb06522befd9e37e76a502 1650w, https://mintcdn.com/smartcar-docs/klvdxjd2EpHsqsG2/images/errors/connect-errors/r2a-pin-entry.png?w=2500&fit=max&auto=format&n=klvdxjd2EpHsqsG2&q=85&s=f2c2ce4edec0b6c34d14575bab4d0d18 2500w" />
    </Frame>
  </Tab>
</Tabs>
