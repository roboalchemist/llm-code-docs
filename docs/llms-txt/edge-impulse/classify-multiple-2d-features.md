# Source: https://docs.edgeimpulse.com/tutorials/topics/machine-learning/classify-multiple-2d-features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Classify multiple 2D input features

Neural networks can work with multiple types of data simultaneously, allowing for sophisticated sensor fusion techniques. Here we demonstrate how to use a single model to perform classification using two separate sets of two-dimensional (2D) input features.

For this tutorial, the two sets of input features are assumed to be spectrograms that are passed through two different convolutional branches of a neural network. The two branches of the network are then combined and passed through a final dense output layer for classification. In the general case, however, there could be more than two branches and the input features could represent different sensor data, channels, or outputs from feature extractors.

<Info>
  This example is for when you would like to pass sets of input features to independent branches of a neural network and then combine the results for a final classification.

  If you plan on passing all input features through a fully connected network, then these steps are unnecessary; Edge Impulse automatically concatenates output features from processing blocks and learning blocks operate on the concatenated array.
</Info>

## Example use cases

By using this architecture, you can perform sophisticated sensor fusion tasks, potentially improving classification accuracy and robustness compared to single-input models.

This type of model is particularly useful in situations such as:

* Combining data from different sensor types (e.g. accelerometer and gyroscope)
* Handling output from multiple feature extractors (e.g. time-domain and frequency-domain features)
* Analyzing data from sensors in different locations

## Model architecture

The architecture in this tutorial consists of separating the model input into two sets of 2D input features (input layer and reshape layers), passing them through independent convolutional branches, and then combining the results for classification (concatenate layer and dense layer). See below for additional details.

### Input layer

The input layer accepts a one-dimensional (1D) input of length `input_length`. The `input_length` argument is available if you are using the [learning blocks](/studio/projects/learning-blocks) pre-built by Edge Impulse and modifying them through [expert mode](/studio/projects/learning-blocks/expert-mode). By default, Edge Impulse flattens the output of all [processing blocks](/studio/projects/processing-blocks) before passing them to the learning block, so the shape is a 1D array.

### Reshape layers

The model input is first split into two halves and then reshaped back into 2D formats. In this example, we assumed spectrogram inputs with 50 columns (time frames) each. We calculated the number of rows based on the number of columns and channels, then used the row and column information for the reshape layer.

### Convolutional branches

Each half of the input goes through its own convolutional branch that contains multiple layers:

* Conv2D layers (8 and 16 filters)
* MaxPooling2D layers for downsampling
* Dropout layers for regularization
* Flatten layer to prepare for concatenation

### Output layers

Finally, the outputs of the two independent branches are combined with a concatenation layer. This combined output is then passed through a final dense layer with a softmax activation to perform classification.

### Keras model

The following code snippet can be copied and pasted into a [classification learning block](/studio/projects/learning-blocks/blocks/classification) using the expert mode feature within Studio.

```python  theme={"system"}
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, InputLayer, Dropout, Conv1D, Conv2D, Flatten, Reshape, MaxPooling1D, MaxPooling2D, AveragePooling2D, BatchNormalization, Permute, ReLU, Softmax, Concatenate, Input
from tensorflow.keras.optimizers.legacy import Adam
from tensorflow.keras.callbacks import EarlyStopping

EPOCHS = args.epochs or 50
LEARNING_RATE = args.learning_rate or 0.0005
# If True, non-deterministic functions (e.g. shuffling batches) are not used.
# This is False by default.
ENSURE_DETERMINISM = args.ensure_determinism
# this controls the batch size, or you can manipulate the tf.data.Dataset objects yourself
BATCH_SIZE = args.batch_size or 32
if not ENSURE_DETERMINISM:
    train_dataset = train_dataset.shuffle(buffer_size=BATCH_SIZE*4)
train_dataset=train_dataset.batch(BATCH_SIZE, drop_remainder=False)
validation_dataset = validation_dataset.batch(BATCH_SIZE, drop_remainder=False)

channels = 1
columns = 50
rows = input_length // (columns * channels)

# Input layer
input_layer = Input(shape=(input_length, ))

# Split the input into two halves
half_length = input_length // 2
# First half
first_half = Reshape((rows // 2, columns, channels))(input_layer[:, :half_length])
branch1 = Conv2D(8, kernel_size=3, kernel_constraint=tf.keras.constraints.MaxNorm(1), padding='same', activation='relu')(first_half)
branch1 = MaxPooling2D(pool_size=2, strides=2, padding='same')(branch1)
branch1 = Dropout(0.5)(branch1)
branch1 = Conv2D(16, kernel_size=3, kernel_constraint=tf.keras.constraints.MaxNorm(1), padding='same', activation='relu')(branch1)
branch1 = MaxPooling2D(pool_size=2, strides=2, padding='same')(branch1)
branch1 = Dropout(0.5)(branch1)
branch1 = Flatten()(branch1)

# Second half
second_half = Reshape((rows // 2, columns, channels))(input_layer[:, half_length:])
branch2 = Conv2D(8, kernel_size=3, kernel_constraint=tf.keras.constraints.MaxNorm(1), padding='same', activation='relu')(second_half)
branch2 = MaxPooling2D(pool_size=2, strides=2, padding='same')(branch2)
branch2 = Dropout(0.5)(branch2)
branch2 = Conv2D(16, kernel_size=3, kernel_constraint=tf.keras.constraints.MaxNorm(1), padding='same', activation='relu')(branch2)
branch2 = MaxPooling2D(pool_size=2, strides=2, padding='same')(branch2)
branch2 = Dropout(0.5)(branch2)
branch2 = Flatten()(branch2)

# Concatenate the outputs of both branches
merged = Concatenate()([branch1, branch2])

# Final dense layer
output_layer = Dense(classes, name='y_pred', activation='softmax')(merged)

# Create model
model = Model(inputs=input_layer, outputs=output_layer)

# this controls the learning rate
opt = Adam(learning_rate=LEARNING_RATE, beta_1=0.9, beta_2=0.999)
callbacks.append(BatchLoggerCallback(BATCH_SIZE, train_sample_count, epochs=EPOCHS, ensure_determinism=ENSURE_DETERMINISM))
# Early stop
callbacks.append(EarlyStopping(patience=3))

# train the neural network
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
model.fit(train_dataset, epochs=EPOCHS, validation_data=validation_dataset, verbose=2, callbacks=callbacks)

# Use this flag to disable per-channel quantization for a model.
# This can reduce RAM usage for convolutional models, but may have
# an impact on accuracy.
disable_per_channel_quantization = False
```

### Extending the model architecture

To extend this model architecture to handle more inputs, you can:

1. Split the input into more sections (e.g. thirds or quarters instead of halves).
2. Create additional convolutional branches for each new input section.
3. Include the new branches in the concatenation step before the final dense layer.

## Conclusion

The architecture defined in this tutorial allows the model to process two separate sets of 2D input features independently before combining them for a final classification. Each branch can learn model parameters specific to its input, which can be particularly useful when dealing with different types of sensor data or feature extractors.


Built with [Mintlify](https://mintlify.com).