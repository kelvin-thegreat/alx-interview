#!/usr/bin/python3
'''A script for parsing HTTP request logs.

This script reads and parses HTTP request logs line by line and computes metrics, including
total file size and the number of lines for specific status codes.
'''

import re

def extract_input(log_line):
    '''Extracts sections of a line of an HTTP request log.

    Args:
        log_line (str): A line from an HTTP request log.

    Returns:
        dict: A dictionary containing extracted information, including status code and file size.
    '''
    log_pattern = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(log_pattern[0], log_pattern[1], log_pattern[2], log_pattern[3], log_pattern[4])
    log_match = re.fullmatch(log_format, log_line)
    if log_match is not None:
        status_code = log_match.group('status_code')
        file_size = int(log_match.group('file_size'))
        log_info['status_code'] = status_code
        log_info['file_size'] = file_size
    return log_info

def print_statistics(total_size, status_code_counts):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_size (int): Total file size.
        status_code_counts (dict): A dictionary containing the count of status codes.
    '''
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts.get(status_code, 0)
        if count > 0:
            print('{:s}: {:d}'.format(status_code, count), flush=True)

def update_metrics(log_line, total_size, status_code_counts):
    '''Updates the metrics from a given HTTP request log.

    Args:
        log_line (str): The line of input from which to retrieve the metrics.
        total_size (int): Current total file size.
        status_code_counts (dict): A dictionary containing the count of status codes.

    Returns:
        int: The new total file size.
    '''
    log_info = extract_input(log_line)
    status_code = log_info.get('status_code', '0')
    if status_code in status_code_counts.keys():
        status_code_counts[status_code] += 1
    return total_size + log_info['file_size']

def run():
    '''Starts the log parser.

    This function initiates the HTTP request log parsing process, updating metrics and
    printing statistics after every 10 lines.
    '''
    line_num = 0
    total_size = 0
    status_code_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            log_line = input()
            total_size = update_metrics(
                log_line,
                total_size,
                status_code_counts,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_size, status_code_counts)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_size, status_code_counts)

if __name__ == '__main__':
    run()
