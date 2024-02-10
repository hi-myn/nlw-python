from typing import Dict #dictionary format elements

class HttpRequest:
    #constructor method
    def __init__(
            self,  #current instance of class, to access instances and methods
            header: Dict = None, #None -> if not filled
            body: Dict = None, 
            query_params: Dict = None
        ) -> None:
        self.header = header
        self.body = body
        self.query_params = query_params
