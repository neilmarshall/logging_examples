import logging

logging.basicConfig()

def log_error():
    """Demonstrate logging.error"""
    try:
        print(1 / 0)
    except Exception as e:
        logging.error(e)


def log_error_with_exception_info():
    """Demonstrate logging.error with exception information"""
    try:
        print(1 / 0)
    except Exception as e:
        logging.error(e, exc_info=True)


def log_error_with_stack_trace_info():
    """Demonstrate logging.error with stack trace information"""
    try:
        print(1 / 0)
    except Exception as e:
        logging.error(e, stack_info=True)


def log_error_format_msg():
    """Demonstrate logging.error with a custom message format"""
    try:
        print(1 / 0)
    except Exception as e:
        logging.error("encountered an error - %s", e)


def log_exception():
    """Demonstrate logging.exception"""
    try:
        print(1 / 0)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    log_error()
    log_error_with_exception_info()
    log_error_with_stack_trace_info()
    log_error_format_msg()
    log_exception()
