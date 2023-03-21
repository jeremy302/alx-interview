#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  const movie = process.argv[2];

  request(`https://swapi-api.hbtn.io/api/films/${movie}/`,
    (e, r, b) => {
      e && console.log(e);

      const bd = JSON.parse(b);
      Promise.all(bd.characters.map(v => new Promise((resolve, reject) =>
        request(v, (e, r, b) => { e && reject(e); resolve(JSON.parse(b).name); }))))
        .then(arr => console.log(arr.join('\n'))).catch(e => console.log(e));
    });
}
