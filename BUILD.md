# Building the API Mockups

## Quick Start

To rebuild all API mockup files from CSV sources:

```bash
python3 build_api_mockups.py
```

## What It Does

The build script automates converting CSV files to JSON mockup APIs:

1. **Verification Status Files**: `status_csv/*.csv` → `verification_api_mock/*.json` (3 files)
2. **Data Network Files**: `data_network_csv/*.csv` → `datanetworks_api_mock/*.json` (37 files)
3. **Data Network Index**: Creates `data_network_index_api_mock/data_network_list.json` with all network names and GitHub raw URLs

## Adding New Data Networks

1. Create `data_network_csv/NewNetwork.csv` with header: `CMS_Aligned_Data_Network_Participating_NPI`
2. Add NPI values (one per line)
3. Run `python3 build_api_mockups.py`
4. The network automatically appears in both `datanetworks_api_mock/` and the index

## Configuration

Set `GITHUB_REPO` environment variable to change the repository for raw URLs:

```bash
GITHUB_REPO="username/repo-name" python3 build_api_mockups.py
```

Default: `ftrotter-gov/simple-cms-status-api-mockup`

## Notes

- The script is idempotent - safe to run multiple times
- All output directories are created automatically
- Existing JSON files are overwritten with fresh data from CSV sources
- The old `go.sh` script is deprecated
