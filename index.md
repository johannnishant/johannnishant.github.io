

# Cloudflare Technical Project - Johann Nishant

  

Really fun to work with this, it gave me a good intro into Cloudflare's Services!

  

# Essentials about the Deliverables

 1. **Application**
	 - Python Based running on EC2
	      - Business Logic
		      - Return all HTTP Request Headers in Response
		   - Hosted on https://tunnel.jnishant.com/
	 - Protected via Cloudflare Tunnel
		 - TLS 1.2 or above

 2. **API to output all jnishant.com DNS Records**

```console

#Scope

jnishant.com - DNS:Read

TTL End Date - November 8, 2025

#API Call

curl "https://api.cloudflare.com/client/v4/zones/cdf864e305f40da949f4d33ca9a02337/dns_records" \

-H "Authorization: Bearer yxRS1r4xa3Zvy4_3e_9ZYKZ0WvUDlH1afa7neeR2"
  
#Output

{"result":[{"id":"54ac0bc23e37dd934ec9c5bd4fd074e2","name":"jnishant.com","type":"A","content":"51.20.218.59","proxiable":true,"proxied":true,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.17977Z","modified_on":"2025-10-25T12:48:34.17977Z"},{"id":"bd4e36afe67d8d41382796875dbc2581","name":"_domainconnect.jnishant.com","type":"CNAME","content":"_domainconnect.gd.domaincontrol.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.190907Z","modified_on":"2025-10-25T12:48:34.190907Z"},{"id":"be377fd7419ca096e0f64e5b9cf8634f","name":"email.jnishant.com","type":"CNAME","content":"email.secureserver.net","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.221688Z","modified_on":"2025-10-25T12:48:34.221688Z"},{"id":"58ec0550fdd0a4bcd700a681bb8b7d11","name":"ftp.jnishant.com","type":"CNAME","content":"jnishant.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.232857Z","modified_on":"2025-10-25T12:48:34.232857Z"},{"id":"5af78b5f27a676fbaa62689ef667d840","name":"tunnel.jnishant.com","type":"CNAME","content":"05819d54-4201-4c60-acc4-562920b9c7e6.cfargotunnel.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T15:13:19.706218Z","modified_on":"2025-10-25T15:13:19.706218Z"},{"id":"433db488004eb11985015dc0e0ed9173","name":"www.jnishant.com","type":"CNAME","content":"jnishant.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.168054Z","modified_on":"2025-10-25T12:48:34.168054Z"},{"id":"1090beac1d20c53324e79b9095cdf7c3","name":"jnishant.com","type":"MX","content":"smtp.secureserver.net","priority":0,"proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.212181Z","modified_on":"2025-10-25T12:48:34.212181Z"},{"id":"fee37fca548943f30580e4735d58c5da","name":"jnishant.com","type":"MX","content":"mailstore1.secureserver.net","priority":10,"proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.20294Z","modified_on":"2025-10-25T12:48:34.20294Z"},{"id":"6eee0785f8096619f86a2d1d6512fc3e","name":"jnishant.com","type":"NS","content":"ns22.domaincontrol.com","proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.252354Z","modified_on":"2025-10-25T12:48:34.252354Z"},{"id":"152896d413a57a4c9b60ec190eef39db","name":"jnishant.com","type":"NS","content":"ns21.domaincontrol.com","proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.244287Z","modified_on":"2025-10-25T12:48:34.244287Z"}],"success":true,"errors":[],"messages":[],"result_info":{"page":1,"per_page":100,"count":10,"total_count":10,"total_pages":1}}%

```

3. **Cloudflare Worker for redirrection**

  

5. jnishant.com/secure locked down only for a particular Group

  

  
  
  

Not so nices

- Argo Tunnel no longer exists (called Cloudflare Tunnel now)

- Free Tier in Zero Trust Require Credit Card Details

- No Native Ubuntu in Tunnel Setup

  
  
  

Cleanup After Interview (Instructions for Johann)

- Remove Cloudflared Daemon

  
  
  

