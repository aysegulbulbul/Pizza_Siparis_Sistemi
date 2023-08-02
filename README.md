## Directory Structure
```
apps
   |-- inference.py
notebooks
   |-- YoloModel.ipynb
setup.py
src
   |-- init.py
   |-- classes
   |   |-- base_class.py
   |-- configs
   |   |-- config.py
   |   |-- data_schema.py
   |   |-- logging_config.yaml
   |-- dataloaders
   |   |-- dataloader.py
   |-- executors
   |   |-- trafficsign.py
   |-- models
   |   |-- PackageModel.py
   |-- utils
   |   |-- config.py
   |   |-- logger.py
   |   |-- plot_image.py
   |-- weights
   |   |-- TrafficSignRecognition.pt
```

## Functionality of the Used Files in the Capsule:

* Apps:
  * inference.py: Used to create a JSON request using classes defined in PackageModel.
* Notebooks:
  * YoloModel.ipynb: Contains python code for local model training.
* Resources: The directory for input images used while creating a request within the inference file.
* src:
  * Configs:
    * config.py: Contains config files that includes options to make changes on inputs.
  * Executors:
    * trafficsign.py: Used to create a JSON response using classes defined in PackageModel. It processes the incoming request and connects with the YOLO capsule, capturing Yolo Capsule's output.
  * Models:
    * PackageModel.py: Contains class definitions for creating JSON requests and responses using the pydantic module.
  * Weights:
    * Traffic:
      * TrafficSignRecognition.pt: Exported model weight file in a format understandable by YOLOv5. The path of this file is also given to the YOLO capsule for use.

## Capsule Workflow

The YOLOv5 weight file used in the TrafficSign capsule is trained with 12367 images of different sizes.
In the inference, the JSON request is created using packagemodel, with parameters and their values defined (BoundingBox, input image, DNN, ConfigThreshold, etc.). This request is then sent to the trafficsign executor file. The request data is captured by the constructor and processed in the InferYolo function. A new JSON request is manually created with the request data captured by the constructor, and it is sent to the YOLOv5 capsule using the script return Detect(Request(request)).run(). The response from YOLOv5 is then parsed in the run function, formatted using class definitions from packagemodel, and returned as the output of the trafficsign capsule.


## Traffic Signs Capsules File Connections
TrafficSignInference -> TrafficSignExecutor -> YoloV5Executor -> YOLOv5 library -> YoloV5Executor -> TrafficSignExecutor -> TrafficSign Inference


## Contributors
