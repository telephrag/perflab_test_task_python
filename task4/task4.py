#!/usr/bin/python3

import argparse
from argparse import HelpFormatter
from functools import partial
from SRC.comparator import compare

class CustomHelpFormatter(HelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)
                return '%s %s' % (', '.join(parts), args_string)

            return ', '.join(parts)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='Describe your project', formatter_class=CustomHelpFormatter)
    
    parser.add_argument('word1', metavar='<word1>', type=str)
    parser.add_argument('word2', metavar='<word2>', type=str)
    
    args = parser.parse_args()

if args.word1 and args.word2 :
    compare(args.word1, args.word2)
    
