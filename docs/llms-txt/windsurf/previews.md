# Source: https://docs.windsurf.com/windsurf/previews.md

# Windsurf Previews

Windsurf Previews allow you to view the local deployment of your app either in the IDE or in the browser (optimized for Google Chrome, Arc, and Chromium based browsers) with listeners, allowing you to iterate rapidly by easily sending elements and errors back to Cascade as context.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/browser-preview-demo.mp4?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b3befa08affd8c5c10a84ae9259d0f15" data-path="assets/windsurf/previews/browser-preview-demo.mp4" />

Windsurf Previews are opened via tool call, so just ask Cascade to preview your site to get started. Alternatively, you can also click the Web icon in the Cascade toolbar to automatically propagate the natural language prompt to enter the proxy.

<Frame style={{ border: 'none', background: 'none' }}>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6a607c6a7beaafe915760d80a78c8da6" data-og-width="392" width="392" data-og-height="216" height="216" data-path="assets/windsurf/previews/website-tools-icon.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=7222fc826af6a55cb824fb3fce30ce84 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=bfbfb672a37d24ef3f11a52c62ae050c 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=bae2bad59e313d1fe53e47c3c9141f5b 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=a3cafe879660aa08f70dca8e269a3032 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=038211eef5f4587cfced6ea316d62ec9 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/previews/website-tools-icon.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=9dff09c4af8de6a34ec980815bdc13cd 2500w" />
</Frame>

# Send Elements to Cascade

In the Preview, you can select and send elements/components and errors directly to Cascade. Simply click on the "Send element" button on the bottom right and then proceed to select the element you want to send.

The selected element will be inserted into your current Cascade prompt as an `@ mention`. You can add as many elements as you want in the prompt.

# In-IDE Preview

Windsurf can open a up a Preview as a new tab in your editor. This is a simple web view that enables you to view web app alongside your Cascade panel.

Because these Previews are hosted locally, you can open them in your system browser as well, complete with all the listeners and ability to select and send elements and console errors to Cascade.

<Warning>The listeners and the abilities to send elements and errors are optimized for Google Chrome, Arc, and Chromium based browsers.</Warning>

# How to Disable

You can disable Windsurf Previews from Windsurf - Settings. This will prevent Cascade from making this tool call.
