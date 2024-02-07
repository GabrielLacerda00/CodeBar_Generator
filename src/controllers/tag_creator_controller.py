from typing import Dict
from src.drivers.barcode_handler import BarCodeHandler

class TagCreatorController:
    '''
        responsibility for bussiness logic
    '''
    def create(self, product_code: str) -> Dict:
        path = self.__create_bar_code(product_code)
        formatted_response = self.__format_response(path)
        return formatted_response
    def __create_bar_code(self, product_code: str) ->str:
        bar_code_handler = BarCodeHandler()
        path_from_tag = bar_code_handler.create_bar_code(product_code)
        return path_from_tag
    def __format_response(self,path_from_tag: str) -> Dict:
        return {
            "data":{
                "type": "Tag Image",
                "Count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
