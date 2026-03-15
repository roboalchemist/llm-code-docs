# Source: https://docs.firehydrant.com/docs/other-incident-settings.md

# Other Incident Settings

There are a multitude of other incident settings that are located at **Settings** > **Incident settings**, detailed below.

## Incident Tag Prefixes

When configuring [Incident Tags](https://docs.firehydrant.com/docs/incident-tags), organizations can require specific tag prefixes from responders. This enforces that all tags must start with any of the specified prefixes, which can ensure data cleanliness and consistency. For example:

<Image alt="All tags must start with &#x22;dev-&#x22; or &#x22;prod-&#x22;" align="center" src="https://files.readme.io/9197d41-image.png">
  All tags must start with "dev-" or "prod-"
</Image>

Attempting to set a tag that doesn't fit the above criteria:

<Image alt="You get an error" align="center" width="400px" src="https://files.readme.io/ab6242c-image.png">
  You get an error
</Image>

## Suspect changes window

<Image alt="Example of suspect changes window set to 1 day" align="center" width="650px" src="https://files.readme.io/2f84ab57aab1cd8a2ba794d15566107add45847e63495196eb14005ee787121c-CleanShot_2025-02-10_at_14.43.002x.png">
  Example of suspect changes window set to 1 day
</Image>

FireHydrant's [Change Events](https://docs.firehydrant.com/docs/change-events) offer a powerful way to ingest any changes that occur into your system and associate them with different components of your [Service Catalog](https://docs.firehydrant.com/docs/intro-to-service-catalog). When conducting incidents, FireHydrant will automatically associate recent change events within a certain window of time before the event so responders can look at which changes may have potentially triggered the incident, if any.

The default time window is 1h, or 1 hour before the start of the incident. Users can modify this value as needed.

## Incident nudge duration

<Image alt="Example of nudging set for 1 hour of inactivity" align="center" width="650px" src="https://files.readme.io/2d198fa1339f7717cae22e9228674c2e30524acfa8ea0d6d2160aa6c196de939-CleanShot_2025-02-10_at_14.43.392x.png">
  Example of nudging set for 1 hour of inactivity
</Image>

You can configure FireHydrant to "nudge" or remind users that there's an open incident to which they are assigned role(s). The amount of time of inactivity before nudging can be configured, and as part of nudging, we will also show the nudged user options for handing off their role, which will automatically re-assign all open tasks to the person being handed off to.