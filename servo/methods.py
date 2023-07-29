from jsonrpcserver import method, Success, Result
from servo import sg_handler as sg


@method
def feed() -> Result:
    sg.feed()
    return Success()


@method
def rotate(angle: int):
    sg.rotate(angle)
    return Success()
