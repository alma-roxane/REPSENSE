import gradio as gr
import numpy as np
import cv2
from core.pose_engine import PoseEngine
from core.angle_calculator import AngleCalculator
from core.form_analyzer import ANALYZERS

pose_engine = PoseEngine()
angle_calculator = AngleCalculator()
def process(frame):
    keypoints = pose_engine.process(frame)
    angles = angle_calculator.calculate(keypoints)
    feedback = ANALYZERS["plank"].analyse(angles)
    for i, fb in enumerate(feedback):
        cv2.putText(frame, fb.message, (50, 50 + i * 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return  frame

demo = gr.Interface(
    fn=process,
    inputs = gr.Image(sources=["webcam"], streaming=True),
    outputs = gr.Image()
)

demo.launch()