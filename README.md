A tiny CLI Tool for https://dog.ceo/dog-api REST API using Python

Built this simple tool in 2 hours to practise the Python scripting and API connectivity.

Features:

- List all dog breeds
- Download image of a specific breed
- Helper menu in tool

Usage:

```bash
$ dog-breeds list-all
# list all dog breeds

$ dog-breeds get-image --breed "Hound" --file "./hound.jpg"
# download an image of a breed, both arguments are required
```

The backend stores multiple images per one breed, the current implementation choose one of them randomly.

The current software is quite simple so I would prefer to publish it as a Gist. But some people may wonder how the code was organized with Git, so I present the code within a repository.


Disclaimer: If you are learning Python, feel free to use this source for practising and building your exercises. You don't need to include a copyright notice.