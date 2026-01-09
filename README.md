# Free AI Image Generator

A powerful and free Python-based image generator that uses **Stable Diffusion XL** (via Hugging Face) and **Pollinations.ai**.

## Features

- **Free & Easy**: No subscription required.
- **Two Modes**:
    - **Pollinations.ai**: Completely free, no API key needed.
    - **Hugging Face**: High-quality generation using SDXL (requires free token).
- **Web Interface**: Beautiful GUI powered by Gradio.
- **Command Line**: Quick generation scripts.

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Web Interface (Recommended)
Launch the full featured web UI:
```bash
python app.py
```
Open the link shown in your terminal (usually `http://127.0.0.1:7860`).

### 2. Quick Command Line (Pollinations Only)
Generate images instantly without any menus:
```bash
python easy_generate.py
```

### 3. Advanced Command Line
Choose between providers and configure settings:
```bash
python generate_image.py
```

## Requirements
- Python 3.x
- `requests`
- `pillow`
- `gradio`
