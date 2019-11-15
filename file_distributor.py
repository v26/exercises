"""File Distributor

The script checks a given directory for new files matching a pattern,
and if found moves them to an appropriate directory according to a date
parsed from the file name. If no target directory found it is created.

Files to process have names following the next pattern:
"f_[YEAR][MONTH][DAY][HOUR][MIN][SEC]_ext.dat"
example filename: "f_20191114155043_ext.dat"

Target directory structure is organized by year/month/day this way:
    out_dir
    |-- 2019
        |-- 01
        ...
        |-- 12
            |-- 01
            ...
            |-- 30
    |-- 2020
        ...

The script parses following arguments from ./config.ini file:
    in (str): the location of files to process
    out (str): the location to put processed files to
    logs (str): the log-files location to write
    time_out (int): interval to check for new files
"""

from re import search
from os import path, makedirs, rename
from glob import iglob
from datetime import datetime


def distr_files(in_dir, out_dir, filename_templ, time_out, logs_dir) -> None:
    """
    Checks for new files in <in_dir> and distributes them to <out_dir> to an
    appropriate directory according to date parsed from file name
    """

    for filepath in iglob(path.join(in_dir, filename_templ)):

        if (_file_not_empty(filepath) and
                _file_older_than(time_out, _filename_from(filepath))):
            print(filepath, path.getsize(filepath))
            _distr_file(filepath, out_dir)


def _file_not_empty(filepath) -> bool:
    return path.getsize(filepath) > 0


def _file_older_than(minutes, filename) -> bool:
    now = datetime.now().replace(microsecond=0)
    mod_time = _get_datetime_from(filename)
    diff_in_min = (now - mod_time).total_seconds() / 60
    return diff_in_min > minutes


def _get_datetime_from(filename) -> datetime:
    date_time = search('f_(.*)_ext.dat', filename)
    return datetime.strptime(date_time.group(1), "%Y%m%d%H%M%S")

def _get_date_from(filename) -> tuple:
    date_time = search('f_(.*)_ext.dat', filename).group(1)
    year = date_time[0:4]
    month = date_time[4:6]
    day = date_time[6:8]
    return year, month, day

def _filename_from(filepath) -> str:
    return path.basename(filepath)


def _move_file(from_path, to_dir) -> None:
    to_path = path.join(to_dir, _filename_from(from_path))
    rename(from_path, to_path)


def _distr_file(filepath, output_dir) -> None:
    """
    Distribute file with <filename> to the appropriate directory in <output_dir>
    """

    date = _get_date_from(_filename_from(filepath))
    target_dir = path.join(output_dir, *date)

    makedirs(target_dir, exist_ok=True)
    _move_file(filepath, target_dir)


def main():
    # hard-coded parameters for distributor draft implementation testing
    kwargs = {
        'in_dir': "./in/",
        'out_dir': "./archive/",
        'time_out': 5,
        'logs_dir': "./logs/",
        'filename_templ': 'f_[12][019][0-9][0-9][01][0-9][0-3][0-9][012][0-9][0-5][0-9][0-5][0-9]_ext.dat'
    }

    distr_files(**kwargs)


if __name__ == "__main__":
    main()
