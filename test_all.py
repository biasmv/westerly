#!/usr/bin/env python3

import os
import sys
import glob
import subprocess
import difflib

pjoin = os.path.join


def expected_output_file_name(input_name):
    return "{}.out.cc".format(input_name[: input_name.index(".in.cc")])


def read_file_contents(fn):
    with open(fn, "r") as f:
        return f.read().split("\n")


def verify_west_to_const_conv(test_case):
    exe_name = pjoin(os.path.dirname(__file__), "bin", "westerly")
    print("verifying '{}'".format(test_case))
    output_file_name = expected_output_file_name(test_case)
    command_output = subprocess.run(
        [exe_name, "--stdout", test_case], stdout=subprocess.PIPE
    )
    expected_output = read_file_contents(output_file_name)
    actual_output = command_output.stdout.decode().split("\n")

    if expected_output == actual_output:
        return True

    the_diff = difflib.unified_diff(
        actual_output,
        expected_output,
        fromfile="actual",
        tofile=output_file_name,
        lineterm="",
    )
    for line in the_diff:
        print(line)
    return False


def test_all():
    test_dir_path = pjoin(os.path.dirname(__file__), "test")
    num_failed = 0
    for test_case in sorted(glob.glob(pjoin(test_dir_path, "*.in.cc"))):
        if not verify_west_to_const_conv(test_case):
            num_failed += 1
    assert num_failed == 0
