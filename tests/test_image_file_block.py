from unittest.mock import MagicMock

from PIL import Image
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..ssd1306_image_file_block import SSD1306ImageFile


class TestSSD1306ImageFile(NIOBlockTestCase):

    def test_get_image(self):
        blk = SSD1306ImageFile()
        blk._display = MagicMock()
        blk._display.width = 64
        blk._display.height = 48
        image = blk._get_image(Signal())
        self.assertEqual(type(image), Image.Image)
        self.assertEqual(image.size, (64, 48))

    def test_file_property(self):
        blk = SSD1306ImageFile()
        # TODO: configure file property to something not default
        blk._display = MagicMock()
        image = blk._get_image(Signal())
        # TODO: make assertions
