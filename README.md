# free-proxies

A snapshot list of free public proxy servers, plus the small Python script that fetches it from the [ProxyScrape](https://proxyscrape.com/) proxy table.

> **Note:** the list in this repository was last updated on 2024-01-31. Free proxies change constantly, so most entries are likely no longer working. Run the script to fetch a fresh list.

## Contents

| File | Description |
|------|-------------|
| [`proxy.py`](proxy.py) | Downloads the ProxyScrape proxy table and writes it to `proxies.json`. |
| [`proxies.json`](proxies.json) | The last downloaded list. |
| `test.html` | An unrelated saved web page; not used by the script. |

## proxies.json format

The file is keyed by proxy type, then by `ip:port`. Each entry has:

| Field | Description |
|-------|-------------|
| `anonymity` | Anonymity level reported by ProxyScrape (integer 1–3) |
| `country` | Two-letter country code (may be empty, or `None`) |
| `timeout` | Response time in milliseconds |
| `last_seen` | Unix timestamp of the last successful check |
| `uptime` | Uptime percentage |
| `alive_since` | Unix timestamp since when the proxy has been up |

Example:

```text
{"http": {"102.132.201.202:80": {"anonymity": 3, "country": "ZA", "timeout": 7420.5, "last_seen": 1706705898.1, "uptime": 88.1, "alive_since": 1706705898.3}, ...}}
```

> **Known issue:** the script saves Python's string form of the data with single quotes replaced by double quotes, not real JSON. Values such as `None` therefore appear as-is, and standard JSON parsers (for example Python's `json.load`) fail on the file.

## Usage

Requirements: Python 3 with `requests` and `loguru`.

```bash
pip install requests loguru
python proxy.py
```

This overwrites `proxies.json` in the current directory. Errors are logged and leave `proxies.json` empty.

## Disclaimer

The proxies are third-party public servers that this project does not run or vet. Traffic sent through an unknown proxy can be logged or modified, so do not send credentials or sensitive data through them.

## License

This repository has no license file.
