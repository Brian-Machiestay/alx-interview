#!/usr/bin/node
// starwars api

const request = require('request');
const arg = process.argv[2]

async function ret_pro(url) {
  return new Promise(function(resolve, reject) {
    request(url, function(err, res, body) {
      resolve(JSON.parse(body).name);
    })
  })
}

async function chars() {
  return new Promise(function(resolve, reject) {
    request(`https://swapi-api.alx-tools.com/api/films/${arg}`,function(err, res, bod) {
      resolve(JSON.parse(bod).characters);
    })
  })
}

async function names() {
  thischars = await chars()
  for(let i = 0; i < thischars.length; i++) {
    console.log(await ret_pro(thischars[i]))
  }
}

names()
