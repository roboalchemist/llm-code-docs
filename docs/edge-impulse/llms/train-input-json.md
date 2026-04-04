# Source: https://docs.edgeimpulse.com/tools/specifications/files/train-input-json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# train_input.json

The `train_input.json` file is passed to [custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks) as the value for the `--input-file <file>` argument. It contains configuration information for model training options that you may want to use within your training script, if applicable. The specification is shown below.

## File structure

```typescript  theme={"system"}
type CreateKerasTrainModelOptions = {
    classes: string[],
    mode: 'classification' | 'regression' | 'object-detection' | 'visual-anomaly' | 'anomaly-gmm';
    printHWInfo: boolean | undefined,
    inputShapeString: string,
    yType: 'npy' | 'structured';
    trainTestSplit: number,
    stratifiedTrainTest: boolean,
    onlineDspConfig: OnlineDspConfig | undefined;
    convertInt8: boolean,
    profileInt8: boolean,
    skipEmbeddingsAndMemory: boolean,
    objectDetectionLastLayer: 'mobilenet-ssd' | 'fomo' | 'yolov2-akida' | 'yolov5' | 'yolov5v5-drpai' |
    'yolox' | 'yolov7' | 'tao-retinanet' | 'tao-ssd' | 'tao-yolov3' | 'tao-yolov4' | undefined;
    objectDetectionAugmentation: boolean | undefined,
    objectDetectionBatchSize: number | undefined,
    syntiantTarget?: boolean,
    maxTrainingTimeSeconds: number,
    remainingGpuComputeTimeSeconds: number,
    isEnterpriseProject: boolean,
    flattenDataset: boolean,
    akidaModel: boolean,
    akidaEdgeModel: boolean,
    skipMemoryProfiling: boolean,
    tensorboardLogging: boolean,
    customValidationSplit: boolean,
    validationMetadataKey?: string,
    customVariantsToProfile: CustomVariantInferenceJobModelVariant[] | undefined;
};
```

## File example

```json  theme={"system"}
{
    "classes": [
        "idle",
        "snake",
        "updown",
        "wave"
    ],
    "mode": "classification",
    "printHWInfo": false,
    "inputShapeString": "(39,)",
    "yType": "npy",
    "trainTestSplit": 0.2,
    "stratifiedTrainTest": false,
    "convertInt8": true,
    "profileInt8": true,
    "skipEmbeddingsAndMemory": false,
    "objectDetectionAugmentation": false,
    "syntiantTarget": false,
    "maxTrainingTimeSeconds": 604800,
    "remainingGpuComputeTimeSeconds": null,
    "isEnterpriseProject": true,
    "flattenDataset": false,
    "akidaModel": false,
    "akidaEdgeModel": false,
    "skipMemoryProfiling": false,
    "tensorboardLogging": false,
    "customValidationSplit": false
}
```


Built with [Mintlify](https://mintlify.com).