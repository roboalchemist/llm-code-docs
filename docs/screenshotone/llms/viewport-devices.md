# Source: https://screenshotone.com/docs/viewport-devices/

# Devices

import Alert from "@/components/Alert.astro";
import devices from "screenshotone-devices";

Instead of manually specifying viewport parameters like width and height, you can specify a device to use for emulation. In addition, other parameters of the viewport, including the user agent, will be set automatically. 

The [viewport_device](/docs/options/#viewport_device) option sets the next options for you: [viewport_width](/docs/options/#viewport_width), [viewport_height](/docs/options/#viewport_height), [device_scale_factor](/docs/options/#device_scale_factor), [viewport_mobile](/docs/options/#viewport_mobile), [viewport_has_touch](/docs/options/#viewport_has_touch), [viewport_landscape](/docs/options/#viewport_landscape). You can change these options and override the ones set by the `viewport_device` option. 

<Alert>
API does not use an actual device to take a screenshot. It is emulation that works in most cases. 
</Alert>

Use the `id` property of the device as the [viewport_device](/docs/options/#viewport_device) option, e.g. `viewport_device=galaxy_s9+_landscape`.

You can get the list of supported devices by:

```
GET https://api.screenshotone.com/devices?access_key=<YOUR ACCESS KEY>`

[
    {
        "id": "iphone_13_pro_max_landscape",
        "name": "iPhone 13 Pro Max landscape",
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
        "viewport": {
            "width": 926,
            "height": 428,
            "deviceScaleFactor": 3,
            "isMobile": true,
            "hasTouch": true,
            "isLandscape": true
        }
    },
    // ... many devices ... 
    {
        "id": "galaxy_s9+",
        "name": "Galaxy S9+",
        "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
        "viewport": {
            "width": 320,
            "height": 658,
            "deviceScaleFactor": 4.5,
            "isMobile": true,
            "hasTouch": true,
            "isLandscape": false
        }
    },
    {
        "id": "galaxy_s9+_landscape",
        "name": "Galaxy S9+ landscape",
        "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
        "viewport": {
            "width": 658,
            "height": 320,
            "deviceScaleFactor": 4.5,
            "isMobile": true,
            "hasTouch": true,
            "isLandscape": true
        }
    }, 
    // ... many devices ... 
]
```

## Devices

The list of devices returned by API is dynamic and continuously updated. But there is a snapshot of all supported devices if you want to take a quick look (**don't rely on it solely, use the API method** `GET /devices` **instead**): 


<table class="table-sm table-sm mt-2 mb-4">
    <thead>
        <tr>
            <th rowspan="2" class="text-center">Device (id)</th>
            <th class="text-center">Viewport (scale)</th>
            <th class="text-center">Mobile</th>
            <th class="text-center">Touch</th>
            <th class="text-center">Landscape</th>
        </tr>
        <tr>
            <th colspan="5" class="text-center">User Agent</th>
        </tr>
    </thead>
    <tbody>
        {Object.entries(devices.default.devices).map(([id, device]) => (
            <>
            <tr class="text-sm">
                <td rowspan="2" class="text-center small">{device.name} ({id})</td>
                <td class="text-center">{device.viewport.width}x{device.viewport.height} ({device.viewport.deviceScaleFactor})</td>
                <td class="text-center">
                    {device.viewport.isMobile ? "Yes" : "No"}
                </td>
                <td class="text-center">
                    {device.viewport.hasTouch ? "Yes" : "No"}
                </td>
                <td class="text-center">
                    {device.viewport.isLandscape ? "Yes" : "No"}
                </td>               
            </tr>
            <tr class="text-sm">
                <td colspan="5" class="text-center">{device.userAgent}</td>
            </tr>
            </>
        ))}

</tbody>    
</table>