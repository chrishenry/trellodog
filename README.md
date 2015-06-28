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
./stats activity <board id> | pbcopy
```

This command will convert timestamps to your current timezone. You can also
explicit ask it to convert to a specific timezone.

```bash
./bin/stats activity h8dlORO8 -d 1 -t "America/New_York"
./bin/stats activity h8dlORO8 -d 1 -t "America/Costa_Rica"
./bin/stats activity h8dlORO8 -d 1 -t "America/Los_Angeles"
```

The complete list of timezone values can be found [on wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).
