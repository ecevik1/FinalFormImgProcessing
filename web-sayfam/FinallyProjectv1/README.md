# FinallyProjectv1

This project is a Flask web application that utilizes the YOLO (You Only Look Once) model for real-time video processing. The application is designed to monitor the occupancy status of tables in a library setting based on a video feed.

## Project Structure

```
FinallyProjectv1
├── app.py                  # Main application file
├── library
│   └── video11.mp4        # Video file for processing
├── templates
│   └── index.html         # Main HTML template
├── static
│   ├── css
│   │   └── style.css      # CSS styles for the web application
│   ├── js
│   │   └── script.js      # JavaScript code for client-side functionality
│   └── images
│       └── placeholder.jpg # Placeholder image
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd FinallyProjectv1
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the necessary video file (`video11.mp4`) in the `library` directory.
2. Run the application:
   ```
   python app.py
   ```
3. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Features

- Real-time monitoring of table occupancy using video processing.
- User-friendly interface to display the status of tables.
- Integration of YOLO model for object detection.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.