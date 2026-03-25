#!/bin/bash
python csv_to_json_is_simple.py src_csv/cms-enrollment-in-good-standing.csv cms-enrollment-in-good-standing apimock/cms-enrollment-in-good-standing.json
python csv_to_json_is_simple.py src_csv/cms-ial2-verified.csv cms-ial2-verified apimock/cms-ial2-verified.json
python csv_to_json_is_simple.py src_csv/aligned-with-cms-data-network.csv aligned-with-cms-data-network apimock/aligned-with-cms-data-network.json
