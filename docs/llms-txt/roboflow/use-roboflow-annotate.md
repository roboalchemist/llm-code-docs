# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/use-roboflow-annotate.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/use-roboflow-annotate.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/use-roboflow-annotate.md

# Source: https://docs.roboflow.com/annotate/use-roboflow-annotate.md

# Annotate an Image

You can access the labeling interface by selecting an image from the Assign or Dataset pages on the Roboflow dashboard.

On the right-hand side of the labeling interface, you will find the toolbar. The toolbar has many features you can use for annotating images.

In this document, we talk through how to use the following features:

* Drag and select
* Bounding box annotation tool
* Polgyon annotation tool
* Smart polygon
* Label assist
* Zoom tool

### Drag and Select

Represented by a hand icon, this feature allows you to select, edit, and drag individual annotations.

* **Single-click** an existing bounding box to select it. Once selected, you can change a bounding box's size with the circular white handles that appear on its corners and on each side. Or use the class editor to change the box's label.
* **Drag a box** to move it.
* **Drag the background** to pan.
* **Click the background** to deselect all boxes.

<div align="center"><figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-fa1f28bc3e8af8fde30737bf577b3ae2ee9ee91c%2Fimage.png?alt=media" alt=""><figcaption><p>Drag Tool (D) selection</p></figcaption></figure></div>

### **Bounding Box Annotation Tool**

The bounding box annotation tool (represented by a rectangular box icon) allows you to draw new bounding-box annotations. In this mode, you will see crosshairs that will help you determine where to start drawing.

Click and drag across an image to create a new annotation, then use the Class Selector to choose its label.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-839e9a8de5a9155f4db78fccd61d1e032cbdd12d%2Fimage.png?alt=media" alt=""><figcaption><p>Bounding Box Tool (B) selection</p></figcaption></figure>

### Polygon Annotation Tool

The polygon annotation tool allows you to [draw new polygonal annotations](https://blog.roboflow.com/polygon-annotation-labeling/). In this mode, you will see crosshairs that will help you determine where to start drawing.

Click on the image around objects of interest to create an enclosed polygon annotation, then use the Class Selector to choose its label.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-707258408089bf681cfdb74335a73c6bc05a717e%2Fimage.png?alt=media" alt=""><figcaption><p>Polygon Tool (P) selection</p></figcaption></figure>

### Brush Annotation Tool

The brush annotation tool lets you paint pixel-precise mask annotations over regions of interest in your image. Use the on-canvas brush controls to adjust the brush size and switch between Add and Subtract modes, which respectively add to or erase from the current mask.

\
Mask annotations represent objects as per-pixel regions rather than outlines or boxes. This enables more accurate shape capture, especially for irregular or fine-grained structures (e.g., hair, foliage, or transparent objects), and is ideal for training instance or semantic segmentation models. For each mask,  we display a bounding box around the masked region, making it easier to see the overall extent of the object and interact with it during review and editing.

\
Click and drag over the image to paint the area you want to include or exclude from the mask, then use the Class Selector to assign or change the label for that mask region.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F7nZNSbSCVLzApnQOyXks%2FScreenshot%202025-11-25%20at%2009.40.10.png?alt=media&#x26;token=51002a32-52e5-420e-b852-ab9735851ed2" alt=""><figcaption><p>Brush Tool (U) selection</p></figcaption></figure>

### Smart Polygon

**Smart Polygon** allows you to draw new Smart Polygon annotations.

In this mode, you will see a green dot when you are selecting a new area of interest (new label); a red dot when selecting areas to remove from the area of interest (parts of the object or image that you don't want to label/enclose with the polygon); and options to adjust the polygon by Convex Hull, Smooth, and Complex settings.

Smart Polygon is particularly useful for (Instance and Semantic) Segmentation projects, however, you [may see performance boosts in Object Detection models](https://blog.roboflow.com/polygons-object-detection/) when labeling with Smart Polygons on Roboflow.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-448764c9e4dda5fd5c29f7e80ae88bbf7ee0c12d%2Fimage.png?alt=media" alt=""><figcaption><p>Smart Polygon (S) Tool selection</p></figcaption></figure>

### **Label Assist**

[**Label Assist**](https://docs.roboflow.com/annotate/ai-labeling/model-assisted-labeling) uses predictions from a public model or a version [trained with Roboflow Train](https://docs.roboflow.com/train/train) to automatically suggest bounding box labels as you annotate.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F1EgT6hilQ7UeeuTbVo8W%2Flabel-assist-img.png?alt=media&#x26;token=b8933ccc-83e8-414c-9c0b-d5234c75d765" alt="Label Assist Tool selection"><figcaption></figcaption></figure>

### **Mark Null**

Mark null (Null annotation) is to be used for the "labeling" of background, or null, images. This setting can also be used to clear all annotations from an image, or to mark the image as Unannotated. To learn more about null annotations, check out our guide "[The Difference Between Missing and Null Annotations](https://blog.roboflow.com/missing-and-null-image-annotations/)".

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-54092b9e3c0db98fc51650f689190db4562f7a32%2Fimage.png?alt=media" alt=""><figcaption><p>Mark Null (N) Tool selection</p></figcaption></figure>

### **Undo, Redo, and Repeat Annotations**

While in Bounding Box (B), Polygon (P), or Smart Polygon (S) mode:

* **Undo** reverts the previous action.
* **Redo** reverses a previously undone action.
* **Repeat Previous** reapplies label(s) on an image in the same location(s) as the last annotated image

### Class Selection

When an image is selected, the **Class Selector** will appear. It contains the following options for choosing the label of a bounding box:

![The Class Selector](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4cbf1759872d620fb11069eab425cb95a2458a4f%2Fimage.png?alt=media)

* **Textfield** to create a new class or filter existing classes.
* **Buttons** to save or discard your changes.
* **Class List** of the existing classes in the dataset (filtered by the text field and with the active option highlighted in purple) and, sometimes, a "Create class" option if the text you typed does not match an existing class.

### Zoom Tool

The zoom tool found at the bottom left of the screen.

* Zoom in and out to fit more of the image on your screen at one time or to get a closer look for more detailed editing. There is also an option to "lock" the zoom to a specified percentage, or reset the zoom to fit the entirety of the image within the Annotation Tool's viewport.
* Note that if you select the "*Zoom Lock*" option, all images will appear at this zoom-level. Deselect, or unlock, the lock to remove Zoom Lock.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c2a10592c3b157feb582f82665e45437b3b74097%2Fimage.png?alt=media" alt=""><figcaption><p>Zoom Tool</p></figcaption></figure>

### Annotation List

Annotations (abbreviated *Annots* in the dashbaord) show which classes are present and not present in an image, what color their boxes are, and layering of labels. The Annotations drawer includes Tags which can be used to help with organizing, filtering or sorting through images in datasets.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2fd8837a48f9fd4d165ce6af19eaa66aeab7e2bc%2Fannots-drawer.png?alt=media" alt="" width="324"><figcaption><p>Annotations (Annots) Sidebar</p></figcaption></figure>

### **Image Attributes**

Attributes represent information about an image including its dimensions, last-modified time, and whether it is in this dataset's [training, validation, or test set](https://blog.roboflow.com/train-test-split/).

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-3951578e294aecf642b3ef9fa98ac9d8eabf32af%2Fimage.png?alt=media" alt="" width="489"><figcaption><p>Attributes Sidebar</p></figcaption></figure>
