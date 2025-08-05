
from importlib import import_module

# carrega submódulo e o deixa visível como atributo do pacote
parser = import_module(".ocr_pdf", package=__name__)

__all__ = ["ocr_pdf"]  
__version__ = "0.1.0"
__author__  = "Dimmy Magalhães"