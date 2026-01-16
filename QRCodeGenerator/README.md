# QR Code Generator

This Python script generates a QR code for a specified URL and saves it as a PNG image.

## Prerequisites

Before running the script, you need to have Python and pip installed on your system.

## Installation
Install the required packages using pip:

    ```bash
    pip install qrcode
    ```

    ```bash
    pip install qrcode[pil]
    ```

## Usage

1.  Make sure you are in the `QRCodeGenerator` directory.
2.  Run the script from your terminal:

    ```bash
    python generator.py
    ```

## Output

The script will generate a QR code image file named `biox_qr_code.png` in the project's root directory. When you scan this QR code, it will redirect to `https://www.bioxsystems.com/`.

Here is the generated QR code:

![BioX QR Code](biox_qr_code.png)
