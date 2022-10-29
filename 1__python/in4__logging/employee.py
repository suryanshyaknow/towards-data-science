import logging as lg

logger = lg.getLogger(__name__) # Specifying a logger name!
logger.setLevel(lg.INFO)
# Now to set the basicConfig for this logger instead of using default config of the `root`` logger, 
# we have to create a fileHandler for this logger.
handler = lg.FileHandler('employee (new).log')
# now need to add this handler to the desired logger
logger.addHandler(handler)

# The same goes for the formatter. All the configuration that needs to be done for the `logger`, gotta be added
# or set to its handler.
formatter = lg.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

### Adding a StreamHandler to print logs in console:
stream_handler = lg.StreamHandler()
stream_handler.setFormatter(lg.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s'))
# adding it to the logger
logger.addHandler(stream_handler)


# NOTE: We can also set the level (that we initially set to the logger itself) to the filehandler, making the file 
# itself to filter all the logs accordingly.

# lg.basicConfig(filename='employee.log', level=lg.INFO,
#                     format='%(name)s %(asctime)s %(levelname)s %(message)s')

# NOTE: Since we haven't specified a logger name, so by default the logger name is `root`. 


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        logger.info('{}{}@email.com'.format(self.first, self.last))
        return '{}{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        logger.info('{} {}'.format(self.first, self.last))
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('suryansh', 'grover1999')
# emp_1.email

emp_2 = Employee('spidey', 'styles')
# emp_2.fullname

emp_3 = Employee('sherlock', 'holmes1854')
# emp_3.email