# Source: https://developers.activecampaign.com/docs/configuration-specification-v2.md

# Reference

An App configuration is a JSON object with five main sections.

* [auth](https://developers.activecampaign.com/docs/auth): Defines how ActiveCampaign authenticates with the integrating system's API.
* [api](https://developers.activecampaign.com/docs/api): Defines the common URL for the integrating system's API and any support for pagination required.
* [data\_intake](https://developers.activecampaign.com/docs/data_intake): Defines how to bring *inbound* data into ActiveCampaign from the integrating system's webhooks or API.
* [workflows](https://developers.activecampaign.com/docs/workflows): Defines the steps and custom configuration required to setup an *inbound* or *outbound* integration between ActiveCampaign and the integrating system.
* [objects Array](https://developers.activecampaign.com/docs/custom-objects): Defines Custom Objects schema, mappings, and transformations to support additional data required for the integration.

For more information on syntax, see the [Commands and Variables](https://developers.activecampaign.com/docs/commands-1) .

<Embed url="https://activecampaign-help.wistia.com/medias/blr69vhuyu" title="Create Your First CX App in 9 Minutes!" favicon="https://activecampaign-help.wistia.com/favicon.ico" image="https://embed-ssl.wistia.com/deliveries/8c488dea22a5c1bbe8aaec073d80fc73.jpg?image_crop_resized=960x540" provider="activecampaign-help.wistia.com" href="https://activecampaign-help.wistia.com/medias/blr69vhuyu" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Ffast.wistia.net%252Fembed%252Fiframe%252Fblr69vhuyu%26display_name%3DWistia%252C%2BInc.%26url%3Dhttps%253A%252F%252Factivecampaign-help.wistia.com%252Fmedias%252Fblr69vhuyu%26image%3Dhttps%253A%252F%252Fembed-ssl.wistia.com%252Fdeliveries%252F8c488dea22a5c1bbe8aaec073d80fc73.jpg%253Fimage_crop_resized%253D960x540%26key%3D02466f963b9b4bb8845a05b53d3235d7%26type%3Dtext%252Fhtml%26schema%3Dwistia%22%20width%3D%22960%22%20height%3D%22540%22%20scrolling%3D%22no%22%20title%3D%22Wistia%2C%20Inc.%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />