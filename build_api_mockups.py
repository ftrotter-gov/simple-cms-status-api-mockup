#!/usr/bin/env python3
"""
Build API Mockups Script

This script automates the conversion of CSV files to JSON format for the CMS Status API mockup.
It handles both verification status data and data network information.
"""

import json
import os
import sys
from pathlib import Path
import csv


def is_numeric(value: str) -> bool:
    """Check if a string value can be converted to a number."""
    try:
        float(value)
        return True
    except ValueError:
        return False


def convert_value(value: str):
    """Convert a numeric string to int or float as appropriate."""
    number = float(value)
    return int(number) if number.is_integer() else number


def csv_to_json(*, input_csv: Path, variable_name: str, output_json: Path) -> None:
    """
    Convert a CSV file to JSON format.
    
    Args:
        input_csv: Path to input CSV file
        variable_name: Name of the JSON variable/key
        output_json: Path to output JSON file
    """
    values = []

    with input_csv.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        # Skip the header row
        next(reader, None)
        
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

    # Ensure output directory exists
    output_json.parent.mkdir(parents=True, exist_ok=True)
    
    with output_json.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"✓ Created {output_json}")


def build_verification_status_files() -> None:
    """Build verification status JSON files from CSV sources."""
    print("\n=== Building Verification Status Files ===")
    
    status_mappings = [
        {
            "input": "status_csv/cms-enrollment-in-good-standing.csv",
            "variable": "cms-enrollment-in-good-standing",
            "output": "verification_api_mock/cms-enrollment-in-good-standing.json"
        },
        {
            "input": "status_csv/cms-ial2-verified.csv",
            "variable": "cms-ial2-verified",
            "output": "verification_api_mock/cms-ial2-verified.json"
        },
        {
            "input": "status_csv/aligned-with-cms-data-network.csv",
            "variable": "aligned-with-cms-data-network",
            "output": "verification_api_mock/aligned-with-cms-data-network.json"
        }
    ]
    
    for mapping in status_mappings:
        csv_to_json(
            input_csv=Path(mapping["input"]),
            variable_name=mapping["variable"],
            output_json=Path(mapping["output"])
        )


def build_data_network_files() -> list:
    """
    Build data network JSON files from CSV sources.
    
    Returns:
        List of data network names (filenames without extension)
    """
    print("\n=== Building Data Network Files ===")
    
    data_network_csv_dir = Path("data_network_csv")
    datanetworks_api_dir = Path("datanetworks_api_mock")
    
    # Ensure output directory exists
    datanetworks_api_dir.mkdir(parents=True, exist_ok=True)
    
    network_names = []
    
    # Process all CSV files except the index file
    csv_files = sorted(data_network_csv_dir.glob("*.csv"))
    
    for csv_file in csv_files:
        filename = csv_file.stem
        
        # Skip the index/list file
        if filename == "cms_aligned_data_networks":
            continue
        
        output_json = datanetworks_api_dir / f"{filename}.json"
        
        csv_to_json(
            input_csv=csv_file,
            variable_name="CMS_Aligned_Data_Network_Participating_NPI",
            output_json=output_json
        )
        
        network_names.append(filename)
    
    print(f"\n✓ Converted {len(network_names)} data network CSV files to JSON")
    return network_names


def build_data_network_index(*, network_names: list, github_repo: str) -> None:
    """
    Build the data network index JSON file.
    
    Args:
        network_names: List of data network names
        github_repo: GitHub repository path (e.g., 'ftrotter-gov/simple-cms-status-api-mockup')
    """
    print("\n=== Building Data Network Index ===")
    
    index_dir = Path("data_network_index_api_mock")
    index_dir.mkdir(parents=True, exist_ok=True)
    
    # Create the index structure with sorted network names
    sorted_networks = sorted(network_names)
    
    index = {
        "CMS_Aligned_Data_Networks": [
            {
                "name": name,
                "link": f"https://raw.githubusercontent.com/{github_repo}/refs/heads/main/datanetworks_api_mock/{name}.json"
            }
            for name in sorted_networks
        ]
    }
    
    output_file = index_dir / "data_network_list.json"
    
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    
    print(f"✓ Created {output_file} with {len(sorted_networks)} data networks")


def main():
    """Main function to orchestrate the build process."""
    print("="*60)
    print("CMS Status API Mockup Builder")
    print("="*60)
    
    # GitHub repository (can be overridden via environment variable)
    github_repo = os.getenv(
        "GITHUB_REPO",
        "ftrotter-gov/simple-cms-status-api-mockup"
    )
    
    try:
        # Step 1: Build verification status files
        build_verification_status_files()
        
        # Step 2: Build data network files
        network_names = build_data_network_files()
        
        # Step 3: Build data network index
        build_data_network_index(
            network_names=network_names,
            github_repo=github_repo
        )
        
        print("\n" + "="*60)
        print("✓ Build completed successfully!")
        print("="*60)
        print("\nGenerated files:")
        print("  - verification_api_mock/*.json (3 files)")
        print(f"  - datanetworks_api_mock/*.json ({len(network_names)} files)")
        print("  - data_network_index_api_mock/data_network_list.json")
        print("\nReady to commit and push to GitHub!")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error during build: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
