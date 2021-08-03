import pytest
from ml import predict


@pytest.mark.parametrize(
    "image_path, expected",
    [
        ("sample-3.png", 3),
        ("sample-7.jpg", 4),
    ],
)
def test_predict(image_path, expected):
    assert predict(image_path) == expected
