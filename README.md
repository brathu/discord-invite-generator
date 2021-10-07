# Discord invite generator

Discord invite generator is a simple Python script to generate discord bot invite links.

## Installation

Just download it or copy and paste the code in a new python file and safe it.

## Usage
You can use arguments to create a invite link like this:
```bash
py gen.py APPLICATION_ID PERMS
```
Example:
```bash
py gen.py 458276816071950337 8
```
Output:
```bash
https://discord.com/oauth2/authorize?client_id=458276816071950337&permissions=8&scope=bot
```
You just run the script without args too.

## Perms
List of all perms: https://discord.com/developers/docs/topics/permissions#permissions-bitwise-permission-flags
