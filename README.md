# Web Scraping API

<p align="center">
<a href="https://dashboard.decodo.com/?page=residential-proxies&utm_source=socialorganic&utm_medium=social&utm_campaign=resi_trial_GITHUB"><img src="https://github.com/user-attachments/assets/60bb48bd-8dcc-48b2-82c9-a218e1e4449c"></a>
</p>


[![](https://dcbadge.vercel.app/api/server/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)

## List of contents
- [Introduction](#introduction)
- [Authentication](#authentication)
- [Scraping](#scraping)
- [Headless](#headless)
- [Facebook](#facebook)
- [Parameters](#parameters)
- [Response Codes](#response-codes)
- [License](#license)

## Introduction

With [our Web Scraping API](https://decodo.com/scraping/web), you can scrape various websites en masse.

## Authentication

Once you have an active Web Scraping API subscription, you can try sending a request right from the dashboard Web Scraping API > Authentication method tab simply by entering your username, password, and clicking on Generate. You will also see an example of curl request generated right below your entered ``` user:pass. ``` 

Note that this is only an example with preset values to get you on the right track for forming your own request, meaning you will not be able to change the request values in the dashboard itself – that will have to be done in your code.


## Scraping

### You can use universal parameter as your target and supply any URL you want, which will return the HTML of the targeted URL.

API Link: https://scraper-api.decodo.com/v2/scrape

```http
  POST /scrape
```

### Target: ```universal``` (not parseable)
Required parameters: ```url``` (ip.decodo.com in this example)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Target URL |
| `target` | `string` | Scraping target - ```universal``` |

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/ipdecodo.py](https://github.com/Decodo/Web-Scraping-API/blob/main/python/ipDecodo.py) |``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/python/ipdecodo.py > ipdecodo.py ``` |
| PHP                 | [php/ipdecodo.php](https://github.com/Decodo/Web-Scraping-API/blob/main/php/ipDecodo.php)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/php/ipdecodo.php > ipdecodo.php ``` |
| Node.js                 | [nodejs/ipdecodo.js](https://github.com/Decodo/Web-Scraping-API/blob/main/nodejs/ipDecodo.js)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/nodejs/ipdecodo.js > ipdecodo.js ``` |


### Response

```http
{
  "results": [
    {
      "content": "Your Ip is: 213.87.163.6",
      "status_code": 200,
      "url": "https://ip.decodo.com/",
      "task_id": "6971034977135771649",
      "created_at": "2022-09-01 09:24:14",
      "updated_at": "2022-09-01 09:24:17"
    }
  ]
}
```

## Headless

**Not seeing the results you wanted?**

Try enabling JavaScript rendering using the ```headless``` parameter. - [Parameters](#parameters)

This parameter renders JavaScript on the target website making more data available for scraping. 


## Facebook

### Facebook Page 

### Target: ```universal``` (not parseable)
Required parameters: ```url``` 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Target URL |
| `target` | `string` | Scraping target - ```universal``` |

### Response

```http

{
  "results": [
    {
      "content": "<html> Facebook page content</html>"
      "status_code": 200,
      "url": "https://www.facebook.com/ladygaga",
      "task_id": "6972452679540839425",
      "created_at": "2022-09-05 07:17:40",
      "updated_at": "2022-09-05 07:17:45"
    }
  ]
}
```
### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/facebookpage.py](https://github.com/Decodo/Web-Scraping-API/blob/main/python/facebookpage.py) |``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/python/facebookpage.py > facebookpage.py ``` |
| PHP                 | [php/facebookpage.php](https://github.com/Decodo/Web-Scraping-API/blob/main/php/facebookpage.php)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/php/facebookpage.php > facebookpage.php ``` |
| Node.js                 | [nodejs/facebookpage.js](https://github.com/Decodo/Web-Scraping-API/blob/main/nodejs/facebookpage.js)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/nodejs/facebookpage.js > facebookpage.js ``` |


### Facebook Post

### Target: ```universal``` (not parseable)
Required parameters: ```url``` 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Target URL |
| `target` | `string` | Scraping target - ```universal``` |
| `headless` | `string` | Javascript rendering - ```html``` |

### Response


```http
{
  "results": [
    {
      "content": "<html> Facebook page content</html>"
      "status_code": 200,
      "url": "https://www.facebook.com/zuck/posts/pfbid0HeY54v4LMcv2EMxDz5RvnWaR6swsGFWikzUbrsEFtvxu9n4GCx7zA2YTM69XdiYnl",
      "task_id": "6972484278999372801",
      "created_at": "2022-09-05 09:23:14",
      "updated_at": "2022-09-05 09:23:32"
    }
  ]
}
```

### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/facebookpost.py](https://github.com/Decodo/Web-Scraping-API/blob/main/python/facebookpost.py) |``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/python/facebookpost.py > facebookpost.py ``` |
| PHP                 | [php/facebookpost.php](https://github.com/Decodo/Web-Scraping-API/blob/main/php/facebookpost.php)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/php/facebookpost.php > facebookpost.php ``` |
| Node.js                 | [nodejs/facebookpost.js](https://github.com/Decodo/Web-Scraping-API/blob/main/nodejs/facebookpost.js)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/nodejs/facebookpost.js > facebookpost.js ``` |


### Facebook Group

### Target: ```universal``` (not parseable)
Required parameters: ```url``` 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url` | `url` |  Target URL |
| `target` | `string` | Scraping target - ```universal``` |

### Response

```http
{
  "results": [
    {
      "content": "<html> Facebook page content</html>"
      "status_code": 200,
      "url": "https://www.facebook.com/groups/1394454774138066",
      "task_id": "6972486765374350337",
      "created_at": "2022-09-05 09:33:07",
      "updated_at": "2022-09-05 09:33:33"
    }
  ]
}
```
### Examples

| Programming Language | Example location         | Download |
| -------------------- | ------------------------ | -------- |
| Python                  | [python/facebookgroup.py](https://github.com/Decodo/Web-Scraping-API/blob/main/python/facebookgroup.py) |``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/python/facebookgroup.py > facebookgroup.py ``` |
| PHP                 | [php/facebookgroup.php](https://github.com/Decodo/Web-Scraping-API/blob/main/php/facebookgroup.php)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/php/facebookgroup.php > facebookgroup.php ``` |
| Node.js                 | [nodejs/facebookgroup.js](https://github.com/Decodo/Web-Scraping-API/blob/main/nodejs/facebookgroup.js)   | ``` curl https://raw.githubusercontent.com/Decodo/Web-Scraping-API/main/nodejs/facebookgroup.js > facebookgroup.js ``` |

## Parameters

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `target` | `string` |  Data source. (universal) |
| `url` | `url` | Direct URL (link) |
| `locale` | `string` | This will change the web interface language. Example: – en-US – en-GB |
| `geo` | `string` | The geographical location that the result depends on. Full Country names required |
| `device_type` | `string` | Device type and browser. Supported: ```desktop```, ```desktop_chrome```, ```desktop_firefox```, ```mobile```, ```mobile_android```, ```mobile_ios```. |
| `headless` | `string` | Enable JavaScript rendering. Supported: ```html```, ```png``` |

## Response Codes

### HTTP Response Codes

| Response | Description     | Solution                |
| :-------- | :------- | :------------------------- |
| **200** - Success | Server has replied and given requested response.	 | Celebrate! |
| **204** - No content | Job not completed yet. | Wait a few seconds before trying again. |
| **400** - Multiple error messages | Bad structure of the request. | Re-check your request to make sure it is in the correct format. |
| **401** - Invalid / not provided authorization header (client not found) | Incorrect login credentials or missing authorization. | Re-check your provided credentials for authorization. |
| **403** - Forbidden | Your account does not have access to this resource. | Make sure the target is supported by us |
| **404** - Not found | Your target was not found. | Re-check your targeted URL. |
| **429** - Too many requests | Exceeded rate limit for your subscription. | Make sure you still have at least one request left. Wait a couple minutes and try again. If you are encountering the error often – chat with us to see if your rate limit can be increased. |
| **500** - Internal error | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |
| **524** - Timeout | Service unavailable, possibly due to some issues we are encountering. | Wait a couple minutes and send another request. Contact us for more information. |

## License


All code is released under [MIT License](https://github.com/Decodo/Decodo/blob/master/LICENSE)
