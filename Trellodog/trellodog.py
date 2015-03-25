

from trello import *
from datetime import datetime, timedelta
import requests
import json

def get_action(self, board_id, filter=None, fields=None, limit=None, page=None, idModels=None, since=None):
    resp = requests.get("https://trello.com/1/boards/%s/actions" % (board_id), params=dict(key=self._apikey, token=self._token, filter=filter, fields=fields, limit=limit, page=page, idModels=idModels, since=since), data=None)
    resp.raise_for_status()
    return json.loads(resp.content)

class Trellodog(object):
    """Trellodog is a tool for sending trello stats to datadog"""

    def __init__(self):
        pass

    def trello(self, api_key, api_token):
        self._trello = TrelloApi(api_key, api_token)

    def datadog(self, api_key):
        pass

    def list_boards(self):
        pass

    def get_card(self, card_id):

        try:
            card = self._trello.cards.get(card_id)
        except Exception, e:
            print e.message
            exit()

        return card

    def get_list(self, list_id):

        try:
            tlist = self._trello.lists.get(list_id)
        except Exception, e:
            print e.message
            exit()

        return tlist

    def num_cards(self, board_id):
        """Return the number of cards for board_id"""

        try:
            cards = self._trello.boards.get_card(board_id)
        except Exception, e:
            print e.message
            exit()

        return len(cards)

    def activity(self, board_id, days=2, filters='all'):
        """Return activity for board_id"""

        # Monkey patch
        self._trello.boards.get_action = get_action

        since = date_N_days_ago = datetime.now() - timedelta(days=days)

        try:
            activity = self._trello.boards.get_action(self._trello.boards, board_id, filter=filters, since=since, limit=1000)
        except Exception, e:
            print e.message
            exit()

        return activity


# trello = TrelloApi(TRELLO_APP_KEY, TRELLO_API_TOKEN)

# cards = trello.boards.get_card(board, actions='createCard')



# for c in cards:
#   pp = pprint.PrettyPrinter(indent=2)
#   pp.pprint(c)

#   pp.pprint(trello.cards.get_action(c['id'], action_fields='createCard'))

#   exit()
    # trello.cards.get_action(c['id'], action_fields='createCard')
