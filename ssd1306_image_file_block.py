from PIL import Image

from nio.properties import VersionProperty, FileProperty

from .ssd1306_base import SSD1306Base


class SSD1306ImageFile(SSD1306Base):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')
    file = FileProperty(title='Image File', default='niologo.png')

    def _get_image(self, signal):
        """ Loads an image file from disk
        """
        # Let's figure out where the file is
        try:
            fileprop = self.file(signal)
        except:
            self.logger.exception('Failed to get file name info from signal')
            return None

        if self.file().file is None:
            self.logger.error(
                'Could not find image file {0}. Should be an absolute path or'
                ' relative to the current environment.'.format(
                    fileprop.file))
            return None
        image = Image.open(self.file().file)
        image = image.resize((self._display.width, self._display.height),
                             Image.ANTIALIAS)
        image = image.convert('1')
        return image
