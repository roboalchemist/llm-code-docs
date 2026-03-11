# Source: https://www.hammerdb.com/docs4.0/ch01s10.html

Title: 10. Themes and Scalable Graphics

URL Source: https://www.hammerdb.com/docs4.0/ch01s10.html

Markdown Content:
HammerDB v4.0 includes an updated graphical interface that adapts to scale to UHD displays such as Microsoft pixelsense displays. The behaviour of the display is set in the theme section of generic.xml.

<theme>
<scaling>auto</scaling>
<scaletheme>auto</scaletheme>
<pixelsperpoint>auto</pixelsperpoint>
</theme>
By default scaling, the scaletheme and pixelsperpoint are all set to auto. This means that HammerDB will detect the display settings and scale the interface accordingly. For example the image shows HammerDB v3.3 and v4.0 on the same UHD display.

**Figure 1.16.Scaling Graphics**

![Image 1: Scaling Graphics](https://www.hammerdb.com/docs4.0/resources/ch1-18.PNG)

However some displays or third-party X Windows servers may not be updated to support scalable graphics. In this case the scaling value can be set to fixed and a standard 96 dpi display will be used with the fixed themes from HammerDB v3.3.

<theme>
<scaling>fixed</scaling>
<scaletheme>auto</scaletheme>
<pixelsperpoint>auto</pixelsperpoint>
</theme>
The scaletheme value will accept settings of "auto", "awlight", "arc" or "breeze". If set to the default of "auto", "awlight" will be used on Linux.

**Figure 1.17.Linux Theme Awlight**

![Image 2: Linux Theme Awlight](https://www.hammerdb.com/docs4.0/resources/ch1-19.PNG)

and "breeze" on Windows.

**Figure 1.18.Windows Theme Breeze**

![Image 3: Windows Theme Breeze](https://www.hammerdb.com/docs4.0/resources/ch1-9.PNG)

The scale factor can be fine-tuned by setting the pixelsperpoint value. By running the command puts [ tk scaling ] in the console you can determine the current value. By setting this value slightly larger or smaller than the default you can adjust the scaling to your system. This value is not intended for large scale changes from the default as settings have been adjusted to the detected value.

(HammerDB-4.0) 49 % puts [ tk scaling ]
1.3333333333333333
