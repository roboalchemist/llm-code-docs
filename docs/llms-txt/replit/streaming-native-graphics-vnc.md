# Source: https://docs.replit.com/additional-resources/streaming-native-graphics-vnc.md

# Streaming native graphics using VNC

> Replit offers virtual network computing (VNC) functionality. VNC is a mature virtual desktop protocol that allows your Replit App to stream a native desktop to your web browser. This protocol allows native applications (developed in Python, Java, C++, etc.) to open desktop windows as they would on any physical computer.

This streaming technology allows you to work with legacy applications in your browser from any device! For example, you could run a Python-powered game designed for desktop right on your mobile phone or tablet without making any changes to the underlying code.

<a href="https://replit.com/@demcrepl/Tetris-in-Pygame" target="_blank">Tetris (powered by PyGame)</a>

<img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ddf138f52d698a6baa7532ad74e88492" alt="image of Tetris in a Replit App" data-og-width="2055" width="2055" data-og-height="1057" height="1057" data-path="images/vnc/tetris.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3d18d886cc73e0e3663c15d392944faf 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b2115704452192c93cefc53928253dc6 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=0419e3226af935fa6aed7914f5650808 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=26c537ff53adfee91804243ebc6d8183 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c333d75b2045bc73c42af78b4a54cd3c 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/tetris.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6aa2d23257e86189c1585e276c758b74 2500w" />

## How Can I Use VNC?

Any Replit App – in any language – can use a virtual desktop. No changes are needed to execute native graphics programs on Replit. The VNC pane will appear when any application attempts to open a native desktop window.

## Securing Your Replit App

By default, your VNC connection does not have a password and can only be accessed from [https://replit.com](https://replit.com) since the connection relies on the same authentication used for the WebSocket. If you need to access your Replit App via the external [noVNC](https://novnc.com) client, you can set a VNC password.

Set a password in your Replit App [secrets](/replit-workspace/workspace-features/secrets) configuration. `Secrets` is a secure place to store passwords without the fear of other users accessing your passwords. Setting `VNC_PASSWORD` will add enhanced security when connecting remotely.

## How Can I Use Fullscreen VNC?

You must have secured your Replit App as instructed above to proceed with these steps.

1. Execute the following command in your "Shell" tab:
   ```sh  theme={null}
   echo $REPL_ID
   ```

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=45fcde093041183e77ba334b780e69ed" alt="image showing the echo command" data-og-width="628" width="628" data-og-height="174" height="174" data-path="images/vnc/replid.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2c4d3cf33ad5c6dbf8bac35fa831831c 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=279e68ac7cd4d55d3990d61acb396186 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cf365abf0511b5a0ef8afeb3c7c59e64 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=72140ebbeb696f060cebaa0602cd156c 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c5ff128421866a1ac394e95e66f9a20a 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/replid.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b147d26cce520f466f3d1fab0f453779 2500w" />
</Frame>

2. Construct your connection URL by replacing `REPL_ID` in with the output from above: `<\REPL_ID\>.id.repl.co`
3. Open the [noVNC client](https://novnc.com/noVNC/vnc.html) in a separate browser tab.
4. Open connection settings.

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1f46fa987102bf1bb95ea027d6b3f43d" alt="open connection settings" data-og-width="126" width="126" data-og-height="302" height="302" data-path="images/vnc/settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=64a3498b1e8262b6ddd885106ee7ac29 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=74acc21da0a56c3dd211eeee8a6f4e06 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f90f9530040a4b9001dc42543534c03b 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=bb561d1d227e70e425d4e04dbbd53e1b 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6c9cd76ca08e9c47b1c29c5e6865041c 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/settings.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6aa73502d35e79740853f7055a4063ec 2500w" />
</Frame>

5. Expand the WebSockets field. Enter your connection URL (`\<REPL_ID\>.id.repl.co`) in the `host` field, and leave the `path` field empty.

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e1a6420a7573bb6f0e7a327ecd89b60d" alt="host" data-og-width="214" width="214" data-og-height="230" height="230" data-path="images/vnc/host.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8d59ba56af397b9277f36847b3131b61 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=47878ae88796b9062194945e05ce8f45 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=fa817238ff8b42a51767950ba6752aec 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=bfd05b862930324281dc8c38601bc263 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=34095f96b0f29bca83bceec2bca7ef0b 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/host.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e4ac70cce1e816d988cfb404e8136ad0 2500w" />
</Frame>

6. Change the `Scaling Mode` to `Remote Resizing`:

<Frame>
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cc7bcd3ec3d8c5cf801d537eef6a2b16" alt="scaling" data-og-width="147" width="147" data-og-height="74" height="74" data-path="images/vnc/scaling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ad3b2b665c2bc724ae6ad3ec418f1634 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9a69d8515a3328e010c9e1b4131505f8 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b8971d15741b8fc114b9502c316413be 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=29ef9f501af31364c4fe4eddaaae3ca4 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=416abafe4b3bce3f2dcb82ed7d081e61 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/vnc/scaling.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=64ea0b0d7ff305921f296220afb8e24e 2500w" />
</Frame>

7. Use the `runner` username and the password configured above when asked for credentials.

## Examples

* <a href="https://replit.com/@demcrepl/Tetris-in-Pygame" target="_blank">PyGame</a>
* <a href="https://replit.com/@amasad-matplotlib" target="_blank">Python matplotlib</a>
* <a href="https://replit.com/@sigcse2021/Game-of-Life-demcrepl" target="_blank">Java Processing</a>
