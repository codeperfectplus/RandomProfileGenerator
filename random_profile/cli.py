from random_profile.main import RandomProfile
import argparse
from pprint import pprint


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Number of random profiles", type=int, default=1)

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f",
        "--fullname",
        help="Get full name instead of first name",
        action="store_true",
    )
    group.add_argument(
        "-p",
        "--profile",
        help="Get full profile instead of first name",
        action="store_true",
    )
    group.add_argument(
        "-l",
        "--lastname",
        help="Get last name instead of first name",
        action="store_true",
    )
    group.add_argument(
        "-ip",
        "--ipv4",
        help="Get an ipv4 IP address",
        action="store_true",
    )
    group.add_argument(
        "-j",
        "--jobtitle",
        help="Get job title",
        action="store_true",
    )

    args = parser.parse_args()

    rp = RandomProfile(args.n)
    if args.fullname:
        pprint(rp.full_name())
    elif args.profile:
        pprint(rp.full_profile())
    elif args.lastname:
        pprint(rp.last_name())
    elif args.jobtitle:
        pprint(rp.job_title())
    elif args.ipv4:
        pprint(rp.ipv4())
    else:
        pprint('Type `random_profile -h` for help')


if __name__ == "__main__":
    main()
