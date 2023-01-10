# Setup #
Create account with OpenAI and generate a key, store key locally as api_key.txt

## Build ##
<code>docker build -t <name> .</code>

## Run ##
<code>docker run -v "$(pwd)/api_key.txt:/run/secrets/api_key:ro" <name> <Question></code>
