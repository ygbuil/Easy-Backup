import os
import pytest


@pytest.mark.parametrize(
    "subsequent_dir",
    [
        [""],
        ["file_1.txt"],
        ["file_2.txt"],
        ["folder_1"],
        ["folder_1", "file_3.txt"],
        ["folder_1", "file_4.txt"],
        ["folder_2"],
    ],
)
def test_origin_folder_creation(origin_folder, subsequent_dir):
    assert os.path.exists(os.path.join(origin_folder, *subsequent_dir))


@pytest.mark.parametrize(
    "subsequent_dir",
    [
        [""],
        ["file_1.txt"],
        ["file_2.txt"],
        ["file_to_delete_1.txt"],
        ["folder_1"],
        ["folder_1", "file_3.txt"],
        ["folder_1", "file_to_delete_2.txt"],
        ["folder_to_delete_1"],
    ],
)
def test_destination_folder_creation(destination_folder, subsequent_dir):
    assert os.path.exists(os.path.join(destination_folder, *subsequent_dir))
