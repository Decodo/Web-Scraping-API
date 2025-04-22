const request = require('request');

const username = 'YOUR_USERNAME';
const password = 'YOUR_PASSWORD';

const options = {
  method: 'POST',
  url: 'https://scraper-api.decodo.com/v2/scrape',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + Buffer.from(username + ':' + password).toString('base64')
  },
  body: JSON.stringify({
    target: 'universal',
    parse: false,
    url: 'https://www.facebook.com/groups/1394454774138066'
  })
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
