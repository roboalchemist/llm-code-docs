:github_url: hide



# CameraServer

**Inherits:** [Object<class_Object>]

Server keeping track of different cameras accessible in Godot.


## Description

The **CameraServer** keeps track of different cameras accessible in Godot. These are external cameras such as webcams or the cameras on your phone.

It is notably used to provide AR modules with a video feed from the camera.

\ **Note:** This class is currently only implemented on Linux, Android, macOS, and iOS. On other platforms no [CameraFeed<class_CameraFeed>]\ s will be available. To get a [CameraFeed<class_CameraFeed>] on iOS, the camera plugin from [godot-ios-plugins ](https://github.com/godotengine/godot-ios-plugins)_ is required.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>` | :ref:`monitoring_feeds<class_CameraServer_property_monitoring_feeds>` | ``false`` |
> +-------------------------+-----------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`add_feed<class_CameraServer_method_add_feed>`\ (\ feed\: :ref:`CameraFeed<class_CameraFeed>`\ )       |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`CameraFeed<class_CameraFeed>`\] | :ref:`feeds<class_CameraServer_method_feeds>`\ (\ )                                                         |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`CameraFeed<class_CameraFeed>`                              | :ref:`get_feed<class_CameraServer_method_get_feed>`\ (\ index\: :ref:`int<class_int>`\ )                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`get_feed_count<class_CameraServer_method_get_feed_count>`\ (\ )                                       |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
> | |void|                                                           | :ref:`remove_feed<class_CameraServer_method_remove_feed>`\ (\ feed\: :ref:`CameraFeed<class_CameraFeed>`\ ) |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**camera_feed_added**\ (\ id\: [int<class_int>]\ ) [🔗<class_CameraServer_signal_camera_feed_added>]

Emitted when a [CameraFeed<class_CameraFeed>] is added (e.g. a webcam is plugged in).


----



**camera_feed_removed**\ (\ id\: [int<class_int>]\ ) [🔗<class_CameraServer_signal_camera_feed_removed>]

Emitted when a [CameraFeed<class_CameraFeed>] is removed (e.g. a webcam is unplugged).


----



**camera_feeds_updated**\ (\ ) [🔗<class_CameraServer_signal_camera_feeds_updated>]

Emitted when camera feeds are updated.


----


## Enumerations



enum **FeedImage**: [🔗<enum_CameraServer_FeedImage>]



[FeedImage<enum_CameraServer_FeedImage>] **FEED_RGBA_IMAGE** = `0`

The RGBA camera image.



[FeedImage<enum_CameraServer_FeedImage>] **FEED_YCBCR_IMAGE** = `0`

The [YCbCr ](https://en.wikipedia.org/wiki/YCbCr)_ camera image.



[FeedImage<enum_CameraServer_FeedImage>] **FEED_Y_IMAGE** = `0`

The Y component camera image.



[FeedImage<enum_CameraServer_FeedImage>] **FEED_CBCR_IMAGE** = `1`

The CbCr component camera image.


----


## Property Descriptions



[bool<class_bool>] **monitoring_feeds** = `false` [🔗<class_CameraServer_property_monitoring_feeds>]


- |void| **set_monitoring_feeds**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_monitoring_feeds**\ (\ )

If `true`, the server is actively monitoring available camera feeds.

This has a performance cost, so only set it to `true` when you're actively accessing the camera.

\ **Note:** After setting it to `true`, you can receive updated camera feeds through the [camera_feeds_updated<class_CameraServer_signal_camera_feeds_updated>] signal.


> **TABS**
>

    func _ready():
        CameraServer.camera_feeds_updated.connect(_on_camera_feeds_updated)
        CameraServer.monitoring_feeds = true

    func _on_camera_feeds_updated():
        var feeds = CameraServer.feeds()


    public override void _Ready()
    {
        CameraServer.CameraFeedsUpdated += OnCameraFeedsUpdated;
        CameraServer.MonitoringFeeds = true;
    }

    void OnCameraFeedsUpdated()
    {
        var feeds = CameraServer.Feeds();
    }




----


## Method Descriptions



|void| **add_feed**\ (\ feed\: [CameraFeed<class_CameraFeed>]\ ) [🔗<class_CameraServer_method_add_feed>]

Adds the camera `feed` to the camera server.


----



[Array<class_Array>]\[[CameraFeed<class_CameraFeed>]\] **feeds**\ (\ ) [🔗<class_CameraServer_method_feeds>]

Returns an array of [CameraFeed<class_CameraFeed>]\ s.


----



[CameraFeed<class_CameraFeed>] **get_feed**\ (\ index\: [int<class_int>]\ ) [🔗<class_CameraServer_method_get_feed>]

Returns the [CameraFeed<class_CameraFeed>] corresponding to the camera with the given `index`.


----



[int<class_int>] **get_feed_count**\ (\ ) [🔗<class_CameraServer_method_get_feed_count>]

Returns the number of [CameraFeed<class_CameraFeed>]\ s registered.


----



|void| **remove_feed**\ (\ feed\: [CameraFeed<class_CameraFeed>]\ ) [🔗<class_CameraServer_method_remove_feed>]

Removes the specified camera `feed`.

