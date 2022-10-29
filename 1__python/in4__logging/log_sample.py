import logging as lg
import employee

logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)
f_handler = lg.FileHandler('sample (new).log')
f_handler.setFormatter(lg.Formatter("%(asctime)s %(name)s %(message)s"))
logger.addHandler(f_handler)

## Now, even after creating a separate filehandler, logs are getting stored to the file created by the basicConfig
## as well, thus, we have to NOT SET the basicConfig or there's no point of creating a separate handler beacuase 
## makes no sense to store logs simultaneously into two files.
# lg.basicConfig(filename='sample.log', level=lg.INFO, format='%(name)s %(asctime)s %(levelname)s %(message)s')

"""
NOTE: Now that I've imported the 'employee' module, 'sample.log' isn't getting created and all the logs are being
stored to the 'employee.log' log file.

REASON: Because by the time logging configuration of this file gets configured, configuration of `epmloyee` module
has already been configured. 
"""

"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING (default level): An indication that something unexpected happened, or indicative of some problem in the near future 
(e.g. ‘disk space low’). The software is still working as expected.

--> default level means here by default only warnings and levels above warning that are error and critical will 
logged into the console.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        return x / y
    # except Exception as e:
    #     logger.error(e)
    ### NOTE: We can also inslude a <traceback> of the error occured 
    # just by replacing logger.error by logger.exception.

    except Exception as e:
        logger.exception(e)

num_1 = 21
num_2 = 0

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))