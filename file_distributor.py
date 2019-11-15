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

from re import compile


def dist_files(in_dir, out_dir, filename_templ, time_out, logs_dir) -> None:
    """
    Checks for new files in <in_dir> and distributes them to <out_dir> to an
    appropriate directory according to date parsed from file name
    """

    filenames = _filenames_by_templ_in(in_dir, filename_templ)

    if filenames:
        for filename in filenames:
            _distribute_file(filename, out_dir)


def _filenames_by_templ_in(directory, template) -> list:
    """
    Check in <directory> for files with names following the <template>
    """

    filenames = list()

    # TODO implement the method

    return filenames


def _distribute_file(filename, output_dir) -> None:
    """
    Distribute file with <filename> to the appropriate directory in <output_dir>
    """

    # TODO implement the method


def main():
    # hard-coded parameters for distributor draft implementation testing
    kwargs = {
        'in_dir': "./in/",
        'out_dir': "./archive/",
        'time_out': 0.5,
        'logs_dir': "./logs/",
        'filename_templ': compile(r'^f_[12][019][0-9][0-9][01][0-9][0-3][0-9][012][0-9][0-5][0-9][0-5][0-9]_ext\.dat$')
    }

    dist_files(**kwargs)


if __name__ == "__main__":
    main()
