#!/usr/bin/node
// fetch starwars API

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request(API_URL + movieId, function (err, res, body) {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  fetchChar(chars, 0);
});

const fetchChar = (chars, idx) => {
  if (idx === chars.length) return;
  request(chars[idx], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    fetchChar(chars, idx + 1);
  });
};
