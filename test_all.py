#!/usr/bin/env python3

import os
import sys
import subprocess
import difflib
import pathlib
import pytest  # type: ignore


def expected_output_file_name(input_name):
    return "{}.out.cc".format(input_name[: input_name.index(".in.cc")])


THIS_DIR = pathlib.Path(__file__).parent

ALL_TEST_CASES = sorted((THIS_DIR / "test").glob("*.in.cc"))


@pytest.mark.parametrize("test_case", ALL_TEST_CASES)
def test_west_to_east_const_conv(test_case):
    exe_name = THIS_DIR / "bin" / "westerly"
    output_file_name = expected_output_file_name(str(test_case))
    command_output = subprocess.run(
        [exe_name, "--stdout", test_case], stdout=subprocess.PIPE
    )
    expected_output = pathlib.Path(output_file_name).read_text().split("\n")
    actual_output = command_output.stdout.decode().split("\n")

    if expected_output == actual_output:
        return

    the_diff = difflib.unified_diff(
        actual_output,
        expected_output,
        fromfile="actual",
        tofile=output_file_name,
        lineterm="",
    )
    for line in the_diff:
        print(line)
    assert False
