<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://scraper-api.decodo.com/v2/scrape', [
  'body' => '{"target":"universal","parse":false,"url":"https://www.facebook.com/ladygaga"}',
  'headers' => [
    'Accept' => 'application/json',
    'Authorization' => 'Basic AUTH',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
