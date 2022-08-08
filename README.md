## requirement
torch==1.2.0

## trainning process


1. Preparation of dataset   
**put dataset in the root directory**  

2. Data set processing   
Modify the annotation_mode=2 in voc_annotation.py, and run voc_annotation.py to generate 2007_train.txt and 2007_val.txt in the root directory.   

3. Start network training   
The default parameters of train.py are used to train the VOC dataset, run train.py directly to start training.   

4. Predict the training results   
To predict the training results, we need to use two files, yolo.py and predict.py. We first need to modify model_path and classes_path in yolo.py, these two parameters must be modified.   
**model_path points to the trained weights file, which is in the logs folder.   
classes_path points to the txt corresponding to the detected classes.**   
After finishing the modification, you can run predict.py for detection. After running, enter the image path to detect.

Translated with www.DeepL.com/Translator (free version)


## Prediction steps
 # b. Use your own trained weights
1. Follow the training steps to train.  
2. Inside the yolo.py file, modify model_path and classes_path in the following section to make them correspond to the trained files; **model_path corresponds to the weights file under the logs folder, and classes_path is the class that corresponds to the division of model_path**.  
```python
_defaults = {
    # --------------------------------------------------------------------------#
    # Use your own trained model for prediction make sure to modify model_path and classes_path!
    # model_path points to the weights file in the logs folder, classes_path points to the txt under model_data
    # If there is a shape mismatch, also pay attention to the modification of model_path and classes_path parameters during training
    # --------------------------------------------------------------------------#
    "model_path" : 'model_data/yolo_weights.pth',
    "classes_path" : 'model_data/coco_classes.txt',
    # ---------------------------------------------------------------------#
    # anchors_path represents the txt file corresponding to the a priori box, which is generally not modified.
    # anchors_mask is used to help the code find the corresponding a priori box, generally not modified.
    # ---------------------------------------------------------------------#
    "anchors_path" : 'model_data/yolo_anchors.txt',
    "anchors_mask" : [[6, 7, 8], [3, 4, 5], [0, 1, 2]],
    # ---------------------------------------------------------------------#
    # The size of the input image, which must be a multiple of 32.
    # ---------------------------------------------------------------------#
    "input_shape" : [416, 416],
    #---------------------------------------------------------------------#
    # Only prediction boxes with scores greater than the confidence level will be kept
    #---------------------------------------------------------------------#
    "confidence" : 0.5,
    #---------------------------------------------------------------------#
    # The size of nms_iou used for non-extreme suppression
    # ---------------------------------------------------------------------#
    "nms_iou" : 0.3,
    # ---------------------------------------------------------------------#
    # This variable is used to control whether or not to use letterbox_image to resize the input image without distortion.
    # After several tests, it was found that turning off letterbox_image and resizing directly worked better
    # ---------------------------------------------------------------------#
    "letterbox_image" : False,
    # -------------------------------#
    # Whether to use Cuda or not
    # No GPU can be set to False
    #-------------------------------#
    "cuda" : True,

Translated with www.DeepL.com/Translator (free version)
}
```
3. Run predict.py and type  
```python
img/street.jpg
```
4. Set up inside predict.py to do fps testing and video video detection.  
