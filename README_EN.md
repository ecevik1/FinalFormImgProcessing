# Library Object Detection System

## Description
This project implements a real-time object detection system using YOLOv8 to detect and track people, books, tables, and chairs in video footage. The system draws colored rectangles around detected objects and displays a person counter.

## Features
- Real-time object detection
- Detection of multiple object classes:
  - People (Green rectangle)
  - Books (Blue rectangle)
  - Tables (Red rectangle)
  - Chairs (Turquoise rectangle)
- Person counter in bottom right corner
- Live video processing

## Requirements
- Python 3.8 or higher
- See requirements.txt for required packages

## Installation
1. Clone the repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Update the video path in the script
2. Run the script:
```bash
python "Proje Bitirme.py"
```
3. Press 'q' to exit the program

## Notes
- Make sure you have sufficient GPU/CPU resources for real-time processing
- The YOLO model file (yolov8n.pt) will be downloaded automatically on first run 