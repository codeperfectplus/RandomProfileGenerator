from .main import RandomProfile
import argparse


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

    args = parser.parse_args()

    rp = RandomProfile(args.n)
    if args.fullname:
        print(*rp.full_name(), sep="\n")
    elif args.profile:
        print(*rp.full_profile(), sep="\n")
    elif args.lastname:
        print(*rp.last_name(), sep="\n")
    else:
        print(*rp.first_name())


if __name__ == "__main__":
    main()
