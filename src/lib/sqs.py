import boto3


class SQS:
    def __init__(self) -> None:
        self.client = boto3.client('sqs')

    def parse_message(self, response):
        messages_returned = response.get('Messages')

        if not messages_returned:
            return None

        message_to_parse = messages_returned[0]

        message = {
            'id': message_to_parse['MessageId'],
            'receipt_handle': message_to_parse['ReceiptHandle'],
            'body': message_to_parse['Body']
        }

        return message
    
    def receive_message(self):
        response = self.client.receive_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/261263095887/teste'
        )

        message = self.parse_message(response)

        return message

    def delete_message(self, message):
        receipt_handle = message['receipt_handle']

        self.client.delete_message(
            QueueUrl='https://sqs.us-east-1.amazonaws.com/261263095887/teste',
            ReceiptHandle=receipt_handle
        )
        