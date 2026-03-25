# Source: https://docs.logrocket.com/reference/ios-capture-custom-fonts.md

# Capture Custom Fonts

iOS instructions to capture custom font files for display in session replay

If you use [custom fonts](https://developer.apple.com/documentation/uikit/text_display_and_fonts/adding_a_custom_font_to_your_app), and notice missing icons or incorrectly sized text in Session Replay, you may want to follow these instructions to upload your fonts on release builds. This will enable custom fonts to display in Session Replay. Custom font replay requires a minimum SDK version of 1.33.8.

# Get `logrocket-cli` binary

`logrocket-cli` will need to be available on the system building your app for release, whether by executing the following steps -- which comprise a local setup process --  in said system or by another means.

## Download and unpack the appropriate CLI package for your machine

```curl
curl -SL --progress-bar "${download_url}" | tar xz --strip-components=1
```

## `download_url`

Replace `${download_url}` in the curl command above with the appropriate value based on the machine on which you are building your application

### For building on arm64 (M1-3) machines

[https://storage.googleapis.com/artifacts.logrocket.com/logrocket-cli/logrocket-cli-0.2.0-darwin-arm64.tar.gz](https://storage.googleapis.com/artifacts.logrocket.com/logrocket-cli/logrocket-cli-0.2.0-darwin-arm64.tar.gz)

### For building on amd64 (Intel) machines

[https://storage.googleapis.com/artifacts.logrocket.com/logrocket-cli/logrocket-cli-0.2.0-darwin-amd64.tar.gz](https://storage.googleapis.com/artifacts.logrocket.com/logrocket-cli/logrocket-cli-0.2.0-darwin-amd64.tar.gz)

## Make CLI available globally for execution

Place the unpacked CLI in a directory already included in your `$PATH`, or add the directory in which you have placed it to `$PATH` by adding the following code to your shell configuration file (`.bashrc`, `.bash_profile`, or `.zshrc`)

```Text Add dir to $PATH
export PATH=$GOPATH/bin:$PATH
// where GOPATH is the path to the directory containing the LogRocket CLI binary
```

# Execute CLI during application build

## Add custom Run Script Build Phase

### Adding the phase

![](https://files.readme.io/4b3be10-add_custom_build_phase.png)

### Implementing the script

![](https://files.readme.io/ef8dd78-implement_custom_script.png)

Use the following ruby script implementation for your custom build phase

```ruby logrocket_asset_upload_script
#!/usr/bin/env ruby
# frozen_string_literal: true

require 'json'

# Ensure the font data file is freshly generated on each build
app_build_resources_dir = "#{ENV['BUILT_PRODUCTS_DIR']}/#{ENV['UNLOCALIZED_RESOURCES_FOLDER_PATH']}"
output_file = "#{app_build_resources_dir}/lr_custom_fonts_data.json"
if File.exist?(output_file)
  File.delete(output_file)
end


# Check whether LogRocket asset upload is enabled for this build
current_build_config = ENV['CONFIGURATION']
enabled_build_configs = ENV['LOGROCKET_ENABLED_BUILD_CONFIGS']&.split(',')

unless enabled_build_configs&.include?(current_build_config) || current_build_config == 'Release'
  puts "LogRocket custom asset upload is not enabled for this build."
  exit 0
end

# Ensure configuration is set that allows script to find the downloaded LogRocket CLI for execution
LOGROCKET_CLI_PATH = ENV['LOGROCKET_CLI_PATH'] || `which logrocket-cli`.strip
if LOGROCKET_CLI_PATH.empty?
  warn 'Error: LOGROCKET_CLI_PATH is not set and logrocket-cli was not found on $PATH'
  exit 1
end

# Ensure configuration is set to authorize asset upload for your LogRocket application
unless ENV['LOGROCKET_API_KEY']
  warn 'Error: LOGROCKET_API_KEY is not set'
  exit 1
end

# Ensure configuration is set that allows LogRocket CLI to find custom font files
unless ENV['LOGROCKET_ASSET_DIR']
  warn 'Error: LOGROCKET_ASSET_DIR is not set'
  exit 1
end

# Execute asset_upload CLI command and collect output
cli_cmd = "#{LOGROCKET_CLI_PATH} asset_upload #{ENV['LOGROCKET_ASSET_DIR']}"
cli_output = `#{cli_cmd}`


# Parse CLI output to report any errors or generate the build resource used by the LogRocket SDK
urls = []
cli_output.each_line do |line|
  data = begin
    JSON.parse(line)
  rescue StandardError
    nil
  end
  next unless data

  case data['level']
  when 'info'
    if data['url']
      urls << data['url']
    else
      warn "Failed to retrieve cached url for #{data['filepath']}"
    end
  when 'error'
    warn "Error: #{data['message']}"
    exit 1
  else
    warn "Unknown level for LogRocket CLI asset-upload output: #{data['level']}"
    exit 1
  end
end

if urls.empty?
  warn 'No valid custom font assets found for upload'
else
  Dir.mkdir(app_build_resources_dir) unless Dir.exist?(app_build_resources_dir)

  json_data = { urls: urls }.to_json
  File.write(output_file, json_data)
end

exit 0

```

For additional information on custom build phases in iOS projects, refer to [this Apple Developer Docs page](https://developer.apple.com/documentation/xcode/customizing-the-build-phases-of-a-target).

## Configure Environment Variables

In your project's Build Settings > User-Defined section, configure the variables used in the above ruby script

```python .env
LOGROCKET_API_KEY = <your-application-api-key> # Found in Settings > Project Settings > Development > API Key
LOGROCKET_ASSET_DIR = <app-assets-path> # Directory in which all custom fonts for the application can be found. If more than one directory contains custom fonts for the application then list all directory paths with a space between each path
LOGROCKET_CLI_PATH = <cli-binary-path> # Downloaded in step 1
```

The default configuration for custom fonts only enables it for Release builds, include a `LOGROCKET_ENABLED_BUILD_CONFIGS` definition in your Build Settings to test custom fonts on other releases (e.g `LOGROCKET_ENABLED_BUILD_CONFIGS = Debug,Release`)

### How to add a User Defined Build Setting

![](https://files.readme.io/22db2be-add_user_defined_setting.png)

### Example User Defined section of application Build Settings

![](https://files.readme.io/091f7df-user_defined_settings.png)