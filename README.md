# Fidgeting (around the) ActivityPub

## Why?

[Wikipedia](https://en.wikipedia.org/wiki/ActivityPub) defines ActivityPub as an "open, decentralized social networking protocol".

My interest peaked when I started using Mastodon instead of twitter. The idea of multiple smaller instances that can talk to each other seemed very interesting, and wanted to look under the hood how this thing works. I highly resonate with [this](https://tinysubversions.com/notes/decentralized-social-networks/) blog post from 2018 by [Darius Kazemi](https://tinysubversions.com/bio.html).

So wanted to read more about this and get some first hand experience kicking some things around.

_Some places I started looking into_

1. [ActivityPub official specification](https://www.w3.org/TR/activitypub/) - Specification. By itself it is difficult to follow through. Use [2] to read through important parts of the specification
2. [A highly opinionated guide to learning about ActivityPub](https://tinysubversions.com/notes/reading-activitypub/)
3. [Decentralizing Social Interactions with ActivityPub](https://hacks.mozilla.org/2018/11/decentralizing-social-interactions-with-activitypub/)
4. [How to implement a basic ActivityPub server](https://blog.joinmastodon.org/2018/06/how-to-implement-a-basic-activitypub-server/)
5. [How to make friends and verify requests](https://blog.joinmastodon.org/2018/07/how-to-make-friends-and-verify-requests/)

## What does this project do?

A simple fastapi server that can be

- [x] [webfingered](https://en.wikipedia.org/wiki/WebFinger) to find this account in other federated instances like Mastodon and
- [ ] then being able to post content that would come up in the feed of federated instances
- [ ] (With probably being able to follow be a side effect)

## Running

_Install dependencies using:_

`pip install -r requirements.txt`

_Setup loophole.site subdomain_

[loophole](https://loophole.cloud/) is a reverse proxy useful for exposing your local port 8000 of the server to the internet.

[Download](https://loophole.cloud/download) cli for exposing local port 8000 to the internet safely.
Follow [This document](https://loophole.cloud/docs/guides/expose) on how to do it, and get a unique subdomain you can use.

_Create .env file_
Copy the sample.env file to .env file and update relevant attributes.

_Create secret and public pem file_

Create public and private pem file using

```
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -outform PEM -pubout -out public.pem

```

and keep it in a gitignored folder (./secrets is already gitignored).
Update `PUBLIC_KEY_PEM_PATH` and `PRIVATE_KEY_PEM_PATH` for the files from the root of the folder (check sample.env where the files reside in `./secrets`)

_To start server:_

`make start`

## Webfinger

Webfinger is a protocol using which activitypub supporting sites can identify and search for users in other instances.

This is a simple HTTP GET call to `/.well-known/webfinger?resource=acct:user@example.com`.
The response of json will contain reference to "Actor" - in activitypub, actor can be any
entity like user, company, group of people , etc.

In this example it is a user, whose username is defined in the `.env`

Other activitypub supporting instances hit this endpoint when someone searches for the user from other instances, and the response to this will contain a pointer to the api which can be called to get the details about the user/actor.

Actor API just defines the public attributes of the users like name, bio, etc, along with a public key that will be used for federation verifications in the future.

### Testing

After starting the loophole, start the server - go to any federated site of your choice that you have account in, in my case hachyderm.io - which is a mastodon instance, and search for the user.
You should be able to view the account and other details

![Image search of the test user shown in mastodon instance](./docs/assets/webfinger.png)

## Tools

1. _fastapi_ as the server with python 3.9
2. [_loophole_](https://loophole.cloud/) for exposing my local server instance to other federated instances for testing (At this point just my Mastodon instance that I am on)

## Implementation logs

_2022-11-27 23:00 IST_

FastAPI hello world. Installed black for the formatting

_2022-11-28 02:00 IST_

Implemented basic actor endpoint and webfinger endpoint.
Now can search the user from other activitypub supporting
sites like Mastodon.

We serve a static user with username defined in .env
