from csv import excel_tab
import os
import sys

class InsuranceException(Exception):
    
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message=InsuranceException.get_detailed_error_message(error_message=error_message,
                                                                        error_detail=error_detail
                                                                        )

    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        #return info about the most resent exception caught by an except clause
        _,_ ,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message= f"Error occured in sript: [{file_name}] at line number: [{line_number}] error_message: [{error_message}]" 
        return error_message
    
    #return a user friendly discription of an object
    def __str__(self) -> str:
        return self.error_message
    
    #string representation of the object
    def __repr__(self) -> str:
        return InsuranceException.__name__.str()