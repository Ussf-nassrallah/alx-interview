#!/usr/bin/node
// fetch starwars API

const request = require('request');
const api_url = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request(api_url + movieId, function (err, res, body) {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  exactOrder(chars, 0);
});
const exactOrder = (chars, idx) => {
  if (idx === chars.length) return;
  request(chars[idx], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(chars, idx + 1);
  });
};