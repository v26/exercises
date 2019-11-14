"""File distributor

The script checks a given directory for new files matching a pattern
and if found moves them to an appropriate directory according to a date
parsed from file name.

The script parses next arguments from ./config.ini file:
    in (str): the location of files to process
    out (str): the location to put processed files to
    logs (str): the log-files location to write
    time_out (int): interval to check for new files at 'in' dir
"""

