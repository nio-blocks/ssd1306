from unittest.mock import MagicMock, patch

from PIL import Image
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..ssd1306_pil_image_block import SSD1306PILImage


class TestSSD1306PILImage(NIOBlockTestCase):

    def test_get_image(self):
        blk = SSD1306PILImage()
        with patch('Adafruit_SSD1306.SSD1306_64_48'), \
                patch('Adafruit_GPIO.SPI.SpiDev'):
            self.configure_block(blk, {})
        image = blk._get_image(
            Signal({'image': Image.new(mode='RGB', size=(64, 48))}))
        self.assertEqual(type(image), Image.Image)

    def test_image_property(self):
        blk = SSD1306PILImage()
        # TODO: configure image property to something not default
        blk._display = MagicMock()
        image = blk._get_image(Signal())
        # TODO: make assertions
