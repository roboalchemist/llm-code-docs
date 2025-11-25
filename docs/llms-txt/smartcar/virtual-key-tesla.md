# Source: https://smartcar.com/docs/help/oem-integrations/tesla/virtual-key-tesla.md

# Virtual Keys

> This page has information regarding the use of Virtual Keys for Tesla vehicles.

## What is a Virtual Key?

A Virtual Key is a digital access method required by Tesla for third-party
applications to issue commands to Tesla vehicles and the preferred method for accessing data.
Please see [this
section](/help/oem-integrations/tesla/developers#adding-a-virtual-key)
for more information.

### Adding the Virtual Key

Smartcar handles this step on your behalf in the Connect flow. You can get started with the default Smartcar Virtual Key with no configurations required.

If you're on an **Enterprise** plan, please reach out to your Account Manager or
Solutions Architect for information on setting up a custom Virtual Key with your own brand name.

## Where can I find my Virtual Key?

Although Smartcar handles this step on your behalf, the Virtual Key URL for your application is sent back along with the authorization code after a user completes the Connect flow. You can redirect users to this URL if they need to add the Virtual Key again.

### Vehicle Owners adding a Virtual Key

Smartcar Connect will present Tesla vehicle owners a prompt to install the Tesla Virtual Key after granting access and prior to redirecting them back to your application.

<Frame caption="Prompting the user to add a Virtual Key">
  <img width="700" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=e504d181b6936f3e0ba17926a2923be2" data-og-width="2283" data-og-height="931" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=02c5b864bdd1e8c5541ed1a1bfc80549 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a1ca3a12ee41154e396ae4ce1b56af65 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=89747ff417caaf5f36b30737aa24bd0a 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=6f5036a32588937a17a0ea6fb0adc4bb 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=3e4e9358fb3e91fc7e6b1ad8bc7bac0d 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/VirtualKeyPageMobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b8b9c2e23830523d41d1c9c753d3b309 2500w" />
</Frame>

The Virtual Key is a URL in the form:

<Tabs>
  <Tab title="Free or Build Plans">
    ```
    https://www.tesla.com/_ak/smartcar.com
    ```
  </Tab>

  <Tab title="Enterprise Plan">
    ```
    https://www.tesla.com/_ak/{{custom_subdomain}}.app.car
    ```
  </Tab>
</Tabs>

After prompting your users to open the link, depending on their device, they will be redirected to the Tesla app or prompted to scan a QR code.

<Tip>
  Adding a Virtual Key will need to be done after a user has granted your application access to their Tesla account in the Connect flow.

  Please see our [FAQs](/help/oem-integrations/tesla/faqs#can-owner-and-driver-accounts-authorize-access-with-smartcar-through-connect) for details on adding a virtual key for accounts with multiple vehicles and different account types.
</Tip>

<Tabs>
  <Tab title="Mobile Device">
    On mobile devices, they will be redirected to the Tesla app and prompted to add the Virtual Key

    <Frame caption="Opening the link on a mobile device with the Tesla app installed">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1aa3cfa6758a83b3c5384019c8ce9516" data-og-width="4964" data-og-height="4854" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=38179fb64a3f35c9c6412881a41f63a2 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=dd132f40eaf0ac8ce3f8c06a4a49937a 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d1f968b7d55de343324b9c34fa1445ae 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=40b9a8fa4ac2c2060da42b5cf08d849b 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=a01aa61cae09b50959b4f8d03936e056 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/mobile.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2978ca715f21ff393c8a6fcd150d6b96 2500w" />
    </Frame>
  </Tab>

  <Tab title="Desktop">
    On Desktop, they will be prompted to scan the QR code which in turn opens up the Tesla app and prompts them to add a Virtual Key

    <Frame caption="Opening the link on a desktop">
      <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d23186ba53fe3df10da5569734e35a55" data-og-width="2000" data-og-height="2283" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=1fef759823638e7e4bef332c9ecc2746 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b540a6e8a73a09c2335212f7e76cc83d 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=925d9141cba67f54650113d5b89eff78 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=fb91f775461570fbf9babf0d1aa09e3f 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=072106f529447f5d80c34d216936f07c 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/desktop.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=c64d864789f7d4e035cc4c50bf2cb7dd 2500w" />
    </Frame>
  </Tab>
</Tabs>

Virtual Key status can be checked at any time from the Tesla infotainment screen under Settings, Locks.

<Frame caption="Check Virtual Key status from your Tesla">
  <img width="600" src="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=2aa353d17ed5cde11109469fd2e0a798" data-og-width="2720" data-og-height="1802" data-path="images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=280&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=79989c8784343f6e73094b0e0ebcf348 280w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=560&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=d8b4063d497c846e867109f96ee6afad 560w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=840&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=4df5837d63f70457f4be3a837ad565d9 840w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1100&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=13e05d49490a3d98848e8045e183fb2c 1100w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=1650&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=b6b2d077092b08c3fb72f852f706d256 1650w, https://mintcdn.com/smartcar-docs/bl2aLGyZU43A919o/images/help-center/oem-integrations/tesla/add-virtual-key/infotainment.png?w=2500&fit=max&auto=format&n=bl2aLGyZU43A919o&q=85&s=990cf7ae17b09c73129ac1eb6cf934ae 2500w" />
</Frame>

## Do all vehicles need a virtual key?

2020 and earlier Model S and X **will not** require a virtual key at this time. Data for these vehicles is refreshed every
5 minutes while the vehicle is awake.

## What if a streaming capable vehicle does not have a virtual key installed?

If a vehicle is streaming capable and does not yet have a virtual key installed,
requests to the vehicle will be limited to 1 request every 8 hours for data. These requests **will
not** wake the vehicle.
