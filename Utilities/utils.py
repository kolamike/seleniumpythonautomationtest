import inspect
import logging

import softest

class utils(softest.TestCase):
    def assertlistitemText(self,list,value):
        for stop in list:
            print("The text is: " + stop.text)
            self.soft_assert(self.assertEqual,stop.text,value)
            if stop.text == value:
                print("test passed")
            else:
                print("test failed")
        self.assert.all()

    def custlogger(self,loglevel=logging.DEBUG):
        # set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        #createlogger
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        #create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        #create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or file handler
        fh.setFormatter(formatter)
        #add console handler to logger
        logger.addHandler(fh)
        return logger

