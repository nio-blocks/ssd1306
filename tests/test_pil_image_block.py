from PIL import Image
from unittest.mock import MagicMock, patch
from collections import defaultdict
from nio.common.signal.base import Signal
from nio.util.support.block_test_case import NIOBlockTestCase
from ..ssd1306_pil_image_block import SSD1306PILImage


class TestSSD1306PILImage(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    def test_get_image(self):
        blk = SSD1306PILImage()
        with patch('Adafruit_SSD1306.SSD1306_64_48'), \
                patch('Adafruit_GPIO.SPI.SpiDev'):
            self.configure_block(blk, {})
        image = blk._get_image(Signal({'image': Image.Image()}))
        self.assertEqual(type(image), Image.Image)

    def test_image_property(self):
        blk = SSD1306PILImage()
        # TODO: configure image property to something not default
        blk._display = MagicMock()
        image = blk._get_image(Signal())
        # TODO: make assertions
