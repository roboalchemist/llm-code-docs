# Source: https://docs.deepconverse.com/product-docs/chatbots/deploy/android-sdk.md

# Android SDK

DeepConverse provides an easy to use SDK for integrating the chatbot into your app. To setup the SDK follow the steps below.

### Installation

**Step 1.** Add it in your root build.gradle at the end of repositories:

```css
allprojects {
	repositories {
		...
		maven { url 'https://jitpack.io' }
	}
}
```

**Step 2.** Add the dependency

```css
dependencies {
        implementation 'com.github.converselabs:android-sdk:1.0.6'
}
```

### Setup

Here is a sample ViewController showing how you can include the SDK and load the bot on the click action of a button. You can also pass in metadata to the chatbot.

You will require ***DOMAIN*** and ***BOT\_NAME*** which can be found from the dashboard.

```
package com.sample.webviewapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;

import com.deepconverse.android_sdk.DeepConverseSDK;
import com.deepconverse.webviewapp.R;

import java.util.HashMap;
import java.util.Map;




public class MainActivity extends AppCompatActivity implements DeepConverseSDK.WebViewCallback {

    private Button openWebViewButton;
    private LinearLayout webUrlContainer;
    private DeepConverseSDK deepConverseSDK;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        openWebViewButton = findViewById(R.id.openWebViewButton);
        webUrlContainer = findViewById(R.id.webUrlContainer);

        openWebViewButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (deepConverseSDK != null) {
                    // Remove the existing WebUrlView if present
                    webUrlContainer.removeView(deepConverseSDK);
                    deepConverseSDK.destroyView();
                }

                // Create a new instance of WebUrlView
                Map<String, String> metadata = new HashMap<>();
                metadata.put("draft", "true");
                deepConverseSDK = new DeepConverseSDK(MainActivity.this, DOMAIN,
                        BOT_NAME, metadata);
                deepConverseSDK.setLayoutParams(new LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.MATCH_PARENT));
                deepConverseSDK.setWebViewCallback(MainActivity.this);
                deepConverseSDK.load();
                webUrlContainer.addView(deepConverseSDK);

                // Show the webUrlContainer and trigger a layout pass
                webUrlContainer.setVisibility(View.VISIBLE);
                webUrlContainer.requestLayout();
            }
        });
    }

    @Override
    public void onViewClosed() {
        // Remove the WebUrlView from the container
        if (deepConverseSDK != null) {
            webUrlContainer.removeView(deepConverseSDK);
            deepConverseSDK.destroyView();
            deepConverseSDK = null;
            webUrlContainer.setVisibility(View.GONE);
        }
    }
}
```

<br>

#### Android Releases

<https://github.com/converselabs/android-sdk/releases>
