from ultralytics import YOLO
import numpy as np
import cv2

class PoseEngine:
    def __init__(self, model_size='m'):
        self.model = YOLO(f'yolov8{model_size}-pose.pt')
        self.model_size = model_size

def detect(self, frame, conf=0.5):
    results = self.model.track(
        frame,
        persist=True,
        conf=conf,
        tracker='bytetrack.yaml'
    )
    return results

def draw(self, frame, results):
    annotated = results[0].plot()
    return annotated

def get_keypoints(self, results):
        """
        Extract keypoints from results.
        Returns list of dicts, one per person.
        Each dict has:
            - id: person tracking ID
            - keypoints: array of shape (17, 3)
                         columns = [x, y, confidence]
            - bbox: [x1, y1, x2, y2]
        """
        people = []

 # No detections
        if results[0].boxes is None:
            return people

        boxes   = results[0].boxes
        kpts    = results[0].keypoints

        for i in range(len(boxes)):
            # Tracking ID — None if ByteTrack
            # hasn't assigned one yet
            track_id = int(boxes.id[i]) \
                if boxes.id is not None else i

            # Keypoints array (17, 3)
            keypoints = kpts.data[i].cpu().numpy()

            # Bounding box
            bbox = boxes.xyxy[i].cpu().numpy()

            people.append({
                'id':        track_id,
                'keypoints': keypoints,
                'bbox':      bbox
            })

        return people