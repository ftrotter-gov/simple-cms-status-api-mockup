#!/usr/bin/env python3

import csv
import json
import sys
from pathlib import Path


def is_numeric(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def convert_value(value: str):
    number = float(value)
    return int(number) if number.is_integer() else number


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} input.csv variable_name output.json")
        sys.exit(1)

    input_csv = Path(sys.argv[1])
    variable_name = sys.argv[2]
    output_json = Path(sys.argv[3])

    values = []

    with input_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            values.append(row[0].strip())

    if not values:
        result = {variable_name: []}
    elif all(is_numeric(v) for v in values):
        result = {variable_name: [convert_value(v) for v in values]}
    else:
        result = {variable_name: values}

    with output_json.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"Wrote {output_json}")


if __name__ == "__main__":
    main()
