# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-crash-reporting/symbolication.md

# Symbolication

Symbolication is a required process to translate your crash reports into a readable format. For Luciq to be able to successfully symbolicate your crashes, make sure you always upload the needed dSYMs. Every new app version or build generates new files.

There are two types of dSYM files:

1. Required dSYM files are used to symbolicate your application’s frames. In the screenshot below, only the required dSYM is missing.
2. Optional dSYM files are used to symbolicate the frames belonging to any plugin or library you are using.

### Using Manual Upload

First, you need to find the needed dSYM files on your machine. You can find the command below to find the file that belongs to a specific UUID.

{% tabs %}
{% tab title="Shell" %}

```sh
mdfind "com_apple_xcode_dsym_uuids == your-UUID-here"
```

{% endtab %}
{% endtabs %}

On your Luciq dashboard, you will find all your missing files and the commands needed to allocate the files locally as displayed below.

<figure><img src="https://files.readme.io/76f5c77-131789f-14.png" alt="2163"><figcaption></figcaption></figure>

An example warning message in the crashes page of your dashboard that alerts you about a required dSYM file that is missing.

After, finding the dSYM files locally, upload them to your dashboard as explained below:

1. Compress the dSYM file you have located on your machine into a zip file.
2. Go to **Upload dSYMs** in the **Settings** menu of your [Luciq dashboard](https://dashboard.luciq.ai/).
3. Upload the compressed file.

### Using Xcode Build Phase Script

### ⚠️ Important: Disable User Script Sandboxing

Starting with recent versions of Xcode, a build setting called User Script Sandboxing is enabled by default for new projects.

This setting must be disabled for the Luciq dSYM upload script to run correctly

#### How to disable

1. Open your project in Xcode
2. Select your project → Build Settings
3. Search for **User Script Sandboxing**
4. Set **User Script Sandboxing** to **NO**
5. Apply the setting to **all relevant** targets (Debug & Release)

Luciq has a shell script that can automatically upload your project's dSYM during the build process. To use it, go to your project's **Build Phases** tab and add a new **Run Script Build Phase**, then add the following to it.

{% tabs %}
{% tab title="Shell" %}

```sh

#- -- SCRIPT BEGIN - --

# SKIP_SIMULATOR_BUILDS=1

# Check PROJECT_DIR first (CocoaPods, Carthage, Manual)
SCRIPT_SRC=$(find "$PROJECT_DIR" -name 'Luciq_dsym_upload.sh' | head -1)

# If not found, check SPM location
if [ -z "$SCRIPT_SRC" ]; then
  SCRIPT_SRC=$(find "$BUILT_PRODUCTS_DIR" -name 'Luciq_dsym_upload.sh' | head -1)
fi

if [ -z "$SCRIPT_SRC" ]; then
  echo "Luciq: err: script not found. Make sure the Luciq SDK is properly installed."
  exit 1
fi

APP_TOKEN="YOUR-APP-TOKEN-HERE"
source "${SCRIPT_SRC}"
#- -- SCRIPT END - --
```

{% endtab %}
{% endtabs %}

Make sure you replace `YOUR-APP-TOKEN-HERE` with your actual **app token** (found under **SDK Integration** in the **Settings** menu of your [Luciq dashboard](https://dashboard.luciq.ai/).

### Using Fastlane

If you're already using Fastlane to automate your mobile development process, you can benefit from our Luciq/Fastlane plugin to automatically upload your dSYM file to Luciq.

### Installing Fastlane

1. If you don’t have Fastlane, open your terminal and navigate to your project then run the next command to install it:

{% tabs %}
{% tab title="Shell" %}
{% code overflow="wrap" %}

```sh
sudo fastlane init
```

{% endcode %}
{% endtab %}
{% endtabs %}

2. If you don’t have the latest Fastlane version installed, run the following command:

{% tabs %}
{% tab title="Shell" %}
{% code overflow="wrap" %}

```sh
sudo gem install fastlane
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Installing Luciq Plugin

1. Open your Gemfile inside your project directory and add the following:

{% tabs %}
{% tab title="Ruby" %}
{% code overflow="wrap" %}

```ruby
gem 'fastlane-plugin-luciq_official', '~> 0.2.1'
```

{% endcode %}
{% endtab %}
{% endtabs %}

2. Run the following to install our official Fastlane plugin:

{% tabs %}
{% tab title="Shell" %}
{% code overflow="wrap" %}

```sh
sudo gem install fastlane-plugin-luciq_official
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Using the Plugin

1. With the plugin installed, you can navigate the project using Finder, open the Fastlane directory, then open the Fastfile.
2. Inside the Fastfile, you can create a new `lane` and name it `upload_dsyms`, for example, then add the following inside your lane implementation:

{% tabs %}
{% tab title="Lane" %}
{% code overflow="wrap" %}

```markup
luciq_official(api_token:<Luciq Token>, dsym_array_paths:<Array of dsyms paths>)

#-------Example Below-------
luciq_official(api_token: <Luciq-Token>, dsym_array_paths: ['/Users/admin/Desktop/dsyms/Alamofire.framework.dSYM', '/Users/admin/Desktop/dsyms/Luciq.framework.dSYM', '/Users/admin/Desktop/dsyms/SDWebImage.framework.dSYM'])
```

{% endcode %}
{% endtab %}
{% endtabs %}

3. The final step is to run the following command:

{% tabs %}
{% tab title="Shell" %}

```sh
sudo bundle exec fastlane upload_dsyms
```

{% endtab %}
{% endtabs %}

## POST API

In addition to the options explained above, you can use our POST API to upload your dSYM files directly from your console. **The input file must be passed as a zip file.**

{% tabs %}
{% tab title="Shell" %}

```sh
URL:
/api/sdk/v3/symbols_files
METHOD:
POST
PARAMS:
symbols_file
os (android, ios,,,)
application_token
```

{% endtab %}
{% endtabs %}

## Troubleshooting

### Debug Builds

To enable crash symbolication for debug builds, you have to change your project's build settings to generate dSYM files for debug builds.

To do so, select your target in Xcode then go to **Build Settings**, search for **Debug Information Format**, and change its value to **DWARF with dSYM File**.
