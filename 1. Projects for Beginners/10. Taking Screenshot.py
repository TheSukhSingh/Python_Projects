import pyscreenshot as ps 

# Captures complete screen image
image = ps.grab()

# Opens the image
image.show()

# Saves the screenshot
image.save("Imagename.png")