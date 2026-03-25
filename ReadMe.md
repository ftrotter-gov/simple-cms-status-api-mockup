# CMS Status API Placeholder

A placeholder for a real API that should allow downstream ETL development until the real API is ready.

## Verification Status APIs

You can use these URLs as a source in your ETL as a mockup:

* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/verification_api_mock/aligned-with-cms-data-network.json>
* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/verification_api_mock/cms-enrollment-in-good-standing.json>
* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/verification_api_mock/cms-ial2-verified.json>

## Data Network APIs

### Data Network Index

Get the list of all CMS-aligned data networks:

* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/data_network_index_api_mock/data_network_list.json>

This index provides a JSON array with each data network's name and a link to its detailed information.

### Individual Data Networks

Each data network has its own endpoint with participating NPI information. Examples:

* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/datanetworks_api_mock/Carequality.json>
* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/datanetworks_api_mock/eHealth_Exchange.json>
* <https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/datanetworks_api_mock/Epic.json>

See the data network index for the complete list of 37+ available data networks.

## Building the Mockups

To rebuild the JSON files from the source CSV files:

```bash
python3 build_api_mockups.py
```

See [BUILD.md](BUILD.md) for detailed documentation on the build process.

## URL Pattern

All raw GitHub URLs follow this pattern:

```
https://raw.githubusercontent.com/ftrotter-gov/simple-cms-status-api-mockup/refs/heads/main/{directory}/{filename}.json
```

Where:

* `{directory}` is one of: `verification_api_mock`, `datanetworks_api_mock`, or `data_network_index_api_mock`
* `{filename}` is the name of the specific resource

Someday I might get the staticsite working with these.. but probably not.

-FT
