from os.path import join, dirname, realpath, isfile
from PIL import Image
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty
from nio.metadata.properties import VersionProperty
from nio.util.environment import NIOEnvironment


@Discoverable(DiscoverableType.block)
class SSD1306(Block):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')
    file = ExpressionProperty(title='Image File', default='niologo.png')

    def __init__(self):
        super().__init__()
        self._display = None

    def configure(self, context):
        super().configure(context)
        self._display = Adafruit_SSD1306.SSD1306_64_48(
            rst=48, dc=36, spi=SPI.SpiDev(5, 1, max_speed_hz=10000000))

    def start(self):
        super().start()
        # Initialize library.
        self._display.begin()
        # Clear display.
        self._display.clear()
        self._display.display()

    def stop(self):
        # Clear display.
        self._display.clear()
        self._display.display()
        super().stop()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            self._display_image(signal)
        self.notify_signals(signals, output_id='default')

    def _display_image(self, signal):
        image = self._load_image_file(signal)
        # Display image.
        self._display.image(image)
        self._display.display()

    def _load_image_file(self, signal):
        """ Loads an image file from disk """

        # Let's figure out where the file is
        try:
            fileprop = self.file(signal)
        except:
            self._logger.exception('Failed to get file name info from signal')
            return None
        filename = self._get_valid_file(
            # First, just see if it's maybe already a file?
            fileprop,
            # Next, try in the NIO environment
            NIOEnvironment.get_path(fileprop),
            # Finally, try relative to the current file
            join(dirname(realpath(__file__)), fileprop),
        )
        if filename is None:
            self._logger.error(
                'Could not find image file {0}. Should be an absolute path or'
                ' relative to the current environment.'.format(
                    fileprop))
            return None
        image = Image.open(filename).resize((self._display.width, self._display.height), Image.ANTIALIAS).convert('1')
        return image

    def _get_valid_file(self, *args):
        """ Go through args and return the first valid file, None if none are.
        """
        for arg in args:
            if isfile(arg):
                return arg
        return None
