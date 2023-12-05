import pyscreenshot

# Capture the entire screen and display the screenshot
screenshot = pyscreenshot.grab()
screenshot.save("File 001.jpg")
screenshot.show()

# Capture a specific region and save it to a file
region_screenshot = pyscreenshot.grab(bbox=(100, 100, 500, 500))
region_screenshot.save("region_screenshot.png")
region_screenshot.show()

