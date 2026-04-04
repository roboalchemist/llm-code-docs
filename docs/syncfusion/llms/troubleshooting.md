# Source: https://docs.syncfusion.com/extension/wpf-extension/troubleshooting.md

# Source: https://docs.syncfusion.com/extension/windowsforms-extension/troubleshooting.md

# Source: https://docs.syncfusion.com/uwp/visual-studio-integration/troubleshooting.md

# Source: https://docs.syncfusion.com/windowsforms/visual-studio-integration/troubleshooting.md

# Source: https://docs.syncfusion.com/wpf/visual-studio-integration/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/conversions/html-to-pdf/net/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-library/net/working-with-ocr/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/troubleshooting/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/vue/troubleshooting/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/troubleshooting/troubleshooting.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/angular/troubleshooting/troubleshooting.md

# Experience the Standalone PDF Viewer Component by copying assets from node_modules into my app

It is must to copy the assets from node_modules in to your app to experience the new Standalone PDF Viewer component. It offers flexibility across different build systems, remaining both framework-agnostic and independent of bundlers. Even without a bundler, you can seamlessly integrate the PDF Viewer by directly linking its assets into your app.

This strategic approach to lazy loading prevents unwieldy file sizes that a single bundle might impose, which is often impractical.

Assets from 'ej2-pdfviewer-lib' need to be manually incorporated due to their on-demand loading. This necessity arises because the host application lacks inherent awareness of these assets' lazy loading behavior.