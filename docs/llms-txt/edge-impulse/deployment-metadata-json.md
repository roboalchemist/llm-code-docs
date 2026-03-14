# Source: https://docs.edgeimpulse.com/tools/specifications/files/deployment-metadata-json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# deployment-metadata.json

The `deployment-metadata.json` file is passed to [custom deployment blocks](/studio/organizations/custom-blocks/custom-deployment-blocks). It provides details about the impulse being deployed.

## File structure

### DeploymentMetadataV1

```typescript  theme={"system"}
interface DeploymentMetadataV1 {
    version: 1;
    // Global deployment counter
    deployCounter: number;
    // The output classes (for classification)
    classes: string[];
    // The number of samples to be taken per inference (e.g. 100Hz data, 3 axis, 2 seconds => 200)
    samplesPerInference: number;
    // Number of axes ((e.g. 100Hz data, 3 axis, 2 seconds => 3)
    axesCount: number;
    // Frequency of the data
    frequency: number;
    // TFLite models (already converted and quantized)
    tfliteModels: {
        // Information about the model type, e.g. quantization parameters
        details: KerasModelIODetails;
        // Name of the input tensor
        inputTensor: string | undefined;
        // Name of the output tensor
        outputTensor: string | undefined;
        // Path of the model on disk
        modelPath: string;
        // Path of the model on disk (ONNX), not always available
        onnxModelPath: string | undefined;
        // Path of a secondary/auxiliary model on disk (ONNX), not always available
        onnxAuxModelPath: string | undefined;
        // Path to .prototxt (in case of YOLOX), not always available
        prototxtPath: string | undefined;
        // Path to .fbz (BrainChip Akida model file), not always available
        akidaModelPath: string | undefined;
        // Path to .fbz (BrainChip Akida model prepared for Edge Learning), not always available
        akidaEdgeLearningModelPath: string | undefined;
        // Calculated arena size when running TFLite in interpreter mode
        arenaSize: number;
        // Number of values to be passed into the model
        inputFrameSize: number;
    }[];
    // Project information
    project: {
        // Project name
        name: string;
        // Project ID
        id: number;
        // Project owner (user or organization name)
        owner: string;
        // API key, only set for deploy blocks with privileged flag and development keys set
        apiKey: string | undefined;
        // Studio host
        studioHost: string;
    };
    // Impulse information
    impulse: DeploymentMetadataImpulse;
    // Sensor guess based on the input
    sensor: 'camera' | 'microphone' | 'accelerometer' | 'positional' | 'environmental' | 'fusion' | undefined;
    // Folder locations
    folders: {
        // Input files are here, the input folder contains 'edge-impulse-sdk', 'model-parameters', 'tflite-model'
        input: string;
        // Write your output file here
        output: string;
    };
}
```

### CreateImpulseStateBase

```typescript  theme={"system"}
/**
 * Fields common to all CreateImpulseStateX
 */
interface CreateImpulseStateBase extends CreateImpulseStateMetadata {
    id: number;
    name: string;
    title: string;
    type: string;
}
```

### CreateImpulseStateDsp

```typescript  theme={"system"}
interface CreateImpulseStateDsp extends CreateImpulseStateBase {
    type: string | 'custom';
    implementationVersion: number;
    axes: string[];
    customUrl?: string;
    input: number;
    tunerBaseBlockId?: number;
    autotune?: boolean;
    organization?: {
        id: number;
        dspId: number;
    };
    namedAxes?: CreateImpulseStateDspNamedAxis[];
}
```

### CreateImpulseStateDspNamedAxis

```typescript  theme={"system"}
type CreateImpulseStateDspNamedAxis = {
    name: string,
    description?: string,
    required?: boolean,
    selectedAxis?: string,
};
```

### CreateImpulseStateInput

```typescript  theme={"system"}
type CreateImpulseStateInput = CreateImpulseStateInputTimeSeries |
    CreateImpulseStateInputImage |
    CreateImpulseStateInputFeatures;
```

### CreateImpulseStateInputFeatures

```typescript  theme={"system"}
interface CreateImpulseStateInputFeatures extends CreateImpulseStateBase {
    type: 'features';
    datasetSubset?: {
        subsetModulo: number;
        subsetSeed: number;
    };
}
```

### CreateImpulseStateInputImage

```typescript  theme={"system"}
interface CreateImpulseStateInputImage extends CreateImpulseStateBase {
    type: 'image';
    imageWidth: number;
    imageHeight: number;
    resizeMode: 'squash' | 'fit-short' | 'fit-long' | 'crop';
    cropAnchor: 'top-left' | 'top-center' | 'top-right' | 'middle-left' | 'middle-center' | 'middle-right' | 'bottom-left' | 'bottom-center' | 'bottom-right';
    resizeMethod: 'nearest' | 'lanczos3';
    labelingMethod?: 'object_detection' | 'single_label';
    datasetSubset?: {
        subsetModulo: number;
        subsetSeed: number;
    };
}
```

### CreateImpulseStateInputTimeSeries

```typescript  theme={"system"}
interface CreateImpulseStateInputTimeSeries extends CreateImpulseStateBase {
    type: 'time-series';
    windowSizeMs: number;
    windowIncreaseMs: number;
    frequencyHz: number;
    classificationWindowIncreaseMs?: number;
    padZeros: boolean;
    datasetSubset?: {
        subsetModulo: number;
        subsetSeed: number;
    };
}
```

### CreateImpulseStateLearning

```typescript  theme={"system"}
interface CreateImpulseStateLearning extends CreateImpulseStateBase {
    dsp: number[];
    type: typeof ALL_CREATE_IMPULSE_STATE_LEARNING_TYPES[number];
}

const ALL_CREATE_IMPULSE_STATE_LEARNING_TYPES = [
    'keras',
    'keras-transfer-image',
    'keras-transfer-kws',
    'keras-object-detection',
    'keras-regression',
    'anomaly',
    'keras-akida',
    'keras-akida-transfer-image',
    'keras-akida-object-detection',
    'anomaly-gmm',
    'keras-visual-anomaly',
];
```

### CreateImpulseStateMetadata

```typescript  theme={"system"}
/**
 * Provides metadata shared between all block types
 */
interface CreateImpulseStateMetadata {
    /**
     * Metadata for block versioning
     */
    // The user-editable description of this block version
    description?: string;
    // Which part of the system created this version (createImpulse | clone | tuner)
    createdBy?: string;
    // The date and time this version was created
    createdAt?: Date;
    // Tuner template block id. This is _always_ -1 if the block is a Tuner block.
    // the only place where this is used is in the DB to query for Tuner-managed blocks
    // in the block config table.
    tunerTemplateId?: number;
    // If this is true, this block is also a tuner block.
    db?: boolean;
}
```

### DeploymentMetadataImpulse

```typescript  theme={"system"}
interface DeploymentMetadataImpulse {
    inputBlocks: CreateImpulseStateInput[];
    dspBlocks: (CreateImpulseStateDsp & { metadata: DSPFeatureMetadata | undefined })[];
    learnBlocks: CreateImpulseStateLearning[];
}
```

### DSPConfig

```typescript  theme={"system"}
interface DSPConfig {
    options: {[s: string]: string | number | boolean | null;};
    performance: { latency: number, ram: number } | undefined;
    calculateFeatureImportance: boolean;
    // Currently only used by EON tuner to identify blocks with the feature explorer
    // skipped.
    skipFeatureExplorer?: boolean;
}
```

### DSPFeatureMetadata

```typescript  theme={"system"}
interface DSPFeatureMetadata {
    created: Date;
    dspConfig: DSPConfig;
    labels: string[];   // the training labels
    featureLabels: string[] | undefined;
    featureCount: number;
    valuesPerAxis: number;
    windowCount: number;
    windowSizeMs: number;
    windowIncreaseMs: number;
    padZeros: boolean;
    frequency: number;
    outputConfig: DSPFeatureMetadataOutput;
    performance: { latency: number, ram: number } | undefined;
    fftUsed: number[] | undefined;
    includeEmptyLabels: boolean;
    inputShape: number[] | undefined;
    includedSamplesAreInOrder: boolean;
    resamplingAlgorithmVersion: number | undefined;
    resizingAlgorithmVersion: number | undefined;
}
```

### DSPFeatureMetadataOutput

```typescript  theme={"system"}
type DSPFeatureMetadataOutput = {
    type: 'image',
    shape: { width: number, height: number, channels: number, frames?: number },
    axes?: number
} | {
    type: 'spectrogram',
    shape: { width: number, height: number },
    axes?: number
} | {
    type: 'flat',
    shape: { width: number },
    axes?: number
};
```

### KerasModelIODetails

```typescript  theme={"system"}
/**
 * Information required to process a model's input and output data
 */
interface KerasModelIODetails {
    modelType: 'int8' | 'float32' | 'akida' | 'requiresRetrain';
    inputs: KerasModelTensorDetails[];
    outputs: KerasModelTensorDetails[];
}
```

### KerasModelTensorDetails

```typescript  theme={"system"}
/**
 * Information necessary to quantize or dequantize the contents of a tensor
 */
type KerasModelTensorDetails = {
    dataType: 'float32';
    // These are added since TF2.7 - older models don't have them
    name?: string;
    shape?: number[];
} | {
    dataType: 'int8' | 'uint8';
    // These are added since TF2.7 - older models don't have them
    name?: string;
    shape?: number[];
    // Scale and zero point are used only for quantized tensors
    quantizationScale?: number;
    quantizationZeroPoint?: number;
};
```

## File example

```json  theme={"system"}
{
    "version": 1,
    "samplesPerInference": 125,
    "axesCount": 3,
    "classes": [
        "idle",
        "snake",
        "updown",
        "wave"
    ],
    "deployCounter": 83,
    "folders": {
        "input": "/home/input",
        "output": "/home/output"
    },
    "frequency": 62.5,
    "impulse": {
        "inputBlocks": [
            {
                "id": 2,
                "type": "time-series",
                "name": "Time series",
                "title": "Time series data",
                "windowSizeMs": 2000,
                "windowIncreaseMs": 240,
                "frequencyHz": 62.5,
                "padZeros": false,
                "primaryVersion": true,
                "db": false
            }
        ],
        "dspBlocks": [
            {
                "id": 24,
                "type": "spectral-analysis",
                "name": "Spectral features",
                "axes": [
                    "accX",
                    "accY",
                    "accZ"
                ],
                "title": "Spectral Analysis",
                "input": 2,
                "primaryVersion": true,
                "createdBy": "createImpulse",
                "createdAt": "2022-08-07T07:39:37.055Z",
                "implementationVersion": 2,
                "db": false,
                "metadata": {
                    "created": "2023-08-29T01:32:50.434Z",
                    "dspConfig": {
                        "options": {
                            "scale-axes": 1,
                            "filter-cutoff": 8,
                            "filter-order": 6,
                            "fft-length": 64,
                            "spectral-peaks-count": 3,
                            "spectral-peaks-threshold": 0.1,
                            "spectral-power-edges": "0.1, 0.5, 1.0, 2.0, 5.0",
                            "do-log": true,
                            "do-fft-overlap": true,
                            "wavelet-level": 1,
                            "extra-low-freq": false,
                            "input-decimation-ratio": "1",
                            "filter-type": "low",
                            "analysis-type": "FFT",
                            "wavelet": "db4"
                        },
                        "performance": {
                            "latency": 4,
                            "ram": 2144
                        },
                        "calculateFeatureImportance": false
                    },
                    "labels": [
                        "idle",
                        "snake",
                        "updown",
                        "wave"
                    ],
                    "featureLabels": [
                        "accX RMS",
                        "accX Skewness",
                        "accX Kurtosis",
                        "accX Spectral Power 0.49 - 1.46 Hz",
                        "accX Spectral Power 1.46 - 2.44 Hz",
                        "accX Spectral Power 2.44 - 3.42 Hz",
                        "accX Spectral Power 3.42 - 4.39 Hz",
                        "accX Spectral Power 4.39 - 5.37 Hz",
                        "accX Spectral Power 5.37 - 6.35 Hz",
                        "accX Spectral Power 6.35 - 7.32 Hz",
                        "accX Spectral Power 7.32 - 8.3 Hz",
                        "accY RMS",
                        "accY Skewness",
                        "accY Kurtosis",
                        "accY Spectral Power 0.49 - 1.46 Hz",
                        "accY Spectral Power 1.46 - 2.44 Hz",
                        "accY Spectral Power 2.44 - 3.42 Hz",
                        "accY Spectral Power 3.42 - 4.39 Hz",
                        "accY Spectral Power 4.39 - 5.37 Hz",
                        "accY Spectral Power 5.37 - 6.35 Hz",
                        "accY Spectral Power 6.35 - 7.32 Hz",
                        "accY Spectral Power 7.32 - 8.3 Hz",
                        "accZ RMS",
                        "accZ Skewness",
                        "accZ Kurtosis",
                        "accZ Spectral Power 0.49 - 1.46 Hz",
                        "accZ Spectral Power 1.46 - 2.44 Hz",
                        "accZ Spectral Power 2.44 - 3.42 Hz",
                        "accZ Spectral Power 3.42 - 4.39 Hz",
                        "accZ Spectral Power 4.39 - 5.37 Hz",
                        "accZ Spectral Power 5.37 - 6.35 Hz",
                        "accZ Spectral Power 6.35 - 7.32 Hz",
                        "accZ Spectral Power 7.32 - 8.3 Hz"
                    ],
                    "valuesPerAxis": 11,
                    "windowCount": 2554,
                    "featureCount": 33,
                    "windowSizeMs": 2000,
                    "windowIncreaseMs": 240,
                    "frequency": 62.5,
                    "padZeros": false,
                    "outputConfig": {
                        "type": "flat",
                        "shape": {
                            "width": 33
                        }
                    },
                    "performance": {
                        "latency": 4,
                        "ram": 2144
                    },
                    "fftUsed": [
                        64
                    ],
                    "includeEmptyLabels": false,
                    "inputShape": [
                        375
                    ],
                    "includedSamplesAreInOrder": true
                }
            }
        ],
        "learnBlocks": [
            {
                "id": 7,
                "type": "keras",
                "name": "NN Classifier",
                "dsp": [
                    24
                ],
                "title": "Neural Network (Keras)",
                "primaryVersion": true,
                "db": false
            },
            {
                "id": 30,
                "type": "anomaly",
                "name": "Anomaly detection",
                "dsp": [
                    24
                ],
                "title": "Anomaly Detection (K-means)",
                "primaryVersion": true,
                "createdBy": "createImpulse",
                "createdAt": "2023-08-29T01:40:50.747Z",
                "db": false
            }
        ]
    },
    "project": {
        "name": "Tutorial: Continuous motion recognition",
        "id": 276194,
        "owner": "Edge Impulse Docs",
        "studioHost": "studio.edgeimpulse.com"
    },
    "sensor": "accelerometer",
    "tfliteModels": [
        {
            "arenaSize": 2982,
            "inputFrameSize": 33,
            "inputTensor": "dense_input",
            "outputTensor": "y_pred/Softmax:0",
            "details": {
                "modelType": "int8",
                "inputs": [
                    {
                        "dataType": "int8",
                        "name": "serving_default_x:0",
                        "shape": [
                            1,
                            33
                        ],
                        "quantizationScale": 0.10049157589673996,
                        "quantizationZeroPoint": -70
                    }
                ],
                "outputs": [
                    {
                        "dataType": "int8",
                        "name": "StatefulPartitionedCall:0",
                        "shape": [
                            1,
                            4
                        ],
                        "quantizationScale": 0.00390625,
                        "quantizationZeroPoint": -128
                    }
                ]
            },
            "modelPath": "/home/input/trained.tflite"
        }
    ]
}
```


Built with [Mintlify](https://mintlify.com).