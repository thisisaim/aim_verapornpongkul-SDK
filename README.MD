# Overview

This is a basic SDK for [The One API](https://the-one-api.dev). The API is an open-source API contains the following information about Lord of The Rings and The Hobbit; movies, books, quotes and characters information.

The purpose of this SDK is for the user to interact with the API in a pleasant manner without having to deal with the specifics of the API.

# Getting started

## First Step

Sign up [here](https://the-one-api.dev/sign-up](https://the-one-api.dev/sign-up) for a bearer token. Place it in the `api_key` field in the `config.yml` file.

## Compatibility

This project needs to use Python 3.10.5 or later to support

## Installation

In the terminal, run command:

> pip install av-lotr-sdk

## Logging

Logs are outputed to `sdk.log`

# Instructions on how to use SDK

```
import sys
import books as books
import chapters as chapters
import characters as characters
import movies as movies
import quotes as quotes

if __name__ == "__main__":
    print("App Started:")
    print(books.Book.get_all_books())
    print(chapters.Chapter.get_all_chapters())
    print(characters.Character.get_all_characters())
    print(movies.Movie.get_all_movies())
    print(quotes.Quote.get_all_quotes())


```

This should print all modules in a form of a list.

## Todos:

- Introduced dataclasses in `get_all` methods, need to expand it to all methods in SDK
- Sorting, Pagination and Filtering was not implemented due to time constraints.
