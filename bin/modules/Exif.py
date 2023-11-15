#!/usr/bin/env python3
# -*-coding:UTF-8 -*
"""
The Exif Module
======================

"""

##################################
# Import External packages
##################################
import os
import sys

from PIL import Image, ExifTags

sys.path.append(os.environ['AIL_BIN'])
##################################
# Import Project packages
##################################
from modules.abstract_module import AbstractModule


class Exif(AbstractModule):
    """
    CveModule for AIL framework
    """

    def __init__(self):
        super(Exif, self).__init__()

        # Waiting time in seconds between to message processed
        self.pending_seconds = 1

        # Send module state to logs
        self.logger.info(f'Module {self.module_name} initialized')

    def compute(self, message):
        image = self.get_obj()
        print(image)
        img = Image.open(image.get_filepath())
        img_exif = img.getexif()
        print(img_exif)
        if img_exif:
            for key, val in img_exif.items():
                if key in ExifTags.TAGS:
                    print(f'{ExifTags.TAGS[key]}:{val}')
                else:
                    print(f'{key}:{val}')
            sys.exit(0)

        # tag = 'infoleak:automatic-detection="cve"'
        # Send to Tags Queue
        # self.add_message_to_queue(message=tag, queue='Tags')


if __name__ == '__main__':

    module = Exif()
    module.run()
