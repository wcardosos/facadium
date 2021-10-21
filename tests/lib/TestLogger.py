from unittest import TestCase, main
from unittest.mock import patch
from src.lib.logger import Logger


class TestLogger(TestCase):
    def setUp(self) -> None:
        self.logger = Logger()

    @patch('src.lib.logger.cprint')
    def test_logger_info(self, cprint_spy):
        with patch('src.lib.logger.datetime') as datetime_stub:
            text = 'info'
            datetime_stub.now = lambda: 'hour'
            expected_text = 'hour - info'

            self.logger.info(text)
            
            cprint_spy.assert_called_once_with(expected_text)
    
    @patch('src.lib.logger.cprint')
    def test_logger_warn(self, cprint_spy):
        with patch('src.lib.logger.datetime') as datetime_stub:
            text = 'warning'
            datetime_stub.now = lambda: 'hour'
            expected_text = 'hour - warning'
            expected_color = 'yellow'

            self.logger.warn(text)
            
            cprint_spy.assert_called_once_with(expected_text, expected_color)
    
    @patch('src.lib.logger.cprint')
    def test_logger_error(self, cprint_spy):
        with patch('src.lib.logger.datetime') as datetime_stub:
            text = 'error'
            datetime_stub.now = lambda: 'hour'
            expected_text = 'hour - error'
            expected_color = 'red'

            self.logger.error(text)
            
            cprint_spy.assert_called_once_with(expected_text, expected_color)

if __name__ == '__main__':
    main()