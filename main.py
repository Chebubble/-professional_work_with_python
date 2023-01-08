import application.salary
import application.db.people
from datetime import datetime, date, time
from secret_santa_bpguasch import *

def datetimetoday():
    print(datetime.now())
datetimetoday()

def my_custom_email_body_generator(pairing: list) -> str:
    return 'The giver is {} and the receiver is {}'.format(pairing[0], pairing[1])


if __name__ == '__main__':
    email_config = EmailServer(
        host="smtp.gmail.com",
        port=465,
        username='',
        password=''
    )

    game_config = Game(
        name="Smith Secret Santa",
        budget=30,
        subject="Smith's family Secret Santa 2022",
        body_generator_func=my_custom_email_body_generator
    )

    participants = {
        'borja': {
            "email": "borja@secretsanta.com",
            "avoidGiftingTo": ["mark"]
        },
        'john': {
            "email": "john@secretsanta.com",
            "avoidGiftingTo": []
        },
        'mark': {
            "email": "mark@secretsanta.com",
            "avoidGiftingTo": []
        }
    }

    secret_santa = SecretSanta(
        game_config,
        email_config,
        participants
    )

    secret_santa.dry_run()