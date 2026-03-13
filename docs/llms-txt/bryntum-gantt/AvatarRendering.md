# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/util/AvatarRendering.md

# [AvatarRendering](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering)

A utility class providing rendering of avatars / resource initials.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[element](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#config-element)
Element used to listen for load errors. Normally the owning widgets own element.

[colorPrefix](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#config-colorPrefix)
Prefix prepended to a supplied color to create a CSS class applied when showing initials.

[tooltip](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#config-tooltip)
A tooltip config object to enable using a custom tooltip for the avatars. Listen for `beforeShow` and set your html there.

[size](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#config-size)
The requested size of the avatars. If not null then the size is added as width and height to the avatar element whether it is image or initials container

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isAvatarRendering](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#property-isAvatarRendering)
Identifies an object as an instance of [AvatarRendering](https://bryntum.com/docs/gantt/api/#Core/widget/util/AvatarRendering) class, or subclass thereof.

[isAvatarRendering](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#property-isAvatarRendering-static)
Identifies an object as an instance of [AvatarRendering](https://bryntum.com/docs/gantt/api/#Core/widget/util/AvatarRendering) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getResourceAvatar](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#function-getResourceAvatar)
Returns a DOM config object containing a resource avatar, icon or resource initials. Display priority in that order.

## Typedefs

Typedefs are type definitions for the class

[AvatarConfig](https://bryntum.com/docs/gantt/api/Core/widget/util/AvatarRendering#typedef-AvatarConfig)
An object that describes properties of an avatar.
