# Forest App API

Unofficial Python client for Forest App API. This package allows you to interact with the Forest App API to plant trees, track time, and manage your Forest account programmatically.

## Installation

```shell
pip install -r requirements.txt
pip install -e .
```

## Getting Your Remember Token

To use this API, you'll need your personal `remember_token`. Here's how to get it:

1. Install the [Forest Chrome Extension](https://chrome.google.com/webstore/detail/forest-stay-focused-be-pre/kjacjjdnoddnpbbcjilcajfhhbdhkpgk)
2. Log in to your Forest account in the extension
3. Open Chrome DevTools (F12 or Right Click -> Inspect)
4. Go to the Network tab
5. Plant a tree using the extension
6. Look for a request to `https://c88fef96.forestapp.cc/api/v1/plants`
7. In the request headers or cookies, find `remember_token=your_token_here`

⚠️ **Security Note**: Keep your remember_token private. Probably isnt a good idea to release it to the world.

## Usage

```python
from forest_app import ForestClient
from datetime import datetime, timedelta

# Initialize client with your remember token

client = ForestClient("your_remember_token")

# Get user info

user = client.get_user_info()
print(f"Welcome {user.name}! You have {user.coin} coins")

# Get available tags

tags = client.get_tags()
for tag in tags:
print(f"Tag: {tag.title} (ID: {tag.tag_id})")

# Get unlocked trees

trees = client.get_unlocked_trees()
for tree in trees:
print(f"Tree: {tree.title} (GID: {tree.gid})")

# Plant a tree with a specific tag and tree type

response = client.plant_tree(
duration_minutes=25,
tree_type_gid=114, # Wishing Flower
tag=2, # Study tag
note="Working on Python"
)
print(f"Planted tree ID: {response.id}")

# Get list of planted trees

plants = client.get_plants()
for plant in plants:
print(f"Tree planted at {plant.start_time}")
```

## Available Methods

- `plant_tree()`: Plant a new tree with specified duration and options
- `get_plants()`: Get list of all planted trees
- `get_user_info()`: Get current user information
- `get_tags()`: Get list of user's tags
- `get_unlocked_trees()`: Get list of available tree types

## Models

The package includes several dataclasses for working with Forest App data:

- `Plant`: Represents a planted tree session
- `Tree`: Individual tree details
- `TreeType`: Available tree types
- `Tag`: Time tracking tags
- `User`: User account information

## Contributing

Feel free to open issues or submit pull requests for improvements.

## Disclaimer

This is an unofficial API client and is not affiliated with or endorsed by Forest App. Use at your own risk.

## License

MIT License
