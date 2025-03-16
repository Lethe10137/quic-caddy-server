# quic-caddy-server

Describe your project here.

## Prepare

Instal caddy:

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install caddy
```

Prepare python:

``` bash
rye sync
```

Prepare cert and key:
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=California/L=San Francisco /O=Example Corp/OU=IT Department/CN=example.com"
```

## run server:

``` sh
python app.py &                             # Http service in port 5000
sudo caddy run --config ./Caddyfile        # Https service in port 59823
```


## Example client:

```bash
curl3 --http3 -k "https://<server ip>:59823/demo/upload" -F "uploadfile=@output.txt"
```