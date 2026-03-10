# Publishing To The Arch User Repository

## Setup

First go to `https://aur.archlinux.org` and make an account. Be sure to add the proper ssh keys. Next, clone an empty git repository using this command.

```sh
git clone https://aur.archlinux.org/your-repo-name
```

After completing the steps above, create a file with the name `PKGBUILD`. Once the file is created you can move onto the next step.

### Writing a PKGBUILD file

```ini title="PKGBUILD"
pkgname=<pkgname>
pkgver=1.0.0
pkgrel=1
pkgdesc="Description of your app"
arch=('x86_64' 'aarch64')
url="https://github.com/<user>/<project>"
license=('MIT')
depends=('cairo' 'desktop-file-utils' 'gdk-pixbuf2' 'glib2' 'gtk3' 'hicolor-icon-theme' 'libsoup' 'pango' 'webkit2gtk-4.1')
options=('!strip' '!emptydirs')
install=${pkgname}.install
source_x86_64=("${url}/releases/download/v${pkgver}/appname_${pkgver}_amd64.deb")
source_aarch64=("${url}/releases/download/v${pkgver}/appname_"${pkgver}_arm64.deb")
```

- At the top of the file, define your package name and assign it the variable `pkgname`.
- Set your `pkgver` variable. Typically it is best to use this variable in the source variable to increase maintainability.
- The `pkgdesc` variable on your aur repo's page and tells vistors what your app does.
- The `arch` variable controls what architectures can install your package.
- The `url` variable, while not required, helps to make your package appear more professional.
- The `install` variable specifies the name of .install script which will be run when the package is installed, removed or upgraded.
- The `depends` variable includes a list of items that are required to make your app run. For any Tauri app you must include all of the dependencies shown above.
- The `source` variable is required and defines the location where your upstream package is. You can make a `source` architecture specific by adding the architecture to the end of the variable name.

### Generating `.SRCINFO`

In order to push your repo to the aur you must generate an `.SRCINFO` file. This can be done with this command.

```sh
makepkg --printsrcinfo > .SRCINFO
```

### Testing

Testing the app is extremely simple. All you have to do is run `makepkg` within the same directory as the `PKGBUILD` file and see if it works

### Publishing

Finally, after the testing phase is over, you can publish the application to AUR (Arch User Repository) with these commands.

```sh
git add .

git commit -m "Initial Commit"

git push
```

If all goes well, your repository should now appear on the AUR website.

## Examples

### Extracting From A Debian Package

```ini title="PKGBUILD"