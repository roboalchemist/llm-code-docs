#    name: org.net_mydomain_MyApp.SingleInstance # Remember to change net_mydomain_MyApp to your app ID with "_" instead of "." and "-"

package-repositories:
  - type: apt
    components: [main]
    suites: [noble]
    key-id: 78E1918602959B9C59103100F1831DDAFC42E99D
    url: http://ppa.launchpad.net/snappy-dev/snapcraft-daily/ubuntu

parts:
  build-app:
    plugin: dump
    build-snaps:
      - node/20/stable
      - rustup/latest/stable
    build-packages:
      - libwebkit2gtk-4.1-dev
      - build-essential
      - curl
      - wget
      - file
      - libxdo-dev
      - libssl-dev
      - libayatana-appindicator3-dev
      - librsvg2-dev
      - dpkg
    stage-packages:
      - libwebkit2gtk-4.1-0
      - libayatana-appindicator3-1
    source: .
    override-build: |
      set -eu
      npm install
      npm run tauri build -- --bundles deb
      dpkg -x src-tauri/target/release/bundle/deb/*.deb $SNAPCRAFT_PART_INSTALL/
      sed -i -e "s|Icon=appname|Icon=/usr/share/icons/hicolor/32x32/apps/appname.png|g" $SNAPCRAFT_PART_INSTALL/usr/share/applications/appname.desktop
```

### Explanation

- The `name` variable defines the name of your app and is required to be set to the name that you have registered earlier.
- The `base` variable defines which core you are using.
- The `version` variable defines the version, and should be updated with each change to the source repository.
- The `apps` section allows you to expose the desktop and binary files to allow the user to run your app.
- The `package-repositories` section allows you to add a package repository to help you satisfy your dependencies.
- `build-packages`/`build-snaps` defines the build dependencies for your snap.
- `stage-packages`/`stage-snaps` defines the runtime dependencies for your snap.
- The `override-build` section runs a series of commands after the sources were pulled.

## Building

```sh
sudo snapcraft
```

## Testing

{/* TODO: This seems to be wrong */}

```shell
snap run your-app
```

## Releasing Manually

```shell
snapcraft login # Login with your UbuntuOne credentials
snapcraft upload --release=stable mysnap_latest_amd64.snap
```

## Building automatically

1. On your apps developer page click on the `builds` tab.
2. Click `login with github`.
3. Enter in your repository's details.