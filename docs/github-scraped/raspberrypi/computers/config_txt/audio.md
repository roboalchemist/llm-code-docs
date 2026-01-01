## Onboard analogue audio (3.5 mm jack)

The onboard audio output uses config options to change the way the analogue audio is driven, and whether some firmware features are enabled or not.

### `audio*pwm*mode`

`audio*pwm*mode=1` selects legacy low-quality analogue audio from the 3.5 mm AV jack.

`audio*pwm*mode=2` (the default) selects high quality analogue audio using an advanced modulation scheme.

NOTE: This option uses more GPU compute resources and can interfere with some use cases on some models.

### `disable*audio*dither`

By default, a 1.0LSB dither is applied to the audio stream if it is routed to the analogue audio output. This can create audible background hiss in some situations, for example when the ALSA volume is set to a low level. Set `disable*audio*dither` to `1` to disable dither application.

### `enable*audio*dither`

Audio dither (see disable*audio*dither above) is normally disabled when the audio samples are larger than 16 bits. Set this option to `1` to force the use of dithering for all bit depths.

### `pwm*sample*bits`

The `pwm*sample*bits` command adjusts the bit depth of the analogue audio output. The default bit depth is `11`. Selecting bit depths below `8` will result in nonfunctional audio, as settings below `8` result in a PLL frequency too low to support. This is generally only useful as a demonstration of how bit depth affects quantisation noise.

## HDMI audio

By default, HDMI audio output is enabled on all Raspberry Pi models with HDMI output.

To disable HDMI audio output, append `,noaudio` to the end of the `dtoverlay=vc4-kms-v3d` line in xref:../computers/config_txt.adoc#what-is-config-txt[`/boot/firmware/config.txt`]:

```ini
dtoverlay=vc4-kms-v3d,noaudio
```