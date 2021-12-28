
# from src.server.instance import server
from src.controllers.load import *

from src.extract import extract
from src.transform import transform

def main(test=False):
    if not test:
        extract()
        transform()
    server.run()


main()


