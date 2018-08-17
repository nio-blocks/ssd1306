SSD1306ImageFile
================
Blocks for writing an image file to an SSD1306 OLED screen on Intel Edison. Loads an image file from disk and then displays it to the screen.

Properties
----------
- **file**: Image file on disk. First checks absolute path, then relative to the nio project directory, then relative to the block code file.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals as input.

Commands
--------
None

Dependencies
------------
Note: Both Adafruit repos need to be neutralio version of the repos. The official Adafruit ones do not work with the Sparkfun Edison oled. Depending on platform, Pillow may require additional prerequisites (libjpeg, zlib, etc)be installed, see the full instructions [**here**](https://pillow.readthedocs.io/en/latest/installation.html).
-   [**Adafruit_GPIO**](https://github.com/neutralio/Adafruit_Python_GPIO)
-   [**Adafruit_SSD1306**](https://github.com/neutralio/Adafruit_Python_SSD1306)
-   Pillow

SSD1306PILImage
===============
Blocks for writing a PIL image to an SSD1306 OLED screen on Intel Edison. Displays a PIL Image file from an input signal to the screen.

Properties
----------
- **image**: Expression property needs to evaluate to a PIL Image object.

Inputs
------
- **default**: Any list of signals. Default *image* config is to have a PIL Image in the `image` attribute of the Signal.

Outputs
-------
- **default**: Same list of signals as input.

Commands
--------
None

Dependencies
------------
Note: Both Adafruit repos need to be neutralio version of the repos. The official Adafruit ones do not work with the Sparkfun Edison oled. Depending on platform, Pillow may require additional prerequisites (libjpeg, zlib, etc)be installed, see the full instructions [**here**](https://pillow.readthedocs.io/en/latest/installation.html).
-   [**Adafruit_GPIO**](https://github.com/neutralio/Adafruit_Python_GPIO)
-   [**Adafruit_SSD1306**](https://github.com/neutralio/Adafruit_Python_SSD1306)
-   Pillow



Pin->Button Table
-----------------
The [SparkFun Block for Intel Edison](https://www.sparkfun.com/products/13035) has built in push buttons that are wired up to the GPIO:

| Button | Edison GPIO Pin | Mraa Pin # |
| ------ | --------------- | ---------- |
| Up     | 47              | 46         |
| Down   | 44              | 31         |
| Left   | 165             | 15         |
| Right  | 45              | 45         |
| Select | 48              | 33         |
| A      | 49              | 47         |
| B      | 46              | 32         |
