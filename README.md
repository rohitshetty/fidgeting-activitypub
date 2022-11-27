# Kicktire ActivityPub

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

A simple fastapi server that can be [webfingered](https://en.wikipedia.org/wiki/WebFinger) to find this account in other federated instances like Mastodon and then being able to post post content that would come up in the feed of federated instances (With probably being able to follow feature be a side effect)

## Tools

1. _fastapi_ as the server with python 3.9
2. [_loophole_](https://loophole.cloud/) for exposing my local server instance to other federated instances for testing (At this point just my Mastodon instance that I am on)

## Implementation logs
