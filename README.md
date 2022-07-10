# Pyly

Pyly is a simple URL shortener.

There is two ways Pyly can map an URL to a simple format (alias). The first one is just giving the url to short and Pyly will create a unique hash for that URL; the second way is to give Pyly the URL to shorten alongside with a short word or sentence to link it with the URL.

Pyly will also gather analytics on who and when your Pyly alias was used.

## Create an alias

The create/ endpoint is used to create a new shorter to the specific URL.
It accepts the following parameters:

- url: url to short
- alias: (optional) the alias of the url. If not provided, then it Pyly will create a short hash for you
- ttl: (Optional) Unix epoch time of how long will the alias valid. If not provided, then it will be available forever

## Delete an alias

The delete/ endpoint will delete the alias provided

## Use an alias

The r/ endpoint will redirect you the original URL

## Gather analytics

The analytics/ endpoint will return you all the information regarding that alias in a JSON format.

## FAQ

1. Can there be multiple alias that points to the same URL?

    Yes. Pyly allows you to create multiple alias so you can use them as you want and gather analytics individually.

2. What happens if there's a collision with the alias?

    If the alias was given, then the endpoint will return an error and will refuse to create that alias.

    If the collision happens when Pyly creates the alias, then Pyly will first verify if that hash points to the URL in the database and return that one; if not, then it will hash that hash recursively until it finds a unique one or points to the URL.

3. What happens when the TTL is reached?

    Pyly will still save the alias and all the analytics. But when a user tries to access it, Pyly will return an error of expired.
