# Source: https://docs.infera.org/node/infera-lite.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Infera Lite

> Infera Lite is an easy-to-use chrome extension UI that connects users to a decentralized AI inference network, allowing them to contribute their GPU for AI model inference.

The Infera Lite extension is used to monitor and manage your [Infera Node](/node/cli/macos). This guide shows you how to install and how to use the Infera Lite extension.

If you have already installed the extension, you can learn how to use it by reading the [Managing Your Node](/node/managing-node) guide.

## Download Infera Lite

1. Open the Chrome Browser (if you do not have Chrome installed, download it [here](https://www.google.com/intl/en_ca/chrome/))
2. Go to the [Infera Lite](https://chromewebstore.google.com/detail/infera-lite/ffoccnmddajjohmmkccnkobelobgcdmp) extension on the Chrome Web Store.
3. Click **"Add to your Chrome"** to install the extension in your browser.

***

## Onboarding Extension

After your install the extension, onboarding pages will pop up. These onboarding instructions are for installing the programs required to run an Infera Node.

<Note> If you have already installed the **Infera Node** on your device, you can skip through these steps without completing any of the tasks </Note>

**Getting started**

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=85fb4d345e84f50b60fa69aedd2bcd7c" data-og-width="1440" data-og-height="1024" data-path="images/node/extension/get-started.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=0b99d1f4514e3398de130db13a174a0a 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=22a30d1576bcc11832edbdd88a8326fb 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=02edef39c2efee40f96cb0749e985fa4 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=b55a748e917c7ef6fb06242b3cca97f1 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=d875cbf00afac98e180e1d0a17837ded 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/get-started.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=35add3f85477da9b302a6c7079484180 2500w" />

**Select your operating system**

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=02f5e271c66c1b5f346c3cf0bc99cd26" data-og-width="1440" data-og-height="1024" data-path="images/node/extension/choose-os.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=a3086e5cf0a63a9c8e7e8cc4a244b6db 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=9f13b8b7588f5652aa529306f288fbc6 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=2cb7b752492df652f1a4ab334eae8b47 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=43f6db6b32c79247a47c8f223d7a2cec 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=d87b02390afa88a02a1ff6945ff56f0f 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/choose-os.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=d27c2b3cac3c2300822a0796dd581c0b 2500w" />

**Install Ollama**

<Warning>Having Ollama installed is very important and your **Infera Node** will not work without it</Warning>

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=3d272f34ee031d16d48f271109335949" data-og-width="1440" data-og-height="1024" data-path="images/node/extension/install-ollama.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=d56615c37beb9b7164c50fc022a73cf4 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=bcc70386fd4aeeaae23c5430440305a7 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=ef2430aa0592985904495df500ee1726 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=94d30958b52980c0859aec8d0dff7109 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=08beb9ab0af78458996d4f9e7e66e1df 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-ollama.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=d4c5680fb273b212408ae4948d61e1a1 2500w" />

**Install Infera Node on your system**

Follow the instructions displayed by your onboarding process (operating system specific) to install the **Infera Node**.

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=630e4b51c0848fcd394ba68a5925bb5d" data-og-width="1440" data-og-height="1024" data-path="images/node/extension/install-node.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=8659ce587bf8472b36c0c8046a671504 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=7201deae971b043f97a5cbcb50c5c43c 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=3e828332186eaafd576cf24849918247 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=81c862fee332fff9cab5980dff4de241 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=a56ed3e4f81723e1e8f964d5fcdd41dc 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/install-node.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=932abb19997894557fc20c429d2868c9 2500w" />

**All set!**

You are ready to use, monitor and manage your Infera Node!

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=f562962519236f6fae8e0825dd457f05" data-og-width="1440" data-og-height="1024" data-path="images/node/extension/all-set.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=9fa34f29fa416239b0c011c1373b840e 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=4d498a089f7ddb34440a1f1af0691b9c 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=ab95bdc62968ab2e29b09f35d543bd06 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=8970323dac80be65c6c70343b6222786 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=29dc1f08f908e6f552238e3d051f1564 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/extension/all-set.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=7de89d8a6771a7da201b31e5c583bdba 2500w" />

***

## Privacy Assurance

* **No Personal Data:** We don't collect or store your personal information.
* **Encryption:** All communications are encrypted for security.
* **Local Processing:** All inference happens on your device; nothing is sent externally.
* **No Tracking:** Your activities are never tracked.
