import io
import base64
from PIL import Image


def get_binary_data(image_path) -> bytes:
    with open(image_path, "rb") as image_file:
        return image_file.read()


def encode_image(image_path) -> bytes:
    """바이너리 데이터를 base64로 인코딩한다.
    주로 데이터를 전송할 떄 사용
    """
    bin_data = get_binary_data(image_path)
    return base64.b64encode(bin_data)


def decode_image(base64_str: bytes) -> bytes:
    """base64로 인코딩된 데이터를 디코딩한다.
    전송받은 데이터를 다시 원본 데이터로서 다룰 때 사용
    """
    return base64.b64decode(base64_str)


def show_image(image_path):
    # 이미지 읽는 방법 1
    # 경로에 있는 이미지는 바로 읽을 수 있음
    image = Image.open(image_path)
    image.show()


def show_image_from_bin(bin_str: bytes):
    # 이미지 읽는 방법 2
    # binary 데이터를 Pillow로 읽을 때는 io.BytesIO를 사용
    image = Image.open(io.BytesIO(bin_str))
    image.show()


if __name__ == "__main__":
    # run in /code_snippets/image_tutorial

    # 1. 경로에 있는 이미지 바로 읽기
    img_path = "./python_pillow.png"
    show_image(img_path)

    # 2. binary 데이터를 읽기
    bin_str = get_binary_data(img_path)
    show_image_from_bin(bin_str)
