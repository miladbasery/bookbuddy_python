import functools
from config.logger import logger

def log_activity(action: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Starting action: {action}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Completed action: {action}")
                return result
            except Exception as e:
                logger.error(f"Error during action: {action} - {e}")
                raise
        return wrapper
    return decorator