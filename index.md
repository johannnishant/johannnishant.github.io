---
title: Cloudflare Technical Project - Johann Nishant
---

Really fun to work with this, it gave me a good intro into Cloudflare's Services!

# Essentials about the Deliverables

## 1. Application
- **Python Based running on EC2**
    - Business Logic
        - Return all HTTP Request Headers in Response
    - Hosted on [https://tunnel.jnishant.com/](https://tunnel.jnishant.com/)
    - **Protected via Cloudflare Tunnel**
        - TLS 1.2 or above

## 2. API to output all jnishant.com DNS Records

#### Scope
- jnishant.com - DNS:Read
- TTL End Date - November 8, 2025

#### API Call
```bash
curl "https://api.cloudflare.com/client/v4/zones/cdf864e305f40da949f4d33ca9a02337/dns_records" \
-H "Authorization: Bearer yxRS1r4xa3Zvy4_3e_9ZYKZ0WvUDlH1afa7neeR2"
```

#### Output
```json
{"result":[{"id":"54ac0bc23e37dd934ec9c5bd4fd074e2","name":"jnishant.com","type":"A","content":"51.20.218.59","proxiable":true,"proxied":true,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.17977Z","modified_on":"2025-10-25T12:48:34.17977Z"},{"id":"bd4e36afe67d8d41382796875dbc2581","name":"_domainconnect.jnishant.com","type":"CNAME","content":"_domainconnect.gd.domaincontrol.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.190907Z","modified_on":"2025-10-25T12:48:34.190907Z"},{"id":"be377fd7419ca096e0f64e5b9cf8634f","name":"email.jnishant.com","type":"CNAME","content":"email.secureserver.net","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.221688Z","modified_on":"2025-10-25T12:48:34.221688Z"},{"id":"58ec0550fdd0a4bcd700a681bb8b7d11","name":"ftp.jnishant.com","type":"CNAME","content":"jnishant.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.232857Z","modified_on":"2025-10-25T12:48:34.232857Z"},{"id":"5af78b5f27a676fbaa62689ef667d840","name":"tunnel.jnishant.com","type":"CNAME","content":"05819d54-4201-4c60-acc4-562920b9c7e6.cfargotunnel.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T15:13:19.706218Z","modified_on":"2025-10-25T15:13:19.706218Z"},{"id":"433db488004eb11985015dc0e0ed9173","name":"www.jnishant.com","type":"CNAME","content":"jnishant.com","proxiable":true,"proxied":true,"ttl":1,"settings":{"flatten_cname":false},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.168054Z","modified_on":"2025-10-25T12:48:34.168054Z"},{"id":"1090beac1d20c53324e79b9095cdf7c3","name":"jnishant.com","type":"MX","content":"smtp.secureserver.net","priority":0,"proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.212181Z","modified_on":"2025-10-25T12:48:34.212181Z"},{"id":"fee37fca548943f30580e4735d58c5da","name":"jnishant.com","type":"MX","content":"mailstore1.secureserver.net","priority":10,"proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.20294Z","modified_on":"2025-10-25T12:48:34.20294Z"},{"id":"6eee0785f8096619f86a2d1d6512fc3e","name":"jnishant.com","type":"NS","content":"ns22.domaincontrol.com","proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.252354Z","modified_on":"2025-10-25T12:48:34.252354Z"},{"id":"152896d413a57a4c9b60ec190eef39db","name":"jnishant.com","type":"NS","content":"ns21.domaincontrol.com","proxiable":false,"proxied":false,"ttl":1,"settings":{},"meta":{},"comment":null,"tags":[],"created_on":"2025-10-25T12:48:34.244287Z","modified_on":"2025-10-25T12:48:34.244287Z"}],"success":true,"errors":[],"messages":[],"result_info":{"page":1,"per_page":100,"count":10,"total_count":10,"total_pages":1}}
```

## 3. Cloudflare Worker for redirection
#### Fixed Worked Code
Implemented as a Worker on [https://tunnel.jnishant.com/](https://tunnel.jnishant.com/) route
```
addEventListener("fetch", event => {
    event.respondWith(doRedirects(event.request))
  })
  
  const newLocationHost = "developers.cloudflare.com";
  const newLocationPath = "/workers/about/";
  
  async function doRedirects(request) {

    let reqUA = request.headers.get('user-agent');
    
    const cookies = request.headers.get('cookie') || '';
    const hasBypassCookie = cookies.includes('cf-noredir=true');
    
    if (hasBypassCookie) {
      return fetch(request);
    }
    
    if (reqUA && reqUA.toLowerCase().includes('curl')) {
      let newLocation = "https://" + newLocationHost + newLocationPath;
      return Response.redirect(newLocation, 302);
    }
    
    return fetch(request);
  }
```

## 4. jnishant.com/secure locked down only for a particular Group
- Access to [jnishant.com/secure](https://jnishant.com/secure) is secured via One Time Pin


# Report 

## Solution Architecture

<div style="text-align: center;">
<img src="assets/images/arch.png" alt="System Architecture Diagram" style="width: 120%; min-width: 1440px; height: auto; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</div>

### Implementation Summary 
* Used my Personal Website, Onboarded DNS to Cloudflare, Secured Client <-> Cloudflare <-> Personal Website Communication with >= TLS 1.2, Full Strict 
* Implemented a simple Python Server running on my personal AWS account
* Installed the cloudflare Daemon 
* Some ClickOps in the Dashboard to get the Tunnel up & running (Can be optimized with IaC)
* Read Cloudflare API, Access Token Concept, Crafted DNS API with specific Scope 
* Implemented Worked, Fixed Code, added bonus logic, Tested with some examples 
* Added a Cloudflare Application for jnishant.com/secure, used One Time Pin for simplicitity (Can be optimized later for more robust authentication)


### Learnings 

Yes, I learnd a lot, More than just tech, also could understand Cloudflare's business model a bit more and why they have particular services
I filled in the gaps by reading docs, googling, checking with LLMs 

### Experience with Tunnels & Cloudflare Workers 
* Quite straightforward to use, Cloudflare workers seems really nice 
* Cloudflare Tunnel helps securely connect systems without directly exposing internal applications 
Usecases: Replacing traditional VPNs 
* Cloudflare Workers helps build more intelligence at the edge 
Usecases: Many, but some could Low-Latency use-cases 


### Would HTTP response headers be different if you were not using Cloudflare?
Yes, for sure, got the below for the Application about using Cloudflare, alot of Cf-* headers
```json
{
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, br",
        "Cdn-Loop": "cloudflare; loops=1; subreqs=1",
        "Cf-Connecting-Ip": "90.231.106.253",
        "Cf-Ew-Via": "15",
        "Cf-Ipcountry": "SE",
        "Cf-Ray": "99431ccc0298abe0-CPH",
        "Cf-Visitor": "{\"scheme\":\"https\"}",
        "Cf-Warp-Tag-Id": "dae16bf1-75af-4cd6-8cd6-fde2b42826e1",
        "Cf-Worker": "jnishant.com",
        "Connection": "keep-alive",
        "Host": "tunnel.jnishant.com",
        "Postman-Token": "46d21b28-e6a3-4417-a7fa-e1c5f4e7b60a",
        "User-Agent": "PostmanRuntime/7.49.0",
        "X-Forwarded-For": "90.231.106.253",
        "X-Forwarded-Proto": "https"
    },
    "method": "GET",
    "remote_addr": "127.0.0.1",
    "timestamp": "Not available",
    "url": "https://tunnel.jnishant.com/",
    "user_agent": "PostmanRuntime/7.49.0"
}
```

## How a Customer will find this experience 
- Straightforward, Well Documented

### Some Opportunities for improvements
- Not sure why there is 2 Domains - the main dashboard and for for Zero Trust (Unifying would be good in the future)
- Free Tier in Zero Trust Requires Credit Card Details
