# VATSIM Status

VATSIM Status is a list of online users in VATSIM. It's open for public and doesn't require any token or verification.
There is two version of VATSIM Status that's currently running, TXT and JSON. This parser will parse JSON file instead.

### Prerequisites

This script made with Python and doesn't require any specific Python version or any extra library to download.
The recommended version is Python 3.7.6 or newer. You can check your Python version by using command:
In Windows Command Prompt:
> python -V

In Linux console:
> python3 -V

### Installing

It's pretty straight forward. get-data.py used to get VATSIM current data, and app.py to run the parser. Parse result will be at /result folder. I also create vatsim-status.sh for cronjob. The best option is run vatsim-status.sh every two minutes. If you run every one minute, your VPS or hosting can be banned for over request by VATSIM.

Follow step below to insert command into cronjob:
1. Login to your cPanel
2. Search Cron Jobs under Advanced submenu
3. Find "Add New Cron Jobs" and follow the settings below:
- Minute: Once per two minutes (*/2)
- Hour: Every hour (*)
- Day: Every day (*)
- Month: Every month (*)
- Weekday: Every day (*)

Command:
> path/to/folder/vatsim-status.sh

## Deployment

Consult with your hosting provider about Python 3 path. It might be different for each hosting.

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE.md](LICENSE.md) file for details
