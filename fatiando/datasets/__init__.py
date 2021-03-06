"""
Functions to read data from files and fetch datasets from the internet.
"""
from .surfer import load_surfer
from .utils import check_hash
from .hawaii_gravity import fetch_hawaii_gravity
from .image import from_image, SAMPLE_IMAGE, SAMPLE_IMAGE_SMALL
