The original header was using the RS256 algorithm  but we changed it to use HS256. Next we changed our username to ad,im and signed the roken using the servers public key. When this is ent to the server it will use the HS26 
algorithm to verify the tone instead of RS256. 
Since the backend code was set up to use a public/private key, the public key will be used during the verification process and our token will pass. 
