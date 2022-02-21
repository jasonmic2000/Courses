// axios.get('https://swapi.dev/api/planets/1/')
//   .then(res => {
//     console.log(res.data.name)
//   })
//   .catch(err => {
//     console.log('ERROR', err)
//   })

// const fetchPlanetName = async () => {
//   try {
//     const res = await axios.get('https://swapi.dev/api/planets/1/')
//     console.log(res.data.name)
//   } catch (e) {
//     console.log('ERROR', e)
//   }
// }

const jokes = document.querySelector('#jokes')
const button = document.querySelector('button')

const addNewJoke = async () => {
  const jokeText = await getDadJoke()
  const newLI = document.createElement('LI')
  newLI.append(jokeText)
  jokes.append(newLI)
}
button.addEventListener('click', addNewJoke)


const getDadJoke = async () => {
  try {
    const config = {headers: { Accept: 'application/json' } }
    const res = await axios.get('https://icanhazdadjoke.com', config)
    return res.data.joke
  } catch (e) {
    return 'No Jokes available!'
  }
}