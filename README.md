# pandascore-python

Python bindings for the Pandascore API. \
I am not associated. Use at your own risk, etc.

Only the Rest API is implemented for now. Live API to come...
Keep in mind it's a work in progess / made for fun. Help, advices and critiques are appreciated.

## Usage

Put your personal token in the "API_Token" field of the SECRETS.json file.
```json
{
	"API_Token": "YOUR-TOKEN-HERE"
}
```
Create the object relative to the game you want to make API calls for.
There are:

```python
from rest_api.general import GeneralPanda
from rest_api.lol import LeaguesOfLegends
from rest_api.dota2 import Dota2
```

Each of these objects give you access to different sets of api calls. Check out the documentation to see the api calls: \
https://api.pandascore.co/doc

GeneralPanda (might find a new name...) lets you make the calls relative to the "All Games" section of documentation. 
So more "general" calls: about all the games, the players, the tournaments, the matches etc.\
\
LeaguesOfLegends lets you make the ones on the game with the same name (duh)\
\
Dota2 the same, but there are very few methods for this one.

## TODO

Documentation of the methods.\
Better naming convention.\
Stop changing design of the structure of the code (this is like my third new way to do it).\
Live API.\
Get rid of bad practices.\
Add stuff.
