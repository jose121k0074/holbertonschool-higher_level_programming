// fetches the character name from this URL:

const characterIdElement = document.getElementById('character');

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
let name;

fetch(url)
  .then((res) => res.json())
  .then((data) => { characterIdElement.textContent = data.name })
