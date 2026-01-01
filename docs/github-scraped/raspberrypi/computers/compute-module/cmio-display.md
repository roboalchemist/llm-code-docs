## Attaching the Touch Display LCD panel

Update your system software and firmware to the latest version before starting. Compute Modules mostly use the same process, but sometimes physical differences force changes for a particular model.

### Connect a display to DISP1/DSI1

NOTE: The Raspberry Pi Zero camera cable can't be used as an alternative to the RPI-DISPLAY adapter. The two cables have distinct wiring.

To connect a display to `DISP1/DSI1`:

1. Disconnect the Compute Module from power.
1. Connect the display to the `DISP1/DSI1` port on the Compute Module IO board through the 22 W to 15 W display adapter.
1. Complete the appropriate jumper connections:
  - For **CM1**, **CM3**, **CM3+**, and **CM4S**, connect the following GPIO pins with jumper cables:
    ** `0` to `CD1*SDA`
    ** `1` to `CD1*SCL`
  - For **CM5**, on the Compute Module 5 IO board, add the appropriate jumpers to J6, as indicated on the silkscreen.
1. Reconnect the Compute Module to power.
1. Add `dtoverlay=vc4-kms-dsi-7inch` to xref:../computers/config*txt.adoc#what-is-config-txt[`/boot/firmware/config.txt`].
1. Reboot your Compute Module with `sudo reboot`. Your device should detect and begin displaying output to your display.

### Connect a display to DISP0/DSI0

To connect a display to `DISP0/DSI0` on CM1, CM3, and CM4 IO boards:

1. Connect the display to the `DISP0/DSI0` port on the Compute Module IO board through the 22 W to 15 W display adapter.
1. Complete the appropriate jumper connections:
  - For **CM1**, **CM3**, **CM3+**, and **CM4S**, connect the following GPIO pins with jumper cables:
    ** `28` to `CD0*SDA`
    ** `29` to `CD0*SCL`
  - For **CM4**, on the Compute Module 4 IO board, add the appropriate jumpers to J6, as indicated on the silkscreen.
1. Reconnect the Compute Module to power.
1. Add `dtoverlay=vc4-kms-dsi-7inch,dsi0` to `/boot/firmware/config.txt`.
1. Reboot your Compute Module with `sudo reboot`. Your device should detect and begin displaying output to your display.

### Disable touchscreen

The touchscreen requires no additional configuration. Connect it to your Compute Module; both the touchscreen element and display work  when successfully detected.

To disable the touchscreen element, but still use the display, add the following line to `/boot/firmware/config.txt`:

```ini
disable*touchscreen=1
```

### Disable display

To entirely ignore the display when connected, add the following line to `/boot/firmware/config.txt`:

```ini
ignore_lcd=1
```

## Attaching the Touch Display 2 LCD panel

Touch Display 2 is an LCD display designed for Raspberry Pi devices (see https://www.raspberrypi.com/products/touch-display-2/). It's available in two sizes: 5 inches or 7 inches (diagonally). For more information about these options, see **Specifications** in xref:../accessories/touch-display-2.adoc[Touch Display 2].

Regardless of the size that you use, Touch Display 2 connects in the same way as the original Touch Display, but the software setup on Compute Modules is slightly different because it uses a different display driver. For connection details, see **Connectors** in xref:../accessories/touch-display-2.adoc[Touch Display 2].

To enable Touch Display 2 on `DISP1/DSI1`, edit the `/boot/firmware/config.txt` file to add the following. You must also add jumpers to J6 as indicated on the silkscreen.

- For the **5-inch** display: `dtoverlay=vc4-kms-dsi-ili9881-5inch`
- For the **7-inch** display: `dtoverlay=vc4-kms-dsi-ili9881-7inch`

To use `DISP0/DSI0`, append `,dsi0` to the overlay name.

- For the **5-inch** display: `dtoverlay=vc4-kms-dsi-ili9881-5inch,dsi0`
- For the **7-inch** display: `dtoverlay=vc4-kms-dsi-ili9881-7inch,dsi0`