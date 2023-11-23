import logging
from datetime import date

def createLoggerObj():
    today = date.today() 
    fileName  = str(today) + '.log' 
    formatStr = '%(asctime)s %(message)s'
    logging.basicConfig(format=formatStr, filename=fileName, level=logging.INFO)
    myLogObj = logging.getLogger('sqa2023-logger') 
    return myLogObj