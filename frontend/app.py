import gradio as gr
import numpy as np
import cv2
from core.pose_engine import PoseEngine
from core.angle_calculator import AngleCalculator
from core.form_analyzer import ANALYZERS

# COCO skeleton joint pairs for drawing limb connections
SKELETON = [
    [15, 13], [13, 11], [16, 14], [14, 12], [11, 12], [5, 11],
    [6, 12], [5, 6], [5, 7], [6, 8], [7, 9], [8, 10],
    [1, 2], [0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]
]

pose_engine = PoseEngine()
angle_calculator = AngleCalculator()

def process(frame):
    # Run YOLOv8 + ByteTrack detection
    results = pose_engine.detect(frame)
    # Extract keypoints for each tracked person
    people  = pose_engine.get_keypoints(results)
    # Skip frame if no one detected
    if not people:
        return frame
    keypoints = people[0]['keypoints']
    # Draw skeleton lines between joint pairs
    for pair in SKELETON:
        # Skip low-confidence joints
        if keypoints[pair[0]][2] < 0.5 or keypoints[pair[1]][2] < 0.5:
            continue
        pt1 = (int(keypoints[pair[0]][0]), int(keypoints[pair[0]][1]))
        pt2 = (int(keypoints[pair[1]][0]), int(keypoints[pair[1]][1]))
        cv2.line(frame, pt1, pt2, (0, 255, 0), 2)
    # Draw keypoint dots on each joint
    for kp in keypoints:
        if kp[2] < 0.5:
            continue
        center = (int(kp[0]), int(kp[1]))
        cv2.circle(frame, center, 4, (0, 255, 255), -1)
    # Calculate joint angles and analyze form
    angles = angle_calculator.calculate(people[0]['keypoints'])
    feedback = ANALYZERS["plank"].analyse(angles)
    # Overlay feedback messages on frame
    for i, fb in enumerate(feedback):
        cv2.putText(frame, fb.message, (50, 50 + i * 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

demo = gr.Interface(
    fn=process,
    inputs=gr.Image(sources=["webcam"], streaming=True),
    outputs=gr.Image()
)

demo.launch()