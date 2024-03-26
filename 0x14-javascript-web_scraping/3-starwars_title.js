#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode number
 * matches a given integer.
    - the first argument is the movie ID.
    - use Star Wars API with the endpoint
    https://swapi-api.hbtn.io/api/films/:id
*/
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
