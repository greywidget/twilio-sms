import keyring
from twilio.rest import Client


def main():
    client = Client(
        keyring.get_password("twilio", "account_sid"),
        keyring.get_password("twilio", "auth_token"),
    )
    message = client.messages.create(
        from_=keyring.get_password("twilio", "phone"),
        body="Hello Mrs Pickle",
        to=keyring.get_password("twilio", "my_mobile"),
    )

    print(message.sid)


if __name__ == "__main__":
    main()
