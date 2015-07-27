SSD1306
=======

Blocks for writing to an SSD1306 OLED screen on Intel Edison

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

SSD1306ImageFile
================

Block for writing to an SSD1306 OLED screen on Intel Edison

Loads an image file from disk and then displays it to the screen.

Properties
----------
-   **file** (exp): Image file on disk. First checks absolute path, then relative to the nio project directory, then relative to the block code file.

Dependencies
------------
Note: Both of these need to be neutralio version of the repos. The official Adafruit ones do not work with the Sparkfun Edision oled.
-   [**Adafruit_GPIO**](https://github.com/neutralio/Adafruit_Python_GPIO)
-   [**Adafruit_SSD1306**](https://github.com/neutralio/Adafruit_Python_SSD1306)

Commands
--------
None

Input
-----
Any list of signals.

Output
------
Same list of signals as input.

------------------------------------------------------------------------------

SSD1306PILImage
===============

Block for writing to an SSD1306 OLED screen on Intel Edison

Displays a PIL Image file from an input signal to the screen.

Properties
----------
-   **image** (exp): Expression property needs to evaluate to a PIL Image object.

Dependencies
------------
Note: Both of these need to be neutralio version of the repos. The official Adafruit ones do not work with the Sparkfun Edision oled.
-   [**Adafruit_GPIO**](https://github.com/neutralio/Adafruit_Python_GPIO)
-   [**Adafruit_SSD1306**](https://github.com/neutralio/Adafruit_Python_SSD1306)

Commands
--------
None

Input
-----
Any list of signals. Default *image* config is to have a PIL Image in the `image` attribute of the Signal.

Output
------
Same list of signals as input.
