#!/usr/bin/node
// fetch starwars API

const request = require('request');
const movieId = process.argv[2];
const API_URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchChar = (url) => {
  request(url, (err, res, body) => {
    if (err) {
      console.log('fetchChar error: ' + err);
    } else if (res.statusCode !== 200) {
      console.log(`error! status: ${res.statusCode}`);
    } else {
      const char = JSON.parse(body);
      console.log(char.name);
    }
  });
};

const fetchFilmChars = (url) => {
  request(url, (error, res, body) => {
    if (error) {
      console.log(error);
    } else if (res.statusCode !== 200) {
      console.log(`error! status: ${res.statusCode}`);
    } else {
      const data = JSON.parse(body);
      const chars = data.characters;

      for (const charIdx in chars) {
        fetchChar(chars[charIdx]);
      }
    }
  });
};

fetchFilmChars(API_URL);
