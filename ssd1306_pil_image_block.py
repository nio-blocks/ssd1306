import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty
from nio.metadata.properties import VersionProperty
from nio.modules.threading import Lock


@Discoverable(DiscoverableType.block)
class SSD1306PILImage(Block):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')
    image = ExpressionProperty(title='PIL Image', default='{{ $image }}')

    def __init__(self):
        super().__init__()
        self._display = None
        self._lock = Lock()

    def configure(self, context):
        super().configure(context)
        self._display = Adafruit_SSD1306.SSD1306_64_48(
            rst=48, dc=36, spi=SPI.SpiDev(5, 1, max_speed_hz=10000000))

    def start(self):
        super().start()
        with self._lock:
            self._display.begin()
            self._display.clear()
            self._display.display()

    def stop(self):
        with self._lock:
            self._display.clear()
            self._display.display()
        super().stop()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            image = self._get_image(signal)
            if image:
                self._display_image(image)
        self.notify_signals(signals, output_id='default')

    def _get_image(self, signal):
        try:
            image = self.image(signal)
            self._logger.debug('Type of image: {}'.format(type(image)))
            return image
        except:
            self._logger.exception('Failed to evaluate PIL Image')
            return None

    def _display_image(self, image):
        try:
            with self._lock:
                self._display.image(image)
                self._display.display()
        except:
            self._logger.exception('Failed to display PIL Image')
