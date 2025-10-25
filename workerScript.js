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