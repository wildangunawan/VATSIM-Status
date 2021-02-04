# VATSIM Status

## Overview

VATSIM Status is a list of online users in VATSIM. It's open for public and doesn't require any token or verification. This parser will parse latest JSON3 from VATSIM Status that's available.

## Prerequisites

This script made with Python and doesn't require any specific Python version or any extra library to download.
The recommended version is Python 3.7.x or newer. You can check your Python version by using command:

In Windows Command Prompt:
> python -V

In Linux console:
> python3 -V

## Installation Guide

It's pretty straight forward. get-data.py used to get VATSIM current data, and app.py to run the parser. Parse result will be at /result folder. I also create vatsim-status.sh for cronjob. VATSIM only allows data fetch every two minutes. If you run every one minute, your VPS or hosting can be banned for too much request by VATSIM.

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE](LICENSE) file for details
