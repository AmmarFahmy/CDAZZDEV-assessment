import argparse
from huggingface_hub import login


def main():
    parser = argparse.ArgumentParser(
        description="Hugging Face CLI Login Script")
    parser.add_argument("--token", type=str,
                        help="Your Hugging Face access token.")
    args = parser.parse_args()

    # Prompt for token if not provided as an argument.
    if args.token is None:
        args.token = input("Enter your Hugging Face token: ").strip()

    if not args.token:
        print("Error: No token provided.")
        exit(1)

    # Log in using the provided token.
    login(token=args.token)
    print("Logged in successfully!")


if __name__ == '__main__':
    main()
