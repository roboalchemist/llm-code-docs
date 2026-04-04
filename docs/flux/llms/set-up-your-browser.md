# Source: https://docs.flux.ai/Introduction/set-up-your-browser.md

# Setting up your browser

Flux runs entirely in your browser, so there are a few things we need to configure to ensure the best possible experience:

1. Enable WebGL
2. Set zoom to 100%
3. Update your browser
4. Browser Plugins
5. Firewalls

### Enable WebGL

To run Flux you are going to have to use a device/browser that supports hardware accelerated WebGL...otherwise you are in for a bad time and your CPU will turn into a room heater or the app will flat out not work at all.

Good news is that devices build in the last 5 years support WebGL just fine and you should be good to go without having to do anything. But for the small chance that you are having issues here is a list of things to check:

#### First: Test to see if WebGL is the problem

Flux uses WebGL2, to find out if WebGL2 is causing the problem, open a browser window and head to [https://get.webgl.org/webgl2/](https://get.webgl.org/webgl2/). **If you DO NOT see a spinning cube,** you can try a couple things depending on your browser before [filing an issue](https://feedback.flux.ai/).

#### Graphics card drivers

On Windows/Linux there is a lot of funky Graphics Card drivers available which might work or not, or just partially work sometimes. We therefore recommend that you use the official stable and certified drivers that come with your operating system. If that doesn't do the trick then use the latest stable and certified drivers that the manufacturer of your graphic cards provides!

If you are using a OSX or iOS device, don't worry...you are all set and good to go out of the box.

#### Chrome

**Check WebGL status**

1. Next, go to chrome://gpu
2. Under the "Graphics Feature Status" list, find WebGL to learn its status.
    1. If it says "Hardware accelerated" then WebGL is running on the graphics card.
    2. If the status is not "Hardware accelerated", then the Problems Detected list (below the the Graphics Feature Status list) may explain why hardware acceleration is unavailable.

**Enable** **WebGL**

1. Open Chrome and go to the Chrome Settings page:
    1. **macOS:** Go to **Chrome Settings** in the menu bar
    2. **Windows:** Go to **File** &gt; **Preferences** or click the vertical ellipses in the top right corner and choose **Settings**.

2. Scroll down and click on the **Advanced** link to expand the settings. In the **System** section, enable **Use hardware acceleration when available**
3. If WebGL isn't currently enabled, you can head to your Chrome Flags settings by typing the URL **[chrome://flags/. ](chrome://flags/)**Update the **Override software rendering list** to "enabled".

#### Firefox

**Enable** **WebGL**

1. Open a browser window in Firefox. Type "about:config" in the URL address bar.
2. In the search box, type "webgl.disabled"
3. The value should be false if WebGL is enabled.

Please note that making any changes in the Firefox configuration area could adversely impact your system.

#### Safari

WebGL is enabled by default in Safari.

#### Edge

**Check WebGL**

1. Next, go to edge://gpu
2. Under the "Graphics Feature Status" list, find WebGL to learn its status.
    1. If it says "Hardware accelerated" then WebGL is running on the graphics card.
    2. If the status is not "Hardware accelerated", then the Problems Detected list (below the the Graphics Feature Status list) may explain why hardware acceleration is unavailable.

**Enable WebGL**

In an Edge browser window, type edge://settings/system in the URL field.

Ensure that "Use hardware acceleration when available" is checked. If you need to check it, be sure to restart your browser afterward so the change takes effect.

## Set Zoom to 100%

#### Chrome

Click on the three dots/stripes menu on the top right and find the **"Zoom"** section. Make sure it's 100%.

![](https://uploads.developerhub.io/prod/86Yw/hqncbn918vad5buizbdlxcjbm6ebin6wmn7yccyzj4wylplsnyth4n6cmlx6xfxu.png)

#### Firefox

Click on the three-stripes menu on the top right and find the **"Zoom"** section. Make sure it's 100%.

![](https://uploads.developerhub.io/prod/86Yw/p4g3675rtg7f795ankcmu223ee1tu89ruebzp259c4ig8fg4g8i3qg5cosatghzv.png)

#### Safari

Go to the **"View"** menu at the top of the screen. Make sure the zoom is set to **"Actual Size"**.

![](https://uploads.developerhub.io/prod/86Yw/mtcv2klrxs9cxp1zb6dmvu8kowmv0y3yda781nl22lw8rp1gxnpcglp38wxtirk3.png)

## Update your browser

Most browsers update automatically. If you're not sure your browser is running the latest version, please visit [www.whatismybrowser.com](https://www.whatismybrowser.com/). If you see a red banner saying your browser is not up to date, click on it to get instructions on how to update it. 

## Browser Plugins

Browser plugins can cause trouble like degrading performance, causing some Flux features to not work or the all as a whole not to work.

If you wanna be safe then just disable all browser plugins for the *.flux.ai domain.

#### Plugins known to cause issues

- Ad blockers like Ublock

## Firewalls

Firewalls or Browser Plugins that block IPs or Domains can cause issues. For example parts of the Flux backend are hosted with Google Cloud and some corporate firewalls and Ad Blocker browser plugins might be too aggressive and block critical access for Flux.

Therefore please ensure to configure firewalls accordingly and disable plugins like Ad Blocker when using Flux.

#### Ways to bypass firewalls

- Use a VPN like [NordVPN](https://nordvpn.com/), [SkyVPN](https://www.skyvpn.net/), [Mullvad](https://mullvad.net/en) or [TunnelBear](https://www.tunnelbear.com/)
- Reach out to your corporate network admin

---

Your browser is now ready to use Flux. Let's begin by [Your First PCB in Flux: Complete Design Walkthrough](https://docs.flux.ai/flux/Introduction/flux-walkthrough-project).