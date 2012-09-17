from sys import argv
import config
import custom_gearman as gearman


client = gearman.GearmanClient(config.GEARMAN_HOSTS)


def main():
    # Take arguments
    if len(argv) < 2:
        raise Exception("Requires at least one url. Use `client help` for more info.")
    urls = argv[1:]
    if 'help' in urls:
        print """Screenshotter:
You enter multiple urls separated by spaces.

eg.
client http://www.jpanganiban.com/ http://www.plurk.com/ http://www.google.com/
        """
        return 0
    # TODO: Validate url
    responses = []
    for url in urls:
        response = client.submit_job('screenshot', {'url': url})
        responses.append(response)
    return 0


if __name__ == '__main__':
    main()
