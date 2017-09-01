from nio.properties import Property
from nio.properties import VersionProperty

from .ssd1306_base import SSD1306Base


class SSD1306PILImage(SSD1306Base):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty("0.1.0")
    image = Property(title='PIL Image', default='{{ $image }}')

    def _get_image(self, signal):
        try:
            image = self.image(signal)
            self.logger.debug('Type of image: {}'.format(type(image)))
            return image
        except:
            self.logger.exception('Failed to evaluate PIL Image')
            return None
