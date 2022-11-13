from loguru import logger

from django.conf import settings

from polyfile.magic import MagicMatcher, DEFS_DIR


def validate_media(media):
    """Make sure we only accepts media file formats.
    
    Used by a form clean method.
    
    Args:
        a media to validate
        
    Returns:
        boolean whether it is valid or not
    """
    list_of_paths_to_definitions = [
        DEFS_DIR / "images", DEFS_DIR / "animation", DEFS_DIR / "jpeg"
    ]
    matcher = MagicMatcher.parse(*list_of_paths_to_definitions)

    for match in matcher.match(media.read()):
        logger.debug(f"Match string: {match!s}")
        return True

    logger.debug("No match, file appears to be invalid")
    return False


def validate_media_size(size):
    """Makes sure our media file is not above a certain size limit.
    
    Args:
        a given size in Bytes

    Returns:
        boolean whether it is under the size limit
    """
    import pdb; pdb.set_trace()
    if size < settings.MAX_UPLOAD:
        return True

    return False
