# TrafficSign Capsule for NovaVision

## Requirements

To use this capsule, first, you need to clone the Novavision PyTorch image. The README file in the following repository explains how to use the PyTorch image:

[Novavision PyTorch Image Repository](https://github.com/novavision-ai/image-pytorch)

- PyTorch Image (to be installed in Docker)
- FastApi Service (to be installed with PyTorch Image)
- Python Ultralytics Module
- Docker
- Novavision YoloV5 Capsule
- GitSCM

## Installation

After obtaining the image succesfully, follow these steps:

1. Pull the Novavision SDK files and necessary capsules into the directories, Capsules should be under capsules directory

```
git submodule add "components github address" component
git submodule add "sdk github address" sdk
git submodule add https://github.com/novavision-ai/cap-traffic-sign-recognition.git" TrafficSignRecognition
git submodule add "https://github.com/novavision-ai/cap-yolov5" YoloV5
```

2. Next, go into the YoloV5 capsule directory, create the "lib" folder under the "src" directory, and pull the yolov5 framework using the following command:
```
git submodule add https://github.com/ultralytics/yolov5.git yolov5
```

3. After this step, modify the "executor" information in the "service.py" file inside the image. Change the "Executor" key value to "Traffic" and set the value of the "Traffic" key to "TrafficInferrer":
```
executors = {'Traffic': {"Traffic": TrafficInferrer}}
```

4. Then, before performing inference, open a terminal and install ultralytics library using pip:
```
pip install ultralytics
```

5. In the project directory, open a terminal and navigate to the "apps" directory under the "TrafficSignRecognition" capsule. Use the following command to perform inference:
```
python inference.py
```

The output should be in JSON format, printed on the terminal screen, and the json must include the class of the given input image.

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
