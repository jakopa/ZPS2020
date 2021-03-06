"""Prepare Adult dataset
Author: Tomasz Nanowski
Group: z1

Example:
    $ python scripts/z1_prepare_data_car_one_hot.py --input-dir datasets_prepared/z2/car_int_prepared \
        --output-dir datasets_prepared/car_one_hot
"""

import argparse

import z1_convert_to_one_hot_encoding

CATEGORICAL_FEATURES_INDEXES = [0, 1, 2, 3, 4]
CATEGORICAL_FEATURES_CLASSES = [4, 4, 4, 3, 3]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--input-dir", required=True, type=str, help="Input directory"
    )
    parser.add_argument(
        "--output-dir", required=True, type=str, help="Output directory"
    )
    return parser.parse_args()


def run_script(input_dir, output_dir):
    z1_convert_to_one_hot_encoding.run_script(input_dir,
                                              output_dir,
                                              CATEGORICAL_FEATURES_INDEXES,
                                              CATEGORICAL_FEATURES_CLASSES)


if __name__ == "__main__":
    args = parse_arguments()
    run_script(args.input_dir, args.output_dir)
