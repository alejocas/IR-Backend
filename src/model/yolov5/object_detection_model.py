import yolov5


def save_results_to(results, dir_path: str, file_name: str):
    try:
        results.save(save_dir=dir_path, filename=file_name)
        return True
    except Exception as e:
        return False


class ObjectDetectionModel:
    def __init__(self, confidence_thresold=0.4, iou_thresold=0.5):
        self.model = yolov5.load('src/model/yolov5/CustomYoloNetV1.pt')

        # set model parameters
        self.model.conf = confidence_thresold  # NMS confidence threshold
        self.model.iou = iou_thresold  # NMS IoU threshold
        self.model.agnostic = False  # NMS class-agnostic
        self.model.multi_label = False  # NMS multiple labels per box
        self.model.max_det = 1000  # maximum number of detections per image

    def predict(self, img_path: str):
        results = self.model(img_path, size=416)
        return results
