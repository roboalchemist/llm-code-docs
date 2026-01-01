## Legacy conditional filters
(See also xref:config*txt.adoc#conditional-filters[config.txt conditional filters].)

### The `[HDMI:*]` filter

NOTE: This filter is for Raspberry Pi 4 only.

Raspberry Pi 4 has two HDMI ports, and for many `config.txt` commands related to HDMI, it is necessary to specify which HDMI port is being referred to. The HDMI conditional filters subsequent HDMI configurations to the specific port.

[source]
```
 [HDMI:0]
   hdmi*group=2
   hdmi*mode=45
 [HDMI:1]
   hdmi*group=2
   hdmi*mode=67
```

An alternative `variable:index` syntax is available on all port-specific HDMI commands. You could use the following, which is the same as the previous example:

[source]
```
 hdmi*group:0=2
 hdmi*mode:0=45
 hdmi*group:1=2
 hdmi_mode:1=67
```