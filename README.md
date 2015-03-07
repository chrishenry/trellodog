trellodog
=========

Trello tool for sending graphs to data and generating activity reports

Authentication
===========

trellodog is configured with 2 environment variables

```bash
$  export TRELLO_APP_KEY=<trello api key>
$  export TRELLO_API_TOKEN=<trello api token>
```

Activity
===========
Can be called, from the `bin` directory, like;

```bash
./stats activity <board id>

# to copy output to clipboard (mac only)
./stats <board id> | pbcopy
```

