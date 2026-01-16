import qrcode

# Define the target URL for the QR code. When scan the generated QR code, it will redirect to this URL.
target_url = "https://www.bioxsystems.com/"

# Configure QR code parameters
qrObj = qrcode.QRCode(
    version=1,
    # Error correction level
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    # Size of each box in pixels in the QR code grid
    box_size=10,
    # Border size in number of boxes thick (minimum is 4)
    border=4,
)

# Add data to QR code and generate the image
qrObj.add_data(target_url)
# Generate the QR code image
qrObj.make(fit=True)
img = qrObj.make_image(fill_color="black", back_color="white")
# Save the generated QR code image to a file
img.save("biox_qr_code.png")

print("QR code generated and saved as 'biox_qr_code.png'")