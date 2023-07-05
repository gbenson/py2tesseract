# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# flake8: noqa: F401
from .pytesseract import ALTONotSupported
from .pytesseract import get_languages
from .pytesseract import get_tesseract_version
from .pytesseract import image_to_alto_xml
from .pytesseract import image_to_boxes
from .pytesseract import image_to_data
from .pytesseract import image_to_osd
from .pytesseract import image_to_pdf_or_hocr
from .pytesseract import image_to_string
from .pytesseract import Output
from .pytesseract import run_and_get_output
from .pytesseract import TesseractError
from .pytesseract import TesseractNotFoundError
from .pytesseract import TSVNotSupported


__version__ = '0.3.10'
