
from src.server.instance import server
from src.controllers.load import *

from src.extract import extract
from src.transform import transform

if __name__ == '__main__':
    extract()
    transform()
    server.run()

