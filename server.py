from jsonrpcserver import serve
from servo.sg_handler import end
import servo.methods

if __name__ == "__main__":
    try:
        serve(port=1337)
    except KeyboardInterrupt:
        end()
