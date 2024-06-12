// fetches and lists the title for all movies by using a URL used in the code
const listMoviesId = document.getElementById('list_movies');

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((res) => res.json())
  .then((data) => {
    for (let i = 0; i < data.results.length; i++) {
      const newFilm = document.createElement('li');
      newFilm.textContent = data.results[i].title;
      listMoviesId.appendChild(newFilm);
    }
  });
