# Source: https://docs.edgeimpulse.com/tutorials/topics/data/collect-image-data-phone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Collect image data using a mobile phone

This page is part of [Image classification](/tutorials/topics/data/collect-image-data-openmv-h7-plus) and describes how you can use your mobile phone to import image data into Edge Impulse.

To add your phone to your project, go to the **Devices** page, select **Connect a new device** and select **Use your mobile phone**. A QR code will pop up. Scan this code with your phone and your phone will pop up on the devices screen.

<Frame caption="Mobile phone connected to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/yaErNg6BwcJv1FZd/.assets/images/25c9536-screenshot_2020-07-16_at_163241.png?fit=max&auto=format&n=yaErNg6BwcJv1FZd&q=85&s=4309d7d6f6b6a402bea3bc5a2781f5ef" width="1121" height="302" data-path=".assets/images/25c9536-screenshot_2020-07-16_at_163241.png" />
</Frame>

### 1. Collecting images

With your phone connected to your project, it's time to start capturing some images and build our dataset. We have a special UI for collecting images quickly, on your phone choose **Collecting images?**.

<Frame caption="Choose Collecting images? to load the image-specific UI">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dc7ec59-collect01.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=8057c220c14f98b0ea39851aade63d4d" width="585" height="904" data-path=".assets/images/dc7ec59-collect01.png" />
</Frame>

On your phone a permission prompt will show up, and then the viewfinder will be displayed. Set the label (in the top corner) to 'lamp', point your camera at your lamp and press **Capture**.

<Frame caption="Taking a photo with your phone.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/53dc17e-capture02.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=32eabc90923a274aba3387e5678388c7" width="380" height="646" data-path=".assets/images/53dc17e-capture02.png" />
</Frame>

Afterwards the photo shows up in the studio on the **Data acquisition** page.

<Frame caption="Photo shows up in the studio.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/3499a66-screenshot_2020-07-16_at_164124.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=c3c91b16bd76a56c404c499397208e3b" width="1369" height="1000" data-path=".assets/images/3499a66-screenshot_2020-07-16_at_164124.png" />
</Frame>

Do this until you have captured 30 images per class from a variety of angles. Also make sure to vary the things you capture for the unknown class.

### 2. Alternative: upload data directly

Alternatively you can also capture your dataset directly through a different app, and then upload the data directly to Edge Impulse There are both options to do this visually (click the 'Upload' icon on the data acquisition screen), or via the CLI. You can find instructions here: [Uploader](/tools/clis/edge-impulse-cli/uploader). In this case it's highly recommended to you use square images, as the transfer learning model expects these; and you probably want to resize these images before uploading them to make sure training remains fast.


Built with [Mintlify](https://mintlify.com).