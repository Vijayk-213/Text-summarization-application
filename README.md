# Text Summarization Application

## Overview

This Text Summarization Application is a web-based tool that allows users to input text and receive a concise summary. It uses Python with Flask for the backend, and HTML/CSS with Tailwind CSS for the frontend. The application features a responsive design with a toggle for light and dark themes.

## Screenshot

![Text Summarization App Screenshot](./image.png)

*Figure 1: Screenshot of the Text Summarization Application showing the main interface with text input area, summary output, and theme toggle.*

## Features

- Text summarization using the `sumy` library
- Adjustable number of sentences for the summary
- Responsive web design
- Light and dark theme toggle
- Input text retention after summarization

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Vijayk-213/Text-summarization-application.git
   cd text-summarization-app
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`

3. Enter the text you want to summarize in the provided text area.

4. Specify the number of sentences you want in the summary.

5. Click the "Summarize" button to generate the summary.

6. Use the theme toggle in the top right corner to switch between light and dark modes.

## Project Structure

```
text-summarization-app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # This file
│
├── templates/
│   └── index.html         # HTML template for the web interface
│
└── images/
    └── app_screenshot.png # Screenshot of the application
```

## Dependencies

- Flask
- sumy
- Tailwind CSS (via CDN)

For a complete list of Python dependencies, see `requirements.txt`.

## Contributing

Contributions to improve the application are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request



## Acknowledgments

- [sumy](https://github.com/miso-belica/sumy) for text summarization
- [Tailwind CSS](https://tailwindcss.com/) for the UI styling
- [Flask](https://flask.palletsprojects.com/) for the web framework