# Lab-93 Argument Handling

# Documentation
## [```ArgumentHandling.__init__```](https://github.com/guyyatsu/ArgumentHandling/blob/121cfb5376992cfcef60b4fdf692c47d7c11c476/src/ArgumentHandling/ArgumentHandling.py#L22-L34)  
Accepts a nested dictionary formatted with everything argparse needs to add a fully fleshed argument.  One argument per nesting.  
  - ```ArgumentDict```: __dictionary__: Contains sub-dictionaries that define individual arguments for argparse to initialize.
    - ```ArgumentDict["options"][0]```: __string__: POSIX short-form flag.
    - ```ArgumentDict["options"][1]```: __string__: POSIX long-form flag.
    - ```ArgumentDict["help"]```: __string__: Help-text for the option.
    - ```ArgumentDict["type"]```: __variable__: The class type of the value to be stored by the option.
    - ```ArgumentDict["action"]```: __string__: The argparse action string that defines what to do with input.