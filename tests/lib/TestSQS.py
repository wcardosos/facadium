from unittest import TestCase, main
from unittest.mock import Mock, patch
from src.lib.sqs import SQS


class TestSQS(TestCase):
    @patch('src.lib.sqs.boto3.client')
    def test_receive_message_call_boto3_sqs_client_receive_message(self, boto3_client_spy) -> None:
        sqs = SQS()
        
        sqs.receive_message()

        sqs.client.receive_message.assert_called()
        
    @patch('src.lib.sqs.boto3.client')
    def test_receive_message_call_boto3_sqs_client(self, boto3_client_spy) -> None:
        MOCK_MESSAGE = {
            'receipt_handle': 'sqs'
        }
        sqs = SQS()
        
        sqs.delete_message(MOCK_MESSAGE)

        sqs.client.delete_message.assert_called()

    def test_parse_message_returns_empty_list_when_do_not_have_messages(self) -> None:
        sqs = SQS()
        MOCK_SQS_RESPONSE = {}

        message = sqs.parse_message(MOCK_SQS_RESPONSE)

        self.assertEqual(message, None)

    def test_parse_message_returns_correctly_when_sqs_response_is_passed(self):
        sqs = SQS()
        MOCK_MESSAGE_ID = 'id'
        MOCK_RECEIPT_HANDLE = 'receipt handle'
        MOCK_BODY = { 'message': 'ok', 'erro': False }
        MOCK_SQS_RESPONSE = {
            'Messages': [{
                'MessageId': MOCK_MESSAGE_ID,
                'ReceiptHandle': MOCK_RECEIPT_HANDLE,
                'Body': MOCK_BODY
            }]
        }

        message = sqs.parse_message(MOCK_SQS_RESPONSE)

        self.assertEqual(message['id'], MOCK_MESSAGE_ID)
        self.assertEqual(message['receipt_handle'], MOCK_RECEIPT_HANDLE)
        self.assertEqual(message['body'], MOCK_BODY)



if __name__ == '__main__':
    main()