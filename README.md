RepSense is a real-time AI fitness coach that uses 
pose estimation to detect exercise form and provide 
instant feedback. Built for fitness enthusiasts and 
beginners who want to learn correct form for bicep 
curls, squats, and pushups without a personal trainer.

## Tech Stack

- Pose Estimation: YOLOv8-Pose (Ultralytics)
- Tracking:        ByteTrack
- Backend:         FastAPI
- Frontend:        Gradio
- Deployment:      Hugging Face Spaces
- Experiment Tracking: Weights & Biases (W&B)

## Project Structure

repsense/
├── core/
│   ├── pose_engine.py        # YOLOv8-Pose wrapper + ByteTrack
│   ├── angle_calculator.py   # Joint angle calculation engine
│   ├── rep_counter.py        # Exercise rep counting state machine
│   └── form_analyzer.py      # Form grading and feedback
├── api/                      # FastAPI backend
├── frontend/                 # Gradio UI
├── database/                 # Session logging
├── experiments/              # W&B experiment tracking
├── assets/                   # Demo images and videos
└── README.md

## How to Run

### 1. Clone the repository
git clone https://github.com/YOURUSERNAME/repsense.git
cd repsense

### 2. Create virtual environment
python3 -m venv repsense_env
source repsense_env/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run the app
python frontend/app.py

## Research Papers Referenced

1. DeepPose — Toshev & Szegedy, 2014
   arxiv.org/abs/1312.4659

2. OpenPose — Cao et al., 2018
   arxiv.org/pdf/1812.08008

3. YOLOv8-Pose — Ultralytics, 2023
   docs.ultralytics.com/tasks/pose

4. ByteTrack — Zhang et al., 2022
   arxiv.org/abs/2110.06864

5. Deep Learning Pose Estimation for 
   Physical Movement Feedback — PMC, 2024
   pmc.ncbi.nlm.nih.gov/articles/PMC11401083