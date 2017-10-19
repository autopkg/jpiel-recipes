#!/usr/bin/env python

import getpass

from autopkglib import Processor, ProcessorError

__all__ = ["GetCurrentUserInfo"]

class GetCurrentUserInfo(Processor):
    """Set the cur_user variable from the user running autopkg"""
    input_variables = {
    }
    
    output_variables = {
       "cur_user": {
            "description": "Current user running autopkg",
        },
    }
   
    description = __doc__
     
    def main(self):
        self.env["cur_user"] = getpass.getuser()


if __name__ == "__main__":
    processor = GetCurrentUserInfo()
    processor.execute_shell()
    