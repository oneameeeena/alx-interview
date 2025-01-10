#!/usr/bin/node

const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getData() {
        try {
                let data = await requestPromise('https://swapi-api.alx-tools.com/api/films/' + process.argv[2]);
                let dtBody = JSON.parse(data.body);

                for (let i in dtBody.characters)
                        request(dtBody.characters[i], (err, body, response) => {

                                console.log(JSON.parse(body.body).name);
                        });

        } catch (err) {
                console.log(err);
        }


}

getData();

