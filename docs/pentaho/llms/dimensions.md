# Source: https://docs.pentaho.com/pba-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/dimensions.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/dimensions.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/dimensions.md

# Dimensions

Due to the inclusion of Bootstrap libraries, the configuration of the columns in the layout is simple. The columns in a row must occupy 12 spans, such that in a single row you could have the following sample configurations:

* Twelve columns of size 1 (12x1)
* Two columns of size 6 (2x6)
* Three columns of size 4 (3x4)
* One column of size 8 and one column of size 4 (8+4)

Whatever your configuration, the spans must add up to 12 for Bootstrap. Other CSS libraries may have different rules. For instance, in the case of the Blueprint library, the total number of spans in a column is 24.

You can assign the width of a column across multiple devices where you will draw the components through the properties:

| Category            | Suggested Device | Width (in pixels) |
| ------------------- | ---------------- | ----------------- |
| Extra Small Devices | Phones           | <768              |
| Small Devices       | Tablets          | 768-992           |
| Medium Devices      | Desktops         | 992-1200          |
| Large Devices       | Desktops         | >1200             |

You only need to assign values to one of these types of devices. If you do not need to have a responsive dashboard, you can set the values only for the ‘Extra Small Devices’, for example. That way, all the other devices will inherit the layout that you assign for that category. However, if you need a responsive dashboard which will fit well in a mobile phone and also in a desktop, you can specify a different layout for each device, assigning different values for the ‘Extra Small Devices’ and the ‘Medium Devices’ categories. For more information, visit <http://getbootstrap.com/css/#grid>.

**Note:** While these properties are specified in Bootstrap units, the height for the rows has to be supplied in pixels.
