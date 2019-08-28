import json
import difflib


def format_dict(dictionary):
    """
    Formats dicts with indentation.

    :param dictionary: dict
    :return: str
    """
    return json.dumps(dictionary, indent=4)


def decode_byte_string_to_dict(out):
    """
    Takes output from Process and converts it to a dict.
    :param out: str
    :return: dict
    """
    try:
        json_data = json.loads(out)
        return json_data
    except json.decoder.JSONDecodeError:
        return None


def dict_comparison(dict1, dict2, show_diff=False):
    """
    Compares two dicts for equality by converting to key-sorted dicts.

    The difference can be plotted by giving an additional show_diff bool.
    :param dict1: dict
    :param dict2: dict
    :param show_diff: bool
    :return: bool
    """
    dict1 = json.dumps(dict1, sort_keys=True, indent=4)
    dict2 = json.dumps(dict2, sort_keys=True, indent=4)
    are_equal = dict1 == dict2

    # only if the two dicts are not the same, show difference
    if not are_equal and show_diff:
        d = difflib.Differ()
        # need to split into lines by newline character but keep newline
        # for better printing
        dict1_lines = [l + '\n' for l in dict1.split('\n')]
        dict2_lines = [l + '\n' for l in dict2.split('\n')]
        difference = d.compare(dict1_lines, dict2_lines)
        print('\nDicts are NOT equal:')
        print(''.join(difference))

    return are_equal
