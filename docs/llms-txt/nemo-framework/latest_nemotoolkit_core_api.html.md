# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md

Title: NeMo Core APIs — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html

Published Time: Fri, 05 Sep 2025 19:01:32 GMT

Markdown Content:
NeMo Core APIs[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo-core-apis "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

Base class for all NeMo models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#base-class-for-all-nemo-models "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.ModelPT(_*args:Any_, _**kwargs:Any_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT "Link to this definition")
Bases: `LightningModule`, `Model`

Interface for Pytorch-lightning based NeMo models

on_fit_start()→None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_fit_start "Link to this definition")
Register debug hooks.

register_artifact(_config\_path:str_,_src:str_,_verify\_src\_exists:bool=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.register_artifact "Link to this definition")
Register model artifacts with this function. These artifacts (files) will be included inside .nemo file when model.save_to(“mymodel.nemo”) is called.

How it works:

1.   It always returns existing absolute path which can be used during Model constructor call
EXCEPTION: src is None or “” in which case nothing will be done and src will be returned

2.   It will add (config_path, model_utils.ArtifactItem()) pair to self.artifacts

> If "src" is local existing path:
>     then it will be returned in absolute path form.
> elif "src" starts with "nemo_file:unique_artifact_name":
>     .nemo will be untarred to a temporary folder location and an actual existing path will be returned
> else:
>     an error will be raised.

WARNING: use .register_artifact calls in your models’ constructors. The returned path is not guaranteed to exist after you have exited your model’s constructor.

Parameters:
*   **config_path** (_str_) – Artifact key. Usually corresponds to the model config.

*   **src** (_str_) – Path to artifact.

*   **verify_src_exists** (_bool_) – If set to False, then the artifact is optional and register_artifact will return None even if src is not found. Defaults to True.

Returns:If src is not None or empty it always returns absolute path which is guaranteed to exist during model
instance life

Return type:
str

has_artifacts()→bool[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.has_artifacts "Link to this definition")
Returns True if model has artifacts registered

has_native_or_submodules_artifacts()→bool[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.has_native_or_submodules_artifacts "Link to this definition")
Returns True if it has artifacts or any of the submodules have artifacts

has_nemo_submodules()→bool[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.has_nemo_submodules "Link to this definition")
Returns True if it has any registered NeMo submodules

register_nemo_submodule(_name:str_,_config\_field:str_,_model:[ModelPT](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT "nemo.core.classes.modelPT.ModelPT")_,)→None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.register_nemo_submodule "Link to this definition")
Adds a NeMo model as a submodule. Submodule can be accessed via the name attribute on the parent NeMo model this submodule was registered on (self). In the saving process, the whole parent model (self) is held as a solid model with artifacts from the child submodule, the submodule config will be saved to the config_field of the parent model. This method is necessary to create a nested model, e.g.

class ParentModel(ModelPT):
    def  __init__ (self, cfg, trainer=None):
        super(). __init__ (cfg=cfg, trainer=trainer)

        # annotate type for autocompletion and type checking (optional)
        self.child_model: Optional[ChildModel] = None
        if cfg.get("child_model") is not None:
            self.register_nemo_submodule(
                name="child_model",
                config_field="child_model",
                model=ChildModel(self.cfg.child_model, trainer=trainer),
            )
        # ... other code

Parameters:
*   **name** – name of the attribute for the submodule

*   **config_field** – field in config, where submodule config should be saved

*   **model** – NeMo model, instance of ModelPT

named_nemo_modules(_prefix\_name:str=''_,_prefix\_config:str=''_,)→Iterator[Tuple[str,str,[ModelPT](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT "nemo.core.classes.modelPT.ModelPT")]][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.named_nemo_modules "Link to this definition")
Returns an iterator over all NeMo submodules recursively, yielding tuples of (attribute path, path in config, submodule), starting from the core module

Parameters:
*   **prefix_name** – prefix for the name path

*   **prefix_config** – prefix for the path in config

Returns:
Iterator over (attribute path, path in config, submodule), starting from (prefix, self)

save_to(_save\_path:str_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.save_to "Link to this definition")Saves model instance (weights and configuration) into .nemo file
You can use “restore_from” method to fully restore instance from .nemo file.

.nemo file is an archive (tar.gz) with the following:model_config.yaml - model configuration in .yaml format. You can deserialize this into cfg argument for
model’s constructor

model_wights.ckpt - model checkpoint

Parameters:
**save_path** – Path to .nemo file where model instance should be saved

_classmethod_ restore_from(_restore\_path:str_,_override\_config\_path:omegaconf.OmegaConf|str|None=None_,_map\_location:torch.device|None=None_,_strict:bool=True_,_return\_config:bool=False_,_save\_restore\_connector:[SaveRestoreConnector](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save\_restore\_connector.SaveRestoreConnector "nemo.core.connectors.save\_restore\_connector.SaveRestoreConnector")|None=None_,_trainer:lightning.pytorch.Trainer|None=None_,_validate\_access\_integrity:bool=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.restore_from "Link to this definition")
Restores model instance (weights and configuration) from .nemo file.

Parameters:
*   **restore_path** – path to .nemo file from which model should be instantiated

*   **override_config_path** – path to a yaml config that will override the internal config file or an OmegaConf / DictConfig object representing the model config.

*   **map_location** – Optional torch.device() to map the instantiated model to a device. By default (None), it will select a GPU if available, falling back to CPU otherwise.

*   **strict** – Passed to load_state_dict. By default True.

*   **return_config** – If set to true, will return just the underlying config of the restored model as an OmegaConf DictConfig object without instantiating the model.

*   **trainer** – Optional, a pytorch lightning Trainer object that will be forwarded to the instantiated model’s constructor.

*   **save_restore_connector** ([_SaveRestoreConnector_](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector "nemo.core.connectors.save_restore_connector.SaveRestoreConnector")) – Can be overridden to add custom save and restore logic.

*   **Example** –

```
`
model = nemo.collections.asr.models.EncDecCTCModel.restore_from('asr.nemo')
assert isinstance(model, nemo.collections.asr.models.EncDecCTCModel)
`
```

Returns:
An instance of type cls or its underlying config (if return_config is set).

_classmethod_ load_from_checkpoint(_checkpoint\_path:str_,_*args_,_map\_location:Dict[str,str]|str|torch.device|int|Callable|None=None_,_hparams\_file:str|None=None_,_strict:bool=True_,_**kwargs_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.load_from_checkpoint "Link to this definition")
Loads ModelPT from checkpoint, with some maintenance of restoration. For documentation, please refer to LightningModule.load_from_checkpoint() documentation.

_abstract_ setup_training_data(_train\_data\_config:omegaconf.DictConfig|Dict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_training_data "Link to this definition")
Setups data loader to be used in training

Parameters:
**train_data_layer_config** – training data layer parameters.

Returns:

_abstract_ setup_validation_data(_val\_data\_config:omegaconf.DictConfig|Dict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_validation_data "Link to this definition")
Setups data loader to be used in validation :param val_data_layer_config: validation data layer parameters.

Returns:

setup_test_data(_test\_data\_config:omegaconf.DictConfig|Dict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_test_data "Link to this definition")
(Optionally) Setups data loader to be used in test

Parameters:
**test_data_layer_config** – test data layer parameters.

Returns:

setup_multiple_validation_data(_val\_data\_config:omegaconf.DictConfig|Dict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_multiple_validation_data "Link to this definition")
(Optionally) Setups data loader to be used in validation, with support for multiple data loaders.

Parameters:
**val_data_layer_config** – validation data layer parameters.

setup_multiple_test_data(_test\_data\_config:omegaconf.DictConfig|Dict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_multiple_test_data "Link to this definition")
(Optionally) Setups data loader to be used in test, with support for multiple data loaders.

Parameters:
**test_data_layer_config** – test data layer parameters.

setup_megatron_optimization(_optim\_config:Dict[str,Any]|omegaconf.DictConfig_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_megatron_optimization "Link to this definition")
Setup mcore optimizer config.

Parameters:
**optim_config** – Nemo optim args used to set up Mcore optimizer options.

setup_optimization(_optim\_config:omegaconf.DictConfig|Dict|None=None_,_optim\_kwargs:Dict[str,Any]|None=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_optimization "Link to this definition")
Prepares an optimizer from a string name and its optional config parameters.

Parameters:
*   **optim_config** –

A dictionary containing the following keys:

    *   ”lr”: mandatory key for learning rate. Will raise ValueError if not provided.

    *   ”optimizer”: string name pointing to one of the available optimizers in the registry. If not provided, defaults to “adam”.

    *   ”opt_args”: Optional list of strings, in the format “arg_name=arg_value”. The list of “arg_value” will be parsed and a dictionary of optimizer kwargs will be built and supplied to instantiate the optimizer.

*   **optim_kwargs** – A dictionary with additional kwargs for the optimizer. Used for non-primitive types that are not compatible with OmegaConf.

setup_optimizer_param_groups()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup_optimizer_param_groups "Link to this definition")
Used to create param groups for the optimizer. As an example, this can be used to specify per-layer learning rates:

optim.SGD([
{‘params’: model.base.parameters()}, {‘params’: model.classifier.parameters(), ‘lr’: 1e-3} ], lr=1e-2, momentum=0.9)

See [https://pytorch.org/docs/stable/optim.html](https://pytorch.org/docs/stable/optim.html) for more information. By default, ModelPT will use self.parameters(). Override this method to add custom param groups. In the config file, add ‘optim_param_groups’ to support different LRs for different components (unspecified params will use the default LR):

model:optim_param_groups:encoder:
lr: 1e-4 momentum: 0.8

decoder:
lr: 1e-3

optim:
lr: 3e-3 momentum: 0.9

configure_optimizers()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.configure_optimizers "Link to this definition")
Configure the optimizer and scheduler.

propagate_model_guid()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.propagate_model_guid "Link to this definition")
Propagates the model GUID to all submodules, recursively.

setup(_stage:str|None=None_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.setup "Link to this definition")
Called at the beginning of fit, validate, test, or predict. This is called on every process when using DDP.

Parameters:
**stage** – fit, validate, test or predict

train_dataloader()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.train_dataloader "Link to this definition")
Get the training dataloader.

val_dataloader()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.val_dataloader "Link to this definition")
Get the validation dataloader.

test_dataloader()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.test_dataloader "Link to this definition")
Get the test dataloader.

on_validation_epoch_end(_sync\_metrics:bool=False_,)→Dict[str,Dict[str,torch.Tensor]]|None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_validation_epoch_end "Link to this definition")
Default DataLoader for Validation set which automatically supports multiple data loaders via multi_validation_epoch_end.

If multi dataset support is not required, override this method entirely in base class. In such a case, there is no need to implement multi_validation_epoch_end either.

Note

If more than one data loader exists, and they all provide val_loss, only the val_loss of the first data loader will be used by default. This default can be changed by passing the special key val_dl_idx: int inside the validation_ds config.

Parameters:
**outputs** – Single or nested list of tensor outputs from one or more data loaders.

Returns:
A dictionary containing the union of all items from individual data_loaders, along with merged logs from all data loaders.

on_test_epoch_end()→Dict[str,Dict[str,torch.Tensor]]|None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_test_epoch_end "Link to this definition")
Default DataLoader for Test set which automatically supports multiple data loaders via multi_test_epoch_end.

If multi dataset support is not required, override this method entirely in base class. In such a case, there is no need to implement multi_test_epoch_end either.

Note

If more than one data loader exists, and they all provide test_loss, only the test_loss of the first data loader will be used by default. This default can be changed by passing the special key test_dl_idx: int inside the test_ds config.

Parameters:
**outputs** – Single or nested list of tensor outputs from one or more data loaders.

Returns:
A dictionary containing the union of all items from individual data_loaders, along with merged logs from all data loaders.

multi_validation_epoch_end(_outputs:List[Dict[str,torch.Tensor]]_,_dataloader\_idx:int=0_,)→Dict[str,Dict[str,torch.Tensor]]|None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.multi_validation_epoch_end "Link to this definition")
Adds support for multiple validation datasets. Should be overriden by subclass, so as to obtain appropriate logs for each of the dataloaders.

Parameters:
*   **outputs** – Same as that provided by LightningModule.on_validation_epoch_end() for a single dataloader.

*   **dataloader_idx** – int representing the index of the dataloader.

Returns:
A dictionary of values, optionally containing a sub-dict log, such that the values in the log will be pre-pended by the dataloader prefix.

multi_test_epoch_end(_outputs:List[Dict[str,torch.Tensor]]_,_dataloader\_idx:int=0_,)→Dict[str,Dict[str,torch.Tensor]]|None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.multi_test_epoch_end "Link to this definition")
Adds support for multiple test datasets. Should be overriden by subclass, so as to obtain appropriate logs for each of the dataloaders.

Parameters:
*   **outputs** – Same as that provided by LightningModule.on_validation_epoch_end() for a single dataloader.

*   **dataloader_idx** – int representing the index of the dataloader.

Returns:
A dictionary of values, optionally containing a sub-dict log, such that the values in the log will be pre-pended by the dataloader prefix.

get_validation_dataloader_prefix(_dataloader\_idx:int=0_,)→str[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.get_validation_dataloader_prefix "Link to this definition")
Get the name of one or more data loaders, which will be prepended to all logs.

Parameters:
**dataloader_idx** – Index of the data loader.

Returns:
str name of the data loader at index provided.

get_test_dataloader_prefix(_dataloader\_idx:int=0_)→str[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.get_test_dataloader_prefix "Link to this definition")
Get the name of one or more data loaders, which will be prepended to all logs.

Parameters:
**dataloader_idx** – Index of the data loader.

Returns:
str name of the data loader at index provided.

load_part_of_state_dict(_state\_dict_,_include_,_exclude_,_load\_from\_string=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.load_part_of_state_dict "Link to this definition")
Load a part of the state dict into the model.

maybe_init_from_pretrained_checkpoint(_cfg:omegaconf.OmegaConf_,_map\_location:str='cpu'_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.maybe_init_from_pretrained_checkpoint "Link to this definition")
Initializes a given model with the parameters obtained via specific config arguments. The state dict of the provided model will be updated with strict=False setting so as to prevent requirement of exact model parameters matching.

Initializations:
init_from_nemo_model: Str path to a .nemo model in order to load state_dict from single nemo file; if loading from multiple files, pass in a dict where the values have the following fields:

> path: Str path to .nemo model
> 
> 
> include: Optional list of strings, at least one of which needs to be contained in parameter name to be loaded from this .nemo file. Default: everything is included.
> 
> 
> exclude: Optional list of strings, which can be used to exclude any parameter containing one of these strings from being loaded from this .nemo file. Default: nothing is excluded.
> 
> 
> hydra usage example:
> 
> init_from_nemo_model:model0:
> path:<path/to/model1> include:[“encoder”]
> 
> model1:
> path:<path/to/model2> include:[“decoder”] exclude:[“embed”]

init_from_pretrained_model: Str name of a pretrained model checkpoint (obtained via cloud).
The model will be downloaded (or a cached copy will be used), instantiated and then its state dict will be extracted. If loading from multiple models, you can pass in a dict with the same format as for init_from_nemo_model, except with “name” instead of “path”

init_from_ptl_ckpt: Str name of a Pytorch Lightning checkpoint file. It will be loaded and
the state dict will extracted. If loading from multiple files, you can pass in a dict with the same format as for init_from_nemo_model.

Parameters:
*   **cfg** – The config used to instantiate the model. It need only contain one of the above keys.

*   **map_location** – str or torch.device() which represents where the intermediate state dict (from the pretrained model or checkpoint) will be loaded.

Extract the state dict(s) from a provided .nemo tarfile and save it to a directory.

Parameters:
*   **restore_path** – path to .nemo file from which state dict(s) should be extracted

*   **save_dir** – directory in which the saved state dict(s) should be stored

*   **split_by_module** – bool flag, which determins whether the output checkpoint should be for the entire Model, or the individual module’s that comprise the Model

*   **save_restore_connector** ([_SaveRestoreConnector_](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector "nemo.core.connectors.save_restore_connector.SaveRestoreConnector")) – Can be overrided to add custom save and restore logic.

Example

To convert the .nemo tarfile into a single Model level PyTorch checkpoint :: state_dict = nemo.collections.asr.models.EncDecCTCModel.extract_state_dict_from(‘asr.nemo’, ‘./asr_ckpts’)

To restore a model from a Model level checkpoint :: model = nemo.collections.asr.models.EncDecCTCModel(cfg) # or any other method of restoration model.load_state_dict(torch.load(“./asr_ckpts/model_weights.ckpt”))

To convert the .nemo tarfile into multiple Module level PyTorch checkpoints :: state_dict = nemo.collections.asr.models.EncDecCTCModel.extract_state_dict_from(

> > ‘asr.nemo’, ‘./asr_ckpts’, split_by_module=True
> 
> 
> )

To restore a module from a Module level checkpoint :: model = nemo.collections.asr.models.EncDecCTCModel(cfg) # or any other method of restoration

# load the individual components model.preprocessor.load_state_dict(torch.load(“./asr_ckpts/preprocessor.ckpt”)) model.encoder.load_state_dict(torch.load(“./asr_ckpts/encoder.ckpt”)) model.decoder.load_state_dict(torch.load(“./asr_ckpts/decoder.ckpt”))

Returns:
The state dict that was loaded from the original .nemo checkpoint

prepare_test(_trainer:lightning.pytorch.Trainer_)→bool[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.prepare_test "Link to this definition")
Helper method to check whether the model can safely be tested on a dataset after training (or loading a checkpoint).

trainer = Trainer()
if model.prepare_test(trainer):
    trainer.test(model)

Returns:
bool which declares the model safe to test. Provides warnings if it has to return False to guide the user.

set_trainer(_trainer:lightning.pytorch.Trainer_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.set_trainer "Link to this definition")
Set an instance of Trainer object.

Parameters:
**trainer** – PyTorch Lightning Trainer object.

set_world_size(_trainer:lightning.pytorch.Trainer_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.set_world_size "Link to this definition")
Determines the world size from the PyTorch Lightning Trainer. And then updates AppState.

Parameters:
**trainer** (_Trainer_) – PyTorch Lightning Trainer object

summarize(_max\_depth:int=1_,)→lightning.pytorch.utilities.model_summary.ModelSummary[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.summarize "Link to this definition")
Summarize this LightningModule.

Parameters:
**max_depth** – The maximum depth of layer nesting that the summary will include. A value of 0 turns the layer summary off. Default: 1.

Returns:
The model summary object

_property_ num_weights[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.num_weights "Link to this definition")
Utility property that returns the total number of parameters of the Model.

trainer()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.trainer "Link to this definition")
Get the trainer object.

_property_ cfg[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.cfg "Link to this definition")
Property that holds the finalized internal config of the model.

Note

Changes to this config are not reflected in the state of the model. Please create a new model using an updated config to properly update the model.

_property_ hparams[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.hparams "Link to this definition")
Overwrite default hparams property to return the lastest model config. Without this change, the hparams property would return the old config if there was a direct change to self._cfg (e.g., in self.setup_optimization()) that was not done via self.cfg = new_cfg.

_property_ validation_step_outputs[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.validation_step_outputs "Link to this definition")
Cached outputs of validation_step. It can be a list of items (for single data loader) or a list of lists (for multiple data loaders).

Returns:
List of outputs of validation_step.

_property_ test_step_outputs[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.test_step_outputs "Link to this definition")
Cached outputs of test_step. It can be a list of items (for single data loader) or a list of lists (for multiple data loaders).

Returns:
List of outputs of test_step.

_classmethod_ update_save_restore_connector(_save\_restore\_connector_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.update_save_restore_connector "Link to this definition")
Update the save_restore_connector for the model.

on_train_start()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_train_start "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-start](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-start) We use it here to copy the relevant config for dynamic freezing.

on_train_batch_start(_batch:Any_,_batch\_idx:int_,_unused:int=0_,)→int|None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_train_batch_start "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-start](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-start) We use it here to enable profiling and dynamic freezing.

on_train_batch_end(_outputs_,_batch:Any_,_batch\_idx:int_,_unused:int=0_,)→None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_train_batch_end "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-end) We use it here to enable nsys profiling.

on_train_end()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_train_end "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-end) We use it here to cleanup the dynamic freezing config.

on_test_end()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_test_end "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end)

on_predict_end()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT.on_predict_end "Link to this definition")
PyTorch Lightning hook: [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end)

Base Neural Module class[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#base-neural-module-class "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.NeuralModule(_*args:Any_, _**kwargs:Any_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule "Link to this definition")
Bases: `Module`, `Typing`, `Serialization`, `FileIO`

Abstract class offering interface shared between all PyTorch Neural Modules.

_property_ num_weights[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule.num_weights "Link to this definition")
Utility property that returns the total number of parameters of NeuralModule.

input_example(_max\_batch=None_, _max\_dim=None_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule.input_example "Link to this definition")
Override this method if random inputs won’t work :returns: A tuple sample of valid input data.

freeze()→None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule.freeze "Link to this definition")
Freeze all params for inference.

This method sets requires_grad to False for all parameters of the module. It also stores the original requires_grad state of each parameter in a dictionary, so that unfreeze() can restore the original state if partial=True is set in unfreeze().

unfreeze(_partial:bool=False_)→None[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule.unfreeze "Link to this definition")
Unfreeze all parameters for training.

Allows for either total unfreeze or partial unfreeze (if the module was explicitly frozen previously with freeze()). The partial argument is used to determine whether to unfreeze all parameters or only the parameters that were previously unfrozen prior freeze().

Example

Consider a model that has an encoder and a decoder module. Assume we want the encoder to be frozen always.

```
`python
model.encoder.freeze()  # Freezes all parameters in the encoder explicitly
`
```

During inference, all parameters of the model should be frozen - we do this by calling the model’s freeze method. This step records that the encoder module parameters were already frozen, and so if partial unfreeze is called, we should keep the encoder parameters frozen.

```
`python
model.freeze()  # Freezes all parameters in the model; encoder remains frozen
`
```

Now, during fine-tuning, we want to unfreeze the decoder but keep the encoder frozen. We can do this by calling unfreeze(partial=True).

```
`python
model.unfreeze(partial=True)  # Unfreezes only the decoder; encoder remains frozen
`
```

Parameters:
**partial** – If True, only unfreeze parameters that were previously frozen. If the parameter was already frozen when calling freeze(), it will remain frozen after calling unfreeze(partial=True).

as_frozen()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.NeuralModule.as_frozen "Link to this definition")
Context manager which temporarily freezes a module, yields control and finally unfreezes the module partially to return to original state.

Allows for either total unfreeze or partial unfreeze (if the module was explicitly frozen previously with freeze()). The partial argument is used to determine whether to unfreeze all parameters or only the parameters that were previously unfrozen prior freeze().

Example

with model.as_frozen(): # by default, partial = True
# Do something with the model pass

# Model’s parameters are now back to original state of requires_grad

Base Mixin classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#base-mixin-classes "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.Typing
Bases: `ABC`

An interface which endows module with neural types

_property_ input_types _:Dict[str,[NeuralType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural\_types.NeuralType "nemo.core.neural\_types.neural\_type.NeuralType")]|None_
Define these to enable input neural type checks

_property_ output_types _:Dict[str,[NeuralType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural\_types.NeuralType "nemo.core.neural\_types.neural\_type.NeuralType")]|None_
Define these to enable output neural type checks

_validate_input_types(_input\_types=None_,_ignore\_collections=False_,_**kwargs_,)
This function does a few things.

1.   It ensures that len(self.input_types <non-optional>) <= len(kwargs) <= len(self.input_types).

2.   For each (keyword name, keyword value) passed as input to the wrapped function:
    *   Check if the keyword name exists in the list of valid self.input_types names.

    *   Check if keyword value has the neural_type property.
        *   If it does, then perform a comparative check and assert that neural types
are compatible (SAME or GREATER).

    *   Check if keyword value is a container type (list or tuple). If yes,
then perform the elementwise test of neural type above on each element of the nested structure, recursively.

Parameters:
*   **input_types** – Either the input_types defined at class level, or the local function overridden type definition.

*   **ignore_collections** – For backward compatibility, container support can be disabled explicitly using this flag. When set to True, all nesting is ignored and nest-depth checks are skipped.

*   **kwargs** – Dictionary of argument_name:argument_value pairs passed to the wrapped function upon call.

_attach_and_validate_output_types(_out\_objects_,_ignore\_collections=False_,_output\_types=None_,)
This function does a few things.

1.   It ensures that len(out_object) == len(self.output_types).

2.   If the output is a tensor (or list/tuple of list/tuple … of tensors), it
attaches a neural_type to it. For objects without the neural_type attribute, such as python objects (dictionaries and lists, primitive data types, structs), no neural_type is attached.

Note: tensor.neural_type is only checked during _validate_input_types which is called prior to forward().

Parameters:
*   **output_types** – Either the output_types defined at class level, or the local function overridden type definition.

*   **ignore_collections** – For backward compatibility, container support can be disabled explicitly using this flag. When set to True, all nesting is ignored and nest-depth checks are skipped.

*   **out_objects** – The outputs of the wrapped function.

__check_neural_type(_obj_,_metadata:TypecheckMetadata_,_depth:int_,_name:str|None=None_,)
Recursively tests whether the obj satisfies the semantic neural type assertion. Can include shape checks if shape information is provided.

Parameters:
*   **obj** – Any python object that can be assigned a value.

*   **metadata** – TypecheckMetadata object.

*   **depth** – Current depth of recursion.

*   **name** – Optional name used of the source obj, used when an error occurs.

__attach_neural_type(_obj_,_metadata:TypecheckMetadata_,_depth:int_,_name:str|None=None_,)
Recursively attach neural types to a given object - as long as it can be assigned some value.

Parameters:
*   **obj** – Any python object that can be assigned a value.

*   **metadata** – TypecheckMetadata object.

*   **depth** – Current depth of recursion.

*   **name** – Optional name used of the source obj, used when an error occurs.

* * *

_class_ nemo.core.Serialization
Bases: `ABC`

_classmethod_ from_config_dict(_config:DictConfig_,_trainer:'Trainer'|None=None_,)
Instantiates object using DictConfig-based configuration

to_config_dict()→omegaconf.DictConfig
Returns object’s configuration to config dictionary

* * *

_class_ nemo.core.FileIO
Bases: `ABC`

save_to(_save\_path:str_)
Standardized method to save a tarfile containing the checkpoint, config, and any additional artifacts. Implemented via [`nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to()`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to "nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to").

Parameters:
**save_path** – str, path to where the file should be saved.

_classmethod_ restore_from(_restore\_path:str_,_override\_config\_path:str|None=None_,_map\_location:'torch.device'|None=None_,_strict:bool=True_,_return\_config:bool=False_,_trainer:'Trainer'|None=None_,_save\_restore\_connector:[SaveRestoreConnector](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save\_restore\_connector.SaveRestoreConnector "nemo.core.connectors.save\_restore\_connector.SaveRestoreConnector")=None_,)
Restores model instance (weights and configuration) from a .nemo file

Parameters:
*   **restore_path** – path to .nemo file from which model should be instantiated

*   **override_config_path** – path to a yaml config that will override the internal config file or an OmegaConf / DictConfig object representing the model config.

*   **map_location** – Optional torch.device() to map the instantiated model to a device. By default (None), it will select a GPU if available, falling back to CPU otherwise.

*   **strict** – Passed to load_state_dict. By default True

*   **return_config** – If set to true, will return just the underlying config of the restored model as an OmegaConf DictConfig object without instantiating the model.

*   **trainer** – An optional Trainer object, passed to the model constructor.

*   **save_restore_connector** – An optional SaveRestoreConnector object that defines the implementation of the restore_from() method.

_classmethod_ from_config_file(_path2yaml\_file:str_)
Instantiates an instance of NeMo Model from YAML config file. Weights will be initialized randomly. :param path2yaml_file: path to yaml file with model configuration

Returns:

to_config_file(_path2yaml\_file:str_)
Saves current instance’s configuration to YAML config file. Weights will not be saved. :param path2yaml_file: path2yaml_file: path to yaml file where model model configuration will be saved

Returns:

Base Connector classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#base-connector-classes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.connectors.save_restore_connector.SaveRestoreConnector[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector "Link to this definition")
Bases: `object`

Connector for saving and restoring models.

save_to(_model:[ModelPT](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.ModelPT "nemo.core.classes.modelPT.ModelPT")_,_save\_path:str_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to "Link to this definition")
Saves model instance (weights and configuration) into .nemo file. You can use “restore_from” method to fully restore instance from .nemo file.

.nemo file is an archive (tar.gz) with the following:model_config.yaml - model configuration in .yaml format.
You can deserialize this into cfg argument for model’s constructor

model_wights.ckpt - model checkpoint

Parameters:
*   **model** – ModelPT object to be saved.

*   **save_path** – Path to .nemo file where model instance should be saved

Returns:Path to .nemo file where model instance was saved (same as save_path argument) or None if not rank 0
The path can be a directory if the flag pack_nemo_file is set to False.

Return type:
str

load_config_and_state_dict(_calling\_cls_,_restore\_path:str_,_override\_config\_path:omegaconf.OmegaConf|str|None=None_,_map\_location:torch.device|None=None_,_strict:bool=True_,_return\_config:bool=False_,_trainer:lightning.pytorch.trainer.trainer.Trainer|None=None_,_validate\_access\_integrity:bool=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.load_config_and_state_dict "Link to this definition")
Restores model instance (weights and configuration) into .nemo file

Parameters:
*   **restore_path** – path to .nemo file from which model should be instantiated

*   **override_config_path** – path to a yaml config that will override the internal config file or an OmegaConf / DictConfig object representing the model config.

*   **map_location** – Optional torch.device() to map the instantiated model to a device. By default (None), it will select a GPU if available, falling back to CPU otherwise.

*   **strict** – Passed to load_state_dict. By default True

*   **return_config** – If set to true, will return just the underlying config of the restored model as an OmegaConf DictConfig object without instantiating the model.

Example

```
`
model = nemo.collections.asr.models.EncDecCTCModel.restore_from('asr.nemo')
assert isinstance(model, nemo.collections.asr.models.EncDecCTCModel)
`
```

Returns:
An instance of type cls or its underlying config (if return_config is set).

modify_state_dict(_conf_, _state\_dict_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.modify_state_dict "Link to this definition")
Utility method that allows to modify the state dict before loading parameters into a model. :param conf: A model level OmegaConf object. :param state_dict: The state dict restored from the checkpoint.

Returns:
A potentially modified state dict.

load_instance_with_state_dict(_instance_,_state\_dict_,_strict_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.load_instance_with_state_dict "Link to this definition")
Utility method that loads a model instance with the (potentially modified) state dict.

Parameters:
*   **instance** – ModelPT subclass instance.

*   **state_dict** – The state dict (which may have been modified)

*   **strict** – Bool, whether to perform strict checks when loading the state dict.

restore_from(_calling\_cls_,_restore\_path:str_,_override\_config\_path:omegaconf.OmegaConf|str|None=None_,_map\_location:torch.device|None=None_,_strict:bool=True_,_return\_config:bool=False_,_trainer:lightning.pytorch.trainer.trainer.Trainer|None=None_,_validate\_access\_integrity:bool=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.restore_from "Link to this definition")
Restores model instance (weights and configuration) into .nemo file

Parameters:
*   **restore_path** – path to .nemo file from which model should be instantiated

*   **override_config_path** – path to a yaml config that will override the internal config file or an OmegaConf / DictConfig object representing the model config.

*   **map_location** – Optional torch.device() to map the instantiated model to a device. By default (None), it will select a GPU if available, falling back to CPU otherwise.

*   **strict** – Passed to load_state_dict. By default True

*   **return_config** – If set to true, will return just the underlying config of the restored model as an OmegaConf DictConfig object without instantiating the model.

*   **trainer** – An optional Trainer object, passed to the model constructor.

Example

```
`
model = nemo.collections.asr.models.EncDecCTCModel.restore_from('asr.nemo')
assert isinstance(model, nemo.collections.asr.models.EncDecCTCModel)
`
```

Returns:
An instance of type cls or its underlying config (if return_config is set).

Extract the state dict(s) from a provided .nemo tarfile and save it to a directory.

Parameters:
*   **restore_path** – path to .nemo file from which state dict(s) should be extracted

*   **save_dir** – directory in which the saved state dict(s) should be stored

*   **split_by_module** – bool flag, which determins whether the output checkpoint should be for the entire Model, or the individual module’s that comprise the Model

Example

To convert the .nemo tarfile into a single Model level PyTorch checkpoint :: state_dict = nemo.collections.asr.models.EncDecCTCModel.extract_state_dict_from(‘asr.nemo’, ‘./asr_ckpts’)

To restore a model from a Model level checkpoint :: model = nemo.collections.asr.models.EncDecCTCModel(cfg) # or any other method of restoration model.load_state_dict(torch.load(“./asr_ckpts/model_weights.ckpt”))

To convert the .nemo tarfile into multiple Module level PyTorch checkpoints :: state_dict = nemo.collections.asr.models.EncDecCTCModel.extract_state_dict_from(

> ‘asr.nemo’, ‘./asr_ckpts’, split_by_module=True

)

To restore a module from a Module level checkpoint :: model = nemo.collections.asr.models.EncDecCTCModel(cfg) # or any other method of restoration

# load the individual components model.preprocessor.load_state_dict(torch.load(“./asr_ckpts/preprocessor.ckpt”)) model.encoder.load_state_dict(torch.load(“./asr_ckpts/encoder.ckpt”)) model.decoder.load_state_dict(torch.load(“./asr_ckpts/decoder.ckpt”))

Returns:
The state dict that was loaded from the original .nemo checkpoint

register_artifact(_model_,_config\_path:str_,_src:str_,_verify\_src\_exists:bool=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.register_artifact "Link to this definition")
Register model artifacts with this function. These artifacts (files) will be included inside .nemo file when model.save_to(“mymodel.nemo”) is called.

How it works:

1.   It always returns existing absolute path which can be used during Model constructor call
EXCEPTION: src is None or “” in which case nothing will be done and src will be returned

2.   It will add (config_path, model_utils.ArtifactItem()) pair to self.artifacts

> If "src" is local existing path:
>     then it will be returned in absolute path form
> elif "src" starts with "nemo_file:unique_artifact_name":
>     .nemo will be untarred to a temporary folder location and an actual existing path will be returned
> else:
>     an error will be raised.

WARNING: use .register_artifact calls in your models’ constructors. The returned path is not guaranteed to exist after you have exited your model’s constructor.

Parameters:
*   **model** – ModelPT object to register artifact for.

*   **config_path** (_str_) – Artifact key. Usually corresponds to the model config.

*   **src** (_str_) – Path to artifact.

*   **verify_src_exists** (_bool_) – If set to False, then the artifact is optional and register_artifact will return None even if src is not found. Defaults to True.

Returns:If src is not None or empty it always returns absolute path which is guaranteed to exists during model
instance life

Return type:
str

_property_ model_config_yaml _:str_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.model_config_yaml "Link to this definition")
Get the path to the model config yaml file.

_property_ model_weights_ckpt _:str_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.model_weights_ckpt "Link to this definition")
Get the path to the model weights checkpoint file.

Get the path to the model extracted directory.

_property_ pack_nemo_file _:bool_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.pack_nemo_file "Link to this definition")
Get the flag for packing a nemo file.

Base Mixin Classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#id1 "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.classes.mixins.access_mixins.AccessMixin[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin "Link to this definition")
Bases: `ABC`

Allows access to output of intermediate layers of a model

register_accessible_tensor(_name_, _tensor_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin.register_accessible_tensor "Link to this definition")
Register tensor for later use.

_classmethod_ get_module_registry(_module:torch.nn.Module_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin.get_module_registry "Link to this definition")
Extract all registries from named submodules, return dictionary where the keys are the flattened module names, the values are the internal registry of each such module.

reset_registry(_registry\_key:str|None=None_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin.reset_registry "Link to this definition")
Reset the registries of all named sub-modules

_property_ access_cfg[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.access_mixins.AccessMixin.access_cfg "Link to this definition")
Returns: The global access config shared across all access mixin modules.

* * *

_class_ nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO "Link to this definition")
Bases: `ABC`

Mixin that provides Hugging Face file IO functionality for NeMo models. It is usually implemented as a mixin to ModelPT.

This mixin provides the following functionality: - search_huggingface_models(): Search the hub programmatically via some model filter. - push_to_hf_hub(): Push a model to the hub.

_classmethod_ get_hf_model_filter()→Dict[str,Any][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.get_hf_model_filter "Link to this definition")
Generates a filter for HuggingFace models.

Additionaly includes default values of some metadata about results returned by the Hub.

Metadata:
resolve_card_info: Bool flag, if set, returns the model card metadata. Default: False. limit_results: Optional int, limits the number of results returned.

Returns:
A dict representing the arguments passable to huggingface list_models().

_classmethod_ search_huggingface_models(_model\_filter:Dict[str,Any]|None=None_,)→Iterable[huggingface_hub.hf_api.ModelInfo][#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.search_huggingface_models "Link to this definition")
Should list all pre-trained models available via Hugging Face Hub.

The following metadata can be passed via the model_filter for additional results. Metadata:

> resolve_card_info: Bool flag, if set, returns the model card metadata. Default: False.
> 
> 
> limit_results: Optional int, limits the number of results returned.

# You can replace <DomainSubclass> with any subclass of ModelPT.
from nemo.core import ModelPT

# Get default filter dict
filt = <DomainSubclass>.get_hf_model_filter()

# Make any modifications to the filter as necessary
filt['language'] = [...]
filt['task'] = ...
filt['tags'] = [...]

# Add any metadata to the filter as needed (kwargs to list_models)
filt['limit'] = 5

# Obtain model info
model_infos = <DomainSubclass>.search_huggingface_models(model_filter=filt)

# Browse through cards and select an appropriate one
card = model_infos[0]

# Restore model using `modelId` of the card.
model = ModelPT.from_pretrained(card.modelId)

Parameters:
**model_filter** – Optional Dictionary (for Hugging Face Hub kwargs) that filters the returned list of compatible model cards, and selects all results from each filter. Users can then use model_card.modelId in from_pretrained() to restore a NeMo Model.

Returns:
A list of ModelInfo entries.

push_to_hf_hub(_repo\_id:str_,_*_,_pack\_nemo\_file:bool=True_,_model\_card:huggingface\_hub.ModelCard|None|object|str=None_,_commit\_message:str='Push model using huggingface\_hub.'_,_private:bool=False_,_api\_endpoint:str|None=None_,_token:str|None=None_,_branch:str|None=None_,_allow\_patterns:List[str]|str|None=None_,_ignore\_patterns:List[str]|str|None=None_,_delete\_patterns:List[str]|str|None=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.push_to_hf_hub "Link to this definition")
Upload model checkpoint to the Hub.

Use allow_patterns and ignore_patterns to precisely filter which files should be pushed to the hub. Use delete_patterns to delete existing remote files in the same commit. See [upload_folder] reference for more details.

Parameters:
*   **repo_id** (str) – ID of the repository to push to (example: “username/my-model”).

*   **pack_nemo_file** (bool, _optional_, defaults to True) – Whether to pack the model checkpoint and configuration into a single .nemo file. If set to false, uploads the contents of the directory containing the model checkpoint and configuration plus additional artifacts.

*   **model_card** (ModelCard, _optional_) – Model card to upload with the model. If None, will use the model card template provided by the class itself via generate_model_card(). Any object that implements str(obj) can be passed here. Two keyword replacements are passed to generate_model_card(): model_name and repo_id. If the model card generates a string, and it contains {model_name} or {repo_id}, they will be replaced with the actual values.

*   **commit_message** (str, _optional_) – Message to commit while pushing.

*   **private** (bool, _optional_, defaults to False) – Whether the repository created should be private.

*   **api_endpoint** (str, _optional_) – The API endpoint to use when pushing the model to the hub.

*   **token** (str, _optional_) – The token to use as HTTP bearer authorization for remote files. By default, it will use the token cached when running huggingface-cli login.

*   **branch** (str, _optional_) – The git branch on which to push the model. This defaults to “main”.

*   **allow_patterns** (List[str] or str, _optional_) – If provided, only files matching at least one pattern are pushed.

*   **ignore_patterns** (List[str] or str, _optional_) – If provided, files matching any of the patterns are not pushed.

*   **delete_patterns** (List[str] or str, _optional_) – If provided, remote files matching any of the patterns will be deleted from the repo.

Returns:
The url of the uploaded HF repo.

Neural Type checking[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#neural-type-checking "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.classes.common.typecheck(_input\_types:[TypeState](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.TypeState "nemo.core.classes.common.typecheck.TypeState")|Dict[str,[NeuralType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural\_types.NeuralType "nemo.core.neural\_types.NeuralType")]=TypeState.UNINITIALIZED_,_output\_types:[TypeState](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.TypeState "nemo.core.classes.common.typecheck.TypeState")|Dict[str,[NeuralType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural\_types.NeuralType "nemo.core.neural\_types.NeuralType")]=TypeState.UNINITIALIZED_,_ignore\_collections:bool=False_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck "Link to this definition")
Bases: `object`

A decorator which performs input-output neural type checks, and attaches neural types to the output of the function that it wraps.

Requires that the class inherit from `Typing` in order to perform type checking, and will raise an error if that is not the case.

# Usage (Class level type support)

@typecheck()
def fn(self, arg1, arg2, ...):
    ...

# Usage (Function level type support)

@typecheck(input_types=..., output_types=...)
def fn(self, arg1, arg2, ...):
    ...

Points to be noted:

1.   The brackets () in @typecheck() are necessary.

> You will encounter a TypeError: __init__() takes 1 positional argument but X were given without those brackets.

2.   The function can take any number of positional arguments during definition.

> When you call this function, all arguments must be passed using kwargs only.

 __call__ (_wrapped_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.__call__ "Link to this definition")
Call self as a function.

_class_ TypeState(_value_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.TypeState "Link to this definition")
Bases: `Enum`

Placeholder to denote the default value of type information provided. If the constructor of this decorator is used to override the class level type definition, this enum value indicate that types will be overridden.

wrapped_call(_wrapped_,_instance:Typing_,_args_,_kwargs_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.wrapped_call "Link to this definition")
Wrapper method that can be used on any function of a class that implements `Typing`. By default, it will utilize the input_types and output_types properties of the class inheriting Typing.

Local function level overrides can be provided by supplying dictionaries as arguments to the decorator.

Parameters:
*   **input_types** – Union[TypeState, Dict[str, NeuralType]]. By default, uses the global input_types.

*   **output_types** – Union[TypeState, Dict[str, NeuralType]]. By default, uses the global output_types.

*   **ignore_collections** – Bool. Determines if container types should be asserted for depth checks, or if depth checks are skipped entirely.

_static_ set_typecheck_enabled(_enabled:bool=True_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.set_typecheck_enabled "Link to this definition")
Global method to enable/disable typechecking.

Parameters:
**enabled** – bool, when True will enable typechecking.

_static_ disable_checks()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.disable_checks "Link to this definition")
Context manager that temporarily disables type checking within its context.

_static_ set_semantic_check_enabled(_enabled:bool=True_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.set_semantic_check_enabled "Link to this definition")
Global method to enable/disable semantic typechecking.

Parameters:
**enabled** – bool, when True will enable semantic typechecking.

_static_ disable_semantic_checks()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.disable_semantic_checks "Link to this definition")
Context manager that temporarily disables semantic type checking within its context.

Neural Type classes[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#neural-type-classes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.neural_types.NeuralType(_axes:Any|None=None_,_elements\_type:Any|None=None_,_optional:bool=False_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.NeuralType "Link to this definition")
Bases: `object`

This is the main class which would represent neural type concept. It is used to represent _the types_ of inputs and outputs.

Parameters:
*   **axes** (_Optional_ _[_ _Tuple_ _]_) – a tuple of AxisTypes objects representing the semantics of what varying each axis means You can use a short, string-based form here. For example: (‘B’, ‘C’, ‘H’, ‘W’) would correspond to an NCHW format frequently used in computer vision. (‘B’, ‘T’, ‘D’) is frequently used for signal processing and means [batch, time, dimension/channel].

*   **elements_type** ([_ElementType_](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.elements.ElementType "nemo.core.neural_types.elements.ElementType")) – an instance of ElementType class representing the semantics of what is stored inside the tensor. For example: logits (LogitsType), log probabilities (LogprobType), etc.

*   **optional** (_bool_) – By default, this is false. If set to True, it would means that input to the port of this type can be optional.

compare(_second_,)→[NeuralTypeComparisonResult](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.comparison.NeuralTypeComparisonResult "nemo.core.neural_types.comparison.NeuralTypeComparisonResult")[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.NeuralType.compare "Link to this definition")
Performs neural type comparison of self with second. When you chain two modules’ inputs/outputs via __call__ method, this comparison will be called to ensure neural type compatibility.

compare_and_raise_error(_parent\_type\_name_,_port\_name_,_second\_object_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.NeuralType.compare_and_raise_error "Link to this definition")
Method compares definition of one type with another and raises an error if not compatible.

* * *

_class_ nemo.core.neural_types.axes.AxisType(_kind:AxisKindAbstract_,_size:int|None=None_,_is\_list=False_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.axes.AxisType "Link to this definition")
Bases: `object`

This class represents axis semantics and (optionally) it’s dimensionality :param kind: what kind of axis it is? For example Batch, Height, etc. :type kind: AxisKindAbstract :param size: specify if the axis should have a fixed size. By default it is set to None and you :type size: int, optional :param typically do not want to set it for Batch and Time: :param is_list: whether this is a list or a tensor axis :type is_list: bool, default=False

* * *

_class_ nemo.core.neural_types.elements.ElementType[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.elements.ElementType "Link to this definition")
Bases: `ABC`

Abstract class defining semantics of the tensor elements. We are relying on Python for inheritance checking

_property_ type_parameters _:Dict[str,Any]_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.elements.ElementType.type_parameters "Link to this definition")
Override this property to parametrize your type. For example, you can specify ‘storage’ type such as float, int, bool with ‘dtype’ keyword. Another example, is if you want to represent a signal with a particular property (say, sample frequency), then you can put sample_freq->value in there. When two types are compared their type_parameters must match.

_property_ fields[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.elements.ElementType.fields "Link to this definition")
This should be used to logically represent tuples/structures. For example, if you want to represent a bounding box (x, y, width, height) you can put a tuple with names (‘x’, y’, ‘w’, ‘h’) in here. Under the hood this should be converted to the last tesnor dimension of fixed size = len(fields). When two types are compared their fields must match.

* * *

_class_ nemo.core.neural_types.comparison.NeuralTypeComparisonResult(_value_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.comparison.NeuralTypeComparisonResult "Link to this definition")
Bases: `Enum`

The result of comparing two neural type objects for compatibility. When comparing A.compare_to(B):

Experiment manager[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#experiment-manager "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.utils.exp_manager.exp_manager(_trainer:lightning.pytorch.Trainer_,_cfg:omegaconf.DictConfig|Dict|None=None_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.exp_manager "Link to this definition")
Bases:

exp_manager is a helper function used to manage folders for experiments. It follows the pytorch lightning paradigm of exp_dir/model_or_experiment_name/version. If the lightning trainer has a logger, exp_manager will get exp_dir, name, and version from the logger. Otherwise it will use the exp_dir and name arguments to create the logging directory. exp_manager also allows for explicit folder creation via explicit_log_dir.

The version can be a datetime string or an integer. Datestime version can be disabled if use_datetime_version is set to False. It optionally creates TensorBoardLogger, WandBLogger, DLLogger, MLFlowLogger, ClearMLLogger, ModelCheckpoint objects from pytorch lightning. It copies sys.argv, and git information if available to the logging directory. It creates a log file for each process to log their output into.

exp_manager additionally has a resume feature (resume_if_exists) which can be used to continuing training from the constructed log_dir. When you need to continue the training repeatedly (like on a cluster which you need multiple consecutive jobs), you need to avoid creating the version folders. Therefore from v1.0.0, when resume_if_exists is set to True, creating the version folders is ignored.

Parameters:
*   **trainer** (_lightning.pytorch.Trainer_) – The lightning trainer.

*   **cfg** (_DictConfig_ _,_ _dict_) –

Can have the following keys:

    *   explicit_log_dir (str, Path): Can be used to override exp_dir/name/version folder
creation. Defaults to None, which will use exp_dir, name, and version to construct the logging directory.

    *   exp_dir (str, Path): The base directory to create the logging directory.
Defaults to None, which logs to ./nemo_experiments.

    *   name (str): The name of the experiment. Defaults to None which turns into “default”
via name = name or “default”.

    *   version (str): The version of the experiment. Defaults to None which uses either a
datetime string or lightning’s TensorboardLogger system of using version_{int}.

    *   use_datetime_version (bool): Whether to use a datetime string for version.
Defaults to True.

    *   resume_if_exists (bool): Whether this experiment is resuming from a previous run.
If True, it sets trainer._checkpoint_connector._ckpt_path so that the trainer should auto-resume. exp_manager will move files under log_dir to log_dir/run_{int}. Defaults to False. From v1.0.0, when resume_if_exists is True, we would not create version folders to make it easier to find the log folder for next runs.

    *   resume_past_end (bool): exp_manager errors out if resume_if_exists is True
and a checkpoint matching `*end.ckpt` indicating a previous training run fully completed. This behaviour can be disabled, in which case the `*end.ckpt` will be loaded by setting resume_past_end to True. Defaults to False.

    *   resume_ignore_no_checkpoint (bool): exp_manager errors out if resume_if_exists is True
and no checkpoint could be found. This behaviour can be disabled, in which case exp_manager will print a message and continue without restoring, by setting resume_ignore_no_checkpoint to True. Defaults to False.

    *   resume_from_checkpoint (str): Can be used to specify a path to a specific checkpoint
file to load from. This will override any checkpoint found when resume_if_exists is True. Defaults to None.

    *   create_tensorboard_logger (bool): Whether to create a tensorboard logger and attach it
to the pytorch lightning trainer. Defaults to True.

    *   summary_writer_kwargs (dict): A dictionary of kwargs that can be passed to lightning’s
TensorboardLogger class. Note that log_dir is passed by exp_manager and cannot exist in this dict. Defaults to None.

    *   create_wandb_logger (bool): Whether to create a Weights and Baises logger and attach it
to the pytorch lightning trainer. Defaults to False.

    *   wandb_logger_kwargs (dict): A dictionary of kwargs that can be passed to lightning’s
WandBLogger class. Note that name and project are required parameters if create_wandb_logger is True. Defaults to None.

    *   create_mlflow_logger (bool): Whether to create an MLFlow logger and attach it to the
pytorch lightning training. Defaults to False

    *   mlflow_logger_kwargs (dict): optional parameters for the MLFlow logger

    *   create_dllogger_logger (bool): Whether to create an DLLogger logger and attach it to the
pytorch lightning training. Defaults to False

    *   dllogger_logger_kwargs (dict): optional parameters for the DLLogger logger

    *   create_clearml_logger (bool): Whether to create an ClearML logger and attach it to the
pytorch lightning training. Defaults to False

    *   clearml_logger_kwargs (dict): optional parameters for the ClearML logger

    *   create_checkpoint_callback (bool): Whether to create a ModelCheckpoint callback and
attach it to the pytorch lightning trainer. The ModelCheckpoint saves the top 3 models with the best “val_loss”, the most recent checkpoint under `*last.ckpt`, and the final checkpoint after training completes under `*end.ckpt`. Defaults to True.

    *   create_early_stopping_callback (bool): Flag to decide if early stopping should be used
to stop training. Default is False. See EarlyStoppingParams dataclass above.

    *   create_preemption_callback (bool): Flag to decide whether to enable preemption callback
to save checkpoints and exit training immediately upon preemption. Default is True.

    *   create_straggler_detection_callback (bool): Use straggler detection callback.
Default is False.

    *   create_fault_tolerance_callback (bool): Use fault tolerance callback. Default is False.

    *   files_to_copy (list): A list of files to copy to the experiment logging directory.
Defaults to None which copies no files.

    *   log_local_rank_0_only (bool): Whether to only create log files for local rank 0.
Defaults to False. Set this to True if you are using DDP with many GPUs and do not want many log files in your exp dir.

    *   log_global_rank_0_only (bool): Whether to only create log files for global rank 0.
Defaults to False. Set this to True if you are using DDP with many GPUs and do not want many log files in your exp dir.

    *   max_time (str): The maximum wall clock time _per run_. This is intended to be used on
clusters where you want a checkpoint to be saved after this specified time and be able to resume from that checkpoint. Defaults to None.

    *   seconds_to_sleep (float): seconds to sleep non rank 0 processes for. Used to give
enough time for rank 0 to initialize

    *   train_time_interval (timedelta): pass an object of timedelta to save the model every
timedelta. Defaults to None. (use _target_ with hydra to achieve this)

Returns:The final logging directory where logging files are saved. Usually the concatenation of
exp_dir, name, and version.

Return type:
log_dir (Path)

_class_ nemo.utils.exp_manager.ExpManagerConfig(_explicit\_log\_dir:str|None=None_,_exp\_dir:str|None=None_,_name:str|None=None_,_version:str|None=None_,_use\_datetime\_version:bool|None=True_,_resume\_if\_exists:bool|None=False_,_resume\_past\_end:bool|None=False_,_resume\_ignore\_no\_checkpoint:bool|None=False_,_resume\_from\_checkpoint:str|None=None_,_create\_tensorboard\_logger:bool|None=True_,_summary\_writer\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_wandb\_logger:bool|None=False_,_wandb\_logger\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_mlflow\_logger:bool|None=False_,_mlflow\_logger\_kwargs:~nemo.utils.loggers.mlflow\_logger.MLFlowParams|None=<factory>_,_create\_dllogger\_logger:bool|None=False_,_dllogger\_logger\_kwargs:~nemo.utils.loggers.dllogger.DLLoggerParams|None=<factory>_,_create\_clearml\_logger:bool|None=False_,_clearml\_logger\_kwargs:~nemo.utils.loggers.clearml\_logger.ClearMLParams|None=<factory>_,_create\_neptune\_logger:bool|None=False_,_neptune\_logger\_kwargs:~typing.Dict[~typing.Any_,_~typing.Any]|None=None_,_create\_checkpoint\_callback:bool|None=True_,_checkpoint\_callback\_params:~nemo.utils.exp\_manager.CallbackParams|None=<factory>_,_create\_early\_stopping\_callback:bool|None=False_,_early\_stopping\_callback\_params:~nemo.utils.exp\_manager.EarlyStoppingParams|None=<factory>_,_create\_preemption\_callback:bool|None=True_,_files\_to\_copy:~typing.List[str]|None=None_,_log\_step\_timing:bool|None=True_,_log\_delta\_step\_timing:bool|None=False_,_step\_timing\_kwargs:~nemo.utils.exp\_manager.StepTimingParams|None=<factory>_,_log\_local\_rank\_0\_only:bool|None=False_,_log\_global\_rank\_0\_only:bool|None=False_,_disable\_validation\_on\_resume:bool|None=True_,_ema:~nemo.utils.exp\_manager.EMAParams|None=<factory>_,_max\_time\_per\_run:str|None=None_,_seconds\_to\_sleep:float=5_,_create\_straggler\_detection\_callback:bool|None=False_,_straggler\_detection\_params:~nemo.utils.exp\_manager.StragglerDetectionParams|None=<factory>_,_create\_fault\_tolerance\_callback:bool|None=False_,_fault\_tolerance:~nemo.utils.exp\_manager.FaultToleranceParams|None=<factory>_,_log\_tflops\_per\_sec\_per\_gpu:bool|None=True_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.utils.exp_manager.ExpManagerConfig "Link to this definition")
Bases: `object`

Experiment Manager config for validation of passed arguments.

Exportable[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#exportable "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

_class_ nemo.core.classes.exportable.Exportable[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable "Link to this definition")
Bases: `ABC`

This Interface should be implemented by particular classes derived from nemo.core.NeuralModule or nemo.core.ModelPT. It gives these entities ability to be exported for deployment to formats such as ONNX.

Usage:
# exporting pre-trained model to ONNX file for deployment. model.eval() model.to(‘cuda’) # or to(‘cpu’) if you don’t have GPU

model.export(‘mymodel.onnx’, [options]) # all arguments apart from output are optional.

export(_output:str_,_input\_example=None_,_verbose=False_,_do\_constant\_folding=True_,_onnx\_opset\_version=None_,_check\_trace:bool|List[torch.Tensor]=False_,_dynamic\_axes=None_,_check\_tolerance=0.01_,_export\_modules\_as\_functions=False_,_keep\_initializers\_as\_inputs=None_,_use\_dynamo=False_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.export "Link to this definition")
Exports the model to the specified format. The format is inferred from the file extension of the output file.

Parameters:
*   **output** (_str_) – Output file name. File extension be .onnx, .pt, or .ts, and is used to select export path of the model.

*   **input_example** (_list_ _or_ _dict_) – Example input to the model’s forward function. This is used to trace the model and export it to ONNX/TorchScript. If the model takes multiple inputs, then input_example should be a list of input examples. If the model takes named inputs, then input_example should be a dictionary of input examples.

*   **verbose** (_bool_) – If True, will print out a detailed description of the model’s export steps, along with the internal trace logs of the export process.

*   **do_constant_folding** (_bool_) – If True, will execute constant folding optimization on the model’s graph before exporting. This is ONNX specific.

*   **onnx_opset_version** (_int_) – The ONNX opset version to export the model to. If None, will use a reasonable default version.

*   **check_trace** (_bool_) – If True, will verify that the model’s output matches the output of the traced model, upto some tolerance.

*   **dynamic_axes** (_dict_) – A dictionary mapping input and output names to their dynamic axes. This is used to specify the dynamic axes of the model’s inputs and outputs. If the model takes multiple inputs, then dynamic_axes should be a list of dictionaries. If the model takes named inputs, then dynamic_axes should be a dictionary of dictionaries. If None, will use the dynamic axes of the input_example derived from the NeuralType of the input and output of the model.

*   **check_tolerance** (_float_) – The tolerance to use when checking the model’s output against the traced model’s output. This is only used if check_trace is True. Note the high tolerance is used because the traced model is not guaranteed to be 100% accurate.

*   **export_modules_as_functions** (_bool_) – If True, will export the model’s submodules as functions. This is ONNX specific.

*   **keep_initializers_as_inputs** (_bool_) – If True, will keep the model’s initializers as inputs in the onnx graph. This is ONNX specific.

*   **use_dynamo** (_bool_) – If True, use onnx.dynamo_export() instead of onnx.export(). This is ONNX specific.

Returns:
A tuple of two outputs. Item 0 in the output is a list of outputs, the outputs of each subnet exported. Item 1 in the output is a list of string descriptions. The description of each subnet exported can be used for logging purposes.

_property_ disabled_deployment_input_names _:List[str]_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.disabled_deployment_input_names "Link to this definition")
Implement this method to return a set of input names disabled for export

_property_ disabled_deployment_output_names _:List[str]_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.disabled_deployment_output_names "Link to this definition")
Implement this method to return a set of output names disabled for export

_property_ supported_export_formats _:List[ExportFormat]_[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.supported_export_formats "Link to this definition")
Implement this method to return a set of export formats supported. Default is all types.

get_export_subnet(_subnet=None_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.get_export_subnet "Link to this definition")
Returns Exportable subnet model/module to export

list_export_subnets()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.list_export_subnets "Link to this definition")
Returns default set of subnet names exported for this model First goes the one receiving input (input_example)

get_export_config()[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.get_export_config "Link to this definition")
Returns export_config dictionary

set_export_config(_args_)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.set_export_config "Link to this definition")
Sets/updates export_config dictionary

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.exportable.Exportable.set_export_config)
- [SaveRestoreConnector](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector)
- [https://pytorch.org/docs/stable/optim.html](https://pytorch.org/docs/stable/optim.html)
- [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-start](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-start)
- [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-start](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-start)
- [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-batch-end)
- [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-train-end)
- [https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#on-test-end)
- [NeuralType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.NeuralType)
- [nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to()](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.connectors.save_restore_connector.SaveRestoreConnector.save_to)
- [TypeState](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.common.typecheck.TypeState)
- [ElementType](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.elements.ElementType)
- [NeuralTypeComparisonResult](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.neural_types.comparison.NeuralTypeComparisonResult)
