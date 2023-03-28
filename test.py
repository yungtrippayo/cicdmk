import os
import pytest

@pytest.fixture
def input_file(tmp_path):
    data = "This is a test.\nThis line contains the keyword.\nThis is another test.\n"
    file_path = tmp_path / "input.txt"
    with open(file_path, "w") as f:
        f.write(data)
    return file_path

    # перевіряємо, чи вихідний файл був створений
    assert os.path.isfile(output_file)

    # перевіряємо, чи відфільтровано правильні рядки
    with open(output_file, "r") as f:
        filtered_lines = f.readlines()
        assert len(filtered_lines) == 1
        assert keyword in filtered_lines[0]


