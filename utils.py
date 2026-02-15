import logging
import io
from typing import Optional
from pypdf import PdfReader

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_text_from_pdf(file_obj: io.BytesIO) -> str:
    """
    Extracts text from a PDF file object.
    
    Args:
        file_obj (io.BytesIO): The uploaded PDF file object.
        
    Returns:
        str: The extracted text from the PDF.
    """
    try:
        reader = PdfReader(file_obj)
        text = ""
        
        # Iterate over all pages
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        
        logger.info(f"Successfully extracted {len(text)} characters from PDF.")
        return text

    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""

def truncate_text(text: str, max_tokens: int = 12000) -> str:
    """
    Primitive truncation to fit context windows if necessary.
    In a real app, use tiktoken for precise counting.
    Here we assume rough character count ~4 chars per token.
    """
    max_chars = max_tokens * 4
    if len(text) > max_chars:
        logger.warning(f"Text too long ({len(text)} chars). Truncating to {max_chars} chars.")
        return text[:max_chars]
    return text
