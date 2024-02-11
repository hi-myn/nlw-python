from src.errors.error_type.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

# creating my element, to enter the validator, to check if it's working or not 
class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

# function or method I want to test, to name function
def test_tag_creator_validator(): 
    req = MockRequest(json={ "product_code" : "123425" })
    tag_creator_validator(req)

def test_tag_creator_validator_with_error():
    req = MockRequest(json={ "product_code" : 12345 })

    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
