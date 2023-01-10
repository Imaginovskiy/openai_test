# Setup #
Create account with OpenAI and generate a key, store key locally as api_key.txt

## Build ##
<code>docker build -t $image_name .</code>

## Run ##
<code>docker run -v "$(pwd)/api_key.txt:/run/secrets/api_key:ro" $image_name $question</code>
