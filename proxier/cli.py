from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from proxier.config import Urls
from proxier.func import save


def register_parser(subparser, name: str, url: str):
    parser = subparser.add_parser(name, help=f'Download {name} proxy')
    parser.set_defaults(name=name)
    parser.set_defaults(url=url)


def parse_args():
    default = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    subparsers = default.add_subparsers()
    register_parser(subparsers, 'http', Urls.HTTP.value)
    register_parser(subparsers, 'socks4', Urls.SOCKS4.value)
    register_parser(subparsers, 'socks5', Urls.SOCKS5.value)

    return default.parse_args()


def main():
    args = parse_args()
    save(args.name, args.url)


if __name__ == '__main__':
    main()
