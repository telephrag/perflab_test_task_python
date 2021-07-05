#!/usr/bin/python3

import argparse
from argparse import HelpFormatter
from functools import partial
from SRC.converter import itoBase


class CustomHelpFormatter(HelpFormatter):

    def _format_action_invocation(self, action):
        if not action.option_strings:
            # Use default methods for positional arguments
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []
            if action.nargs == 0:
                # Just add options, if they expects no values (like --help)
                parts.extend(action.option_strings)
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)
                # Join the argument names (like -p --param ) and add the metavar at the end
                return '%s %s' % (', '.join(parts), args_string)

            return ', '.join(parts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='', formatter_class=CustomHelpFormatter)
    parser.add_argument('number',  metavar='<number>', type=str)
    parser.add_argument('base_1',  metavar='<base_1>', type=str)
    parser.add_argument('-base_2',  metavar='<base_2>', type=str, default = None)
    args = parser.parse_args()
    
print(itoBase(args.number, args.base_1, args.base_2))
