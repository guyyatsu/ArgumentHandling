#!/bin/python3
"""
"""
import argparse


class ArgumentHandling:
  """ Automated argument handling framework for bigger projects.
      Accepts a single required argument, ArgumentDictionary, which
  is a nested dictionary structured with keys for flag options, help text,
  a classification type, and the correct action to apply.
      Example:
        ArgumentDict = {
          0: {
            "options": ["-short", "--long"],
            "help": 'A short description of what this argument does.',
            "type": type(value_to_be_collected_by_argument),
            "action": str("ArgParse action string to be taken.")
          }
        } """

  def __init__(self, ArgumentDict: dict):
    self.parser = argparse.ArgumentParser()

    for argument in ArgumentDict.keys():
      argument = ArgumentDict[argument]
      self.parser.add_argument(
                                argument['options'][0],
                                argument['options'][1],
                                help=str(argument['help']),
                                type=argument['class'],
                                action=str(argument['action']) )

    self.args = self.parser.parse_args()