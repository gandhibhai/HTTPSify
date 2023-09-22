import argparse

def add_https_to_urls(input_file, output_file):
    try:
        with open(input_file, 'r') as input_file:
            urls = input_file.readlines()

        with open(output_file, 'w') as output_file:
            for url in urls:
                url = url.strip()
                if not url.startswith('http://') and not url.startswith('https://'):
                    url = 'https://' + url
                output_file.write(url + '\n')

        print(f"HTTPS added to URLs and saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add 'https://' prefix to URLs in a wordlist file.")
    parser.add_argument("-l", "--list", help="Input wordlist file containing URLs", required=True)
    args = parser.parse_args()

    input_file = args.list
    output_file = "output.txt"  # Replace with your desired output file name
    add_https_to_urls(input_file, output_file)
