# Microphone Volume Enforcer

This script monitors the system microphone volume and enforces a target volume level.

## Setup

1. **Install Python**: Ensure Python 3.7 or later is installed. Download it from [python.org](https://www.python.org/).

2. **Clone or Download the Project**:
   - Download the project files or clone the repository.

3. **Set Up the Virtual Environment**:
   - Open a terminal in the project directory.
   - Run the following commands:
     ```bash
     python -m venv venv
     call venv\Scripts\activate
     pip install -r requirements.txt
     ```

4. **Run the Script**:
   - Use the provided batch file to run the script:
     ```bash
     run_script.bat
     ```

## Configuration
- To change the target microphone volume, edit the `TARGET_VOLUME` constant in `microphone_system_volume_detection.py`.

## Notes
- The script requires Windows and administrative privileges to modify the microphone volume.