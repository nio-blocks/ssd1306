from os.path import join, dirname, realpath, isfile
from PIL import Image
from nio.common.discovery import Discoverable, DiscoverableType
from nio.metadata.properties import ExpressionProperty
from nio.metadata.properties import VersionProperty
from nio.util.environment import NIOEnvironment
from .ssd1306_base import SSD1306Base


@Discoverable(DiscoverableType.block)
class SSD1306ImageFile(SSD1306Base):

    """ Block for writing to an SSD1306 OLED screen on Intel Edison """

    version = VersionProperty('0.1.0')
    file = ExpressionProperty(title='Image File', default='niologo.png')

    def _get_image(self, signal):
        """ Loads an image file from disk
        """
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
        image = Image.open(filename)
        image = image.resize((self._display.width, self._display.height), 
                             Image.ANTIALIAS)
        image = image.convert('1')
        return image

    def _get_valid_file(self, *args):
        """ Go through args and return the first valid file, None if none are.
        """
        for arg in args:
            if isfile(arg):
                return arg
        return None
