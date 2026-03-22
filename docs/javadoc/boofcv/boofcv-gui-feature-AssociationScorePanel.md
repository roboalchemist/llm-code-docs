JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

boofcv.gui.feature

## Class AssociationScorePanel<D>

- java.lang.Object

- 

  - java.awt.Component

  - 

    - java.awt.Container

    - 

      - javax.swing.JComponent

      - 

        - javax.swing.JPanel

        - 

          - boofcv.gui.feature.CompareTwoImagePanel

          - 

            - boofcv.gui.feature.AssociationScorePanel<D>

- 

All Implemented Interfaces:
java.awt.event.MouseListener, java.awt.event.MouseMotionListener, java.awt.image.ImageObserver, java.awt.MenuContainer, java.io.Serializable, java.util.EventListener, javax.accessibility.Accessible

---

```
public class AssociationScorePanel<D>
extends CompareTwoImagePanel
implements java.awt.event.MouseListener
```

Displays relative association scores for different features.  When a feature is clicked on in
 an image the best fit scores are show in the other image.
Author:
  Peter Abeles
See Also:Serialized Form

- 

  - 

### Nested Class Summary

    - 

### Nested classes/interfaces inherited from class javax.swing.JPanel

`javax.swing.JPanel.AccessibleJPanel`

    - 

### Nested classes/interfaces inherited from class javax.swing.JComponent

`javax.swing.JComponent.AccessibleJComponent`

    - 

### Nested classes/interfaces inherited from class java.awt.Container

`java.awt.Container.AccessibleAWTContainer`

    - 

### Nested classes/interfaces inherited from class java.awt.Component

`java.awt.Component.AccessibleAWTComponent, java.awt.Component.BaselineResizeBehavior, java.awt.Component.BltBufferStrategy, java.awt.Component.FlipBufferStrategy`

  - 

### Field Summary

    - 

### Fields inherited from class boofcv.gui.feature.CompareTwoImagePanel

`borderSize, firstClick, leftImage, leftPts, mousePosition, rightImage, rightPts, scaleLeft, scaleRight, selectedIsLeft, selectRegion`

    - 

### Fields inherited from class javax.swing.JComponent

`accessibleContext, listenerList, TOOL_TIP_TEXT_KEY, ui, UNDEFINED_CONDITION, WHEN_ANCESTOR_OF_FOCUSED_COMPONENT, WHEN_FOCUSED, WHEN_IN_FOCUSED_WINDOW`

    - 

### Fields inherited from class java.awt.Component

`BOTTOM_ALIGNMENT, CENTER_ALIGNMENT, LEFT_ALIGNMENT, RIGHT_ALIGNMENT, TOP_ALIGNMENT`

    - 

### Fields inherited from interface java.awt.image.ImageObserver

`ABORT, ALLBITS, ERROR, FRAMEBITS, HEIGHT, PROPERTIES, SOMEBITS, WIDTH`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociationScorePanel**(double containmentFraction)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`protected void`
`**computeScore**(boolean isTargetLeft,
            int targetIndex)` 

`protected void`
`**drawFeatures**(java.awt.Graphics2D g2,
            double scaleLeft,
            int leftX,
            int leftY,
            double scaleRight,
            int rightX,
            int rightY)`
Implement this function to draw features related to each image.

`protected boolean`
`**isValidPoint**(int index)` 

`void`
`**setLocation**(java.util.List<Point2D_F64> leftPts,
           java.util.List<Point2D_F64> rightPts,
           java.util.List<D> leftDesc,
           java.util.List<D> rightDesc)` 

`void`
`**setScorer**(ScoreAssociation<D> scorer)` 

    - 

### Methods inherited from class boofcv.gui.feature.CompareTwoImagePanel

`mouseClicked, mouseDragged, mouseEntered, mouseExited, mouseMoved, mousePressed, mouseReleased, paintComponent, setImages, setLocation`

    - 

### Methods inherited from class javax.swing.JPanel

`getAccessibleContext, getUI, getUIClassID, paramString, setUI, updateUI`

    - 

### Methods inherited from class javax.swing.JComponent

`addAncestorListener, addNotify, addVetoableChangeListener, computeVisibleRect, contains, createToolTip, disable, enable, firePropertyChange, firePropertyChange, firePropertyChange, fireVetoableChange, getActionForKeyStroke, getActionMap, getAlignmentX, getAlignmentY, getAncestorListeners, getAutoscrolls, getBaseline, getBaselineResizeBehavior, getBorder, getBounds, getClientProperty, getComponentGraphics, getComponentPopupMenu, getConditionForKeyStroke, getDebugGraphicsOptions, getDefaultLocale, getFontMetrics, getGraphics, getHeight, getInheritsPopupMenu, getInputMap, getInputMap, getInputVerifier, getInsets, getInsets, getListeners, getLocation, getMaximumSize, getMinimumSize, getNextFocusableComponent, getPopupLocation, getPreferredSize, getRegisteredKeyStrokes, getRootPane, getSize, getToolTipLocation, getToolTipText, getToolTipText, getTopLevelAncestor, getTransferHandler, getVerifyInputWhenFocusTarget, getVetoableChangeListeners, getVisibleRect, getWidth, getX, getY, grabFocus, isDoubleBuffered, isLightweightComponent, isManagingFocus, isOpaque, isOptimizedDrawingEnabled, isPaintingForPrint, isPaintingOrigin, isPaintingTile, isRequestFocusEnabled, isValidateRoot, paint, paintBorder, paintChildren, paintImmediately, paintImmediately, print, printAll, printBorder, printChildren, printComponent, processComponentKeyEvent, processKeyBinding, processKeyEvent, processMouseEvent, processMouseMotionEvent, putClientProperty, registerKeyboardAction, registerKeyboardAction, removeAncestorListener, removeNotify, removeVetoableChangeListener, repaint, repaint, requestDefaultFocus, requestFocus, requestFocus, requestFocusInWindow, requestFocusInWindow, resetKeyboardActions, reshape, revalidate, scrollRectToVisible, setActionMap, setAlignmentX, setAlignmentY, setAutoscrolls, setBackground, setBorder, setComponentPopupMenu, setDebugGraphicsOptions, setDefaultLocale, setDoubleBuffered, setEnabled, setFocusTraversalKeys, setFont, setForeground, setInheritsPopupMenu, setInputMap, setInputVerifier, setMaximumSize, setMinimumSize, setNextFocusableComponent, setOpaque, setPreferredSize, setRequestFocusEnabled, setToolTipText, setTransferHandler, setUI, setVerifyInputWhenFocusTarget, setVisible, unregisterKeyboardAction, update`

    - 

### Methods inherited from class java.awt.Container

`add, add, add, add, add, addContainerListener, addImpl, addPropertyChangeListener, addPropertyChangeListener, applyComponentOrientation, areFocusTraversalKeysSet, countComponents, deliverEvent, doLayout, findComponentAt, findComponentAt, getComponent, getComponentAt, getComponentAt, getComponentCount, getComponents, getComponentZOrder, getContainerListeners, getFocusTraversalKeys, getFocusTraversalPolicy, getLayout, getMousePosition, insets, invalidate, isAncestorOf, isFocusCycleRoot, isFocusCycleRoot, isFocusTraversalPolicyProvider, isFocusTraversalPolicySet, layout, list, list, locate, minimumSize, paintComponents, preferredSize, printComponents, processContainerEvent, processEvent, remove, remove, removeAll, removeContainerListener, setComponentZOrder, setFocusCycleRoot, setFocusTraversalPolicy, setFocusTraversalPolicyProvider, setLayout, transferFocusDownCycle, validate, validateTree`

    - 

### Methods inherited from class java.awt.Component

`action, add, addComponentListener, addFocusListener, addHierarchyBoundsListener, addHierarchyListener, addInputMethodListener, addKeyListener, addMouseListener, addMouseMotionListener, addMouseWheelListener, bounds, checkImage, checkImage, coalesceEvents, contains, createImage, createImage, createVolatileImage, createVolatileImage, disableEvents, dispatchEvent, enable, enableEvents, enableInputMethods, firePropertyChange, firePropertyChange, firePropertyChange, firePropertyChange, firePropertyChange, firePropertyChange, getBackground, getBounds, getColorModel, getComponentListeners, getComponentOrientation, getCursor, getDropTarget, getFocusCycleRootAncestor, getFocusListeners, getFocusTraversalKeysEnabled, getFont, getForeground, getGraphicsConfiguration, getHierarchyBoundsListeners, getHierarchyListeners, getIgnoreRepaint, getInputContext, getInputMethodListeners, getInputMethodRequests, getKeyListeners, getLocale, getLocation, getLocationOnScreen, getMouseListeners, getMouseMotionListeners, getMousePosition, getMouseWheelListeners, getName, getParent, getPeer, getPropertyChangeListeners, getPropertyChangeListeners, getSize, getToolkit, getTreeLock, gotFocus, handleEvent, hasFocus, hide, imageUpdate, inside, isBackgroundSet, isCursorSet, isDisplayable, isEnabled, isFocusable, isFocusOwner, isFocusTraversable, isFontSet, isForegroundSet, isLightweight, isMaximumSizeSet, isMinimumSizeSet, isPreferredSizeSet, isShowing, isValid, isVisible, keyDown, keyUp, list, list, list, location, lostFocus, mouseDown, mouseDrag, mouseEnter, mouseExit, mouseMove, mouseUp, move, nextFocus, paintAll, postEvent, prepareImage, prepareImage, processComponentEvent, processFocusEvent, processHierarchyBoundsEvent, processHierarchyEvent, processInputMethodEvent, processMouseWheelEvent, remove, removeComponentListener, removeFocusListener, removeHierarchyBoundsListener, removeHierarchyListener, removeInputMethodListener, removeKeyListener, removeMouseListener, removeMouseMotionListener, removeMouseWheelListener, removePropertyChangeListener, removePropertyChangeListener, repaint, repaint, repaint, resize, resize, setBounds, setBounds, setComponentOrientation, setCursor, setDropTarget, setFocusable, setFocusTraversalKeysEnabled, setIgnoreRepaint, setLocale, setLocation, setLocation, setName, setSize, setSize, show, show, size, toString, transferFocus, transferFocusBackward, transferFocusUpCycle`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

    - 

### Methods inherited from interface java.awt.event.MouseListener

`mouseClicked, mouseEntered, mouseExited, mousePressed, mouseReleased`

- 

  - 

### Constructor Detail

    - 

#### AssociationScorePanel

```
public AssociationScorePanel(double containmentFraction)
```

  - 

### Method Detail

    - 

#### setScorer

```
public void setScorer(ScoreAssociation<D> scorer)
```

    - 

#### setLocation

```
public void setLocation(java.util.List<Point2D_F64> leftPts,
               java.util.List<Point2D_F64> rightPts,
               java.util.List<D> leftDesc,
               java.util.List<D> rightDesc)
```

    - 

#### computeScore

```
protected void computeScore(boolean isTargetLeft,
                int targetIndex)
```

    - 

#### drawFeatures

```
protected void drawFeatures(java.awt.Graphics2D g2,
                double scaleLeft,
                int leftX,
                int leftY,
                double scaleRight,
                int rightX,
                int rightY)
```

**Description copied from class: `CompareTwoImagePanel`**
Implement this function to draw features related to each image.

**Specified by:**
`drawFeatures` in class `CompareTwoImagePanel`
`scaleLeft` - Scale of left image.`leftX` - Left image (0,0) coordinate.`leftY` - Left image (0,0) coordinate.`scaleRight` - Scale of right image.`rightX` - Right image (0,0) coordinate.`rightY` - Right image (0,0) coordinate.

    - 

#### isValidPoint

```
protected boolean isValidPoint(int index)
```

**Specified by:**
`isValidPoint` in class `CompareTwoImagePanel`

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**