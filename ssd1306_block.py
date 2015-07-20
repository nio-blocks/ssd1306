import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import VersionProperty


@Discoverable(DiscoverableType.block)
class SSD1306(Block):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')

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
        self._image = Image.open('/home/nio/ssd1306/niologo.png').resize((self._display.width, self._display.height), Image.ANTIALIAS).convert('1')

    def stop(self):
        # Clear display.
        self._display.clear()
        self._display.display()
        super().stop()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            self._display_image()
        self.notify_signals(signals, output_id='default')

    def _display_image(self):
        # Display image.
        self._display.image(self._image)
        self._display.display()
