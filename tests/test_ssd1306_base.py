from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..ssd1306_base import SSD1306Base


class SSD1306Test(SSD1306Base):

    def _get_image(self, signal):
        return 'image'


class TestSSD1306Base(NIOBlockTestCase):

    def test_notified_signals(self):
        blk = SSD1306Test()
        with patch('Adafruit_SSD1306.SSD1306_64_48'), \
                patch('Adafruit_GPIO.SPI.SpiDev'):
            self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal()])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
                             {})

    def test_display_method_calls(self):
        blk = SSD1306Test()
        with patch('Adafruit_SSD1306.SSD1306_64_48'), \
                patch('Adafruit_GPIO.SPI.SpiDev'):
            self.configure_block(blk, {})
        # start block and assert display methods are called
        blk.start()
        self.assertEqual(1, blk._display.begin.call_count)
        self.assertEqual(1, blk._display.clear.call_count)
        self.assertEqual(1, blk._display.display.call_count)
        # process a signal and assert display methods are called
        blk.process_signals([Signal()])
        self.assertEqual(1, blk._display.image.call_count)
        blk._display.image.assert_called_with('image')
        self.assertEqual(2, blk._display.display.call_count)
        # stop block and assert display methods are called
        blk.stop()
        self.assertEqual(2, blk._display.clear.call_count)
        self.assertEqual(3, blk._display.display.call_count)

    def test_process_multiple_signals(self):
        blk = SSD1306Test()
        with patch('Adafruit_SSD1306.SSD1306_64_48'), \
                patch('Adafruit_GPIO.SPI.SpiDev'):
            self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal(), Signal()])
        self.assertEqual(2, blk._display.image.call_count)
        blk._display.image.assert_called_with('image')
        self.assertEqual(3, blk._display.display.call_count)
        blk.stop()
