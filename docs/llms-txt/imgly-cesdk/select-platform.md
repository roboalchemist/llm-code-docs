# Source: https://img.ly/docs/cesdk/select-platform/

---
title: "Get Started With CreativeEditor SDK"
description: "Get Started with CE.SDK"
platform: unknown
url: "https://img.ly/docs/cesdk//select-platform/"
---


Select your platform to get started with the CreativeEditor SDK (CE.SDK) and
bring powerful photo, video, and design editing capabilities into your
application.

## Mobile

{
  PLATFORMS.sort(
    // sort alphabetically by label
    (a, b) => a.label.localeCompare(b.label)
  ).filter(p => p.groups.includes("Mobile")).map((platform) => (
    <PlatformCard
      key={platform.id}
      href={props.pathsByPlatform[platform.id]['e18f40']}
      icon={platform.id}
      title={platform.label}
    />
  ))
}

## Web

{PLATFORMS.filter(p => p.groups.includes('Web')).map(platform => (
    <PlatformCard
      key={platform.id}
      href={props.pathsByPlatform[platform.id]['e18f40']}
      icon={platform.id}
      title={platform.label}
    />
  ))}

## Desktop

{PLATFORMS.filter(p => p.groups.includes('Desktop')).map(platform => (
    <PlatformCard
      key={platform.id}
      href={props.pathsByPlatform[platform.id]['e18f40']}
      icon={platform.id}
      title={platform.label}
    />
  ))}

## Server

{
  PLATFORMS.filter(p => p.groups.includes("Server")).map((platform) => (
    <PlatformCard
      key={platform.id}
      href={props.pathsByPlatform[platform.id]['e18f40']}
      icon={platform.id}
      title={platform.label}
    />
  ))
}


