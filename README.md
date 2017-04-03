# WetterKassel
Code for [@WetterKassel](https://twitter.com/WetterKassel) Twitter bot.

This bot tweets forecasts for the current and next day.

[Powered by the DarkSky API](https://darksky.net/poweredby)

## Installation
```bash
git clone https://github.com/jakobbbb/wetterkassel
cd wetterkassel
python setup.py build
python setup.py install
```

## Running
```bash
python WetterKassel.py today # today's forecast
python WetterKassel.py tomorrow # tomorrow's forecast
```

## Configuring
On the first run 'config.json' is generated and can be edited to configure WetterKassel.

## Sample Crontab
```cron
MAILTO=user@example.com
0 19 * * * /usr/bin/python /home/user/wetterkassel/WetterKassel.py tomorrow >> /home/user/wetterkassel/wetterkassel.log
0 7 * * * /usr/bin/python /home/user/wetterkassel/WetterKassel.py today >> /home/user/wetterkassel/wetterkassel.log
```
