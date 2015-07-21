from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty
from nio.metadata.properties import VersionProperty
from .ssd1306_base import SSD1306Base


@Discoverable(DiscoverableType.block)
class SSD1306PILImage(SSD1306Base):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')
    image = ExpressionProperty(title='PIL Image', default='{{ $image }}')

    def _get_image(self, signal):
        try:
            image = self.image(signal)
            self._logger.debug('Type of image: {}'.format(type(image)))
            return image
        except:
            self._logger.exception('Failed to evaluate PIL Image')
            return None
