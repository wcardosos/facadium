from datetime import datetime
from termcolor import cprint

class Logger:
    def info(self, text: str) -> None:
        text_to_print = f"{datetime.now()} - {text}"
        cprint(text_to_print)
    
    def warn(self, text: str) -> None:
        text_to_print = f"{datetime.now()} - {text}"
        cprint(text_to_print, 'yellow')
    
    def error(self, text: str) -> None:
        text_to_print = f"{datetime.now()} - {text}"
        cprint(text_to_print, 'red')
