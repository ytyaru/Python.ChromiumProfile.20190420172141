#!/usr/bin/python3
#coding: utf8
import argparse
from ChromiumProfile import ChromiumProfile

def command_tsv(args):
    c = ChromiumProfile()
    print(c.Tsv)
def command_list(args):
    c = ChromiumProfile()
    if args.dirname: print(c.Dirnames)
    elif args.username: print(c.Usernames)
    else: parser_list.print_help()
def command_get(args):
    c = ChromiumProfile()
    if args.dirname: print(c.GetDirname(args.dirname))
    elif args.username: print(c.GetUsername(args.username))
    elif args.last_used: print(c.LastUsed)
    else: parser_get.print_help()

parser = argparse.ArgumentParser(description='Chromiumのプロファイル情報を取得する。')
subparsers = parser.add_subparsers()

parser_tsv = subparsers.add_parser('tsv', help='')
parser_list = subparsers.add_parser('list', help='')
parser_get = subparsers.add_parser('get', help='')

parser_tsv.set_defaults(handler=command_tsv)

parser_list.add_argument('-d', '--dirname', action='store_true', help='ディレクトリ名の一覧')
parser_list.add_argument('-u', '--username', action='store_true', help='ユーザ名の一覧')
parser_list.set_defaults(handler=command_list)

parser_get.add_argument('-d', '--dirname', help='ディレクトリ名（Profile 1 等）')
parser_get.add_argument('-u', '--username', help='ユーザ名（任意名）')
parser_get.add_argument('-l', '--last-used', action='store_true', help='最後に使用したユーザ名')
parser_get.set_defaults(handler=command_get)

args = parser.parse_args()
if hasattr(args, 'handler'): args.handler(args)
else: parser.print_help()

