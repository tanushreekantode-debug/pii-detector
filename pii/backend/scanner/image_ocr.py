import os
import shutil
from pathlib import Path

from PIL import Image, ImageOps
import pytesseract


def _configure_tesseract() -> None:
    """Configure Tesseract for Windows, Linux and Docker deployments."""
    configured = os.environ.get("TESSERACT_CMD")
    if configured:
        pytesseract.pytesseract.tesseract_cmd = configured
    elif os.name == "nt":
        current = getattr(pytesseract.pytesseract, "tesseract_cmd", "")
        if not current or current == "tesseract":
            for path in (
                Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
                Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
            ):
                if path.exists():
                    pytesseract.pytesseract.tesseract_cmd = str(path)
                    break

    executable = shutil.which(pytesseract.pytesseract.tesseract_cmd)
    if not executable and os.path.isfile(pytesseract.pytesseract.tesseract_cmd):
        executable = pytesseract.pytesseract.tesseract_cmd
    if not executable:
        raise RuntimeError(
            "Tesseract OCR is not installed or is not on PATH. "
            "Install the tesseract-ocr system package or set TESSERACT_CMD."
        )
    pytesseract.pytesseract.tesseract_cmd = executable


def extract_text_from_image(path: Path) -> str:
    _configure_tesseract()
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        return pytesseract.image_to_string(image)
