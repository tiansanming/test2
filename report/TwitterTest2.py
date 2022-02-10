import twint

def main():
    # Configure
    c = twint.Config()
    c.Username = "elonmusk"
    c.Proxy_host = '127.0.0.1'
    c.Proxy_port = '7890'
    c.Proxy_type = 'socks5'
    # Run
    twint.run.Search(c)


if __name__ == "__main__":
    main()